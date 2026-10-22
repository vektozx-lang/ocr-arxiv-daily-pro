# OCR arXiv Daily Pro — 2026-10-22

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-21 09:10 - 2026-10-22 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bdcd0345-cfd0-4

---

## 📄 论文详情

### 1. RealMe: Immersive Volumetric Video from Minimal Captures

- **ArXiv ID**: [2610.30023v1](https://arxiv.org/abs/2610.30023v1)
- **作者**: Chenxu Zhou, Zhiyuan Yu, Yudong Jin, Yinji Shentu, Yu Zhang...
- **发布时间**: 2026-10-22
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.30023v1](https://arxiv.org/pdf/2610.30023v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality volumetric videos, but their reliance on costly capture setups makes them impractical in real-world scenarios. Recent approaches use generative models to relax capture requirements, but still suffer from limited resolution and 4D inconsistency. To overcome these constraints, we propose RealMe, a unified framework built around a high-resolution video diffusion model that enhances limited captures into high-resolution (2K), 4D-consistent videos for volumetric video reconstruction. Specifically, RealMe constructs auxiliary data from capture videos and encodes them into latents along with layout-aware positional embeddings. The video diffusion model adapts factorized spatio-temporal attention to the multi-view capture layout, denoises these latents across viewpoints and time, and decodes them into enhanced videos to refine the 4D representation. This adaptation helps the model capture temporal dynamics and multi-view relationships, leading to more 4D-consistent generation. To reduce the data gap between generated videos and real captures, we apply a latent frequency loss that provides frequency-domain supervision in latent space. Extensive experiments on the public DNA-Rendering benchmark and our self-captured RealVV dataset demonstrate that RealMe is able to create immersive volumetric videos and outperforms state-of-the-art methods in visual fidelity and 4D consistency.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d026d890-e25d-4

---

### 2. What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion

- **ArXiv ID**: [2610.30026v1](https://arxiv.org/abs/2610.30026v1)
- **作者**: Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra
- **发布时间**: 2026-10-22
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.30026v1](https://arxiv.org/pdf/2610.30026v1)
- **相关度评分**: 10/10

#### 英文摘要

Enterprise agents act on documents. Before an agent can follow a policy, answer a compliance question or file a ticket, some ingestion layer must turn a Word file or PDF into tokens - and that layer is where an agent deployed in the wild silently loses information. We show that one layer is lost by every mainstream converter - the meaning an author encodes in how text looks - and that the loss makes agents confidently wrong rather than visibly incomplete. We build a task from 76 real policy documents: recover the requirements the author singled out, scored against the file's own OOXML properties by a deterministic matcher with no LLM judge. Formatting-blind ingestion collapses from micro F1 0.690 to 0.150 (docling) and 0.075 (plain text), a gap that replicates across six answering models from two vendors - five Claude models spanning the Opus, Sonnet and Haiku tiers, and OpenAI's GPT-5.6. An agent that cannot see the cue guesses, and docling's false-positive rate on requirements the author did not flag is four times ours. A span-level leave-one-out localises the loss to two cues - highlight (+0.302) and colour (+0.262), both Holm-adjusted p < 1e-4 - while bold, italic, monospace and strikethrough each sit within +/-0.003 of zero. The same asymmetry appears in PDF. Colour is also the cue no mainstream converter preserves and no parsing benchmark scores, and it is common: 32.8% of 6,460 documents carry a deliberate colour or highlight, 10.3% on an obligation. A pre-registered test shows that typing a cue for the agent adds +0.085 beyond merely preserving it (Holm-adjusted p = 0.049). We validate the labels against rendered page images through an independent modality (kappa = 0.72) and bound what wording alone can achieve (AUC 0.664). For agent builders the practical finding is that ingestion, not reasoning, is where this reliability is won or lost, and that the fix is cheap and measurable.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 101f0403-a182-4

---

### 3. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

- **ArXiv ID**: [2610.30132v1](https://arxiv.org/abs/2610.30132v1)
- **作者**: Zhennan Wan, Jianfei Chen
- **发布时间**: 2026-10-22
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.30132v1](https://arxiv.org/pdf/2610.30132v1)
- **相关度评分**: 10/10

#### 英文摘要

Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 67c0e208-8a2f-4

---

### 4. GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation

- **ArXiv ID**: [2610.30067v1](https://arxiv.org/abs/2610.30067v1)
- **作者**: Quang Anh Kiet Tran, Nam Anh Tran, Manh Hung Trinh, Thanh Danh Le, Khang Nhat Hoang Vo...
- **发布时间**: 2026-10-22
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.30067v1](https://arxiv.org/pdf/2610.30067v1)
- **相关度评分**: 10/10

#### 英文摘要

Vietnamese pre-trained encoders have improved rapidly, but the strongest ones are large, multilingual-vocabulary models or depend on external word segmentation, which makes them costly to deploy. We present GoiBERT, a family of two compact Vietnamese encoders with 26M and 49M parameters that operate directly on raw text. GoiBERT learns from two complementary teachers. A same-tokenizer Vietnamese encoder first teaches general-purpose representations. A much larger teacher then provides task-level guidance through soft labels that are generated without ever labeling its own training data. Across eight benchmarks covering text classification, aspect-based sentiment analysis, natural language inference, and named entity recognition, GoiBERT-large achieves the highest average score among non-teacher models. It does so with fewer than half the parameters of the strongest compact baseline and twice its throughput. GoiBERT-base retains 99% of that baseline's performance at a quarter of its size. Our analysis shows that compression is nearly lossless for sentiment and classification tasks but remains costly for inference and entity recognition, which points to clear directions for future work. Our code and models are available at: https://github.com/Nhantran65/GoiBERT.git

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 009b12aa-99b2-4

---

### 5. Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories

- **ArXiv ID**: [2610.30016v1](https://arxiv.org/abs/2610.30016v1)
- **作者**: Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao, Martin Klitte, Diarmuid Corcoran
- **发布时间**: 2026-10-22
- **分类**: cs.SE, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.30016v1](https://arxiv.org/pdf/2610.30016v1)
- **相关度评分**: 10/10

#### 英文摘要

Understanding large, complex, and rapidly evolving code bases remains a core challenge for software engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis. Providing this information to a Large-Language Model (LLM) is another hurdle, as the LLM must understand not only the required code method but also its associated methods in the grand scheme of the repository. We propose Code Comprehensor, a hybrid retrieval-reasoning framework combining (i) a code dependency callgraph, (ii) CodeScribe, which uses code-aware LLMs to generate hierarchical documentation across repository call graphs, and (iii) CodeContrast, a CLIP-style dual-encoder model trained on CodeScribe output to learn aligned text-code embeddings. CodeContrast enables fast, semantically precise retrieval of relevant code-context neighborhoods, which serve as grounded evidence for an MCP-based LLM orchestrator answering domain-specific queries. Evaluation on OpenCV and a proprietary 5M-LOC repository shows that CodeScribe-derived supervision significantly improves cross-modal retrieval in text-to-code accuracy over baseline approaches. Richer textual supervision (hierarchical documentation, parent/sibling context, and LLM-generated synthetic questions) consistently enhances performance across both repositories. LLM-as-a-judge evaluation using the popular RAGAS of the Code Comprehensor output yields above 90% faithfulness scores.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0e11f64c-abb1-4

---

### 6. Towards English - Mizo Legal Machine Translation: Corpus Creation, Analysis, and Benchmarks

- **ArXiv ID**: [2610.29943v1](https://arxiv.org/abs/2610.29943v1)
- **作者**: Telem Joyson Singh, Sanabam Boyshana, Sanasam Ranbir Singh, Priyankoo Sarmah
- **发布时间**: 2026-10-22
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.29943v1](https://arxiv.org/pdf/2610.29943v1)
- **相关度评分**: 10/10

#### 英文摘要

Indian court proceedings are held in English, so speakers of languages with limited translation technology have limited access to them. We present the first English Mizo parallel dataset of Indian court judgments. It contains 13,168 sentence pairs from the Gauhati High Court and the Supreme Court of India. Professional native Mizo translators translated complete documents; sentence pairs were manually aligned, and two independent reviewers checked the results. Our study finds that English words are borrowed in a very selective way: official and legal terms are almost always kept in English, but words for everyday things like actions, situations, and results are usually expressed in native Mizo. Mizo diacritics are also used inconsistently across the corpus. When we fine tune the NLLB 200 1.3B model on our training data, it scores 27.47 BLEU on a balanced legal test set of 1,000 sentence pairs, an improvement of 7.16 BLEU over the base model. However, it still uses English words about three times more often than a human translator does.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 14f6596e-133f-4

---

### 7. Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation

- **ArXiv ID**: [2610.29933v1](https://arxiv.org/abs/2610.29933v1)
- **作者**: Yufeng Li, Zaijing Li, Fuchen Zhang, Zongzong Wu, Ming Zhao...
- **发布时间**: 2026-10-22
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.29933v1](https://arxiv.org/pdf/2610.29933v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation (RAG) frequently integrates knowledge graphs (KGs) for complex multi-hop question answering. However, their performance is increasingly bottlenecked by the knowledge structuring and reasoning processes. (i) Severe semantic loss: Distilling continuous texts into discrete symbols strips away contextual nuances and narrative coherence. (ii) Pronounced modality mismatch: Fragmented graph structures clash with the continuous texts LLMs are pre-trained on, while rewriting them into natural language introduces generative noise and omits information. To address these limitations, we propose ThreadRAG, a semantic-topology-based RAG framework for context-preserving knowledge structuring and modality-native evidence reasoning. ThreadRAG introduces a Semantic Topology Mapper (STM), which organizes retrieved documents into context-intact Semantic Nodes and constructs a Semantic Topology Graph (STG) through narrative, semantic, and lexical edges. It further incorporates Energy-Driven Pathfinding (EDP), which identifies query-relevant subgraphs via energy diffusion and deterministically linearizes them into coherent textual evidence paths. Experiments on three multi-hop QA benchmarks demonstrate that ThreadRAG consistently outperforms strong baselines. Notably, it achieves a 14.4% EM improvement over text-centric methods on HotpotQA and surpasses the best baseline by 5.8% EM on 2WikiMultihop, while reducing token cost to 23.3% of the strongest baseline.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 13363a4d-84c5-4

---

### 8. Automated Materials Data and Knowledge Extraction using Machine Learning and Large Language Models

- **ArXiv ID**: [2610.29895v1](https://arxiv.org/abs/2610.29895v1)
- **作者**: Aravindan Kamatchi Sundaram, B. Pabitramohan Prusty, Rohit Batra
- **发布时间**: 2026-10-21
- **分类**: cond-mat.mtrl-sci, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.29895v1](https://arxiv.org/pdf/2610.29895v1)
- **相关度评分**: 10/10

#### 英文摘要

Over the past decade, substantial efforts have been devoted to developing machine learning (ML) methods for extracting materials data and, where possible, materials knowledge directly from the scientific literature. This review traces the evolution of these methods from heuristic, rule-based pipelines through natural language processing (NLP) models and transformer-based encoders to, lastly, large language models (LLMs) and agentic systems capable of extracting materials information across multiple modalities, including text, tables, and figures. Beside construction of large, queryable materials databases and knowledge graphs that support downstream materials discovery, we discuss how these advances have enabled new capabilities, such as, generic question answering across materials science, AI co-scientists and chatbots for research assistance, and closed-loop optimization and discovery when integrated with autonomous laboratories. We critically assess the datasets generated using these approaches, their extraction accuracy and computational costs, and the respective strengths and limitations of different methodologies, and even provide practical guidelines for developing more reliable and scalable materials data extraction pipelines. Finally, we identify key open challenges, including the extraction of full materials structure-property-processing-performance tetrahedron at the sample level, the scarcity of reliable benchmark datasets for systematic evaluation, and the resolution of non-standard materials terminology across different document modalities.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3bdb6dc1-a8b6-4

---

### 9. UniRAP: Towards Unified Part-level Physical Affordance Reasoning and Actionable Perception

- **ArXiv ID**: [2610.29768v1](https://arxiv.org/abs/2610.29768v1)
- **作者**: Linfei Li, Ruining Hu, Lin Zhang, Zhong Wang, Fengyi Zhang...
- **发布时间**: 2026-10-21
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.29768v1](https://arxiv.org/pdf/2610.29768v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language perception has achieved impressive progress in aligning natural language with visual observations, yet grounding high-level semantics into part-level physical interaction remains challenging. To address this gap, we propose UniRAP, a unified model for inferring part-level physical affordances and mapping language instructions to actionable geometric representations. UniRAP formulates this problem as a conditional multimodal generation task, integrating visual inputs, textual instructions, and optional prompts into a shared spatiotemporal representation space through a unified interface token mechanism. To predict executable contact geometry, we introduce a Unified Affordance Decoder (UAD), which jointly performs object detection, part-level affordance segmentation, and 4-DoF interaction pose estimation by leveraging intermediate segmentation features. In addition, we propose a curriculum-based transfer training strategy that progressively adapts the model from general visual parsing to interaction-aware perception, improving data efficiency under limited textual annotations. Experiments show that UniRAP achieves state-of-the-art performance on referring expression segmentation, affordance grounding, and interaction pose estimation, while maintaining strong spatiotemporal consistency in dynamic video scenarios. These results demonstrate the effectiveness of UniRAP as a unified perception framework for language-guided physical manipulation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d2399a71-7f24-4

---

### 10. Retrieval Augmented Generation Compositionality

- **ArXiv ID**: [2610.29722v1](https://arxiv.org/abs/2610.29722v1)
- **作者**: Ido Levy, Segev Shlomov, Leshem Choshen
- **发布时间**: 2026-10-21
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.29722v1](https://arxiv.org/pdf/2610.29722v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a time. It remains unclear whether their isolated gains survive composition, whether retrieval quality and answer faithfulness favor the same design choices, and whether conclusions from small corpora hold at large scale. We pre-declare three hypotheses and introduce LASAGNA, an open-source framework for controlled RAG evaluation. We test 450 configurations across eight benchmarks and corpora ranging from 5K to 200K documents. Three findings emerge. First, individually strong techniques from different phases of a RAG pipeline do not necessarily compose: three retrieval techniques predict a +47% combined improvement but deliver only +17% when used together. Second, component gains stack differently for retrieval and faithfulness, and optimizing one can hurt the other. Third, the best composition changes as the corpus grows: the combination that wins on a small corpus may not remain best at large scale. These findings show that gains measured in isolation are not reliable predictors of realistic performance, and that new RAG techniques should be tested with the full surrounding stack. We call on researchers to do so and supply LASAGNA to simplify these experiments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ad829a3f-01d4-4

---

### 11. Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement

- **ArXiv ID**: [2610.29669v1](https://arxiv.org/abs/2610.29669v1)
- **作者**: Kardelen Subasi, Jarosław A. Chudziak
- **发布时间**: 2026-10-21
- **分类**: cs.DB, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.29669v1](https://arxiv.org/pdf/2610.29669v1)
- **相关度评分**: 10/10

#### 英文摘要

LLM-generated records increasingly populate production information systems where they are treated as data assets subject to the same quality expectations as records from operational databases. A single such record can simultaneously satisfy and violate a quality rule: a grounded fact adjacent to a hallucination, a useful answer adjacent to a stereotype. Classical data cleaning cannot resolve this because the two judgments are incompatible over the same span; a single LLM judge cannot either, since it shares the training biases that produced the conflict. Existing interventions such as prompt engineering, chain-of-thought, and RLHF reduce surface error rates but provide no audit trail and cannot distinguish genuine remediation from blanket suppression. The question is whether a deterministic check over structured inter-agent records can catch the defects that referential checks alone miss. We present BiasGuard-D: two adversarial roles drawn from distinct model families exchange typed claim documents, a three-model quorum adjudicates by majority vote, and a combined referential-plus-semantic invariant validates the verdict. The semantic component fires on verdicts referential checks miss; removing the iterative loop drops invariant satisfaction sharply. The deliberation layer transfers from stereotype to hallucination remediation on HaluEval QA with only role-framing changes, raising right-answer recovery by 49 percentage points; the triage gate required a cross-family second auditor to maintain recall on objective hallucination. Every claim, vote, and instruction is stored as a typed record giving operators a provenance trail auditable under emerging AI regulations.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 44772f29-3a21-4

---

### 12. Spatially Gated Demographic Steering for Debiasing Multi-Person Text-to-Image Generation

- **ArXiv ID**: [2610.29651v1](https://arxiv.org/abs/2610.29651v1)
- **作者**: Venkatesh Thirugnana Sambandham, Torsten Schon
- **发布时间**: 2026-10-21
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.29651v1](https://arxiv.org/pdf/2610.29651v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-to-Image models reproduce societal stereotypes, and existing mitigation applies one demographic correction to the whole scene. In multi-person scene generation this creates a trade-off: global steering improves aggregate balance only by homogenizing the people within an image. Steering-based methods like Embedding Arithmetic drive the intra-image diversity below the unsteered baseline. Text- and latent-projection approaches shift the aggregate skew with only marginal gains in intra-image diversity. We present Spatially Gated Steering (SGS), which steers the demographics of each person independently by extracting per-person masks from the Diffusion Transformer's (DiT) internal attention maps at a critical denoising timestep and applying a distinct demographic vector within each mask for the remaining steps. SGS needs no fine-tuning, inversion or layout specifications, and uses a lightweight segmentor over frozen DiT attention features to localize subjects at early timesteps. On skewed occupational prompts, SGS reaches high intra-image racial and gender diversity while keeping aggregate balance competitive and image quality near baseline, a result we validate on two architecturally distinct diffusion transformers, FLUX.1-Dev and SD3.5-Large. Codebase and model weights are available at https://github.com/cvims/spatially-gated-steering

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 107931a9-4698-4

---

### 13. Rethinking Video Autoencoders for Interactive World Models

- **ArXiv ID**: [2610.30129v1](https://arxiv.org/abs/2610.30129v1)
- **作者**: Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour, Patrick Pérez, David Picard
- **发布时间**: 2026-10-22
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.30129v1](https://arxiv.org/pdf/2610.30129v1)
- **相关度评分**: 10/10

#### 英文摘要

Video world models predict future frames from past frames and actions. They serve as simulators in which agents train, plan or are evaluated, and that humans can control interactively. They generate in the latent space of a video autoencoder, whose compression sets their cost per frame and how long each action waits to take effect. Yet world models often reuse the autoencoders of text-to-video generators, built for offline generation with no agent waiting and, without their training data and code, not retrainable at another compression. We therefore ask how, where and how much a world model should compress. We build CADRE, an open family of causal diffusion representation autoencoders spanning multiple spatio-temporal compressions. Its members differ only in a small bottleneck on frozen features and share a diffusion decoder self-distilled to one or a few steps. We train the same world model on each autoencoder in two domains, manipulation and navigation, with two environments each. CADRE forms most of the latency-quality frontier, especially with a moving camera. Our study also leads to four findings. At strong compression, a diffusion decoder is sharper than perceptual regression. In robot manipulation, temporal compression is more effective in the autoencoder than in the world model. Manipulation and navigation call for opposite compressions: temporal compression costs little when the camera is still, and spatial compression when it moves. Surprisingly, with a still camera, coarser spatial tokens hurt motion far more than image quality. Code, models and a live demo are at https://kyutai.org/blog/2026-10-21-cadre

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e33900e9-9f09-4

---

### 14. VoxProg: 3D Spatial Reasoning through Voxel Programming

- **ArXiv ID**: [2610.30127v1](https://arxiv.org/abs/2610.30127v1)
- **作者**: Zhichao Zhai, Menglei Zhao, Guikun Chen, Zihao Yan, Kanzhi Wu...
- **发布时间**: 2026-10-22
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.30127v1](https://arxiv.org/pdf/2610.30127v1)
- **相关度评分**: 10/10

#### 英文摘要

Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geometric references that language leaves implicit. In this work, we introduce VoxProg, which formulates 3D object placement through voxel programming: a language model translates task interpretations into executable programs over local voxel views of scene surfaces. Because these views index surface geometry on regular grids with explicit coordinates and neighborhood relations, an evidence program can isolate task-relevant regions and boundaries directly from scene meshes, and a downstream pose program can measure the resulting geometry to compute a target $SE(3)$ pose. Visual and numerical feedback from execution lets the model inspect intermediate selections and candidate placements to iteratively revise its code. To evaluate open-ended placement across functional use, geometric fit, and contextual arrangements, we introduce the 71-task VoxProg-Bench benchmark along with an evaluation suite pairing perceptual Intent Alignment and 3D Physical Validity. Across VoxProg-Bench and external benchmarks, VoxProg consistently outperforms relation-based, keypoint-based, and mesh-based baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: af1d5dc1-efe4-4

---

### 15. PhysiCalWorld: In-Context Physics Calibration for World Models

- **ArXiv ID**: [2610.30125v1](https://arxiv.org/abs/2610.30125v1)
- **作者**: Yunhao Luo, Wentao He, Yinpei Dai, Hyelin Nam, Hongze Fu...
- **发布时间**: 2026-10-22
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.30125v1](https://arxiv.org/pdf/2610.30125v1)
- **相关度评分**: 10/10

#### 英文摘要

Existing world models typically perceive a scene through current visual frame or a narrow history window. However, these observations may not reveal the physics properties that determine transition dynamics, such as an object's mass distribution, joint damping, or surface friction. Without calibrating these physics factors for world models, predictions tend to regress toward an empirical prior and induce severe drift in novel test scenes. To this end, we propose PhysiCalWorld, which calibrates action-conditioned world models to the instance-specific dynamics via in-context prompting, without fine-tuning or analytical physics modeling. Our method encodes an exploratory interaction clip collected within the test scene into a compact physics descriptor token, which grounds subsequent predictions in the scene's actual physical behavior. PhysiCalWorld is trained end-to-end with the latent prediction loss alone, without physics labels. At inference time, the descriptor token is extracted once and can be reused across rollouts with negligible compute overhead. We evaluate PhysiCalWorld across four environments covering diverse physics variations and show that it substantially improves rollout prediction accuracy and visual planning success rate. The learned descriptors also form a physically structured latent space and generalize beyond the physics ranges seen during training.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 48819cfb-3071-4

---
