# OCR arXiv Daily Pro — 2026-10-23

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-22 09:10 - 2026-10-23 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a8395743-e1d6-4

---

## 📄 论文详情

### 1. A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions

- **ArXiv ID**: [2610.31385v1](https://arxiv.org/abs/2610.31385v1)
- **作者**: Yufei Tong, Guanjie Cheng, Tianle Wu, Leilei Zhang, Hang Zheng...
- **发布时间**: 2026-10-22
- **分类**: cs.CV, cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.31385v1](https://arxiv.org/pdf/2610.31385v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual document understanding is essential for acquiring knowledge from visually rich documents and is attracting growing research interest. Existing surveys emphasize architectures or technical approaches, with limited attention to how task bottlenecks shape technical choices and research priorities. We present a task-centric survey that decomposes long-document visual question answering (VQA) into four components: document parsing, evidence organization and retrieval, generator organization and learning, and evaluation. For each, we develop a fine-grained taxonomy and trace motivations, technical responses, and cross-component connections. We focus on explicit retrieval while covering direct reading. Our temporal analysis traces expanding priorities from multimodal content understanding to sufficient, high-fidelity evidence acquisition and sustained evidence management. We outline future directions in evidence sufficiency, verifiable and correctable understanding, and budget-aware coordination, with an outlook on continual document understanding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cf3f2027-5198-4

---

### 2. Cross-Spectral Feature Fusion for Multispectral Document Binarization

- **ArXiv ID**: [2610.30863v1](https://arxiv.org/abs/2610.30863v1)
- **作者**: Yasas Savinda, Maheshi Buddhinee Dissanayake
- **发布时间**: 2026-10-22
- **分类**: cs.CV, eess.SP
- **PDF**: [https://arxiv.org/pdf/2610.30863v1](https://arxiv.org/pdf/2610.30863v1)
- **相关度评分**: 10/10

#### 英文摘要

Historical document binarization remains challenging when faded ink, bleed-through, and background degradation exhibit wavelength-dependent behavior across visible and near-infrared observations. This study investigates whether adaptive cross-spectral feature fusion and targeted structural guidance can improve multispectral document binarization beyond fixed fusion and generic attention mechanisms. Four registered SMADI bands at 500, 600, 700, and 1000 nm are processed using a multi-branch conditional generative adversarial network (cGAN). Visible, NIR, and structural feature streams are fused at encoder depth L = 3 using spatial- and channel-wise softmax gating, while auxiliary edge maps derived from selected VIS-NIR band pairs provide targeted structural guidance. Nine controlled fusion and structural configurations are evaluated using five-fold document-level cross-validation, DIBCO-standard metrics, and Holm-corrected statistical testing. The F3 + NIR edge-guided configuration provides the strongest overall performance among the evaluated models, achieving mean F1 = 0.7916, p-FM = 0.8044, and IoU = 0.6654. Relative to the fixed Mid AVG baseline, it improves F1 by 0.0269, p-FM by 0.0360, and IoU by 0.0321, with all three gains remaining statistically significant after Holm correction. Mean NRM and DRD are also reduced, although these reductions are not statistically significant after correction. Targeted cross-spectral structural guidance provides an effective mechanism for regulating intermediate multispectral fusion, improving primary foreground-overlap performance while retaining the complete four-band observation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d1d8c94d-e0be-4

---

### 3. Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas

- **ArXiv ID**: [2610.31565v1](https://arxiv.org/abs/2610.31565v1)
- **作者**: Xuhui Zuo, Chenjie Cao, Tengfei Wang, Junta Wu, Yisu Zhang...
- **发布时间**: 2026-10-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.31565v1](https://arxiv.org/pdf/2610.31565v1)
- **相关度评分**: 10/10

#### 英文摘要

Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel representation CubeAtlas, which unfolds all cubemap faces into a single compact canvas. By arranging orientation-aligned, rotated polar regions alongside the equatorial faces, this representation preserves the perspective geometry of cubemaps while organizing the cross-face relationships required for seamless panorama assembly. It further enables a pretrained diffusion transformer to model the complete panorama jointly in a single pass, without altering the backbone architecture or positional encoding. While CubeAtlas has a token count comparable to ERP, its structured layout makes many dense attention interactions unnecessary. We therefore introduce a layout-aware sparse attention mask that preserves the interactions required for panorama continuity while removing geometrically irrelevant token pairs. As a result, CubeAtlas achieves better quality than ERP modeling with lower attention computation. Furthermore, we introduce a training-free super-resolution technique and a fusion scheme that enhance fine details in distortion-free perspective space before achieving the final ERP panorama. Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: dab329f4-f7b7-4

---

### 4. WeVisOne-VL: Unified Visual Perception from Objects to Pixels

- **ArXiv ID**: [2610.31329v1](https://arxiv.org/abs/2610.31329v1)
- **作者**: Tianming Liang, Junyi Pan, Yuxi Li, Canmiao Fu, Zhipeng Huang...
- **发布时间**: 2026-10-22
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.31329v1](https://arxiv.org/pdf/2610.31329v1)
- **相关度评分**: 10/10

#### 英文摘要

Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual tasks including object detection, referring localization, counting, OCR, segmentation, and matting, enabling localization at any user-specific granularity, from points and boxes to masks and alpha mattes. Architecturally, we integrate a lightweight pixel decoder into the VLM via a special <OBJ> token to generate instance-level pixel outputs. We train the model with a three-stage curriculum SFT followed by mixed-task RL. Across over 30 benchmarks, WeVisOne-VL demonstrates leading performance on both object-level and pixel-level tasks, while maintaining robust rejection for object-absent queries. By releasing WeVisOne-VL to the open-source community, we hope to advance VLMs from broad visual understanding toward truly reliable perception systems for real-world deployment.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 87221f3a-74cb-4

---

### 5. Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2

- **ArXiv ID**: [2610.31636v1](https://arxiv.org/abs/2610.31636v1)
- **作者**: Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan
- **发布时间**: 2026-10-23
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.31636v1](https://arxiv.org/pdf/2610.31636v1)
- **相关度评分**: 10/10

#### 英文摘要

Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four phenomena. The largest is a machine-generated content farm of 1,408,437 documents (5.32%) that passed the pipeline's filters, 86.6% of it passing even stricter thresholds. Blinded labels support 6 of the 7 findings (defect rates .53-1.00 against .08 in a random control) and do not support one. The compiled suite scans the full corpus in 0.7 s of wall-clock time without a GPU, against \$12k-\$90k per LLM classification pass. The best static sampling baseline validates more selectors than any agent run, at under half the cost. The agent contributes exact prevalence, a precision estimate checked against sampled documents, an account of why the pipeline missed each slice, and a reusable test. We release the framework, Slovak test suite, validation data and agent trajectories.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 562c4b2d-8504-4

---

### 6. HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction

- **ArXiv ID**: [2610.31635v1](https://arxiv.org/abs/2610.31635v1)
- **作者**: Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
- **发布时间**: 2026-10-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.31635v1](https://arxiv.org/pdf/2610.31635v1)
- **相关度评分**: 10/10

#### 英文摘要

Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level $\mathrm{Sim}(3)$ graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared $\mathrm{SE}(3)$ camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at https://kkakkkka.github.io/HiP3R.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 935d949c-a204-4

---

### 7. How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions

- **ArXiv ID**: [2610.31606v1](https://arxiv.org/abs/2610.31606v1)
- **作者**: Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros...
- **发布时间**: 2026-10-23
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.31606v1](https://arxiv.org/pdf/2610.31606v1)
- **相关度评分**: 10/10

#### 英文摘要

Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens, overlaps of 0 to 20%, and four retriever configurations were evaluated. Relevance was defined by evidence spans mapped to all containing chunks, treating overlapping chunks with equivalent evidence as relevant. Retrieval was evaluated using R-Precision, Recall@K, MRR, and nDCG@K. Separately, generation was assessed on a 512-token index at K=1 to 5 using DeepEval claim-level metrics, with deepseek-v4-pro as the LLM judge, and BLEU/ROUGE metrics. Results: The selected hybrid retriever, using 384-token chunks and 20% overlap, retrieved accepted evidence in the top three results for 17 of 18 queries. Recall@3, R-Precision, MRR@3, and nDCG@3 each reached 0.94. Ground-truth curation increased evidence spans from 25 to 37 and accepted chunk targets from 36 to 51 without changing retrieval rankings. Conclusion: Cross-encoder reranking achieved the highest retrieval scores. Expanded relevance annotations increased recognized evidence without changing rankings, highlighting annotation sensitivity. The small development set and retrieval-informed curation require independent validation, including radiologist assessment of evidence sufficiency.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5eae7a8b-1b5d-4

---

### 8. Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems

- **ArXiv ID**: [2610.31553v1](https://arxiv.org/abs/2610.31553v1)
- **作者**: Humza Akhtar, Brian Freeman
- **发布时间**: 2026-10-23
- **分类**: cs.AI, cs.DB, cs.HC
- **PDF**: [https://arxiv.org/pdf/2610.31553v1](https://arxiv.org/pdf/2610.31553v1)
- **相关度评分**: 10/10

#### 英文摘要

Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and documenting them depends on a small group of employees with deep domain knowledge. Agents built on large language models can propose metadata, cite documents, and flag quality issues, but unreviewed proposals can spread errors into downstream systems. A perfunctory approval leaves no record of what a reviewer checked. We present contestable governance: specialist agents produce scored, cited arguments for disputed metadata decisions; a steward can accept, reject, modify, or add arguments before commit; and a governance record retains the evidence, interventions, and outcome. A versioned domain glossary supplies model-specific terms and acronym definitions to the agents. We describe the workflow, a triage path that reserves full argumentation for uncertain proposals while preserving review before commit, the scoring and record models, and a gate that controls which verified decisions become precedent. Two HVAC use cases illustrate the pattern: point classification using Brick Schema class labels, supported by an open reference implementation, and an illustrative warranty failure-mode decision linking claim fields and telemetry to service notes and revisioned bulletins.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1709b970-cef3-4

---

### 9. From Prompt Rules to Golden Data Model: Production-Scale Generation of Personalized, Compliant Pharmaceutical Claims

- **ArXiv ID**: [2610.31519v1](https://arxiv.org/abs/2610.31519v1)
- **作者**: Suyash Mishra, Qiang Li, Subhabrata Adak, Upender Phogat, Srikanth Patil...
- **发布时间**: 2026-10-23
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.31519v1](https://arxiv.org/pdf/2610.31519v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language models (LLMs) are increasingly used to generate domain-specific commercial & medical content (e.g., claims, statements, and promotional phrases) in regulated industries such as pharmaceuticals. However, ensuring its regulatory compliance, factual accuracy, and audience-specific personalization remains a major challenge. We report a production case study asking whether moving compliance and personalization signal from prompt-level rules into retrieval time structured context improves pharmaceutical claims generation, using Composer, a deployed internal tool built on a Golden Data Model (GDM) of 1,867 pharmaceutical claims spanning four products. The GDM integrates claim metadata, references, audience labels, material type, usage history, Match Text Variant (MTV) links, and a six dimension quality score (6C). Across six product-audience segments, the context pipeline improves intended indication (+29%), intended content type (+62%) and intended target audience (+67%), 6C quality score (+86%), and claim reuse (+34%). Production log analysis over the deployment period shows a 29.5% reduction in weekly API cost. We report this as descriptive deployment evidence. This work is a systems and data architecture contribution: it shows that in a regulated, high-stakes domain, restructuring claim data for retrieval-time filtering is a more scalable lever than expanding prompt-level rules, and documents the engineering path data cleaning, graph linking, and quality scoring.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 208bd15e-4969-4

---

### 10. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark

- **ArXiv ID**: [2610.31466v1](https://arxiv.org/abs/2610.31466v1)
- **作者**: Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- **发布时间**: 2026-10-22
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.31466v1](https://arxiv.org/pdf/2610.31466v1)
- **相关度评分**: 10/10

#### 英文摘要

AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact. Our AnyGameRenderer generalizes across a wide range of genres that agents build, such as tower defense, auto-battlers, top-down survivors, turn-based battles, kart racing, and crowd runners. AnyGameRenderer takes plain video as its game-state input, with no complex representations such as engine G-buffers, per-object class labels, or low-poly proxies. Gray blockouts, colored primitives, semantic maps, and wireframes all work as input. It also preserves entity correspondence: group counts stay correct, and entities appear and disappear on the right frame. We implement AnyGameRenderer by LoRA fine-tuning MiniMax-H3 ref2va, a 33B reference-video-conditioned video generation model. Training uses $\sim$10k paired clips from three sources: (i) multi-stream rendering data from 38 agent-made games exported from GEAR, an AI game-creation tool; (ii) two-stream rendering data from Unreal Engine, with programmatically controlled crowds, count changes, and entity scales; and (iii) real gameplay recordings, with pairs reconstructed via 3D-box detection. To evaluate the entity correspondence, we propose an entity-level benchmark of 59 held-out cases with 753 entities, scored against ground-truth boxes. Compared with the base model, AnyGameRenderer better preserves entity correspondence: temporal match rises from 50.9\% to 62.9\%, missed count changes fall from 34.7\% to 21.3\%, and fewer entities are hallucinated or left unrendered.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 33298023-fdb2-4

---

### 11. Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language

- **ArXiv ID**: [2610.31397v1](https://arxiv.org/abs/2610.31397v1)
- **作者**: Mullosharaf K. Arabov, Svetlana S. Khaybullina
- **发布时间**: 2026-10-22
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.31397v1](https://arxiv.org/pdf/2610.31397v1)
- **相关度评分**: 10/10

#### 英文摘要

Bashkir is a low-resource agglutinative language written in Cyrillic and remains poorly represented in modern LLMs. We present an open resource suite and a systematic benchmark of adaptation methods: the Bashkir Web Corpus (71,567 documents, 46.9M tokens, 16 sources) and three labelled datasets for binary, multiclass and multilabel text classification; the benchmark covers the first two. Experiments use eight architectures (82M-8B: DistilGPT2, GPT-2 base/medium, Phi-3-mini, Mistral-7B, YandexGPT-5-Lite-8B, mBERT, XLM-R) and three adaptation groups (full fine-tuning, QLoRA, in-context learning), plus continual pretraining (CPT). (1) QLoRA on 3.8-8B models outperforms encoder-only fine-tuning on binary classification: YandexGPT-5-Lite-8B with CPT reaches macro-F1 0.748 vs 0.653 (XLM-R) and 0.650 (mBERT); pairwise differences are significant after Holm correction (p<0.001). (2) YandexGPT-5-Lite-8B significantly outperforms Mistral-7B and Phi-3-mini on multiclass classification, BPB and native-speaker ratings (mean 3.28 vs 2.52 and 2.22; n=100; alpha=0.69-0.77; p<0.05); on binary classification its QLoRA advantage is not significant (p>=0.084). (3) CPT effects depend on model and task: perplexity improves for Phi-3-mini (+0.58) and YandexGPT-5-Lite-8B (+0.33) but worsens for Mistral-7B (-1.15, p<0.001); on binary classification CPT helps Mistral-7B most (+4.0 macro-F1). (4) Tokeniser fertility on Bashkir varies 2.67x (2.92-7.80) and tracks adaptation quality, while perplexity across tokenisers is not comparable. Cyrillic tokenisers with Russian pretraining are preferable; LLM judges reproduce native ratings for grammar and coherence (rho=0.33-0.46) but not language correctness (rho=0.16, p=0.11); native evaluation remains necessary. All artefacts are open-licensed.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3087222e-de81-4

---

### 12. AI Risk Ontologies for the EU AI Act Compliance: AIRO, VAIR, and their Integration with DPV

- **ArXiv ID**: [2610.31380v1](https://arxiv.org/abs/2610.31380v1)
- **作者**: Delaram Golpayegani, Harshvardhan J. Pandit, Declan O'Sullivan, Dave Lewis
- **发布时间**: 2026-10-22
- **分类**: cs.CY, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.31380v1](https://arxiv.org/pdf/2610.31380v1)
- **相关度评分**: 10/10

#### 英文摘要

As the use of AI, and consequently its harms, becomes more prevalent, the global discourse around AI has become increasingly risk-aware. With new risks emerging more frequently than ever, a key challenge is how to represent, document, and catalogue AI risks in an effective, interoperable, and queryable manner. Additionally, the European Union (EU) AI Act's requirements for "high-risk" AI systems to manage and document the risks creates the need for open and interoperable tools, methods, and standards that facilitate AI risk management in an ever-changing environment. In this paper, we present ontologies and taxonomies developed to assist with risk management and documentation, in line with the requirements of the EU the AI Act. We developed the AI Risk Ontology (AIRO) to specify AI use cases and their associated risks, complemented by the Vocabulary of AI Risks (VAIR), which populates AIRO with taxonomies of concepts. Key international standards on AI and risk, namely ISO/IEC 23894 on AI risk management and ISO/IEC 22989 on AI terminology informed the development of the ontologies. To promote reuse and enable multi-regulatory compliance, AIRO and VAIR have been integrated in the Data Privacy Vocabulary (DPV) through a consensus-building process, expanding DPV's scope from data to AI.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3224e49a-8211-4

---

### 13. SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs

- **ArXiv ID**: [2610.31317v1](https://arxiv.org/abs/2610.31317v1)
- **作者**: Yifan Yuan, Yancheng Zhu, Zuoyu Zhang, Xiaogang Peng
- **发布时间**: 2026-10-22
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.31317v1](https://arxiv.org/pdf/2610.31317v1)
- **相关度评分**: 10/10

#### 英文摘要

Most automated survey generation systems retrieve papers as flat documents, limiting their ability to capture research structure. We present SurveyGraph, a framework built around a Methods-Entity Knowledge Graph (MEKG) encoding method-level follow-on, competition, and shared-resource relations. The graph supports core-paper discovery, retrieval, hybrid outlining, and evidence-gated narrative synthesis. We evaluate retrieval, semantic edges, citation grounding, collection coverage, and generation-stage components. In a controlled seven-method equal-budget benchmark, MEKG-anchored fusion balances recall and structural density, with an independent co-citation check. In a separate archived graph-native diagnostic, graph-aware retrieval nearly doubles recall over flat lexical baselines across eight runs (p = 0.004). A semantic evidence gate achieves AUC = 0.75. Audits of 160 generated sentences find 80.6% anchored-or-partial citation support. Human adjudication of 108 stratified semantic edges finds 68.5% supported-or-partial relations (binary-support Cohen's kappa = 0.64), with improves strongest (80.6%) and extends weakest (52.8%). A SurveyBench-facing collection probe reaches mean reference coverage of 0.521 across four topics with an eight-paper budget. Same-backend Qwen diagnostics on a 30-paper/74-relation graph show reduced organization signals when hybrid outlining is removed. Concurrent-system comparisons provide bounded context rather than matched-backend end-to-end evidence. The results position MEKG as an auditable structural layer for typed diagnostics, relation-specific filtering, and controlled survey generation. Code and artifacts: https://github.com/xzzvsxd/SurveyGraph.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5709ced3-bbad-4

---

### 14. The Delayed Countdown Method for Validating Review-Oriented AI Workflows in eDiscovery

- **ArXiv ID**: [2610.31311v1](https://arxiv.org/abs/2610.31311v1)
- **作者**: David D. Lewis, Tara Emory, Lenora Gray, Mark Noel, Jeremy Pickens...
- **发布时间**: 2026-10-22
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.31311v1](https://arxiv.org/pdf/2610.31311v1)
- **相关度评分**: 10/10

#### 英文摘要

Review-oriented workflows have become the dominant approach to AI-assisted document review in electronic discovery (eDiscovery). How to validate the effectiveness of review-oriented workflows has, however, remained a confusing and controversial topic in technology-assisted review (TAR) in the law. We examine the sources of this controversy, and propose a simple and practical evaluation approach for review-oriented workflows. Our Delayed Countdown method is easily incorporated into existing review-oriented workflows and software, is compatible with arbitrary stopping rules, and produces valid frequentist confidence intervals on effectiveness. We explain the conceptual foundations of the method, provide example computations, discuss the handling of logically impossible recall values, and suggest future work on decreasing review costs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 391cfb7f-c29e-4

---

### 15. CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring

- **ArXiv ID**: [2610.31277v1](https://arxiv.org/abs/2610.31277v1)
- **作者**: Shmuel Amar, Benjamin Lieber, Ori Shapira, Debanjana Kar, Sebastian Maximilian Dennerlein...
- **发布时间**: 2026-10-22
- **分类**: cs.CL, cs.AI, cs.HC
- **PDF**: [https://arxiv.org/pdf/2610.31277v1](https://arxiv.org/pdf/2610.31277v1)
- **相关度评分**: 10/10

#### 英文摘要

While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typically address isolated writing phases, leaving comprehensive end-to-end human-LLM collaboration largely unexplored. In this paper, we introduce CoWriter, a proactive agentic scheme that adapts expert human (co-)authoring methodologies from cognitive science to flexibly steer the entire writing workflow while actively encouraging the user to engage. In an exploratory user study, compared to a standard LLM baseline, authors using CoWriter better expressed their perspectives and maintained a higher sense of document ownership, supported quantitatively by $2.2\times$ more successful agent engagements. Furthermore, external reader judges rated the resulting texts higher in "human touch" qualities like storytelling and integrating unique personal experiences. Overall, our results demonstrate that proactively engaging users through established human practices is beneficial for effective LLM-supported co-authoring, providing useful methodologies, techniques and insights for future research on collaborative agents.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3e21c59a-ba17-4

---
