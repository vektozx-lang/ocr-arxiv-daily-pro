# OCR arXiv Daily Pro — 2026-11-25

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-24 09:10 - 2026-11-25 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4c0049c8-e0

---

## 📄 论文详情

### 1. When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents

- **ArXiv ID**: [2611.32446v1](https://arxiv.org/abs/2611.32446v1)
- **作者**: Akshata A Bhat, Daman Deep Singh, Niyati Chhaya
- **发布时间**: 2026-11-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.32446v1](https://arxiv.org/pdf/2611.32446v1)
- **相关度评分**: 10/10

#### 英文摘要

Human annotations on documents (such as arrows, carets, strikethroughs, and insertions) express corrective intent yet existing OCR and document understanding systems treat these marks as visual noise rather than semantic edit operations. We introduce intent-aware OCR, the task of generating corrected transcriptions by jointly reasoning over original document content and visual intent cues (handwritten or digital) that convey edit intent. To support this setting, we present DocIntent, a multimodal dataset of 1,600 financial documents with over 5,700 annotated visual intent cues, each paired with layout-aware, intent-resolved OCR targets. We further introduce IntentBench, a 216-document benchmark designed to evaluate model robustness under diverse real-world annotation conditions. Leveraging DocIntent, we fine-tune DocIntentOCR, a suite of 3B and 7B parameter vision-language models, under direct intent supervision on corrected transcriptions. On IntentBench, the fine-tuned 3B and 7B models achieve F1-scores of 0.81 and 0.83, respectively, substantially outperforming commercial closed-source (e.g., GPT-4.1 (0.626)), and open-source models (e.g., LLaMA-3.2-Vision-90B (0.50)) demonstrating that intent-aware supervision enables compact domain-specific models to outperform substantially larger general-purpose systems on this task. This work establishes intent-aware OCR as a novel human-in-the-loop document understanding task and provides foundational resources (dataset, benchmark, models) to advance research in interactive document processing.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 096a942c-47

---

### 2. ArEssays: Towards Robust Arabic Handwritten Text Understanding in Educational Settings

- **ArXiv ID**: [2611.32211v1](https://arxiv.org/abs/2611.32211v1)
- **作者**: Hamdy Mubarak, Anas Madkoor, Ehsaneddin Asgari, Majd Hawasly
- **发布时间**: 2026-11-24
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.32211v1](https://arxiv.org/pdf/2611.32211v1)
- **相关度评分**: 10/10

#### 英文摘要

Automated understanding of handwritten Arabic student essays remains challenging due to script complexity and high variability in children's writing. We introduce ArEssays, a large-scale dataset of authentic essays from primary to secondary students across Egypt, with both verbatim transcriptions and linguistically corrected versions. We benchmark 34 vision-language and OCR models, including fine-tuned systems, and find large performance gaps on real student handwriting. We release the dataset, training pipelines, and results to support research in Arabic OCR, document understanding, and educational NLP.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f737bcc3-77

---

### 3. VenusOCR2.0: Towards Efficient and Effective Document Parsing

- **ArXiv ID**: [2611.32617v1](https://arxiv.org/abs/2611.32617v1)
- **作者**: Lei Li, Zheng Wei, Yi Yuan, Qingbin Liu, Jiang Bian...
- **发布时间**: 2026-11-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.32617v1](https://arxiv.org/pdf/2611.32617v1)
- **相关度评分**: 10/10

#### 英文摘要

We present VenusOCR2.0, a compact 1B-parameter vision-language recognizer designed for both high-accuracy and high-throughput document parsing across text, tables, and formulas. To continuously improve recognition quality without self-training collapse, we build a bounded recursive self-improvement (RSI) data engine where the model acts strictly as a weakness probe, while external multi-expert medoid consensus, VLM visual verification, and factorized synthesis supply reliable supervision across pretraining, curated SFT, and RLVR. VenusOCR2.0 couples a dynamic-resolution SigLIP2 encoder and 2x2 spatial token merging with a Qwen3-0.6B decoder, adopting compact atomic OTSL tokens to shorten table sequences and reduce structural errors. To further eliminate the autoregressive decoding bottleneck, we introduce PTPv2, a lightweight ($\sim$67M) decoupled parallel draft module that combines frozen multi-layer verifier conditioning, a standalone learned mask, and block-causal all-position next-token prediction. On OmniDocBenchv1.6, VenusOCR2.0 achieves an overall score of 96.45 and a state-of-the-art 98.57 formula CDM, substantially outperforming massive general-purpose VLMs such as Gemini-3-Pro (92.91) and Qwen3-VL-235B (89.78). Deployed in vLLM on a single H20 GPU, PTPv2 delivers a 2.96x single-request speedup and up to 2.36x higher batched throughput while guaranteeing lossless, token-for-token equivalence with standard autoregressive decoding.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6f1e089f-02

---

### 4. DocPristine: Content-Aware Document Appearance Enhancement under Real-World Mixed Degradations

- **ArXiv ID**: [2611.32176v1](https://arxiv.org/abs/2611.32176v1)
- **作者**: Zihan Huang, Junle Liu, Zhonghao Ye, Yuyi Zhang, Peirong Zhang...
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.32176v1](https://arxiv.org/pdf/2611.32176v1)
- **相关度评分**: 10/10

#### 英文摘要

Camera-captured documents often exhibit mixed degradations, such as highlights, shadows, and blur, that distort backgrounds and obscure text details. Document appearance enhancement (DAE) aims to mitigate these degradations and improve readability. Existing document appearance enhancement methods rely either on input-derived visual cues that can become unreliable under severe degradation or on LLM-based degradation diagnosis that lacks spatial guidance. Notably, we find that pretrained document visual encoders continue to attend to text regions in degraded documents, providing content-aware guidance. Based on this insight, we propose DocPristine, which adaptively fuses multi-layer features from a frozen document visual encoder and injects them into a pixel restoration network. To integrate these features into a pixel restoration network, DocPristine combines Adaptive Multi-Layer Feature Fusion (AMFF), Hierarchical Gated Conditioning (HGC), and Shifted-Window Cross-Attention (SWCA). Specifically, SWCA draws on structural cues from neighboring locations across window boundaries to recover fine text details.We also introduce DocACE, with a synthetic mixed-degradation training set (DocACE-Synthetic) and a real-world test set (DocACE-Real) containing manually restored ground-truth images and document parsing annotations. Comprehensive experiments across three benchmarks demonstrate that DocPristine achieves state-of-the-art appearance enhancement quality and consistently improves downstream document parsing. Code, models, and data will be publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8df6a235-f1

---

### 5. SciFig2Data: A Workflow for Recovering Structured Data from Scientific Figures

- **ArXiv ID**: [2611.31787v1](https://arxiv.org/abs/2611.31787v1)
- **作者**: Xinhe Wu, Yicheng Ye, Yadong Jin
- **发布时间**: 2026-11-24
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.31787v1](https://arxiv.org/pdf/2611.31787v1)
- **相关度评分**: 10/10

#### 英文摘要

Scientific measurements reported in scholarly articles are often embedded in compound figures rather than available as machine-readable data. Recovering these measurements at literature scale requires an integrated workflow for figure localization, panel decomposition, chart identification, numerical reconstruction, and experimental context association. We present \textit{SciFig2Data}, an automated, high-throughput workflow for harvesting structured experimental data from scientific PDF repositories. The system integrates multi-scale document element detection, adaptive compound figure decomposition, two-stage OCR-based semantic filtering, Swin-based chart classification, and instruction-guided multimodal large language model (MLLM) reconstruction. It further incorporates directory-level batch execution, caching, and structured logging to support large-scale processing. We demonstrate the workflow on two biomedical literature corpora comprising 605 toxicology and pharmacology articles and 551 lipid nanoparticle (LNP) articles. The pipeline successfully reconstructed 468 and 242 tabular outputs from the respective corpora, illustrating its practical applicability to literature-scale scientific data harvesting. By associating reconstructed measurements with caption-derived experimental metadata, SciFig2Data provides a workflow for transforming graphical evidence in scholarly publications into structured, context-enriched data records for downstream AI4Science applications.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5a90c071-6f

---

### 6. Interactive Neural Computers

- **ArXiv ID**: [2611.32811v1](https://arxiv.org/abs/2611.32811v1)
- **作者**: Ross Murphy, Marcel Hedman, Gabriel Brostow
- **发布时间**: 2026-11-24
- **分类**: cs.AI, cs.NE, cs.SC
- **PDF**: [https://arxiv.org/pdf/2611.32811v1](https://arxiv.org/pdf/2611.32811v1)
- **相关度评分**: 10/10

#### 英文摘要

Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents. This is limiting when someone needs a different workflow, or an interface suited to hands-free use or a disability. We explore an overlooked alternative. Rather than training an agent to operate an existing computer, we train a generative model to be the computer, predicting each next screen from past screens and the user's mouse and keyboard actions. Treating a desktop as an interactive world model raises problems that natural-video world models largely avoid. Without a camera pose to index memory, the model must remember content that has left the screen without any geometric cues. Arithmetic in a terminal has to be exactly right, not merely plausible. Small interface text must also stay legible at interactive frame rates. Our Interactive Neural Computer is structured like a Neural Turing Machine and starts to address these problems with three modules trained end to end from pixels and actions. A surprise-gated slot memory, supervised by latent next-frame prediction (MEMORY-JEPA), stores what is off screen. An exploratory query bridge brings in the reasoning of a pretrained VLM, and a residual renderer predicts only the latent changes between frames. In long closed-loop rollouts, our model recalls occluded files in 64.2% of trials (chance is 33.3%), compared with at most 56.0% for recurrent and sliding-window baselines. It also raises terminal-text OCR accuracy from 1.3% to 50.1%. Finally, because the memory is explicit, it can be transplanted at test time to causally change what the model renders.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b789e5ad-c4

---

### 7. DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models

- **ArXiv ID**: [2611.31969v1](https://arxiv.org/abs/2611.31969v1)
- **作者**: Yunchao Ke, Yanzhe Hu, Yi Yang, Jiachun Jin, Zhihong Liu...
- **发布时间**: 2026-11-24
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.31969v1](https://arxiv.org/pdf/2611.31969v1)
- **相关度评分**: 10/10

#### 英文摘要

Flow-based diffusion models have become a mainstream paradigm for text-to-image generation, where task-specific post-training produces specialist models with complementary strengths. Multi-teacher on-policy distillation (OPD) offers an efficient way to consolidate these specialists into a single unified student. Recent methods strengthen supervision through teacher extrapolation, constructing stronger proxy teachers that allow distilled students to surpass the original specialists. However, their extrapolation directions remain defined solely by frozen teacher and reference models, leaving the student's own training progress unexploited. To address this limitation, we introduce DexOPD, a dual-extrapolation on-policy distillation method for diffusion models. DexOPD retains extrapolated teacher supervision while leveraging a lagging historical student as the reference for student self-extrapolation. Sampling across multiple self-extrapolation gains from shared initial noise broadens exploration along the student's evolving trajectory, and task rewards convert pairwise differences in candidate quality into a normalized auxiliary regression direction. Empirically, we evaluate DexOPD on GenEval, OCR, and DrawBench. The resulting unified SD3.5-Medium student achieves a GenEval reward of 0.9736, an OCR score of 0.9515, and a DrawBench Aesthetic score of 6.4875, surpassing the corresponding specialist teachers as well as all evaluated OPD and multi-task reinforcement learning baselines across these three benchmarks while preserving standard single-model inference.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8707f3ff-62

---

### 8. Biomechanically Grounded Prediction of Selective Motor Control and Clinical Outcomes from Infant Video

- **ArXiv ID**: [2611.32890v1](https://arxiv.org/abs/2611.32890v1)
- **作者**: Divya Joshi, Ruize Yang, Colleen Peyton, R. James Cotton
- **发布时间**: 2026-11-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.32890v1](https://arxiv.org/pdf/2611.32890v1)
- **相关度评分**: 10/10

#### 英文摘要

Early identification of cerebral palsy (CP) relies on observational assessments of spontaneous infant movement, such as the General Movement Assessment (GMA) and the Baby Observational Selective Control AppRaisal (BabyOSCAR), which require trained raters and substantial scoring time. Existing automated approaches derive hand-engineered features from two-dimensional keypoints, which describe image-plane motion rather than the three-dimensional behavior of individual joints. We present Baby Biomechanical 3D Body (BB3D), an infant-adapted, biomechanical pipeline that estimates joint-angle trajectories from single-camera video. Against a multi-view markerless motion capture reference in 17 infants, BB3D's median Procrustes-aligned error was 17.5~mm for joint centers and 20.4~mm for marker sites. A spatio-temporal transformer, pretrained on BB3D joint-angle trajectories from 1k+ single-camera recordings, and fine-tuned on 550 videos from 350 infants, predicted each individual BabyOSCAR item with a mean within-site AUC of 0.79 and the BabyOSCAR total with a Spearman correlation of 0.86 on held-out recordings. Without being trained on diagnosis, the predicted total separated infants with CP from those without CP with an AUC of 0.86, exceeding a replicated two-dimensional feature classifier (0.67) but below the expert clinician rater's total (0.97). Predicted scores also carried information about functional ability and body distribution, though less than expert clinician scores. These results show that biomechanically grounded representations of monocular video can support scalable, joint-level assessment of selective motor control in infancy

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: aab29e0c-f8

---

### 9. Beyond Fixed-Context Likelihood: Zero-Shot AI-Generated Text Detection via Context Perturbation Discrepancy

- **ArXiv ID**: [2611.32778v1](https://arxiv.org/abs/2611.32778v1)
- **作者**: Yifan Tang, Jingran Li, Yihao Wang, Zhen Yang, Jianyi Liu...
- **发布时间**: 2026-11-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.32778v1](https://arxiv.org/pdf/2611.32778v1)
- **相关度评分**: 10/10

#### 英文摘要

The same increase in token log probability from earlier context can be typical at one position and unusually large at another. We introduce Context Perturbation Discrepancy (CPD), a zero-shot detector that measures this gain relative to what a single pretrained language model expects. Keeping the passage fixed, CPD scores each observed token under its full prefix and under a short window of recent tokens. Under the full-prefix distribution, the expected gain equals the KL divergence from that distribution to the restricted-prefix distribution. CPD subtracts this expectation from each observed gain and scales the sum of the signed deviations by its analytical reference standard deviation. On unedited human and AI texts from GEN, DetectRL-X, and HART, subtracting the expected gain raises AUROC by 32.78-35.81 percentage points at the same variance scale. CPD outperforms seven zero-shot baselines, averaging 94.80% AUROC and 79.60% recall at a 5% false-positive rate. On original and edited HART passages, the same scores separate texts more clearly by draft origin than by the benchmark's final-expression labels (89.15% versus 65.50% AUROC). Code is available at https://github.com/BUPT-tyf/CPD.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 30599c4f-89

---

### 10. Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action

- **ArXiv ID**: [2611.33137v1](https://arxiv.org/abs/2611.33137v1)
- **作者**: Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner, Angela Dai
- **发布时间**: 2026-11-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.33137v1](https://arxiv.org/pdf/2611.33137v1)
- **相关度评分**: 10/10

#### 英文摘要

We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves performance over alternative synthetic datasets. In addition, we introduce a mobile manipulation benchmark, evaluating vision-language-action models performing physical pick and place in diverse 3D scenes with realistic layouts, and using our part annotations to also score where each object is grasped. Our dataset will be released publicly to facilitate research in visual and embodied AI.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: de833933-bd

---

### 11. Latent Merger: Latent-Space Composition of Hypernetwork-Generated LoRAs

- **ArXiv ID**: [2611.33048v1](https://arxiv.org/abs/2611.33048v1)
- **作者**: Yanlai Yang, Minki Kang, Divyam Madaan, Sung Ju Hwang, Mengye Ren
- **发布时间**: 2026-11-25
- **分类**: cs.LG, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.33048v1](https://arxiv.org/pdf/2611.33048v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent work proposes hypernetworks that convert a document into a low-rank parameter update (LoRA) in a single forward pass, enabling fast injection of new knowledge into a frozen LLM. However, storing separate LoRA adapters for each document can be unsustainable in streaming settings. In this paper, we study the problem of composing hypernetwork-generated LoRAs using two representative systems, Doc-to-LoRA and SHINE. We show that hypernetwork-generated LoRAs have a geometry sharply different from directly fine-tuned LoRAs. They exhibit greater spectral concentration and stronger cross-document alignment than next-token prediction and QA fine-tuned adapters, which are diffuse and nearly orthogonal across documents. Guided by this observation, we propose latent-space LoRA merging. We compose the intermediate hypernetwork latents and then decode the merged latent through the frozen LoRA-generation head. We show that latent-space merging techniques consistently improve over weight-space and factor-space baselines while preserving a single fixed-rank adapter. These results support latent-space composition as a promising mechanism for combining hypernetwork-generated LoRAs under a fixed output-rank budget.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8d0273de-3b

---

### 12. SOARS: System One Assisted Reranking for Agentic Search

- **ArXiv ID**: [2611.32917v1](https://arxiv.org/abs/2611.32917v1)
- **作者**: Amin Bigdeli, Liye Fu, Fattane Zarrinkalam, Joel Stremmel, Elizabeth Lingg
- **发布时间**: 2026-11-25
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.32917v1](https://arxiv.org/pdf/2611.32917v1)
- **相关度评分**: 10/10

#### 英文摘要

Deep search agents address complex information needs through iterative retrieval and reasoning, where the relevance of retrieved evidence influences downstream performance. Existing rerankers improve retrieval effectiveness but introduce substantial latency and cost when invoked throughout the search trajectory. We introduce SOARS, a training-free framework leveraging a System One model for fast, calibrated relevance estimation. At each search step, SOARS selects query-relevant passages from long documents and reranks candidates in a single call, jointly considering the original question and agent-generated sub-query. Across six LLM backbones on BrowseComp-Plus and WebShaper, SOARS consistently improves answer accuracy and evidence recall while reducing search calls, end-to-end latency, and inference cost. On BrowseComp-Plus, it improves GPT-5.4 Mini's accuracy from 73.9% to 84.7% while reducing search calls from 23 to 14, demonstrating the potential of System One reranking for more effective and efficient deep search.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f6001af9-a2

---

### 13. OmniAct: One Policy, One Million Embodiments

- **ArXiv ID**: [2611.33158v1](https://arxiv.org/abs/2611.33158v1)
- **作者**: Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo...
- **发布时间**: 2026-11-25
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.33158v1](https://arxiv.org/pdf/2611.33158v1)
- **相关度评分**: 10/10

#### 英文摘要

A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how differences in robot morphology should shape manipulation strategies. We introduce OmniAct, a cross-embodiment manipulation policy that conditions directly on each robot's kinematics in a specific scene to produce embodiment-specific behavior. This kinematic graph represents the robot's joint positions, motion axes, and connectivity to its visual observation, allowing the policy to account for how its embodiment related to objects and surfaces in the scene. A flow-matching policy predicts relative joint motions for each node, enabling control across robots with different degrees of freedom and kinematic configurations. To learn how physical structure shapes behavior at scale, we procedurally design and filter one million physically feasible robot embodiments; next, we develop algorithms to generate robot trajectories in simulation for all embodiments; finally, we train across diverse simulated manipulation tasks. On 2,000 embodiment-scene-held-out evaluation episodes, OmniAct achieves 63.0% success, compared to 17.8% for pi 0.5 and 57.9% for the strongest baseline; on the task families GPT-6 Astra was evaluated on, it achieves 64.7% against GPT-6 Astra's 41.1%. On a previously unseen real-world robot, it achieves nearly twice the success rate of the next best method, MolmoAct2. Beyond task success, we observe that OmniAct learns distinct manipulation strategies that exploit the capabilities and accommodate the limitations of different morphologies. Project: https://omniact.github.io/

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d4bc5e96-f6

---

### 14. PointX: Multi-View Consistent Intrinsics by Querying Surface Points

- **ArXiv ID**: [2611.33157v1](https://arxiv.org/abs/2611.33157v1)
- **作者**: Miguel Farinha, Sam Sartor, Iliyan Georgiev, Giuseppe Vecchio, Ronald Clark...
- **发布时间**: 2026-11-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.33157v1](https://arxiv.org/pdf/2611.33157v1)
- **相关度评分**: 10/10

#### 英文摘要

The appearance of a scene is determined by the albedo, roughness, metallicity and normal of every point on its surface, and by the light that reaches it, its irradiance. Recovering these intrinsics from images is ambiguous, and methods that predict them per pixel give the same surface point a different decomposition in every view. We introduce PointX, a simple feed-forward model that predicts intrinsics per 3D surface point instead. A multi-view transformer encodes a set of unposed images, and for any queried surface point, PointX pools the point's tokens across the views in which it appears and decodes the point's intrinsics once. Each point of a 3D reconstruction of the scene, such as a point cloud or a mesh, thus receives a single prediction, which is exactly consistent across views by construction and enables view-consistent relighting and editing. The same model also predicts per-view maps, from one image or many, by querying the point seen at every pixel. These maps agree across views up to the precision of the estimated geometry and correspondences. PointX is significantly more consistent than existing methods, while remaining competitive in accuracy from a single image and improving as views are added. Project page: https://pointx-paper.github.io/

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cd1e5ada-6f

---

### 15. BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles

- **ArXiv ID**: [2611.33151v1](https://arxiv.org/abs/2611.33151v1)
- **作者**: Yuwei Yang, Xiaoxiao Sun, Alejandro Lozano, Yuan-Sen Ting, Yuhui Yuan...
- **发布时间**: 2026-11-25
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.33151v1](https://arxiv.org/pdf/2611.33151v1)
- **相关度评分**: 10/10

#### 英文摘要

The development of biomedical vision-language models (VLMs) with contrastive image-text pretraining has been driven by scaling to increasingly large and diverse image-text datasets. Beyond scaling, further progress can come from learning richer representations from existing data. We hypothesize that the structure of scientific literature itself provides an additional source of supervision: figures, panels, captions, and accompanying article text encode rich relationships across modalities. Yet, treating these as independent image-text pairs overlooks their relationships. To address this limitation, we incorporate these structural relationships into contrastive image-text supervision. We preserve exact image-text matches while introducing weaker positive supervision for related pairs, such as a panel and the caption of a sibling panel. We upweight cross-article negatives of the same content type to encourage finer discrimination. We also enrich panel descriptions using visual content, original figure captions, and mentioning paragraphs. Pairing panels with these descriptions and whole figures with their original captions yields Loom52M, a dataset of 52.4 million image-text pairs spanning scientific charts and biomedical images. Using Loom52M, BioLoom (DFN-2B) achieves 56.82% domain-balanced mean accuracy across 67 zero-shot classification tasks from 43 datasets in 10 domains, compared with 48.77% for MedPMC-CLIP. On BioLoomBench with concise captions and BioMedFlickr, it achieves bidirectional mean Recall@1 of 63.20% and 10.59%, versus 46.37% and 7.55% for the respective strongest evaluated baselines, BiomedCLIP and MedPMC-CLIP. Code, datasets, benchmarks, and models are available at https://bioloom-clip.github.io/.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4a8fbc7f-a6

---
