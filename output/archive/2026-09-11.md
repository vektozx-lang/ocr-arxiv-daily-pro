# OCR arXiv Daily Pro — 2026-09-11

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-10 09:10 - 2026-09-11 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. ReGround: Grounding Reviewer Comments in Multimodal Evidence

- **ArXiv ID**: [2609.11460v1](https://arxiv.org/abs/2609.11460v1)
- **作者**: Serwar Basch, Lizhen Qu, Iryna Gurevych
- **发布时间**: 2026-09-10
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.11460v1](https://arxiv.org/pdf/2609.11460v1)
- **相关度评分**: 10/10

#### 英文摘要

Reviewer comments naturally relate to specific parts of the reviewed paper, yet grounding these comments to the underlying evidence is difficult due to long multimodal documents. Existing benchmarks do not capture this setting and largely focus on explicit, information-seeking queries. We introduce ReGround, a large-scale dataset for reviewer comment grounding that links 10,267 reviewer comments to 16,274 evidence in the original anonymous submission of 3,656 papers. We build on a simple observation: author rebuttals often include explicit references to content of the submission used to address reviewer comments, providing a high-precision annotation source. We cast grounding as a retrieval task and evaluate a wide range of retrieval methods. Results show that retrieval over the entire paper content performs poorly, evidence-type inference is a major bottleneck, and multimodal evidence provides complementary signals that text alone misses. Our dataset exposes grounding reviewer comments as a difficult and practically important problem for scientific document understanding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. A Training-Free, Alignment-Free Approach to Corporate Intelligence: Application to SEC Filings

- **ArXiv ID**: [2609.11620v1](https://arxiv.org/abs/2609.11620v1)
- **作者**: Jean-François Delpech
- **发布时间**: 2026-09-10
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.11620v1](https://arxiv.org/pdf/2609.11620v1)
- **相关度评分**: 10/10

#### 英文摘要

High-dimensional dense text embeddings and large language models face real obstacles in financial-disclosure analysis: context-window limits, hallucination risk, high computational cost, and the arbitrary rotation of vector spaces across independently trained models. We present a training-free, alignment-free framework for corporate intelligence built on deterministic sparse seed vectors. Hashing word strings into a fixed high-dimensional basis places all documents and all temporal epochs in a common coordinate system by construction, removing any need for training or alignment. Accumulating these seed vectors across sentence contexts yields corpus-specific semantic signatures that compose linearly, supporting sub-second document comparison, issuer fingerprinting, tracking of how an issuer's vocabulary shifts between filings, and thematic sentence extraction, all on ordinary CPU hardware. Demonstrating the approach on a multi-year corpus of SEC filings (10-K, 10-Q, 8-K), we show how material corporate events, among them Boeing's 737 MAX crisis, Intel's supply-chain disruptions, and Bunge's acquisition of Viterra, emerge as distinct, interpretable semantic profiles, each traceable to the exact source sentences that produced it, with no domain-specific training and no LLM inference.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development

- **ArXiv ID**: [2609.11493v1](https://arxiv.org/abs/2609.11493v1)
- **作者**: Reza Amirmoshiri, Faryad Sahneh, Yasser Jangjou
- **发布时间**: 2026-09-10
- **分类**: cs.AI, cs.MA
- **PDF**: [https://arxiv.org/pdf/2609.11493v1](https://arxiv.org/pdf/2609.11493v1)
- **相关度评分**: 10/10

#### 英文摘要

Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. This knowledge is traditionally fragmented across functions and heterogeneous formats, causing traceability gaps and significant knowledge-management costs during technology transfer and regulatory filing. We present a modular agentic-AI platform that converts a heterogeneous corpus of process-development documents into a queryable, dual-layer knowledge graph. A base knowledge layer builds a lexical graph with a Document-Section-Chunk hierarchy through lossless ingestion of digital, scanned, handwritten, and multilingual documents, while an intelligence layer extracts ontology-aligned entities and bridges cross-document concepts through a provenance-anchored domain graph. LLM agents operate across both layers, selecting the retrieval path best suited to each question. We evaluate the lexical layer with a novel three-tier protocol measuring the deployment-fidelity of a retrieval-augmented generation (RAG) system on proprietary data, demonstrated on 505 questions curated from 38 development reports of a Sanofi small-molecule program. Tier-1 multiple-choice accuracy of 95% signals strong platform reliability; the stricter Tier-2 LLM-judge pass rate of 85%, which degrades on comparative and corpus-wide questions, reveals a failure taxonomy that Tier-1 accuracy alone fails to capture. A router agent selects between layers according to question type. We anticipate this protocol will enable future designers of agentic platforms to assess their systems against nonpublic databases, and that graph-based architectures will see broader adoption in pharma as a means of transforming fragmented document repositories into structured process intelligence.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. Cross-Lingual Clinical Annotation Projection as Constrained Text Generation: A Six-Language Study

- **ArXiv ID**: [2609.11450v1](https://arxiv.org/abs/2609.11450v1)
- **作者**: Álvaro Rey-Blanes, Francisco J. Moreno-Barea, Francisco J. Veredas
- **发布时间**: 2026-09-10
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.11450v1](https://arxiv.org/pdf/2609.11450v1)
- **相关度评分**: 10/10

#### 英文摘要

Background: To determine whether cross-lingual clinical annotation projection can be formulated as a text-preserving, document-level generative task that produces verifiable character-level annotations for multilingual clinical corpus construction, and to characterize its robustness and computational trade-offs relative to candidate-based projection pipelines. Methods: We developed a constrained LLM projection workflow that inserts entity tags directly into immutable target-language text, followed by deterministic validation and character-offset reconstruction. We evaluated it alongside supervised candidate-span projection and hybrid ML-LLM refinement for transferring Spanish Disease, Symptom, and Procedure annotations into six languages. Evaluation used MultiClinAI gold standard with strict span matching and character-overlap F1 Results: Direct LLM projection achieved the strongest and most consistent performance. GLM 5.2 obtained a mean Strict F1 of 0.9201 across 18 language-entity combinations, while locally deployable Gemma4:31B achieved 0.9133. The best LLM configuration improved Strict F1 over the previous state of the art in all 18 settings, by 0.0564-0.1512, yielding 55,416 grounded mentions with reconstructed offsets. Conclusions: Direct LLM-based projection enables high-quality multilingual clinical annotation transfer and provides a practical approach for extending clinical NLP resources to languages with fewer annotated datasets and language-specific tools. Combined with local inference and deterministic validation, it can substantially reduce expert time and cost for multilingual clinical corpus construction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Prompt Revision as a Source of Cultural Bias in Text-to-Image Systems

- **ArXiv ID**: [2609.11532v1](https://arxiv.org/abs/2609.11532v1)
- **作者**: Aleksandra Urman, Elsa Lichtenegger, Salima Jaoua, Azza Bouleimen, Robin Forsberg...
- **发布时间**: 2026-09-10
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.11532v1](https://arxiv.org/pdf/2609.11532v1)
- **相关度评分**: 10/10

#### 英文摘要

Commercial text-to-image systems silently revise user prompts before generating images, a step users typically cannot disable or even see. Yet, existing audits of cultural bias examine only the final images and treat generation as a single pipeline, so they cannot tell where the bias originates. We introduce WORLDVIEW, a multilingual benchmark of 8,960 prompts across 15 languages and 31 language-context pairings. Using it, we audit the revision layer in three systems (DALL-E-3, Imagen-4, GPT-Image-1.5) through a three-step analysis of how heavily it marks each cultural context, whether it flattens that context into a narrow vocabulary, and whether that vocabulary is stereotypical. Relative to a no-context English baseline, the US is the least-marked context, while non-Western and non-Anglophone contexts are marked far more heavily, flattened into narrow vocabularies applied across topically diverse prompts, and reduced to recognizable cultural stereotypes. Comparing images from original versus revised prompts on models without a revision layer, we identify the layer itself as a previously undocumented, causal source of this stereotyping. To locate cultural bias, and fix it, we must audit the system as deployed, not the model alone.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Generative Late-Interaction Embeddings For Visual Document Retrieval

- **ArXiv ID**: [2609.11808v1](https://arxiv.org/abs/2609.11808v1)
- **作者**: Mohamed Eltahir, Talal Aloushan, Rose Khairoalsendi, Jana Shata, Mohammed Alhassan...
- **发布时间**: 2026-09-11
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.11808v1](https://arxiv.org/pdf/2609.11808v1)
- **相关度评分**: 10/10

#### 英文摘要

Late-interaction retrieval is the state-of-the-art for visual document search, but it pays for its accuracy in storage. Existing compression methods retain a subset or local average of the N~1,000 vectors per page. Under aggressive storage budgets, however, these methods degrade sharply, and alternatives require retraining the encoder. Investigating this degradation across three encoders, we found two consistent properties: the vectors lie exactly on the unit sphere and concentrate near a manifold of intrinsic dimension five to six. This geometry yields two insights. First, standard k-means centroids fall inside the sphere, causing systematic underestimation of MaxSim scores. Normalizing them to the surface is a free correction worth up to +0.093 nDCG@5 over raw centroids. Second, because the page manifold has few degrees of freedom, the full set of vectors can be regenerated from only a few. To this end, we introduce Generative Late-Interaction Embeddings (GLIE): k << N vectors per page learned from the normalized centroids to serve as both a lightweight index and a basis for regenerating the page's full embedding set. At query time, search runs exclusively on these k vectors, and a decoder expands only the top candidates back to all N vectors for exact rescoring. At four vectors per page on ViDoRe v1, GLIE retains nearly 80% of the uncompressed system's nDCG@5, against 70% for the best prior post-hoc method. These results use a 415K-parameter network fitted in under three GPU-minutes on just a thousand training pages. At a matched training budget, fine-tuning the encoder does not reach even the training-free stage of GLIE, and the full system beats it at every budget. These patterns hold across a second encoder and ViDoRe v2. By reconstructing evidence on demand rather than sampling it, GLIE opens a new axis for storage-efficient retrieval, with the decoder as its main design surface.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

- **ArXiv ID**: [2609.11758v1](https://arxiv.org/abs/2609.11758v1)
- **作者**: Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser
- **发布时间**: 2026-09-11
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.11758v1](https://arxiv.org/pdf/2609.11758v1)
- **相关度评分**: 10/10

#### 英文摘要

Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corporate documents and knowledge bases into LLM-based systems. We introduce RAG-Safety-Bench, a benchmark to measure the safety impact of RAG on LLM models. By removing the confounding effect of retriever quality, and cleanly separating the problem into four conditions -- non-RAG, RAG with an oracle document containing the answer to the harmful request, RAG with documents related to the harmful request but without the specific answer, and RAG with random, safe documents -- the benchmark isolates the impacts of different factors in the observed safety degradation. We report results across five open-source LLMs, showing an inverse relationship between benign and unsafe capability, strong evidence that baseline safety guardrails do not lead to downstream safety guarantees in the RAG case, and model-specific support for previous findings that even benign documents can lead to unsafe generation in retrieval-enabled systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Geospatial AI, Dataverse Metadata, and the Study of Place-Based Government

- **ArXiv ID**: [2609.11674v1](https://arxiv.org/abs/2609.11674v1)
- **作者**: Danny EBanks, Devika Jain
- **发布时间**: 2026-09-10
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.11674v1](https://arxiv.org/pdf/2609.11674v1)
- **相关度评分**: 10/10

#### 英文摘要

Harvard Dataverse hosts over 150,000 research datasets, but the geographic information those datasets carry is entered as free text by depositors and has never been assembled into a searchable structure. We construct a knowledge graph from the repository's public data and metadata, organizing 102,650 datasets within a 215,985-node network of 528,003 edges linking datasets to keywords, publications, subjects, journals, and locations. Of those datasets, 43,991 (42.9 percent) carry at least one geospatial field, geographic coverage, geographic unit, or a bounding box and 96.9 percent of all nodes sit in a single connected component, so datasets remain reachable from one another even when their geospatial metadata share nothing in common. A conservative keyword search identifies 7,654 geospatially tagged datasets (17.4 percent) as directly policy-relevant, with elections and legislatures the largest cluster, followed by government administration, health policy, transportation, and education. Five datasets illustrate how this metadata behaves across policy domains and spatial scales, and an extended use case shows how community language models, stance detection with geographic aggregation, and partisan language bridging tools can attach discourse to place. The central obstacle is place resolution: the same location appears as many disconnected nodes. We argue that the graph provides a concrete setting for developing AI-driven metadata enrichment and entity resolution, and we document its coverage skew toward American, city-level data.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents

- **ArXiv ID**: [2609.11572v1](https://arxiv.org/abs/2609.11572v1)
- **作者**: Youngeun Nam, Joeun Kim, Hwanjun Song, Susik Yoon, Jae-Gil Lee...
- **发布时间**: 2026-09-10
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.11572v1](https://arxiv.org/pdf/2609.11572v1)
- **相关度评分**: 10/10

#### 英文摘要

Although large language models (LLMs) and retrieval-augmented generation (RAG) have advanced open-domain question answering (QA), they remain unreliable when documents evolve through amendments. Existing time-sensitive retrieval methods address only the disjoint-evolving environment, where each update is an independent snapshot. However, laws, policies, and regulations often operate in overlapping-evolving environments, where amendments override earlier clauses while preserving most content, creating strong semantic overlap across versions. We propose TimelyRAG, a retriever-agnostic framework that incorporates temporal distance into ranking to align queries with version-appropriate documents. We also introduce TimelyQABench, the first benchmark for regulation-heavy domains with overlapping-evolving challenges. Experiments show consistent gains, up to +28.6% in nDCG@10, highlighting the importance of temporal reasoning for reliable QA over evolving documents. All resources are available at https://github.com/kaist-dmlab/TimelyRAG.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Learning Interaction between Image and Layout Priors for Joint Image-Layout Generation in Design Templates

- **ArXiv ID**: [2609.11519v1](https://arxiv.org/abs/2609.11519v1)
- **作者**: Shirong Yang, Bo Yang, Ying Cao
- **发布时间**: 2026-09-10
- **分类**: cs.CV, cs.AI, cs.GR
- **PDF**: [https://arxiv.org/pdf/2609.11519v1](https://arxiv.org/pdf/2609.11519v1)
- **相关度评分**: 10/10

#### 英文摘要

In this paper, we address the problem of graphic design template creation, which generates a background image and a layout of foreground elements over the background to form a harmonious composition from an input text. Prior work on graphic design generation mostly adopts a sequential paradigm, where design elements are generated sequentially. We argue that such a sequential scheme falls short of faithfully capturing the dependency between the background and layout (and thus the joint image-layout distribution), which limits the quality of generated design templates. To overcome this limitation, we propose a model, InterIL, which jointly generates the two modalities, background image and layout, in a single generative process. The novel design of our joint model connects the backbones of pretrained image and layout diffusion models with a learnable communication module to explicitly model bidirectional image-layout interaction. During training, the image and layout backbones are frozen to maintain and leverage the vast pretrained single-modality prior knowledge, while only the communication module is updated, so that the model can focus on learning image-layout interaction and thereby better capture the joint image-layout distribution for improved composition harmony. Our model has no design-specific inductive bias, which allows it to better preserve the original characteristics of realistic designs. We further introduce a test-time guidance strategy to enable users to impose their specific preferences on generated results. Our experiments show that, compared with prior approaches, our model can generate significantly better results in terms of image, layout and image-layout harmonization, producing outputs closer to real samples. We also demonstrate the flexibility of our model in enforcing user preferences at inference without retraining.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. From Queries to Narratives: Cultural Heritage Data Stories for Knowledge Graph Exploration and Quality Assessment

- **ArXiv ID**: [2609.11403v1](https://arxiv.org/abs/2609.11403v1)
- **作者**: Tabea Tietz, Torsten Schrade, Etienne Posthumus, Linnaea Söhn, Jonatan Jalle Steller...
- **发布时间**: 2026-09-10
- **分类**: cs.AI, cs.DL
- **PDF**: [https://arxiv.org/pdf/2609.11403v1](https://arxiv.org/pdf/2609.11403v1)
- **相关度评分**: 10/10

#### 英文摘要

Cultural-heritage KGs such as the NFDI4Culture-KG contain millions of triples about artworks, music, inscriptions, historical events, and the people and places connected to them. For many users, however, discovering this knowledge can be difficult. While SPARQL can be learned, writing meaningful queries first requires an in-depth understanding of the graph's data model, an investment many domain researchers and practitioners are unwilling to make. Even with existing user interfaces, a starting point and some guidance are usually needed, because the data contained in the graph is highly specialized, heterogeneous, and constantly growing, making it challenging to know what it contains or which questions it can answer. In this paper, we present data stories as a way not only to lower this barrier, but also to turn exploration into data-quality assessment, and thus combine accessible querying with the discovery of issues that remain hidden in aggregate statistics. In this contribution, a data story is understood as a narrative document that integrates explanatory text and images with executable SPARQL queries and their visualized results. It is described how they are authored against the graph and how they serve several purposes: guiding users through an unfamiliar graph, creating reproducible narratives, and surfacing data-quality issues previously hidden in aggregate statistics. The authoring platform LODEON including its Sparnatural and AI-supported authoring assistants is introduced as a proof-of-concept. Within the authoring environment, every claim made about the data can be backed by an explicit query, making these narratives transparent and reproducible. This paper also reflects on lessons learned from hands-on seminars and workshops. Early experience suggests that such data stories make cultural-heritage knowledge graphs more accessible for both exploration and quality assessment.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents

- **ArXiv ID**: [2609.11390v1](https://arxiv.org/abs/2609.11390v1)
- **作者**: Peiyuan Gao, Gaoyuan Zhang, Haojie Qin, Yahui Sun, Qianyi Zhang...
- **发布时间**: 2026-09-10
- **分类**: cs.IR, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.11390v1](https://arxiv.org/pdf/2609.11390v1)
- **相关度评分**: 10/10

#### 英文摘要

State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present {\sf VikingRAG}, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. To further reduce token overhead of multi-round interaction, we materialize agentic multi-round retrieval traces as experience edges, and reuse these edges for similar queries, avoiding repeated multi-round exploration. To additionally reduce token costs when agentic multi-round retrieval is unnecessary, we introduce an adaptive escalation strategy that answers from one-round experience-augmented retrieval when the evidence is sufficient, and invokes agentic multi-round retrieval only otherwise. Experiments on real datasets show that the base system {\sf VikingRAG} matches high accuracy of state-of-the-art methods while consuming only 11.6\%--51.9\% of their tokens. With retrieval-trace reuse and adaptive escalation, token costs drop to 5.1\%--32.5\% while maintaining competitive accuracy and practical document-storage performance, showing the utility of this work for emerging AI knowledge bases.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. IndicTriMix: Developing Language Identification Datasets and Models for Tri-Language Code-Mixing

- **ArXiv ID**: [2609.11851v1](https://arxiv.org/abs/2609.11851v1)
- **作者**: Pruthwik Mishra, Rudra Trivedi, Avi Patel, Ashok Urlana, Shrikant Malviya
- **发布时间**: 2026-09-11
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.11851v1](https://arxiv.org/pdf/2609.11851v1)
- **相关度评分**: 10/10

#### 英文摘要

Language identification in code-mixed text, largely observed in social media, is highly essential when users frequently switch between multiple languages within a single utterance. Accurately identifying the languages of code-mixed tokens becomes an urgent necessity. Traditional language identification models, designed for monolingual text, are not well suited for token-level language identification in code-mixed settings. We formulate the task as a sequence labeling problem and fine-tune contextual transformer-based models MuRIL and XLM-RoBERTa best suited for Indian languages. We evaluate these systems on three different data configurations (Hindi, Gujarati, and Bengali) to predict language labels for individual tokens. We release a benchmark for language identification in code-mixed tokens with manually annotated test sets. We propose two approaches of code-mixed generation using parallel sentences of three languages. The trained models demonstrate the effectiveness of contextual embeddings for token-level language identification in multilingual social media text. For reproducibility and to facilitate future research, we publicly release our fine-tuned models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. SenseNova-U1.5: Towards Native Unified Visual Intelligence

- **ArXiv ID**: [2609.11929v1](https://arxiv.org/abs/2609.11929v1)
- **作者**: Haiwen Diao, Jiahao Wang, Chenjing Ding, Hanming Deng, Jiangnan Chen...
- **发布时间**: 2026-09-11
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.11929v1](https://arxiv.org/pdf/2609.11929v1)
- **相关度评分**: 10/10

#### 英文摘要

We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K. For post-training, we optimize specialized experts for visual aesthetics, bilingual text rendering, infographic generation, and image editing, and consolidate their capabilities through multi-expert on-policy distillation. Across extensive evaluations, SenseNova-U1.5 largely advances image fidelity, text rendering, complex composition, multi-reference editing, and interleaved generation, while improving instruction following and preserving subject identity, geometry, and unmodified regions. Despite limited exposure to structured formats in its generation data, SenseNova-U1.5 generalizes effectively to long, complex, and structured visual instructions, further proving that multimodal understanding can transfer to visual planning and creation. Together, these findings position native unified modelling as a promising path towards systems that perceive, reason and create within a fully end-to-end framework. We will open-source training code, including supervised fine-tuning, reinforcement learning, and on-policy distillation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. MindTopo: Can Foundation Models Reason in Topological Space?

- **ArXiv ID**: [2609.11900v1](https://arxiv.org/abs/2609.11900v1)
- **作者**: Yunfei Ge, Anbang Liu, Qineng Wang, Johnalbert Garnica, Jianwen Lyu...
- **发布时间**: 2026-09-11
- **分类**: cs.AI, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.11900v1](https://arxiv.org/pdf/2609.11900v1)
- **相关度评分**: 10/10

#### 英文摘要

Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity, separation, order, enclosure, and knots. MindTopo evaluates each property at two cognitive levels. Reasoning asks a model to identify topological relations or infer how they change. Planning instantiates a foundation model as a closed-loop agent whose policy selects environment actions. MindTopo contains 11,030 instances across 13 procedurally generated task types with controllable difficulty. We benchmark 14 MLLMs and study agent configurations augmented with image and video generation, including 3 video generative models in planning settings. Every MLLM performs better on reasoning than on planning, and the best-performing model remains far below observed human performance. On Qwen3-VL-2B-Instruct, supervised fine-tuning and reinforcement learning improve reasoning more than planning. Generated observations retain local cues and reach plausible endpoints, but audited rollouts do not reliably follow environment dynamics or preserve topology across transitions. Our website is at https://mind-topo.github.io/

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
