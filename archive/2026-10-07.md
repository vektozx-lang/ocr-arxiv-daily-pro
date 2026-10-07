# OCR arXiv Daily Pro — 2026-10-07

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-06 09:10 - 2026-10-07 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5ebfd1b4-69de-4

---

## 📄 论文详情

### 1. DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents

- **ArXiv ID**: [2610.08102v1](https://arxiv.org/abs/2610.08102v1)
- **作者**: Jike Zhong, Ritwick Chaudhry, Xuanbai Chen, Tianchen Zhao, Linghan Xu...
- **发布时间**: 2026-10-06
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.08102v1](https://arxiv.org/pdf/2610.08102v1)
- **相关度评分**: 10/10

#### 英文摘要

Conversational MLLM agents are increasingly expected to assist in professional workflows, from AI research and engineering design to product management and business operations. Yet this capability remains underexplored: existing benchmarks largely focus on informal, everyday interactions and personal-life scenarios featuring photographic natural images, isolated static artifacts, and recall-oriented questions. In contrast, professional scenarios often involve structured, information-heavy artifacts that undergo frequent revisions and authority updates, and compositional queries requiring reconciliation of many artifact versions while tracking state precisely. To address these challenges, we introduce DSV-Mem, a benchmark for evaluating Dense Stateful Visual Memory. DSV-Mem comprises expert-reviewed scenarios and 1,000 questions across five user-oriented categories (Current State, Past State, Derived State, Change History, and Conflict/Refusal). A Hartley-inspired criterion favors questions with broader visual-evidence inspection demands. We also introduce a generation harness that produces evaluation suites by decoupling state-transition synthesis from conversation filling. Evaluation over 27 configurations spanning frontier and open-weight models and memory management methods reveals that the strongest baseline scores below 45% on DSV-Mem. Analysis surfaces findings: 1) multimodality and information density both contribute to difficulty, but state evolution, particularly the number of governing updates, is the dominant tested factor. Raw conversation/haystack length, OCR, and arithmetic are not the primary bottlenecks; 2) models often fail to verify user premises against prior state updates before answering; 3) increased reasoning effort and memory management methods yield limited gains, whereas state-aware designs prove more effective. The benchmark and code will be publicly released.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 37645aaf-8de0-4

---

### 2. How Well Do LLMs Reason with Noisy Evidence? An Active Visual Reasoning Benchmark

