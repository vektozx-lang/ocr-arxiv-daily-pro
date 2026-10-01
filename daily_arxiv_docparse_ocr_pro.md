# OCR arXiv Daily Pro — 2026-10-01

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-30 09:10 - 2026-10-01 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 483469b9-3636-4

---

## 📄 论文详情

### 1. ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing

- **ArXiv ID**: [2609.40356v1](https://arxiv.org/abs/2609.40356v1)
- **作者**: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu
- **发布时间**: 2026-10-01
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.40356v1](https://arxiv.org/pdf/2609.40356v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene text editing is well studied for images, video scene text editing that achieves high visual quality, temporal consistency, and edit locality remains underexplored. Existing resources offer limited paired real-video data, and general video-editing metrics do not directly measure whether the requested text remains correct over time. We introduce ViTeX-Bench, a benchmark suite comprising ViTeX-Dataset and a three-axis evaluation protocol. The dataset contains 387 real-world 720p videos with text-region masks and editing instructions: 230 provide reviewed, pipeline-generated paired edits for training, and 157 form a frozen evaluation split. The protocol evaluates text correctness, visual and temporal quality, and edit locality through 13 metrics, with one primary metric per axis and a Pareto comparison of their trade-offs. OCR calibration, human evaluation, and annotation-sensitivity analyses support the interpretation of these scores. Across eight baselines from four editing families, accurate text, temporal stability, and scene preservation remain difficult to achieve together. We also release ViTeX-Edit-14B, an open-source reference editor fine-tuned on the paired training split with motion-aligned glyph-video conditioning. It achieves CharAcc 0.688, the highest mean among the evaluated video-native editors, and the lowest comparable text-crop Warp among raw editor outputs. ViTeX-Bench provides a reproducible foundation for studying these trade-offs in video scene text editing.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b25b6d21-f7c5-4

---

### 2. Linguistic Loopholes in LLM Unlearning: From a 174-Language Benchmark to Coverage-Aware Unlearning

- **ArXiv ID**: [2609.40286v1](https://arxiv.org/abs/2609.40286v1)
- **作者**: Tyler Skow, Shravan Chaudhari, Rama Chellappa, Abhay Yadav
- **发布时间**: 2026-10-01
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.40286v1](https://arxiv.org/pdf/2609.40286v1)
- **相关度评分**: 10/10

#### 英文摘要

Unlearning a fact in one language does not guarantee its removal in others as changing the query or even the requested answer language can reopen seemingly forgotten knowledge -- a cross-lingual loophole. The most straightforward solution to this challenge -- unlearning in all languages -- is neither scalable nor desirable as it amplifies damage to unrelated model capabilities. We introduce the task of language budgeted multilingual unlearning where the goal is to select a subset of languages that maximizes cross-lingual erasure. To study this task we introduce the Cross-Lingual Unlearning Tensor, an unlearning benchmark that spans 174 language--script pairs and 25 atomic paraphrase types to examine when forgetting generalizes across linguistic expressions of the same knowledge. We further propose COVER, which selects source languages to maximize predicted COVERage of languages receiving no forget supervision, enabling unlearning on a language budget. Surprisingly, we find naively selecting strong individual sources does not reliably compose into strong source sets motivating our development of COVER. At deployment COVER only requires benign calibration data and access to the frozen model. Across three model families and two disjoint forget sets, COVER reduces mean held-out residual access by 7.8--27.3% relative to uniform source selection. We find these gains extend beyond synthetic benchmarks to real news documents in low-resource language settings using human translated data from the Low Resource Languages for Emergent Incidents (LORELEI) corpus.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 569e7038-57bf-4

---

### 3. Index-Translate: A Multilingual Translation Model Family -- Text, Speech, Controlled Dubbing, and Long-Document Translation

- **ArXiv ID**: [2609.40181v1](https://arxiv.org/abs/2609.40181v1)
- **作者**: Tianjiao Li, Mengran Yu, Chenyu Shi, Lusheng Zhang, Qisi Chen...
- **发布时间**: 2026-10-01
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.40181v1](https://arxiv.org/pdf/2609.40181v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce Index-Translate, a multilingual translation model family that combines a shared multilingual foundation with specialized training for general translation, instruction following, speech translation, controlled dubbing, and long-document translation. It includes three model sizes, 2B, 9B, and 35B-A3B, and supports translation in 150 languages, with multilingual instruction following. Evaluations on general translation and complex translation instructions show that Index-Translate outperforms translation models of comparable size and achieves performance comparable to 100B-scale translation models and frontier models. Index-Echo provides end-to-end speech-to-text and speech-to-speech translation, outperforming existing end-to-end models and achieving performance comparable to frontier omni models. Index-Homura extends the family to syllable-controlled dubbing. Index-NativeLong introduces native long-document translation with a dedicated task formulation and benchmark. These capabilities support diverse translation tasks, including multilingual content production.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 55db2bdd-84ed-4

---

### 4. MatLoom: Layered Text-to-Material Generation in a Compact Program Space

- **ArXiv ID**: [2609.40322v1](https://arxiv.org/abs/2609.40322v1)
- **作者**: Anson Y. Lam, Shuqing Li, Michael R. Lyu
- **发布时间**: 2026-10-01
- **分类**: cs.CV, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.40322v1](https://arxiv.org/pdf/2609.40322v1)
- **相关度评分**: 10/10

#### 英文摘要

Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretrained language models. Each program composes alpha-masked layers whose shared spatial expressions define coverage and physically based rendering (PBR) channels, making dependencies between patterns, color, and relief explicit. A standalone interpreter evaluates the program into material maps, while the source retains named fields and layer parameters for subsequent authoring. Without task-specific fine-tuning, our pipeline uses parser-guided repair and preview-based critique to revise material designs, then searches noise seeds while keeping each candidate's remaining source fixed. On a curated benchmark of 141 prompts evaluated with six backbones, our best-performing configuration achieves higher mean scores than three diffusion baselines on all four flat-layout prompt-alignment metrics. Its initial programs already exceed all three baselines on mean BLIPScore, before critique or seed search. Retained programs have a median length of 21 lines when pooled across backbones. In a blind four-way comparison involving 30 participants and 20 prompts, our renders receive 59.2% of choices, compared with 19.3% for the most-preferred baseline. Compact executable programs thus offer a way to generate prompt-aligned materials while retaining their construction as part of the asset.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: edf4a6e9-d0a5-4

---

### 5. Better Deck or Different Judge? Evaluating Agentic Harness Gains in Corporate and Investment Banking

- **ArXiv ID**: [2609.39958v1](https://arxiv.org/abs/2609.39958v1)
- **作者**: Ludovic Gibert, Matis Despujols, Andre-Louis Rochet
- **发布时间**: 2026-09-30
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.39958v1](https://arxiv.org/pdf/2609.39958v1)
- **相关度评分**: 10/10

#### 英文摘要

Corporate and investment banking teams use presentations to support credit decisions and advise clients on financing and transactions. Producing these decks requires reconciling financial data, tracing sources and turning analysis into a recommendation. We retrospectively study the development of an agentic harness combining a 27B language model, financial calculations, narrative templates and validation checks. LLM judges guide engineering changes and assess the resulting decks, raising the question of whether higher scores reflect better documents or changes in grading. In shared-session text-only grading with template markers removed, five judges score the complete system 20.4 to 33.6 points out of 95 above the same model generating directly from a short prompt. Every judge scores the system higher on all seventeen development deliverables. Margins against direct Opus generation from a short prompt range from -4.7 to +0.8 points. Judges agree on broad progress across development rounds but agree less on final-deck rankings than on pooled scores. Repeated grading also shifts scores on unchanged decks, making small improvements difficult to distinguish from judge variability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b6bae101-dbff-4

---

### 6. TRACE: Trajectory Selection for Parallel Scaling of Search Agents

- **ArXiv ID**: [2609.39912v1](https://arxiv.org/abs/2609.39912v1)
- **作者**: Qisheng Zhou, Zhen Xiong, Qiaoyu Tan
- **发布时间**: 2026-09-30
- **分类**: cs.LG, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.39912v1](https://arxiv.org/pdf/2609.39912v1)
- **相关度评分**: 10/10

#### 英文摘要

Parallel search may generate a correct answer that final-answer voting fails to select. We formulate this consolidation stage as trajectory selection and introduce TRACE (Trajectory Ranking with Aggregated Cross-Rollout Evidence), a lightweight learned selector that ranks completed trajectories using the search evidence behind their answers. TRACE preserves individual query and evidence occurrences, connects rollouts through shared content or document identity, and propagates information across these relations. Each candidate answer then reads the updated states of its own trajectory, preserving retrieval provenance while incorporating evidence from related rollouts. Trained with answer-level supervision over frozen text embeddings, TRACE returns an existing answer without additional search or autoregressive aggregation. One selector per search setting transfers across rollout policies and agent backbones without agent-specific fine-tuning, improving over voting across six WebQA policies and six long-horizon dataset-backbone combinations at $K=16$. On Qwen2.5-14B Base/SFT WebQA pools, TRACE achieves 45.2/49.2% EM, compared with 43.9/48.0% for the strongest Qwen3-32B generative aggregators. On long-horizon FRAMES, GAIA, and BrowseComp, it reaches 78.6% average accuracy, exceeding majority voting by 3.1 percentage points. On Base WebQA pools, TRACE with only 8 rollouts comes within 0.4 points of majority voting over 64. TRACE also achieves at least $10\times$ higher processing throughput than SolAgg, SummAgg, and AggAgent across all seven WebQA benchmarks. These results show that reusing cross-rollout search evidence provides an effective and efficient alternative to heavyweight generative aggregation for parallel search. Code is available at https://github.com/Jaasssoooonnnnn/TRACE.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 54106729-f394-4

---

### 7. Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces

- **ArXiv ID**: [2609.40362v1](https://arxiv.org/abs/2609.40362v1)
- **作者**: Hongyuan Tao, Xinggang Wang, Lianghui Zhu, Yongkang Li, Yunchao Wei...
- **发布时间**: 2026-10-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40362v1](https://arxiv.org/pdf/2609.40362v1)
- **相关度评分**: 10/10

#### 英文摘要

We present Multimodal Flow, a fully continuous generative model of language and vision. Most unified multimodal models either model both language and quantized images as discrete tokens or combine discrete language prediction with continuous image generation. The former introduces a visual quantization bottleneck. The latter requires modality-dependent objectives and sampling procedures. Fully continuous modeling avoids these trade-offs and enables a shared generative process, but remains underexplored for multimodal pretraining. Multimodal Flow introduces a unified continuous architecture that integrates multimodal continuous representations with a shared chunk-causal flow backbone. It organizes text blocks and images as ordered continuous hyperchunks, preserving textual token order and visual spatial structure. The backbone learns a single vector field over these hyperchunks through Flow Matching. Joint attention enables cross-modal interaction, while modality-specific feed-forward networks process each modality. The model predicts multiple target chunks in parallel during training and generates hyperchunks sequentially at inference. We instantiate MF-1 and pretrain it on multimodal data. Across 0.6B, 1.2B, and 1.6B scales, continued pretraining consistently improves multimodal modeling. With only 150B pretraining tokens, MF-1 achieves an average score of 82.8 across GenEval and DPG-Bench and 75.3 across VQAv2, MMBench, and POPE, remaining competitive with unified models trained on substantially more data. Under matched data, optimization, and parameter budgets, Multimodal Flow further outperforms representative hybrid and discrete models. These results establish continuous chunk-based embedding flow modeling as a new fully continuous paradigm for unified multimodal modeling. The related code and model are publicly released at https://github.com/hustvl/Multimodal-Flow.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1c5695b0-740c-4

---

### 8. Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis

- **ArXiv ID**: [2609.40361v1](https://arxiv.org/abs/2609.40361v1)
- **作者**: Tian Xia, Minghao Liu, Yiqing Liang, Laixi Shi, Jiayun Wang
- **发布时间**: 2026-10-01
- **分类**: cs.LG, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40361v1](https://arxiv.org/pdf/2609.40361v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above 90% accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives and is invariant to class balance. We focus on prompt optimization in MLLMs. Reflective methods such as GEPA use a binary scores matrix with one row per evaluation instance and one column per candidate prompt; cells record per-instance correctness, so the column average is accuracy and drives candidate selection. We introduce pair-level Pareto prompt evolution (Ranking-PE), which replaces each correctness row with a pairwise-ordering row over (positive, negative) instance pairs: the cell is 1 if the candidate scores the positive higher than the paired negative. The column average then equals empirical AUROC (by the Wilcoxon-Mann-Whitney identity). We apply this swap at all three layers the prompt evolution search reads from - the scores matrix that decides Pareto dominance, the per-example feedback to the reflection LM, and final candidate selection - at no extra model calls and with no surrogate loss. Across three diseases on MIMIC, accuracy-based prompt evolution can degrade ranking; Ranking-PE reverses this, beating the accuracy-based recipe by +5.8 AUROC pp on fine-tuned Qwen3-VL-8B and +16.2 pp on MedGemma-4B. Ablations examine each design component and show that a medical-grade visual backbone - via vision-encoder-tuned SFT or medical pretraining - is a prerequisite that prompt search cannot replace - our recipe extends reflective prompt evolution from text-only data to multimodal clinical decision-making.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1c6644a8-beaf-4

---

### 9. Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model

- **ArXiv ID**: [2609.40358v1](https://arxiv.org/abs/2609.40358v1)
- **作者**: Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao...
- **发布时间**: 2026-10-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40358v1](https://arxiv.org/pdf/2609.40358v1)
- **相关度评分**: 10/10

#### 英文摘要

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video generation. Physis-Lang represents physical processes through language that describes their relevant entities, causes, interactions, governing principles, temporal evolution, and effects. To improve this representation, we construct PhysCapBench, which decomposes physical processes into atomic assertions and evaluates captions using recall and precision. An agentic loop iteratively analyzes assertion-level errors and refines the instruction used to produce physical captions. Physis-Lang further converts model deficiencies into textual descriptions and uses language-guided retrieval to identify visually diverse videos that cover missing physical processes. Experiments on four widely used physical video benchmarks with Wan and Cosmos backbones demonstrate consistent improvements in physical plausibility. Notably, starting from open-source Cosmos3-Nano backbones, our Physis-Lang-enhanced models surpass the leading proprietary Veo 3.1 model.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bf62534a-09f8-4

---

### 10. AssemblyWorld: Rethinking 3D Assembly with General-Purpose Agents

- **ArXiv ID**: [2609.40353v1](https://arxiv.org/abs/2609.40353v1)
- **作者**: Jiahao Zhang, Yeying Fan, Moitreya Chatterjee, Suhas Lohit, Bernhard Egger...
- **发布时间**: 2026-10-01
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2609.40353v1](https://arxiv.org/pdf/2609.40353v1)
- **相关度评分**: 10/10

#### 英文摘要

The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual interaction without additional assembly-specific fine-tuning? To investigate this question, we introduce AssemblyWorld, an interactive 3D environment in which agents inspect rendered views and manipulate supplied rigid parts, guided by images or assembly manuals when available. Agents perceive part geometry through 2D views rather than direct access to mesh vertices or faces, while their resulting assemblies are evaluated geometrically. Building on this environment, we construct AssemblyWorldBench, comprising 100 assembly tasks across 80 objects spanning furniture, industrial assembly, and fracture reassembly. Evaluating eight agent systems reveals substantial differences in their capabilities. The strongest system achieves 80.9% part accuracy but 59.4% complete-assembly success. The evaluated open-source systems lag substantially behind their stronger closed-source peers in both execution reliability and assembly accuracy. Analyses of visual references, interaction trajectories, and failures show how agents revise assemblies while leaving residual positioning errors. AssemblyWorld provides a common setting for both assessing the capabilities of interactive assembly agents and characterizing the gap between approximate structure recovery and precise reconstruction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 377eb566-0041-4

---

### 11. Image Classifiers are Efficient Self-Supervised Video Representation Learners

- **ArXiv ID**: [2609.40347v1](https://arxiv.org/abs/2609.40347v1)
- **作者**: Owais Iqbal, Sudipta Sarkar, Shyam Marjit, Omprakash Chakraborty, Anirban Chakraborty...
- **发布时间**: 2026-10-01
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.40347v1](https://arxiv.org/pdf/2609.40347v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. From each super image, we construct two views: one with spatial patch masking and the other with temporal frame masking, ensuring no information leakage across frames. A shared Vision Transformer (ViT) encoder aligns their embeddings using a masked Siamese loss, capturing both motion and appearance cues without reconstruction. Our decoder-free formulation leverages an image foundation model towards efficient video representation learning. Starting from pretrained DINO-v3 and DeiT-v3 image encoders, VideoMSN achieves state-of-the-art performance on Kinetics-400, UCF101, and HMDB51 while requiring up to $32\times$ fewer and $160\times$ fewer video pretraining epochs compared to prior video self-supervised learning methods. Our proposed approach also shows strong performance in low-shot classification, confirming the transferability of the learned representations in a label-scarce scenario. Project Page: https://cvir.github.io/projects/videomsn.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4cfbf235-0287-4

---

### 12. Ego4WAM: What Matters When Scaling Egocentric Human Data for Robot Learning?

- **ArXiv ID**: [2609.40341v1](https://arxiv.org/abs/2609.40341v1)
- **作者**: Zhihao Sun, Liu Liu, Xinjiang Wang, Haoyi Jiang, Wei Feng...
- **发布时间**: 2026-10-01
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40341v1](https://arxiv.org/pdf/2609.40341v1)
- **相关度评分**: 10/10

#### 英文摘要

Egocentric human data provides a scalable source of experience for robot learning, but varies substantially in human-robot alignment, behavioral coverage, and available supervision. Existing work shows favorable scaling with increasing human data, but it remains unclear which data properties drive downstream robot gains and how to use such data throughout the training pipeline. We present a systematic study of egocentric human data with different alignment and supervision under a unified world-action model framework. With the model backbone fixed, we disentangle the effects of human-robot alignment, data duration and task diversity, action supervision, and data usage strategies. We find that aligned human demonstrations substantially improve out-of-distribution generalization and reduce target-task robot data requirements; data duration and task diversity affect downstream capabilities differently; and video-only supervision remains effective without action labels, providing a strong foundation for subsequent video-action training. We validate these findings through closed-loop policy evaluation on both real robots and RoboDojo. Rather than treating data duration as the sole scaling axis, Ego4WAM shows how alignment, task diversity, available supervision, and usage strategy jointly shape the value of egocentric human data for robot learning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 69dc3ec8-ab88-4

---

### 13. I Have a Stream: Making Self-Supervised Learning Work on Continuous Video

- **ArXiv ID**: [2609.40333v1](https://arxiv.org/abs/2609.40333v1)
- **作者**: Ivan Martinović, Lukas Knobel, Yuki M. Asano
- **发布时间**: 2026-10-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40333v1](https://arxiv.org/pdf/2609.40333v1)
- **相关度评分**: 10/10

#### 英文摘要

Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across epochs. We study self-supervised learning from continuous video streams, where frames are consumed in temporal order using strict sliding-window batches, without global reshuffling or multi-epoch replay. To this end, we construct WT++, a 95-hour urban walking-tour video dataset for streaming pretraining. Combined with a comprehensive evaluation suite we find that contrastive and distillation-based methods struggle in this setting, while MAE is more robust but still falls short of standard i.i.d. pretraining. We find that high inter-batch similarity, caused by sliding-window consumption across consecutive batches, does not explain this gap. The main challenge is high intra-batch similarity, where frames within each batch are near-duplicates. To mitigate this, we propose StreamMAE, which preserves the core MAE reconstruction objective while adapting the input pipeline with stream-aware regularization and motion-biased crop selection. StreamMAE outperforms streaming baselines, matches i.i.d. MAE trained on the same video data, remains competitive with ImageNet-pretrained MAE, and scales positively as the pretraining stream grows from 12 to 95 hours.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1a82bb8d-bf88-4

---

### 14. Atomizer-IO: Beyond Pixels, Patches and Grids

- **ArXiv ID**: [2609.40320v1](https://arxiv.org/abs/2609.40320v1)
- **作者**: Hugo Riffaud de Turckheim, Sylvain Lobry, Nicolas Houdré, Damien Robert, Roberto Interdonato...
- **发布时间**: 2026-10-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.40320v1](https://arxiv.org/pdf/2609.40320v1)
- **相关度评分**: 10/10

#### 英文摘要

Most vision architectures assume that observations lie on a regular grid, an effective abstraction for natural images but a restrictive one for sensing data whose channels, temporal sampling, spatial resolution, and geometry can vary. Generic set-based architectures remove the grid, but also remove useful spatial inductive biases. We introduce Atomizer-IO, an architecture that places observations first and derives structure from their physical relationships. Building on top of an atomic representation of the data, each observation is described by its measurement and acquisition metadata, while local cross-attention maps observations to anchor points that can be arbitrarily placed. We evaluate this design by progressively relaxing the grid assumption, from varying input raster configurations and incomplete channel sets to flexible output density and, ultimately, inputs without a raster grid. Atomizer-IO is competitive with flexible EO-specific architectures on most tasks, while offering post-training control over inference cost and competitive compute--performance trade-offs. The same formulation extends without architectural redesign to unordered 3D point clouds, showing that the atomic interface generalizes beyond regular raster inputs. These results suggest that pixels, patches, and grids do not need to define the interface of a sensing architecture.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3b2b7969-c814-4

---

### 15. Looped Diffusion Transformer

- **ArXiv ID**: [2609.40305v1](https://arxiv.org/abs/2609.40305v1)
- **作者**: Yong Xien Chng, Tianyi Chen, Wenwen Tong, Haiwen Diao, Zhongang Cai...
- **发布时间**: 2026-10-01
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.40305v1](https://arxiv.org/pdf/2609.40305v1)
- **相关度评分**: 10/10

#### 英文摘要

Improving text-to-image models has traditionally relied on increasing model size or the number of denoising steps. In this work, we explore an alternative way to scale computation by repeatedly running shared Transformer blocks within each denoising step, effectively increasing computational depth while keeping the parameter count fixed. This looped computation enables iterative refinement of internal representations without explicit reasoning tokens. However, naive looping fails to consistently improve image quality. We trace this problem to weak supervision across intermediate loops and unregulated attention updates that progressively erode local information. To overcome these challenges, we propose Looped Diffusion Transformer (Looped-DiT), which combines deep supervision across intermediate loops with self-modulating attention to stabilize looped feature updates. Under matched-parameter and matched-compute settings, Looped-DiT consistently outperforms non-looped baselines. Notably, a 260M-parameter looped model can surpass a model 6.5x larger across multiple text-to-image benchmarks while requiring 4.9x lower inference compute. Beyond this performance gain, we find that looped computation can offer a more effective form of iterative computation for diffusion models, with increasing loop depth yielding larger gains than adding more denoising steps under a fixed inference budget. Furthermore, deeper loops can progressively correct mistakes made in earlier loops, exhibiting behaviors suggestive of latent reasoning. Together, these results show that looped computation offers a promising way to scale visual generation models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5f34ee85-7976-4

---
