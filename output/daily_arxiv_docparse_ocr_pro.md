# OCR arXiv Daily Pro — 2026-08-25

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-08-24 09:10 - 2026-08-25 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. WildHandBench: A Benchmark for Handwritten Text Understanding that Challenges MLLMs and Humans

- **ArXiv ID**: [2608.22959v1](https://arxiv.org/abs/2608.22959v1)
- **作者**: Jun Zhang, Qiao Zhao, Cheng Cui, Jianying Qu, Zhongkai Sun...
- **发布时间**: 2026-08-24
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.22959v1](https://arxiv.org/pdf/2608.22959v1)
- **相关度评分**: 10/10

#### 英文摘要

While the top model on OmniDocBench now reaches 96.34% overall on printed-document parsing, the ability of current models to handle challenging handwritten documents remains largely uncharacterized. Existing benchmarks focus on isolated text or formulas, overlook handwritten tables and real-world degradation, and report aggregate accuracy without explaining why models fail. We present WildHandBench, a benchmark containing 500 handwritten documents across three structures (free text, tables, formulas), four languages, and nine real-world scenarios. We introduce a Prior-Driven Error (PDE) metric that quantifies whether errors originate from language priors rather than visual evidence. Evaluating 18 state-of-the-art models together with calibrated human baselines, we find: (1) the best model achieves only 71.85% overall; (2) humans outperform all models yet the gap is narrow (77.09% vs. 71.85%); and (3) model errors are qualitatively different from human errors -- 63-91% of model errors are prior-driven versus only 49% for humans, exposing systematic reliance on language priors that conventional accuracy metrics cannot capture.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. FinixDoc: Rethinking Financial Document Parsing Beyond Saturated Benchmarks

- **ArXiv ID**: [2608.22842v1](https://arxiv.org/abs/2608.22842v1)
- **作者**: Hang Wang, Jin Zhang, Guoliang Xu, Pengyue Lu, Yao Li...
- **发布时间**: 2026-08-24
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.22842v1](https://arxiv.org/pdf/2608.22842v1)
- **相关度评分**: 10/10

#### 英文摘要

Financial document parsing requires accuracy, structural consistency, and verifiability that current benchmarks often fail to reflect. We present FinixDoc, an end-to-end agentic parsing system for real-world financial documents, with FinixDoc-VL, a 4B-scale vision-language model built on Qwen3-VL-4B, as its core parser. To characterize the gap between benchmark and deployment performance, we introduce a Document Parsing Capability Matrix organized along two practical axes: visual quality and document scale. Guided by this matrix, FinixDoc-VL is trained with a domain-adapted recipe combining homoglyph-aware contrastive learning and multi-stage reinforcement learning with composite domain-specific rewards. To better leverage our accumulated advantage in low-quality financial-document data and support large-scale, high-quality data production, we further build a human-in-the-loop Data Factory pipeline with confidence-aware expert review. For evaluation, we construct FinixDocBench, a financial-domain evaluation suite covering digital-native, camera-captured, ultra-large-page, and internal-workflow scenarios, with a compliance-reviewed subset released alongside this technical report. On its main subsets, FinixDoc-VL achieves the highest overall score (81.43) among evaluated baselines, outperforming the next-best open-source model by 5.13 points, with the largest gains on internal financial workflows (FinixInner: 84.08 vs. 78.73).

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning and Benchmark Datasets from Industrial Technical Reports

- **ArXiv ID**: [2608.22817v1](https://arxiv.org/abs/2608.22817v1)
- **作者**: Parsa Bakhtiari, Hassan Bashiri, Alireza Khalilipour, Masoud Nasiripour, Moharram Challenger
- **发布时间**: 2026-08-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.22817v1](https://arxiv.org/pdf/2608.22817v1)
- **相关度评分**: 10/10

#### 英文摘要

Industrial technical reports contain high-value knowledge for maintenance, troubleshooting, and product engineering, but their heterogeneous structure (dense prose, specifications, tables) makes them difficult to index and reason over with standard retrieval and QA pipelines, and no public instruction-tuning or benchmark datasets are built from such documents. We address this gap with Industrial-Instruction, contributing (i) two open QA datasets built from real industrial technical reports and (ii) the end-to-end pipeline that produces them. Using 906 public Panasonic documents (7,525 pages), we apply layout-aware extraction, build a semantic retrieval index, and synthesize multiple-choice QA grounded in retrieved evidence under five query-document relationships (irrelevant retrieval, single-/multi-document support, single-/multi-document answer). After filtering an initial 23.9k generated samples, each dataset provides approximately 13.6k QA pairs with source documents and a held-out benchmark split. Fine-tuning small open LLMs (under 10B parameters) improves Set-Match Accuracy from 28.5% to 42.0% and F1 from 46.6% to 63.5% on the Panasonic benchmark. We release two parallel versions built by the same pipeline: one generated with the open-weight Qwen3-30B-A3B-Instruct model and one with the closed, API-based Claude-Opus-4.6 model, enabling a direct comparison of open- versus frontier-model data generation. The Claude-Opus-4.6 dataset yields a cleaner raw corpus and larger fine-tuning gains, at roughly two orders of magnitude higher cost. MMLU evaluation shows models trained on the Claude-Opus-4.6 data retain essentially all general knowledge, versus a small but measurable forgetting effect for the Qwen-generated data. Together, these datasets and pipeline offer a practical, reproducible path toward scalable industrial benchmarks and training data from real-world documentation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. A Scalable Cross-Domain Event Extraction System via a Unified Generative Training Framework

- **ArXiv ID**: [2608.23261v1](https://arxiv.org/abs/2608.23261v1)
- **作者**: Siting Liang, Omar Adjali, Omair Shahzad Bhatti, Daniel Sonntag
- **发布时间**: 2026-08-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.23261v1](https://arxiv.org/pdf/2608.23261v1)
- **相关度评分**: 10/10

#### 英文摘要

Event extraction is fundamental to information extraction. Prior approaches often separate event detection and argument extraction or depend on dataset-specific designs, limiting scalability and cross-domain generalization. We propose a unified generative sequence-to-sequence framework that performs event extraction subtasks jointly and supports both pipeline and end-to-end configurations. We fine-tune pretrained language models on multiple event datasets across diverse domains, enabling a single model to retain domain-specific semantics while generalizing over large and evolving label spaces. We demonstrate these capabilities through a web-based application tailored for researchers and practitioners. The platform supports document upload, schema-aware event extraction, visualization of triggers and arguments, and comparison of different extraction configurations across domains.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards

- **ArXiv ID**: [2608.23525v1](https://arxiv.org/abs/2608.23525v1)
- **作者**: Zhiqing Cui, Xinxiang Yin, Yihong Tang, Xinglang Zhang, Yuanzhe Hu...
- **发布时间**: 2026-08-25
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.23525v1](https://arxiv.org/pdf/2608.23525v1)
- **相关度评分**: 10/10

#### 英文摘要

Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evidence can change estimates of severity, exposure, and mechanism. We introduce EarthVerse, a benchmark that evaluates scientific agents through package-scoped investigations. Its 405 reproducible tasks are grounded in 199 documented events and 19 hazard families. Agents inspect heterogeneous event packages, choose compatible evidence, execute transparent calculations, reconcile source differences, and preserve provenance in the final answer. We provide executable ground truth that decomposes each task into fine-grained answer units, together with task-specific rubrics that assess the supporting research process while allowing multiple valid paths. We evaluate 25 model and agent systems under a controlled tool-using protocol, then use controlled studies to locate failures in evidence access, tool selection, memory, reasoning, interaction, and scientific execution. Across systems, the best mean answer-unit accuracy is 84.65%, while the highest Strict@95 is only 34.81%. The gap shows that current agents often complete individual steps without maintaining a consistent chain across evidence, scales, units, calculations, and physical interpretation. EarthVerse provides a reproducible basis for measuring end-to-end scientific reliability in dynamic Earth systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Robustness of IR Models to Collection Growth

- **ArXiv ID**: [2608.23419v1](https://arxiv.org/abs/2608.23419v1)
- **作者**: Emmanouil Georgios Lionis, Debasis Ganguly, Sean MacAvaney
- **发布时间**: 2026-08-25
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.23419v1](https://arxiv.org/pdf/2608.23419v1)
- **相关度评分**: 10/10

#### 英文摘要

Information Retrieval (IR) systems seek to identify relevant documents within a collection. In practical applications, collections are dynamic, with documents frequently added. We argue that ideally, a retriever's effectiveness should not decrease when non-relevant documents are added to a collection. This study formalises this concept and empirically evaluates it by merging two collections with negligible topic overlap. We hypothesise that the way an IR model conditions its ranking on other documents in a collection (e.g., the IDF component in BM25 or contextual documents in listwise rerankers) plays an important role in its robustness to the addition of non-relevant documents. We broadly classify models as those that do not depend on other documents (Multi-Document-Agnostic, MDA) and those that do (Multi-Document-Dependent, MDD). Our results show that neither MDD nor MDA models are fully robust to the addition of non-relevant documents, as all models exhibit some performance degradation. Interestingly, among the models we test, MDA is more effective than MDD for retrieval, whereas MDD and MDA rerankers are equally effective.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning

- **ArXiv ID**: [2608.23338v1](https://arxiv.org/abs/2608.23338v1)
- **作者**: Matthew Perlman, Atharva Nijasure, James Allan
- **发布时间**: 2026-08-24
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.23338v1](https://arxiv.org/pdf/2608.23338v1)
- **相关度评分**: 10/10

#### 英文摘要

LoRA fine-tuning is standard for adapting LLMs to reranking, but it remains unclear where in the network task-specific relevance behavior is learned and what attention-level changes accompany that learning. Through ablation and attention experiments, we identify where LoRA attention updates to RankLLaMA improve performance and whether those gains coincide with interpretable relevance-oriented attention patterns such as lexical matching, rarity sensitivity, and query-document interaction. We find that given LoRA fine-tuned MLPs throughout the network, restricting LoRA attention updates to a compact mid-network region is sufficient for recovering over half of the performance gained by applying LoRA to all attention layers, and that omitting attention fine-tuning in this region hurts performance more than elsewhere in the network. Additionally, we show that regions where applying LoRA affects performance the most overlap with regions where fine-tuning increased attention to axiomatic IR features. Rarity sensitivity, document-query interaction, and several compositional features are highly correlated with gains in ranking performance. Our results support an interpretable, correlational account of how relevance-oriented behavior emerges during LoRA fine-tuning and point toward improved strategies for adapting rerankers.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Flesch-Kincaid Readability Depends Only on the Topic Distribution in Long Texts under Topic Models

- **ArXiv ID**: [2608.23327v1](https://arxiv.org/abs/2608.23327v1)
- **作者**: Yo Ehara
- **发布时间**: 2026-08-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.23327v1](https://arxiv.org/pdf/2608.23327v1)
- **相关度评分**: 10/10

#### 英文摘要

Flesch Reading Ease (FRE) and the Flesch-Kincaid Grade Level (FKGL) are widely used readability scores for English computed from the same two document statistics, yet their stability on long documents need not imply invariance to lexical composition. Surprisingly, under a topic model with an explicit sentence-boundary token, both scores converge almost surely to deterministic functions of the document topic distribution through just two scalar rates: in the long-text limit, all score variation is mediated by topical composition rather than any residual readability signal. The theory covers both formulae, while the experiments evaluate FKGL. In a fixed admixture with rank[1, q, s] = 3, fibres through interior topic vectors are locally (K-3)-dimensional, whereas regular iso-score level sets are locally (K-2)-dimensional and curved. In out-of-fold evaluation on two balanced corpora, Brown and the written BNC, a topic vector inferred from one document half's content words predicts the other half's FKGL at r = 0.779 and 0.884, respectively. On Brown, adding the topic prediction to genre and mean content-word syllable count yields $ΔR^2$ = 0.002, with a confidence interval spanning zero; on the BNC, the corresponding split-half increment is 0.024, positive in four of five K = 100 fits (median 0.021). Because inferred topics may also absorb genre, register, and style, we do not interpret these results as evidence about human readability or causal effects.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. Future Querying: Can LLMs Serve as Implicit Medical World Models?

- **ArXiv ID**: [2608.23248v1](https://arxiv.org/abs/2608.23248v1)
- **作者**: Siri Willems, James Butterworth, Lore Goetschalckx, Peter Vrancx, Philippe Modard...
- **发布时间**: 2026-08-24
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.23248v1](https://arxiv.org/pdf/2608.23248v1)
- **相关度评分**: 10/10

#### 英文摘要

Traditional clinical prediction models rely on task-specific pipelines and curated, structured data, which scale poorly and underutilize unstructured text. To address this, we introduce future querying, a paradigm that probes whether large language models (LLMs) can function as implicit medical world models by evaluating their ability to answer time-indexed clinical queries about a patient's future. Our framework operates on unstructured clinical documentation using endpoint-agnostic training, enabling a single model to answer diverse clinical queries over patient trajectories without manual feature engineering or task-specific retraining. We show that small, locally fine-tuned open-weight models can match or approach larger proprietary systems, making the framework suitable for privacy-preserving, on-premise deployment. Evaluated on a new synthetic medical reports dataset and real ICU notes from the MIMIC-IV dataset, our results provide encouraging evidence that LLMs can capture aspects of clinical dynamics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Retrieval-Augmented Classification of Environmental Mitigations in Hydropower Licensing Documents

- **ArXiv ID**: [2608.23241v1](https://arxiv.org/abs/2608.23241v1)
- **作者**: Hong-Jun Yoon, Tom Ruggles, Joanna Lee, Debjani Singh
- **发布时间**: 2026-08-24
- **分类**: cs.IR, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.23241v1](https://arxiv.org/pdf/2608.23241v1)
- **相关度评分**: 10/10

#### 英文摘要

Identifying and classifying environmental mitigation obligations in Federal Energy Regulatory Commission hydropower licensing documents is a labor-intensive task requiring deep domain expertise. We formulate this as a multi-label classification problem over a structured 135-category taxonomy and address the central challenge of severe label scarcity: 40 of 135 categories have no training examples, and 26 have fewer than five. A supervised Bidirectional Encoder Representations from Transformers (BERT)-based pipeline, while effective on well-represented categories, achieves F1 of zero on unseen classes regardless of augmentation strategy. We introduce a Retrieval-Augmented Generation (RAG) pipeline that conditions classification on retrieved category definitions, enabling zero-shot generalization across the full label space. We further propose a hybrid system that combines BERT detection with RAG classification, exploiting the high recall of fine-tuned detection and the zero-shot coverage of retrieval-augmented reasoning. Evaluated on the full set of 2017 license documents (5,860 paragraphs, 135 categories), the hybrid achieves a Micro F1 of 0.524, outperforming the BERT-only pipeline (0.477) and the RAG-only pipeline (0.416) across all training-support buckets.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation

- **ArXiv ID**: [2608.23224v1](https://arxiv.org/abs/2608.23224v1)
- **作者**: Zhiruo Zhou, Zelin Li, Xiwen Chen, Jiazhuo Li, Chenwei Wang...
- **发布时间**: 2026-08-24
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.23224v1](https://arxiv.org/pdf/2608.23224v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval can efficiently and effectively augment a frozen vision--language--action (VLA) policy without retraining, yet retrieved text becomes a control intervention once it enters the executed prompt. In a matched audit, raw appended text reduces mean success from 92.47\% to 3.00\%, while meaningful and length-matched meaningless appends both fail on all 500 states. This result identifies \emph{prompt-form collapse}: changing the instruction form, rather than adding useful semantics, can dominate execution. We introduce TOWN-VLA (Think Only When Needed), a prompt-authority interface that separates candidate generation from permission to alter the policy input. A fixed compatibility rule authorizes a canonical compact instruction; otherwise, the interface restores the original Base prompt exactly. Across 900 audited routes, every route follows this contract: 525 routes recover Base with matching hashes, and all 375 authorized prompts preserve the task signature. On a matched $4\times7$ LIBERO-Plus evaluation with 10{,}030 episodes per method, success rises from 69.5\% to 73.1\% ($+362$ episodes; 95\% CI 1.89--5.45 points), improving on six perturbation axes and all four suites. On a physical PiPER arm with a frozen \pizerofive{} checkpoint, success rises from 52.7\% to 78.7\% over 150 trials per method ($p=3.16\times10^{-6}$). Prompt authority is enforceable for a frozen controller; oracle-free admission calibration is the next deployment target.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. Aligning Biomedical Texts and Knowledge Graphs: A Systematic Comparison of Lightweight Alignment Strategies

- **ArXiv ID**: [2608.23214v1](https://arxiv.org/abs/2608.23214v1)
- **作者**: Artem Bisliouk, Elizaveta Nosova, Heiko Paulheim, Andreea Iana, Rita T. Sousa
- **发布时间**: 2026-08-24
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.23214v1](https://arxiv.org/pdf/2608.23214v1)
- **相关度评分**: 10/10

#### 英文摘要

Biomedical knowledge exists in two complementary but distinct forms: unstructured scientific literature and structured knowledge graphs (KGs). Aligning them is essential for knowledge grounding, evidence retrieval, and KG completion, yet existing methods do not explicitly align free-text evidence with KG triples. We present a unified framework for systematically studying design choices for aligning biomedical text and KGs. With a text encoder and a KG embedding model both frozen, we learn only a lightweight projection between their spaces via a contrastive objective. This enables a fair comparison across six design dimensions: text encoder, KG embedding model, projection head, triple composition, training direction, and hard-negatives sampling. We construct CTD-Align, a corpus of over 22K one-to-one tripledocument pairs linking chemical-gene interactions from the Comparative Toxicogenomics Database to supporting PubMed passages. We evaluate alignment on it in two retrieval settings: document-to-triple and triple-to-document. We find that the triple composition and the training direction (i.e., shared retrieval space) have the greatest impact, whereas the text encoder and hard-negatives sampling matter little. Overall, simple choices win: projecting text into the KG space with a linear head over concatenated subject, predicate, and object embeddings performs best. These findings establish lightweight contrastive alignment as an effective, practical foundation for bridging biomedical text and KGs.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings

- **ArXiv ID**: [2608.23563v1](https://arxiv.org/abs/2608.23563v1)
- **作者**: Md Thamed Bin Zaman Chowdhury, Moazzem Hossain
- **发布时间**: 2026-08-25
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.23563v1](https://arxiv.org/pdf/2608.23563v1)
- **相关度评分**: 10/10

#### 英文摘要

Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety expertise into a compact vision-language model for scalable visual road safety auditing. The key innovation is a quantified expert-grounding stage in which the teacher vision-language model is calibrated against authoritative field audits. Large-scale annotation is permitted only after the teacher reaches substantial agreement with expert risk assessments (Cohen's kappa = 0.74). The calibrated teacher then generates structured supervision that is distilled into an 8-billion-parameter student vision-language model using Low-Rank Adaptation and a single leakage-free prompt. We also introduce Bangladesh Road Safety Audit (BD-ARSA), the first open, expert-grounded Bangladeshi visual road safety audit dataset containing 21,947 image-audit records with near-national coverage, and Expert-Grounded Road Safety Auditor (EG-ARSA), the first vision-language model developed specifically for this task. Experimental results show that grounded fine-tuning substantially improves ordinal risk assessment over the zero-shot baseline, while blind expert evaluation demonstrates that the compact student outperforms both its 31 billion-parameter teacher and Gemini-2.5-Flash. These findings demonstrate that EGD provides an effective and scalable engineering solution for proactive road safety auditing in resource-constrained environments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors

- **ArXiv ID**: [2608.23549v1](https://arxiv.org/abs/2608.23549v1)
- **作者**: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan
- **发布时间**: 2026-08-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.23549v1](https://arxiv.org/pdf/2608.23549v1)
- **相关度评分**: 10/10

#### 英文摘要

Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensive retraining. We present FixAnything, a single model for fixing a wide range of rendering artifacts. It does so by repurposing a pretrained video generative model, leveraging its implicit multi-view priors with only minimal modification and lightweight finetuning. Our key insight is that even noisily-rendered sequences preserve camera motion and coarse scene structure, allowing cleanup to be formulated as video-to-video translation. To control what scene structure should be preserved, we introduce a binary mask denoting the clean pixels, enabling the model to anchor its output to high-quality inputs (e.g. training views) while refining the rest. To encourage FixAnything to produce 3D-consistent renderings that support downstream reconstruction, we use camera pose accuracy (recovered via structure-from-motion) as a reward signal for direct preference optimization (DPO). Across four distinct 3D representations, FixAnything consistently improves rendering quality with lightweight finetuning, demonstrating that a single generalist video prior can replace multiple specialist refinement pipelines. The simplicity of the framework enables immediate adoption of stronger future video models without architectural redesign.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. Adapter-Based Few-Shot Continual Learning for Malicious Packet Recognition

- **ArXiv ID**: [2608.23536v1](https://arxiv.org/abs/2608.23536v1)
- **作者**: Kyle Stein, Guillermo Francia, III Eman El-Sheikh, Andrew Arash Mahyari
- **发布时间**: 2026-08-25
- **分类**: cs.CR, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.23536v1](https://arxiv.org/pdf/2608.23536v1)
- **相关度评分**: 10/10

#### 英文摘要

The continual evolution of malware variants necessitates detection systems that can adapt to new threats without retraining from scratch. However, continually updating models on new data often leads to catastrophic forgetting, where previously learned knowledge is overwritten. While continual learning has been increasingly explored for malware detection, the specific setting of Few-Shot Class-Incremental Learning (FSCIL), where new malware classes must be learned from only a small number of labeled examples, remains comparatively underexplored. Therefore, this work investigates the FSCIL setting for malware classification. To address the stability-plasticity dilemma, we propose a hybrid framework that leverages a Self-Supervised Learning (SSL) backbone initialized through domain-specific pre-training on malware packets. Our method incorporates Low-Rank Adaptation (LoRA) to efficiently adapt the model during the base session while freezing the core backbone to preserve previously learned representations, alongside a prototype-based classification head for incremental sessions to establish robust decision boundaries from limited samples. Extensive experiments across several datasets demonstrate that our approach consistently outperforms prior malware FSCIL baselines and achieves state-of-the-art performance.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
