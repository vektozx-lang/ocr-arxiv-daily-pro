# OCR arXiv Daily Pro — 2026-09-01

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-08-31 09:10 - 2026-09-01 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. OCR-MetaReasoning Benchmark: Evaluating the Meta-Reasoning Ability of MLLMs in Text-Rich Image Understanding

- **ArXiv ID**: [2608.30678v1](https://arxiv.org/abs/2608.30678v1)
- **作者**: Gengxu Li, Yuan Wu, Yi Chang
- **发布时间**: 2026-08-31
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.30678v1](https://arxiv.org/pdf/2608.30678v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-rich image understanding requires multimodal large language models (MLLMs) to organize OCR (Optical Character Recognition)-grounded evidence across words, layout, fields, charts, and visual correspondences. Existing evaluations often conflate extraction with reasoning and rarely test whether models follow the required reasoning direction: applying visible rules, abstracting hidden regularities, or recovering missing premises. We introduce OCR-MetaReasoning, a controlled single-image benchmark that treats deduction, induction, and abduction as distinct directions and separates final-answer correctness from reasoning-process compliance. The benchmark contains 1,500 verified samples in a balanced \(3\times5\) taxonomy crossing three reasoning types with five OCR-object categories, along with reference reasoning steps, automatic answer scoring, the Meta-Reasoning Macro Score (MRMS), and the Reasoning Process Compliance Score (RPCS). Experiments with representative closed-source and open-source MLLMs show that OCR-grounded meta-reasoning remains far from saturated: models struggle with visible-rule application and layout-sensitive inference, while process-compliant rationales can accompany incorrect final answers under exact-match evaluation. The code is available at https://github.com/gengxuli/OCR-MetaReasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. Towards a Joint Khmer Text Recognition and Word Segmentation

- **ArXiv ID**: [2608.30213v1](https://arxiv.org/abs/2608.30213v1)
- **作者**: Marry Kong, Rina Buoy, Sovisal Chenda, Nguonly Taing, Masakazu Iwamura...
- **发布时间**: 2026-08-31
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.30213v1](https://arxiv.org/pdf/2608.30213v1)
- **相关度评分**: 10/10

#### 英文摘要

Text recognition, or extracting electronic text from document images, has been indispensable for knowledge retrieval tasks, such as retrieval-augmented generation (RAG). For Khmer, extracted text is subject to an extra word segmentation step, as Khmer does not use any visible word delimiters to denote word boundaries. Thus, a recognition-then-segmentation pipeline for Khmer requires two separate sequential models; this is not only error-prone but also adds significant latency for large-scale document processing. This paper proposes a novel joint Khmer text recognition and word segmentation framework in a unified model. The proposed model, using a connectionist-temporal-classification (CTC) decoder for fast, parallel decoding, can be instructed to recognize Khmer text with ($b=1$) and without ($b=0$) word segmentation. Experimental results on different benchmark datasets of different document modalities (document, scene, and handwritten images) show that the proposed model can not only recognize characters in document images but also locate word boundaries, removing the need for an extra word segmentation step in a conventional sequential pipeline.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. OCR-Based Field Extraction for Archaeological Pottery Metadata: The CENTURIA Dataset

- **ArXiv ID**: [2608.30616v1](https://arxiv.org/abs/2608.30616v1)
- **作者**: Gissu Valentina Naghavi, Dominik Hagmann, Martin Kampel, Irene Ballester
- **发布时间**: 2026-08-31
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.30616v1](https://arxiv.org/pdf/2608.30616v1)
- **相关度评分**: 10/10

#### 英文摘要

Pottery is a primary source for reconstructing the chronological and economic dimensions of past societies. Archaeologists often document ceramic finds through technical drawings and handwritten metadata. This metadata is critical for dating, provenance attribution, and cross-site comparison, but remains inaccessible to computational analysis, requiring manual transcription of every record. We investigate whether state-of-the-art document analysis models can address this task, and introduce CENTURIA, a dataset of 507 pottery records from the Roman site of Carnuntum, providing transcriptions, bounding boxes, and structured field-level labels across seven metadata categories. Benchmarking five OCR models reveals a substantial domain gap: zero-shot transcription error reaches 15-32% SpACER-M, far exceeding rates on printed archival documents, with domain-specific fields recovered in fewer than 3% of cases. LoRA fine-tuning on just 57 samples, reflecting a realistic archival annotation budget, closes this gap, reducing transcription error to below 1.5% and recovering overall field-level accuracy above 87%. Our results show that a small expert-validated fine-tuning set suffices to convert handwritten pottery documentation into structured, searchable metadata ready for archaeological databases.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. VeriCam: A Verification Baseline for the Classification of Unknown Data

- **ArXiv ID**: [2608.31107v1](https://arxiv.org/abs/2608.31107v1)
- **作者**: Lucas Wojcik, Gabriel E. Lima, Sergio M. Silva, Eduil Nascimento, David Menotti
- **发布时间**: 2026-09-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.31107v1](https://arxiv.org/pdf/2608.31107v1)
- **相关度评分**: 10/10

#### 英文摘要

The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training knowledge, both foundation models for image and text as well as vision-text hybrids lack the representational power needed for fine-grained, minutiae-based class separation that some real-world tasks require. To address the current gaps in the literature, we propose VeriCam, a pipeline designed to learn highly specialized features that enable classification of unknown classes in unseen data. VeriCam works by leveraging the representation power of image models trained for the verification task, where the model develops an intricate feature space that incorporates fine-grained details. By training a model to discriminate between pairs of images from the same and different classes, a relational graph is constructed, representing the class relationships between data points. We then present two approaches for graph clustering: a naive algorithm and a specific setup for the Leiden graph clustering algorithm. The pipeline is validated on the LPLCv2 dataset, which comprises real-world traffic surveillance images. We show that the dataset carries an inherent capture device bias that is posed as a generalization challenge for downstream License Plate recognition tasks such as OCR. As such, we dynamically identify capture devices with a label-agnostic approach, enabling the construction of a fair and unbiased benchmark. In the cross-device scenario, our pipeline reaches an F1-Score of 93.45 in the verification baseline and a V-Measure score of 80.13 in the clustering step. All code is publicly available at https://github.com/lmlwojcik/VeriCam

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Improving Information Extraction with Learned Queries

- **ArXiv ID**: [2608.31058v1](https://arxiv.org/abs/2608.31058v1)
- **作者**: Omar Sharif, Soroush Vosoughi, Nikhil Singh
- **发布时间**: 2026-09-01
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.31058v1](https://arxiv.org/pdf/2608.31058v1)
- **相关度评分**: 10/10

#### 英文摘要

When information extraction fails, a natural instinct is to improve the model doing it: for example, by scaling it up or refining its reasoning. In this paper, we show that another part of the pipeline matters at least as much: the queries used to elicit this information. Across four clinical benchmarks and five LLMs, improving the question design alone raises performance by 18.6 F1-score points, i.e. more than using larger extraction models. To make such question design learnable, we introduce List of Questions (LoQ), which generates document-specific question sets, and FeedQ, a feedback-driven optimization method that iteratively refines questions against extraction outcomes. The resulting optimized questions can be used to train lightweight generators: with fine-tuning, 4B-parameter models match or outperform expert-derived baselines and substantially exceed the performance of much larger untuned models. We release a dataset of 12,820 optimized questions to support a broader shift in information extraction research toward treating question design as a first-class problem.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Uncertainty-Aware Trajectory Forecasting from Imperfect Tracking

- **ArXiv ID**: [2608.30899v1](https://arxiv.org/abs/2608.30899v1)
- **作者**: Stephane Da Silva Martins, Victor Petrovic, Emanuel Aldea, Sylvie Le Hégarat-Mascle
- **发布时间**: 2026-08-31
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.30899v1](https://arxiv.org/pdf/2608.30899v1)
- **相关度评分**: 10/10

#### 英文摘要

Most trajectory forecasting models are trained on clean annotated histories, and are often evaluated under the same idealized assumption, although practical deployments rely on trajectories produced by imperfect multi-object trackers. The real-world observations exhibit localization jitter, missed or unstable detections, and data-association ambiguity, which are usually either ignored or removed through denoising. This paper instead treats tracking-derived reliability cues as an informative signal to be propagated to the predictor. We propose a plug-in uncertainty-aware formulation in which each observed state is encoded as an uncertain state representation, modeled by a Gaussian distribution whose covariance combines detection-level localization uncertainty and association-level ambiguity through the law of total variance. Existing backbones are adapted with minimal architectural changes: input trajectories are represented as Gaussian observations, and predicted trajectories are produced as Gaussian forecasts rather than deterministic coordinates. To train predictors that remain robust under structured observation noise, we combine temporally correlated Ornstein-Uhlenbeck perturbations with response-based knowledge distillation from a teacher trained on clean trajectories. Experiments on Oxford Town Centre and VIRAT using real tracker outputs, together with a complementary ETH/UCY pseudo-detection protocol, show that the proposed formulation improves displacement accuracy and the reliability-sharpness trade-off of probabilistic forecasts.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation

- **ArXiv ID**: [2608.31139v1](https://arxiv.org/abs/2608.31139v1)
- **作者**: Riya Ahuja, Tim Kacprowski, Roya Shiasi Sardoabi
- **发布时间**: 2026-09-01
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.31139v1](https://arxiv.org/pdf/2608.31139v1)
- **相关度评分**: 10/10

#### 英文摘要

BioMedRAG introduced retrieval-augmented generation with a learned chunk scorer for biomedical information extraction. However, it relies on fixed-size chunking which can fragment semantic evidence. We propose a configurable semantic chunking framework that addresses this limitation by combining entity-preserving windows, trigger-centered chunking, proposition-first extraction, tiered trigger prioritization, and hierarchical relation resolution. The framework integrates with BioMedRAG by replacing only the chunk construction stage while preserving the embedding model, learned chunk scorer, generator, and evaluation protocol. We evaluate the framework on biomedical relation extraction benchmarks (GM-CIHT, DDI, ChemProt) and adverse event classification (ADE). On GM-CIHT, the full hybrid configuration achieves 82.6% F1, improving over the fixed-size baseline (74.2% F1) by 8.4 points under our experimental setup. Cross-dataset analysis shows that semantic chunking improves extraction datasets with explicit relation cues, such as GM-CIHT and DDI, while fixed chunking remains competitive or stronger for dense biochemical extraction and binary classification settings such as ChemProt and ADE. By externalizing chunking logic into configuration files, the framework provides an interpretable and adaptable alternative to rigid fixed-size chunking for biomedical RAG pipelines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Type-Balanced Contextual Learning for Incremental Named Entity Recognition

- **ArXiv ID**: [2608.31038v1](https://arxiv.org/abs/2608.31038v1)
- **作者**: Duzhen Zhang, Yahan Yu, Xiuyi Chen, Chenxing Li, Dong Yu
- **发布时间**: 2026-09-01
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.31038v1](https://arxiv.org/pdf/2608.31038v1)
- **相关度评分**: 10/10

#### 英文摘要

Incremental Named Entity Recognition (INER) stands as a pivotal task in information extraction, emphasizing the successive identification of new entity types within unstructured text. Faced with the continuous influx of entity types, INER grapples with two significant challenges: the widespread issue of catastrophic forgetting and the unique shift issue of the non-entity type semantics. While pseudo-labeling-based INER methods have proven effective in addressing these challenges, a previously overlooked issue arises: the biased context problem. Our analysis shows that, in new sentences, the contextual associations of tokens representing old entity types exhibit a significantly stronger bias towards new entity types compared to their contexts in old sentences. This tendency intensifies the degradation of old knowledge while promoting the overfitting of new knowledge. To solve this biased context, we propose a Type-Balanced Contextual Learning (TBCL) method, featuring a sentence-duplet learning scheme and a contextual consistency loss. This approach offers a fresh perspective for INER through context analysis. Extensive experiments across ten INER settings on three highly recognized datasets showcase the efficacy of our TBCL method, highlighting its proficiency in resolving the biased context issue inherent in pseudo-labeling based INER approaches.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings

- **ArXiv ID**: [2608.31115v1](https://arxiv.org/abs/2608.31115v1)
- **作者**: Mohammad Abolnejadian, Matthew Brehmer
- **发布时间**: 2026-09-01
- **分类**: cs.HC, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.31115v1](https://arxiv.org/pdf/2608.31115v1)
- **相关度评分**: 10/10

#### 英文摘要

Missing institutional context during meetings can impede effective participation. Retrieving relevant information, often scattered across heterogeneous internal and external sources, requires costly task-switching that disrupts both individual focus and collective conversational flow, particularly detrimental during cognitively demanding tasks such as decision-making. We introduce InsightToast, a mixed-initiative application that monitors verbal discourse in real time, identifies topics and informational needs as they emerge, and proactively retrieves relevant information through a multi-agent large language model (LLM)-based pipeline integrating retrieval-augmented generation (RAG) to produce source-grounded insights as succinct text and glanceable interactive charts, delivered through a peripheral interface as ephemeral toasts in the conversation's side channel. To demonstrate the potential for yielding serendipitous insights, we showcase a usage scenario involving a knowledge base of legislative documents as the meeting's context. We then report on a comparative study (N=16), in which participants arrived at informed policy decisions while maintaining natural conversation flow.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data

- **ArXiv ID**: [2608.31082v1](https://arxiv.org/abs/2608.31082v1)
- **作者**: Milad Rezaei Hajidehi, Qitong Wang, Stratos Idreos
- **发布时间**: 2026-09-01
- **分类**: cs.AI, cs.CL, cs.DB
- **PDF**: [https://arxiv.org/pdf/2608.31082v1](https://arxiv.org/pdf/2608.31082v1)
- **相关度评分**: 10/10

#### 英文摘要

Valuable data remains embedded in unstructured sources: web pages, reports, contracts, filings, earnings calls, and PDFs. The big bet in enterprise AI is deploying LLM agents that reason over this data to answer complex questions for every knowledge worker. Agents can do this today, but at prohibitive cost. Each question repeatedly opens large documents to recover scattered evidence, consuming up to a million tokens. However, if the data were already structured, the same question would reduce to a cheap database lookup. For example, on FanOutQA benchmark, reasoning over an ideal pre-structured store is 28X cheaper, and the gap grows to orders of magnitude as questions fan out over more documents. Yet structuring everything in advance is not viable: documents hold vastly more possible structure than any workload will use, and the useful structure and documents are unknown until queries arrive. We propose agentic data cracking, a method that structures unstructured data adaptively and speculatively as a byproduct of reasoning itself. Structuring is adaptive because observed queries decide when it happens and what matters, and speculative because it goes beyond the current question. Whenever the agent opens a document to answer, a cracking sub-agent forks from the already-loaded context at marginal cost and extracts grounded structure likely to serve related future queries. Over time, an increasing share of queries is fully covered by structured data and answered without opening a document, keeping agentic accuracy at close to RAG cost. On FanOutQA, extended with merely one related question per test question, cracking cuts cost by 53% while preserving accuracy. Agentic data cracking is a first step toward next-generation data infrastructure for agentic reasoning over unstructured data: a shared substrate beneath the model where knowledge that reasoning already paid to uncover accumulates.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. When Can We Work in Embedding Space? What Text Embeddings Preserve

- **ArXiv ID**: [2608.31059v1](https://arxiv.org/abs/2608.31059v1)
- **作者**: Simon Freyaldenhoven
- **发布时间**: 2026-09-01
- **分类**: econ.EM, cs.CL, stat.ML
- **PDF**: [https://arxiv.org/pdf/2608.31059v1](https://arxiv.org/pdf/2608.31059v1)
- **相关度评分**: 10/10

#### 英文摘要

When do text embeddings work as inputs to empirical analysis? Their use rests on an assumption: that we can trade text for its low-dimensional embedding, and lose little in doing so. I make that assumption precise under a generative model in which documents are mixtures of latent topics. I study two uses---clustering units in embedding space and controlling for high-dimensional text. A cluster of embeddings is a set of documents with similar topic mixtures; controlling for the embedding is equivalent to controlling for the topic mixture, so validity reduces to whether that mixture captures the confounding. In an application to 363 U.S. metropolitan areas, embedding-based clusters of LLM-generated economic descriptions recover interpretable economic archetypes and separate local employment dynamics more sharply than clustering on model residuals, or on a curated set of industry and demographic covariates.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. OmniRAS: Standardizing Foundation Model Training and Evaluation in Robot-Assisted Surgery

- **ArXiv ID**: [2608.31048v1](https://arxiv.org/abs/2608.31048v1)
- **作者**: Leonardo Borgioli, Neil Getty, Wenli Xiu, Jessica Cassiani, Alvaro Ducas...
- **发布时间**: 2026-09-01
- **分类**: eess.IV
- **PDF**: [https://arxiv.org/pdf/2608.31048v1](https://arxiv.org/pdf/2608.31048v1)
- **相关度评分**: 10/10

#### 英文摘要

Few foundation models exist for robot-assisted surgery, partly because large robotic-surgery video corpora are difficult to assemble and existing models are evaluated mostly on laparoscopic benchmarks. Further, most existing models are evaluated on a small set of public benchmarks, mostly focused on laparoscopic surgery. We present OmniRAS, a family of 1B- and 2B-parameter V-JEPA-2.1 encoders for robot-assisted surgery, and detail their training. First, we release two densely annotated robotic-cholecystectomy datasets: OmniRAS-PR and a multi-label YT-Chole tool-verb-target task, the first triplet-style annotation for robotic cholecystectomy, together with splits, probe protocols, and an inter-rater study validating the shared phase ontology. Second, we document continued pretraining at up to 256 compute nodes with global batch 6,144 over 19 sources totaling approximately 2,650 hours of surgical video, 51% robotic, and analyze compute and data composition. Third, we evaluate against raw V-JEPA-2.1 and specialized surgical models on six tasks spanning triplet, phase, and step recognition, action segmentation, and detection, under frozen-encoder and final-four-block fine-tuning regimes. Across three seeds, this yields 254 downstream runs, including 109 with partial backbone fine-tuning. The best OmniRAS models achieve the strongest adapted results across all task families, while frozen differences are smaller.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation

- **ArXiv ID**: [2608.30996v1](https://arxiv.org/abs/2608.30996v1)
- **作者**: Atta Ul Asad, Ahsan Bilal, Muhammad Ali, Muhammad Haseeb, Dean F. Hougen
- **发布时间**: 2026-08-31
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.30996v1](https://arxiv.org/pdf/2608.30996v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query. Quantizing these caches further reduces storage, but no prior work asks whether compression damages faithfulness, whether responses remain grounded in the retrieved evidence. Faithfulness and accuracy are not equivalent: a model can produce a correct answer that is no longer supported by the context it was given. We evaluate Qwen2.5-7B-Instruct under INT8 and INT4 quantization on RGB and HotpotQA, measuring both accuracy and faithfulness with a hallucination detector, NLI entailment, and an LLM judge. INT8 is near-lossless across both metrics. INT4 reduces accuracy and, more critically, even among answers that remain factually correct, over 90% of faithfulness changes are negative, i.e., accuracy metrics are blind to this regression. The harm grows under noisy retrieval and with more retrieved chunks. Faithfulness must be audited before compressed caches are deployed.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval

- **ArXiv ID**: [2608.30949v1](https://arxiv.org/abs/2608.30949v1)
- **作者**: Seokwon Song, Sohyeon Kim, Gunhee Kim
- **发布时间**: 2026-08-31
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.30949v1](https://arxiv.org/pdf/2608.30949v1)
- **相关度评分**: 10/10

#### 英文摘要

Information retrieval (IR) increasingly targets open-ended queries that admit diverse perspectives. Existing IR benchmarks, however, focus primarily on closed-ended queries, while even open-ended benchmarks largely consist of queries whose supporting documents span a single subject domain and modality. We introduce Multi$^3$IR, a benchmark that evaluates how well retrievers cover the multifaceted perspectives of open-ended queries across diverse domains and modalities. It comprises 104.9K Stack Exchange queries, each annotated with perspective descriptions that capture the query's implicit viewpoints. We further propose SPIN, a parameter- and label-efficient method that learns noise vectors to steer embeddings toward diverse yet meaningful semantic directions. Experiments show that existing multimodal retrievers suffer from single-perspective bias, while SPIN substantially improves perspective coverage on Multi$^3$IR and generalizes well to unseen open-ended IR benchmarks. The dataset and experimental code are available at https://github.com/seokwon99/Multi3IR.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. Annotated Surrogate Retrieval for Polish Statutory Law

- **ArXiv ID**: [2608.30929v1](https://arxiv.org/abs/2608.30929v1)
- **作者**: Orkun Yiğit Cengiz
- **发布时间**: 2026-08-31
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.30929v1](https://arxiv.org/pdf/2608.30929v1)
- **相关度评分**: 10/10

#### 英文摘要

We present a family of retrieval methods for Polish statutory law built on document surrogates: language-model annotations attached to statutory articles at index time. Three designs occupy different points on the cost-quality frontier. ASCR is a surrogate cascade with reranking; ASCR-H fuses a dense list into that cascade; and DTF replaces both language-model stages with three lexical and dense retrievers, weighted reciprocal rank fusion, and a deterministic re-scoring prior, using no model call before generation. We evaluate all three against fourteen lexical, dense, fused and ablated baselines plus four controls, on 300 questions from the 2024 and 2025 Polish bar and legal counsel entrance examinations (264 with their reference article in the corpus), over 82,508 articles from 1,133 acts. On paired McNemar tests, ASCR-H places the reference provision at rank one significantly more often than every other non-oracle configuration except one of its own ablations (eighteen of twenty comparisons significant in its favour at p < 0.005), reaching 72.3% against 61.7% for BM25 and 52.3% for dense retrieval. The advantage is concentrated at the head and does not survive depth: it is significant at cutoffs of one and five, disappears by ten, and by twenty DTF leads on point estimate (86.0% versus 84.5%) at one ninth the latency and less than half the cost. Ablation attributes 27.6 points of rank-one accuracy to the reranking stage alone. We further report that the ranking advantage does not extend to citation accuracy, where DTF matches the oracle ceiling, and three negative results on lemmatisation, pseudo-relevance feedback and query rewriting. Surrogate annotation covers 27.0% of the corpus but every reference provision in the benchmark, an asymmetry we disclose and discuss. Benchmark, per-question outputs and paired significance tests are publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
