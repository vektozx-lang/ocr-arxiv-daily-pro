# OCR arXiv Daily Pro — 2026-11-18

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-17 09:10 - 2026-11-18 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9cd4998b-b5

---

## 📄 论文详情

### 1. Semantic-Guided Geometric Decoding for Token-Efficient Visual Grounding

- **ArXiv ID**: [2611.22577v1](https://arxiv.org/abs/2611.22577v1)
- **作者**: Zhaojie Chen, Junyan Yang, Le Yang, Qi Dang, Yucheng Huang...
- **发布时间**: 2026-11-17
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.22577v1](https://arxiv.org/pdf/2611.22577v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) provide a unified interface for language-conditioned visual perception. In pixel-to-sequence grounding, autoregressive coordinate generation requires multiple sequential decoding steps per box, increasing inference cost with the number of instances. Pixel-to-embedding methods reduce this overhead but lack explicit spatial encoding when using a shared special token. We introduce SemGeo, a token-efficient visual grounding framework that represents each instance with a single grid token for coarse localization. A geometric decoder reuses visual features and hidden states to recover precise discrete box coordinates in parallel. To train proposal generation and box localization together, we introduce Gaussian soft labels that encode coordinate distances during supervised fine-tuning (SFT). Reinforcement post-training further combines box-set rewards with coordinate supervision on model-generated proposals. This stage trains the language model and geometric decoder on their own predictions to mitigate the mismatch between teacher-forced training and inference. Across eight benchmarks spanning object detection, referring object detection, and document layout grounding, SemGeo achieves the highest F1@mIou among compared MLLMs on six benchmarks. It also delivers $2.07\times$ and $1.25\times$ the mean box-generation throughput of representative grounding baselines under vLLM and Transformers, respectively, while achieving higher accuracy in both comparisons.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b6314b10-38

---

### 2. What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super

- **ArXiv ID**: [2611.22161v1](https://arxiv.org/abs/2611.22161v1)
- **作者**: Sushant Mehta, Edwin Chen
- **发布时间**: 2026-11-17
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.22161v1](https://arxiv.org/pdf/2611.22161v1)
- **相关度评分**: 10/10

#### 英文摘要

We post-train NVIDIA's Nemotron 3.5 Super (120B total, 12B active parameters) with reinforcement learning (RL) on five expert-built task datasets, one at a time: real-world software engineering, complex constraints, long-horizon tool use, professional chart understanding and enterprise document reasoning. Each run trains a fresh rank-32 LoRA adapter with CISPO on Tinker, with no supervised stage, and each adapter is compared with the base model on the same tasks, harness and settings. On twelve headline benchmarks, eight built by other groups and four by Surge AI, the gains range from +4.5 points on IFBench to +13.8 on GDP_pdf, which rises from 10.4% to 24.2%; SWE-bench Pro V2 rises from 86.9% to 92.1%, Terminal-Bench 2.1 from 63.9% to 70.3%, MultiChallenge from 58.3% to 66.6%, AutomationBench from 14.8% to 27.5% and Chartography from 39.4% to 50.6%. The document adapter, trained without API tools, also gains +8.0 points on AutomationBench. In attempts read side by side with the base model's on tasks each adapter newly solves, the base model's failures recur in a few modes, and each adapter does more often what the base model missed: the tool-use adapter finds the data and the rules before acting, the coding adapter writes its own test or scratch files on SWE-bench Pro V2, the constraints adapter carries earlier turns into its answers, the chart adapter measures the marks in code, and the document adapter reads AutomationBench's spreadsheets.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5847690a-d6

---

### 3. Learning Grounded Reasoning from Human Gaze

- **ArXiv ID**: [2611.23209v1](https://arxiv.org/abs/2611.23209v1)
- **作者**: Gabriel Sarch, Declan Campbell, Nicholas Budny, Kia Ghods, Katerina Fragkiadaki...
- **发布时间**: 2026-11-18
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23209v1](https://arxiv.org/pdf/2611.23209v1)
- **相关度评分**: 10/10

#### 英文摘要

Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes noise and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be effectively leveraged to improve visual reasoning in VLMs, while maintaining alignment with human behavior. We collect 7,109 human gaze trials from a diverse and challenging set of visual reasoning tasks, and train grounded reasoning models with different forms of gaze guidance. Across evaluations in chart understanding, visual search, and counting, we find that using human gaze as a prior for grounded reasoning consistently outperforms supervision using the full gaze sequence. Based on these findings, we introduce GGR (Gaze-Guided Reasoner), which achieves greater human alignment and more reliable visual grounding while matching or outperforming leading grounded-reasoning baselines in accuracy. Reinforcement learning further improves task accuracy, gaze alignment, and grounding quality despite using no gaze supervision. Behavioral analyses show that gaze supervised models exhibit more visual exploration before arriving at an answer. Our results suggest that the value of human gaze lies in guiding spatial exploration and shaping reasoning behavior without requiring complete imitation of human behavior.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: af125292-f6

---

### 4. Do LLM Agents Still Need to Be Told How to Self-Improve?

- **ArXiv ID**: [2611.23219v1](https://arxiv.org/abs/2611.23219v1)
- **作者**: Shobhita Sundaram, Cansu Sancaktar, Phillip Isola
- **发布时间**: 2026-11-18
- **分类**: cs.LG, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.23219v1](https://arxiv.org/pdf/2611.23219v1)
- **相关度评分**: 10/10

#### 英文摘要

LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for context-based optimization. Using the setting of gameplay as a testbed, a frozen LLM agent is given a compute budget and tools for collecting experience and updating text documents, and allowed to freely experiment without an externally imposed loop or access to real-world data. We find that sufficiently capable models do self-improve under these conditions, demonstrating strategies that align with classic cognitive frameworks for self-regulated learning and constructs from machine learning literature on self-generated curricula. Furthermore, we study the extent to which the learned text artifacts transfer to external benchmarks, observing improvement across different game horizons, mechanics, and 3D navigation.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3086cf3b-9e

---

### 5. Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance

- **ArXiv ID**: [2611.23142v1](https://arxiv.org/abs/2611.23142v1)
- **作者**: Lorenzo Masoero
- **发布时间**: 2026-11-18
- **分类**: cs.SE, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.23142v1](https://arxiv.org/pdf/2611.23142v1)
- **相关度评分**: 10/10

#### 英文摘要

The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind already exist in abundance, both explicit (e.g., resolved support tickets revealing what documentation lacks) and implicit (e.g., code-documentation discrepancies detectable from automated loops). We deploy a multi-agent system, built around a triage agent we call "TriAgent," that continuously extracts these signals and repairs documentation drift. Over 43 days of shadow-mode operation, our system triaged 499 tickets and surfaced 92 gaps in the documentation. Using a panel of LLM judges from independent model families, 81.1% of TriAgent's verifiable assertions were correct (245 of the 302 assertions the human resolution addresses; majority of three judges); on length-comparable pairs the panel preferred TriAgent's response in 70.5% of pairs and the human engineer's in 23.2% (the rest had no judge majority). Importantly, agent- and human-sourced replies tended to be complementary, with the human often surfacing insights that were either buried within the existing documentation or missing from it entirely; our system turns each such insight into a documentation gap and, after human review, a fix. Repairing a gap measurably improved the agent's later answer: when the agent re-answered the same ticket after the repair, blinded judges preferred the post-repair answer over its own pre-repair answer 71.4% of the time (n=35). A blinded human audit confirms strong alignment on self-improvement.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ddfc6767-c0

---

### 6. The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?

- **ArXiv ID**: [2611.23127v1](https://arxiv.org/abs/2611.23127v1)
- **作者**: Basavaraj R M, Harshal Chandel
- **发布时间**: 2026-11-18
- **分类**: cs.LG, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23127v1](https://arxiv.org/pdf/2611.23127v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome, each expanded into controlled stress conditions: hard-negative retrieval noise (1-20 documents), visual ambiguity (Gaussian and motion blur, low-resource crops) and cross-modal conflict with counterfactual flip pairs. Instead of only measuring degradation, we ask how models combine the two modalities. From ideal Bayesian cue combination we derive a testable prediction that yields formal definitions of Knowledge Inertia (text over-weighted relative to the model's own image evidence) and Sensory Capture (the reverse), and we estimate the weights with a measurement-error-corrected regression whose recovery of known weights we verify. A counterfactual flip decomposition separates modality bias from concept priors, and a Grounding Illusion Score measures how much clean accuracy is not grounded in the image. We evaluate 4 open models on one frozen, seeded evaluation split of 2,000 GIB-200K items. All models are accurate on clean inputs (92.5%-94.2%) but adverse accuracy falls to 41.3%-59.9%. The two LLaVA models over-weight the text (Knowledge Inertia, w_T/w_I = 1.229 and 1.322), whereas InternVL3 favours the image (w_T/w_I = 0.680); between 34.8% and 71.4% of the clean answers that are correct are abandoned when the document lies. A training-free consistency check that compares the answer with and without retrieval trades coverage for accuracy under misleading documents, while falling back to the image fails when the image is heavily degraded. All per-instance outputs, code, and an audit that recomputes every reported open-model number are released.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 84d5393e-17

---

### 7. Uncovering the Invisible in Routine Radiology: Cross-Modal Detection of MRI-Verified Soft-Tissue Pathologies from CBCT via Physics-Guided 3D Self-Supervised Learning

- **ArXiv ID**: [2611.23042v1](https://arxiv.org/abs/2611.23042v1)
- **作者**: Evgeny Alves Limarenko
- **发布时间**: 2026-11-18
- **分类**: eess.IV, cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.23042v1](https://arxiv.org/pdf/2611.23042v1)
- **相关度评分**: 10/10

#### 英文摘要

Routine X-ray modalities like cone-beam computed tomography (CBCT) are optimized for high-contrast mineralized tissues, leaving soft-tissue abnormalities buried beneath photon noise and below human visual perception. Thus, detecting non-calcified pathologies requires secondary magnetic resonance imaging (MRI). We demonstrate that sub-visual radiographic signatures of soft-tissue pathology are physically preserved within routine CBCT scans and can be extracted for opportunistic screening using a targeted, physics-guided deep learning pipeline, even under extreme paired-data scarcity. Using the temporomandibular joint (TMJ) as a model system (N = 212 paired CBCT-MRI joints), we address the severe overfitting of high-capacity 3D networks through a two-stage framework. First, we employ a frozen full-grid 3D masked autoencoder (BertsWin) pre-trained on 6,550 unlabeled CBCT volumes via the GradientConductor (GCond) optimizer and an anatomy-aware objective (PhysLoss) redirecting gradient flow into the [-300, 300] HU soft-tissue window. Second, automated localization of the condylar zenith drives a deterministic 3D cropping that eliminates 81% of background osseous variance. Evaluated via a patient-isolated 3x10-fold stratified cross-validation protocol, a statistically robust sub-visual signal for MRI-verified synovial effusion (ROC AUC = 0.793) emerges exclusively from representations pre-trained with the PhysLoss and GCond regime. Crucially, only this setup captures true 3D anatomical chirality (p < 0.001) and high intra-patient structural consistency (0.791) over inter-patient noise; conversely, identical architectures pre-trained with standard L2 loss or unmasked variance decomposition (MVC) collapse to random guessing. These findings establish a generalizable paradigm for repurposing routine, low-contrast radiographic scans into opportunistic screening tools for occult soft-tissue disease.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a5abb2ae-77

---

### 8. MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study

- **ArXiv ID**: [2611.23158v1](https://arxiv.org/abs/2611.23158v1)
- **作者**: Nikit Srivastava, Joel Dag, René Speck, Axel-Cyrille Ngonga Ngomo
- **发布时间**: 2026-11-18
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.23158v1](https://arxiv.org/pdf/2611.23158v1)
- **相关度评分**: 10/10

#### 英文摘要

Routed low-rank adapters offer a parameter-efficient means to improve the performance of large language models (LLMs) across tasks. Hence, it is assumed that they can also be used to improve the support of low-resource languages in LLMs, which currently serve English far better than the thousands of other languages spoken worldwide. However, this assumption has never been verified empirically under a shared multilingual evaluation protocol. We address exactly this gap by comparing eight low-rank adaptation (LoRA) methods on a frozen base model using 200 unique languages in more than 9{,}000 evaluation settings. Our results suggest that a reduced-scale search can identify viable configurations of LoRA methods but does not reliably predict their relative performance, as the top-ranking configuration is never best at scale. LoRA reliably improves language-model fit on translation data, consistently degrades reading comprehension, and benefits low-resource languages most. These findings suggest that LoRA methods should be regarded as targeted tools rather than general-purpose means for improving the multilingual capabilities of LLMs.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a1d528db-8a

---

### 9. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

- **ArXiv ID**: [2611.23228v1](https://arxiv.org/abs/2611.23228v1)
- **作者**: Rui Ning, Om Chabra, Hari Balakrishnan
- **发布时间**: 2026-11-18
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.23228v1](https://arxiv.org/pdf/2611.23228v1)
- **相关度评分**: 10/10

#### 英文摘要

Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frames normally requires re-running the entire window through the model. We observe that the recurrent update is affine in the state with input-dependent coefficients, so the effect of each frame can be captured as a transformation that composes associatively. We present Spool, a training-free framework that caches per-frame state transformations and composes them efficiently as the window advances, removing expired frames from each recurrent layer's state without replaying frames through the backbone. Removal is exact within each layer; as with key-value eviction in attention, expired frames can retain residual influence through the cached inputs computed by earlier layers. We design a dedicated data structure and GPU kernels to achieve low caching and composition overhead. Across five open-source hybrid VLMs and four video reasoning benchmarks, Spool achieves the lowest p95 time-to-first-token in all 20 model-benchmark tests, reducing it by a geometric mean of $6.6\times$ over the faster of two recent vLLM baselines, while improving accuracy by 2.3 percentage points on average.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 978246fb-ed

---

### 10. FastFrames: Video Generation at Interactive Latency

- **ArXiv ID**: [2611.23226v1](https://arxiv.org/abs/2611.23226v1)
- **作者**: Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong...
- **发布时间**: 2026-11-18
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23226v1](https://arxiv.org/pdf/2611.23226v1)
- **相关度评分**: 10/10

#### 英文摘要

Autoregressive video diffusion models generate frames based on new observations and inputs, making them a promising medium for interactive visual experiences. However, existing models are orders of magnitude too slow for fluid interaction. This paper introduces FastFrames, a family of fast autoregressive video diffusion models that achieves interactive latency without compromising quality. We profile the inference pipeline of state-of-the-art models and find that operations often treated as fixed implementation details, such as VAE decoding and KV cache updates, in fact account for over half of end-to-end inference latency. We challenge the assumption that these components are indispensable and replace them with lightweight alternatives. Our 1.3B variant runs at 36 ms per frame, or 28 responses per second (RPS), on a single B200 GPU while matching the generation quality of a state-of-the-art model that is nearly 8x slower. Our 14B variant runs at 45 ms per frame, or 22 RPS, on an 8x B200 GPU node and yields significantly better visual quality and realism. We show that FastFrames enables real-time interaction in applications such as camera-conditioned and physics-conditioned video generation.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ab0f18e4-f4

---

### 11. EviSlide-MIL: Multi-Query Pooling and Shared Prediction for Class-Incremental Whole-Slide Image Classification

- **ArXiv ID**: [2611.23212v1](https://arxiv.org/abs/2611.23212v1)
- **作者**: Zhouhan Qian, Sicheng Chen, Chad Wong, Tianyi Zhang, Enhui Chai...
- **发布时间**: 2026-11-18
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23212v1](https://arxiv.org/pdf/2611.23212v1)
- **相关度评分**: 10/10

#### 英文摘要

Histopathological analysis of whole-slide images (WSIs) plays a critical role in cancer diagnosis, and multiple instance learning (MIL) is widely adopted for WSI analysis under weak supervision. As new tumor subtypes are introduced, extending existing MIL models requires learning new classes while retaining knowledge of previously learned ones. This presents a class-incremental learning challenge, where models must acquire new classes with limited access to historical training data and recognize all learned classes without task identifiers at inference. A major obstacle is forgetting, as updates to feature aggregation and prediction modules can degrade performance on previously learned classes. To address this challenge, we propose \textbf{EviSlide-MIL}, a class-incremental WSI framework that integrates multiple learnable queries per class with a shared prediction module. The queries aggregate frozen patch features into class-specific representations, while the shared prediction module limits parameter growth across incremental stages. By freezing queries associated with previously learned classes, EviSlide-MIL preserves their attention patterns for identical inputs, while experience replay and knowledge distillation further mitigate forgetting as shared parameters are updated. Experiments on eight tumor subtypes from The Cancer Genome Atlas demonstrate that EviSlide-MIL achieves improved performance and reduced forgetting compared with competing methods across most learning settings, demonstrating its potential for scalable and knowledge-preserving WSI classification. Code and pretrained models will be released.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a3b1ad21-f3

---

### 12. Multimodal Masked Diffusion Autoencoder for Modeling Impaired Driving

- **ArXiv ID**: [2611.23211v1](https://arxiv.org/abs/2611.23211v1)
- **作者**: John Gideon, Anshul Gupta, Megan Applegate-Kenton, Kayli Battel, Todd J Rowell...
- **发布时间**: 2026-11-18
- **分类**: cs.CV, cs.LG, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.23211v1](https://arxiv.org/pdf/2611.23211v1)
- **相关度评分**: 10/10

#### 英文摘要

Human cognitive state (e.g., distraction, stress), gaze, and behavior interact with the driving environment in subtle ways that AI could use to assist drivers, but ground-truth labels for human cognitive state levels are costly to obtain at scale. We propose a multimodal masked-diffusion autoencoder, ID-MAE, that adds a self-supervised objective to impairment prediction: alongside predicting the impairment label as a masked token, it reconstructs masked gaze and trajectory. To probe the effects of different modalities and types of impairments on model inference, we introduce DIVERT, a driving-simulator dataset containing 103 hours of driving data (n = 109) with ten impairment inductions spanning cognitive, visual, and emotional states, recorded with gaze, vehicle state, and scene video. We demonstrate how ID-MAE affords significant improvements in impairment inference results on both the DIVERT dataset and existing datasets, and enables strong results in additional tasks, such as trajectory and gaze prediction. For location-matched pairs, our model achieves a paired AUC of 0.706 for impairment detection on DIVERT, compared to 0.590 without reconstruction loss, improving over existing baselines. We probe the design space in terms of input modalities, masking scheme, positional encoding, attention mechanism, and decoding. We also investigate the interaction between various impairments in training and inference, demonstrating that visually demanding distractions are separable from cognitive distractions. Code and data will be available upon acceptance.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f9077425-90

---

### 13. Distortion-Free Semantic Watermarks for Black-Box Generative Models

- **ArXiv ID**: [2611.23208v1](https://arxiv.org/abs/2611.23208v1)
- **作者**: Aviv Yossef, Or Patashnik, Or Zamir
- **发布时间**: 2026-11-18
- **分类**: cs.LG, cs.CR, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23208v1](https://arxiv.org/pdf/2611.23208v1)
- **相关度评分**: 10/10

#### 英文摘要

We present a provably distortion-free semantic watermarking algorithm that requires only black-box sampling access to a generative model and black-box access to a semantic embedding. A watermark is called distortion-free if, averaged over its secret detection key, it leaves the generator's output distribution unchanged; this provides a formal guarantee that watermarking does not reduce output quality. Conventional such watermarks are often brittle to transformations. This is especially problematic for images, where benign operations such as compression, cropping, or resizing change the entire pixel representation. Semantic watermarks therefore require detection to be robust to content-preserving transformations. Previous methods combining these properties rely heavily on specific white-box properties of the underlying model: either to autoregressive text generation or to diffusion-specific access, such as control of the initial noise or diffusion inversion. In contrast, our construction is fully generic: It only interacts with the generative model and the semantic embedding, a function that determines the notion of "preserving content" under which detection should be robust, via sample and query access. We then instantiate this framework for image generation. We characterize the two competing properties required of the semantic embedding: it should remain stable under transformations that preserve an image's content, but should distinguish independent generations from the same prompt. We train an image encoder directly for this tradeoff. The resulting encoder improves separation while maintaining stability over off-the-shelf alternatives and enables strong aggregate detection while remaining robust to various transformations. We demonstrate the effectiveness of our watermark scheme on both open-source and closed models, which is possible only due to restriction to black-box access.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e3cf9f53-7f

---

### 14. WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition

- **ArXiv ID**: [2611.23192v1](https://arxiv.org/abs/2611.23192v1)
- **作者**: Almog Anschel, Sarah Keren
- **发布时间**: 2026-11-18
- **分类**: cs.AI, cs.LG, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.23192v1](https://arxiv.org/pdf/2611.23192v1)
- **相关度评分**: 10/10

#### 英文摘要

Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous trajectories rely on an explicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous trajectory prefixes where such knowledge is most needed. We present WoRD (Waypoint Recognition with Diffusion), which uses a learned trajectory prior to infer the agent's goal from partial observations. At each step, WoRD runs one warm-started denoising chain per candidate goal, steers each chain toward the observed trajectory through a closed-form log-likelihood gradient, and reweights the resulting samples by Bayes' rule into a calibrated posterior over goals. We evaluate WoRD on simulated robot settings, pedestrian trajectories, and vehicle trajectories using four metrics targeting distinct failure modes. Across all three settings, the same inference procedure preserves calibrated multimodal beliefs through ambiguous prefixes where filter- and classifier-based observers collapse to a single mode or grow overconfident.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a7fd1a3b-47

---

### 15. Any2Building: Unifying Point Clouds and Images for Building Reconstruction via Shared Spatial Queries

- **ArXiv ID**: [2611.23187v1](https://arxiv.org/abs/2611.23187v1)
- **作者**: Hongye Hou, Zhuoxiao Li, Liu Xiangyu, Tengxi Wang, Jing Ou...
- **发布时间**: 2026-11-18
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23187v1](https://arxiv.org/pdf/2611.23187v1)
- **相关度评分**: 10/10

#### 英文摘要

Abstracting structured buildings from limited observations is essential for 3D urban modeling and digital twins. Partial point clouds and overhead images of the same building provide incomplete 3D surface measurements and visual cues to its footprint, roof geometry, and rooftop structures, respectively. This motivates a unified framework that aligns geometric and visual cues in 3D and reconstructs buildings from either or both modalities. Building on this connection, we present Any2Building, a unified model for Level of Detail 2 (LoD2) building reconstruction from partial point clouds, overhead images, or both, with optional coarse geometric priors. At its core is an occupancy-grounded shared spatial queries representation that organizes available observations within a common 3D grid. Supervised by complete building surface voxels, these queries connect observational evidence to target geometry, enabling a shared generator to learn structural priors across tasks and providing spatial guidance for recovering missing structure. A trained voxel conditional surface-generation and low-poly remeshing pipeline then converts the predicted structure into compact LoD2 building models. To support this framework, we introduce BuildingWorld-Image, comprising approximately one million paired samples of partial point clouds, overhead images, and LoD2 building models across 18 cities. Experiments on multiple benchmarks demonstrate that Any2Building outperforms existing methods in geometric reconstruction accuracy across unimodal and multimodal point-cloud completion, single-image building generation, and prior-assisted generation, while maintaining detailed and robust recovery when point cloud input modality is degraded.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b13e2680-ae

---
