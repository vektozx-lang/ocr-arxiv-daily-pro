# OCR arXiv Daily Pro — 2026-09-04

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-03 09:10 - 2026-09-04 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. How Far Can Synthetic Data Take Thai OCR?

- **ArXiv ID**: [2609.03595v1](https://arxiv.org/abs/2609.03595v1)
- **作者**: Kunat Pipatanakul
- **发布时间**: 2026-09-03
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.03595v1](https://arxiv.org/pdf/2609.03595v1)
- **相关度评分**: 10/10

#### 英文摘要

We investigate what makes synthetic OCR supervision transfer to real Thai documents and use the resulting insights to build Wayu-Paxa-OCR-Zero, a Thai OCR model adapted without OCR labels from real Thai document pages. Synthetic data provide exact labels at scale, but "realism" conflates source domain, page context, typography, spatial structure, and glyph variation. We disentangle these factors with a controlled document-reconstruction pipeline and evaluate each variant under page- and crop-level training on printed and handwritten Thai documents. Non-text context has little consistent effect, whereas typeface diversity, two-dimensional structure, and real handwriting glyphs improve transfer; moreover, source-domain matching depends on training granularity, with in-domain reconstruction approaching real printed supervision under page-level training (1.82% versus 1.31% median character error rate) but underperforming out-of-domain reconstruction under crop-level training (15.59% versus 5.52%). Guided by these findings, we adapt the 0.9B-parameter PaddleOCR-VL-1.6 into Wayu-Paxa-OCR-Zero using 45,723 synthetic pages: relative to its base checkpoint, it reduces median character error rate from 6.64% to 1.24% on printed pages and from 74.87% to 20.55% on handwriting and outperforms Typhoon OCR v1 7B on all five evaluation sets, showing that synthetic-only training can be competitive.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. KhatianDoc: A Human-Verified Benchmark Diagnosing Multimodal LLM Failure on Bengali Legal Land Records

- **ArXiv ID**: [2609.03597v1](https://arxiv.org/abs/2609.03597v1)
- **作者**: Tasmiad Hasan, Arafat Zaman Ratul, Sarker Sadman Saalim, S. M. Shah Nawaz Hossain, Khan Raiyan Ibne Reza...
- **发布时间**: 2026-09-03
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.03597v1](https://arxiv.org/pdf/2609.03597v1)
- **相关度评分**: 10/10

#### 英文摘要

Land ownership in Bangladesh is recorded in Ana-Ganda-Kora-Kranti-Til, a base-16 positional fraction system with dedicated Unicode glyphs, no mainstream font, and no coverage in any OCR pipeline or tokenizer. The handwritten records that carry these fractions, RS Khatians, are the authoritative title record for millions of parcels and a frequent subject of civil litigation, yet no benchmark has asked whether a machine can read one. We introduce KhatianDoc, a four-task benchmark built from 107 real RS Khatian records from the Vumi (land) Office of Munshiganj, Bangladesh: symbol recognition, base-16-to-decimal conversion, structured field extraction, and legal document question answering over 1,634 QA pairs. Ground truth was transcribed by hand, verified by a land-law practitioner to full agreement, and anonymized through positional tokens that keep the referential distinctions multi-hop questions depend on. We evaluate six multimodal LLMs (8B to 72B+, open and closed) under a fixed zero-shot protocol. Five QA categories, 39.3% of our stratified set, return zero correct answers from every model; on the arithmetic task, every model that emits a number does worse than a constant-mean baseline, with exact- and near-match scores coinciding: decorrelation, not approximation. Auditing our own metrics surfaced two artifacts in opposite directions: we correct a refusal-scoring bug and report the fixed scores beside the originals, and flag an inflated metadata metric as an upper bound. KhatianDoc documents not a performance gap but the absence of a capability, with verified ground truth for future systems. Code and data, with a redacted image release, are publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. OCR-EDR: Rendering-Aware Diagnosis and Repair for Closed-Loop OCR Improvement

- **ArXiv ID**: [2609.03445v1](https://arxiv.org/abs/2609.03445v1)
- **作者**: Linnan Zhao, Kang Liu, Hao Yu, Jiabo Zhan, Chong Sun...
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.03445v1](https://arxiv.org/pdf/2609.03445v1)
- **相关度评分**: 10/10

#### 英文摘要

Although document OCR systems perform increasingly well on routine documents, complex formulas, structured text, and long-tail formats remain error-prone. OCR predictions may omit fine-grained content or hallucinate unsupported outputs, while equivalent encodings of the same visible content must be accommodated. Existing OCR evaluation methods mostly report aggregate metrics, offering limited support for analyzing case-level errors and improving OCR performance. We propose OCR-EDR (OCR Error Diagnosis and Repair), a rendering-aware framework that advances from fine-grained diagnosis to iterative repair. Given a source image, an editable OCR prediction, and its rendered image, OCR-EDR first jointly assesses whether the prediction and its rendering are consistent with the source, preserving valid predictions, including rendering-equivalent ones, while diagnosing and localizing genuine errors. It then applies executable edits and may request an updated rendering for iterative reassessment. We construct OCRErrBench from diverse real OCR predictions, covering text and formulas, exact and rendering-equivalent positives, and genuine errors, and develop the DocEDR model to execute the diagnosis--repair loop. On OCRErrBench, DocEDR achieves 94.78% diagnostic accuracy. It repairs 86.23% of erroneous inputs to visual consistency, raises formula Case-F1 by 30.99 percentage points over DOCR-Inspector-7B on DOCRcaseBench, and improves formula CDM by up to 4.62 percentage points on the identified Bad subsets of four OCR systems on UniMER-Test. These results show that OCR-EDR turns fine-grained OCR analysis into verified corrections and performance gains.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation

- **ArXiv ID**: [2609.04031v1](https://arxiv.org/abs/2609.04031v1)
- **作者**: Shuaiting Li, Zelin Gao, Haibin Shen, Yujun Shen, Haotong Qin...
- **发布时间**: 2026-09-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.04031v1](https://arxiv.org/pdf/2609.04031v1)
- **相关度评分**: 10/10

#### 英文摘要

Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment. Quantization-aware training (QAT) is an effective solution for compressing and accelerating advanced generative models without runtime overhead at inference. However, existing QAT methods suffer from a distinctive challenge in VDMs: while they often preserve prompt semantics, global layout, and coarse motion, the quantized model severely degrades visual details, texture fidelity, and sharpness. In this paper, we trace this degradation to the timestep-agnostic design of conventional quantization pipelines, which overlooks the stage-wise functionality of video denoising. In VDMs, early denoising steps mainly establish global structure and motion, whereas middle and late steps refine local appearance and high-frequency details. Based on this insight, we propose DSAQuant, a Denoising-Stage-Aligned Quantization-aware training framework for VDMs. During training, Denoising-Stage Oriented Supervision preserves teacher distillation in early steps for stable structure planning, while shifting later steps toward target-driven optimization to enhance detail reconstruction. During inference, Denoising-Stage Gated Guidance disables CFG in the final denoising steps to prevent it from amplifying quantization-induced errors into high-frequency artifacts. Extensive experiments on the Wan and CogVideoX families under W4A4 and W3A3 settings show that DSAQuant consistently outperforms the SOTA QAT baseline, improving the VBench average score by up to 6.60 under aggressive W3A3 quantization while preserving strong text-video alignment. These results demonstrate that effective VDM quantization requires not only reducing quantization error, but also aligning quantization training and inference with the stage-wise nature of video diffusion.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views

- **ArXiv ID**: [2609.04180v1](https://arxiv.org/abs/2609.04180v1)
- **作者**: Joseph Lee, Yidi Huang, Dokyoon Kim, Shu Yang, Li Shen
- **发布时间**: 2026-09-04
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.04180v1](https://arxiv.org/pdf/2609.04180v1)
- **相关度评分**: 10/10

#### 英文摘要

Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the token budget fixed, allocating tokens from document repetition to auxiliary views improves learning, counterintuitively, even for factual recall. Third, the effectiveness of auxiliary views is not contingent on the strength of the teacher model that generates them. Fourth, we identify forms of knowledge, contextual and foundational, that aid learning in the presence of prior knowledge gaps. Finally, we examine how these effects manifest mechanistically via layer-wise biases and compression. Together, our findings suggest that auxiliary representations of knowledge, which arise naturally in large pre-training corpora, are a key factor in the success of pre-training and offer a plausible explanation for why data diversity matters.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Efficient Test-Time Adaptation through Human-AI Interaction

- **ArXiv ID**: [2609.04141v1](https://arxiv.org/abs/2609.04141v1)
- **作者**: Zora Zhiruo Wang, Apurva Gandhi, Rulin Shao, Aspen Chen, Jonas Mueller...
- **发布时间**: 2026-09-04
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.04141v1](https://arxiv.org/pdf/2609.04141v1)
- **相关度评分**: 10/10

#### 英文摘要

AI agents are trained on population-scale data to encode broad capabilities spanning those of many practitioners. Yet the artifacts they produce rarely meet the personal bar professionals need to stake their reputation on. On realistic, open-ended tasks where success criteria are heterogeneous and insufficiently documented, individual expertise lives precisely in the elevation and departure from the average. In practice, iterative human-agent interaction surfaces criteria that users cannot fully specify up front, yet apply repeatedly across tasks. We argue this cross-session interaction data is a rich, underused signal for closing the gap to individual expertise. In this work, we propose test-time adaptation through human-agent interaction (TAHI), which integrates these signals into agent context and weights, and crystallizes each user's training and evaluation criteria via an evolving rubric module. We adapt agents to 30 individuals in two high-utility domains, writing and visual creation, on a total of 600 tasks. Our agents improve solo task success by 4.5-20.9% within only tens of tasks. Meanwhile, our evolving rubric module serves as a scalable annotation tool, creating evaluation rubrics that catch 16.0-22.3% more failures than those from LMs or humans alone. While agents are adapted towards individuals, we show these personalized agents also produce improvements in success of up to 8.8% that generalize across users.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Editable Visual Design

- **ArXiv ID**: [2609.04034v1](https://arxiv.org/abs/2609.04034v1)
- **作者**: Junyan Ye, Wei Liu, Dongzhi Jiang, Zichen Wen, HaoDong Li...
- **发布时间**: 2026-09-04
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.04034v1](https://arxiv.org/pdf/2609.04034v1)
- **相关度评分**: 10/10

#### 英文摘要

While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets. To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain'' for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator'' to synthesize standalone visual assets. Operating under an ``imagine first, then act'' closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback. Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations

- **ArXiv ID**: [2609.04030v1](https://arxiv.org/abs/2609.04030v1)
- **作者**: Chen Li, Dimitrios Chrysostomou
- **发布时间**: 2026-09-04
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.04030v1](https://arxiv.org/pdf/2609.04030v1)
- **相关度评分**: 10/10

#### 英文摘要

IRWOZ has improved industrial human-robot interaction (HRI) dialogue systems through domain-specific annotations. However, its initial version contains substantial noise in dialogue states and utterances, limiting state-tracking accuracy. We introduce IRWOZ 2.0, which addresses these limitations through large language model (LLM) enhanced generation (Mistral/Claude-3.5) and quality refinements. Our improved dataset expands to 390 dialogues across 4 industrial domains (Assembly, Delivery, Position, Relocation), featuring manual corrections and automated typo removal. Benchmark experiments on dialogue state tracking demonstrate significant improvements, with GPT-2's BLEU-4 score increasing from 0.1651 to 0.5604 compared to original IRWOZ. To support industrial HRI research, we publicly released IRWOZ 2.0 dataset at https://ieee-dataport.org/documents/irwoz-20-large-language-model-driven-dialogue-dataset-industrial-robot-conversations

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. IchthyoNoma: Nomenclature and Context Sensitivity of Zero-Shot Biological Vision--Language Models for Bangladeshi Freshwater Fish Recognition

- **ArXiv ID**: [2609.03985v1](https://arxiv.org/abs/2609.03985v1)
- **作者**: Nazim-E-Alam, Tarek Rahman, Md Kishor Morol
- **发布时间**: 2026-09-03
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.03985v1](https://arxiv.org/pdf/2609.03985v1)
- **相关度评分**: 10/10

#### 英文摘要

Zero-shot vision-language models (VLMs) are increasingly used as training-free species recognizers, but reported accuracy can reflect more than visual species knowledge. We audit CLIP, BioCLIP, BioCLIP2, and a multilingual Jina CLIP v2 control on seven freshwater-fish categories from two Bangladeshi sources (10,321 images). BioCLIP2 reaches 72.36% on BFF-15 with English common names and 68.91% on SylFishBD with scientific names, versus 25.15% and 14.40% for generic CLIP. BioCLIP2 Bengali prompts are near chance in balanced accuracy (14.22-14.29%); Jina partially recovers Bengali discrimination to 21.89% and 16.36%, but bare Bengali names return to 14.29% on both sources. Paired SylFishBD interventions show no significant weak-blur effect, modest losses from stronger blur/gray masking, a larger white-mask artifact, and strong species dependence. Zero-shot biological VLM scores therefore jointly reflect biological specialization, multilingual alignment, nomenclature, prompt formulation, and context.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. FiMI Banking: A Sovereign Model for Indian Retail Banking

- **ArXiv ID**: [2609.03960v1](https://arxiv.org/abs/2609.03960v1)
- **作者**: NPCI AI Research Team, Aman Kumar, Asit Desai, Chandra Bhushan, Harsh Sharma...
- **发布时间**: 2026-09-03
- **分类**: cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.03960v1](https://arxiv.org/pdf/2609.03960v1)
- **相关度评分**: 10/10

#### 英文摘要

Banks need conversational systems that can answer product questions, assist customers with account-related requests, and operate safely within strict operational and regulatory constraints. General-purpose language models do not reliably meet these requirements. They fall short when a task requires grounded information, correct tool use, or cautious handling of bank-specific sensitive situations. We introduce FiMI Banking, a controlled Indian retail-banking setting. We build it from vetted banking documents, structured ground truth, synthetic customer backgrounds, and banking tools. We evaluate two post-training approaches: preference optimization for response-level behavior, and reinforcement learning with verifiable rewards for multi-turn tool-use tasks. Preference optimization improves safe behavior substantially: out-of-scope refusal rises from 52% to 80%. Reinforcement learning improves edge-case performance from 0.509 to 0.718 and order-sensitive task performance from 0.590 to 0.679, while using 29% fewer generated tokens. These results show that preference optimization and verifiable-reward reinforcement learning address complementary requirements for reliable banking agents.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs

- **ArXiv ID**: [2609.03892v1](https://arxiv.org/abs/2609.03892v1)
- **作者**: Junqing Du, Fernando Ropero, Erkin Turkoz, Yanfeng Zhang, Lu Liu
- **发布时间**: 2026-09-03
- **分类**: cs.CV, cs.AI, cs.RO
- **PDF**: [https://arxiv.org/pdf/2609.03892v1](https://arxiv.org/pdf/2609.03892v1)
- **相关度评分**: 10/10

#### 英文摘要

3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to costly supervision and a specific backbone. We instead introduce GraFT, a training-free framework that supplies the missing 3D structure through a compact, easily maintained 3D scene graph (3DSG). From this 3DSG, GraFT provides three spatial reasoning capabilities: (1) deterministic geometry through symbolic tools, (2) allocentric layout through a bird's-eye-view (BEV) rendering, and (3) visual-attribute grounding through task-relevant egocentric frames. On ScanQA, GraFT improves every metric over the same-backbone baseline, raising CIDEr by 27%. On VSI-Bench, GraFT improves frozen MLLMs by up to 65%, surpassing every proprietary and general-purpose open-source baseline, and several prominent fine-tuned spatial models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation

- **ArXiv ID**: [2609.03874v1](https://arxiv.org/abs/2609.03874v1)
- **作者**: Vineet Kumar, Meghanadh Pulivarthi, vishwajeet kumar, Jaydeep Sen, Riyaz Ahmad Bhat...
- **发布时间**: 2026-09-03
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.03874v1](https://arxiv.org/pdf/2609.03874v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost in the middle" problem. Thus, precise and accurate retrieval is important. Current retrievers chunk long context into length-based manageable chunks - in the process throwing away rich and informative semantic global structure in the corpus. We introduce a novel retrieval system STAIR that empowers an LLM to exploit global structure in a corpus such as a Table of Contents (ToC) to efficiently store and retrieve information from its model parameters. Our thorough and careful ablation studies with a finetuned Differentiable Search Index (DSI) system show that ToC helps build a low hallucination (less than 0.05%) generative Information Retrieval (IR) system and can generalize to examples where very few training samples are available. To further research in this novel direction of ToC based retrieval we release SearchTome - a diverse benchmark created from 18 books across 6 diverse domains to further research in this novel direction. STAIR achieves a high Recall@1 score of 82.6% on SearchTome as compared to DSI (76.9%), where the difference is found to be statistically significant. STAIR easily beats other strong baselines such as BM25 (59.5%), DPR (68.7%) and out-of-the-box Mistral (13.8%).

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Semantic Bayesian World Models

- **ArXiv ID**: [2609.03834v1](https://arxiv.org/abs/2609.03834v1)
- **作者**: Tommaso Soru
- **发布时间**: 2026-09-03
- **分类**: cs.AI, cs.DB, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.03834v1](https://arxiv.org/pdf/2609.03834v1)
- **相关度评分**: 10/10

#### 英文摘要

Knowledge graphs describe reality in crisp assertions, while the systems now consuming them, foundation models and autonomous agents, reason natively in probabilities. We argue that this mismatch is why the integration of language models and knowledge graphs remains a data-feeding pipeline rather than a unified reasoning architecture. We envision Semantic Bayesian World Models (SBWMs): a Web that describes the world not as a database of facts but as a shared, evolving fabric of beliefs over knowledge graphs, where ontological axioms constrain priors, observations update beliefs by Bayesian conditioning, and actions intervene upon the world. We work through what an agent gains from such a model: a home-security agent deciding whether the figure at the gate is a courier or a burglar, an actuarial estimate aggregated by entailment rather than by string frequency, a planning task that language models reliably fail, and the estimation of quantities that no document has ever stated. We then set out what the community must build to make them possible: belief annotation over RDF~1.2, probabilistic entailment regimes, semantic calibration layers, and protocols by which agents that have never met can exchange, and disagree over, calibrated beliefs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. Urban Boundaries, Social Barriers: A Benchmark and Vision-Centric Framework for Mapping Gated Communities and Equity Implications

- **ArXiv ID**: [2609.03804v1](https://arxiv.org/abs/2609.03804v1)
- **作者**: Minwei Zhao, Weiming Zhang, Jiawang Du, Qiming Liu, Weiming Zhuang...
- **发布时间**: 2026-09-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.03804v1](https://arxiv.org/pdf/2609.03804v1)
- **相关度评分**: 10/10

#### 英文摘要

Communities are fundamental spatial units that shape urban form and social life. Whether a residential compound is spatially open or enclosed affects mobility, access to public services, and equity, yet studies of Chinese fengbi xiaoqu remain largely qualitative or small-scale, limiting reproducible city-scale analysis. We address this gap by introducing GBA-GCs, a metropolitan-scale multimodal benchmark for locally grounded gated/open community recognition in China's Greater Bay Area, covering 37,444 residential compounds with aligned boundary polygons, high-resolution satellite imagery, Chinese metadata, and structured attributes, together with expert-verified labels, inter-annotator reliability, and official evaluation splits. Built on this benchmark, we present Multimodal Classifier for Gated Community (MCGC), a vision-centric multimodal framework based on DINOv3-SAT that fuses imagery, text, and structured cues via modality-aware cross-attention and adaptive gating to mitigate modality imbalance. MCGC consistently outperforms strong unimodal and multimodal baselines. Finally, we apply the validated model to metropolitan-scale mapping and report equity-oriented findings including spatial clustering of GCs, privatized green space, and reduced pedestrian connectivity. The benchmark, code, and release documentation are available at https://github.com/MinweiZhao/GBA-GCs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval

- **ArXiv ID**: [2609.03788v1](https://arxiv.org/abs/2609.03788v1)
- **作者**: Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono
- **发布时间**: 2026-09-03
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.03788v1](https://arxiv.org/pdf/2609.03788v1)
- **相关度评分**: 10/10

#### 英文摘要

Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions with a multilingual sentence encoder: a reverse sign language dictionary that needs no gloss supervision and admits an open vocabulary. On 1,300 sign-level segments from a Japanese Sign Language (JSL) dialogue corpus annotated with procedural descriptions (against a 2% top-10 chance floor over the 503-entry target vocabulary), fine-tuning the captioner substantially improves seen-class retrieval: language and vision tower fine-tuning raises top-10 retrieval on seen classes from 4.5% (untrained) to 49%, becoming statistically indistinguishable from a standard supervised closed-set classifier (I3D) on two of the three test sets where a closed-set classifier can be evaluated at all. More importantly, unseen-class retrieval also improves significantly over the untrained pipeline (11.5% -> 21.0% top-10, p=0.0094), a regime in which the closed-set classifier cannot participate. A matcher-side empirical upper-bound analysis shows the sentence encoder already recovers close to 100% of paraphrased gold descriptions, locating a gap in captioning quality that we aim to address in future work. To our knowledge this is the first description-based, open-vocabulary sign lookup from continuous signing without gloss supervision, and the first for JSL.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