- **ArXiv ID**: [2610.07751v1](https://arxiv.org/abs/2610.07751v1)
- **作者**: Bach Nguyen, Zhaonan Li, Mau Son Nguyen, Sanika Chavan, Nilay Kumar...
- **发布时间**: 2026-10-06
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.07751v1](https://arxiv.org/pdf/2610.07751v1)
- **相关度评分**: 10/10

#### 英文摘要

Real-world reasoning rarely reduces to static question answering: agents must actively gather information from tools and sensors that are often noisy and unreliable. Yet most existing active reasoning benchmarks assume that environmental feedback is trustworthy, or introduce noise without exposing an explicit, calibrated uncertainty signal, leaving open how LLMs should reason when the evidence itself is uncertain. We introduce VisualNoiseQA, a novel benchmark for active reasoning under noisy visual feedback. A text-only LLM must solve VQA problems by iteratively querying a fixed, off-the-shelf VLM treated as a stochastic visual sensor. For each query, we draw multiple samples and expose an empirical uncertainty signal via self-consistency, enabling the reasoner to probe from different angles and decide what to ask next and when to stop. Our construction is automatic and scalable: starting from diverse VQA sources and two noisy VLMs, we retain only questions where the sensor is inconsistent yet human-solvable. We evaluate multiple LLM reasoners on 1,000 instances spanning perception, chart understanding, and knowledge-intensive reasoning. VisualNoiseQA thus provides a controlled playground to study how different LLMs exploit uncertainty signals for robust reasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 74c223df-9548-4

---

### 3. A Systematic Study of Semantic ID Spaces for Generative Information Retrieval

- **ArXiv ID**: [2610.08732v1](https://arxiv.org/abs/2610.08732v1)
- **作者**: Alexia Allal, Hicham Randrianarivo, Sylvain Lamprier
- **发布时间**: 2026-10-07
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.08732v1](https://arxiv.org/pdf/2610.08732v1)
- **相关度评分**: 10/10

#### 英文摘要

Generative Information Retrieval (GIR) has emerged as a transformative paradigm, shifting document retrieval from a traditional "retrieve-and-rank" workflow to sequence-to-sequence generation, where a model directly predicts document identifiers (DocIDs). While the semantic design of these DocIDs is known to be critical for performance, a fundamental question remains under-explored: what makes a good DocID? Current approaches rely heavily on computationally expensive downstream evaluations, hindering systematic analysis and rapid iteration. In this work, we address this challenge by presenting a comprehensive study on the properties, metrics, and trade-offs that define effective numerical DocIDs. Specifically, our contributions are threefold: First, we propose a unified framework that unifies Product Quantization (PQ) and Residual Quantization (RQ), and their hybrid variants within a single design space. This enables us to systematically study key DocID properties, such as hierarchy versus parallelism, as well as the impact of hyperparameters like DocID length and codebook size. Second, we define a suite of training-free, intrinsic metrics, to quantify DocID quality and evaluate structural fidelity without the overhead of full model training. Through extensive experiments on MS MARCO 300K and NQ320K, we analyze how these structural properties influence retrieval effectiveness.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b13f9dac-4bf2-4

---

### 4. Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval

- **ArXiv ID**: [2610.08716v1](https://arxiv.org/abs/2610.08716v1)
- **作者**: Hicham Randrianarivo, Logan Renaud, Alexia Allal
- **发布时间**: 2026-10-07
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.08716v1](https://arxiv.org/pdf/2610.08716v1)
- **相关度评分**: 10/10

#### 英文摘要

Generative retrieval trains a language model to generate the identifier of a relevant document. Recent work replaces the autoregressive decoder with diffusion, but changes identifiers, training recipe and decoding at once, so differences cannot be credited to the paradigm. On NQ320K and MS300K, we train autoregressive, masked-diffusion and block-diffusion models with residual-quantised, product-quantised and random identifiers. With identifier length and training budget fixed, we decode each model in several ways. Decoding alone moves a diffusion model's Hit@1 by 6.6 to 13.7 points. Our reference diffusion decoding, generate-and-match, generates an identifier, then retrieves the closest corpus identifiers. The generated identifier is right for 14-21% of NQ320K queries. We test one-pass scoring to decode diffusion retrievers: the model reads a fully masked identifier once, and each document is scored by its codes' probabilities. It matches or beats generate-and-match in 11 of 12 settings. Autoregressive models still lead in Hit@1; on NQ320K, the lead comes from the model, not beam search. Starting from one sampled identifier, one-pass scoring removes 46-83% of masked diffusion's deficit to beam search; from generate-and-match, at most a quarter. On NQ320K, every paradigm largely memorises which identifier answers which query: random identifiers keep 83-90% of the Hit@1 of residual-quantised ones. There, product-quantised identifiers lead residual-quantised ones by 3.4 points in the autoregressive model and by -0.7 to +3.6 in diffusion models; across decodings, AR's gap exceeds diffusion's by 1.5-2.3 points, around our 2-point threshold. Paradigm comparisons must report each paradigm at its own recipe and best decoding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b28156e2-9f10-4

---

### 5. Towards In-Parameter Memory Augmentation for Large Language Models

- **ArXiv ID**: [2610.08630v1](https://arxiv.org/abs/2610.08630v1)
- **作者**: Haoyu Huang, Zhongwei Xie, Jiaxin Bai, Yisen Gao, Hong Ting Tsang...
- **发布时间**: 2026-10-07
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.08630v1](https://arxiv.org/pdf/2610.08630v1)
- **相关度评分**: 10/10

#### 英文摘要

Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. \textbf{In-parameter memory} offers a complementary substrate: reusable memory information is represented in model parameters, adapters, or other parameter-like objects that are composed into the forward pass at inference time. This survey focuses on methods that augment LLMs with such parametric memory at deployment: a memory-bearing parameter object is plugged into the forward pass during inference, whether it is acquired before or during deployment. We organize the landscape with two orthogonal axes: \textbf{Parameter Placement}, which includes Embedding, Attention, FFN layers, or Hybrid when two or more layers are used; and \textbf{Parameter Acquisition Time}, which distinguishes methods whose memory object is acquired during deployment (online) from those acquired before it (offline). We clarify boundaries, conduct comparisons, and discuss open directions in interference, safety, co-design with ICL, and recursive self-improvement.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f9408d0b-817f-4

---

### 6. Incidental information contaminates patient notes and disrupts clinical reasoning in large language models

- **ArXiv ID**: [2610.08585v1](https://arxiv.org/abs/2610.08585v1)
- **作者**: Krithik Vishwanath, Brandon Ye, Anton Alyakin, John E. Markert, Aaron Hsieh...
- **发布时间**: 2026-10-06
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.08585v1](https://arxiv.org/pdf/2610.08585v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language models (LLMs) are increasingly relied upon to support ambient documentation and clinical reasoning. Here we examine the impact of a failure mode shared between these two applications by assessing their sensitivity to information incidental to the patient encounter. In 576 patient-clinician dialogues, we found that frontier models inserted small-talk exchanges into 35% of notes, while mean quality scores changed by at most 0.20 points on five-point scales. In 3.7% of frontier notes, models misattributed the asides or used them clinically. In 57 mock recorded consultations, background speech from a separate patient encounter at -10 dB leaked into 48.2% of transcripts, with contamination detected in 5.3% of downstream notes generated by four open-weight models. We propose a dual encoding hypothesis of clinical reasoning and distraction in LLMs, with preliminary evidence that LLM components associated with disruption by incidental information also support clinical reasoning. These findings support evaluating resistance to incidental information before clinical use, with safeguards that prevent contamination while preserving clinical reasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e7027252-79a6-4

---

### 7. World Models' Last Exam in Physics

- **ArXiv ID**: [2610.08791v1](https://arxiv.org/abs/2610.08791v1)
- **作者**: Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin...
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08791v1](https://arxiv.org/pdf/2610.08791v1)
- **相关度评分**: 10/10

#### 英文摘要

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks spanning mechanics, optics, fluids, thermal and phase-change phenomena, electromagnetism, and surface tension. Each task pairs an initial image and a generation prompt with predefined physical criteria, enabling interpretable tests of observable physical relationships without requiring reference videos. Its evaluator combines task-observability screening with task-specific quantitative physical measurements. Experiments on eight video generation models across 1,280 videos reveal persistent physical inconsistencies and substantial variation across tasks, with the best model achieving an overall score of 57.76 out of 100. Evaluation on synthetic videos with known physical relationships provides evidence for the validity of the measurement module under controlled conditions. The evaluator also achieves higher agreement with human judgments than a direct vision-language model baseline in both within-task rankings and pairwise comparisons. By combining coverage across physical domains with scores grounded in measurable evidence and explicit measurement limitations, the benchmark provides an interpretable basis for diagnosing physical inconsistencies and tracking progress toward physically consistent video world models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5d631870-f7f5-4

---

### 8. Building Rome from a Single Image

- **ArXiv ID**: [2610.08790v1](https://arxiv.org/abs/2610.08790v1)
- **作者**: Jiraphon Yenphraphai, Fang Li, Tianshuo Xu, Depu Meng, Quentin Herau...
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08790v1](https://arxiv.org/pdf/2610.08790v1)
- **相关度评分**: 10/10

#### 英文摘要

Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that redesigns such an object-centric generator, e.g., Trellis 2, to work on both indoor and outdoor scenes while retaining its prior. We accomplish this by (a) partitioning the scene into adaptive chunks that scale relative to the distance to the camera; nearby chunks have a smaller size to keep the finer detail, while distant structures, e.g., buildings, are covered by large chunks; (b) making the generator capture explicit 2D-3D correspondence by lifting image features and making the model aware of the free space, observed surface, and unobserved region; (c) synthesizing around 4,000 outdoor scenes to broaden the training data, as existing scene datasets are largely indoor. Experiments on Tanks and Temples, ScanNet++, and in-the-wild images show that our method outperforms all baselines in geometric accuracy and perceptual quality across both indoor and outdoor scenes.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 09472a37-15e8-4

---

### 9. 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction

- **ArXiv ID**: [2610.08782v1](https://arxiv.org/abs/2610.08782v1)
- **作者**: Shiqi Li, Sean Cho, Yijie Li, Fengzhi Guo, Bowen Wen...
- **发布时间**: 2026-10-07
- **分类**: cs.CV, cs.AI, cs.GR
- **PDF**: [https://arxiv.org/pdf/2610.08782v1](https://arxiv.org/pdf/2610.08782v1)
- **相关度评分**: 10/10

#### 英文摘要

Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-object states toward an interaction manifold, allowing the model to correct errors in translation, rotation, and alignment in a feed-forward manner. A key advantage of our generative formulation is that it naturally enables test-time guidance within the transport process. Rather than applying a separate post-hoc optimization after reconstruction, we directly steer the evolving generative states using physical interaction constraints and observed 2D evidence, allowing the reconstruction to be refined as part of the generative process itself. By training the generative model on diverse datasets, 4D-HOF generalizes robustly to challenging in-the-wild scenarios. Experiments on out-of-domain benchmarks show that 4D-HOF achieves state-of-the-art performance, producing more stable and accurate 4D hand-object reconstructions.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1bdafce0-1fbc-4

---

### 10. DepthWorld: 3D World Model for Robot Manipulation

- **ArXiv ID**: [2610.08780v1](https://arxiv.org/abs/2610.08780v1)
- **作者**: Jai Bardhan, Josef Sivic, Vladimir Petrik
- **发布时间**: 2026-10-07
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08780v1](https://arxiv.org/pdf/2610.08780v1)
- **相关度评分**: 10/10

#### 英文摘要

World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absorb it without disturbing strong pretrained video priors. We introduce a calibration pipeline that combines learned stereo depth with a joint factor graph, pooling all episodes collected from the same physical robot to recover its shared kinematic parameters alongside per-scene extrinsics. Applied to the DROID dataset, this yields DROID-3D, a calibrated 3D dataset providing dense metric depth and recalibrated multi-view extrinsics (achieving <0.7 px reprojection error on 90% of episodes for external cameras). We then train DepthWorld, a Stable Video Diffusion-based world model that jointly predicts multi-view RGB and depth via spatial latent tiling, leaving the pretrained Variational Autoencoder (VAE) unchanged. Depth supervision improves RGB prediction itself by +1.48 dB PSNR over an identical RGB-only baseline at equal training budget, while simultaneously yielding accurate metric depth for downstream geometric reasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cc51479a-524d-4

---

### 11. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing

- **ArXiv ID**: [2610.08779v1](https://arxiv.org/abs/2610.08779v1)
- **作者**: Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08779v1](https://arxiv.org/pdf/2610.08779v1)
- **相关度评分**: 10/10

#### 英文摘要

Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs in the target object's presence while preserving the surrounding action, teaching editors coordinated object behavior and source preservation. We further train a vision-language model (VLM) to predict interaction guidance from the same inputs. We introduce the ALIVE-interaction benchmark to assess interaction fidelity, source preservation, and visual coherence using a unified VLM-based protocol, and evaluate on the general video object insertion benchmark. Without VLM guidance, ALIVE improves Overall over the strongest evaluated baseline by 43.9% and 4.4% on the two benchmarks, respectively. VLM-predicted guidance further improves the ALIVE-interaction score by 0.95 points without additional user inputs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 965da587-edef-4

---

### 12. CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching

- **ArXiv ID**: [2610.08777v1](https://arxiv.org/abs/2610.08777v1)
- **作者**: Shangye Song, Dong Gong, Hong Jia, Yun Sing Koh, Xinyu Zhang
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08777v1](https://arxiv.org/pdf/2610.08777v1)
- **相关度评分**: 10/10

#### 英文摘要

Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explicitly exposes a signal they do not use: the controls for a chunk arrive before it is denoised, so a schedule derived from them costs no forward pass. To this end, we analyze adjacent chunks under different control regimes and find that structural similarity drops around action changes, while low-frequency structure remains more persistent than high-frequency detail. Motivated by these observations, we propose CtrlCache, a training-free control-aware caching framework that adapts computation to the current control sequence. Specifically, the action-aware scheduling and refresh policy detects action changes across and within chunks, and labels each chunk as initial, transition, turning, or steady state. At one selected interior denoising step, initial and transition chunks retain full computation, while turning and steady chunks reuse the transformer residual from the most recent fully computed step in the same chunk. To exploit the persistence of low-frequency structure during steady interaction, we further introduce a frequency-mixed history prior guidance that incorporates complementary information from the preceding clean latent without an additional DiT forward pass. Evaluated on Matrix-Game 2.0 and LingBot-World v1/v2, CtrlCache achieves 1.21x to 1.41x DiT-backbone speedups without model retraining while improving WBench Overall scores over original inference across all three models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3824dd42-2263-4

---

### 13. Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation

- **ArXiv ID**: [2610.08772v1](https://arxiv.org/abs/2610.08772v1)
- **作者**: Liao Ma, Jiayi Song, Yunfeng Wu, Songhua Liu, Peilin Zhao
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08772v1](https://arxiv.org/pdf/2610.08772v1)
- **相关度评分**: 10/10

#### 英文摘要

Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible grid-like artifacts in the generated results. Fine-grained sliding-window attention effectively restores interactions across neighboring windows and improves visual quality. However, its irregular computation patterns create a substantial gap between theoretical and practical speedups and require specialized kernels tailored to each hardware backend. To tackle these challenges, we propose BASA, a backend-agnostic sparse attention, which brings the best of both worlds: visual quality and practical acceleration. Specifically, BASA replaces visual self-attention with shifted local-window attention. By introducing a structured window-shifting scheme across DiT blocks, we allow tokens divided by window boundaries in one layer to communicate in the following layers, thereby achieving global information exchange and eliminating window-induced visual artifacts. Notably, our design introduces no additional irregular operators or customized kernels, making it readily deployable on existing attention backends and closing the gap between theoretical sparsity and practical acceleration. Experiments demonstrate that BASA achieves measured speedups exceeding 90\% of the theoretical estimates on FLUX and delivers a 4.52$\times$ attention speedup on Wan while maintaining competitive generation quality.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6c87df6e-3804-4

---

### 14. Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap

- **ArXiv ID**: [2610.08770v1](https://arxiv.org/abs/2610.08770v1)
- **作者**: Mohammed Q. Alkhatib
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08770v1](https://arxiv.org/pdf/2610.08770v1)
- **相关度评分**: 10/10

#### 英文摘要

Patch-based learning improves hyperspectral image (HSI) classification by exploiting local spectral-spatial information, but random train-test sampling from the same image can cause spatial patch overlap, leading to data leakage and optimistic performance estimates. This paper investigates same-class train-test spatial overlap in patch-based HSI classification using two measures: overlap percentage (OP), which quantifies the global amount of overlapped testing patch pixels, and average overlap ratio (AOR), which measures the local severity among affected testing patches. Experiments on the Pavia University dataset compare random and non-random spatial sampling using SVM, MLP, 2D-CNN, 3D-CNN, ViT, and MorpMamba. The results show that deep patch-based models achieve high accuracy under random sampling, with 3D-CNN reaching 96.17% Overall Accuracy (OA), but drop substantially under non-random spatial sampling, where 3D-CNN decreases to 55.20% and ViT and 2D-CNN drop by 40.71 and 38.81 percentage points (PP), respectively. Patch-size analysis further shows that increasing the patch size from 5x5 to 19x19 raises the random-sampling overlap percentage from 23.28% to 77.02%. These findings demonstrate that random patch-based evaluation can substantially inflate classification performance, especially for models that strongly exploit spatial context. The code associated with this paper is available at: https://github.com/mqalkhatib/Data_Leakage_in_HSI_Classification.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8ad98e79-9c2a-4

---

### 15. Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error

- **ArXiv ID**: [2610.08756v1](https://arxiv.org/abs/2610.08756v1)
- **作者**: Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González
- **发布时间**: 2026-10-07
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.08756v1](https://arxiv.org/pdf/2610.08756v1)
- **相关度评分**: 10/10

#### 英文摘要

The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combines the information coming from all the views. Target and non-target evidence are accumulated simultaneously, weighted by the visibility of each Gaussian in each view. After that, the Gaussians are filtered with two thresholds: a main threshold $β$ selects the high-confidence seeds, and a lower one $γβ$ adds the connected components around them. For the evaluation, the labels are transferred from the Gaussians to the mesh vertices that are both visible and annotated. With this design, we can separate three sources of error: the 2D detector, the lifting and the transfer between representations. The thresholds and the transfer operator are chosen on seven Replica validation scenes, and the method is evaluated on ten held-out ScanNet++ scenes with the same values for every scene and class. The mean mIoU on the validation scenes was 0.93 with masks from the dataset annotations and 0.65 with YOLO masks, and on the ScanNet++ test scenes it was 0.80 and 0.54. Compared with thresholding the evidence per view, as a previous version of the method did, the fraction improves the test mIoU by 0.24 and makes it possible to use a single threshold for all the classes and scenes of both datasets. Finally, the error analysis shows that most of the remaining error comes from the detector.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d5371f9f-28b0-4

---
