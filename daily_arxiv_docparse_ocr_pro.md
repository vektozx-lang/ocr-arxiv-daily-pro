# OCR arXiv Daily Pro — 2026-11-03

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-02 09:10 - 2026-11-03 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0ee1110d-985f-4

---

## 📄 论文详情

### 1. ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting

- **ArXiv ID**: [2611.03339v1](https://arxiv.org/abs/2611.03339v1)
- **作者**: Yakoub Bazi, Sarah Alsaleh, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Mansour Zuair
- **发布时间**: 2026-11-02
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.03339v1](https://arxiv.org/pdf/2611.03339v1)
- **相关度评分**: 10/10

#### 英文摘要

Geospatial text spotting involves locating and transcribing geographic labels, such as road names, district names, and landmarks, in raster maps. These labels are often small, densely arranged, and arbitrarily oriented. Although Arabic text recognition has been studied extensively in documents and natural scenes, Arabic geospatial text spotting remains underexplored. We introduce ARABGEOTEXT, an Arabic-centric benchmark covering 970 geographic locations in Riyadh and Jeddah, with 17,875 manually annotated text instances per view type. For each location, we pair an OpenStreetMap (OSM) rendering with a composite created by overlaying that rendering on the corresponding remote sensing (RS) imagery. The paired views preserve label content and pixel geometry, allowing evaluation across different backgrounds. Geographic partitions support in-city and city-disjoint evaluation of detection, recognition, and end-to-end spotting. Experiments with direct Qwen3.5-4B spotting show difficulties in recovering all labels within a tile. We therefore propose a tool-augmented vision-language framework that combines YOLO26 localization and crop rectification with Qwen3.5-4B recognition adapted through low-rank adaptation (LoRA). The framework outperforms direct LoRA-adapted Qwen3.5-4B spotting across both image views and test cities. With localization held fixed, reader adaptation further improves recognition over the pretrained zero-shot reader. The dataset and code will be made publicly available at https://github.com/yakoubbazi/ArabGeoText.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9cca0423-0e59-4

---

### 2. DR Pixel: Page-Native Deep Research with Vision-Language Models

- **ArXiv ID**: [2611.03097v1](https://arxiv.org/abs/2611.03097v1)
- **作者**: Tiansheng Hu, Yichuan Wang, James V. Talwar, Nicholas Tomlin, Chen Zhao...
- **发布时间**: 2026-11-02
- **分类**: cs.CV, cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.03097v1](https://arxiv.org/pdf/2611.03097v1)
- **相关度评分**: 10/10

#### 英文摘要

Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep research: directly retrieving and reasoning over rendered document page images. We introduce DR Pixel, the first open-source end-to-end multimodal DR agent that uses rendered page images as its sole retrieval and reasoning unit, operating over a corpus of 1.06M pages. To evaluate this setting, we construct DRPixelBench, a benchmark on scientific papers requiring reasoning over text, figures, tables, and equations. Surprisingly, page-native DR already works well without training, outperforming OCR-based baselines across state-of-the-art models like GPT-5.4, Gemini-3.5-Flash, and Qwen3.6-27B, while requiring fewer tool calls. We next turn to DR training. A key challenge is that teacher trajectories for agentic supervised finetuning are noisy, mixing critical reasoning and action steps with redundant or failed attempts. To address this, we introduce counterfactual credit reweighting, a fine-grained credit assignment method that weights individual reasoning and action steps by their counterfactual contribution to the final answer. Our training improves retrieval recall by about 15 points and final accuracy by over 10 points on DRPixelBench, and likewise outperforms the untrained baseline on four existing benchmarks. On out-of-distribution ViDoRe-V3, DR Pixel comes within 1.8 points of an oracle that is given the gold pages directly. Our results suggest that the conventional OCR-then-retrieve pipeline is not only unnecessary but suboptimal: directly retrieving and reasoning over visual document pages makes complex DR both more effective and more efficient.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e8db24d6-0c8c-4

---

### 3. Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents

- **ArXiv ID**: [2611.03384v1](https://arxiv.org/abs/2611.03384v1)
- **作者**: Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez, Ethan Setrouk, Chamyl Saadi...
- **发布时间**: 2026-11-03
- **分类**: cs.AI, q-fin.ST
- **PDF**: [https://arxiv.org/pdf/2611.03384v1](https://arxiv.org/pdf/2611.03384v1)
- **相关度评分**: 10/10

#### 英文摘要

Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introduce PROMOTE, a protocol that assigns every candidate predictable testing wealth at birth and accumulates a cost-aware e-process only from subsequent returns. If lifetime allocations sum to at most one, a weighted Ville argument bounds the probability of ever promoting a rule whose declared bounded net score has always had nonpositive conditional mean. The result permits dependent candidates, adaptive births, and indefinite monitoring. We audit the implementation in two settings. A retrospective pseudo-out-of-sample replay contains 24 panel--rule hypotheses, 3,000 shared-sign null paths, injected alternatives, and public ETF and industry data. Repeated unadjusted tests produce a family crossing in 94.5% of null paths, versus 0.0% for PROMOTE; at a 15-bp aligned ETF-component perturbation, PROMOTE has 70.1% target power and median crossing session 2,327. A separate exact mean-zero experiment lets an agent select candidate identities and birth times from past scores; the funded gate has 1.77% false-family crossings across 3,000 programs. The market replay produces zero promotions after costs. The certificate controls historical false promotion under the declared null; it is not a certificate that an earlier edge remains profitable at deployment. AI-use disclosure. Generative AI tools, including OpenAI Codex, assisted manuscript preparation. For this preprint version, Codex assisted with LaTeX editing, author and venue metadata, compilation, and layout checks.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 20a1962d-48ee-4

---

### 4. Specificity Bias and the Wikipedia Paradox: An xAI Analysis of AI Text Detectors under Domain Shift

- **ArXiv ID**: [2611.03280v1](https://arxiv.org/abs/2611.03280v1)
- **作者**: Nico Morloher, Johannes Reschke, Mohamed Mady
- **发布时间**: 2026-11-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03280v1](https://arxiv.org/pdf/2611.03280v1)
- **相关度评分**: 10/10

#### 英文摘要

The widespread adoption of Large Language Models (LLMs) demands reliable detection of human-authored versus synthetic text. However, current Transformer-based detectors often experience severe performance degradation during domain shifts and operate as opaque classifiers. This paper investigates the robustness and interpretability of fine-tuned Transformer models (DistilBERT, RoBERTa) by evaluating them against a custom out-of-distribution (OOD) dataset of hyper-local news synthesized via open-source LLMs (Llama 3, Mistral, Gemma). To analyze model decision boundaries, we apply a tripartite Explainable AI (xAI) framework using SHAP. Our analysis reveals three key phenomena: First, detectors often rely on a "Call-to-Action" syndrome inherent to instruction-tuned LLMs rather than generic machine text. Second, we observe a "Specificity Bias," where LLMs successfully bypass detection by hallucinating specific named entities and mimicking conversational imperfection. Finally, we illustrate the "Wikipedia Paradox," wherein formal, objective human writing is frequently misclassified as AI due to its low statistical burstiness. These findings demonstrate that purely statistical detection paradigms face systematic limitations in highly structured human domains, emphasizing the critical need for semantically-aware, interpretable detection architectures.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c273bd7a-fbf4-4

---

### 5. CoLa3D: Composable Latent 3D Decomposition

- **ArXiv ID**: [2611.03533v1](https://arxiv.org/abs/2611.03533v1)
- **作者**: Xudong Cai, Yongcai Wang, Deying Li, Chuanxia Zheng
- **发布时间**: 2026-11-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.03533v1](https://arxiv.org/pdf/2611.03533v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce CoLa3D, a simple and effective model for composable 3D scene decomposition that, given a single whole-scene latent from either a single image or an existing scene mesh as input, directly outputs a set of object meshes with consistent spatial layout that can be assembled back into a coherent scene. CoLa3D introduces a novel paradigm for 3D scene decomposition within a shared whole-scene latent, unlike alternatives that perform per-object generation in canonical spaces and then glue the objects back together with fragile pose and scale estimation. The network is a lightweight, flexible, and scalable query-based transformer that accepts various types of queries, including 2D masks, 3D points, and learnable queries, and learns to decompose the scene into objects in a compact latent space. On both synthetic and real-world datasets, CoLa3D achieves state-of-the-art performance on composable 3D scene decomposition, substantially improving global scene-level consistency and object-level quality while running 2 times faster and using less than 1% of SAM 3D's training data. Visible depth on par with MoGe2 further confirms that latent decomposition preserves accurate visible scene geometry while producing physically complete, decomposable object meshes.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8291e683-ec9e-4

---

### 6. Grading the Unannotated: Insights from the WorkRB Skill Extraction Challenge at RecSys-HR 2026

- **ArXiv ID**: [2611.03525v1](https://arxiv.org/abs/2611.03525v1)
- **作者**: Warre Veys, Luis Gasco, Jens-Joris Decorte
- **发布时间**: 2026-11-03
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.03525v1](https://arxiv.org/pdf/2611.03525v1)
- **相关度评分**: 10/10

#### 英文摘要

Skill extraction benchmarks score models against a few human-annotated positives and treat every other skill in the vocabulary as equally wrong. At the scale of ESCO (13,939 skills) this binary view can reward models that rank the annotated positive high for the wrong reason, and hides semantically nonsensical predictions. The WorkRB Challenge at RecSys-HR 2026 replaces it with graded relevance: every candidate skill in a model's ranking window carries a 0 to 4 grade, and the leaderboard scores nDCG@100 against these grades. Since ternary judgements proved too coarse for objective annotation, relevance is decomposed into a cascade of four binary questions (same domain, activity mentioned, right granularity, replacement of a gold positive) that a smaller LLM judge can answer reliably; the labels are validated with blind human and frontier-model re-annotation. This paper documents the annotation methodology, the construction of five benchmark datasets (four with vacancy sentences as queries, one with lexically distant skill surface forms), the validation of the LLM cascade, and insights from the submissions. The field converged on multi-stage retrieve-and-rerank pipelines, whose gains come from clearing nonsense out of the ranking window rather than finding more positives: at the top of the leaderboard, the graded ordering is uncorrelated with what binary evaluation would have said. Graded labels expose much bigger gaps between top submissions and baselines than binary evaluation does, and show that semantic-understanding skill recommendation is still wide open. The clear next direction is bringing efficiency back: every submitted system we could size uses at least 42x, typically several hundred times, more parameters than the baselines it beats.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0ad54cd8-e251-4

---

### 7. LLMs Depend on Specialist Tools for Out-of-Distribution Generalization in MS/MS Structural Elucidation

- **ArXiv ID**: [2611.03308v1](https://arxiv.org/abs/2611.03308v1)
- **作者**: Gabriel Asher, Cailum M. K. Stienstra, Tomo Oga, Devesh Shah Antonio H. de O. Fonseca, Niall O'Connor...
- **发布时间**: 2026-11-02
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03308v1](https://arxiv.org/pdf/2611.03308v1)
- **相关度评分**: 10/10

#### 英文摘要

A frontier language model was recently reported to solve 1D NMR structural elucidation without tools. We ask whether this capability transfers to tandem mass spectrometry (MS/MS) in the de novo setting, where the model must propose a structure directly from the spectrum without a candidate list or reference library. To separate reasoning from recall, we build a 100-analyte benchmark from MassSpecGym, split by each analyte's textual footprint into in-distribution (well documented in literature) and out-of-distribution (essentially undocumented) arms. We hold the model, harness, and output format fixed and vary only the LLM's access to domain-specific tools. Without tools, a frontier LLM reaches 52% Top-1 accuracy in-distribution but only 2% out-of-distribution. Only access to de novo structure generators improves out-of-distribution accuracy, raising it to as much as 38% Top-1, and the resulting agent outperforms the standalone de novo models both in and out of distribution. These results suggest that LLMs are not effective at de novo MS/MS structural elucidation on their own, and that further gains depend on the specialist tools available to the agent rather than on the LLM itself.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 13c32ae6-e9c6-4

---

### 8. ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents

- **ArXiv ID**: [2611.03238v1](https://arxiv.org/abs/2611.03238v1)
- **作者**: Daiqiang Li, Jingyi Peng, Rui Hu, Jia Li, Xuyang Liu...
- **发布时间**: 2026-11-02
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.03238v1](https://arxiv.org/pdf/2611.03238v1)
- **相关度评分**: 10/10

#### 英文摘要

Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches between documented and deployed software versions and differences in scope between documentation coverage and task requirements. We introduce ScienceCUA, a two-stage framework combining resource-to-skill construction with execution-guided skill evolution. First, ScienceCUA identifies tasks supported by the software from its documentation, infers operational trajectories, and generalizes them into reusable Skills. Command catalogs, syntax constraints, and shortcuts are organized separately as References for on-demand lookup. Then, ScienceCUA uses execution feedback to drive skill self-evolution by contrasting successful and failed trajectories for the same task, identifying deficiencies, revising existing skills or adding new ones, and updating the skill library only after repeated validation in real environments. To enable reliable evaluation without benchmark noise or task leakage, we introduce two improved benchmarks. ScienceBoard-Verified provides an audited and corrected basis for measuring task performance, while ScienceBoard-VE separates skill evolution from final testing through disjoint evolution and test tasks and further supports native-agent evaluation. Experiments show that the initial Skills and References improve average task success rate by up to 7.23 percentage points over the base model, while skill self-evolution increases the total gain over the baseline to as much as 17.12 percentage points. ScienceCUA turns software documentation into an evolving set of executable skills and queryable references, offering a practical way for general-purpose agents to use scientific software reliably and at scale.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 23013786-cf80-4

---

### 9. Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions

- **ArXiv ID**: [2611.03179v1](https://arxiv.org/abs/2611.03179v1)
- **作者**: S. M. Mahbub Uddin Ahmed, Abdullah Al Musaddiq
- **发布时间**: 2026-11-02
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03179v1](https://arxiv.org/pdf/2611.03179v1)
- **相关度评分**: 10/10

#### 英文摘要

People often attach instructions to their search queries, asking for pages written for beginners, documents in a certain language or official sources only. Most rerankers were trained to judge topical relevance and treat such instructions as a few extra words. On the InfoSearch benchmark, even GPT-4o used as a list-wise reranker reaches an average WISE (Weighted Instruction Sensitivity Evaluation) of only 33.5. We present DMReranker (Decision-Model Reranker), a zero-shot reranker that splits an instructed query into a topic and a short list of typed clauses. A small judge model answers one narrow question per clause, and the answer probabilities are multiplied into a single score. Nothing is trained, and the configuration was frozen before the test runs. Reranking the same top-100 candidates as the published baselines, DMReranker reaches a macro WISE of 50.9 over all six InfoSearch dimensions while keeping original-mode nDCG@10 at 82.9. It trails GPT-4o on the stricter SICR (Strict Instruction Compliance Ratio) metric, 19.2 against 32.1. We show that this gap follows from how a product of probabilities behaves when SICR compares raw scores across runs. Computed from ranks, our SICR is 67.0. On the same judge, splitting the instruction raises WISE from 32.9 to 47.6 over a single combined question, while raw-score SICR falls. Scoring all six dimensions cost about $10 at list price.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e6a5f733-79af-4

---

### 10. CoworkOS:Scaling Agent Coworkers for Real-world Automation

- **ArXiv ID**: [2611.03178v1](https://arxiv.org/abs/2611.03178v1)
- **作者**: Jiajie Jin, Guanting Dong, Chengjun Pan, Xin Deng, Zhuohui Sheng...
- **发布时间**: 2026-11-02
- **分类**: cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03178v1](https://arxiv.org/pdf/2611.03178v1)
- **相关度评分**: 10/10

#### 英文摘要

Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decision-making over long horizons, a combination that remains an open challenge. We introduce CoworkOS, a general-purpose harness for long-horizon work that separates task strategy from execution management: the model decides actions, delegation, and acceptance, while the runtime maintains state and feedback. Its three-layer architecture enables direct execution or delegation to Subagents, synchronously or asynchronously, under stable responsibilities. Through a shared application layer, humans and agents inspect and revise the same evolving documents, presentations, CAD models, and Blender scenes, so human-in-the-loop participation can enter both through conversation and through direct modification of the work itself. To sustain continuity across agents and sessions, CoworkOS further introduces hierarchical workspaces and persistent semantic memory, so working files, key decisions, and long-running Job logs remain shareable, reusable, and resumable after interruption. Across 12 benchmarks and 6 categories of real-world applications, CoworkOS proves highly competitive with frontier agent applications such as Codex and DeepSeek Harness. As a sustained-work case study, CoworkOS uses GLM-5.3 as its backbone to conduct RSI-driven automated post-training on Qwen3.6-35B-A3B. Over five rounds, the model's average score across eight benchmarks rose from 33.19 to 42.95 (+9.76). Looking ahead, we believe CoworkOS opens a meaningful path toward general cowork-agent intelligence.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3e4d3a27-beec-4

---

### 11. Beyond Surface Metrics: Multi-Condition Requirements in Enterprise Maintenance and AI Coding Benchmarks

- **ArXiv ID**: [2611.03162v1](https://arxiv.org/abs/2611.03162v1)
- **作者**: Heeyong Eun
- **发布时间**: 2026-11-02
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.03162v1](https://arxiv.org/pdf/2611.03162v1)
- **相关度评分**: 10/10

#### 英文摘要

Repository-level AI coding benchmarks measure task success but do not directly capture the conditions required for software maintenance completion. We study multi-condition fulfillment, where a maintenance task must satisfy multiple operational conditions, sometimes with directional dependencies. Using a fixed 18-criterion taxonomy, we analyze 2,925 Apache Fineract issues and 944 tasks from SWE-bench Pro, SWE-PolyBench Java, and SWE-EVO. We examine condition breadth, corpus-level co-occurrence, and source-grounded directional requirement relationships. Among 1,177 benchmark task pairs matched on issue classification, modified-file count, and code churn, the mean fulfillment-set Jaccard distance is 0.8138, and 57.4% have disjoint condition sets. Condition count alone does not explain this contrast: SWE-bench Pro averages 2.47 conditions per task, versus 1.78 for Fineract. Temporal (B4) and numerical (B2) conditions have a phi coefficient of +0.430 in Fineract versus -0.013 in the pooled benchmark corpus. Among temporally tagged tasks, numerical conditions are also specified in 48.85% (254/520) of Fineract cases versus 5.81% (5/86) of benchmark cases. We document 16 directional relationships in Fineract requirements involving time, calculation, and state preservation, and inspect four benchmark cases to illustrate how relevant conditions appear in evaluation assertions. These examples do not quantify benchmark-wide oracle omissions. The results show that similar surface task profiles can mask substantially different fulfillment-condition sets. We recommend reporting condition breadth, co-occurrence, and directional relationships separately. The corpus comparisons are descriptive and may reflect domain differences; they do not establish causality or production failure rates.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 274bb184-33a0-4

---

### 12. Visual-to-Executable Procedural Reconstruction of Buildings

- **ArXiv ID**: [2611.03143v1](https://arxiv.org/abs/2611.03143v1)
- **作者**: Zichong Zhu, Zhihao Liu, Andrei Sharf, Zhanglin Cheng
- **发布时间**: 2026-11-02
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.03143v1](https://arxiv.org/pdf/2611.03143v1)
- **相关度评分**: 10/10

#### 英文摘要

Procedural modeling offers compact, editable, and reusable representations for architectural content, but building such models still depends heavily on manually authored grammars. We study image-based procedural building reconstruction from in-the-wild images, with the goal of recovering an executable procedural description that can be instantiated as an editable 3D building asset. Because a single image provides only partial and view-dependent evidence, we focus on recovering the dominant visible facade(s) and attach the recovered facade program to a simple mass model for building-level instantiation. Our method decomposes this task into two structured prediction stages. First, a Global Structure Layout Tree recovers facade-scale split-and-repeat organization through a fine-tuned layout model with render-guided visual-symbolic reflection. Second, a Component Parameterization schema maps representative facade tiles to structured procedural attributes for local architectural component synthesis. These two representations are then deterministically compiled into executable Computer Generated Architecture (CGA) programs, avoiding the brittleness of direct low-level program generation. Experiments show that the proposed framework handles both regular facades and challenging in-the-wild images, while maintaining high structural consistency, procedural executability, and fine-grained architectural detail. The recovered programs further enable controllable and reusable 3D building asset generation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bb97a9ff-7eba-4

---

### 13. Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime

- **ArXiv ID**: [2611.03526v1](https://arxiv.org/abs/2611.03526v1)
- **作者**: Abdellah Rahmani, Sean McLeish, Ang Li, Sanae Lotfi, Pascal Frossard...
- **发布时间**: 2026-11-03
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03526v1](https://arxiv.org/pdf/2611.03526v1)
- **相关度评分**: 10/10

#### 英文摘要

Computer programmers chain together the same reusable computational primitives, for example, conditional statements or loops, but in different orders to implement different algorithms. In contrast, existing language model architectures always execute their layers in the same order. We introduce Library of Layers (LoL), an architecture that dynamically orders its layers during inference to solve the problem at hand. LoL has a single hyperparameter, the size of its global library of transformer blocks, that allows it to transition seamlessly between parameter reuse and sparsity, generalizing the parameter-efficiency and FLOPs-efficiency tradeoffs of dense, depth-recurrent, and mixture of experts architectures in one unified family. We show that LoL achieves competitive performance with all three above baselines when pretrained on text data. On synthetic sudoku and maze data, we observe that the model employs distinct layer orderings to implement different solution strategies, and we can intervene on routing to force a model to apply a specific solution strategy to a problem instance. In a multilingual natural language setting, we find that LoL chooses different layer order patterns based on language and script. Similarly, we train LoL on safety data and fit probes to its router outputs, finding that these probes distinguish safe from unsafe text with high AUROC. LoL provides a path toward a future in which models dynamically compose their own computational graph, enabling more efficient and controllable reasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9a753fc8-b3fa-4

---

### 14. Steering with Multilingual Lexicons for Sentiment Control in Low-Resource Languages

- **ArXiv ID**: [2611.03317v1](https://arxiv.org/abs/2611.03317v1)
- **作者**: Lucinda Laurent, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto
- **发布时间**: 2026-11-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.03317v1](https://arxiv.org/pdf/2611.03317v1)
- **相关度评分**: 10/10

#### 英文摘要

Activation steering offers a lightweight mechanism for controlling model behavior, but existing methods depend on sentence-level contrastive data that is unavailable for most of the world's languages. We show that multilingual sentiment lexicons are a viable substitute across three model families: aggregated multilingual lexicons outperform English-derived steering vectors for mid- and low-resource languages, while monolingual lexicons remain stronger for languages a model has specialized in during pre-training. The steering efficacy is mechanistically dictated by both representational density and pre-training priors. Large-magnitude English vectors overwhelm the compact representations of low-resource languages, causing "linguistic collapse." This fragility is mitigated by the norm-dampening of multilingual aggregation. Architectural biases, including bilingual specialization penalty and latent numerical rigidity, also heavily constrain cross-lingual steering responsiveness. Ultimately, our work establishes lexicons as a practical steering signal and offers a comprehensive mechanistic account of cross-lingual steering dynamics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bae8a34c-f723-4

---

### 15. Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations

- **ArXiv ID**: [2611.03647v1](https://arxiv.org/abs/2611.03647v1)
- **作者**: Jason Jingzhou Liu, Tony Tao, Deepak Pathak, Ruslan Salakhutdinov
- **发布时间**: 2026-11-03
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.03647v1](https://arxiv.org/pdf/2611.03647v1)
- **相关度评分**: 10/10

#### 英文摘要

Sensorized human demonstrations offer scalable data for mobile manipulation, but embodiment differences complicate policy learning. We present Pixel-UMI, a pipeline for learning environment-aware whole-body policies from human data. We first introduce Environment-Aware Retargeting (EAR), which combines reconstructed scene geometry with demonstrated head and gripper trajectories to determine robot posture and generate collision-aware joint and base targets. Delay-calibrated action assignment converts these trajectories into actions. However, kinematic differences can leave residual pose errors, creating viewpoint mismatches between human demonstrations and robot observations. We therefore introduce Retargeting-Error-Aware Masking (REAM), which uses these errors during training to reduce reliance on mismatched views at deployment. Finally, because estimated actions cannot fully capture contact-rich interactions, we collect on-policy human corrections through DAgger to improve performance. We evaluate Pixel-UMI on five challenging tasks spanning articulated-object manipulation, deformable-object handling, constrained-space reaching, whole-body collision avoidance, and contact-rich bimanual coordination, achieving 87.0% average task progress. Video results are available at https://pixel-robot.com/pixel-umi

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 25feeb40-7f6e-4

---
