# OCR arXiv Daily Pro — 2026-10-08

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-07 09:10 - 2026-10-08 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a2ab99e5-022f-4

---

## 📄 论文详情

### 1. InscriptionOCR: A Dataset and Method for Understanding Inscriptions

- **ArXiv ID**: [2610.09439v1](https://arxiv.org/abs/2610.09439v1)
- **作者**: Jaidev Sanjay Khalane, Akbar Ali, V. N. Prabhakar, Shanmuganathan Raman
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.09439v1](https://arxiv.org/pdf/2610.09439v1)
- **相关度评分**: 10/10

#### 英文摘要

Ancient script image restoration is a fundamental problem in computer vision, as it directly affects the reliable analysis and interpretation of historical documents and inscriptions. Ashokan Brahmi is an ancient script extensively used during the reign of Emperor Ashoka in the 3rd century BC, primarily for inscriptions in Prakrit. These inscriptions, including major and minor rock and pillar edicts, constitute a valuable yet largely unexplored source of data for computational analysis. The degraded nature of inscription imagery and the lack of standardized digital resources pose significant challenges for automated processing. We present an end-to-end AI-based framework for understanding ancient inscriptions that encompasses image enhancement, optical character recognition (OCR), transliteration, and neural machine translation (NMT). The proposed pipeline processes low-quality images captured directly from stone inscriptions, performs image restoration and Brahmi script character recognition, maps the recognized characters to the Roman script, and finally translates the resulting Prakrit text into English. We also introduce two new datasets: (i) InscriptionOCR Dataset: the largest publicly usable digital OCR dataset for Brahmi script to date, consisting of over 200,000 character images across about 600 classes, and (ii) a bilingual Prakrit-English parallel corpus comprising over 2,000 sentence pairs for NMT. We believe that the proposed framework and datasets will facilitate future research in ancient script analysis, low-resource OCR, and digital epigraphy.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 93ee16ac-c79d-4

---

### 2. TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning

- **ArXiv ID**: [2610.09360v1](https://arxiv.org/abs/2610.09360v1)
- **作者**: Ruochi Li, Jianzhe Lin, Haoxuan Zhang, Haihua Chen, Junhua Ding...
- **发布时间**: 2026-10-07
- **分类**: cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.09360v1](https://arxiv.org/pdf/2610.09360v1)
- **相关度评分**: 10/10

#### 英文摘要

Real-world documents distribute evidence across text, tables, figures, and captions within complex page layouts. Answering complex questions over such documents therefore requires more than retrieving relevant passages: systems must recover the evidence topology that connects heterogeneous evidence units. Existing GraphRAG evaluations remain largely text-centered, while multimodal document RAG benchmarks assess cross-modal retrieval and generation without directly evaluating recovery of the intended evidence topology. We introduce TOPOGRAPHRAG-BENCH, a layout-grounded benchmark for multimodal evidence reasoning in GraphRAG, comprising 2,024 questions over 201 long, visually rich documents. Questions are constructed bottom-up from text, figure, and table evidence units under three controlled topologies: single-hop retrieval, bridge-chain reasoning, and multi-source synthesis. To ensure that questions preserve their intended structure, we apply counterfactual validation for shortcut resistance, modality necessity, and evidence necessity. We evaluate text-only GraphRAG, page-level visual retrieval, and multimodal GraphRAG systems using retrieval, generation, and topology-aware reasoning metrics. Multimodal GraphRAG systems achieve the strongest overall performance, but still fail when visual-textual evidence alignment or multi-unit composition is incomplete. Text-only GraphRAG struggles when key dependencies are grounded in figures or tables, while page-level visual retrieval lacks the fine-grained structure needed for topology recovery. These findings motivate GraphRAG systems that move beyond text-derived entity relation graphs to explicitly model document layouts, cross-modal evidence alignment, and the reasoning roles of evidence units. Code and data are available at https://richardlrc.github.io/TopoGraphRAG-Bench/.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d7dd932b-f5d2-4

---

### 3. Inverting Multi-Vector Visual Document Indices

- **ArXiv ID**: [2610.09920v1](https://arxiv.org/abs/2610.09920v1)
- **作者**: Zhuchenyang Liu, Yao Zhang, Yu Xiao
- **发布时间**: 2026-10-07
- **分类**: cs.IR, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.09920v1](https://arxiv.org/pdf/2610.09920v1)
- **相关度评分**: 10/10

#### 英文摘要

Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we hypothesize that whoever runs or breaches the store can reproduce a page from its index alone. We frame inversion as conditional document image generation and infer from the vectors what the attack needs: the encoder, the page shape and, for shuffled vectors, their order. On the ViDoRe v3 benchmark, pages inverted from raw indices recover 47% of the words and 45% of the sensitive tokens. Used as queries against the stored indices, they rank their source page first 98.4% of the time. We test two cheap protections, token pooling and shuffling, which both cut word recall to about 8%. A model that restores the order of a shuffled index raises the share of source pages ranked first from 3.8% to 93.5%, while inverting a pooled index remains open. To test generalisation, we apply the same attack unchanged to another multi-vector retriever: its inverted pages still rank their source page first 70.2% of the time, though its word recall stays below a nearest-neighbour baseline. Multi-vector visual document retrievers are therefore vulnerable to inversion through their stored index, which should be protected like the documents it encodes.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4bc8aef7-3b62-4

---

### 4. Rubix: Global Correspondence-Free Point Set Alignment through Assignment Geometry

- **ArXiv ID**: [2610.10408v1](https://arxiv.org/abs/2610.10408v1)
- **作者**: Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.CG, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.10408v1](https://arxiv.org/pdf/2610.10408v1)
- **相关度评分**: 10/10

#### 英文摘要

Procrustes-Wasserstein alignment jointly estimates a matching and rotation without supplied correspondences, but alternating minimization can stop at suboptimal solutions. Rubix solves the equally weighted planar problem globally under squared Euclidean loss. Each matching $σ$ of two centered $n$-point sets defines a complex correlation $z_σ=\sum_i\bar x_i y_{σ(i)}$. Their convex hull is the permutation polygon: supporting vertices give optimal matchings at fixed rotations, and the farthest vertex gives the global alignment. We prove the sharp bound of $n(n-1)$ vertices for $n\ge2$, answering Rote's rotation-assignment open problem. In exact arithmetic, assignment queries recover the polygon in $\mathcal O(n^5)$ operations. Assignment-based bounds extend the approach to three-dimensional rotations and partial matching at a supplied translation through branch-and-bound. On timed MPEG-7 shape pairs, Rubix attains every numerical reference value in 12 ms on average, 50 times faster than a rotation grid at the same accuracy. Its distances improve gravity-aligned matching of real 3D scans, shape retrieval and noisy crystal classification over alternating minimization.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bfea45c8-a7b4-4

---

### 5. LoomSC: Scalable Deep Subspace Clustering with Projector Factorization and Exact Spectral Reduction

- **ArXiv ID**: [2610.10266v1](https://arxiv.org/abs/2610.10266v1)
- **作者**: Nairouz Mrabah, Youssef Melki, Mohamed Bouguessa, Riadh Ksantini, Shakeeb Murtaza...
- **发布时间**: 2026-10-07
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.10266v1](https://arxiv.org/pdf/2610.10266v1)
- **相关度评分**: 10/10

#### 英文摘要

Dense self-expression matrices and full-affinity spectral clustering limit the scalability of subspace clustering. We introduce the Latent Orthogonal Optimization Model for Subspace Clustering (LoomSC), a framework that addresses both bottlenecks through projector factorization and exact spectral reduction. Motivated by the spectral structure of least-squares regression, LoomSC jointly learns latent features and a projector self-representation through two thin factors. Alternating Procrustes and least-squares updates preserve the sample factor's orthogonality while keeping the coefficient matrix implicit. We construct a nonnegative quadratic affinity that preserves the projector's support. An exact feature map then reduces its normalized spectral problem to an eigenproblem whose dimension depends only on the factor width. Neither the full affinity nor the sample Laplacian needs to be formed. Our analysis quantifies the projector approximation and identifies conditions for subspace preservation and within-subspace connectivity. For fixed dimensions and iteration budgets, the complete pipeline has linear time and memory complexity in the number of samples. Across five image-clustering benchmarks, LoomSC ranks first or second in all 15 dataset-metric comparisons against 9 state-of-the-art baselines. Its mean accuracy exceeds the highest baseline mean by 6.66 percentage points. Synthetic experiments scale to 500,000 samples while maintaining at least 99.8% accuracy.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4a6b7558-70a4-4

---

### 6. Document-Level Text Simplification in Estonian Using Large Language Models

- **ArXiv ID**: [2610.10378v1](https://arxiv.org/abs/2610.10378v1)
- **作者**: Meeri-Ly Muru, Eduard Barbu
- **发布时间**: 2026-10-08
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.10378v1](https://arxiv.org/pdf/2610.10378v1)
- **相关度评分**: 10/10

#### 英文摘要

Document-level text simplification involves transformations that go beyond sentence-internal edits, addressing discourse coherence, anaphora resolution, and cross-paragraph consistency. Despite advances in sentence-level simplification for high-resource languages, document-level simplification in morphologically rich, low-resource languages such as Estonian remains largely unexplored. This study presents a comprehensive evaluation of five state-of-the-art multilingual large language models (LLMs) for document-level simplification in Estonian. Three prompting strategies are examined: single-pass generation, pipeline-based modular agents, and guideline-augmented pipelines. The evaluation framework integrates automatic metrics assessing readability, semantic preservation, and discourse coherence, alongside a structured manual annotation protocol. The findings indicate that Gemini-2.0 and LLaMA-3.3 produce outputs with near-native fluency and strong meaning preservation, whereas other models display notable grammatical and semantic limitations. This work contributes novel document-level coherence metrics, evidence-based prompting strategies, and publicly available resources for reproducibility.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c2dab10e-5a5a-4

---

### 7. ECHO: Embodied Camera Observations of Human Object Carrying

- **ArXiv ID**: [2610.10438v1](https://arxiv.org/abs/2610.10438v1)
- **作者**: Xuefei Sun, Lorin Achey, Kali Hamilton, Alberto Speranzon, Gregory Grebe...
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2610.10438v1](https://arxiv.org/pdf/2610.10438v1)
- **相关度评分**: 10/10

#### 英文摘要

Embodied and assistive agents must do more than recognize objects: they must reason about where an object belongs given the layout of an environment and the habits of the people who live in it. Progress on this problem has been limited, in part because no dedicated benchmark or dataset exists to define and evaluate it. Existing RGB-D scan datasets reconstruct static rooms without human activity, while human-object-interaction datasets capture motion without a navigable, fully reconstructed scene or a ground-truth notion of an object's natural destination. We introduce contextual object placement as a benchmark task: predicting an object's destination during an observed object-carrying episode. To support this task, we present Embodied Camera observations of Human Object carrying (ECHO), a large-scale synthetic dataset that pairs dense RGB-D scans of indoor scenes with recordings of an embodied human carrying everyday objects to context-appropriate destinations. ECHO is the first publicly available dataset to combine reconstructed scenes, human activity, natural language, and contextual-placement annotations. It comprises 3,805 human-annotated episodes across 159 floors of 115 HM3D scenes, involving 198 distinct objects. Each floor includes a complete RGB-D scan with human-annotated room labels and a surface list. Each episode provides synchronized RGB-D encounter clips; 6-DoF camera, human, and object trajectories; start and destination surfaces; an action caption; and a human-written context: a single sentence describing the inhabitant's routine that implies the destination without naming it. We evaluate contextual object placement using input-masked probes and an end-to-end baseline. Results show that no single input modality is sufficient, highlighting the need to jointly reason over scene structure, human activity, and contextual knowledge.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 86f6cb82-8ebb-4

---

### 8. SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions

- **ArXiv ID**: [2610.10407v1](https://arxiv.org/abs/2610.10407v1)
- **作者**: Yizhen Xie, Mengyang Liu
- **发布时间**: 2026-10-08
- **分类**: cs.AI, cs.LG, q-fin.PM
- **PDF**: [https://arxiv.org/pdf/2610.10407v1](https://arxiv.org/pdf/2610.10407v1)
- **相关度评分**: 10/10

#### 英文摘要

As option markets grow and AI advances, agentic systems for option trading are gaining increasing attention. Language-model-based agents can reason over contextual information such as news, but option trading presents a particularly challenging decision problem: a single stock can have thousands of contracts, and the agent must decide both which contracts to trade and how to combine them. Existing approaches often sidestep this complexity by restricting the policy to a fixed strategy structure, such as a straddle, limiting their ability to switch strategies as market conditions change. We present SOTA (Stock Options Trading Agents), an agentic trading framework for structured option-strategy selection. SOTA abstracts the large option universe into strategy-level decisions while deterministic resolvers handle portfolio implementation. We develop SOTA by post-training Qwen3.8-27B with supervised fine-tuning followed by reinforcement learning. SOTA is evaluated on options on nine large-cap U.S. equities and SPY against rule-based and machine-learning strategy selectors in the same trading environment. Over a six-month out-of-sample period, SOTA earns an 18.3% total return with a Sharpe ratio of 1.60 and a maximum drawdown of 8.96%. We also document an asymmetric role of news: news improves frontier-teacher trajectories, but retaining news during reinforcement learning reduces out-of-sample return from 18.3% to -2.7%.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 348e82a5-a17a-4

---

### 9. TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity

- **ArXiv ID**: [2610.10374v1](https://arxiv.org/abs/2610.10374v1)
- **作者**: Chengwei Shi, Yunnong Chen, Tingting Zhou, Qiang Lu, Shiyu Yue...
- **发布时间**: 2026-10-08
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.10374v1](https://arxiv.org/pdf/2610.10374v1)
- **相关度评分**: 10/10

#### 英文摘要

A key challenge for multimodal large language models (MLLMs) is moving beyond visual recognition to constraint-aware cross-modal reasoning. This involves combining visual cues with information from other modalities to understand elements' relationships under domain-specific rules. This challenge is acutely evident in industrial design-to-code (D2C), which converts user interface (UI) designs into code and requires MLLMs to connect design images with disorganized layer metadata, infer component and layout implementation requirements, and realize them in code under target-library constraints. However, these capabilities remain insufficiently evaluated in realistic industrial settings. To fill this gap, we present TaoD2C-Bench, a benchmark for evaluating MLLMs' ability to generate UI code that satisfies implementation requirements in industrial applications. The TaoD2C dataset consists of 2,861 production designs from 17 commercial platforms with 97,652 expert annotations across four categories: Component, Group, Alignment, and Position. These annotations distinguish required constraints from permitted implementation choices. TaoD2C-Bench defines three tasks: end-to-end UI code generation, requirement inference, and requirement realization. Evaluating eight MLLMs reveals substantial gaps in generating UI code that satisfies implementation requirements, alongside distinct performance profiles in inference and realization. We further show that MLLMs' visual reconstruction ability does not necessarily imply an ability to generate code that meets these requirements. We release TaoD2C to support research on industrial UI code generation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5d51ab2a-886a-4

---

### 10. QuSema: Detecting Silent Bugs in Quantum Libraries via Quantum-knowledge-enhanced Agents

- **ArXiv ID**: [2610.10258v1](https://arxiv.org/abs/2610.10258v1)
- **作者**: Yujin Song, Kaining Zhang, Qixin Zhang, Shuai Wang, Pingchuan Ma...
- **发布时间**: 2026-10-07
- **分类**: cs.SE, cs.AI, quant-ph
- **PDF**: [https://arxiv.org/pdf/2610.10258v1](https://arxiv.org/pdf/2610.10258v1)
- **相关度评分**: 10/10

#### 英文摘要

Quantum libraries are now critical infrastructure for quantum algorithm development, yet their correctness remains difficult to test. Existing testing techniques mainly rely on failure-based or comparison-based oracles, exposing bugs only when executions fail, violate runtime checks, or disagree with another implementation. Their applicability is limited when suitable execution-based oracles are unavailable, leaving some silent bugs undetected. Such missed bugs can produce incorrect results that propagate into experimental conclusions, simulation studies, and algorithmic designs. Here we present QuSema, an autonomous testing agent for finding silent bugs in quantum libraries. QuSema uses constraints from quantum semantics and documentation as a source-level semantic oracle to assess whether implementation logic can produce invalid outputs from valid inputs. It operates through an agentic loop that repeatedly inspects library API documentation and source code, reasons about the intended behavior of quantum operations, identifies potential semantic deviations, and validates them by generating executable tests through library APIs. Guided by quantum-domain reasoning, QuSema turns high-level behavioral mismatches into concrete, user-triggerable bug reports, enabling it to uncover non-crash defects. We implement QuSema for Qiskit and PennyLane. On a benchmark of 20 historical silent bugs, QuSema achieves higher mean bug relocation counts than Claude Code and Codex, with the DeepSeek configuration costing less than Claude Code. QuSema also discovers 40 previously unknown bugs confirmed by the developers, including 30 silent bugs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1c09b509-323b-4

---

### 11. OOM-RL II: Reality Is an Oracle, Not a Debugger Provenance-Constrained Diagnosis in Continually Evolving Agent-Engineered Systems

- **ArXiv ID**: [2610.10256v1](https://arxiv.org/abs/2610.10256v1)
- **作者**: Kun Liu, Liqun Chen
- **发布时间**: 2026-10-07
- **分类**: cs.AI, cs.SE, q-fin.PM
- **PDF**: [https://arxiv.org/pdf/2610.10256v1](https://arxiv.org/pdf/2610.10256v1)
- **相关度评分**: 10/10

#### 英文摘要

Reality may establish that an outcome occurred without identifying which evolving procedure produced it or why. This distinction matters in production ML systems whose code, configuration, and artifacts change while external feedback accumulates. We examine it in a human-directed, agent-engineered quantitative trading system, using oracle to mean an external source of realized outcomes rather than a complete correctness specification. Across one year, the account gained and outperformed a broad market index, while annual alpha was not statistically distinguishable from zero under the main retrospective specification. Retrospectively selected subperiods include adverse relative performance and conditional candidate-level weakness under declared approximate references. Engineering records document changes during the episode, and complete recommendation-to-runtime binding is unavailable. The archive does not establish a common frozen instance or a unique cause. The case motivates an outcome--diagnosis gap: outcome evidence, evaluated-object identity, and causal explanation support distinct claims. We distinguish frozen instances, pre-specified adaptive procedures, and ad-hoc development; organize archive-relative claim identifiability and an evidence hierarchy; and propose a prospective production-binding protocol. An illustrative compatible-history example shows how factual binding can resolve a recommendation's referent without supplying its counterfactual effect. The protocol is proposed rather than prospectively validated. External feedback constrains outcome claims, while provenance and additional identification structure determine the resolution of diagnosis.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a5b2abf7-cac3-4

---

### 12. Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming

- **ArXiv ID**: [2610.10184v1](https://arxiv.org/abs/2610.10184v1)
- **作者**: Ángel Sánchez-Fernández, Javier Pernas-Álvarez, Diego Crespo-Pereira
- **发布时间**: 2026-10-07
- **分类**: cs.AI, cs.SE
- **PDF**: [https://arxiv.org/pdf/2610.10184v1](https://arxiv.org/pdf/2610.10184v1)
- **相关度评分**: 10/10

#### 英文摘要

Developing optimization models for production scheduling requires substantial expert effort. Research on large language models (LLMs) has followed two directions: specialized approaches for automated modeling, mostly for mixed-integer linear programming, which often rely on dedicated training or problem-specific architectures that limit industrial deployment; and agentic artificial intelligence for operational decision support, which generally assumes that the optimization model already exists. This study bridges both directions by assessing whether general-purpose LLMs, orchestrated as agents without task-specific training, can formulate and implement constraint programming models from natural-language problem descriptions. Singleagent and multi-agent architectures are integrated with a Model Context Protocol server that provides context-aware retrieval of solver documentation to mitigate hallucinations during implementation. Both are compared with a direct LLM baseline on six industry-oriented problems covering flow-shop, job-shop, flexible job-shop and resource-constrained warehouse scheduling, using three LLMs and assessing modeling accuracy, execution success, latency and token consumption. Formulation proves largely within reach of current LLMs, whereas implementation is the main barrier. The multi-agent workflow raises the share of scripts that run correctly as generated from 14.8% with a direct LLM call to 59.3%, reaching 80.6% on the four less complex problems, while tightly coupled intralogistics models remain an open challenge.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 357a56ba-8e11-4

---

### 13. Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora

- **ArXiv ID**: [2610.10170v1](https://arxiv.org/abs/2610.10170v1)
- **作者**: Andrey Kuehlkamp, Priscila Correa Saboia Moreira, Samuel Rund
- **发布时间**: 2026-10-07
- **分类**: cs.IR, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.10170v1](https://arxiv.org/pdf/2610.10170v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation systems increasingly rely on document-structure treatments: structure-aligned chunking, LLM-generated chunk contexts, heading-path metadata, and hierarchical two-stage retrieval. Separate studies support each on different corpora, embedders, and metrics, and none control for a shared confound: any text prepended to a chunk perturbs its embedding. We present a mechanism-isolating ablation testing all four treatments under one protocol, matching chunk sizes across conditions and adding a semantically null placebo---heading paths that are structurally valid but shuffled across documents. We score retrieval with a coverage-aware nDCG and test four pre-registered contrasts via document-clustered bootstrap with Holm correction, on two distant corpora: 200 Wikipedia Featured Articles (951 queries) and 1,585 QASPER papers (4,303 questions). Organization helps, and the cause is content, not tokens: structure-aligned chunks with real heading paths beat contextualized fixed windows (+0.022 / +0.012 cov-nDCG@10) and the placebo (+0.010 / +0.016). Naive two-stage hierarchical retrieval hurts (-0.033 / -0.015), traceable to first-stage section recall. Gold structure beats LLM-induced structure on Wikipedia but not on QASPER. Effects are small ($dz$ 0.06-0.11) but Holm-significant and consistent across corpora.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a18549ce-da7e-4

---

### 14. Tetris3D: 3D Scene Generation With Objects That Fit Together

- **ArXiv ID**: [2610.10539v1](https://arxiv.org/abs/2610.10539v1)
- **作者**: Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee, Kyehong Park, Seungryong Kim
- **发布时间**: 2026-10-08
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.10539v1](https://arxiv.org/pdf/2610.10539v1)
- **相关度评分**: 10/10

#### 英文摘要

We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, we explicitly condition the generation of each object on the geometry of surrounding objects and their physical relationships, guiding its shape and pose to remain geometrically and physically plausible within the scene. Moreover, we introduce ComOb, a physics simulation-based dataset of 1.2M scenes featuring physical interactions across diverse object categories, with per-object meshes and pairwise physical relation annotations. Comprehensive experiments on synthetic and realworld scenes show that Tetris3D recovers coherent object shapes and poses even when interacting regions are occluded, and achieves state-of-the-art performance in both generation quality and physical stability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 326eb6fc-3112-4

---

### 15. Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos

- **ArXiv ID**: [2610.10538v1](https://arxiv.org/abs/2610.10538v1)
- **作者**: Shravan Chaudhari, William Paul, Suchi Saria, Rama Chellappa, Homanga Bharadhwaj
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.AI, cs.RO
- **PDF**: [https://arxiv.org/pdf/2610.10538v1](https://arxiv.org/pdf/2610.10538v1)
- **相关度评分**: 10/10

#### 英文摘要

As we move through the world and carry out everyday tasks, we encounter objects that may become relevant only later. We are capable of recalling where we left something or what was inside a container, even without knowing we would need it later. Here, we study how an embodied assistant can build a similar memory from egocentric videos, by observing a person's day-to-day activities. We present Ledger, a persistent 3D object memory that combines object locations, their histories, and contextual descriptions. It associates observations across the recording and retains objects after they leave the view, including those the person never touches. It clusters each object's observations by resting locations and records a move only after repeated evidence, reducing the effect of localization noise. Short descriptions preserve details such as an object's contents or supporting surface. It saves these records to later answer spatial questions without having to access the original images or video. Our memory raises HD-EPIC accuracy from 29.7% to 42.6%, UCS-Bench accuracy from 33.8% to 38.5% and localizes Ego4D objects with a 0.99 m median error on returned predictions. Our analyses identify complementary roles for temporal persistence, contextual descriptions, and retrieval. Our study on 100 stitched streams of multiple scenes each further exposes failures in both retrieval and construction. Per-scene construction partially recovers the performance lost across scene changes compared to that of single scene streams.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a9ac6cc6-5e6a-4

---
