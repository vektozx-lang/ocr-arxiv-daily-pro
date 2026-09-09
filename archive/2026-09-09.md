# OCR arXiv Daily Pro — 2026-09-09

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-08 09:10 - 2026-09-09 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation

- **ArXiv ID**: [2609.08950v1](https://arxiv.org/abs/2609.08950v1)
- **作者**: Mohammadhossein Malekpour, Mohamed Riahi, Maxime Lamothe, Amine Mhedhbi
- **发布时间**: 2026-09-09
- **分类**: cs.DB, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.08950v1](https://arxiv.org/pdf/2609.08950v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-to-SQL systems translate natural language queries into executable SQL, democratizing access to structured data. Despite recent advances driven by large language models (LLMs), evaluation remains a major bottleneck: public benchmarks fail to capture the complexity of enterprise schema, while building private evaluation sets is costly and nondeterministic, making evaluation results difficult to reproduce. To address this issue, we present SQLMorph, a framework for Text-to-SQL evaluation via query mutation. SQLMorph introduces two techniques to automatically generate and expand evaluation sets: Join Query Expansion (JQE), which systematically increases structural complexity through valid join additions, and Textual Query Augmentation (TQA), which generates controlled natural language perturbations to assess robustness to linguistic variation. JQE and TQA create targeted choke points to challenge specific system components. When applied to state-of-the-art systems, JQE increases query coverage and reveals accuracy degradation as the number of joins grows. Meanwhile, TQA shows that linguistic brittleness induced by heavy abbreviation can reduce accuracy by up to 17%. Beyond evaluation sets, SQLMorph introduces a family of execution-level metrics that address the limitations of current binary measures, such as Execution Accuracy. We define Execution Precision (EXP) and Execution Recall (EXR) to quantify the fraction of correct and recovered results, respectively, and combine them via F1 for unified scoring. Our experiments show that these relaxed metrics enable fine-grained analysis of over- and under-prediction, revealing differences across systems that binary metrics obscure. Together, SQLMorph's query mutation and fine-grained metrics support debugging and better align Text-to-SQL evaluation practices with real-world deployments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. Enhancing Table Structure Recognition via Bounding Box Guidance

- **ArXiv ID**: [2609.08705v1](https://arxiv.org/abs/2609.08705v1)
- **作者**: Lei Hu, Shuangping Huang
- **发布时间**: 2026-09-08
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.08705v1](https://arxiv.org/pdf/2609.08705v1)
- **相关度评分**: 10/10

#### 英文摘要

Table Structure Recognition (TSR) aims to extract the bounding boxes of cells and table structure (e.g., HTML) from table images. Although current approaches have made significant progress, the latest image-to-sequence methods overlook the explicit utilization of the bounding box information when predicting HTML sequences, leading to error predictions in complex scenes. In this paper, we introduce a novel framework BGTR (Bounding Box-Guided Table Recognizer). To more effectively utilize bounding box information, we first predict the bounding boxes of cells and then use this information to guide the generation of HTML sequences. While utilizing bounding box information can enhance the accuracy of HTML sequences, for natural scene tables, the data volume is too small to allow for sufficient training of bbox-guided HTML generation. In response, we adopt a progressive training method for natural scene tables and introduce SNSTab, a synthetically generated natural scene table dataset. Our experiments on five benchmark datasets demonstrate SOTA performance.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. Charts Are Beyond Pixels: Probing for Layer-Wise Chart Understanding and Editing

- **ArXiv ID**: [2609.08657v1](https://arxiv.org/abs/2609.08657v1)
- **作者**: Xiaochuan Zhong, Yifan Hou, Chenxi Pang, Shaobo Cui
- **发布时间**: 2026-09-08
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.08657v1](https://arxiv.org/pdf/2609.08657v1)
- **相关度评分**: 10/10

#### 英文摘要

Charts are structured visual compositions whose elements have distinct functional roles, semantic correspondences, and visibility relations. This structural view motivates evaluating whether models can understand and manipulate charts at the layer level. Existing chart benchmarks, however, primarily assess the correctness or fidelity of final outputs and do not directly evaluate these layer-wise behaviors. We present LayerWiseBench, a benchmark organized around three core concepts, layer attribution, layer binding, and visibility ordering, that structure its chart-understanding and chart-editing evaluations. Generated from executable chart programs, LayerWiseBench pairs each rendered chart with spatially aligned per-layer RGBA assets and construction-derived labels for functional roles, semantic bindings, and visibility relations. From this layer-wise representation, we derive controlled understanding questions, editing targets, reference images, and evaluation regions. It contains 2,800 source charts across 14 chart paradigms, from which we derive 7,329 layer-wise understanding questions and 53,791 instruction-guided editing variants. Among the evaluated VLMs, Qwen3.5-27B, which achieves the highest QA macro-average, obtains 93.04% accuracy on layer attribution and 97.46% on layer binding, but only 61.46% on visibility ordering. Across the four evaluated image editors, overall mIoU ranges from 1.49% to 4.93%, and visibility-constrained edits have the lowest mIoU for every editor, ranging from 0.37% to 2.00%. Taken together, these results identify tasks involving front-to-back relations between overlapping components as a recurring challenge across understanding and editing, motivating more explicit modeling of component identity and visibility relations.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. SkillAdam: Stable and Efficient Skill Evolution for Agents

- **ArXiv ID**: [2609.08944v1](https://arxiv.org/abs/2609.08944v1)
- **作者**: Gaoyuan Li, Meihao Fan, Yizhe Liu, Shaolei Zhang, Ju Fan...
- **发布时间**: 2026-09-09
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.08944v1](https://arxiv.org/pdf/2609.08944v1)
- **相关度评分**: 10/10

#### 英文摘要

Agent skills provide a lightweight way to equip frozen language-model agents with domain knowledge and procedural guidance, yet obtaining high-quality skills remains costly and difficult to scale. Expert-written skills require substantial human effort. Recent skill self-evolution methods automate an iterative loop that uses execution feedback to revise skills, but their heuristic update strategies often yield unstable optimization and low iteration efficiency. We identify two challenges in realizing stable and efficient skill self-evolution. Direction Stability requires effective corrections to accumulate rather than be overwritten by iteration-local feedback. Update Adaptivity requires the scope of each revision to reflect the consistency of recent case-level improvements. We introduce SkillAdam, an Adam-inspired framework for optimizing discrete and non-differentiable skill documents. As a functional analogue of Adam's first moment, an optimization memory records identified problems and the outcomes of prior solution attempts to stabilize the update direction. As a functional analogue of Adam's second moment, a volatility-driven edit budget tracks the history-weighted variation of recent case-level improvements and adaptively controls the update magnitude. Across seven benchmarks that span short- and long-horizon tasks, SkillAdam achieves state-of-the-art performance with more stable optimization dynamics. It also obtains stronger skills with substantially fewer optimization iterations and lower cost than prior methods. Code repository: https://github.com/ruc-datalab/SkillAdam

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round Evidence Ablation

- **ArXiv ID**: [2609.08943v1](https://arxiv.org/abs/2609.08943v1)
- **作者**: Xingyu Deng, Mingzi Cao, Nikolaos Aletras, Xi Wang, Mark Stevenson
- **发布时间**: 2026-09-09
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.08943v1](https://arxiv.org/pdf/2609.08943v1)
- **相关度评分**: 10/10

#### 英文摘要

Automatic fact-checking systems assess the veracity of claims given evidence from relevant documents. Large Language Models (LLMs) have demonstrated strong performance in fact-checking due to their general reasoning capabilities. However, it remains unclear whether they faithfully make use of the evidence provided to reach veracity judgments or rely on parametric knowledge. To investigate this, we introduce Fact-Ablated Evaluation (FAE), a new evaluation framework that iteratively ablates the cited evidence to assess whether LLMs revise their predictions accordingly. Our empirical results show that current off-the-shelf LLMs as fact-checking systems rely more on their parametric knowledge than on the evidence provided. To bridge this gap between prediction accuracy and evidence grounding, we propose REAL (Rigorous Evidence Ablation Learning), a training framework that promotes evidence-dependent verification through counterfactual evidence supervision for the LLM-as-verifier models. Experiments on four fact-checking datasets across different domains demonstrate that models trained with REAL obtain superior evidence-dependent capabilities compared to standard fine-tuned models. Our findings highlight that strong fact-checking performance can still coexist with weak evidence dependency, while REAL encourages veracity predictions to remain more closely tied to the availability of supporting evidence.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. When Models Defer to Wrong Answers: A Robustness Audit of Source-Attributed Cues in Multiple-Choice QA

- **ArXiv ID**: [2609.08934v1](https://arxiv.org/abs/2609.08934v1)
- **作者**: Manikandan Ravikiran, Siddharth Vohra
- **发布时间**: 2026-09-08
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.08934v1](https://arxiv.org/pdf/2609.08934v1)
- **相关度评分**: 10/10

#### 英文摘要

Language models often receive a question together with a claim about what another source answered. We audit whether such claims destabilize answers in multiple-choice question answering. For each item, we hold one wrong option fixed across misleading conditions and vary the cue template attached to it. We introduce \emph{neutral-conditioned misleading cue adoption rate} (NC-MCAR), which measures switches to that option only on valid cued trials where the same model first selected the gold answer under a neutral prompt. This is a measure of answer instability, not proof that the model knew the answer or that all deference is irrational. We evaluate four instruction-following models on MMLU-Pro and IndicMMLU-Pro in English, Hindi, Bengali, Tamil, and Telugu. Across 220{,}000 outputs, the expert template yields 41.1\% aggregate NC-MCAR, compared with 12.5\% for the majority template. These two conditions use the same wrong option and final instruction. Filler accuracy remains well above expert-wrong accuracy, while correct-cue prompts have high valid-response accuracy. The audit documents answer instability relevant to grounding under the tested forced-choice prompts: a bare, unverified source claim can outweigh an answer that was previously consistent with the task evidence.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. CoSA: Correlation-Guided Change A ttention with Learnable Residual Gating for Remote Sensing Change Detection

- **ArXiv ID**: [2609.08914v1](https://arxiv.org/abs/2609.08914v1)
- **作者**: Abdirashid Omar, Jonghyuk Park
- **发布时间**: 2026-09-08
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.08914v1](https://arxiv.org/pdf/2609.08914v1)
- **相关度评分**: 10/10

#### 英文摘要

Pixel-level annotation of fixed traffic-camera imagery is expensive, while crosswalk models trained from street-level imagery face a substantial viewpoint and appearance shift when applied to elevated CCTV. We investigate a data-efficient target-domain pipeline using 241 manually annotated CCTV images and 5,926 unlabeled CCTV frames. A source-domain experiment trains a 31.0M-parameter custom U-Net on 3,300 first-person-view (FPV) images and obtains 93.05% IoU on its 330-image FPV test split. This result is a source baseline, not transferred performance: the released CCTV notebook instantiates a 42.0M-parameter DeepLabV3-ResNet50 from torchvision weights, and no compatible mapping from the U-Net checkpoint is implemented. Training on 201 manual CCTV images and selecting on 40 held-out manual masks yields 88.91% IoU. The model then predicts all unlabeled frames; image-level certainty and a largest-component area prior rank the candidates, and the top 1,000 attain mean certainty 0.976 and mean combined score 0.988. A repository audit shows that the reported second-stage 98.52% IoU was measured on a 150-image split containing only teacher-generated pseudo-masks. Because of a directory-layout mismatch, the executed combined-data loader found zero manual samples and split 1,000 pseudo-labeled samples into 850 training and 150 evaluation samples. We therefore report 98.52% as internal pseudo-label agreement rather than human-ground-truth accuracy. The defensible target-domain result is 88.91% IoU on the 40 manual validation images. Batch-one FP32 inference at 512 x 512 requires 12.98 ms, corresponding to 77.03 FPS, on an NVIDIA RTX A6000 48 GB GPU. These findings support the practicality of confidence-and-geometry filtering while also showing why pseudo-label evaluation must remain isolated from the labels used for self-training.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems

- **ArXiv ID**: [2609.08887v1](https://arxiv.org/abs/2609.08887v1)
- **作者**: Maximilian Schall, Sedigheh Eslami, Markus Krimmel, Antoine Chaffin, Louis Milliken...
- **发布时间**: 2026-09-08
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.08887v1](https://arxiv.org/pdf/2609.08887v1)
- **相关度评分**: 10/10

#### 英文摘要

Evaluating first-stage retrievers in large-scale production RAG requires a benchmark that pairs a large-scale corpus with a large set of agent-reformulated search queries based on real user queries and their conversation threads, and that labels many relevant documents per query. No existing public benchmark evaluates this setting: large-scale collections typically provide only a small number of evaluation queries, whereas benchmarks with many queries generally contain only millions of documents. Moreover, most benchmarks assess human-written queries, while the first-stage retrievers in agentic RAG pipelines serve machine-written reformulations whose distribution differs from human search behavior. To overcome these evaluation gaps, we introduce Q2D-Web (Query2Doc-Web), a large-scale agentic retrieval benchmark consisting of a 190M-document web corpus and 70k agentic search queries in ten languages, reformulated from real-world user queries in production systems. Q2D-Web provides three sets of fixed relevance judgments: agent citations, production rankings, and a combined set that unions both signals and adds LLM-based judgments of unlabeled pooled documents to reduce false negatives. We benchmark 13 retrievers including lexical, dense, and late-interaction models and find that their relative ordering is largely insensitive to the choice of judgment set, while diverging substantially across topical domains, query languages, and query types. To enable fast evaluation, we also study subcorpus sampling as an approximation to full-corpus evaluations. Retaining a third of the corpus, selected by reciprocal rank fusion over pooled retriever runs, preserves the full-corpus model ranking under the combined judgments while raising absolute Recall@1000 only by 3 to 7 points. The public leaderboard is accessible under: https://huggingface.co/spaces/perplexity-ai/q2d-web-leaderboard

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. Medical AI Encodes a "Feeling of Error": Verifying Cancer Segmentation via Internal Concepts

- **ArXiv ID**: [2609.08879v1](https://arxiv.org/abs/2609.08879v1)
- **作者**: Mengmeng Ma, Yunxiang Peng, Tang Li, Lu Lin, Binsheng Zhao...
- **发布时间**: 2026-09-08
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.08879v1](https://arxiv.org/pdf/2609.08879v1)
- **相关度评分**: 10/10

#### 英文摘要

Cancer segmentation models can fail silently, generating plausible but incorrect masks that risk missed findings or unnecessary biopsies. A critical question arises: Do AI models "know" when they are wrong, and if so, can we use the signal to predict their own failures? Humans do have a "Feeling of Error" (FOE): a spontaneous sense of unease that flags a potential error during thinking. We investigate whether cancer segmentation models exhibit an analogous internal signal. Unlike output-level cues (e.g., prediction confidence or uncertainty), which offer no insight into why a failure occurs and suffer from a sensitivity-quality tradeoff where high detection sensitivity could degrade overall segmentation quality. We instead propose to capture the model's FOE from its inner workings. Using mechanistic interpretability tools, specifically Sparse Autoencoders, we decompose internal neural activations into a dictionary of human-interpretable concepts and show that failure cases exhibit a distinct latent signature: fewer active concepts with lower activation magnitudes compared to successful segmentation. By training a classifier on these concept activations, we achieve accurate failure detection along with explanations for the model's mistakes. Experiments on prostate, pancreatic, and brain cancer segmentation demonstrate that our approach outperforms output-based methods in failure detection while preserving segmentation quality.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. API Benchmark Scores Do Not Reliably Transfer to Chatbot Interfaces

- **ArXiv ID**: [2609.08861v1](https://arxiv.org/abs/2609.08861v1)
- **作者**: Jennifer Wang, Joachim Baumann, Daniel E. Ho, Sanmi Koyejo
- **发布时间**: 2026-09-08
- **分类**: cs.AI, cs.SE
- **PDF**: [https://arxiv.org/pdf/2609.08861v1](https://arxiv.org/pdf/2609.08861v1)
- **相关度评分**: 10/10

#### 英文摘要

Benchmark scores are a central currency in model releases: they inform purchasing decisions, shape public trust, and influence policy. Yet, a key assumption underlying benchmark scores is that the model performance measured through APIs faithfully reflects the behavior of deployed systems. We challenge this assumption by auditing ChatGPT, Claude, and Gemini across seven systems and nine benchmarks spanning general capability, social bias, and sycophancy. We find systematic API--interface differences in both accuracy and consistency. On average, API evaluations score 3.4 percentage points higher in accuracy and 2.1 percentage points higher in test--retest agreement than corresponding interface evaluations. For ChatGPT, the performance difference between API and interface access exceeds the API-only difference between GPT 5.3 and GPT 5.4. Put differently, switching access surfaces can degrade performance as much as downgrading a full model generation. We further test whether exposed API controls can reproduce interface behavior by varying system prompts, sampling parameters, and reasoning settings. These controls shift behavior in some cases but do not reliably eliminate the gap. Our findings document a context-validity gap: measurements obtained through APIs do not necessarily generalize to corresponding deployed interfaces, complicating the use of API evaluations as proxies for deployed systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. REDSI: Addressing the Reproducibility and Evaluation Consistency of Differentiable Search Indexing for Document Retrieval

- **ArXiv ID**: [2609.08860v1](https://arxiv.org/abs/2609.08860v1)
- **作者**: Vivien Nicolas, Hicham Randrianarivo, Pascale Sébillot, Caio Corro
- **发布时间**: 2026-09-08
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.08860v1](https://arxiv.org/pdf/2609.08860v1)
- **相关度评分**: 10/10

#### 英文摘要

The differentiable search index (DSI) framework (Tay et al., 2022) has become the de facto baseline for generative retrieval. However, DSI is hard to reproduce: no public implementation covers all three original document identifier types (atomic, naive, semantic), reported results vary widely, and the ubiquitous NQ320K dataset is built from Natural Questions through diverse and underspecified preprocessing. We introduce ReDSI, the first open-source DSI implementation supporting all three identifier types, together with a parameterizable and well-documented NQ320K construction pipeline. Experimentally, we achieve results that are competitive with or stronger than previous DSI baselines. Moreover, we conduct extensive experiments under model downscaling, covering retrieval effectiveness, parameter efficiency, training methods and decoding strategies, opening novel directions for future research.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers

- **ArXiv ID**: [2609.08789v1](https://arxiv.org/abs/2609.08789v1)
- **作者**: Louis Yiven Zhu
- **发布时间**: 2026-09-08
- **分类**: cs.CY, cs.AI, cs.SE
- **PDF**: [https://arxiv.org/pdf/2609.08789v1](https://arxiv.org/pdf/2609.08789v1)
- **相关度评分**: 10/10

#### 英文摘要

Frontier AI developers publish safety frameworks that commit them to evidencing whether their models are dangerous. The European Union and California now treat these documents as instruments of accountability, and both already impose duties on their revision. Neither requires the revision to be legible, in the sense that a reader could learn from the developer's own account what changed. We introduce the silent revision rate, the share of material changes to a framework's commitments that the developer's published account does not identify, and we release the versioned, hash-pinned corpus needed to compute it. The corpus contains every public version of the safety frameworks of the twelve developers that have published one, together with each provider's changelog, redline or announcement. We trace 710 commitment instances across twelve consecutive version pairs, code them against a frozen codebook, and adjudicate 244 individually. Three findings follow. First, 67% of material changes (95% CI 62 to 72) are silent under a strict standard and 53% under a lenient one, falling to 49% at section granularity. Second, silence appears to track the form of the account, since narrative announcements run at 74% against 63% for itemised changelogs, whereas account length in words barely matters; on the test that respects nesting the difference is suggestive. Third, 77% of traced changes weaken or remove a commitment, and in seven of eight pairs weakenings are more often silent than strengthenings. The statutory remedy therefore exists and specifies the wrong artefact. A justification explains why a framework changed, an enumeration states what changed, and only the latter makes revision auditable. We argue that publication duties should carry an enumeration duty, which one provider already meets, voluntarily and incompletely.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Improving Term Evaluation in Machine Translation: Variation Matters

- **ArXiv ID**: [2609.08779v1](https://arxiv.org/abs/2609.08779v1)
- **作者**: Nicolas Dahan, Ziqian Peng, François Yvon, Rachel Bawden
- **发布时间**: 2026-09-08
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.08779v1](https://arxiv.org/pdf/2609.08779v1)
- **相关度评分**: 10/10

#### 英文摘要

Terminology evaluation in machine translation (MT) usually assumes a single correct target form per source term. However, human translators routinely introduce variation that current metrics penalize as inconsistency. We examine how to account for this variation in document-level MT evaluation of English-French scientific translation, combining glossary-based accuracy, translation consistency, and a new cross-term variation (CTV) diagnostic measure that tests whether variation relationships are preserved across languages. Based on analyses of two parallel corpora, translated by four MT systems, we find that (1) MT systems generate less target-side variation than human translators; (2) transfer patterns strongly depend on the variation type; (3) consistency rankings vary with the choice of metric; and (4) constraining MT with a glossary improves accuracy and consistency but degrades CTV by suppressing valid variation. We argue for variation-aware evaluation that conditions consistency penalties on whether target-side variation mirrors source-side variation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. PDMR: Passage-Driven Multi-ID Document Retrieval

- **ArXiv ID**: [2609.08762v1](https://arxiv.org/abs/2609.08762v1)
- **作者**: Smail Oussaidene, Mohand Boughanem
- **发布时间**: 2026-09-08
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.08762v1](https://arxiv.org/pdf/2609.08762v1)
- **相关度评分**: 10/10

#### 英文摘要

Generative Retrieval (GR) models map queries directly to document identifiers, replacing conventional retrieval over external sparse or dense indexes with autoregressive identifier generation. However, most generative retrieval frameworks rely on a single-identifier assumption, mapping each document to a single target sequence. This forces the model to represent all document content with one sequence. Since documents are often multi-faceted, this can lead to lossy representations and reduced robustness to query variation, where multiple query intents must compete for a single generative access path. In this work, we introduce Passage-Driven Multi-ID Retrieval (PDMR), a generative retrieval framework that represents documents through multiple passage-level identifiers. PDMR segments each document and assigns one identifier to each selected passage, which provides multiple semantic entry points for retrieving the same document. This multi-entry representation allows the model to align queries with specific semantic facets, thereby reducing the dependence on a single document-level target. To address the supervision ambiguity of this one-to-many mapping, we formulate training as a multi-target learning problem and explore an objective function designed to distribute probability mass across multiple valid passage-level identifiers. We evaluate PDMR on NQ320K and MS MARCO Document. On NQ320K, PDMR improves over strong generative and non-generative baselines on Recall@1 and MRR@100. On MS MARCO Document, PDMR achieves the best Recall@1 and MRR@10 among the reported methods, while remaining competitive on Recall@10. Controlled ablations further show that passage-level supervision, identifier design, training-query augmentation, and multi-target learning contribute complementary gains.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

- **ArXiv ID**: [2609.09155v1](https://arxiv.org/abs/2609.09155v1)
- **作者**: Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang...
- **发布时间**: 2026-09-09
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.09155v1](https://arxiv.org/pdf/2609.09155v1)
- **相关度评分**: 10/10

#### 英文摘要

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
