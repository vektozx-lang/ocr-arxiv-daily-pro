#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import litellm
import yaml

# ==================== 配置加载 ====================
CONFIG_PATH = Path("config.yaml")
if CONFIG_PATH.exists():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        CONFIG = yaml.safe_load(f)
else:
    CONFIG = {"llm": {"provider": "deepseek", "model": "deepseek-chat", "api_key_env": "DEEPSEEK_API_KEY"}}

# ==================== System Prompt ====================
SYSTEM_PROMPT = (
    "你是一位 OCR 与文档智能领域的资深研究员，"
    "熟悉文字识别、文档版面分析、表格/公式识别、文档理解等方向的最新进展。"
    "输出时请严格遵循用户要求的格式，使用准确的学术中文表达，不要添加任何额外说明。"
)

def call_llm(prompt: str, temperature: float = 0.7, use_system: bool = True) -> str:
    """生产版 LLM 调用，支持 system prompt"""
    model = "deepseek/deepseek-chat"
    api_key = os.getenv(CONFIG["llm"].get("api_key_env", "DEEPSEEK_API_KEY"))
    messages = []
    if use_system:
        messages.append({"role": "system", "content": SYSTEM_PROMPT})
    messages.append({"role": "user", "content": prompt})
    try:
        response = litellm.completion(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=CONFIG["llm"].get("max_tokens", 4096),
            api_key=api_key,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM 调用失败: {e}")
        return f"LLM 调用失败: {str(e)[:150]}"

# ==================== 第一层：arXiv 检索配置 ====================
# 说明：这些关键词用于 arXiv API 的 all: 字段搜索（标题+摘要+全文）
# 加引号 = 精确短语匹配，不加引号 = 单词匹配
# 覆盖范围越广，召回越多，但噪音也越多，依赖后两层过滤

ARXIV_API = "http://export.arxiv.org/api/query"

DEFAULT_TERMS = [
    # —— 核心 OCR ——
    '"optical character recognition"',
    'OCR',
    '"text recognition"',
    '"scene text recognition"',
    '"scene text detection"',
    '"text detection"',
    '"end-to-end text spotting"',
    '"text spotting"',
    '"handwritten text recognition"',
    '"handwriting recognition"',
    '"handwritten digit"',
    # —— 文档解析与版面 ——
    '"document parsing"',
    '"document understanding"',
    '"document layout"',
    '"layout analysis"',
    '"document layout analysis"',
    '"page understanding"',
    '"document intelligence"',
    '"document image"',
    # —— 表格与公式 ——
    '"table recognition"',
    '"table detection"',
    '"table structure recognition"',
    '"table extraction"',
    '"math formula recognition"',
    '"formula recognition"',
    '"mathematical expression recognition"',
    # —— 关键信息提取 ——
    '"information extraction"',
    '"key information extraction"',
    '"named entity recognition" document',
    '"invoice" recognition',
    '"receipt" recognition',
    # —— 文档问答与预训练 ——
    '"document visual question answering"',
    '"DocVQA"',
    '"document pre-training"',
    '"layout-aware"',
    # —— 图表理解 ——
    '"chart understanding"',
    '"chart recognition"',
    '"figure parsing"',
    # —— 文档图像增强 ——
    '"document dewarping"',
    '"document binarization"',
    '"document enhancement"',
    '"document super resolution"',
    # —— 多语言/历史文献 ——
    '"historical document"',
    '"multilingual OCR"',
    '"low-resource" text recognition',
    # —— 印章/签名 ——
    '"stamp detection"',
    '"signature verification"',
]

# arXiv 分类限定：只在这几个方向的论文里搜索
# cs.CV=计算机视觉, cs.AI=人工智能, cs.CL=计算语言学,
# cs.IR=信息检索, eess.IV=图像视频处理
DEFAULT_CATEGORIES = ["cs.CV", "cs.AI", "cs.CL", "cs.IR", "eess.IV"]

# ==================== 第二层：本地关键词权重打分 ====================
# 说明：对 API 返回的论文做快速粗筛，分数越高越相关
# 这一层速度快（无网络），为第三层 LLM 精筛做预排序

KEYWORD_WEIGHTS = [
    # 高权重：核心 OCR 方向
    ("optical character recognition", 8),
    ("ocr", 7),
    ("text recognition", 6),
    ("scene text", 6),
    ("text detection", 6),
    ("text spotting", 6),
    ("handwritten", 5),
    ("handwriting", 5),
    # 中权重：文档相关
    ("document parsing", 7),
    ("document understanding", 6),
    ("document intelligence", 6),
    ("document layout", 5),
    ("layout analysis", 5),
    ("document image", 4),
    # 中权重：结构化识别
    ("table recognition", 6),
    ("table detection", 5),
    ("table structure", 5),
    ("formula recognition", 6),
    ("math formula", 5),
    # 中权重：信息提取
    ("information extraction", 4),
    ("key information", 5),
    ("invoice", 4),
    ("receipt", 4),
    # 中权重：文档问答与预训练
    ("docvqa", 6),
    ("document visual question", 6),
    ("layout-aware", 5),
    # 低权重：广义相关
    ("document", 3),
    ("layout", 3),
    ("parsing", 3),
    ("chart understanding", 5),
    ("figure parsing", 4),
    ("dewarping", 5),
    ("binarization", 4),
    ("stamp detection", 4),
    ("signature", 3),
    ("multilingual", 3),
    ("historical document", 4),
]

NEGATIVE_WEIGHTS = [
    # 明确无关方向，降分避免噪音
    ("speech recognition", -8),
    ("automatic speech recognition", -8),
    ("asr", -7),
    ("audio", -5),
    ("speaker recognition", -6),
    ("voice", -5),
    ("acoustic", -5),
    ("self-driving", -6),
    ("autonomous driving", -6),
    ("medical image segmentation", -4),
    ("protein", -5),
    ("drug", -5),
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
    """第二层：本地关键词权重打分（快速粗筛）"""
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
    """
    第一层：构造 arXiv API 查询语句
    格式：(all:term1 OR all:term2 ...) AND (cat:cs.CV OR cat:cs.AI ...)
    arXiv API 文档：https://arxiv.org/help/api/user-manual
    """
    term_query = " OR ".join(f"all:{t}" for t in terms)
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    return f"({term_query}) AND ({cat_query})"

def fetch_arxiv(query: str, max_results: int) -> list[Paper]:
    """向 arXiv API 发起请求，按提交时间倒序返回论文列表"""
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
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in entries:
        title = normalize_text(entry.findtext("atom:title", default="", namespaces=ns))
        summary = normalize_text(entry.findtext("atom:summary", default="", namespaces=ns))
        published = normalize_text(entry.findtext("atom:published", default="", namespaces=ns))
        authors = [normalize_text(a.findtext("atom:name", default="", namespaces=ns))
                   for a in entry.findall("atom:author", ns)]
        categories = [c.attrib.get("term", "") for c in entry.findall("atom:category", ns)]
        link = pdf_url = ""
        for link_node in entry.findall("atom:link", ns):
            href = link_node.attrib.get("href", "")
            if link_node.attrib.get("rel") == "alternate":
                link = href
            if link_node.attrib.get("title") == "pdf":
                pdf_url = href
        arxiv_id = normalize_text(entry.findtext("atom:id", default="", namespaces=ns)).rsplit("/", 1)[-1]
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

# ==================== 第三层：LLM 精筛与分析 ====================

def llm_relevance_score(paper: Paper) -> int:
    """
    第三层：LLM 相关度精筛
    比本地关键词打分更准确，能理解语义，识别隐性相关论文
    """
    prompt = f"""请根据以下评分标准，为这篇论文与 OCR/文档智能领域的相关度打分。
严格只返回一个整数（1-10），不要任何解释或其他文字。

【评分标准】
9-10：核心方向，包括但不限于：
      · 文字检测（text detection, DBNet, CRAFT 等）
      · 光学字符识别 OCR / 场景文字识别 / 手写识别
      · 端到端文字识别（end-to-end text spotting）
      · 文档版面分析（layout analysis, document layout）
      · 表格识别与解析（table recognition/detection/structure）
      · 数学公式识别（math formula, LaTeX OCR）
      · 文档理解与文档解析（document understanding/parsing）
      · 关键信息提取 KIE（发票/票据/证件识别, invoice, receipt）
      · 文档视觉问答（DocVQA, document VQA）
      · 文档预训练模型（LayoutLM, document pre-training）
      · 图表/图形理解（chart understanding, figure parsing）
      · 文档图像增强（去模糊/去阴影/矫正/超分, dewarping, binarization）
      · 印章/签名检测（stamp detection, signature verification）
      · 多语言/历史文献识别（multilingual OCR, historical document）

6-8 ：强相关：
      · 多模态文档问答（非纯文档但重度依赖文字理解）
      · 视觉信息抽取（含文字的非文档场景）
      · 通用视觉-语言模型但在文档场景有显著应用
      · 文档检索与匹配

3-5 ：弱相关：
      · 通用视觉问答（VQA，不聚焦文档/文字）
      · 通用目标检测/图像分割
      · 纯 NLP 文本分类/生成（无视觉文档场景）

1-2 ：不相关：
      · 语音识别（ASR）、纯音频处理
      · 无文字/文档场景的纯视觉任务
      · 机器人、自动驾驶、医学图像、生物信息等完全无关领域

【论文信息】
标题：{paper.title}
类别标签：{', '.join(paper.categories[:3])}
摘要：{paper.summary[:1200]}"""
    try:
        score_str = call_llm(prompt, temperature=0.0, use_system=False)
        score = int(re.search(r'\d+', score_str).group())
        return max(1, min(10, score))
    except:
        return paper.score // 2


def generate_single_paper_analysis(paper: Paper) -> Paper:
    """单篇论文深度分析，传入完整上下文，格式约束严格"""
    authors_str = ", ".join(paper.authors[:5]) + ("等" if len(paper.authors) > 5 else "")
    prompt = f"""请深度分析以下论文，严格按照下方格式输出，每节必须有实质内容（不少于2句话），禁止输出"暂无"或省略号。

【论文信息】
- 标题：{paper.title}
- 作者：{authors_str}
- 领域分类：{', '.join(paper.categories[:3])}
- 发布时间：{paper.published[:10]}
- ArXiv ID：{paper.arxiv_id}
- 英文摘要：{paper.summary}

【输出格式（Markdown，严格遵守）】

### 中文摘要
（用2-3句话精准概括论文核心内容，避免泛泛而谈）

### 解决的核心问题
（现有方法存在哪些痛点？本文针对什么具体问题展开研究？）

### 核心创新
（方法/模型/数据集层面的主要贡献，说明"新在哪里"）

### 创新点拆解
- 创新点1：（具体描述）
- 创新点2：（具体描述）
- 创新点3：（如有）

### 实验结果亮点
（在哪些基准/数据集上取得了什么提升？列出关键数字）

### 当前局限
（该方法的适用范围限制、未解决的问题、潜在的失败场景）

### 后续改进方向
- 方向1：（具体可落地的改进思路）
- 方向2：（具体可落地的改进思路）

### 工程落地启发
（对实际 OCR/文档解析工程项目最有参考价值的点是什么？）"""
    analysis = call_llm(prompt, temperature=0.7)
    paper.zh_summary = analysis
    return paper


def generate_daily_synthesis(papers: list[Paper]) -> str:
    """综合日报，传入标题+摘要，避免仅凭标题产生幻觉"""
    papers_info = "\n\n".join([
        f"**论文{i}**：{p.title}\n摘要：{p.summary[:500]}"
        for i, p in enumerate(papers, 1)
    ])
    prompt = f"""今日共有 {len(papers)} 篇 OCR/文档智能高相关论文，请基于以下论文内容生成专业中文日报。
严格按照下方格式输出，每节不少于3句话，内容需有实质性判断，禁止泛泛而谈。

【今日论文】
{papers_info}

【输出格式（Markdown，严格遵守）】

### 今日执行摘要
（一段话概括今日研究整体态势：热度、主要方向、最值得关注的突破）

### 今日研究趋势
（从今日论文中归纳出2-3个明显的技术趋势或研究热点，结合具体论文举例说明）

### 核心技术创新汇总
（跨论文汇总今日最值得关注的技术创新点，说明其意义）

### 研究空白与机会
（哪些重要问题今日论文仍未覆盖？哪些方向存在明显研究机会？）

### 工程落地启发
（对实际 OCR/文档解析工程项目最有价值的参考点，尽量具体）

### 今日优先精读推荐
按重要性列出最值得精读的 3 篇，每篇说明推荐理由（1-2句）。"""
    return call_llm(prompt, temperature=0.7)


# ==================== 报告构建 ====================

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
        lines.append(f"- **PDF**: [{p.pdf_url}]({p.pdf_url})")
        lines.append(f"- **相关度评分**: {p.score}/10\n")
        lines.append("#### 英文摘要\n")
        lines.append(f"{p.summary}\n")
        if p.zh_summary:
            lines.append("#### 深度分析（中文）\n")
            lines.append(p.zh_summary)
        lines.append("\n---\n")
    return "\n".join(lines)


# ==================== 主流程 ====================

def main():
    print("🚀 OCR arXiv Daily Pro v2.0 最终生产版启动...")

    # 第一层：arXiv API 检索
    query = build_query(DEFAULT_TERMS, DEFAULT_CATEGORIES)
    papers = fetch_arxiv(query, CONFIG["arxiv"].get("max_results", 200))
    papers = dedup_papers(papers)
    papers = filter_recent(papers, CONFIG["arxiv"].get("days_back", 14))
    print(f"✅ 第一层：arXiv 检索到 {len(papers)} 篇论文（最近 {CONFIG['arxiv'].get('days_back')} 天）")

    # 第二层：本地关键词权重粗筛，预排序，减少 LLM 调用次数
    papers = sorted(papers, key=lambda p: p.score, reverse=True)
    pre_limit = CONFIG["arxiv"].get("pre_limit", 60)  # 送入 LLM 的候选数量
    papers = papers[:pre_limit]
    print(f"✅ 第二层：本地关键词打分，保留前 {len(papers)} 篇进入 LLM 精筛")

    # 第三层：LLM 相关度精筛
    print("🔍 第三层：LLM 智能相关度评分...")
    for p in papers:
        p.score = llm_relevance_score(p)

    final_limit = CONFIG["arxiv"].get("final_limit", 15)
    top_papers = sorted(papers, key=lambda p: p.score, reverse=True)[:final_limit]
    print(f"📊 最终选中 {len(top_papers)} 篇高相关论文（LLM 评分 ≥ {top_papers[-1].score}/10）")

    # 深度分析每篇论文
    for i, paper in enumerate(top_papers, 1):
        print(f"[{i}/{len(top_papers)}] 深度分析：{paper.title[:60]}...")
        top_papers[i - 1] = generate_single_paper_analysis(paper)

    # 综合日报
    synthesis = generate_daily_synthesis(top_papers)

    # ==================== 写出文件 ====================
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path("output")
    archive_dir = out_dir / "archive"
    out_dir.mkdir(parents=True, exist_ok=True)
    archive_dir.mkdir(parents=True, exist_ok=True)

    report_md = build_markdown_report(top_papers, synthesis, today)

    (out_dir / "LATEST.md").write_text(report_md, encoding="utf-8")
    (archive_dir / f"{today}.md").write_text(report_md, encoding="utf-8")
    (out_dir / "daily_arxiv_docparse_ocr_pro.md").write_text(report_md, encoding="utf-8")

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

    print("✅ 文件已写出到 output/ 目录：")
    print(f"   - output/LATEST.md")
    print(f"   - output/archive/{today}.md")
    print(f"   - output/daily_arxiv_docparse_ocr_pro.md")
    print(f"   - output/daily_arxiv_docparse_ocr_pro.json")
    print("🎉 最终版日报生成完成！")

if __name__ == "__main__":
    main()
