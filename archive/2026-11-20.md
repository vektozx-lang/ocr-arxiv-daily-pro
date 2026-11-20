# OCR arXiv Daily Pro — 2026-11-20

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-19 09:10 - 2026-11-20 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4dc8a80e-88

---

## 📄 论文详情

### 1. SEAF: Selective Semantic Enrichment and Visual Evidence Fusion for Multimodal Sarcasm Detection

- **ArXiv ID**: [2611.25672v1](https://arxiv.org/abs/2611.25672v1)
- **作者**: Faxian Wan, Xiaocui Yang, Yifan Cao, Shi Feng, Daling Wang...
- **发布时间**: 2026-11-19
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.25672v1](https://arxiv.org/pdf/2611.25672v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal sarcasm detection requires textual, visual, and contextual evidence, particularly when multiple images provide complementary cues. Multimodal large language models (MLLMs) can generate auxiliary information from a post's text and images, but their outputs may mix useful background knowledge with redundant visual descriptions. We propose SEAF, a dual-branch framework for selective semantic enrichment and visual evidence fusion. SEAF assigns generated fields to distinct roles: entity background enriches semantic input, while image descriptions supply alignment statistics. The semantic branch combines the original post text, background from a frozen MLLM, and optical character recognition (OCR) text. The aligned visual branch combines global and local visual features with statistics of cross-modal and inter-image similarity. Text-Anchored Smoothed Aggregation (TASA) weights images by their similarity to the original post text while preserving contributions from images with low literal similarity. Summing the branch classification scores integrates contextual semantics with visual evidence. Experiments on the multi-image MMSD3.0 benchmark show that SEAF outperforms all compared methods.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 006ae0c3-39

---

### 2. Uncontrolled source titles: When Nature, Science, and PNAS meet Scopus

- **ArXiv ID**: [2611.25627v1](https://arxiv.org/abs/2611.25627v1)
- **作者**: Weishu Liu, Ruifeng Zhang, Haifeng Wang
- **发布时间**: 2026-11-19
- **分类**: cs.DL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.25627v1](https://arxiv.org/pdf/2611.25627v1)
- **相关度评分**: 10/10

#### 英文摘要

Bibliographic databases such as Scopus and Web of Science play a critical role in literature discovery, systematic reviews, bibliometric analyses, and research evaluation, yet their reliability depends on effective control of the quality of the bibliographic data. This study examines the problem of uncontrolled source titles in Scopus by comparing five possibly adopted journal-level retrieval strategies across three flagship journals-Nature, Science, and PNAS. Substantial discrepancies across retrieval results indicate persistent fragmentation in the source title field. A comparative analysis using the Web of Science Core Collection shows that no comparable degree of uncontrolled source-title variation is observed for the same journals. The study further explores possible mechanisms, including inheritance of different title forms from (different) upstream providers, automated parsing and OCR-related artifacts, and insufficient cross-validation. Based on these findings, the study proposes recommendations at both the user and database-provider levels to improve source-title normalization and strengthen source-level metadata governance, with implications for the accuracy and reproducibility of journal-level retrieval and evaluative uses.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: be985676-9f

---

### 3. Carry the Fine Print: Budget-Aware Visual Token Compression for Document OCR

- **ArXiv ID**: [2611.25506v1](https://arxiv.org/abs/2611.25506v1)
- **作者**: Yixuan Huang, ShengFan Zhang, Jiawei Chen
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.25506v1](https://arxiv.org/pdf/2611.25506v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual token compression often treats salience or similarity as a proxy for transcription importance. Complete document OCR breaks this assumption: small symbols and repeated entries can be indispensable to the transcript despite being visually inconspicuous. We present Select and Compensate, a two-stage framework built on a simple idea: choosing where to retain a token need not determine all the evidence it carries. Selection combines adaptive encoding resolution with global importance and local contrast to choose which tokens to retain as anchors. Compensation enriches these anchors with nearby discarded content and its relative position, without adding tokens. The OCR backbone remains frozen, and native coordinates and structural tokens are preserved. We evaluate complete page transcription across five backbones on OmniDocBench and document reconstruction on MPDocBench. With half the original visual tokens, our input-adapted configuration reaches 95.42 OmniDocBench Overall on Ovis versus 96.09 for the uncompressed model, and paired evaluations show gains over simply reducing the input resolution on both benchmarks. With the original input grid, our method stays within 0.17 points of the uncompressed model at 75% retention and exceeds a learned global selector by 4.70 points at 25%. On a fixed 200-page Ovis workload at the same 50% visual-token budget, only 3 of its outputs hit the length limit, versus 30-34 for the evaluated RTPrune, DivPrune, and HiPrune adaptations, and it finishes the batch 35-40% sooner. Code will be made publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 750ee00e-8b

---

### 4. Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem

- **ArXiv ID**: [2611.26398v1](https://arxiv.org/abs/2611.26398v1)
- **作者**: Oriol Alàs, Ian Palacín, Iván Cester, Edgar Rubión
- **发布时间**: 2026-11-20
- **分类**: cs.IR, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.26398v1](https://arxiv.org/pdf/2611.26398v1)
- **相关度评分**: 10/10

#### 英文摘要

EU-funded projects produce extensive evidence in the form of deliverables, reports, and case studies. However, this knowledge is typically scattered across projects and document structures, making it difficult to locate relevant, contextual information when making decisions. This paper introduces an Agentic AI Ecosystem that consolidates heterogeneous project documentation into a domain-aware knowledge base and provides adaptive access through an agentic Retrieval-Augmented Generation pipeline. Documents from three EU-funded projects (IMPETUS, NATALIE, and InnWater) are reconstructed into hierarchical section trees and indexed with structured metadata. Retrieval is supported by two domain-specific embedding models fine-tuned on domain data (water and climate). On top of this knowledge base, a ReAct-style controller iteratively orchestrates retrieval actions by allocating retrieval budget across domain collections and accumulating evidence until a stopping criterion is met. In a retrieval benchmark over the corpus, the proposed approach improves Mean Reciprocal Rank by 26.7% (relative) compared to a single-domain embedding baseline, indicating more consistent retrieval of relevant evidence to support cross-project knowledge synthesis and climate-resilient decision-making.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 819fe7f6-e9

---

### 5. Prism: Hierarchical Text Detection with Minimalist Design

- **ArXiv ID**: [2611.26254v1](https://arxiv.org/abs/2611.26254v1)
- **作者**: Yuchen Su, Xuesheng Wang, Zhilong Ji, Jinfeng Bai, Shijian Lu...
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26254v1](https://arxiv.org/pdf/2611.26254v1)
- **相关度评分**: 10/10

#### 英文摘要

Hierarchical text detection aims to localize words, text lines, and paragraphs while parsing their structural relationships. It provides essential structural cues for visual text understanding. To maximize accuracy, existing methods typically rely on complex multi-scale feature fusion necks and heavy-weight heads, resulting in bloated architectures and low inference efficiency. In this paper, we argue that a sufficiently pre-trained backbone can effectively replace these sophisticated external modules, while simple geometric inclusion suffices for hierarchical text structural parsing. Thus, we propose Prism, a minimalist framework for hierarchical text detection. Prism performs multi-granularity detection by attaching parallel lightweight heads to a single-scale backbone feature map, covering words, text lines, and paragraphs, and reconstructs the structural hierarchy via an efficient geometric inclusion algorithm. In addition, we systematically compare representative lightweight head archetypes and show that pixel-level regression offers the best accuracy-efficiency trade-off in this setting. Experiments on multiple public benchmarks show that our significantly simplified architecture achieves state-of-the-art (SOTA) performance with remarkable efficiency. Specifically, it runs $1.7\times$ faster than LRANet on CTW1500 while achieving higher accuracy, and surpasses the current SOTA method, OmniParser V2, by over 6 PQ points on the hierarchical HierText dataset. Code will be released soon.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f7fdd68e-41

---

### 6. RL Post-Training in Diffusion Transformers Is Activation Steering

- **ArXiv ID**: [2611.26627v1](https://arxiv.org/abs/2611.26627v1)
- **作者**: Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau...
- **发布时间**: 2026-11-20
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.26627v1](https://arxiv.org/pdf/2611.26627v1)
- **相关度评分**: 10/10

#### 英文摘要

Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately simple parameterization: a fixed set of steering vectors added to the block outputs of the frozen base model. On SD3.5-M, these vectors hold 65x fewer parameters than the RL-tuned LoRA (0.29M against 18.8M). We fit them to match the velocity predictions of public RL-tuned checkpoints, with no reward in the objective. Although the vectors are identical for every prompt, token, and sampling seed, they recover 90.0-96.3% of the reward gains of six RL-tuned image models, and 89.8% and 111.9% on two RL-tuned video models. Initialized at zero and trained with online RL, the vectors alone exceed the reward gains of weight-based RL on text rendering (OCR) and human preference (PickScore) on SD3.5-M. A constant shift thus suffices for most of the gain of policy-gradient RL post-training: without new input-dependent transformations, it steers the pretrained generator toward what it can already compute.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7d76fa7e-0a

---

### 7. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control

- **ArXiv ID**: [2611.26613v1](https://arxiv.org/abs/2611.26613v1)
- **作者**: Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo...
- **发布时间**: 2026-11-20
- **分类**: cs.RO, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26613v1](https://arxiv.org/pdf/2611.26613v1)
- **相关度评分**: 10/10

#### 英文摘要

Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an intent-grounded critique framework in which the policy agent states a local intent alongside each action, and a critic evaluates the action's outcome and failure mode against this intent. Our action-level analysis demonstrates the promising capabilities of frontier agents on direct robot control, including closed-loop recovery from local execution failures, reliable semantic grounding across diverse scenes, and strong zero-shot manipulation without task-specific adaptation. It also identifies their current limitations, including task-relevant physical execution bottlenecks such as grasping and alignment, and uneven recovery across failure modes. Finally, we validate our critic on a 400-action human-annotated benchmark and release a dataset of 12,844 annotated actions alongside a fine-tuned open-source critic, Muse-Glimmer-30B, whose failure-mode accuracy rises from 32.58% to 74.24%, enabling low-cost action-level analysis.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e6b71d56-19

---

### 8. Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware

- **ArXiv ID**: [2611.26437v1](https://arxiv.org/abs/2611.26437v1)
- **作者**: Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis, Alejandro Lancho
- **发布时间**: 2026-11-20
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.26437v1](https://arxiv.org/pdf/2611.26437v1)
- **相关度评分**: 10/10

#### 英文摘要

Frontier text-to-image (T2I) foundation models predominantly rely on multi-billion parameter Diffusion Transformers (DiTs) pretrained across massive compute clusters, creating an accessibility barrier for academic laboratories. When training DiTs from scratch on single consumer GPUs (e.g., an NVIDIA RTX 4090 with 24\,GB VRAM), practitioners encounter three primary bottlenecks: quadratic attention sequence costs, Just-In-Time (JIT) compilation graph breaks induced by variable aspect-ratio bucketing, and an autoencoder throughput wall where frozen Variational Autoencoder (VAE) operations dominate step latency. In this work, we introduce \textbf{Asuka-FM}, an end-to-end system and architectural framework demonstrating that competitive dual-stream DiTs ($\sim$206M parameters) can be pretrained from scratch on a single consumer GPU in $\sim$160 GPU hours for under \$55. Asuka-FM integrates four core designs: (i) an AdaLN-free dual-stream DiT backbone reducing parameter count; (ii) structured sequence sparsification via Sparse-Dense Residual Fusion (SPRINT) to cut attention FLOPs by over 50\%; (iii) continuous aspect-normalized Rotary Position Embeddings (RoPE) coupled with shifted square crop training, guaranteeing static tensor shapes while unlocking zero-shot virtual camera control; and (iv) a pixel adaptation phase utilizing a lightweight (10M parameter) Patch Detailer Head operating under velocity regression ($v$-prediction). Evaluated on open-domain benchmarks without benchmark-specific fine-tuning, Asuka-FM achieves GenEval 0.588 / DPG 78.96 scores at 256px and GenEval 0.609 / DPG 78.51 scores at 512px, setting a new Pareto-optimal efficiency standard for democratic foundation modeling.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 689182ac-4a

---

### 9. ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step

- **ArXiv ID**: [2611.26389v1](https://arxiv.org/abs/2611.26389v1)
- **作者**: Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan...
- **发布时间**: 2026-11-20
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26389v1](https://arxiv.org/pdf/2611.26389v1)
- **相关度评分**: 10/10

#### 英文摘要

Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of decisions. We present ViDecide, a decision-centric framework that trains video diffusion models to predict state transitions causally and decide when to stop, with a decision-focused training schedule. We further propose Corrective Fine-tuning (CFT), which corrects failed decisions by mapping their noise to the model's own successful continuations, achieving stable improvement without policy-gradient optimization. Across abstract games, planning tasks, and a new benchmark of multi-step robot planning, ViDecide achieves an average strict success rate of 83.8%, far above 23.3% for standard fine-tuning and 67.8% for the strongest prior method, and generalizes to larger puzzles and unseen layouts. Our framework therefore unlocks greater potential for video generation models as reliable reasoners and planners in the visual world. Project page: https://kevin-thu.github.io/ViDecide.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 282dd092-a3

---

### 10. ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images

- **ArXiv ID**: [2611.26586v1](https://arxiv.org/abs/2611.26586v1)
- **作者**: Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan, Emilio Tylson Baixauli, Yu Cao...
- **发布时间**: 2026-11-20
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.26586v1](https://arxiv.org/pdf/2611.26586v1)
- **相关度评分**: 10/10

#### 英文摘要

Graphic designs are ordered compositions of RGBA layers whose separation enables selection, movement, and reuse. Existing layered models represent each layer with a full-canvas or region-sized spatial latent grid, so representation size grows with the cumulative spatial extent of the layers. We present ProtoDiffusion, a latent-diffusion framework built on ProtoVAE, a multi-layer variational autoencoder that encodes a design into one shared spatial prototype and one candidate vector per layer. Each candidate conditions a shared decoder to reconstruct its corresponding RGBA layer. For $N$ layers, the representation contains $HW+N$ tokens before backbone-specific packing, compared with $NHW$ for full-grid-per-layer representations. ProtoDiffusion jointly denoises the prototype and a fixed set of candidate slots, conditioned on an image or text, with bounding boxes as optional layout guidance. The model leaves unneeded slots empty and determines the number of layers and, in absence of boxes, their layout, requiring neither as input. The same architecture supports both image-to-design and text-to-design. ProtoVAE achieves high-fidelity reconstruction from its compact shared latent representation, reaching 40.43 dB PSNR on layer crops. On the LayerD evaluation split, image-to-design achieves RGB L1 scores of 0.040 with bounding boxes and 0.057 without, with box-guided alpha soft IoU (0.850) comparable to the strongest fine-tuned baseline (0.871). On merged images, text-to-design reaches 66.41 FID versus 86.84 for FLUX.2 [klein], achieves a 0.860 text-accuracy score, and runs $19.1\times$ faster than the same-backbone generation-then-decomposition cascade.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d20acd3f-16

---

### 11. Posterior Matching Distillation

- **ArXiv ID**: [2611.26629v1](https://arxiv.org/abs/2611.26629v1)
- **作者**: Hidir Yesiltepe, Julius Berner, Arash Vahdat, Pinar Yanardag
- **发布时间**: 2026-11-20
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26629v1](https://arxiv.org/pdf/2611.26629v1)
- **相关度评分**: 10/10

#### 英文摘要

Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this by matching the student's output distribution to the teacher's. This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity across samples. We introduce Posterior Matching Distillation (PMD), a new member of the distribution-based distillation family that combines mode-covering posterior sampling with any-step generation. At zero population loss, PMD recovers the teacher's full posterior of clean images at each trained noise level. Its stochastic student supports any-step sampling budgets within the trained timestep grid without further training. To learn these posteriors, PMD matches exponentially reweighted averages of student samples conditioned on a fixed noisy state to corresponding teacher posterior means. Under Gaussian corruption, exponentially tilted posterior mean is a single teacher evaluation at a shifted input. We prove that, matching tilted means over an open neighborhood uniquely identifies the full posterior. PMD thus supervises the entire conditional distribution through a family of mean constraints, without any auxiliary student-score network. Experiments on SDXL and FLUX.2 [klein] 4B demonstrate that PMD achieves the best FID among 4-step methods on both models, while maintaining competitive or leading performance across prompt-alignment and perceptual-quality metrics.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 823c577e-d5

---

### 12. PlayCraft: Designing Engaging Games from Agent Play Experience

- **ArXiv ID**: [2611.26624v1](https://arxiv.org/abs/2611.26624v1)
- **作者**: Weihao Cheng
- **发布时间**: 2026-11-20
- **分类**: cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26624v1](https://arxiv.org/pdf/2611.26624v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 718cb320-97

---

### 13. One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning

- **ArXiv ID**: [2611.26617v1](https://arxiv.org/abs/2611.26617v1)
- **作者**: Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang...
- **发布时间**: 2026-11-20
- **分类**: cs.CV, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.26617v1](https://arxiv.org/pdf/2611.26617v1)
- **相关度评分**: 10/10

#### 英文摘要

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics. By controlling information access and optimizing both dynamics end-to-end through a compact bottleneck, O$^{2}$LaF learns transferable actions from unlabeled videos. Across navigation and robotic manipulation, O$^{2}$LaF sets a new state of the art in few-shot action probing and enables stronger zero-shot action transfer across visual contexts and embodiments. Beyond generative video priors, we further extend our framework to predictive representation priors such as V-JEPA2, achieving competitive performance. Our findings suggest a broader paradigm for latent-action learning: repurposing pretrained video models to discover transferable actions and predict their consequences.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f0159e38-43

---

### 14. ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement

- **ArXiv ID**: [2611.26615v1](https://arxiv.org/abs/2611.26615v1)
- **作者**: Yansong Qu, Wesker Zheng, Quanjian Song, Zhiyuan Zhang, Xiao Cao...
- **发布时间**: 2026-11-20
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.26615v1](https://arxiv.org/pdf/2611.26615v1)
- **相关度评分**: 10/10

#### 英文摘要

High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory costs. We present ScaleWorld, a causal video model that unifies low-resolution world prediction and high-resolution refinement within a single shared backbone. By refining its own predictions, ScaleWorld produces high-resolution world videos without requiring a separate refinement model. For each video chunk, the shared backbone first completes a low-resolution prediction and then performs one-step high-resolution refinement conditioned on that prediction. To support efficient streaming generation, we maintain separate causal states with a long low-resolution history for prediction and a short high-resolution history for refinement. To address task interference during distillation, we separate specialist optimization from capability consolidation and introduce task-asymmetric on-policy distillation (TA-OPD). This procedure transfers prediction and refinement behaviors from specialized teachers into a shared student through local velocity matching under their respective sampling and history policies. {Extensive experiments demonstrate that ScaleWorld achieves high-quality world generation with improved computational and memory efficiency.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b094d7e0-0d

---

### 15. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

- **ArXiv ID**: [2611.26603v1](https://arxiv.org/abs/2611.26603v1)
- **作者**: Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong...
- **发布时间**: 2026-11-20
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.26603v1](https://arxiv.org/pdf/2611.26603v1)
- **相关度评分**: 10/10

#### 英文摘要

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 24ea1c6d-f3

---
