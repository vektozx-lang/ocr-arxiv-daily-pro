# OCR arXiv Daily Pro — 2026-10-14

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-13 09:10 - 2026-10-14 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 933997c7-7378-4

---

## 📄 论文详情

### 1. AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface

- **ArXiv ID**: [2610.18724v1](https://arxiv.org/abs/2610.18724v1)
- **作者**: Emory Salaun, Syed Ayon, Kaleel Mahmood, Shaun Wallace
- **发布时间**: 2026-10-14
- **分类**: cs.CV, cs.HC, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.18724v1](https://arxiv.org/pdf/2610.18724v1)
- **相关度评分**: 10/10

#### 英文摘要

The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of AIRRI machine-resistant text designs. AIRRI employs two categories of machine-resistance techniques. First, AIRRI applies image transformations including character spacing, word spacing, line spacing, character opacity variation, stripe overlays, and image noise. Second, AIRRI applies decision-based adversarial attacks: RayS, SurFree, and ADBA. We evaluate AIRRI against three image-to-text systems: Tesseract, EasyOCR, and the transformer-based GOT-OCR2 model. Our results show that AIRRI substantially degrades automated text extraction performance. AIRRI increased character error rates for EasyOCR (6.9% to 55.9%), Tesseract (2.3% to 100.0%), and GOT-OCR2 (30.7% to 48.1%). Word error rates increased for EasyOCR (24.9% to 96.7%) and Tesseract (10.7% to 100.0%). Among the evaluated decision-based attacks, ADBA consistently produced the largest degradation in image-to-text performance, while RayS and SurFree produced more moderate reductions. EasyOCR and Tesseract were generally more susceptible to both image-based and adversarial perturbations than the transformer-based GOT-OCR2 model. Our findings suggest that AIRRI can significantly reduce the reliability of image-to-text-to-LLM workflows, increasing the effort required for AI-assisted assignment completion.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b53c6647-edd1-4

---

### 2. PLAYGROUND: Progressive Layout Generation with Render-Grounded Planning

- **ArXiv ID**: [2610.18865v1](https://arxiv.org/abs/2610.18865v1)
- **作者**: Jaeho Lee, Junhwan Heo, Junghyun Park, WonJun Moon, Eunju Yang...
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18865v1](https://arxiv.org/pdf/2610.18865v1)
- **相关度评分**: 10/10

#### 英文摘要

Generating editable graphic designs requires arranging visual and textual elements into a coherent composition while preserving their content and editability. Although recent MLLM-based approaches employ iterative generation and visual refinement to reflect the real-world design workflows, their high-level plans are predetermined prior to execution, limiting their adaptability as the design evolves. To address this limitation, we propose PlayGround, a progressive layout generation framework that dynamically adapts to the current rendered canvas. PlayGround establishes a progressive design loop comprising a Progressive Planner, a Layout Generator, and a Visual Verifier, guided by a Structure-Aware Retriever. Given an initial set of unordered elements, the Structure-Aware Retriever initially infers a coarse layout structure to retrieve structurally similar reference designs. Subsequently, at each turn, the Progressive Planner examines the current rendered canvas alongside the remaining elements, forms the next functional group, and plans its composition. The Layout Generator then predicts editable layout attributes, while the Visual Verifier evaluates rendered candidates and provides feedback when refinement is necessary. To train the Progressive Planner with step-wise supervision, we construct a two-stage data generation pipeline that extracts functional groups and turn-level planning trajectories from completed designs. Experiments on Crello and LICA demonstrate the effectiveness of PlayGround over existing methods. Our code and weights will be publicly released.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e7569469-1b79-4

---

### 3. LayerCanvas: Infographic Generation in AI Learning Assistants via Hybrid Layer-Set Diffusion

- **ArXiv ID**: [2610.18763v1](https://arxiv.org/abs/2610.18763v1)
- **作者**: Keshav Gupta, Jeremy Owen, Christopher Lloyd, Shaunak Mishra, Manav Sharma
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18763v1](https://arxiv.org/pdf/2610.18763v1)
- **相关度评分**: 10/10

#### 英文摘要

Online learning platforms are increasingly deploying AI assistants to provide personalized, on-demand tutoring. These can leverage infographics to communicate complex information and improve the learning experience. However, automating effective infographic generation remains a challenging task, requiring a combination of visual richness with precise typography, structured layouts, and continued editability. Existing representation methods satisfy these goals only in part: Scalable Vector Graphics (SVG) representations preserve geometry, hierarchy, and text but provide limited aesthetic flexibility, while raster diffusion models produce richer appearances by flattening content and layout into a single image. Conditioning a diffusion model on a rasterized SVG does not resolve this conflict because the raster preserves approximate placement but discards element ownership, occlusion relationships, and the structure needed to modify and recompose the result. We introduce LayerCanvas, a hybrid approach that retains SVG as the semantic, structural, and typographic program while using diffusion to aestheticize non-text content. Rather than generating one flattened raster, LayerCanvas partitions SVG elements into z-ordered sets of mutually non-overlapping elements and processes them through communicating parallel RGB generation streams. The resulting layers are independently editable and deterministically recomposed, while text is rendered from preserved vector metadata. Our approach combines rich visual synthesis with accurate typography and localized editing. LayerCanvas substantially improves text fidelity over state-of-the-art raster image generators while achieving the highest overall aesthetic quality. We further demonstrate non-destructive content editing, localization, asset reuse, and animation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0b4fa910-ad92-4

---

### 4. DTScribe: Generating Models for Digital Twin Reporting using Local Large Language Models

- **ArXiv ID**: [2610.18635v1](https://arxiv.org/abs/2610.18635v1)
- **作者**: Kérian Fiter, Angelica Portocarrero, Bentley Oakes
- **发布时间**: 2026-10-14
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.18635v1](https://arxiv.org/pdf/2610.18635v1)
- **相关度评分**: 10/10

#### 英文摘要

The development of a digital twin brings together many stakeholders and technical components. We have previously investigated the reporting of the conceptual architecture for these digital twins as an artifact for discussion. However, we find that the activity of modeling the digital twin for visualization and consensus-building can be quite tedious and time-consuming. In this article, we explore the automation of model generation using large language models, targeting the model required for digital twin reporting. Our approach is designed to ingest digital twin documents and output both the conceptual architecture visualization and a reporting page for that digital twin. We first extract from the input the key details aligning with our twenty-one-characteristic Digital Twin Description Framework described in previous work. Then, we generate a description model in the Ontological Modeling Language, representing the digital twin as a constellation of models, data, enablers, and services. We utilize refinement loops with large language models acting as judges and ontological reasoning to increase artifact quality as measured by our metrics. We investigate how architectural and parameter choices affect artifact quality, such as how refinement loops enable local large language models to produce sufficiently high-quality results comparable to larger models. We also detail insights and lessons learned useful for practitioners, such that they can integrate our techniques to accelerate their digital twin reporting or for other model generation tasks. These insights include the use of medium-sized local models (around 20 billion parameters), the avoidance of large language models as judges and clustering for characteristic extraction, and the recommendation of at least two reasoner loops for Ontological Modeling Language refinement.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8817bd9a-5e1b-4

---

### 5. Structural Segmentation for Brazilian Legal Document Retrieval

- **ArXiv ID**: [2610.18622v1](https://arxiv.org/abs/2610.18622v1)
- **作者**: Leandro Carísio Fernandes, João Alberto de Oliveira Lima, Hudson de Martim, Eduardo Seiti de Oliveira, Roberto Lotufo...
- **发布时间**: 2026-10-14
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.18622v1](https://arxiv.org/pdf/2610.18622v1)
- **相关度评分**: 10/10

#### 英文摘要

Long legal documents are often represented as single retrieval units, which can dilute relevant content and limit retrieval effectiveness. This study investigates structural segmentation as a document representation strategy to improve Brazilian legal document retrieval. Using the hierarchical structure of legal acts, we represent each document as a collection of chunks. We evaluate four representation strategies: a multi-layered hierarchy representation and three simplified versions based on core chunks (articles and non-normative document components), with varying contextual details. We test these strategies on two publicly available Brazilian legal datasets containing normative acts and legislative proposals, using both lexical and dense retrieval models. Results show that structural segmentation improves dense retrieval compared with whole-document indexing, despite substantially increasing the number of indexed units. However, it does not consistently benefit lexical retrieval. Finally, we find that full hierarchicy representation is not necessary: core chunks enriched with document metadata yield comparable or better results.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 40c42f02-0987-4

---

### 6. Code-Switching Detection via Language-Selective Dimensions in Speech Foundation Models

- **ArXiv ID**: [2610.18726v1](https://arxiv.org/abs/2610.18726v1)
- **作者**: Jie Chi, Zakaria Aldeneh, Masha Fedzechkina, Maureen de Seyssel, Natalie Schluter
- **发布时间**: 2026-10-14
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.18726v1](https://arxiv.org/pdf/2610.18726v1)
- **相关度评分**: 10/10

#### 英文摘要

Code-switching (CS), the alternation between languages within an utterance, is common in multilingual speech but underrepresented in pretraining corpora. Increasing CS coverage requires finding relevant utterances in large speech collections so that they can be included in training data. One way to find such utterances is to transcribe the speech and detect language alternation in the text, but this depends on obtaining accurate multilingual transcriptions. We propose a lightweight method that detects CS directly from speech. It uses frame-level language information in pretrained speech encoders to determine whether both languages are present within an utterance. Specifically, we identify language-selective hidden-state dimensions using monolingual recordings and aggregate their frame-level activations into a CS prediction. With a small CS set used to tune a decision rule, we show that the Whisper-small encoder achieves a mean F1 of $0.798$ across 14 language pairs in CS-FLEURS, compared with $0.776$ for a CNN and $0.751$ for a HuBERT linear baseline trained for monolingual language identification. Our findings suggest that pretrained speech encoders already encode the information needed to identify CS utterances, and they provide a lightweight tool for building more representative multilingual corpora.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8f8fc5d9-91fc-4

---

### 7. ChunkAct: Action Chunking for Agentic Robotics

- **ArXiv ID**: [2610.18874v1](https://arxiv.org/abs/2610.18874v1)
- **作者**: Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang...
- **发布时间**: 2026-10-14
- **分类**: cs.RO, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.18874v1](https://arxiv.org/pdf/2610.18874v1)
- **相关度评分**: 10/10

#### 英文摘要

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c3bd2171-b794-4

---

### 8. LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts

- **ArXiv ID**: [2610.18873v1](https://arxiv.org/abs/2610.18873v1)
- **作者**: Wenxuan Guo, Yingping Liang, Zhaoguo Wang, Ziyuan Li, Angyuan Ma...
- **发布时间**: 2026-10-14
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18873v1](https://arxiv.org/pdf/2610.18873v1)
- **相关度评分**: 10/10

#### 英文摘要

Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment. Real-world rollouts contain successes, suboptimal behavior, and failures: imitating every recorded action can reinforce poor behavior, while filtering out failures discards evidence of physical interactions and their consequences. We introduce \textbf{LoopWAM}, a closed-loop world-action model that learns directly from this full quality spectrum, using rollouts from both itself and other deployed policies. Source-dependent noise sampling unifies behavior learning and action-conditioned world modeling, while quality steering and quality-weighted supervision retain full video supervision across qualities and regulate action imitation. Video and action tokens interact throughout parallel denoising, allowing learned consequences to inform action generation directly. On RoboChallenge Table30-V2, three deployment-and-training rounds raise success from 23.67\% to 43.33\%, a 19.7-percentage-point gain, with a final score of 56.80. LoopWAM also achieves 94.5\% average success on RoboTwin~2.0 and 49.5\% overall success on RoboCasa365 without additional embodied pretraining, obtaining the best overall results among the compared methods across all three benchmarks. On challenging shirt folding task, two rounds of deployment-driven improvement after single-task post-training raise success from 13.20\% to 55.56\%. These results demonstrate closed-loop improvement from mixed-quality experience under both multi-task learning and single-task post-training. \href{https://loop-wam.github.io/}{\textcolor{orange}{Project Page}}

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7f2ab5bf-f53c-4

---

### 9. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- **ArXiv ID**: [2610.18872v1](https://arxiv.org/abs/2610.18872v1)
- **作者**: Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi...
- **发布时间**: 2026-10-14
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18872v1](https://arxiv.org/pdf/2610.18872v1)
- **相关度评分**: 10/10

#### 英文摘要

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of human loco-manipulation built with a wearable system. With an emphasis on professional activities, its continuous recordings align egocentric video with reconstructed whole-body motion, fine-grained finger articulation, and tactile observations, accompanied by step-level descriptions. To achieve this coverage with sparse body sensing, we develop the Calibrate-Complete-Constrain pipeline. Concretely, reusable calibration fixes participant geometry and sensor attachments before motion inference to disentangle mounting offsets from articulation. A temporal prior then completes unobserved joint motion, while layered constraints promote measurement agreement, temporal continuity, and geometric consistency, properties that motion plausibility alone does not guarantee. Against tracker-fitted references, the method reduces body-point error by 71.9% relative to the strongest baseline; matched evaluations also show gains in hand stability and contact estimation. Preliminary studies explore multimodal generation and conditioning alongside humanoid retargeting with whole-body control in simulation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 45855ccb-71c8-4

---

### 10. Dog-Breed Text-to-image Flow Matching from Pretraining to Fine-Tuning on 4 Consumer GPUs

- **ArXiv ID**: [2610.18870v1](https://arxiv.org/abs/2610.18870v1)
- **作者**: Reyhaneh Esmailizadeh, Xingjian Leng, Zhanhao Liang, Liang Zheng
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18870v1](https://arxiv.org/pdf/2610.18870v1)
- **相关度评分**: 10/10

#### 英文摘要

We generally perceive that training text-to-image diffusion models requires heavy compute: it is true if we aim at a comprehensive frontier model. This understanding prevents people from training their own models when getting started in the field. We develop MiniDog, a framework that enables pretraining diffusion transformers in 55 minutes and fine-tuning in another 15 minutes on four 3090 GPUs. For data, we use 26k dog images from ImageNet and caption them for pretraining and use 2k images generated by FLUX.1-schnell for fine-tuning. We precompute the image and text features and cache them for efficiency. For architecture, we use E2E-INVAE for its semantic latent space, a small transformer with 22M parameters, a small Qwen model for text encoding, and in-context conditioning. For training, we use iREPA and an EUPE perception encoder for acceleration. For evaluation, our repository supports FID, HPSv2 score, PickScore, and various VAE reconstruction metrics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a76f2db7-8d99-4

---

### 11. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion

- **ArXiv ID**: [2610.18871v1](https://arxiv.org/abs/2610.18871v1)
- **作者**: Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu
- **发布时间**: 2026-10-14
- **分类**: cs.CV, cs.GR, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.18871v1](https://arxiv.org/pdf/2610.18871v1)
- **相关度评分**: 10/10

#### 英文摘要

Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale depends on unknown target motion, it cannot be measured directly at test time. We decouple residual structure from physical scale by learning a dimensionless prior, estimating amplitude from observables and a lightweight correction fitted only on training sources. Our unified model surpasses harmonic extension across all evaluated families, including unseen cloth and legged bodies, without skeletons, registration, or cross-mesh correspondence. The same prior applies without retraining to point-tracked animal video and a robot grasping a soft body. Project page: https://su-terry.github.io/cepheid-website/

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e7090ac9-4cf4-4

---

### 12. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

- **ArXiv ID**: [2610.18868v1](https://arxiv.org/abs/2610.18868v1)
- **作者**: Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, Nanyun Peng, Kai-Wei Chang...
- **发布时间**: 2026-10-14
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18868v1](https://arxiv.org/pdf/2610.18868v1)
- **相关度评分**: 10/10

#### 英文摘要

Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to curate and verify, and their rewards are sparse. We address both. First, we introduce Tev-Gym, the first long-horizon agent training dataset with verifiable, dense, progressive rewards -- 1,170 verified task environments across 7 domains. It is built on a latent-world-first approach that first constructs a latent world: a complete and correct hidden specification of the task domain, workflow, and expected state after each step. Each task is then progressively rendered from this specification into an agent-facing environment, enabling controllable complexity and a natural progress metric. Second, we turn this metric into a training recipe: via progress-potential reward shaping (PPRS), we convert progress into a dense per-step reward that improves training efficiency and makes otherwise-intractable tasks trainable. Training with this recipe yields Tev-27B, which achieves substantial gains on the Agents' Last Exam computing and math sciences domains (ALE-CM), matching GPT-6 Astra and Claude Opus 5 at Pass@5. Despite training only on ALE-related data, it generalizes to the Terminal-Bench (TB) 3.0 and 4.0 subsets, surpassing GLM 5.2 and Gemini 3.7 Flash, and reaches Claude Opus 4.8-level performance on middle-horizon tasks such as TB 2.1.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6c2db8fd-7abe-4

---

### 13. Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs

- **ArXiv ID**: [2610.18858v1](https://arxiv.org/abs/2610.18858v1)
- **作者**: Aimon Rahman, Joymallya Chakraborty, Vidit Bansal, Abhishek Dan
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18858v1](https://arxiv.org/pdf/2610.18858v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models have advanced rapidly, but most remain optimized for single-image inputs. Multi-image reasoning is costly because each image adds many visual tokens, increasing encoding and attention demands. Existing techniques that address the above issue, including visual token pruning, token merging, visual token compression, learned resampling, hierarchical compression, retrieval-augmented visual reasoning, and memory-based architectures, have largely been designed for single-image scenarios, where redundancy is primarily spatial and local. Multi-image reasoning introduces additional challenges: redundancy may occur across images, task-relevant evidence may be sparse or distributed, and aggressive per-image compression can remove details needed for comparison, counting, temporal reasoning, retrieval, or evidence grounding. Moreover, existing token-reduction methods are often either (i) training-free but inference-inefficient, typically relying on accessing attention matrices to get token-importance that may be impractical to access with memory-efficient attention implementations such as FlashAttention, or (ii) training-dependent, requiring the base MLLM to be retrained or adapted to a new compressed-token paradigm. In this work, we study scalable multi-image reasoning and understanding without retraining the base model and without accessing attention matrices at inference time. To this end, we propose mmVB, a lightweight plug-and-play module that assigns query-conditioned per-image token budgets via cross-image context, adding only 1.6M trainable parameters while reducing visual input tokens by 9x. This reduction yields 5x faster time-to-first-token and 7x fewer prefill FLOPs, while maintaining 94.4% of full-resolution accuracy across eight multi-image reasoning benchmarks.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: dbe8fc55-8a85-4

---

### 14. PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts

- **ArXiv ID**: [2610.18857v1](https://arxiv.org/abs/2610.18857v1)
- **作者**: Ruixiao Dong, Jianmin Bao, Bozhi Luan, Zijie Meng, Xin Tao...
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18857v1](https://arxiv.org/pdf/2610.18857v1)
- **相关度评分**: 10/10

#### 英文摘要

Pixel-space diffusion models provide an appealing alternative to latent-space diffusion models by directly modeling raw images without relying on a learned tokenizer. However, scaling pixel-space models has predominantly followed dense strategies, tightly coupling model capacity with active computation. In this work, we show that standard LLM-style Mixture-of-Experts (MoE) architectures can be effectively transferred to pixel-space diffusion. Building on this finding, we introduce PixelMoE, a pixel-space generative framework that sparsely scales model capacity with standard LLM-style MoE, without diffusion-specific routing mechanisms or auxiliary routing objectives. Specifically, PixelMoE combines standard Token-Choice (TC) routing with fine-grained routed experts for input-adaptive sparse computation, a shared expert for capturing common representations, and a bias-based load-balancing strategy. To complement sparse capacity scaling, PixelMoE further introduces Pixel-Space Hierarchical Flow Matching, which varies spatial resolution along the denoising trajectory from global structure formation to fine-grained detail refinement. At comparable active parameter counts, PixelMoE consistently outperforms its dense counterparts across model scales, demonstrating effective sparse capacity scaling in pixel space. On class-conditional ImageNet-1K, PixelMoE achieves FID scores of 1.47 at 256x256 and 1.53 at 512x512 without representation alignment or perceptual losses, comparing favorably with leading pixel-space and latent-space generative models. Code and models will be released soon.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d5dee1e1-7a5b-4

---

### 15. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

- **ArXiv ID**: [2610.18846v1](https://arxiv.org/abs/2610.18846v1)
- **作者**: Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.18846v1](https://arxiv.org/pdf/2610.18846v1)
- **相关度评分**: 10/10

#### 英文摘要

Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud and camera poses estimated from the input images by a reconstruction model as a global scaffold for whole-scene generation and partitions it into overlapping spatial blocks. To robustly leverage these imperfect geometric priors, we equip the native 3D generative model TRELLIS.2 with a dedicated reconstruction-based conditioning architecture that generates each block from its local point-cloud crop and block-relevant image observations, producing sparse structure, detailed geometry, and PBR materials. To maintain scene-level coherence, we introduce neighbour-aware latent inpainting and a causal world-generation procedure that propagates structural, geometric, and material context across overlapping blocks. Together, these designs scale multi-view generative reconstruction to large-scale scenes, yielding coherent, unified meshes. Extensive experiments demonstrate that WorldRecon achieves state-of-the-art reconstruction performance, reducing Chamfer distance by 14.9% and 43.1% while improving F-score by 17.3% and 12.0% over the strongest baselines on synthetic and real-world indoor scenes, respectively, thereby demonstrating faithful and complete generative reconstruction as well as strong sim-to-real generalization. Project page: https://kszpxxzmc.github.io/WorldRecon-website/.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 81c38a7d-7f33-4

---
