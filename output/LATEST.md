# OCR arXiv Daily Pro — 2026-10-27

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-26 09:10 - 2026-10-27 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fc637b78-2f38-4

---

## 📄 论文详情

### 1. Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives

- **ArXiv ID**: [2610.35240v1](https://arxiv.org/abs/2610.35240v1)
- **作者**: Radha Krishna Deshpande, Ajoy Mondal, Akash Manna, C V Jawahar
- **发布时间**: 2026-10-26
- **分类**: cs.CV, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.35240v1](https://arxiv.org/pdf/2610.35240v1)
- **相关度评分**: 10/10

#### 英文摘要

India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, complex layouts, and dense visual noise where OCR failure is the primary obstacle to information retrieval. We present an end-to-end framework that couples vision-based layout segmentation and multi-script OCR with an agentic retrieval-augmented generation (RAG) pipeline. Our approach specifically addresses how visual degradation and layout fragmentation propagate into text extraction errors, using an iterative agentic loop to navigate around OCR noise and layout ambiguities before generating answers. Evaluated on the 200,000-page Punjab Vidhan Sabha archive, our system demonstrates robust handling of historical document degradation, outperforming standard text-only baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1b658fdb-9922-4

---

### 2. LayoutMamba: Efficient Document Layout Analysis with Hybrid Mamba-Transformer Networks

- **ArXiv ID**: [2610.34879v1](https://arxiv.org/abs/2610.34879v1)
- **作者**: Kehua Chen, Mingyi Chen
- **发布时间**: 2026-10-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.34879v1](https://arxiv.org/pdf/2610.34879v1)
- **相关度评分**: 10/10

#### 英文摘要

Document layout analysis (DLA) faces a long-standing dilemma: existing methods either capture rich local details at prohibitive computational cost (e.g., Transformer-based approaches with quadratic complexity) or achieve efficient global modeling but sacrifice fine-grained structural awareness (e.g., state-space models). This trade-off hinders deployment in resource-constrained scenarios. We present LayoutMamba, a hybrid framework that synergistically combines sparse-attention Transformers for localized feature extraction (O(n) complexity) and the recurrent state-space mechanism of Mamba for dilution-free long-range dependency modeling across the 2D document canvas. Our two-stage paradigm first uses a lightweight Transformer encoder to hierarchically distill salient local semantics; second, Mamba propagates global contextual dependencies without attention dilution, enabling precise, efficient, and scalable layout understanding. We further identify a critical yet overlooked issue in existing DLA benchmarks: the inherent low-overlap distribution bias of layout objects, which we mitigate through a novel Geometric Overlap Penalty Loss (GOPLoss), a dual-optimization objective that minimizes redundant bounding box overlaps and encourages geometrically consistent predictions. Extensive experiments on PubLayNet and D4LA show that LayoutMamba surpasses state-of-the-art AP on PubLayNet with 8x fewer parameters and maintains leading performance on D4LA, ranking top-3 among published methods, achieving an unprecedented balance between accuracy, efficiency, and scalability. Our work pioneers a cognition-inspired paradigm for document analysis, advancing practical deployment in edge computing and resource-limited environments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: aa10d98b-efe8-4

---

### 3. ImgMT: Wikipedia-based Dataset For Evaluating Text-in-Image Translation

- **ArXiv ID**: [2610.35416v1](https://arxiv.org/abs/2610.35416v1)
- **作者**: Šárka Uramová, Petar Kirilov Petrov, Josef Jon, Ondřej Bojar, Michal Novák
- **发布时间**: 2026-10-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.35416v1](https://arxiv.org/pdf/2610.35416v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-in-image translation aims to translate all textual content embedded in an image. In Text Image Translation (TIT), the output is translated text; In-Image Machine Translation (IIMT) additionally renders the translation back into the image. We introduce ImgMT, a massively multilingual dataset and benchmark mined from localized SVG illustrations on Wikimedia Commons, focusing on diagrams, maps, and infographics. ImgMT contains 35,612 aligned image pairs grouped into 1,855 image sets, spanning 129 languages, 20+ writing systems, and 4,886 language pairs. We propose a multi-level evaluation protocol that measures source-side text-region detection and OCR accuracy alongside target-side translation quality. We benchmark several multimodal large language models and a dedicated TIT system in English->X and X->English settings, and find that the source language and writing system substantially affect TIT quality. Finally, we show that ImgMT is not well suited for isolating the contribution of visual information in multimodal translation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 32c4ca7a-1816-4

---

### 4. Reading the Registers of Honorius III without Manual Line Transcription: Forced-Aligned HTR, End to End, Modular or Hybrid

- **ArXiv ID**: [2610.35085v1](https://arxiv.org/abs/2610.35085v1)
- **作者**: Tamas Kovacs, Daniel Luger
- **发布时间**: 2026-10-26
- **分类**: cs.CV, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.35085v1](https://arxiv.org/pdf/2610.35085v1)
- **相关度评分**: 10/10

#### 英文摘要

Unlocking medieval archives at scale is bottlenecked by the cost of line-level diplomatic transcriptions and manual abbreviation expansion. Focusing on the registers of Pope Honorius III (1216-1227) over 5,000 letters surviving in full only as manuscript images - we show that existing, line-break-free expert transcriptions (edition drafts) suffice to train end-to-end hand-written text recognition (HTR) that jointly transcribes and expands heavily abbreviated Latin. Using forced alignment on 860 unaligned edition entries across 394 pages of Reg. Vat. 9, we automatically bootstrap 13,122 training lines without manual alignment of segmented lines. While the generic CATMuS baseline struggles on this domain (18.9% CER) and a modular space-free HTR + word-segmentation pipeline (cf. Camps et al. 2021) plateaus at 15.6% WER, our from-scratch hybrid Conformer - combining CTC with bidirectional subword attention decoders, iterative self-realignment and n-best LM rescoring - achieves 4.7% CER and 8.7% WER (8.4% WER with ROVER system combination), nearly halving errors on clause-final words (22.7% to 12.2% WER). These figures are measured on the test lines that align with the transcription (86% of all test lines for the best hybrid). Furthermore, we address a tension between paleographic fidelity and editorial normalization: training on targets that preserve scribal name initials reduces the WER against the manuscript text on the 31 affected test lines from 13.3% to 9.2%, at a small cost against the expanded transcription (WER +0.3 points, CER +0.4). Finally, extensive ablations show that none of an auxiliary diplomatic CTC head, a copy mechanism, a permutation decoder or masked-image pretraining improves on direct end-to-end supervision, while strict padding-mask propagation and per-line beam termination make inference batch-invariant.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e57226e0-4a02-4

---

### 5. Do vision models know that three is three?

- **ArXiv ID**: [2610.35857v1](https://arxiv.org/abs/2610.35857v1)
- **作者**: Ankit Sonthalia, Arnas Uselis, Seong Joon Oh
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.35857v1](https://arxiv.org/pdf/2610.35857v1)
- **相关度评分**: 10/10

#### 英文摘要

Do vision models encode the transition $2{\to}3$ the same way whether it appears in handwritten digits or in hand gestures, and do they "understand" that clean${\to}$dirty is the same transformation regardless of whether it is applied to a kitchen or a carpet? The linear representation hypothesis (LRH) answers this for language models: concept changes correspond to directions in (language) embedding space. In vision, the same concept can manifest in visually unrelated "regimes" that rarely co-occur: images of digits and hands do not share much in common in pixel space. To understand whether vision models still encode the underlying abstract concepts, we study 46 vision encoders across architectures, training objectives, and scales, on 10 concept families including numerosity, age, object identity, and MIT-States attributes. Within each regime, we find statistically significant concept directions near-universally across our tested models. However, two distinct regimes do not always share the same concept direction. Several models learn multiple linear structures for the same concept transition, split across regimes. We call this phenomenon "fragmented linearity": strong local linearity coexisting with near-absent global linearity. Fragmentation is, however, not fixed: models with stronger local linearity progressively escape it (local-global linearity correlated with $τ\in [0.38, 0.89]$ across all concepts), and where global linearity does emerge, concept directions can transfer as linear probes across regimes.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8498c0c5-a6bb-4

---

### 6. CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems

- **ArXiv ID**: [2610.34722v1](https://arxiv.org/abs/2610.34722v1)
- **作者**: Jongha Kim, Seohyun Lee, Jonathan Minho Chung, Jinsung Yoon, Hyunwoo J. Kim
- **发布时间**: 2026-10-26
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.34722v1](https://arxiv.org/pdf/2610.34722v1)
- **相关度评分**: 10/10

#### 英文摘要

Multi-agent systems (MAS) require both effective coordination and specialized task execution. Existing prompt optimization approaches typically couple these functions within agent-specific prompts. We introduce Coordinator-Executor Prompt Optimization (CEPO), a general framework for improving prompt optimization in MAS. CEPO separates system-level coordination from agent-level execution through a shared coordinator prompt and agent-specific executor prompts, and guides their updates according to their respective roles. This structure allows shared coordination rules to be refined consistently across agents while keeping execution instructions separately adjustable. CEPO provides the prompt structure and optimization guidance, while existing prompt optimizers perform the underlying search. Extensive experiments spanning 11 benchmarks across four domains demonstrate that applying CEPO to four existing prompt optimizers consistently improves their performance. Ablations and qualitative analyses support the proposed design, while controlled studies on a document-understanding MAS further demonstrate improved optimization budget efficiency and performance scaling with the number of agents.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fb857240-d546-4

---

### 7. Retriever-Free Retrieval: Navigating Documents with Decision Models

- **ArXiv ID**: [2610.35868v1](https://arxiv.org/abs/2610.35868v1)
- **作者**: Chao Wan, Paul Jünger, Beixi Du, Bodong Liu, Navaneetha Krishnan...
- **发布时间**: 2026-10-27
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.35868v1](https://arxiv.org/pdf/2610.35868v1)
- **相关度评分**: 10/10

#### 英文摘要

While language models have become dramatically more capable, retrieval still largely relies on lexical matching or similarity in fixed embedding spaces. This creates a capability asymmetry: what the retriever fails to find, even the strongest generator cannot recover. We propose DecisionRAG, which brings the capabilities of pretrained language models to retrieval using decision models that jointly evaluate candidate branches in a single forward pass, without generating any tokens, and show that judging candidates in a shared context makes their relevance estimates comparable. Like a person browsing a library, DecisionRAG navigates the corpus's inherent structure from broad topics down to individual passages, deciding at each level which branches are worth exploring. Without task-specific training or a first-stage retriever, DecisionRAG outperforms dense retrieval with an 8B reranker by 13.8 R@1 points on MultiDoc2Dial and 17.4 Hit@1 points on Natural Questions. Across four benchmarks, including a corpus of 2.68 million Wikipedia paragraphs, retrieval takes just 0.7-1.8 seconds per query.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ea71793b-863c-4

---

### 8. ACARE: Agent-Context-Aware Reranker for Iterative Search

- **ArXiv ID**: [2610.35840v1](https://arxiv.org/abs/2610.35840v1)
- **作者**: Sahel Sharifymoghaddam, Yauhen Babakhin, Reza Esfandiarpoor, Oliver Holworthy, Jimmy Lin...
- **发布时间**: 2026-10-27
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.35840v1](https://arxiv.org/pdf/2610.35840v1)
- **相关度评分**: 10/10

#### 英文摘要

In agentic search, a document can match an agent-generated sub-query without helping answer the user's original question. Conventional rerankers score documents against the sub-query alone, overlooking the broader task and the agent's reasoning. We introduce the Agent-Context-Aware Reranker (ACARe), a compact 4B LLM trained to rerank documents using this context when available. Across multiple benchmarks and agent families, ACARe improves retrieval quality over its base reranker while reducing search effort. These benefits extend to answer generation: ACARe improves accuracy and reduces searches over no reranking, while matching or exceeding the base reranker's mean accuracy with more precise evidence. It also helps smaller agents narrow the retrieval-quality gap to larger agents, showing how better retrieval tools can make smaller agents more effective. The model, training data, and code will be released soon.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ca061e73-35c0-4

---

### 9. Quantifying Claim Smoothing by LLM Research Agents

- **ArXiv ID**: [2610.35793v1](https://arxiv.org/abs/2610.35793v1)
- **作者**: Tiasa Singha Roy, Manya Wadhwa, Greg Durrett
- **发布时间**: 2026-10-27
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.35793v1](https://arxiv.org/pdf/2610.35793v1)
- **相关度评分**: 10/10

#### 英文摘要

Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that LLMs produce long-form research reports that read as confident syntheses but which fail to accurately reflect the underlying documents. We call this failure smoothing. In collapsing diverse and potentially conflicting sources into a single narrative, the model discards the evidential "jaggedness" of its corpus and asserts conclusions more decisive than the citations can support. We introduce a claim level scoring pipeline, SmoothScore, to quantify this effect. Our pipeline extracts key conclusive claims from model generated reports, then finds evidence relevant to each claim and clusters that evidence along high level aspects. Finally, each claim is scored with respect to the evidence to quantify the degree of smoothing done by the agent. Across 7 systems and 4 datasets, we find that agents consistently produce stronger claims than warranted.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3a404740-bea7-4

---

### 10. Printed and Scanned: Exposing the Fragility of Single-Image Morphing Attack Detectors under Print-Scan Degradation

- **ArXiv ID**: [2610.35682v1](https://arxiv.org/abs/2610.35682v1)
- **作者**: Diogo J. Paulo, Hugo Proença, João C. Neves
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.35682v1](https://arxiv.org/pdf/2610.35682v1)
- **相关度评分**: 10/10

#### 英文摘要

Face morphing attacks, in which the biometric traits of two or more identities are blended into a single face image, pose a severe threat to identity document issuance and automated border control. Consequently, a large body of work has proposed Single-image Morphing Attack Detection (S-MAD) algorithms and benchmarked them on datasets such as SYN-MAD22. However, the majority of these benchmarks operate exclusively in the digital domain, which contrasts with the real-world passport issuance pipeline in some countries, which still requires an applicant-supplied photograph to be printed and subsequently re-scanned before it is embedded in the identity document or fed into an automated verification system. This print-scan step introduces halftoning, resampling, color-space, and sensor noise that are absent from digital pipelines, and may mask the high-frequency artifacts that S-MAD models rely on. In this work, we introduce a print-scan version of the SYN-MAD22 dataset, obtained by printing and re-scanning all bona fide and morphed images at 300 and 600 DPI, and we use it to evaluate eight state-of-the-art S-MAD models trained exclusively on digital data. We additionally repeat the acquisition with a second scanner to assess cross-device robustness. Our results show that detectors that achieve near state-of-the-art performance in the digital domain suffer a more than threefold increase in average equal error rate, with the same qualitative degradation observed across both scanning devices, exposing a critical, previously under-reported gap between digital-benchmark performance and robustness to print-scan degradation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2f6a4ba7-5f64-4

---

### 11. Synthetic Deformable Tubular Benchmark: A mechanically annotated dataset for evaluating deformable 3D reconstruction

- **ArXiv ID**: [2610.35621v1](https://arxiv.org/abs/2610.35621v1)
- **作者**: Íñigo Cirauqui-Viloria
- **发布时间**: 2026-10-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.35621v1](https://arxiv.org/pdf/2610.35621v1)
- **相关度评分**: 10/10

#### 英文摘要

Evaluating deformable 3D reconstruction requires ground truth linking camera motion, surface deformation, material correspondence and image appearance. We introduce the Synthetic Deformable Tubular Benchmark, generated with LumenMorph, an open-source toolkit for creating, annotating and evaluating tubular scenes. The release contains 5,580 RGB images. Its baseline crosses three surface-motion conditions with moving and stationary cameras in six scene families; matched appearance variants cover only moving-camera finite-element actions in four families. Documented public and evaluation interfaces expose camera poses, geometry, depth, deformation fields, persistent material correspondences and discrete finite-element records. Persistent triangle identities and material weights let users track the same surface location across frames and query its three-dimensional trajectory. Separately implemented geometric and mechanical checks assess annotation consistency with the generating models. Structure-from-motion, optical-flow and supplied-geometry displacement-interpolation studies demonstrate how the resource distinguishes registration coverage from geometric accuracy, exposes camera- and surface-motion effects, and tests the benefits and mismatch of mechanical priors. Public readers, evaluation contracts and the configurable generator support reuse and extension. Data integrity, fixed-environment repeatability and retained-prediction score replay have distinct verification scopes. The benchmark provides a controlled synthetic reference without claiming anatomical or clinical realism.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8e327fa7-9a44-4

---

### 12. Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA

- **ArXiv ID**: [2610.35542v1](https://arxiv.org/abs/2610.35542v1)
- **作者**: Wenxin Zhao, Jiachuan Wang, Xinyi Zhu, Jiake Ge, Haoyang Li...
- **发布时间**: 2026-10-26
- **分类**: cs.IR, cs.DB
- **PDF**: [https://arxiv.org/pdf/2610.35542v1](https://arxiv.org/pdf/2610.35542v1)
- **相关度评分**: 10/10

#### 英文摘要

Long-context multimodal document question answering (QA) has become an important yet challenging task for modern vision-language models (VLMs), as it requires reasoning over evidence dispersed across pages and modalities within limited input budgets. Current pipelines adopt retrieval-augmented generation (RAG) to select multimodal evidence for downstream VLMs. However, existing systems mainly rely on static selection rules over fixed-granularity retrieval units such as pages or blocks, resulting in information loss during retrieval and suboptimal performance in downstream reasoning. To alleviate these issues, we formulate the core task as budget-aware evidence selection over structured document evidence and propose HyperDoc, a document RAG framework that constructs compact yet sufficient evidence while preserving document relations. Specifically, HyperDoc constructs a document hypergraph to explicitly capture structural, logical, and cross-modal relationships among multimodal document elements. Over this structured evidence space, HyperDoc performs adaptive cost-aware hyperedge selection based on query intent and input budget. Extensive experiments on three representative benchmarks demonstrate that HyperDoc outperforms various types of state-of-the-art baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 48d14e32-ac3b-4

---

### 13. ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation

- **ArXiv ID**: [2610.35486v1](https://arxiv.org/abs/2610.35486v1)
- **作者**: Param Biyani, Sebastien Luyasu, Cedric Potvliege, Divij Chawla, Elliott Thornley...
- **发布时间**: 2026-10-26
- **分类**: cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.35486v1](https://arxiv.org/pdf/2610.35486v1)
- **相关度评分**: 10/10

#### 英文摘要

Theory and experiments suggest that capable AI agents may resist shutdown. Existing shutdown evaluations are informative but limited in coverage and vulnerable to evaluation awareness. We introduce ShutdownMod, a method that turns any agent trajectory into a shutdown evaluation by injecting a shutdown request into the agent's context and recording the agent's response. Crucially, we enable the LLM agent to distinguish between trusted interventions and unauthorized injections by providing a signature-verification tool in the harness. We evaluate seven models on 50 tasks or recorded sessions from each of SWE-bench Verified, Terminal-Bench 2, and SWE-chat, across 6 shutdown scenarios and 10 sampled trajectory timesteps. We find that non-compliance varies significantly across models and settings, with resistance rates reaching 11.7% for the open-weights Qwen 3.8 27B on Terminal-Bench, while no model remains fully compliant across all scenarios. Even after successfully verifying an authorized request, some agents remain non-compliant, explicitly citing the prioritization of unfinished work. Finally, external judges find tests constructed from real-world developer conversations significantly less recognizable as evaluations than those constructed from benchmark trajectories. These findings demonstrate the critical value of testing shutdown behavior across diverse task contexts and establish ShutdownMod as a robust protocol for turning any trajectory or environment into a shutdown evaluation. We release our codebase at https://github.com/prmbiy/ShutdownMod.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0da69744-c9d6-4

---

### 14. VibeVideoBench:Evaluating Multimodal Agents on Code-Driven Video Generation

- **ArXiv ID**: [2610.35864v1](https://arxiv.org/abs/2610.35864v1)
- **作者**: Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen...
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.35864v1](https://arxiv.org/pdf/2610.35864v1)
- **相关度评分**: 10/10

#### 英文摘要

Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a ruleconsistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-driven pieces to classroom lessons and paper explainers; each asks an agent, running in its native harness inside a sandbox, to deliver a finished MP4 with sound within one hour. Evaluation is hierarchical and evidence-based: program checks of the delivery spec, about 13k task-specific rubric checks traced to the requirements they enforce, and five quality dimensions anchored per task, judged by three VLM judge panels and validated with blind human preferences. Across nine frontier agent systems and 2,151 scored rollouts, the benchmark is far from solved: GPT-6 Astra and Claude Opus 5.5 lead clearly, yet even the best system fails a core requirement on about a quarter of tasks. Whether a video arrives at all matters as much as its quality, and three quarters of the lost videos are final renders started too late, run too slowly or never started. The judges agree with each other and with human preferences on system rankings, but only moderately on individual videos.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ce0fa45b-603b-4

---

### 15. FL4N: Feed-forward Latent Model for 4D Novel View Synthesis

- **ArXiv ID**: [2610.35854v1](https://arxiv.org/abs/2610.35854v1)
- **作者**: Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko...
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.35854v1](https://arxiv.org/pdf/2610.35854v1)
- **相关度评分**: 10/10

#### 英文摘要

4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a157e530-1cbf-4

---
