# OCR arXiv Daily Pro

面向 OCR、文档解析、版面分析、表格识别、公式识别和文档理解方向的 arXiv 自动日报项目。

项目会定期抓取近几天的 arXiv 论文，先做本地关键词粗筛，再用 LLM 做相关度精筛，最后为入选论文生成中文深度分析和日报级综合总结，并将结果写入 `output/` 目录。

当前 GitHub Actions 的日报口径已经固定为“调度窗口日报”：

- 工作流每天按 `01:10 UTC` 运行
- 按北京时间等价于每天 `09:10`
- `YYYY-MM-DD.md` 表示本次运行结束时刻所在的日期
- `2026-04-08.md` 对应的时间窗口是 `2026-04-07 09:10` 到 `2026-04-08 09:10`（北京时间）
- 每天的归档只覆盖这个 24 小时窗口，不会再用前一天的论文补齐数量

## 当前项目包含什么

- `scripts/fetch_arxiv_daily_pro.py`
  主脚本。负责抓取 arXiv、打分、调用 LLM、生成 Markdown/JSON 报告。
- `config.yaml`
  本地配置文件，控制抓取数量、回溯天数、日报时区、日报窗口锚点、预筛选数量、最终保留数量，以及 API Key 环境变量名等。
- `.github/workflows/daily-arxiv-ocr-pro.yml`
  GitHub Actions 工作流。支持定时执行、手动触发、推送 `output/` 内容并部署到 `gh-pages`。
- `output/`
  当前仓库已提交的日报产物，包括最新报告、历史归档、JSON 输出和一个简单静态页面。

## 功能流程

1. 使用内置 OCR / Document AI 关键词和 arXiv 分类构造查询。
2. 分批请求 arXiv API，避免 URL 过长导致请求失败。
3. 抓取最近几天的论文，保证能覆盖完整的日报窗口。
4. 仅保留当前日报窗口内的论文。
5. 用本地关键词权重做第一轮相关性排序。
6. 用 LLM 对候选论文做 1 到 10 分相关度精筛。
7. 对最终入选论文生成中文深度分析。
8. 生成综合日报，并写出 Markdown 和 JSON 结果到 `output/`。

## 目录结构

```text
.
├── .github/
│   └── workflows/
│       └── daily-arxiv-ocr-pro.yml
├── output/
│   ├── archive/
│   ├── daily_arxiv_docparse_ocr_pro.json
│   ├── daily_arxiv_docparse_ocr_pro.md
│   ├── index.html
│   └── LATEST.md
├── scripts/
│   ├── fetch_arxiv_daily_pro.py
│   └── generate_github_pages.py
├── config.yaml
├── index.html
├── requirements.txt
└── README.md
```

## 环境要求

- Python 3.11 或更高版本
- 可访问 arXiv API
- DeepSeek API Key

## 安装

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 本地运行

先设置 API Key：

```bash
export DEEPSEEK_API_KEY="your_api_key"
python scripts/fetch_arxiv_daily_pro.py
```

Windows PowerShell：

```powershell
$env:DEEPSEEK_API_KEY="your_api_key"
python scripts\fetch_arxiv_daily_pro.py
```

运行完成后会生成：

- `output/LATEST.md`
- `output/archive/YYYY-MM-DD.md`
- `output/daily_arxiv_docparse_ocr_pro.md`
- `output/daily_arxiv_docparse_ocr_pro.json`

## 日报口径

当前默认使用“固定调度窗口”而不是“自然日”：

- 窗口结束时间由 `config.yaml` 中的 `arxiv.schedule_utc_hour` 和 `arxiv.schedule_utc_minute` 决定
- 默认配置是 `01:10 UTC`
- 报告内部会显示完整时间窗口，例如：
  `2026-04-07 09:10 - 2026-04-08 09:10 (Asia/Shanghai)`
- 归档文件名仍然使用窗口结束时刻在本地时区对应的日期，例如 `2026-04-08.md`

这意味着：

- `2026-04-08.md` 不是“北京时间 2026-04-08 自然日的论文”
- 它表示“截至北京时间 2026-04-08 09:10 这次运行所覆盖的过去 24 小时窗口”

这样做的目的是避免：

- 当天自然日尚未结束导致日报不完整
- 连续两天日报因为“最近 3 天”滚动筛选而出现大量重复论文

## 论文数量规则

最终日报篇数由 `arxiv.final_limit` 控制，当前默认是 `15`。处理规则如下：

- 少于 `15` 篇：按实际数量发布，不补前一天或更早的论文
- 等于 `15` 篇：全部发布
- 多于 `15` 篇：按分数排序取前 `15` 篇
- 等于 `0` 篇：生成空日报，不报错

