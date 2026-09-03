# OCR arXiv Daily Pro — 2026-09-03

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-02 09:10 - 2026-09-03 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering

- **ArXiv ID**: [2609.02486v1](https://arxiv.org/abs/2609.02486v1)
- **作者**: Adrien Mialland, Marc Plantevit, Julien Gallois, Céline Robardet
- **发布时间**: 2026-09-02
- **分类**: cs.IR, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.02486v1](https://arxiv.org/pdf/2609.02486v1)
- **相关度评分**: 10/10

#### 英文摘要

Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to identify document pages relevant to a user query, before answer generation by a Large Vision-Language Model (LVLM). Existing approaches typically retrieve a fixed top-$k$ number of pages regardless of query complexity, which increases LVLM latency and may degrade answer accuracy. We introduce ViSAR (Visual Semantic Activation Retrieval), a training-free adaptive-$k$ retrieval method for late-interaction visual document retrieval. ViSAR operates directly in the embedding space to construct a query-conditioned page-level similarity matrix that highlights query-relevant semantics and dynamically determines the number of pages to retrieve. Across multiple encoders and LVLMs, ViSAR retrieves compact, query-adapted page sets that reduce RAG latency by up to 58.7\%, while maintaining or improving answer accuracy compared with fixed top-$k$ and adaptive retrieval heuristics. Furthermore, we show that the similarity matrix structure correlates with answer accuracy, suggesting future directions for retrieval quality-aware document understanding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images

- **ArXiv ID**: [2609.02207v1](https://arxiv.org/abs/2609.02207v1)
- **作者**: Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov
- **发布时间**: 2026-09-02
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.02207v1](https://arxiv.org/pdf/2609.02207v1)
- **相关度评分**: 10/10

#### 英文摘要

Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR errors, layout structure, and visual noise determine whether sensitive information is actually removed. Existing PII benchmarks are mostly text-centric and do not measure document-level redaction risk: a page remains unsafe if even one identifier is missed. We introduce LeakageBench, a challenge set of 500 document images with 11,954 GDPR-aligned PII annotations spanning direct identifiers, linkage keys, and contextual re-identification surfaces. We evaluate generic OCR pipelines, commercial and task-adapted OCR-dependent detectors, and OCR-free vision-language models using entity-level F1, group-wise leakage, and document-level leakage metrics. Code Interpreter raises GPT-5.5 localization F1 from 0.090 to 0.249, but critical page-level leakage remains 0.968. These results show that stronger detection and tool assistance improve localization without making most pages safe for release. LeakageBench provides a diagnostic benchmark for high-recall, spatially grounded PII redaction in document images.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs

- **ArXiv ID**: [2609.02679v1](https://arxiv.org/abs/2609.02679v1)
- **作者**: Urja Pawar, Rajitha Ramanayake, Owen O'Neill, Nabeel Kemal, Abhishek Mandal...
- **发布时间**: 2026-09-02
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.02679v1](https://arxiv.org/pdf/2609.02679v1)
- **相关度评分**: 10/10

#### 英文摘要

When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-review capacity. When no trusted context or reference document is available, we study two signals accessible through black-box model APIs: semantic entropy, which measures disagreement among sampled response meanings, and uncertainty derived from token log-probabilities. Their failure modes can be complementary: semantic entropy becomes uninformative when responses form one semantic cluster, while token uncertainty can miss consistently confident errors. We extend token-based uncertainty detection by aggregating token-level signals across sampled responses through our TopK method, evaluate the hybrid CoCoA method, which combines target-response uncertainty with semantic dissimilarity, and propose and study two supervised methods: Gated, which routes single-cluster cases to an aggregated-token-feature classifier, and Stacked, which learns jointly from semantic uncertainty and broader token features. We evaluate seven benchmarks, including five public benchmarks (four text datasets and multimodal handwritten-cheque extraction) and two constructed benchmarks (Financial Summaries and Long-Text QA), using four language models. In our evaluation across models and datasets, Stacked gave the best performance in nearly half of the cases, while TopK and CoCoA remain competitive without supervised training labels, although their thresholds require careful calibration. No method is universally strongest. We therefore evaluate performance at false-positive-rate budgets from 1% to 15%, assess their sensitivity to generation and calibration choices, and examine variation across dataset characteristics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework

- **ArXiv ID**: [2609.02861v1](https://arxiv.org/abs/2609.02861v1)
- **作者**: Cagri Temel
- **发布时间**: 2026-09-03
- **分类**: cs.RO, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.02861v1](https://arxiv.org/pdf/2609.02861v1)
- **相关度评分**: 10/10

#### 英文摘要

Autonomous robots powered by deep learning face a fundamental auditability challenge: when incidents occur, investigators cannot reconstruct why the system made specific decisions. This paper presents TRACE (Transparent Reasoning Architecture for Credible Execution), a decision framework that ensures every autonomous action can be traced back to sensor evidence through documented causal chains. The framework organizes decision-making into four auditable layers: Semantic Perception for evidence-grounded entity recognition, Belief Reasoning for probabilistic state estimation with causal graphs, Action Synthesis for constraint-aware planning with counterfactual documentation, and Execution Verification for compliance monitoring. TRACE is model-agnostic yet designed to integrate learning-based perception modules (CNNs, transformers) while preserving decision-level auditability. We evaluate the framework using three objective metrics: Evidence Traceability (sensor-to-decision linkage), Decision Reconstructability (post-hoc analysis capability), and Temporal Continuity (audit trail completeness). Experimental evaluation on warehouse robot navigation demonstrates that TRACE achieves 98.6% evidence traceability, 99.0% temporal continuity, and 98.1% decision reconstructability across 500 simulated decision cycles. Post-hoc methods like LIME provide feature attributions but lack the artifact structure needed for decision-level reconstruction. The framework addresses EU AI Act requirements for high-risk system transparency and contributes to Explainable AI for safety-critical autonomous systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. GDB-Reward: From Evaluation Metrics to Training Rewards for Graphic Design

- **ArXiv ID**: [2609.02813v1](https://arxiv.org/abs/2609.02813v1)
- **作者**: Adrienne Deganutti, Purvanshi Mehta, Simon Hadfield, Andrew Gilbert
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02813v1](https://arxiv.org/pdf/2609.02813v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-to-image models excel at natural image synthesis but struggle with graphic design, where success depends on satisfying precise constraints on typography, layout, color, and visual communication. While prompt optimization offers an attractive alternative to expensive diffusion model fine-tuning, learning prompts for frozen image generators requires informative reward functions despite the entirely non-differentiable generation process. Reinforcement learning does not require differentiable objectives; it requires only scalar rewards capable of ranking candidate outputs. This raises a simple question: can design evaluation metrics themselves become reinforcement learning rewards? Our central contribution is GDB-Reward, a framework that systematically transforms heterogeneous graphic design evaluation metrics into a unified reinforcement learning reward. Experiments demonstrate that GDB-Reward provides an effective optimization objective, substantially improving adherence to the design specification in perceptual quality, rendering fidelity, and spatial accuracy while keeping the image generator entirely frozen. More broadly, our results demonstrate that heterogeneous, non-differentiable evaluation metrics can move beyond passive benchmarking to become effective optimization objectives for reinforcement learning in domains where differentiable supervision is unavailable.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented Factory Agents

- **ArXiv ID**: [2609.02760v1](https://arxiv.org/abs/2609.02760v1)
- **作者**: Vasileios Rizeakos, Georgios Paisios, Alexandros Machairas, Michael Birbas, Athanasios Bachoumis
- **发布时间**: 2026-09-03
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.02760v1](https://arxiv.org/pdf/2609.02760v1)
- **相关度评分**: 10/10

#### 英文摘要

On-premise assistants can give factory workers conversational access to machine documentation, but models capable of the task rarely fit shop-floor hardware. We show that after structural compression and retrieval-grounded adaptation, model size is no longer a reliable predictor of adapted answer quality: general capability falls almost linearly with parameter count, while judged retrieval-augmented answer quality does not. We therefore treat deployment as a post-adaptation selection problem, committing one sub-network per device on judged answer quality and measured on-device throughput under a configurable general-capability floor and memory budget; rules that optimize size, speed, or quality alone each give up capability or throughput. A weight-shared supernetwork trained with sandwich-style in-place distillation keeps this selection inexpensive. In a manufacturing-manual case study, extraction costs 13.7 percent of the unpruned model's judged quality and retrieval-grounded distillation returns it to within 4.6 percent, recovering two thirds of the loss, and the same assistant runs across three heterogeneous edge tiers at 1.3 to 5 watts standby.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection

- **ArXiv ID**: [2609.02745v1](https://arxiv.org/abs/2609.02745v1)
- **作者**: Max Nelson, Hanoz Bhathena, Aviral Joshi, Saket Sharma
- **发布时间**: 2026-09-02
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.02745v1](https://arxiv.org/pdf/2609.02745v1)
- **相关度评分**: 10/10

#### 英文摘要

Selecting a retrieval model for a production RAG system requires reliable comparative evaluation, but obtaining relevance judgments at scale is expensive and difficult to repeat as new candidate systems arrive. We study pooled LLM evaluation, in which an LLM judges the union of documents retrieved by the current set of candidate systems, and the pool is then expanded incrementally as new systems are introduced by judging only the new documents they contribute. These judgments are reused to evaluate all systems on a common basis. We validate this approach on four retrieval benchmarks with 11 systems spanning dense, sparse, and hybrid configurations, and deploy it to compare 62 retrieval configurations for a financial news QA system. Pooled LLM rankings correlate strongly with gold-standard evaluation across datasets, and 97% of pairwise system orderings are preserved once bootstrap uncertainty in the qrels is taken into account. In production, document overlap yields 65-80% judgment reuse and up to 4.9x lower evaluation cost, allowing teams to benchmark new retrieval candidates without re-judging previously assessed documents. These results suggest pooled LLM evaluation is a practical and cost-effective workflow for incremental retrieval model selection in deployed systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis

- **ArXiv ID**: [2609.02473v1](https://arxiv.org/abs/2609.02473v1)
- **作者**: Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim, Zicheng Li, Xuanqi Peng...
- **发布时间**: 2026-09-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.02473v1](https://arxiv.org/pdf/2609.02473v1)
- **相关度评分**: 10/10

#### 英文摘要

Ontology rankers remain useful for rare-disease diagnosis because each candidate can be traced to matched patient phenotypes. Large language models (LLMs) can generate differential diagnoses from the same patient description, but their predictions lack an equally clear evidence trail. Rather than asking which system should replace the other, we ask whether an LLM can improve the ranker without giving up its evidence. Our behavior-based fusion model examines the two ranked lists, their agreement, and the ontology support behind each candidate, and learns how much to rely on each system for the individual case. Before comparison, we remove a documented test-set leakage pathway caused by benchmark cases and ontology annotations being derived from the same publications. Across eight open LLMs, fusion improves Phenomizer Recall@1 by 7.86 percentage points on Phenopacket Store and 20.18 points on RAMEDIS. When paired with DeepSeek-V4-Flash through an API, a fusion model trained only on the other LLMs improves Recall@1 from 0.1657 to 0.2176, a 5.19-point gain, without retraining. For 90.8% of correct fused diagnoses, the disease retains candidate-level ontology evidence that can be inspected. These results show that LLMs can strengthen an established diagnostic tool without discarding the structured evidence that makes it useful.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. WinoQueer-NL: Assessing Bias in Dutch Language Models toward LGBTQ+ Identities

- **ArXiv ID**: [2609.02651v1](https://arxiv.org/abs/2609.02651v1)
- **作者**: Jiska Beuk, Gerasimos Spanakis
- **发布时间**: 2026-09-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.02651v1](https://arxiv.org/pdf/2609.02651v1)
- **相关度评分**: 10/10

#### 英文摘要

While English language models have been widely examined for anti-queer bias, Dutch models remain understudied. To address this gap, we developed a culturally and linguistically adapted Dutch dataset based on the English WinoQueer benchmark, containing pairs of stereotypical and counter-stereotypical sentences. To validate and expand it, we conducted an online survey with 43 Dutch queer participants, confirming 145 of 171 stereotypes as culturally relevant and identifying 22 new biases through free-text responses. The final released dataset, comprising 42,906 sentences, was evaluated using a range of Dutch-specific and multilingual models, including both masked language models (MLMs) and autoregressive language models (ARLMs), with bias measured via a score comparing log-likelihoods of stereotypical versus counter-stereotypical sentences. While the mean bias score across models appeared neutral (~50%), closer analysis revealed significant disparities: some models favored stereotypical sentences up to 97% of the time for transgender identities, but only 6% of the time for gay-related pairs, with transgender and non-binary identities consistently receiving the highest bias scores. Our findings highlight the importance of culturally grounded datasets for evaluating and mitigating biases that disproportionately impact marginalized groups in Dutch language models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

- **ArXiv ID**: [2609.02886v1](https://arxiv.org/abs/2609.02886v1)
- **作者**: Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao...
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02886v1](https://arxiv.org/pdf/2609.02886v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B--33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacher-forced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation

- **ArXiv ID**: [2609.02864v1](https://arxiv.org/abs/2609.02864v1)
- **作者**: Yutong Liu, Nan Huang, Xu Cao, James M. Rehg
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02864v1](https://arxiv.org/pdf/2609.02864v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introduce RIG-BENCH, a novel comprehensive benchmark that systematically evaluates Reasoning-driven Image Generation (RIG) across four cognitively demanding domains: Concept-based, Transformation-based, Pattern & Structure, and Scenario-based. Featuring 2000 curated samples, RIG-BENCH serves as a rigorous stress test for RIG. Our extensive evaluations of state-of-the-art UGMs and image/video generation models reveal a significant reasoning-generation gap, wherein models frequently produce locally plausible but globally illogical outputs. RIG-BENCH provides a vital diagnostic framework to guide the development of next-generation, logically grounded UGMs and world simulators.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation

- **ArXiv ID**: [2609.02860v1](https://arxiv.org/abs/2609.02860v1)
- **作者**: Yu Tian, Xintong Jiang, Jan Franklin Adamowski, Shiv O. Prasher, Shangpeng Sun
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02860v1](https://arxiv.org/pdf/2609.02860v1)
- **相关度评分**: 10/10

#### 英文摘要

Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To address this, we propose PlantC2USeg, a deep transfer learning framework featuring cross-scale consistency learning to explicitly align features across spatial scales and an information-restricted decoding strategy that prevents reconstruction shortcuts and promotes robust adaptation. The resulting pre-training enables stable few-shot generalization across species and sensing conditions, while unified fine-tuning with inherited thresholds further reduces adaptation overhead. Under full supervision on Soybean3D, PlantC2USeg achieves the highest semantic IoU and instance mWCov among compared methods, at 91.91% and 94.62%. With 20 labeled samples, it leads both metrics at 89.78% and 90.27%; with only 10 samples, it retains the highest mWCov of 83.23% while achieving 83.19% IoU. Across HR3D, 10-shot transfer to tobacco, tomato, and sorghum averages 78.41% IoU and 79.42% mWCov, while 22-shot transfer to SYAU-Maize achieves the highest IoU and mRec at 92.75% and 93.51%. Furthermore, a leading category-averaged mIoU of 85.0% on ShapeNet Part demonstrates the framework's capability to handle diverse shape variations beyond agricultural domains. These results demonstrate that PlantC2USeg reduces overall adaptation effort under distribution shifts, enabling scalable plant phenotyping and transferable 3D representation learning beyond agriculture.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion

- **ArXiv ID**: [2609.02854v1](https://arxiv.org/abs/2609.02854v1)
- **作者**: Aidan Bradshaw, Marco Giordano, David Rode, Andreas Habersack, Elif Basokur...
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02854v1](https://arxiv.org/pdf/2609.02854v1)
- **相关度评分**: 10/10

#### 英文摘要

The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulation methods either optimize 3D keypoint accuracy without anatomical constraints or carry compute and capture infrastructure too heavy to deploy where CoM tracking is most useful. As a result, the metric CoM remains difficult for coaches and movement analysts to measure from a single camera where athletes train and compete. In this work, we introduce MuyBridge, an on-device system that estimates the athlete's segmental center of mass trajectory from a single phone camera video stream. MuyBridge couples a compact 2D pose network and a distilled single-step monocular depth network through an analytic metric fusion that uses anatomical and physical priors to anchor the metric CoM, requiring no 3D or task-specific supervision. Evaluated on the athletic movements of AthletePose3D (running, track and field, and figure skating), MuyBridge achieves 33-41 mm vertical CoM error and 2.3-6.6% absolute-relative range error (AbsRel) under a one-time calibration, and produces CoM estimates at the 63 FPS pose-estimation rate using asynchronous 2.86 Hz depth updates on iPhone 15. Code is available at: https://github.com/Abradshaw1/Muybridge

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation

- **ArXiv ID**: [2609.02847v1](https://arxiv.org/abs/2609.02847v1)
- **作者**: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02847v1](https://arxiv.org/pdf/2609.02847v1)
- **相关度评分**: 10/10

#### 英文摘要

Novel view synthesis from sparse inputs requires both geometric grounding from the observed views and generative priors of unobserved regions, motivating recent hybrid methods that combine reconstruction and generation. However, existing methods bridge the two with rendered images or explicit 3D representations such as point maps or 3D Gaussians. Generation is thus conditioned on a lossy and imperfect projection of the scene, inheriting its errors, and reconstruction receives no signal from generation to correct them. We present RoGe, an end-to-end unified reconstruction and generation framework that removes this explicit bridge. It targets roaming within a scene anchored by sparse views: given a few posed images and a camera trajectory, it synthesizes a temporally coherent video along that trajectory. From the sparse input views, RoGe builds an implicit scene representation with a feed-forward reconstruction model, and queries it with target camera rays to obtain per-view geometric features. These features are injected into a video diffusion model as conditioning, without any 3D intermediate. Both modules are trained jointly, so the generation objective directly shapes its own geometric conditioning. We conduct experiments on DL3DV, where RoGe outperforms reconstruction-based, generation-based, and hybrid baselines on image-level metrics and video-level temporal consistency. Ablations confirm that ray-queried implicit features outperform both raw reconstruction tokens and rendered RGB as conditioning, and that joint training brings further gains.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. Efficient All-in-One Weather Restoration using Spectral Harmonization

- **ArXiv ID**: [2609.02839v1](https://arxiv.org/abs/2609.02839v1)
- **作者**: Paula Garrido-Mellado, Daniel Feijoo, Yuning Cui, Alvaro Garcia, Marcos V. Conde
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.02839v1](https://arxiv.org/pdf/2609.02839v1)
- **相关度评分**: 10/10

#### 英文摘要

Adverse weather conditions such as rain, haze, and snow significantly degrade image quality, posing challenges for both human perception and physical AI. Existing restoration methods require large computational budgets, struggling to process high-resolution images and handle different degradations. In this paper, we present Frequency Reconstruction via Spectral Harmonization, a novel lightweight all-in-one restoration method that explicitly decomposes feature representations into high- and low-frequency components at each scale of a hierarchical encoder-decoder architecture. By combining spectral decomposition with spatial processing through Fourier-based skip connections, FReSH-IR captures complementary frequency information without sacrificing spatial detail. Our approach achieves similar restoration quality with 80% fewer parameters and operations than transformer-based models. Extensive experiments demonstrate that our method offers a great efficiency-performance trade-off, highlighting its practical applications in constrained-resource systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
