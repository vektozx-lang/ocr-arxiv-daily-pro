#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import html
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import json

import litellm
import yaml

# ==================== 配置加载 ====================
CONFIG_PATH = Path("config.yaml")
if CONFIG_PATH.exists():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        CONFIG = yaml.safe_load(f)
else:
    CONFIG = {"llm": {"provider": "deepseek", "model": "deepseek-chat", "api_key_env": "DEEPSEEK_API_KEY"}}

def call_llm(prompt: str, temperature: float = 0.7) -> str:
    """最终生产版 LLM 调用"""
    model = "deepseek/deepseek-chat"
    api_key = os.getenv(CONFIG["llm"].get("api_key_env", "DEEPSEEK_API_KEY"))
    try:
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=CONFIG["llm"].get("max_tokens", 4096),
            api_key=api_key,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM 调用失败: {e}")
        return f"LLM 调用失败: {str(e)[:150]}"

# ==================== arXiv 配置 ====================
ARXIV_API = "http://export.arxiv.org/api/query"
DEFAULT_TERMS = [
    '"document parsing"', '"document understanding"', '"optical character recognition"',
    'OCR', '"layout analysis"', '"document layout analysis"', '"text recognition"',
    '"table recognition"', '"form understanding"', '"document intelligence"',
    '"page understanding"', '"scene text recognition"', '"handwritten text recognition"',
    '"information extraction"',
]
DEFAULT_CATEGORIES = ["cs.CV", "cs.AI", "cs.CL", "eess.IV"]

KEYWORD_WEIGHTS = [
    ("ocr", 6), ("optical character recognition", 7), ("text recognition", 5),
    ("scene text", 4), ("document", 4), ("layout", 4), ("table", 3),
    ("form", 3), ("parsing", 5), ("document intelligence", 5),
]

NEGATIVE_WEIGHTS = [
    ("speech recognition", -7), ("audio", -4), ("asr", -7),
]

@dataclass
class Paper:
    title: str
    summary: str
    link: str
    pdf_url: str
    authors: list[str]
    published: str
    updated: str
    categories: list[str]
    arxiv_id: str
    score: int = 0
    zh_summary: str | None = None
    innovation_points: list[str] | None = None
    limitations: str | None = None
    improvement_directions: list[str] | None = None
    engineering_value: str | None = None

# ==================== 工具函数 ====================
def normalize_text(text: str) -> str:
    text = html.unescape(text or "")
    return re.sub(r"\s+", " ", text).strip()

def score_paper(title: str, summary: str, categories: Iterable[str]) -> int:
    text = f"{title} {summary} {' '.join(categories)}".lower()
    score = 0
    for key, weight in KEYWORD_WEIGHTS:
        if key in text:
            score += weight
    for key, weight in NEGATIVE_WEIGHTS:
        if key in text:
            score += weight
    return score

def build_query(terms: list[str], categories: list[str]) -> str:
    term_query = " OR ".join(f"all:{t}" for t in terms)
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    return f"({term_query}) AND ({cat_query})"

def fetch_arxiv(query: str, max_results: int) -> list[Paper]:
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ocr-arxiv-daily-pro/2.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        root = ET.fromstring(resp.read())
    entries = root.findall("atom:entry", {"atom": "http://www.w3.org/2005/Atom"})
    papers: list[Paper] = []
    for entry in entries:
        title = normalize_text(entry.findtext("atom:title", default="", namespaces={"atom": "http://www.w3.org/2005/Atom"}))
        summary = normalize_text(entry.findtext("atom:summary", default="", namespaces={"atom": "http://www.w3.org/2005/Atom"}))
        published = normalize_text(entry.findtext("atom:published", default="", namespaces={"atom": "http://www.w3.org/2005/Atom"}))
        authors = [normalize_text(a.findtext("atom:name", default="", namespaces={"atom": "http://www.w3.org/2005/Atom"})) for a in entry.findall("atom:author", {"atom": "http://www.w3.org/2005/Atom"})]
        categories = [c.attrib.get("term", "") for c in entry.findall("atom:category", {"atom": "http://www.w3.org/2005/Atom"})]
        link = pdf_url = ""
        for link_node in entry.findall("atom:link", {"atom": "http://www.w3.org/2005/Atom"}):
            href = link_node.attrib.get("href", "")
            if link_node.attrib.get("rel") == "alternate":
                link = href
            if link_node.attrib.get("title") == "pdf":
                pdf_url = href
        arxiv_id = normalize_text(entry.findtext("atom:id", default="", namespaces={"atom": "http://www.w3.org/2005/Atom"})).rsplit("/", 1)[-1]
        papers.append(Paper(
            title=title, summary=summary, link=link, pdf_url=pdf_url,
            authors=authors, published=published, updated=published,
            categories=categories, arxiv_id=arxiv_id,
            score=score_paper(title, summary, categories)
        ))
    return papers

def dedup_papers(papers: list[Paper]) -> list[Paper]:
    seen = set()
    result = []
    for p in papers:
        key = re.sub(r"\W+", "", p.title.lower())
        if key in seen:
            continue
        seen.add(key)
        result.append(p)
    return result

def filter_recent(papers: list[Paper], days_back: int) -> list[Paper]:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days_back)
    return [p for p in papers if dt.datetime.fromisoformat(p.published.replace("Z", "+00:00")) >= cutoff]

