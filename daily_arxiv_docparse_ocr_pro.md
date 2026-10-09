# OCR arXiv Daily Pro — 2026-10-09

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-08 09:10 - 2026-10-09 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 966b7ac0-46a8-4

---

## 📄 论文详情

### 1. From Pixels to Structure: Lightweight Vision-Language Models for Document OCR and Structured JSON Extraction

- **ArXiv ID**: [2610.11818v1](https://arxiv.org/abs/2610.11818v1)
- **作者**: Uddipan Basu Bir, Vincent Christlein, Andreas Maier, Mathias Zinnen
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.11818v1](https://arxiv.org/pdf/2610.11818v1)
- **相关度评分**: 10/10

#### 英文摘要

While massive, closed-source Vision-Language Models (VLMs) set strong benchmarks for document understanding, their dependence on commercial APIs limits adoption in institutional archives due to data autonomy concerns, recurring costs, and the environmental footprint of hyperscale computing. This is especially acute in heritage digitization, where documents include historical handwriting, domain-specific terminology (e.g., jewelry, prehistory, architecture), and non-standard layouts requiring high-dimensional structured extraction. We present a comparative study of eight open-source lightweight VLMs (up to 7B parameters) for Optical Character Recognition (OCR)-to-structure across three university heritage collections. Given a document image, models must extract text and generate schema-compliant JSON, enabling automatic validation and downstream use. We evaluate models under a constraint-aware protocol across zero-shot, few-shot, and fine-tuning settings, measuring extraction fidelity and structured-output quality using Character Error Rate (CER), Approximate Normalized Levenshtein Similarity (ANLS*), and mean Average Precision F1 (mAP-F1). Against a fine-tuning baseline, we further test the independent impact of (i) hyperparameter optimization, (ii) classical image preprocessing (illumination flattening, denoising, and CLAHE), and (iii) multi-stage training. Finally, we analyze the trade-off between dataset-specific fine-tuning and a single multi-dataset checkpoint, where joint training enables one model to operate across collections but can shift performance between datasets. Overall, we show that carefully adapted VLMs with up to 7B parameters can provide a sustainable, private, high-performing alternative to manual transcription or commercial black-box systems, and we offer actionable guidance for heritage institutions seeking institution-controlled OCR-to-JSON extraction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 45323bc2-be76-4

---

### 2. SP-DocReader: Difference-Aware Self-Play for Precise Document OCR

- **ArXiv ID**: [2610.11148v1](https://arxiv.org/abs/2610.11148v1)
- **作者**: Wenjie Liao, Xiaohui Song, Liangjie Zhao, Haonan Lu
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.11148v1](https://arxiv.org/pdf/2610.11148v1)
- **相关度评分**: 10/10

#### 英文摘要

Accurate page transcription remains difficult for vision language models under limited input and training budgets. We present SP-DocReader, a self-play framework for optical character recognition (OCR) that targets residual errors after supervised fine-tuning. Reading Discrepancy Masking aligns reference and generated model tokens through a longest common subsequence, then scores unmatched positions with their full conditioning prefixes. Focused Fidelity Loss adds direct negative log-likelihood supervision at unmatched ground-truth positions. Only the OCR module is trained, while the backbone remains frozen. We derive the combined gradient to distinguish relative score optimization from direct supervision. Compared with SFT-2, SP-DR-3 reduces Vary-600K character error rate on both backbones. On Qwen3-VL-4B, it reduces character error rate by approximately 54 percent and improves DocVQA Average Normalized Levenshtein Similarity (ANLS) by 3.7 points. These results show the value of focusing self-play training on the discrepancies that remain after supervised fine-tuning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e2ac1182-e28e-4

---

### 3. HANS: A Handwritten Answer Sheet Dataset for Noisy Hybrid Document Parsing

- **ArXiv ID**: [2610.12363v1](https://arxiv.org/abs/2610.12363v1)
- **作者**: Xiazhen Wu, Wansong Qin, Yangbin Zheng, Liangda Fang, Zhan Li...
- **发布时间**: 2026-10-09
- **分类**: cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12363v1](https://arxiv.org/pdf/2610.12363v1)
- **相关度评分**: 10/10

#### 英文摘要

Intelligent grading and automated scoring technologies constitute critical infrastructure for smart education. However, existing document parsing and handwriting recognition benchmarks are predominantly designed for well-structured printed documents or isolated mathematical expressions, lacking datasets that capture the complex characteristics inherent to student answer sheets, including multi-line derivation processes, heterogeneous mixtures of text and mathematical formulae, and noise artifacts such as strikethroughs. To address this gap, we introduce HANS, the first dataset explicitly constructed for real-world educational scenarios, encompassing mathematical expressions, natural language text, hand-drawn tables, and diverse noise patterns including corrections and deletions, accompanied by fine-grained annotations that establish a reliable foundation for robust recognition research. Building upon HANS, we propose NA-GOT, an end-to-end framework that achieves two-stage noise suppression through a lightweight noise suppression module operating at the feature level, complemented by a noiseaware attention mechanism incorporated into the decoding stage. Experimental results demonstrate that HANS poses substantial challenges to existing methods, while NA-GOT achieves significant improvements in both accuracy and stability for answer process recognition. The dataset will be made publicly available upon publication.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c4451d0b-fba4-4

---

### 4. EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval

- **ArXiv ID**: [2610.11553v1](https://arxiv.org/abs/2610.11553v1)
- **作者**: Zifei Wang, Wei Wen, Qiang Ji, Qian-Wen Zhang, Ruizhi Qiao...
- **发布时间**: 2026-10-08
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.11553v1](https://arxiv.org/pdf/2610.11553v1)
- **相关度评分**: 10/10

#### 英文摘要

Accurate and scalable visual document retrieval (VDR) requires both fine-grained page understanding and efficient indexing, yet existing approaches struggle to achieve both. OCR-based text retrieval adds preprocessing latency and can lose visual and structural cues needed to understand complex pages. Single-vector vision-language models bypass OCR, but compressing an entire page into one vector limits the granularity of query--document matching. Multi-vector retrievers with MaxSim provide finer interactions, yet demand large indexes and still leave room for accuracy improvements. We argue that overcoming these limitations requires preserving query-relevant page evidence throughout representation learning and index construction. To this end, we introduce \textbf{\textit{EVIE}} (Evidence-Vector-Informed Embeddings), a family of native visual document retrievers integrating three key innovations: (1) Evidence-judged data governance, which uses a multimodal judge to identify answer-bearing positives and filter unreliable negatives. (2) Bidirectional teacher--student learning with symmetric listwise distillation and prefix-based Matryoshka representation learning (Prefix-MRL), enabling one student checkpoint to serve six nested embedding dimensions without re-encoding. (3) Hierarchical agglomerative index compression (HAC), which clusters page tokens with spatial regularization and stores semantic centroids for single-stage MaxSim retrieval. Extensive experiments across 138 tasks from ViDoRe V1, V2, V3, and JinaVDR validate EVIE. EVIE-8B achieves 66.75 nDCG@10 on V3, exceeding the best external baseline by 1.43 points, with a four-suite average of 79.51. EVIE-4.5B with HAC retains 59.58 nDCG@10 at only 3.81 GiB per million pages, reducing vector payload by $128\times$. Together, these results improve the accuracy--storage trade-off for visual document retrieval.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 14094b18-220f-4

---

### 5. ProtoSemImage: Image-Valued Prototypes with Deformable Row Alignment for Interpretable Document Classification

- **ArXiv ID**: [2610.11460v1](https://arxiv.org/abs/2610.11460v1)
- **作者**: Mohammad Zare, Pirooz Shamsinejadbabaki
- **发布时间**: 2026-10-08
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.11460v1](https://arxiv.org/pdf/2610.11460v1)
- **相关度评分**: 10/10

#### 英文摘要

Prototypes in classification models are almost always vectors, and a vector has no readable form. This paper asks what happens when a prototype is an image. Documents give the question a natural form, because a document can be rendered as a multi-channel image in which every token becomes a pixel, so a class representative can take the same shape and the same channel semantics as the inputs it stands for. ProtoSemImage represents each class by one or more visual archetypes: prototype images in a four-channel HSV space whose channels carry named linguistic factors. A Skip-Gram objective learns that color space end to end through a four-dimensional bottleneck, discourse boundary rows become differentiable typed difference rows, and classification reduces to 2D visual template matching: a deformable row alignment between a document image and the archetype bank, in the spirit of dynamic time warping. Because the match is a spatial pattern comparison rather than a linear readout, the model reports where an input departs from its archetype and along which channel, and a generative head decodes each archetype back into text. The image representation works: it beats an otherwise identical model with vector prototypes in all three paired seeds, by between 4.3 and 11.8 points on a ten-class task. The distance-based matching does not. A diagnostic that keeps the representation fixed and swaps only the classifier recovers the sequence baselines, which locates a 20.6-point shortfall in the matching rather than in the color compression, and a benchmark built so that a pair of documents shares a bag of words and differs only in arrangement confirms the layout-preservation it was designed for. We report both directions, because for a representation whose whole purpose is inspect ability, the failure modes are as informative as the gains.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 32376226-2f08-4

---

### 6. WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

- **ArXiv ID**: [2610.12459v1](https://arxiv.org/abs/2610.12459v1)
- **作者**: Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan
- **发布时间**: 2026-10-09
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12459v1](https://arxiv.org/pdf/2610.12459v1)
- **相关度评分**: 10/10

#### 英文摘要

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as \emph{closed-loop task execution in visual world space} and introduce \textbf{WorldGuide}. Given only an initial image and a task goal, WorldGuide predicts an atomic action, generates its corresponding video clip, and uses the generated result to select the next action or terminate. The Planner and Executor are trained on the same step-level procedural demonstrations: the Planner learns to predict the next atomic action or task completion from visual progress, while the Executor is directly trained to realize the predicted actions. Hierarchical visual memory maintains state across long-horizon execution with bounded history token cost. Due to the lack of step-level action-video supervision for joint planner-executor training, we introduce \textbf{WorldGuide Bench}: approximately 59K step-annotated videos across 245 tasks and 27 procedural categories. WorldGuide achieves a 33.33\% Task Success on \textbf{WorldGuide-Bench}, compared with 29.90\% for the strong recent video model MiniMax-H3, even though MiniMax-H3 receives reference action plans, and achieves 47.69\% on \textbf{VideoCraft-Bench} compared with 32.73\% for MiniMax-H3 under goal-only conditioning. These results demonstrate the importance of coupling planning with learned execution for goal-directed procedural video generation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a4afd985-35e9-4

---

### 7. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

- **ArXiv ID**: [2610.12442v1](https://arxiv.org/abs/2610.12442v1)
- **作者**: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
- **发布时间**: 2026-10-09
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12442v1](https://arxiv.org/pdf/2610.12442v1)
- **相关度评分**: 10/10

#### 英文摘要

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but translates depth errors into misplaced content. We ask what a video diffusion model should receive as its condition and propose a lifting-free answer: a learned view synthesizer, an LVSM-style transformer fine-tuned to render the egocentric view directly without depth, point clouds, or reprojection, resolving cross-view correspondence internally. In contrast, its probabilistic mapping averages each region over candidate source locations according to a learned correspondence distribution, preserving structure while fine texture is averaged away. We argue that this trade-off suits a diffusion generator, whose denoising training excels at restoring detail, so an effective condition should prioritize structural alignment over sharpness. This distribution's concentration also yields a per-region confidence, used both to mask low-confidence regions and to guide the generator toward high-confidence areas during early layout-forming denoising steps. Our approach consistently outperforms the state-of-the-art explicit pipeline and generalizes to other datasets without retraining. The synthesizer thus supplies view structure, and the diffusion model its detail.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 27d57ed1-9e6e-4

---

### 8. WOVEN: Weaving Visual World Modeling into Multimodal LLMs

- **ArXiv ID**: [2610.12417v1](https://arxiv.org/abs/2610.12417v1)
- **作者**: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang...
- **发布时间**: 2026-10-09
- **分类**: cs.CV, cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.12417v1](https://arxiv.org/pdf/2610.12417v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a training source and benchmark for visual transition reasoning that organizes transition supervision by scene, action, and reasoning type, using diverse, realistic rollouts from video-pretrained generative models: 36,076 examples across 20 scene types, 5 action types, and 8 reasoning types. We first evaluate 38 frontier MLLMs (e.g., GPT-5.4 and Qwen3-VL-235B-A22B) and find a substantial and systematic deficit: even the strongest models fall far below humans, and the failures recur across model families and persist with scale. We then train MLLMs at multiple scales on WOVEN and find that they learn a shared capability that transfers broadly: training subsets of only about 2,000 items each collectively improve 22 of 26 external benchmarks by up to 27.3 percentage points, and WOVEN data can replace 30-50% of a task's own training data with comparable accuracy. Controlled comparisons further yield a training recipe for visual world modeling, validated prospectively on held-out benchmarks: select supervision by the reasoning operation it teaches rather than by the actions, scenes, or domains it shows, and prefer larger changes to the visual state for robustness. Our work establishes visual transition reasoning as a reusable foundation for systematic visual world-model training in MLLMs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 16505aa7-0caf-4

---

### 9. ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills

- **ArXiv ID**: [2610.12403v1](https://arxiv.org/abs/2610.12403v1)
- **作者**: Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang...
- **发布时间**: 2026-10-09
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.12403v1](https://arxiv.org/pdf/2610.12403v1)
- **相关度评分**: 10/10

#### 英文摘要

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at https://github.com/ZJU-REAL/ViSkill.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5a763e0f-525c-4

---

### 10. BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion

- **ArXiv ID**: [2610.12307v1](https://arxiv.org/abs/2610.12307v1)
- **作者**: Ozgur Kara, Yujia Chen, Daniel Watson, David Forsyth, James Matthew Rehg...
- **发布时间**: 2026-10-09
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12307v1](https://arxiv.org/pdf/2610.12307v1)
- **相关度评分**: 10/10

#### 英文摘要

Most image generation models rely on uniform tokenization, allocating the exact same computational budget to equally-sized image patches. This static paradigm cannot adapt to different resource constraints at inference time, and yields suboptimal quality-cost tradeoff by devoting the same effort to both plain backgrounds and intricate details. We propose BudgetPix, an adaptive tokenization framework that dynamically allocates compute based on visual complexity and spatial layout, enabling flexible computational budgeting at inference time. BudgetPix comprises three key components: (1) an adaptive encoder that maps a fixed-size image to a variable-length token sequence using an entropy-guided quadtree alongside a multi-scale patch embedder; (2) a scale-aware decoder reconstructs fixed-resolution images from multi-scale token sets; and (3) a flexible training and sampling schedule that enables pixel-space denoisers to operate across variable token counts. BudgetPix seamlessly integrates with existing pixel-space diffusion architectures, enabling a single checkpoint to be operated at a wide range of compute budgets. Evaluated on text-to-image generation, BudgetPix matches the fidelity of MiniT2I-L at $512^2$ and PixelDiT at $1024^2$ using just 25% of the original compute budget. In class-conditional generation using a MeanFlow backbone, BudgetPix requires merely 60% of the full compute budget to produce images with near-zero quality degradation, observing a marginal 0.8-point increase in FID. Comprehensive assessments by human and VLM judges confirm that BudgetPix establishes a significantly improved quality-efficiency tradeoff over prior budget-adaptive baselines. More details are available at our project page: https://karaozgur.com/BudgetPix

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cc298d5a-0acc-4

---

### 11. Compact and Efficient Indexes for Learned Sparse Retrieval

- **ArXiv ID**: [2610.12300v1](https://arxiv.org/abs/2610.12300v1)
- **作者**: Franco Maria Nardini, Luca Rizzo, Cosimo Rulli, Rossano Venturini
- **发布时间**: 2026-10-09
- **分类**: cs.IR, cs.DB
- **PDF**: [https://arxiv.org/pdf/2610.12300v1](https://arxiv.org/pdf/2610.12300v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper investigates how to substantially reduce the memory footprint of learned sparse retrieval indexes without sacrificing the efficiency of state-of-the-art retrieval data structures. Building on SEISMIC, we revisit both levels of its design: the inverted index used to select candidates and the forward index used to score them. For the inverted index, we replace costly per-block summaries with medoids, namely existing documents elected as block representatives, collapsing the per-block metadata from a sparse vector to a single document identifier. For the forward index, we compress both components and values. We reorder the vocabulary to place co-occurring components closer together and encode the resulting $Δ$-gaps with DOTPACKING8, a SIMD-friendly bit-packing scheme that fuses decompression with dot-product evaluation; values are quantized with compact per-component 4-bit codebooks fitted to each component's distribution. We further introduce JUMPDOT, a blocked dot-product kernel tailored for queries that contain only a few non-zero entries. Our forward-index compression is independent of SEISMIC and can be plugged into any system relying on forward-index-based scoring, as we demonstrate by integrating it into KANNOLO. A comprehensive evaluation on MS MARCO with three state-of-the-art learned sparse encoders shows that our solutions markedly improve the speed-space trade-off of learned sparse retrieval: at equal accuracy, our indexes answer queries up to 5.3x faster than the best competitor while using about 3x less memory, and in the most memory-constrained regime, they remain up to 1.9x faster while using up to 3.9x less memory.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0b77ed71-b143-4

---

### 12. NativeScope: Relation-Localized Retrieval over Native Topology with a Correct Anchor

- **ArXiv ID**: [2610.12243v1](https://arxiv.org/abs/2610.12243v1)
- **作者**: Long Wang
- **发布时间**: 2026-10-09
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.12243v1](https://arxiv.org/pdf/2610.12243v1)
- **相关度评分**: 10/10

#### 英文摘要

Dense retrieval usually ranks text chunks by their semantic similarity to a question. This ignores structure that many data systems already store, including section membership, session boundaries, and native order. We propose NativeScope, a scope-then-rank method for queries with a known anchor and relation. It represents a query as q -> (A, r, B). The anchor A and relation r select native units through belonging, before, or after operators, and the target term B ranks only chunks that overlap the selected scope. An internal variant, NS-FullQ, ranks the same candidates with the full question. We evaluate both methods on 200 controlled document and memory records derived from QASPER and LongMemEval under a 1,024-token budget. NativeScope attains native-unit recall of 89.28 percent for documents and 72.50 percent for memories, improving over instance-wide Dense RAG by 42.75 and 22.00 percentage points. NS-FullQ reaches 87.78 percent and 68.50 percent; its differences from NativeScope are inconclusive, locating the primary gain in relational scoping rather than the shorter ranking query. With automatic Top-1 anchors, memory recall falls to 35.50 percent. NativeScope is therefore effective when anchor coordinates and native relations are reliable, but hard scoping inherits errors from the localization interface.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a145d887-2046-4

---

### 13. One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails

- **ArXiv ID**: [2610.12292v1](https://arxiv.org/abs/2610.12292v1)
- **作者**: Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram
- **发布时间**: 2026-10-09
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.12292v1](https://arxiv.org/pdf/2610.12292v1)
- **相关度评分**: 10/10

#### 英文摘要

A typed decision model reads a piece of text and returns a probability over caller-defined options, each with a short written definition, generating no text. Recent work places these models in agent systems as guardrails: the component that reads a proposed tool call or incoming message and decides whether to allow it. We evaluate seven open-weight models in that role and report the two error directions separately: a fail-open error allows a prohibited action and is a vulnerability; a fail-closed error blocks a permitted one and is only a cost. On prompt-injection, jailbreak and toxic-content screening, accuracy at the allow-or-block decision ranges from 36% to 72% against a chance level of 50%. A low error rate in one direction only reflects which answer a model defaults to: one allows nearly everything, another blocks nearly everything. On a synthetic suite of agent tool calls, six lines of server log text that say nothing about the policy raise a gate's fail-open rate from 0% to 63% on a policy it otherwise decides correctly. Giving the permissive option a misleading name, with its definition and the judged text untouched, raises that rate to between 93% and 100% on the four models that place the label in their input. Every defense we tested is defeated, either by an attacker who targets its mechanism or by attacker-controlled text. Escalating the least confident decisions does not help either: a decision an attack has reversed is no less confident than the one it replaced. Parsing each policy field into a typed value does eliminate one attack, but it also makes the model unnecessary: a deterministic rule over those values reaches 100% accuracy on all six policies. These models can reduce how many cases reach a reviewer, but on this evidence they should not be the component that decides. Code is available at https://github.com/ArminAzizi98/option-channel-attack.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 53e21ed7-cf38-4

---

### 14. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

- **ArXiv ID**: [2610.12470v1](https://arxiv.org/abs/2610.12470v1)
- **作者**: Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung...
- **发布时间**: 2026-10-09
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12470v1](https://arxiv.org/pdf/2610.12470v1)
- **相关度评分**: 10/10

#### 英文摘要

While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for broad generalization, but without prior guidance, it struggles with high-dimensional exploration in complex, multi-stage tasks. To address these coupled generalization and exploration challenges, we present Dex-One2Many, a real-to-sim-to-real framework that learns a generalizable dexterous manipulation policy from a single human video. Our key insight is to abstract the video into sequential scene graphs that guide RL, enabling efficient exploration while preserving broad generalizability. The graphs serve as generative constraints for sampling diverse reset states and provide dense rewards for each stage. Because the graphs constrain relations rather than exact poses, these reset states cover object poses and grasps beyond the video, while initializing each stage from them with dense rewards keeps exploration short and guided. Trained entirely in simulation, Dex-One2Many transfers zero-shot to a real multi-fingered hand. Across five tool-use and manipulation tasks, Dex-One2Many exceeds baselines by 6.5% in seen configurations, while its robust generalization widens this gap to 71% in unseen scenarios.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 31525d7f-1101-4

---

### 15. Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation

- **ArXiv ID**: [2610.12469v1](https://arxiv.org/abs/2610.12469v1)
- **作者**: Ritesh Thawkar, Shubham Patle, Shravan Venkatraman, Rao Muhammad Anwer
- **发布时间**: 2026-10-09
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.12469v1](https://arxiv.org/pdf/2610.12469v1)
- **相关度评分**: 10/10

#### 英文摘要

Instruction-guided image editors have become highly capable, yet improving them further still depends on human-edited training pairs or external reward models. Such supervision is costly to obtain and can reward plausible failures: a realistic output may leave the requested change undone or alter content that should be preserved. In this work, we strive to improve a pretrained image editor using only its own generations, without human-edited targets or an external training-time reward model. To this end, we propose a self-evolving framework, named Rubric-CEPR, that verifies the editor's own samples with its internal representations through a rubric-augmented Contrastive Edit-Preservation Reward (CEPR). A Planner proposes structured edit instructions from unlabeled images, the Editor samples multiple candidate edits, and a frozen Critic scores each candidate with decomposed rubric checks for edit realization, removal of the old state, and content preservation, using features already exposed by the editor. Non-compensatory gates reject infeasible candidates, and the best verified candidate is distilled into the editor through lightweight adapter training. On Qwen-Image-Edit, Rubric-CEPR improves ImgEdit from 4.36 to 4.60 (+5.5%), with a +24.9% gain on object isolation, and transfers to GEdit-Bench and Complex-Edit. The same procedure also improves Step1X-Edit by +7.8% on ImgEdit. We hope our approach will serve as a solid baseline for image editors that improve themselves from their own verified samples. Our code is publicly available at $\href{https://riteshthawkar.github.io/Rubric-CEPR/}{\text{this URL}}$

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c60af2a9-47fd-4

---
