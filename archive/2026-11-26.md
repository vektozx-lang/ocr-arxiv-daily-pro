# OCR arXiv Daily Pro — 2026-11-26

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-25 09:10 - 2026-11-26 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 32f68f2d-e1

---

## 📄 论文详情

### 1. DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding

- **ArXiv ID**: [2611.34420v1](https://arxiv.org/abs/2611.34420v1)
- **作者**: Hoang-Nhat Nguyen, Chen Change Loy
- **发布时间**: 2026-11-25
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.34420v1](https://arxiv.org/pdf/2611.34420v1)
- **相关度评分**: 10/10

#### 英文摘要

Multi-page document vision-language models encode each page independently, creating a feature-level discontinuity at page boundaries: visual tokens are formed without access to content on adjacent pages, and the language model must reason over these page representations formed in isolation. We introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module inserted between a pretrained vision encoder and the language model that injects the inductive bias of local cross-page context into visual representations. For each page, DocSEAM forms a local triplet with its two neighbors, applies center-anchored masked self-attention with directional salience gates to fuse information from neighbor pages, and returns only the enriched center-page tokens, leaving the visual token count unchanged. After a supervised cross-page warm-up and multi-page fine-tuning with DocSEAM frozen, our 9B-parameter model achieves state-of-the-art results among the evaluated open-weight models of up to 10B parameters on five multi-page document VQA benchmarks. We further show that under controlled re-pagination, DocSEAM reduces sensitivity to boundary placement and improves cross-page span localization

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8ac6c621-c6

---

### 2. Knowledge-Base Gradient Descent: Self-Structuring Learning through Question Answering

- **ArXiv ID**: [2611.34841v1](https://arxiv.org/abs/2611.34841v1)
- **作者**: Masahiro Kato
- **发布时间**: 2026-11-26
- **分类**: cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.34841v1](https://arxiv.org/pdf/2611.34841v1)
- **相关度评分**: 10/10

#### 英文摘要

We consider the problem of constructing knowledge bases for applications based on large language models, in which the structure of a knowledge base determines how an application can retrieve and connect the information needed to answer a question. We study Self-Structuring Learning, a setting in which questions and expected answers guide the construction of a persistent knowledge base whose editable structure can be a graph schema or the organization of linked knowledge documents. We propose Knowledge-Base Gradient Descent, which diagnoses discrepancies between expected answers and responses obtained through the current knowledge base. At each round, the method proposes a structural edit, rebuilds the knowledge base, and adopts the edit when the learning loss decreases. The retained structure is evaluated on other questions about the same sources. By randomizing over candidate edits, we express the loss change of an edit as a derivative with respect to the probability of selecting it, and we evaluate joint edits as single candidates because their changes interact. Schema Descent instantiates the method for graph schemas. In experiments on large documents, each a bundle of research papers, the updated knowledge cards and graph schemas obtain higher mean Answer F1 on held-out generated questions than their initial structures, with schema gains in every document. On human questions, mean F1 rises for schemas and falls for cards: the updated structures serve the kind of question they were learned from.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a9d29604-75

---

### 3. DocDUR-Net: Degradation-Aware Unified Document Image Restoration

- **ArXiv ID**: [2611.34860v1](https://arxiv.org/abs/2611.34860v1)
- **作者**: Haowei Xu, Peirong Zhang, Xuhan Zheng, Lianwen Jin
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34860v1](https://arxiv.org/pdf/2611.34860v1)
- **相关度评分**: 10/10

#### 英文摘要

Captured document images often suffer from diverse degradations caused by uncontrolled imaging conditions, which reduce readability and obscure fine text structures. Single-degradation restoration methods are usually trained and deployed for individual degradation types, and therefore require model selection before restoration. Unified restoration models alleviate the need to maintain multiple restoration networks by sharing one network across tasks, but representative unified document image restoration methods still depend on external task selection. This dependency limits automatic document image restoration. We propose DocDUR-Net, a degradation-aware unified restoration network that derives restoration guidance directly from the input image. It introduces a Degradation Perception Module (DPM) to extract degradation representations and predict degradation weights, and Degradation Prior-guided Adaptive Feature Fusion (DP-AFF) to combine learnable degradation priors with degradation features extracted from the input. The resulting guidance is injected into a shared restoration backbone, enabling adaptive restoration without external task selection. DocDUR-Net also supports a manual mode with explicit task selection. Experiments on document image restoration benchmarks show that DocDUR-Net achieves the best average PSNR of 29.405 dB and SSIM of 0.960 among unified methods while remaining competitive with single-degradation methods.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4f8eb950-d0

---

### 4. SpiderSkel: Sub-Pixel Multi-Tangent 2D Skeletonization from Inscribed-Disc Geometry

- **ArXiv ID**: [2611.33805v1](https://arxiv.org/abs/2611.33805v1)
- **作者**: Zhexian Zhou, Lian Ren, Xiao Feng, Sebastian Scherer
- **发布时间**: 2026-11-25
- **分类**: eess.IV, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.33805v1](https://arxiv.org/pdf/2611.33805v1)
- **相关度评分**: 10/10

#### 英文摘要

Skeletonization reduces a binary shape to a compact medial representation, but pixel-grid discretization perturbs the boundary-contact geometry underlying the medial axis, creating tension among connectivity, reconstruction fidelity, and skeleton compactness. SpiderSkel is a family of training-free two-dimensional skeletonization methods built on multi-tangent inscribed-disc geometry. A tie-aware exact Euclidean distance transform retains tied nearest boundary sites rather than collapsing them to a single label; medial candidates are localised to sub-pixel positions from the inscribed disc's tangent contacts, filtered by the angular span of those contacts, and completed by connectivity-aware refinement. Across nineteen public benchmarks comprising 11,323 images of shapes, retinal vessels, cracks and roads, and document images, a single operating point fixed across datasets yields skeletons that, on every image, have exact skeleton topology under the component/hole certificate, remain fully connected, and have exact per-object reconstruction topology. The three SpiderSkel variants are the only evaluated methods to satisfy all three properties across every category; within each category, every variant is Pareto-optimal with respect to all twenty-two baselines in strict sub-pixel reconstruction Dice versus reduction rate. Incremental engines for all three variants reproduce the skeleton of a complete recomputation exactly across 23,040 verified edit steps, with median update latencies of 15.4-18.1 ms per foreground edit and 4.3-4.4 ms per canvas edit, and speedups reaching 33.0-fold on canvas edits.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: efd370c8-85

---

### 5. AnyCam: Anything Can Represent Camera for Video Generation

- **ArXiv ID**: [2611.34944v1](https://arxiv.org/abs/2611.34944v1)
- **作者**: Weijie Lyu, Zhixin Shu, Yuntian Ke, Ming-Hsuan Yang
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34944v1](https://arxiv.org/pdf/2611.34944v1)
- **相关度评分**: 10/10

#### 英文摘要

Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene, remains difficult. Existing methods condition either on camera parameters, which are scale-ambiguous in monocular video, or on explicit geometry such as warped point clouds or depth, which breaks down under large viewpoint changes. We present AnyCam, a method that represents the camera with an anchor object in the scene: we reconstruct it in 3D and render it along the target trajectory, a camera signal that is scale-aware, view-complete and easy to specify relative to the object. A video diffusion model transfers the content and dynamics of the source video to the new viewpoint. Its H-Concat layout aligns source and target frames in time, so the model can be distilled into AnyCam-AR, a streaming few-step generator for on-the-fly camera control. Both models are trained on paired videos with pixel-aligned anchor renderings from multi-camera videos and static-scene captures. Experiments on diverse datasets and trajectories show that AnyCam performs favorably against camera-controlled video generation and 3D reconstruction methods in camera control and visual quality.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f5db0649-22

---

### 6. Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs

- **ArXiv ID**: [2611.34914v1](https://arxiv.org/abs/2611.34914v1)
- **作者**: Agelos Kratimenos, Kostas Daniilidis, Evangelos Chatzipantazis
- **发布时间**: 2026-11-26
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34914v1](https://arxiv.org/pdf/2611.34914v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wrong place or into collisions. Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has. We introduce Cairn, which keeps the VLA frozen and steers it at test time along learned 3D trajectories of the object in its gripper. A small prior reads point clouds of the scene and the held object, along with its pose when grasped and the instruction, and samples SE(3) trajectories up to its release that lead it around obstacles and turn it to fit through gaps. The prior and the VLA form the two levels of a hierarchical planner in which feedback runs both ways: the VLA's intended motion chooses and reshapes the trajectories, and the chosen one guides the VLA's denoising. Its predicted actions, mapped to the held object's poses through the grasp, are pulled toward the next waypoint, while the VLA's weights stay untouched. Across 1,941 held-out LIBERO scenes with displaced objects and obstacles, Cairn raises the success rate of a frozen π0.5 from 24.5% to 95.1%, above that of a π0.5 fine-tuned on our training layouts, without hurting standard LIBERO. On the third-party LIBERO-PRO benchmark, it raises success from 27.3% to 38.0%, and from 54.4% to 81.1% on the episodes it steers. On a real Franka, with a prior trained purely in simulation, it guides the frozen DROID π0.5 around an obstacle and to a placement at the limit of the arm's reach, where it otherwise fails. All code, models and data will be made public.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 13080785-85

---

### 7. Stranger Things: When Objects Appear Without Their Typical Neighbors

- **ArXiv ID**: [2611.34881v1](https://arxiv.org/abs/2611.34881v1)
- **作者**: Siddhartha Gairola, Jiahao Xie, Anna Kukleva, Francesco Locatello, Bernt Schiele
- **发布时间**: 2026-11-26
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.34881v1](https://arxiv.org/pdf/2611.34881v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic across the modern vision stack remains absent. We provide such a diagnostic framework. We measure typicality bias via normalized pointwise mutual information (NPMI) over object pairs, and introduce STRANGE-Bench (Synthetic Typicality-RANked Grounded Evaluation Benchmark): a photorealistic, layout-controlled benchmark spanning 17 sub-tiers from typical to never-co-occurring object pairs. Across five model families (specialist detectors, open-vocabulary detectors, self-supervised, vision-language, and multimodal large language models) and three recognition tasks (supervised detection, open-vocabulary detection, and classification), the bias is prevalent: gaps of 5-11 p.p. persist when objects appear outside their typical company, and do not consistently shrink with scale. To mitigate it, we turn to data augmentation: existing augmentations are designed for visual diversity, not for breaking co-occurrence shortcuts, and sample from the very distribution that produces typicality bias. We propose Anchor-Atypicality Sampling (AAS), a simple sampling rule for paste-based augmentations that uses the NPMI signal to tilt the training-time co-occurrence distribution toward atypical partners. AAS reduces the typicality gap by up to 1.6 p.p. on natural-image COCO splits and 23.0 p.p. on synthetic STRANGE-Bench across three model families, without sacrificing overall performance.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f7949b65-3d

---

### 8. How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches

- **ArXiv ID**: [2611.34875v1](https://arxiv.org/abs/2611.34875v1)
- **作者**: Aakash Goel, Benjamin Steenhoek, Yu Hu
- **发布时间**: 2026-11-26
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.34875v1](https://arxiv.org/pdf/2611.34875v1)
- **相关度评分**: 10/10

#### 英文摘要

Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every block (unit) of the final patch to the step that wrote it, reverts each unit, and reruns the task tests to decide whether the unit is needed. We apply DRA to 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models on SWE-bench Verified (6,728) and DeepSWE (932), and grade developer patches using the same method. Agent patches do change more lines than developers'; on SWE-bench Verified the majority of extra edits add tests (61%) and documentation (13%) while on DeepSWE, most extra edits are code (58%). On both benchmarks, agents' code is on average at least as necessary as developers' (mean $NP_{code}$ 0.887 vs. 0.864 on SWE-bench Verified, where 11 of 18 models leave less unneeded code than developers, and 0.797 vs. 0.785 on DeepSWE). On average, 11% of an agent patch's code units on SWE-bench Verified are still unneeded, and 89% of those change behavior. Debug steps write almost none of the unneeded code. Code necessity differs substantially by model; it is unrelated to resolve rate on SWE-bench Verified and negatively correlated with it on DeepSWE (Spearman -0.59, p = 0.01). On SWE-bench Verified, pruning with DRA using only the tests the agent can see (its own tests and the repository's) removes the majority of unneeded code but also some needed code (67% recall, 46% precision), and 89% of pruned patches still resolve the task; asking the agent to audit its own diff is more precise but less effective (36% recall, 66% precision). We recommend that benchmarks report code necessity next to resolve rate and that over-editing be addressed through model training and harness-level pruning.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 822ff4a9-1b

---

### 9. Probing Visual Idiosyncrasies in Text-to-Image Models

- **ArXiv ID**: [2611.34843v1](https://arxiv.org/abs/2611.34843v1)
- **作者**: Yongqian Peng, Hongjie Li, Yichao Zhou, Chi Zhang, Yixin Zhu
- **发布时间**: 2026-11-26
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.34843v1](https://arxiv.org/pdf/2611.34843v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-to-Image (T2I) models turn short text descriptions into images, and the leading models now produce images of comparable visual quality. Whether their outputs still carry model-specific characteristics matters for attribution, for model comparison beyond aggregate quality, and for evaluations that assume anonymity. We ask whether images from frontier T2I models can still be classified by source, and which visual properties make this possible. Here we show that a standard ResNet-50 identifies the source of an image among HiDream-O1-Dev, FLUX.2-dev, HunyuanImage-3.0, and Qwen-Image-2512, the four highest-ranked open-source models on the Text-to-Image Arena, with 100.00% accuracy on held-out prompts. Human participants reach only 62.61% on the pairwise version of this task, so the distinguishing cues are not visually obvious. They are also not tied to a particular classifier and survive severe image corruptions and out-of-distribution prompts. We trace them to visual idiosyncrasies at three levels. Low-level texture statistics alone let a lightweight multi-layer perceptron match ResNet-50. Object layout, depth, and albedo estimated from the images each carry a source signal. Image captions reveal model-specific preferences in style and background that the prompts never specify. A one-sentence hint about these cues raises human accuracy by 9.03 percentage points. These idiosyncrasies make source classification a tool for measuring similarity between models and between real and generated images, and they caution against assuming anonymity in human preference evaluation of T2I models.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 03c72278-b4

---

### 10. The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?

- **ArXiv ID**: [2611.34823v1](https://arxiv.org/abs/2611.34823v1)
- **作者**: Maxime Lelièvre, Alasdair Mackintosh, Dominic Andrews, Tobias Murray, Moritz Boos...
- **发布时间**: 2026-11-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.34823v1](https://arxiv.org/pdf/2611.34823v1)
- **相关度评分**: 10/10

#### 英文摘要

Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely automated pipeline that turns curriculum documents, teacher guides and pupil books into a vetted question set organised on a fixed grid of nine linguistic domains and seven grade levels. The pipeline combines LLM-driven source survey, feature consolidation, item generation and quality control with an item-selection step inspired by item response theory and a final expert review. We instantiate it for Kiswahili (Kenya; 135 items) and English (United Kingdom; 137 items) and evaluate 121 and 119 models respectively. Frontier models exceed 90% accuracy in both languages, but accuracy falls steeply for smaller and cheaper models, and more so in Kiswahili. The two best models under 10 billion parameters reach 91.7% and 73.0% in English but only 51.9% and 40.7% in Kiswahili, and the mean accuracy of models deployable on mobile and tablet hardware is 47% in English against 24% in Kiswahili. The models most practical for low-resource classrooms are therefore the least capable in the languages they would serve. We release a 20-item sample per language, all pipeline prompts, open-source code, and a public leaderboard. This is the first rung of a three-level evaluation ladder for measuring and generating decodable text to support foundational literacy.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 00ea5305-ce

---

### 11. SceneDesigner3D: Agentic Evolutionary Search for Principled Rearrangement of 3D Indoor Scenes

- **ArXiv ID**: [2611.34783v1](https://arxiv.org/abs/2611.34783v1)
- **作者**: Chandan Yeshwanth, Angela Dai
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34783v1](https://arxiv.org/pdf/2611.34783v1)
- **相关度评分**: 10/10

#### 英文摘要

Scene rearrangement is an essential task for 3D content creation applications, requiring generation of diverse, aesthetic and functional scene rearrangements. We present SceneDesigner3D, an agentic evolutionary search method for 3D indoor scene rearrangement that systematically explores the design space of 3D scenes and generates multiple solutions according to common interior design principles. Given an input scene and a text prompt, SceneDesigner3D represents the rearrangement as an editable program and evolves a population of candidate layouts. Starting from distinct design ideas, a VLM agent mutates the programs by refining promising candidates, exploring new rearrangement strategies or redesigning from scratch, while verifying the layouts for physical validity. Proposals are scored by a VLM judge for adherence to the input prompt and satisfaction of design principles such as balance, zoning and emphasis, as well as numerically computed principles such as circulation and clutter. An archive of top-performing, structurally varied candidates further increases diversity of rearrangements. Experiments on the SAGE-10k and SceneSmith datasets show that SceneDesigner3D improves prompt adherence and computed design principle scores over baselines by up to 5.1% and 15.2%, respectively. Code will be made publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7fe6a10d-4a

---

### 12. PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona Bank

- **ArXiv ID**: [2611.34785v1](https://arxiv.org/abs/2611.34785v1)
- **作者**: Bich Ngoc Doan, Hanna Yukhymenko, Imanol Schlag
- **发布时间**: 2026-11-26
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.34785v1](https://arxiv.org/pdf/2611.34785v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language models increasingly replace real people in the AI development pipeline, as they are used to generate training dialogues at scale and to drive alignment and evaluation. However, out-of-the-box models produce monolingual and stylistically flat texts as synthetic user prompts, failing to replicate the real user-AI communication mechanics. We present PersonaFactory, an end-to-end pipeline that generates detailed user personas and uses them to augment existing user prompts from their point of view, producing a bank of over 740000 structured synthetic personas detailing their background and communication behaviors, and a corpus of roughly 1.24 million persona-styled synthetic conversations spanning 85 languages. We evaluate the effect of personal features on style adoption and intent preservation, using an LLM-judge and heuristic metrics to assess augmentation fidelity together with the downstream impact on assistant persona control through training data. Results show that our structured, attribute-based style representation enables per-axis control and better intent preservation at comparable style fidelity than free-text persona descriptions used in existing methods. A human expert evaluation found the augmented conversations plausible, with favorable ratings for intent preservation, style naturalness, and multilingual authenticity. Finally, PersonaFactory conversations achieve comparable performance to original training data on capability benchmarks, are preferred on real user prompts at equal reply length, and adapt their reply style more closely to users without explicit steering.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 40409dd8-0e

---

### 13. Tracking Any Point with Agentic Visual Reasoning

- **ArXiv ID**: [2611.34943v1](https://arxiv.org/abs/2611.34943v1)
- **作者**: Xuweiyi Chen, Jin Yao, Linzhan Mou, Lei Gong, Di Liu...
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34943v1](https://arxiv.org/pdf/2611.34943v1)
- **相关度评分**: 10/10

#### 英文摘要

A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappears and later reappears. In this paper, we introduce AgenTAP, a VLM-based agent that directly predicts point coordinates and visibility and actively reasons over videos. Starting from its own estimate, the agent autonomously chooses what to inspect and uses the resulting evidence to verify point identity and refine its predictions. With GPT-6 Astra, it surpasses expert vision models in both point localization and visibility prediction, without correspondence-specific fine-tuning. We further use AgenTAP to re-identify physical points after disappearance and reconnect fragmented tracks, constructing EgoTAP-4D, a dataset of 3D point trajectories in long real-world egocentric videos. On sampled reappearing points, its predictions approach human agreement, and adding EgoTAP-4D to D4RT training improves average 3D tracking performance.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 51e8c686-33

---

### 14. Improving and Expanding Video Editing Capabilities Without Videos

- **ArXiv ID**: [2611.34941v1](https://arxiv.org/abs/2611.34941v1)
- **作者**: Ji Xie, Yanhao Jia, Xiangpeng Yang, Martin Q. Ma, Sihan Xu...
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34941v1](https://arxiv.org/pdf/2611.34941v1)
- **相关度评分**: 10/10

#### 英文摘要

Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks using an image editor. It enables efficient post-training with no architectural changes and no new videos, using only individual images. Our key idea is to let the video editor role-play as an image editor: it edits an image as a one-frame video, with the image editor guiding the video editor's predictions at each denoising step. Although the video editor sees only single images during training, at test time it applies the improved and expanded capabilities to whole video clips while preserving temporal consistency. To push the boundaries of video editing, we introduce OpenVE++, an extension of OpenVE-Bench that adds four new editing tasks useful for video production, including action changes, expression changes, body movements, and scene relighting. Our experiments across three different video editors show that I2VT improves existing editing capabilities and expands them to new tasks, and our models achieve state-of-the-art (SOTA) performance on both OpenVE-Bench and OpenVE++.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b936f96e-11

---

### 15. LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies

- **ArXiv ID**: [2611.34940v1](https://arxiv.org/abs/2611.34940v1)
- **作者**: Yipengjing Sun, Chenyang Wang, Boyao Zhou, Jiapeng Zhu, Ka Leong Cheng...
- **发布时间**: 2026-11-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.34940v1](https://arxiv.org/pdf/2611.34940v1)
- **相关度评分**: 10/10

#### 英文摘要

We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasterizing deformed Gaussians into view- and motion-consistent PBR buffers. Conditioned on these buffers, our neural shader formulates forward rendering as a conditional video diffusion process, bypassing explicit PBR computation to synthesize realistic shading effects under target illumination. We achieve real-time streaming through heterogeneous distillation from a pretrained multi-step bidirectional relighting teacher to a two-step causal autoregressive neural shader, inheriting broad synthetic lighting priors while minimizing conditioning and decoding latency. To further specialize these priors to human heads, we construct a hybrid relighting dataset for domain-specific fine-tuning, capturing authentic facial dynamics and physically grounded light transport. Extensive experiments show that our framework enables 3D-controllable, real-time portrait animation and relighting, outperforming state-of-the-art methods in visual fidelity, motion control, and lighting accuracy.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6e7491b2-c4

---