def llm_relevance_score(paper: Paper) -> int:
    prompt = f"""严格只返回一个整数（1-10），不要任何解释：
标题：{paper.title}
摘要：{paper.summary[:1200]}
与 OCR / 文档解析 / 版面分析 / 表格识别 / 文档理解 领域的相关度是多少？"""
    try:
        score_str = call_llm(prompt, temperature=0.0)
        score = int(re.search(r'\d+', score_str).group())
        return max(1, min(10, score))
    except:
        return paper.score // 2

def generate_single_paper_analysis(paper: Paper) -> Paper:
    prompt = f"""请用中文详细分析这篇 OCR/文档解析论文（严格按以下格式输出）：

标题：{paper.title}
摘要：{paper.summary}

输出格式（Markdown）：
### 中文摘要
...
### 核心创新
...
### 创新点拆解
- ...
### 当前局限
...
### 后续改进方向
- ...
### 工程启发
..."""
    analysis = call_llm(prompt, temperature=0.7)
    paper.zh_summary = analysis
    return paper

def generate_daily_synthesis(papers: list[Paper]) -> str:
    titles = "\n".join([f"- {p.title}" for p in papers])
    prompt = f"""今天共有 {len(papers)} 篇 OCR/文档解析高相关论文，标题如下：
{titles}

生成专业的中文日报总结（严格按以下格式）：
### 今日执行摘要
...
### 今日趋势判断
...
### 主要创新点
...
### 值得推进的改进方向
...
### 工程落地启发
...
### 优先关注论文列表
..."""
    return call_llm(prompt, temperature=0.7)

def build_markdown_report(papers: list[Paper], synthesis: str, today: str) -> str:
    """将分析结果拼装成完整 Markdown 报告"""
    lines = []
    lines.append(f"# OCR arXiv Daily Pro — {today}\n")
    lines.append(f"> 自动生成，共收录 **{len(papers)}** 篇高相关论文\n")
    lines.append("---\n")
    lines.append("## 📊 今日综合分析\n")
    lines.append(synthesis)
    lines.append("\n---\n")
    lines.append("## 📄 论文详情\n")
    for i, p in enumerate(papers, 1):
        authors_str = ", ".join(p.authors[:5]) + ("..." if len(p.authors) > 5 else "")
        lines.append(f"### {i}. {p.title}\n")
        lines.append(f"- **ArXiv ID**: [{p.arxiv_id}]({p.link})")
        lines.append(f"- **作者**: {authors_str}")
        lines.append(f"- **发布时间**: {p.published[:10]}")
        lines.append(f"- **分类**: {', '.join(p.categories[:3])}")
        lines.append(f"- **PDF**: [{p.pdf_url}]({p.pdf_url})\n")
        lines.append("#### 英文摘要\n")
        lines.append(f"{p.summary}\n")
        if p.zh_summary:
            lines.append("#### 深度分析（中文）\n")
            lines.append(p.zh_summary)
        lines.append("\n---\n")
    return "\n".join(lines)


def main():
    print("🚀 OCR arXiv Daily Pro v2.0 最终生产版启动...")
    query = build_query(DEFAULT_TERMS, DEFAULT_CATEGORIES)
    papers = fetch_arxiv(query, CONFIG["arxiv"].get("max_results", 200))
    papers = dedup_papers(papers)
    papers = filter_recent(papers, CONFIG["arxiv"].get("days_back", 14))

    print(f"✅ 抓取到 {len(papers)} 篇论文（最近 {CONFIG['arxiv'].get('days_back')} 天）")

    print("🔍 LLM 智能二次相关性打分...")
    for p in papers:
        p.score = llm_relevance_score(p)

    top_papers = sorted(papers, key=lambda p: p.score, reverse=True)[:CONFIG["arxiv"].get("final_limit", 15)]

    print(f"📊 最终选中 {len(top_papers)} 篇高相关论文")

    for i, paper in enumerate(top_papers, 1):
        print(f"[{i}/{len(top_papers)}] 深度分析：{paper.title[:60]}...")
        top_papers[i - 1] = generate_single_paper_analysis(paper)

    synthesis = generate_daily_synthesis(top_papers)

    # ==================== 写出文件 ====================
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path("output")
    archive_dir = out_dir / "archive"
    out_dir.mkdir(parents=True, exist_ok=True)
    archive_dir.mkdir(parents=True, exist_ok=True)

    report_md = build_markdown_report(top_papers, synthesis, today)

    # LATEST.md —— gh-pages 首页显示
    (out_dir / "LATEST.md").write_text(report_md, encoding="utf-8")

    # 按日期归档
    (archive_dir / f"{today}.md").write_text(report_md, encoding="utf-8")

    # 原有兼容文件名（daily_arxiv_docparse_ocr_pro.md）
    (out_dir / "daily_arxiv_docparse_ocr_pro.md").write_text(report_md, encoding="utf-8")

    # JSON 原始数据
    json_data = [
        {
            "title": p.title,
            "arxiv_id": p.arxiv_id,
            "link": p.link,
            "pdf_url": p.pdf_url,
            "authors": p.authors,
            "published": p.published,
            "categories": p.categories,
            "score": p.score,
            "zh_summary": p.zh_summary,
        }
        for p in top_papers
    ]
    (out_dir / "daily_arxiv_docparse_ocr_pro.json").write_text(
        json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✅ 文件已写出到 output/ 目录：")
    print(f"   - output/LATEST.md")
    print(f"   - output/archive/{today}.md")
    print(f"   - output/daily_arxiv_docparse_ocr_pro.md")
    print(f"   - output/daily_arxiv_docparse_ocr_pro.json")
    print("🎉 最终版日报生成完成！")

if __name__ == "__main__":
    main()
