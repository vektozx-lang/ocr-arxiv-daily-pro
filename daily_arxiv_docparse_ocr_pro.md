# OCR arXiv Daily Pro — 2026-10-20

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-19 09:10 - 2026-10-20 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 991f0454-fd75-4

---

## 📄 论文详情

### 1. GAIDA: Generative AI for Human-in-the-Loop Document Annotation

- **ArXiv ID**: [2610.26362v1](https://arxiv.org/abs/2610.26362v1)
- **作者**: Islam Mesabah, Ali Elhosary, Priyabanta Sandulu, Darko Obradovic, Sebastian J. Vollmer
- **发布时间**: 2026-10-19
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.26362v1](https://arxiv.org/pdf/2610.26362v1)
- **相关度评分**: 10/10

#### 英文摘要

Document annotation is a fundamental yet labor-intensive step in building document information extraction systems. While Optical Character Recognition (OCR) and Large Language Models (LLMs) can automate parts of this process, we argue that annotation systems should be judged not by how completely they remove human effort, but by how effectively they redirect it toward review and correction. We propose a modular human-in-the-loop architecture that integrates OCR-based extraction, LLM-based semantic pre-annotation, and human validation in a single editable workflow, and present \textbf{GAIDA}, a research prototype serving as its reference implementation. GAIDA supports interchangeable OCR engines, LLM backends, and prompt configurations, and enables stage-specific measurement of annotation effort. In an initial single-annotator, stage-specific study on the FUNSD scanned-form and WildReceipt retail-receipt benchmarks, OCR assistance reduced region-creation and transcription time by up to \textbf{80.9\%}, and reviewing LLM pre-annotations reduced semantic-labeling time by up to \textbf{73.7\%}, despite imperfect pre-annotations of 78.86\% and 86.98\% Micro F1 on FUNSD and WildReceipt, respectively. Finally, we reuse the same implementation, adapting only OCR and prompt configuration, to build and openly release \textbf{AraReceipt}, a manually annotated dataset of 100 Arabic receipt images labeled with 25 key-information classes. The results indicate that imperfect automated outputs provide practical value when presented as editable suggestions under human control.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a7e606e0-b565-4

---

### 2. One Fact, Many Places: Redundant Evidence in Long Visual Documents Breaks Single-Gold Evaluation of Retrieval, Citation and Attribution

- **ArXiv ID**: [2610.26401v1](https://arxiv.org/abs/2610.26401v1)
- **作者**: Xiaokang Yuan, Binhui Yao, Luwei Yang, Ruimin Chen, Zeng Wang
- **发布时间**: 2026-10-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26401v1](https://arxiv.org/pdf/2610.26401v1)
- **相关度评分**: 10/10

#### 英文摘要

Document understanding is increasingly judged on where an answer comes from, scored against annotated gold locations as if each fact lived in one place. In long visual documents, a fact often lives in several places: a chart value is restated in the text, a key figure reappears in the summary. We ask how often such copies occur in standard benchmarks and what they do to evaluation. We annotate 420 questions from MMLongBench-Doc and MMDocRAG with the locations that independently establish each required fact, checked by two independent reviewers. Copies are common and often cross-modal: 19.5% of MMLongBench-Doc test questions have a strict copy outside the gold, and in 28% of MMDocRAG questions a non-gold candidate alone supplies a required fact. Single-gold scoring then fails in three predictable ways. A retriever that finds a copy is scored as a miss: page recall@1 of text and visual retrievers is underestimated by 13-24 points on questions with a cross-page copy. A model that cites a copy is scored as citing wrongly: crediting equivalent evidence reverses 11% of pairwise orderings among 65 competitive MMDocRAG systems. Masking the gold region leaves the fact available elsewhere: with a copy in the input, 41-56% of correct answers across four models survive it yet fail once every annotated instance is masked. Set-level masking with automatically found copies closes 78% of the gap to masking every annotated instance at matched granularity (three models); an unverified key-string rule lowers survival at least as far but masks three times the area. We release the annotations and redundancy-aware metrics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 78910f1c-09d4-4

---

### 3. DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal

- **ArXiv ID**: [2610.26081v1](https://arxiv.org/abs/2610.26081v1)
- **作者**: Deshui Miao, Yuhang Ma, Shaoyong Jia, Wenzhao Gao, Yue Zhang...
- **发布时间**: 2026-10-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26081v1](https://arxiv.org/pdf/2610.26081v1)
- **相关度评分**: 10/10

#### 英文摘要

Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while preserving surrounding content. Existing methods use temporal propagation or source-conditioned generation, but can leave residual overlays and distort scene structure when useful source information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the clean video from the source latent with fixed source guidance. Specifically, we train a shared velocity network along paired source-to-clean paths using region-weighted flow matching, enabling successive cor- rections from intermediate states. To select local source cues, we develop visibility-normalized temporal aggregation that excludes masked positions and averages the remaining observations. Global source context and edit-region embeddings complement these cues through additive condi- tioning, retaining a single video-token sequence. To evaluate scene recovery across diverse overlay conditions, we introduce DVTE-Bench, comprising 1,631 paired videos across eight text-overlay categories, with OCR-screened clean targets, frame-aligned pixel masks, and a common evaluation protocol. Experiments on the complete release show that DeOverlay outperforms four baselines on all five reconstruction and perceptual metrics, reducing Mask LPIPS and Mask VFID by 58.3% and 70.3%, respectively, relative to the strongest evaluated baseline. Additional qualitative examples demonstrate the removal of graphic logos and stickers. We will make the complete benchmark, evaluation code, and test outputs availabl. Project page:https://yahooo-m.github.io/DVTE-Bench/

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ca04cfee-421d-4

---

### 4. VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token

- **ArXiv ID**: [2610.26857v1](https://arxiv.org/abs/2610.26857v1)
- **作者**: Sangbeom Lim, Seoung Wug Oh, Heeji Yoon, Seungryong Kim, Joon-Young Lee
- **发布时间**: 2026-10-20
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26857v1](https://arxiv.org/pdf/2610.26857v1)
- **相关度评分**: 10/10

#### 英文摘要

Diffusion-based video matting has recently emerged as a leading approach, leveraging video diffusion priors from internet-scale pretraining to achieve strong zero-shot generalization from limited synthetic data. However, the heavy compute of these diffusion backbones limits inference to a short chunk of just 6 to 24 frames, so even ordinary videos span multiple chunks. Because each chunk is matted independently from coarse mask guidance, existing methods fail to maintain consistency across chunk boundaries, producing flickering edges and discontinuous transparency. We address this with a mask-guided diffusion-matting framework built on two ideas. The RGB and mask conditioning are represented as separate token streams that interact through full spatio-temporal self-attention, letting the model adaptively combine fine RGB texture with coarse mask layout rather than committing to a fixed channel-wise fusion. On top of this, we propose a novel pair of learnable embeddings, the preserve token and the refine token, that act as a per-frame conditioning interface and enable a sliding-window inference scheme in which already-generated mattes are propagated across chunk boundaries for local temporal consistency, complemented by a globally shared reference anchor at every chunk to prevent error accumulation in long sequences without any additional training. Across standard video matting benchmarks and in-the-wild long footage, our framework outperforms prior diffusion-based methods in both fine-detail accuracy and temporal consistency, and uniquely maintains consistency across chunk boundaries on long videos.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3b8e713f-8223-4

---

### 5. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

- **ArXiv ID**: [2610.26848v1](https://arxiv.org/abs/2610.26848v1)
- **作者**: Zekai Li, Jiayi Yu, Jinlu Zhang, Luyang Niu, Zekun Qi...
- **发布时间**: 2026-10-20
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26848v1](https://arxiv.org/pdf/2610.26848v1)
- **相关度评分**: 10/10

#### 英文摘要

In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analysis of experimental results motivates the Physical Barrel Hypothesis: different capabilities may constrain different parts of improvement. The five-axis metrics also distinguish systems with close public benchmark averages and show that high scores need not come with early or efficient gains. We study observational scaling from two perspectives: predicting the relative performance of VLM agents from their public capabilities, and forecasting later progress from early physical feedback. Together, these analyses ask how quickly and how far an agent can improve. Moreover, we conduct workspace interventions and then analyze what improvement leaves behind. Removing history reduces late-round success, frozen workspaces remain useful on unseen layouts, and three cross-task cases achieve success earlier. The results suggest that scene-specific adaptation and reusable experience can coexist.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4ccf2870-13e9-4

---

### 6. Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation

- **ArXiv ID**: [2610.26801v1](https://arxiv.org/abs/2610.26801v1)
- **作者**: Yingshuang Zou, Xiaoyu Shi, Yawen Luo, Ziang Li, Qinghe Wang...
- **发布时间**: 2026-10-20
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.26801v1](https://arxiv.org/pdf/2610.26801v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and fine-grained controllability. Existing multi-shot video generation approaches achieve strong consistency but still fall short in controllability. In this paper, we propose Mise-en-Video (MeV), a highly controllable multi-shot video generation framework that allows video creators to conduct staging the multi-shot in the 3D space and then generate the corresponding multi-shot video. To achieve this, our framework combines a hierarchical attention mechanism for multi-level narrative consistency with 3D-aware layout guidance for precise, per-shot spatial control. To support training and evaluation, we develop standardized annotation pipelines and construct a 160K-video dataset with hierarchical multi-shot texts and oriented 3D bounding boxes. Extensive experiments demonstrate that MeV consistently outperforms strong baselines in video quality, inter-shot consistency, and subject-level controllability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d7d50008-7400-4

---

### 7. Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models

- **ArXiv ID**: [2610.26797v1](https://arxiv.org/abs/2610.26797v1)
- **作者**: Agus Sudjianto, Denis Burakov
- **发布时间**: 2026-10-20
- **分类**: stat.ML, cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.26797v1](https://arxiv.org/pdf/2610.26797v1)
- **相关度评分**: 10/10

#### 英文摘要

Candidate-scoring decision models return a probability distribution over a presented set of answers. Public documentation of one such system, Jev, and of an open counterpart, JevAny, describes three training ingredients that determine what these probabilities estimate: soft targets from larger models, a frozen pretrained backbone and temperature calibration. We analyze each ingredient in Gaussian surrogates where the finite-sample risk can be computed exactly. A student trained on teacher targets inherits the teacher's bias, which more student data does not remove and agreement with the teacher does not reveal. A fixed representation lowers the risk only below an explicit sample-size threshold. In a probit model the exact recalibration map is a temperature scaling, which removes all excess risk only when the teacher's coefficient has the correct direction and otherwise leaves a residual that calibration diagnostics do not detect. Under Luce's choice axiom, candidate scores are coherent across refinements of an event if and only if they aggregate by log-sum-exp. On 231,521 credit card complaints from the Consumer Financial Protection Bureau, where the decision is whether a complaint ends in monetary relief, a student trained on a logistic teacher's probabilities ends at the teacher's decision cost while a student trained on outcomes goes 8% below it, a 30B model read zero-shot remains worse than the teacher after recalibration, and that model departs from the coherence condition by 17.5 decibans. Pretrained representations reduce the labeled data required and calibration corrects the scale of the probabilities, but neither corrects a biased teacher, so the probabilities have to be checked against realized outcomes.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 002d628a-002b-4

---

### 8. TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning

- **ArXiv ID**: [2610.26754v1](https://arxiv.org/abs/2610.26754v1)
- **作者**: Liana Patel, Rishabh Ranjan, Ion Stoica, Matei Zaharia, Carlos Guestrin
- **发布时间**: 2026-10-20
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.26754v1](https://arxiv.org/pdf/2610.26754v1)
- **相关度评分**: 10/10

#### 英文摘要

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to-end learning despite the non-differentiable top-K operator for token pruning, we introduce token-gated attention, a mechanism inspired by Mixture-of-Experts that re-weights attention logits using token importance scores. Across diverse tasks, TokenGate achieves $1.4$-$11.3\times$ faster time-to-first token (TTFT) and $1.5$-$3.4\times$ lower peak memory at no accuracy degradation for prefill in transformers. Compared to the best-performing prior methods for token-pruning, TokenGate gives up to $6.4\times$ faster prefill and $2\times$ lower peak memory. TokenGate natively extends both standard transformers (e.g., Qwen3) and hybrid-attention models (e.g., Qwen3.5) with simple lightweight adaptation comparable to standard parameter-efficient fine-tuning. We make our code available at: https://github.com/tokengate-models/TokenGate.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f8de0368-f2bb-4

---

### 9. EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition

- **ArXiv ID**: [2610.26730v1](https://arxiv.org/abs/2610.26730v1)
- **作者**: Vincenzo Perri, Ciro Cattuto, Daniela Paolotti
- **发布时间**: 2026-10-20
- **分类**: cs.CL, cs.DL, physics.soc-ph
- **PDF**: [https://arxiv.org/pdf/2610.26730v1](https://arxiv.org/pdf/2610.26730v1)
- **相关度评分**: 10/10

#### 英文摘要

To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources. We present EpiLens, a lightweight, open-source retrieval-augmented generation package that applies a fixed retrieval template and output schema to every paper in a corpus and links outputs to source passages. We build a corpus of 2,297 papers from the sources of a multi-pathogen parameter study and evaluate EpiLens's paper-classification workflow against 214 manually labelled papers. Without task-specific training data, the classifier matches or exceeds the tested supervised and zero-shot baselines across four tasks. The study's early extraction sheets cite published sources for 327 estimates. We link each estimate to a cited document or to corpus studies included by a review. Then, we use the classifier's labels to compare the papers associated with different parameters and pathogens. EpiLens labels more papers linked to reproduction numbers than fatality risks as model-based (54% versus 22%, compared with 62% versus 24% in the manual labels). The gap is consistent with the frequent use of transmission models to estimate reproduction numbers and persists within each of five pathogens compared. Beyond the contrast between parameters, the model-based share of papers linked to incubation-period estimates differs by pathogen: 55% for SARS-CoV-2 versus 6% for mpox.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c4547578-5406-4

---

### 10. SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

- **ArXiv ID**: [2610.26659v1](https://arxiv.org/abs/2610.26659v1)
- **作者**: Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan...
- **发布时间**: 2026-10-20
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.26659v1](https://arxiv.org/pdf/2610.26659v1)
- **相关度评分**: 10/10

#### 英文摘要

Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target objects. Given an object inventory, RGB observations, camera calibration, and camera poses, agents control a camera to explore each scene and estimate object centers in a shared coordinate frame. The task requires coordinating viewpoint selection, cross-view association, geometric estimation, and map revision under bounded interaction budgets. Evaluation jointly measures localization accuracy and target coverage through object-scale overlap scores that penalize missing predictions. Experiments with frontier VLMs reveal substantial limitations: the strongest evaluated model, Claude Opus 5.5, achieves a mean overlap score of 41.71%, with 47.23% of targets exceeding an intersection-over-union (IoU) threshold of 0.5 and only 3.25% exceeding 0.9. These results reveal a substantial gap between recovering coarse object layouts and constructing complete, precise metric maps. SpatialScout provides a quantitative testbed for developing agents that build reliable 3D spatial representations through active perception. Code is available at https://github.com/JesseZZZZZ/SpatialScout.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cbdec856-a652-4

---

### 11. Text-to-Image Generative Modeling Without Language Pretraining

- **ArXiv ID**: [2610.26863v1](https://arxiv.org/abs/2610.26863v1)
- **作者**: Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas, Ehsan Adeli, Jiajun Wu...
- **发布时间**: 2026-10-20
- **分类**: cs.LG, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26863v1](https://arxiv.org/pdf/2610.26863v1)
- **相关度评分**: 10/10

#### 英文摘要

Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with 18.2$\times$ less pretraining compute. Further, Halcyon-1.6B outperforms JiT-T2I-XXL/8++ (35.3 vs. 41.0 gFD) with 275$\times$ less pretraining compute. Controlled experiments show that text-only pretraining does not improve T2I generation. Halcyon also learns image captioning by replacing caption dropout with I2T supervision, maintaining competitive T2I generation quality under the same pretraining budget. We show that strong T2I systems can be trained from scratch without internet-scale language pretraining. Code and models are available at https://cs.stanford.edu/~keshik/halcyon

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8454c917-1dee-4

---

### 12. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

- **ArXiv ID**: [2610.26860v1](https://arxiv.org/abs/2610.26860v1)
- **作者**: Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, Sibo Peng...
- **发布时间**: 2026-10-20
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.26860v1](https://arxiv.org/pdf/2610.26860v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through heterogeneous tools, whose outputs must be made interpretable to the model and retained across reasoning steps. We introduce OpenVLHarness, a multimodal reasoning harness organized around a capability layer and persistent multimodal memory. The capability layer combines task-level tool interfaces with evidence rendering, providing consistent access to heterogeneous backends and converting their outputs into model-readable observations. Persistent multimodal memory retains the corresponding images, structured data, and web references as addressable artifacts throughout each query. A coding interface executes generated programs over stored data, enabling computations that combine results from multiple tools. Together, these mechanisms support an iterative process of acquiring, inspecting, and composing multimodal evidence. Evaluated on 22 benchmarks with eight open and proprietary backbones, OpenVLHarness improves average scores by 9.7-12.6 points over matched no-tool baselines, including +11.2 with Qwen3-VL-8B, +9.7 with Kimi K3, and +9.9 with GPT-6 Astra. With GPT-6 Luna at medium reasoning effort, OpenVLHarness outperforms the base model, Codex, and Visual Sketchpad at maximum effort by 7.7-8.5 points while incurring at most 37% of their model-token cost.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: de6b2292-0362-4

---

### 13. Can It Actually Work? Synthesizing Functional CAD Mechanisms

- **ArXiv ID**: [2610.26861v1](https://arxiv.org/abs/2610.26861v1)
- **作者**: Wenqian Zhang, Yangyi Huang, Zigeng Xu, Weiyang Liu, Zhen Liu
- **发布时间**: 2026-10-20
- **分类**: cs.CV, cs.CL, cs.GR
- **PDF**: [https://arxiv.org/pdf/2610.26861v1](https://arxiv.org/pdf/2610.26861v1)
- **相关度评分**: 10/10

#### 英文摘要

While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework that translates abstract requirements into candidate-specific physical tests and uses simulation feedback to guide design revisions. To systematically evaluate this capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families with interdependent and multi-step operations. Experiments across frontier LLM agents show that FunCAD-Harness exposes subtle mechanical failures invisible to visual inspection, substantially improving functional success rates over standard simulation-augmented baselines. Ultimately, our work marks a step toward CAD agents capable of translating human intent into working mechanisms.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 25bc1bfc-dfef-4

---

### 14. Reinforcement Learning with Visually Attributable On-Policy Self-Distillation

- **ArXiv ID**: [2610.26856v1](https://arxiv.org/abs/2610.26856v1)
- **作者**: Shiao Xie, Siyu Chen, Jianwei Lv, Xiandong Li, Yujin Wang
- **发布时间**: 2026-10-20
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.26856v1](https://arxiv.org/pdf/2610.26856v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate visual evidence with non-visual shifts induced by linguistic priors, response style, or the privileged view itself. We formalize this phenomenon as privileged-correction contamination: a token-level correction is contaminated when its update direction cannot be consistently attributed to the privileged visual evidence. Directly distilling contaminated corrections may therefore reinforce erroneous token-level updates. To address this issue, we propose reinforcement learning with visually attributable on-policy self-distillation, an evidence-consistent paradigm that augments task-level RLVR supervision with privileged token-level corrections grounded in visual evidence. We instantiate this paradigm with Visual-Attribution Gating (VAG), which uses the verifier-derived advantage as the optimization anchor and validates each privileged correction against the contrast between evidence-present and evidence-degraded teacher views. By admitting only corrections directionally supported by this visual contrast, VAG preserves visually grounded guidance while suppressing inconsistent residuals. Experiments across six visual reasoning benchmarks show that VAG consistently outperforms GRPO and OPSD methods, establishing new state-of-the-art average performance.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c498677d-dc1b-4

---

### 15. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- **ArXiv ID**: [2610.26855v1](https://arxiv.org/abs/2610.26855v1)
- **作者**: Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu...
- **发布时间**: 2026-10-20
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2610.26855v1](https://arxiv.org/pdf/2610.26855v1)
- **相关度评分**: 10/10

#### 英文摘要

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through camera poses and manipulation through projected skeletons, with robot skeletons combining embodiment-specific forward kinematics with extensive manual keypoint annotation and correction. We also introduce Xp-Teleop, a long-horizon loco-manipulation benchmark based on high-quality dexterous humanoid teleoperation data. Evaluations demonstrate state-of-the-art performance across five cross-embodiment benchmarks (DreamDojo, $Ψ_0$, $ω$-HOME, Xp-Teleop, and AgiBot) and on held-out human egocentric video, from zero-shot inference to few-shot and full-data post-training. Scaling human pre-training data improves performance on both human and robot evaluations. After distillation, our model supports real-time, minute-long rollouts, enabling live VR interaction. Applications in policy evaluation, model-based planning, and world-action modeling further demonstrate the model's utility for embodied decision-making.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2b6f9f81-bc1b-4

---
