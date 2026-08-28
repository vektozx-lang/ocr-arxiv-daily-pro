# OCR arXiv Daily Pro — 2026-08-28

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-08-27 09:10 - 2026-08-28 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition

- **ArXiv ID**: [2608.27169v1](https://arxiv.org/abs/2608.27169v1)
- **作者**: Hiuyi Cheng, Nuo Xu, Yuyi Zhang, Xuhan Zheng, Wei Pan...
- **发布时间**: 2026-08-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.27169v1](https://arxiv.org/pdf/2608.27169v1)
- **相关度评分**: 10/10

#### 英文摘要

Ancient Chinese artifact text recognition is fundamental to heritage digitization, and benchmarks for ancient texts are essential for evaluating current model capabilities. However, existing benchmarks suffer from ''fragmentation'', manifested in limited temporal coverage, limited medium diversity, and incomplete script types. Therefore, we present Ancient-Bench, a comprehensive benchmark of 2,700 images for ancient Chinese artifact text recognition, featuring three dimensions: Multi-millennial (spanning 3,000 years of character evolution), Multi-medium (covering nine artifact categories), and Multi-script (encompassing seven historical script forms). To enable consistent and fair evaluation across heterogeneous media, we further define three annotation standards tailored to the medium-specific characteristics of ancient texts: symbol standardization, character standardization, and parsing standardization. Extensive experiments on Ancient-Bench covering general Vision-Language Models (VLMs) and OCR-specialist models reveal that ancient Chinese artifact text recognition remains fundamentally unsolved, with persistent challenges in variant characters, specialized symbols, and hallucination. The dataset is available at https://github.com/SCUT-DLVCLab/Ancient_Bench.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations

- **ArXiv ID**: [2608.26921v1](https://arxiv.org/abs/2608.26921v1)
- **作者**: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim
- **发布时间**: 2026-08-27
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.26921v1](https://arxiv.org/pdf/2608.26921v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. D2C-Routing: Dimension-to-Composition Evidence Routing for Mixed-Origin AI-Generated Text Detection

- **ArXiv ID**: [2608.27380v1](https://arxiv.org/abs/2608.27380v1)
- **作者**: Xin Chen, Fuwei Zhang, Yiqi Tong, Wei Guo, Yutian Xiao...
- **发布时间**: 2026-08-28
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.27380v1](https://arxiv.org/pdf/2608.27380v1)
- **相关度评分**: 10/10

#### 英文摘要

AI-generated text detection is commonly framed as a binary document-level judgment about whether a text is human-written or machine-generated. This framing breaks down for mixed-origin writing, where content origin and expression origin may differ. We cast mixed-origin detection as dimension-to-composition source attribution, inferring content origin and expression origin before composing them into four collaboration types. We propose Dimension-to-Composition Routing (D2C-Routing), which routes content-side and expression-side evidence to supervised dimension heads before a learned gated composition layer predicts the final label. On MixD2C, a reconstructed split derived from the HART mixed-origin benchmark, our disclosed D2C-Routing-based detector system reaches 0.8603 four-way Avg TPR@1%FPR, 6.5 points above the same-split RACE-local rerun. Core ablations support the routing design, while error analysis shows that distinguishing AI-content/human-expression from fully AI-generated text remains the hardest boundary. Code is available at https://github.com/bystander563/d2c-routing-artifact.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. PailitaoGR: Latent Think-with-Images for Generative Image Retrieval

- **ArXiv ID**: [2608.26658v1](https://arxiv.org/abs/2608.26658v1)
- **作者**: Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan...
- **发布时间**: 2026-08-27
- **分类**: cs.CV, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.26658v1](https://arxiv.org/pdf/2608.26658v1)
- **相关度评分**: 10/10

#### 英文摘要

Generative retrieval has demonstrated strong performance by directly generating product semantic identifiers (SIDs). Extending this paradigm to image search, however, is nontrivial because real-world query images contain diverse information, including the search target, useful auxiliary evidence, and irrelevant visual content. This requires the model to identify and focus on the search target while selectively utilizing auxiliary evidence. In this paper, we propose \textbf{PailitaoGR}, a \emph{Latent Think-with-Images} method for generative image retrieval, which internalizes target-focused perception and selective auxiliary-evidence utilization into a the generative retrieval model, enabling \textit{Zooming without Cropping} and \textit{Reading without OCR}. Specifically, we design a target-focused perception mechanism that identifies and enhances visual tokens of the search target, consisting of a target Enhancer and a learning strategy based on on-policy distillation and attention guidance loss, enabling the model to focus on search-target regions. We also design a selective auxiliary-evidence utilization mechanism that identifies and enhances visual tokens of auxiliary evidence, including an auxiliary enhancer and an in-capacity incremental contrastive distillation strategy, enabling the model to exploit auxiliary evidence. We construct training and validation sets sampled from real-world online image-search logs. Experiments show that our method outperforms existing baselines by an average of 13.8\%, validating its effectiveness.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases

- **ArXiv ID**: [2608.27391v1](https://arxiv.org/abs/2608.27391v1)
- **作者**: Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno...
- **发布时间**: 2026-08-28
- **分类**: cs.AI, cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.27391v1](https://arxiv.org/pdf/2608.27391v1)
- **相关度评分**: 10/10

#### 英文摘要

LLMs are increasingly able to answer complex questions about enterprise-scale document collections. But evaluation is hard: companies don't want to share internal communications, and synthetic datasets have been overly simple. We present CorporateBench (CB), a human-validated multi-task Q&A benchmark whose scale approaches the conditions LLMs encounter in corporate communication networks, with evaluation corpora surpassing 230,000 documents. CB evaluates LLMs across two dimensions (information extraction and knowledge base querying) through four synthetically generated firms ranging from 12 to 10,000 employees. Each corpus is sampled from a temporally evolving knowledge base describing a consistent world, guaranteeing cross-document logical consistency even across hundreds of thousands of documents. We evaluate five LLMs on CB, revealing increasingly poor performance as input size approaches realistic scales. CB provides LLM developers a metric for corporate communication reasoning, filling a crucial gap in the benchmarking ecosystem.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Relational Over-Regularization: Graph-Based AI-Generated Text Detection via Sentence Transition Deviation

- **ArXiv ID**: [2608.26694v1](https://arxiv.org/abs/2608.26694v1)
- **作者**: Hyeonchu Park, Bugeun Kim
- **发布时间**: 2026-08-27
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.26694v1](https://arxiv.org/pdf/2608.26694v1)
- **相关度评分**: 10/10

#### 英文摘要

Detecting AI-generated text (AIGT) remains challenging because existing approaches rely on token-level statistical signals or independent stylometric features, causing them to overfit to specific generators and fail under distribution shift. We identify a structural signal at the sentence-pair level: LLMs produce inter-sentence transition variance that deviates from human writing through inflated variance driven by recurring similarity bursts at paragraph boundaries and templated transitions. We formalize this as Relational Over-Regularization (ROR) and validate it across four benchmarks (p < 0.001). The central contribution is this relational problem formulation, not a novel GNN architecture; CSFG is one concrete instantiation for operationalizing ROR. To exploit this signal, we propose the Cross-Source Stylometric Fingerprint Graph (CSFG), a graph-based framework that encodes positional, sequential, semantic, and transition deviation signals as learnable GNN edge features. The per-edge signed deviation δ_ij operationalizes ROR without hand-crafted thresholds and acts as a false-positive calibrator. CSFG achieves 97.14% accuracy under binary detection, outperforming the strongest graph-based baseline by 11.14 pp, with a false-positive rate of 1.57% and robust generalization to unseen LLMs in the inflated-variance regime; detection degrades for generators whose transition variance falls at or below the human baseline.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Sophistication in GenAI Use: Field Evidence from a Large Firm

- **ArXiv ID**: [2608.27364v1](https://arxiv.org/abs/2608.27364v1)
- **作者**: Nicholas J. Hallman, Zachary T. Kowaleski, Anu Puvvada, Jaime J. Schmidt
- **发布时间**: 2026-08-28
- **分类**: cs.AI, econ.GN
- **PDF**: [https://arxiv.org/pdf/2608.27364v1](https://arxiv.org/pdf/2608.27364v1)
- **相关度评分**: 10/10

#### 英文摘要

We study how sophistication in generative AI (genAI) use varies among the back-office workforce of a large firm. Using proprietary data, we observe 713,564 employee prompts and their corresponding large language model responses from nearly 4,000 back-office employees across 15 functional areas over eight months in 2025. We document three main findings. First, senior employees exhibit more sophisticated genAI use, consistent with domain expertise complementing genAI capabilities. Second, sophistication varies considerably across functions and is highest in Strategy, Digital Innovation, and Project Management, three groups that share a focus on firmwide strategic initiatives and organizational change. Third, we observe neither improvements in sophistication over time nor lasting improvements following formal AI training, suggesting that sophisticated use can be difficult to change. Together, our study provides measures of and insights into sophisticated genAI use that managers can use to improve outcomes and that researchers can use in future research.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers

- **ArXiv ID**: [2608.27343v1](https://arxiv.org/abs/2608.27343v1)
- **作者**: Ke Shu, Kira Hinderks, Eetu Mäkelä, Mikko Tolonen
- **发布时间**: 2026-08-28
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.27343v1](https://arxiv.org/pdf/2608.27343v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottish philosopher David Hume, spanning books from ECCO (Eighteenth Century Collections Online) and historical newspapers. Because the input consists of fragmented reuse hits instead of clean document pairs, and positive coverage is inherently incomplete, we formulate the task as pair-level evidence consolidation into plausible transmission relations and compare three methodological families: a staged rule-based workflow, baselines (a decision tree and two direct LLM settings), and automated rule adaptation. On labeled ECCO--ECCO slices, pair-level feature aggregation alone already reaches 0.948 F1 on the main labeled slice, while the final workflow gives the strongest overall precision-recall trade-off among the tested rule stages. On the full ECCO--ECCO candidate universe, direct LLM baselines flag up to 14,886 pairs as reprints compared to 771 for the final workflow, behaving in this direct-prompt setup as high-recall candidate expanders rather than precision-controlled deployment classifiers. On ECCO--Newspaper, manual audit confirms all 176 predicted positives as genuine cases of republication or reuse, while issue duplication and source-side multiplicity reveal additional provenance structure. Under incomplete ground truth, auditable pair-level evidence consolidation provides a practical way to produce compact candidate spaces for historical inspection.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. STAR : Sentence Translation Alignment Rate for Document-to-Document Machine Translation

- **ArXiv ID**: [2608.27161v1](https://arxiv.org/abs/2608.27161v1)
- **作者**: Yichen Dong, Hao Wang, Junhui Li, Linlong Xu, Longyue Wang...
- **发布时间**: 2026-08-27
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.27161v1](https://arxiv.org/pdf/2608.27161v1)
- **相关度评分**: 10/10

#### 英文摘要

Large Language Models (LLMs) have enabled a shift from sentence-level to document-to-document (Doc2Doc) machine translation, promising improved global coherence. However, document-to-document generation in a single pass frequently suffers from structural misalignment, manifesting as sentence omissions or hallucinations that violate the core requirement of source-target correspondence. To address this, we introduce Sentence Translation Alignment Rate (STAR), an auxiliary metric that explicitly quantifies sentence-level structural fidelity. Building on this, we propose STAR-masked Preference Optimization (StarPO), a framework that ranks document-level hypotheses by structural quality and utilizes a dynamic alignment mask to focus optimization on misaligned segments. Experimental results across news and literary domains demonstrate that StarPO significantly enhances translation quality and structural integrity. Notably, StarPO allows compact models to surpass the performance of massive proprietary systems like GPT-4o while maintaining superior token efficiency.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. LAAF: A Layered Accountability Architecture Framework for LLM Applications

- **ArXiv ID**: [2608.27102v1](https://arxiv.org/abs/2608.27102v1)
- **作者**: Prachi Chaturvedi, Shahnawaz Ahmad, Ehsan Nowroozi, Muhammad Waqas, George Loukas...
- **发布时间**: 2026-08-27
- **分类**: cs.AI, cs.CR
- **PDF**: [https://arxiv.org/pdf/2608.27102v1](https://arxiv.org/pdf/2608.27102v1)
- **相关度评分**: 10/10

#### 英文摘要

Large Language Models (LLMs) operate in hospitals, courtrooms, banks, and public service desks, where fluent, confident outputs are treated as authoritative even when ungrounded or incorrect. When such an output contributes to harm, who is answerable, and through what mechanisms can responsibility be traced, explained, and acted upon? Following PRISMA guidance, five databases were searched from January 2022 to March 2026 against four review questions; of 4,512 records identified, 122 primary studies were included, together with 12 regulatory and standards documents analysed as primary sources. The review consolidates a sociotechnical account of accountability as an actor-forum relation resolved into five dimensions, and synthesises mechanisms across four families: technical controls, human oversight, organisational governance, and documentation and traceability, each with a maturity assessment. The corpus is read through a four-layer classification device spanning provenance, application logic, human oversight, and governance and redress, cross-cut by traceability, role clarity, and continuous monitoring. Both are mapped onto the EU AI Act, whose high-risk obligations have applied since 2 August 2026, the NIST AI RMF with its Generative AI Profile, ISO/IEC 42001, and sectoral guidance in healthcare, consumer finance, education, and the public sector. Four persistent gaps emerge: under-specification of human oversight, absence of shared accountability metrics, disciplinary disconnection, and limited empirical evaluation, alongside five structural tensions that no surveyed instrument resolves. The review closes by consolidating the classification device into an integrated accountability architecture, LAAF, with cybersecurity aligned to the OWASP LLM Top 10 (2025); it is a synthesis of the surveyed evidence rather than a validated artefact.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. Beyond Classification: Task-Dependent Learnability under Privacy-Motivated Image Transformations

- **ArXiv ID**: [2608.27066v1](https://arxiv.org/abs/2608.27066v1)
- **作者**: Leon Ranke, Wolfgang Hübner, Ronny Hug, Michael Arens, Jürgen Beyerer
- **发布时间**: 2026-08-27
- **分类**: cs.CV, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2608.27066v1](https://arxiv.org/pdf/2608.27066v1)
- **相关度评分**: 10/10

#### 英文摘要

Privacy-Enhancing Technologies (PETs) in computer vision often rely on noise or image perturbations to protect visual data while securely processing it, creating a trade-off between task performance and protection. This trade-off is commonly evaluated using image classification, which primarily captures semantic separability and remains robust despite significant geometric, spatial layout or local boundary alterations. As a result, it is too simplistic as a proxy for generic vision tasks. Exhaustive downstream-task evaluation, however, is computationally expensive because models must often be trained for each PET transformation and parameter setting. We therefore propose a compute-aware multi-task protocol for evaluating PETs in model training. It combines lightweight proxy tasks that target complementary aspects of visual structure while remaining simple and fast to compute. Across irreversible privacy transformations, key-based block primitives, and learnable image encryption schemes, we demonstrate that PETs with similar classification accuracy can differ substantially on other tasks. The outcomes highlight the need for PET evaluation protocols that move beyond classification-only reporting.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. ITL: Interpretable Document Alignment with Structured Reference Frameworks

- **ArXiv ID**: [2608.27031v1](https://arxiv.org/abs/2608.27031v1)
- **作者**: Raúl Giráldez, Dayrelis Mena, Jesús S. Aguilar--Ruiz
- **发布时间**: 2026-08-27
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.27031v1](https://arxiv.org/pdf/2608.27031v1)
- **相关度评分**: 10/10

#### 英文摘要

Measuring alignment between documents and structured reference frameworks requires identifying conceptual evidence distributed throughout the text and reporting it through measures that are quantitative, interpretable, and traceable. Many commonly used retrieval and classification approaches return either pairwise similarity scores or one or more class labels, whereas fewer methods provide concept-level scores that are directly traceable to the terminological evidence supporting them. We present \emph{Intelligent Target Locator} (ITL), a domain-agnostic and language-portable methodology that estimates the affinity between the textual units of a target document and the concepts defined in a \emph{Structured Reference Document} ($SRD$). From the $SRD$, ITL induces concept-specific terminological profiles built from independent terms, bigrams, trigrams, and co-occurrences. Each term is assigned an importance weight that combines concept membership, term-type specificity and inter-concept discriminability. The output is a textual-unit--concept affinity matrix that can be aggregated at different levels of granularity. We conduct an internal consistency assessment using the 17 Sustainable Development Goals (SDGs), evaluating each official goal statement against the $SRD$ induced from the same set of descriptors. Every statement reached its highest affinity with the corresponding concept, and the mean affinity across the remaining concepts stayed marginal relative to the mean reference affinity. This separation indicates that ITL distinguishes the conceptual profiles of the framework. ITL thus offers a general basis for quantifying document alignment with structured frameworks while keeping each result traceable to the terminological evidence that supports it.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Conversational Recommendation over Live E-Commerce Catalogues with Self-Refreshing Retrieval

- **ArXiv ID**: [2608.27006v1](https://arxiv.org/abs/2608.27006v1)
- **作者**: Ante Kapetanovic, Tomislav Duricic, Dionizije Fa, Andro Mercep, Emanuel Lacic
- **发布时间**: 2026-08-27
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.27006v1](https://arxiv.org/pdf/2608.27006v1)
- **相关度评分**: 10/10

#### 英文摘要

Conversational recommender systems based on large language models (LLMs) are usually evaluated on static, pre-indexed item collections, yet e-commerce catalogues change continuously as products are added or removed, repriced, and restocked. We present a merchant-agnostic, multi-turn conversational shopping assistant that operates over such live catalogues. Its central component is a self-refreshing retriever that ingests a merchant product feed, enriches the records, and synchronizes them into a vector index. On each run, per-item hashes identify which products are new, changed, deleted, or unchanged, so only the delta is processed rather than rebuilding the whole catalogue. A controller-based dialogue layer consumes this index, using an LLM only for intent classification and preference elicitation while retrieval, reranking, and diversity selection run as dedicated functions. Our demonstration is a WhatsApp shopping assistant in which catalogue changes reach the recommendations after the next successful sync. A live chatbot, documentation, and a recorded walkthrough are available at https://github.com/infobip/infobip-agentic-crs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- **ArXiv ID**: [2608.27142v1](https://arxiv.org/abs/2608.27142v1)
- **作者**: Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke...
- **发布时间**: 2026-08-27
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.27142v1](https://arxiv.org/pdf/2608.27142v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City

- **ArXiv ID**: [2608.27456v1](https://arxiv.org/abs/2608.27456v1)
- **作者**: Tianjie Ju, Zheng Wu, Yueqing Sun, Yuhan Cui, Bobo Li...
- **发布时间**: 2026-08-28
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.27456v1](https://arxiv.org/pdf/2608.27456v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