这条规则对 GitHub Actions 很重要：日报语义始终以“当前窗口内的新论文”为准，而不是为了凑满数量回填旧论文。

## 配置说明

当前项目主要通过 `config.yaml` 配置：

```yaml
llm:
  provider: deepseek
  model: deepseek-chat
  api_key_env: DEEPSEEK_API_KEY
  temperature: 0.7
  max_tokens: 4096

arxiv:
  timezone: Asia/Shanghai
  schedule_utc_hour: 1
  schedule_utc_minute: 10
  max_results: 200
  days_back: 3
  pre_limit: 60
  final_limit: 15
```

字段含义：

- `llm.api_key_env`
  读取 API Key 的环境变量名。
- `llm.max_tokens`
  单次 LLM 调用的最大输出 token 数。
- `arxiv.timezone`
  报告展示时间和归档日期使用的时区。
- `arxiv.schedule_utc_hour`
  工作流窗口结束时刻的 UTC 小时。
- `arxiv.schedule_utc_minute`
  工作流窗口结束时刻的 UTC 分钟。
- `arxiv.max_results`
  arXiv 总抓取上限。
- `arxiv.days_back`
  抓取候选集时向前回溯的天数。它用于保证抓取范围足够覆盖日报窗口，不代表日报最终展示这几天的全部论文。
- `arxiv.pre_limit`
  本地粗筛后送入 LLM 精筛的候选数量。
- `arxiv.final_limit`
  最终日报中保留的论文数量上限。

## 调试环境变量

为了便于本地重跑历史日报，脚本支持两个覆盖变量：

- `REPORT_DATE`
  仅用于本地重放。它会把窗口结束时间固定到该日期对应的调度点。
  例如在当前默认配置下，`REPORT_DATE=2026-04-08` 表示窗口结束于 `2026-04-08 01:10 UTC`。
- `REPORT_END_UTC`
  直接指定窗口结束时间，格式为 ISO 8601，例如：
  `2026-04-08T01:10:00+00:00` 或 `2026-04-08T01:10:00Z`

如果两者同时存在，`REPORT_DATE` 的优先级更高。

## 输出内容

Markdown 报告结构大致包括：

- 报告标题
- 时间窗口
- 今日综合分析
- 今日执行摘要
- 今日研究趋势
- 核心技术创新总结
- 研究空白与机会
- 工程落地启发
- 今日优先精读推荐
- 论文详情

每篇论文详情包括：

- 标题、arXiv 链接、PDF 链接
- 作者、发布时间、分类
- 英文摘要
- 中文深度分析

JSON 输出适合接入知识库、检索系统、前端展示或后续统计分析。

## GitHub Actions

工作流文件是 `.github/workflows/daily-arxiv-ocr-pro.yml`，当前行为如下：

- 支持 `workflow_dispatch` 手动触发
- 定时任务是 `10 1 * * *`
- 按 UTC 计算是每天 `01:10`
- 按北京时间计算是每天 `09:10`
- 运行时默认生成“过去 24 小时窗口”的日报
- 执行完成后会把 `output/` 部署到 `gh-pages`
- 同时会把新的 `output/` 内容提交回仓库

如果你要启用自动运行，需要在仓库 `Actions secrets` 中配置：

- `DEEPSEEK_API_KEY`

## 仓库内现状说明

根据当前代码，下面这些点需要在 README 里明确说明：

- arXiv 查询词和分类目前写死在 [scripts/fetch_arxiv_daily_pro.py](./scripts/fetch_arxiv_daily_pro.py) 的 `DEFAULT_TERMS` 和 `DEFAULT_CATEGORIES` 中，不是通过环境变量动态传入。
- `config.yaml` 中虽然有 `llm.provider` 和 `llm.model` 字段，但当前脚本实际调用的是固定模型 `deepseek/deepseek-chat`。
- `scripts/generate_github_pages.py` 目前是占位文件，没有独立生成逻辑。
- `output/index.html` 当前是仓库内已有的静态页面，不是 `fetch_arxiv_daily_pro.py` 运行时生成的产物。

## 依赖

`requirements.txt` 当前只有两个运行时依赖：

- `litellm`
- `pyyaml`

## 可直接查看的产物

- 最新日报：`output/LATEST.md`
- 当前完整日报：`output/daily_arxiv_docparse_ocr_pro.md`
- 结构化数据：`output/daily_arxiv_docparse_ocr_pro.json`
- 历史归档：`output/archive/`

## 后续可以继续完善的方向

- 将查询词、分类和模型配置进一步外置到 `config.yaml`
- 让 `output/index.html` 由脚本自动生成，而不是手工维护
- 增加失败重试、缓存和增量更新逻辑
- 增加周报、趋势统计和标签聚合
- 增加飞书、企业微信、Telegram 等推送能力
