# OCR arXiv Daily Pro — 2026-10-30

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-29 09:10 - 2026-10-30 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 80da141a-a294-4

---

## 📄 论文详情

### 1. Mobilizing the Archive: Bitext Extraction at Scale from Archival Documents for Extremely Low-resource Languages

- **ArXiv ID**: [2610.40233v1](https://arxiv.org/abs/2610.40233v1)
- **作者**: Chutong Meng, Alec J. Bateman, Antonios Anastasopoulos
- **发布时间**: 2026-10-29
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.40233v1](https://arxiv.org/pdf/2610.40233v1)
- **相关度评分**: 10/10

#### 英文摘要

While mining parallel sentences from web pages has proven effective for low-resource machine translation, the majority of the world's languages have little to no web presence. What they do have, though, are resources that are the result of centuries of efforts by linguists, such as grammars, dictionaries, and other documentation materials. We propose extracting translation examples from such linguistic resources, which offer parallel data for languages under-represented online and could potentially scale to thousands more languages. We develop a pipeline to achieve this, leveraging an Optical Character Recognition (OCR) model as well as a vision language model (VLM), to ensure identified content to be aligned with visual layout information. We demonstrate the utility of the extracted bitexts for bootstrapping translation systems across 20 languages, both by training machine translation models and by applying in-context learning for large language models. For in-context learning, we observe improvements of +15.78 and +6.94 chrF2++ over zero-shot translation for into low- and high-resource languages, respectively.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: def65107-3424-4

---

### 2. Unlimited OCR Works 2

- **ArXiv ID**: [2610.39308v1](https://arxiv.org/abs/2610.39308v1)
- **作者**: Shu Wei, Jingjing Wu, Qunyi Xie, Lingshu Zhang, Xiangcheng Du...
- **发布时间**: 2026-10-29
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.39308v1](https://arxiv.org/pdf/2610.39308v1)
- **相关度评分**: 10/10

#### 英文摘要

Unlimited OCR ushers the era of long-horizon parsing, substantially mitigating the growth of working memory as document lengthens. However, as document length scales to hundreds of pages, the visual context grows substantially, sharply increasing the computational cost of each decoding step and limiting the scalability of ultra-long document parsing. Inspired by human book transcription via localized focus without re-scanning preceding pages, we introduce Unlimited OCR 2, a document parsing model that looks only at what it transcribes. Building on Unlimited OCR, we upgrade all the decoder attention modules to Sparse Reference Sliding Window Attention (SR-SWA), bounding active reference tokens to a fixed capacity and thus sustaining constant computational costs across arbitrarily long documents. By combining SR-SWA with Unlimited-Horizon Decoding Paradigm, Unlimited OCR 2 enables document parsing over virtually unlimited lengths without prohibitive memory overhead. At the hundred-page scale, Unlimited OCR 2 achieves 7.0$\times$ and 5.6$\times$ per-step speedups over Full Attention and R-SWA, respectively. Furthermore, it delivers state-of-the-art end-to-end performance on both MPDocBench and MarathonDocBench, our newly proposed benchmark targeting hundred-page document parsing. Ultimately, the capacity for uninterrupted, one-shot document parsing signifies a fundamental paradigm shift into the OCR 3.0 era.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: eac83267-05d3-4

---

### 3. Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records

- **ArXiv ID**: [2610.40379v1](https://arxiv.org/abs/2610.40379v1)
- **作者**: Daniel Palacios, Guantong Qi, Anna Kadi, Natali Borrego, Sukru Aras...
- **发布时间**: 2026-10-30
- **分类**: q-bio.QM, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.40379v1](https://arxiv.org/pdf/2610.40379v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24 months from 18 months of follow-up. CEDAR (Clinical Evidence-Driven Agent for Risk-prediction), an evidence-citing, self-auditing LLM pipeline, outperformed trained machine learning in both cohorts (pooled area under the receiver operating characteristic curve 0.815 versus 0.656 to 0.700 in T2D and 0.756 versus 0.603 to 0.631 in T1D), most on the sparsely screened outcomes. Only 4 of 70,246 values it cited did not match the chart. Reading only the evidence and reasoning cited by CEDAR, two pediatric endocrinologists reached the same prediction as CEDAR in about nine of ten cases, agreeing with each other on 90.5%.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7aa3459e-aefc-4

---

### 4. Factorized Representations of Concurrent Temporal Variables in Pretrained Language Models

- **ArXiv ID**: [2610.40328v1](https://arxiv.org/abs/2610.40328v1)
- **作者**: Xinhe Zhang, Arnau Marin-Llobet
- **发布时间**: 2026-10-29
- **分类**: cs.LG, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.40328v1](https://arxiv.org/pdf/2610.40328v1)
- **相关度评分**: 10/10

#### 英文摘要

Language models often need to maintain multiple contextual variables that evolve independently within a document. Prior work has identified structured representations of individual temporal or contextual quantities, but their joint organization remains less understood. We study this question using controlled documents with independently phased language-switch and topic-change timers. Across ten pretrained checkpoints, both timers are linearly decodable from the same hidden states. Removing a timer-associated centroid plane substantially reduces access to its associated variable while having little effect on the concurrent timer, although the planes are nonorthogonal and contain cross-timer information. Separate timer contributions also explain most reproducible variation among joint-state centroids. These signatures persist from 3 to 51 timer values and across Qwen3 checkpoints from 0.6B to 14B. Schedule position affects continuation probabilities, but the tested centroid displacement produces no consistent timer-specific output effect. Together, these results support approximate factorization based on selective accessibility and approximately additive joint-state geometry in overlapping subspaces.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8421e9e9-d85c-4

---

### 5. Elucidating the Design Space of LM Data Attribution

- **ArXiv ID**: [2610.40655v1](https://arxiv.org/abs/2610.40655v1)
- **作者**: Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, David Bau
- **发布时间**: 2026-10-30
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.40655v1](https://arxiv.org/pdf/2610.40655v1)
- **相关度评分**: 10/10

#### 英文摘要

Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled Attribution Benchmark (CATT) for fact tracing, in which we fine-tune LLMs on entirely fictitious knowledge, providing unambiguous ground truth for attribution. This synthetic setup allows us to systematically alter one dataset configuration at a time, such as document redundancy and lexical distractors. With this configurable evaluation, we demonstrate that redundancy and distractors consistently degrade attribution performance. Rather than proposing a new estimator, we examine two design choices that are underexplored: the loss used to compute gradients and how per-token attribution scores are aggregated into a document score. We find that the true causal evidence within a training document is highly localized, but standard methods dilute this evidence into noise by averaging attribution scores across the entire document. We find that replacing standard cross-entropy loss gradients with the negative log-odds gradients surfaces the critical tokens from other uninformative ones. We can then aggregate only the top token scores to improve ground truth recall by 35 to 72 percentage points across multiple baselines on our diagnostic benchmark. The negative log-odds correction also generalizes to FTRACE-TREX, improving counterfactual retraining performance for every method we test, by up to 4.9x.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f7c538e8-0a9b-4

---

### 6. Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation

- **ArXiv ID**: [2610.40409v1](https://arxiv.org/abs/2610.40409v1)
- **作者**: Chenjie Qiu, Zixuan Zeng, Shaobin Shi, Bingfeng Chen, Dongsheng Luo...
- **发布时间**: 2026-10-30
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.40409v1](https://arxiv.org/pdf/2610.40409v1)
- **相关度评分**: 10/10

#### 英文摘要

Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls no language model outperforms graph-based systems and is competitive with a search agent. This training, however, leaves a gap. At test time the retriever conditions on its own retrievals, which soon contain mistakes: by the third step, about half or more of the states it visits hold a wrong passage, and these passages lower its chance of retrieving a missing gold passage well beyond what the difficulty of the states explains. We propose on-policy state training, which trains the encoder on the states it reaches itself. At every epoch the current encoder retrieves chains for the training questions; each state it visits, including those built on its own mistakes, is labeled with the earliest gold passage still missing while the other missing gold passages are masked, so that no correct continuation is penalized; and the encoder is updated contrastively on these states mixed with teacher-forced ones, so that its training distribution follows it as it learns. The resulting retriever retrieves complete evidence more often than teacher-forced training and the systems we compare, and it transfers without further training to harder long-chain variants of HotpotQA and 2WikiMultiHopQA that we construct. On the same states, it recovers from its own mistakes far more often, and controlled comparisons attribute the gain to training on the states the encoder currently reaches.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 85214392-2bc4-4

---

### 7. Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG

- **ArXiv ID**: [2610.40314v1](https://arxiv.org/abs/2610.40314v1)
- **作者**: He Tu, Aleena Bosco Kurumthottam, Torsten Suel
- **发布时间**: 2026-10-29
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.40314v1](https://arxiv.org/pdf/2610.40314v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation (RAG) grounds a language model's output in retrieved evidence, but for complex questions spanning multiple aspects of an information need, relevance-based retrieval may return redundant evidence while leaving some aspects unsupported. We propose a coverage-aware retrieval pipeline that decomposes queries into subquestions, ranks candidates with a coverage-trained bi-encoder, predicts a document\,$\times$\,subquestion coverage matrix with a cross-encoder, and selects documents by greedy maximum-marginal coverage. On TREC RAG 2024, our approach improves $α$-nDCG@10, which rewards newly covered nuggets and discounts redundant evidence, from $0.625$ to $0.702$, approaching the $0.718$ gold-nugget upper bound without sacrificing relevance. We then find that ground-truth oracle retrieval, despite substantially higher retrieval coverage, delivers no more nugget coverage to the answer than our estimated selection. This suggests that answer completeness depends not only on what evidence is retrieved, but also on how effectively the generator uses it. To address this, we introduce a \emph{grounded self-feedback loop} in which the model identifies underused evidence from its first answer and generates again without gold supervision, raising $V_{\mathrm{strict}}$, the fraction of vital reference nuggets fully supported by the answer, by $0.086$ over two passes while largely preserving faithfulness.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2fe6e085-0d61-4

---

### 8. Towards Full-Text Scholarly Argument Mining using Entity-Anchored Claim Extraction

- **ArXiv ID**: [2610.40196v1](https://arxiv.org/abs/2610.40196v1)
- **作者**: Bhuvanesh Verma, Andy Lüking, Mounika Marreddy, Leon Lukas Hammerla, Alexander Mehler
- **发布时间**: 2026-10-29
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.40196v1](https://arxiv.org/pdf/2610.40196v1)
- **相关度评分**: 10/10

#### 英文摘要

Argument mining in full-text scholarly articles remains an important yet challenging task. This difficulty stems not only from the need to model long-distance dependencies but also from the substantial effort required to annotate sentence-level argumentative components throughout lengthy documents. To address these challenges, we introduce a novel approach that leverages scientific entity mentions (e.g., tasks, datasets, and models) to identify and structure claims in scholarly literature. We validate our approach through a case study involving 50 full-text research papers on sentiment analysis. We first establish a reliable human gold standard (Krippendorff's $α= 0.80$), identifying 113 claim-bearing sentences and extracting 199 structured claim records from 300 candidate sentences. To address the annotation bottleneck, we employ a majority-voting ensemble of large language models (LLMs) to generate a silver-standard dataset comprising 1,487 claims. Encoders fine-tuned exclusively on the silver-standard dataset outperform those trained on a small human-annotated gold-standard dataset and demonstrate strong zero-shot transfer to NLP papers outside the training corpus.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8d9fc1c6-6344-4

---

### 9. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates

- **ArXiv ID**: [2610.40516v1](https://arxiv.org/abs/2610.40516v1)
- **作者**: Max Neuwinger, Hanna Yukhymenko, Imanol Schlag
- **发布时间**: 2026-10-30
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.40516v1](https://arxiv.org/pdf/2610.40516v1)
- **相关度评分**: 10/10

#### 英文摘要

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual refusal and benign corpora, extracting safe templates from harmful prompts, translating them and then filling in the slots with culturally authentic entities, both harmful and benign. As a result, we release MSafeTemp, a validated corpus spanning 60 languages useful for multilingual safety alignment and evaluation. Using the dataset, we show that English-only evaluation misjudges multilingual safety: for several models, attacks that fail in English succeed once translated, while culturally localized variants expose further failures that translation alone misses. We also confirm that augmenting safety training data through templates allows for higher diversity and quality of alignment, resulting in improved safety performance beyond English. MSafeTemp and the respective pipeline are aimed at facilitating research and development of safer and more responsible models for less-represented cultures.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f6b9edcf-6cb4-4

---

### 10. Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities

- **ArXiv ID**: [2610.39301v1](https://arxiv.org/abs/2610.39301v1)
- **作者**: Yunhang Shen, Zhangquan Chen, Xiaotian Li, Zhongpeng Cai, Qing Zhou...
- **发布时间**: 2026-10-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.39301v1](https://arxiv.org/pdf/2610.39301v1)
- **相关度评分**: 10/10

#### 英文摘要

We present Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio, and video into structured records grounded in space and time, providing a perception layer for agents that read, locate, and cite evidence across modalities. Its design rests on one encoder for every modality and one schema for every task. Youtu-Omni-Encoder, initialized from a pre-trained language model to strengthen text reading, encodes all modalities with shared weights in a unified space-time coordinate system, and a few fusion layers let video frames attend to concurrent audio, bringing cross-modal fusion and temporal alignment into perception itself. OmniSchema unifies the outputs of all ten parsing tasks, allowing a single self-evolving post-training procedure, OmniSchema-Aware On-Policy Distillation (OSAD), to provide a shared token-role-based objective across tasks. In each round, the model is trained on its own rollouts against token-level targets from a reference-conditioned copy of itself, which is then refreshed with the trained weights, so that the parser and its supervision co-evolve. With a single 5 B-parameter checkpoint, Youtu-Parsing-Omni achieves state-of-the-art performance on OmniDocBench v1.6 (96.96 Overall) and leads all open-weight models on OmniParsingBench (75.08 Avg.), with its advantage concentrated on audio and video. It also achieves the best overall chart-parsing score (95.02) and the highest exact chemical-fingerprint agreement among compared systems, and matches a dedicated optical-music model in character-level transcription of typeset sheet music while staying far ahead of general-purpose systems. Code and model weights are publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 76ca180e-9493-4

---

### 11. Micro-Edits: Computational Support for Fine-Scale Edits in Film

- **ArXiv ID**: [2610.40653v1](https://arxiv.org/abs/2610.40653v1)
- **作者**: Nhan Tran, Hijung Valentina Shin, Abe Davis, Mackenzie Leake
- **发布时间**: 2026-10-30
- **分类**: cs.HC, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.40653v1](https://arxiv.org/pdf/2610.40653v1)
- **相关度评分**: 10/10

#### 英文摘要

In film editing, every frame matters. While macro, content-level edits shape the high-level narrative of a film, small local edits often control timing and direct visual attention. For example, editors can adjust the precise timing of clips to control the length of a meaningful silence, or cut to shots that highlight a specific character's reactions to important moments. These small, detailed edits are slow and tedious to make in standard editing tools because users have to map high-level narrative goals to low-level frame-by-frame adjustments. At the same time, these fine-scale adjustments, which we call micro-edits, can be nuanced and expressive, with different choices serving different creative goals. In this work, we start by conducting a formative study with professional editors to understand the structure of micro-edits and how they are used. We then derive a mathematical formalization for this structure to develop tools that leverage AI and optimization to make exploring micro-edits simpler and more efficient for users. Finally, we validate our tools in multiple user studies and a wide range of video examples.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e2b42ab1-a14c-4

---

### 12. Rethinking Neural Thickets Without Weight Perturbations

- **ArXiv ID**: [2610.40649v1](https://arxiv.org/abs/2610.40649v1)
- **作者**: Nicolas Dufour, Elouan Gardès, Amil Dravid, Patrick Pérez, Loic Landrieu
- **发布时间**: 2026-10-30
- **分类**: cs.LG, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.40649v1](https://arxiv.org/pdf/2610.40649v1)
- **相关度评分**: 10/10

#### 英文摘要

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions. This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits with a fully frozen model, providing a simple, training-free alternative to full-weight perturbation ensembles across language and vision.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 34ec453e-a31a-4

---

### 13. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

- **ArXiv ID**: [2610.40647v1](https://arxiv.org/abs/2610.40647v1)
- **作者**: Jiongfan Yang, Weichen Fan, Haiwen Diao, Zhongang Cai, Ziwei Liu
- **发布时间**: 2026-10-30
- **分类**: cs.CV, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.40647v1](https://arxiv.org/pdf/2610.40647v1)
- **相关度评分**: 10/10

#### 英文摘要

Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length of the global attention sequence. SpecSlot expands each spatial anchor into multiple slots, each assigned a disjoint band of DCT coefficients; this separates anchor density from spectral subdivision. Only the lowest-frequency slot from each anchor participates in global attention, while all slots interact locally. This allows the model to increase spectral detail without enlarging the global sequence. A spatial head further adds a local correction to the spectral prediction, while the generative state, target, and loss remain in pixel space. On ImageNet-256, SpecSlot achieves a comparable final FID to a FLOPs-matched JiT control while converging faster. On ImageNet-512, it improves FID by 2.84 over the control with 3.9% fewer FLOPs, and comes within only 0.69 FID of JiT-B/16 at 38.2% lower cost. On text-to-image generation, SpecSlot surpasses JiT-B/8 on DPG-Bench by 1.06 at 40.6% lower forward cost.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: df9f1f74-5450-4

---

### 14. Luggage re-identification: A study of strategies towards a real-world application

- **ArXiv ID**: [2610.40643v1](https://arxiv.org/abs/2610.40643v1)
- **作者**: Quentin Dhôte, Romaric Audigier
- **发布时间**: 2026-10-30
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.40643v1](https://arxiv.org/pdf/2610.40643v1)
- **相关度评分**: 10/10

#### 英文摘要

Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (lost luggage recovery). It enables the association of observations of the same luggage across disjoint camera views in complex environments such as airports, train stations and border crossing. While existing approaches primarily focus on appearance-based cropped image matching under relatively clean conditions, real-world scenarios are characterized by frequent occlusions, cluttered background and crowded scenes which significantly degrade performance. Yet, strategies leveraging the complementarity of multiple shots and views from different video streams is overlooked. In this paper, we study strategies for an end-to-end pipeline that operates from multiple video streams to detect and re-identify luggage. We evaluate different variants on a benchmark dataset acquired in real-world environments to address the questions of selecting and merging different views and shots of the same luggage as well as training on different environment datasets for an overall ReID performance improvement in practical applications.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b183deff-e0d7-4

---

### 15. Probing Spatial State Representations in Visual Foundation Models

- **ArXiv ID**: [2610.40636v1](https://arxiv.org/abs/2610.40636v1)
- **作者**: Baiqiao Yin, Zhongang Cai, Ruisi Wang, Qiwei Liang, Lei Yang...
- **发布时间**: 2026-10-30
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.40636v1](https://arxiv.org/pdf/2610.40636v1)
- **相关度评分**: 10/10

#### 英文摘要

An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through four levels of spatial capability---spatial structure, object persistence, predictive spatial update, and actionability---using frozen-feature probes on ten representations under streaming egocentric observations of static indoor environments. The resulting capability profiles vary across tasks, network layers, and prefix lengths: strong readout of the visible scene does not ensure accurate object persistence or future-feature retrieval. Matched controls separate readout accuracy from reliance on visual history and motion. Native future prediction retains recoverable spatial structure, but a spatial reader trained on real features does not transfer to predicted features unchanged. Finally, goal-dependent candidate selection does not establish reliable continuous action utility: predicted actions respond to goal changes, yet supplying the correct goal does not reliably improve progress. Across the four levels, object persistence and actionability build on camera-pose readout, whereas feature prediction builds on visible-scene readout. Together, these findings motivate evaluating spatial representations not only by what can be decoded from them, but by whether that information is maintained beyond observation, updated predictively, and used for goal-directed action.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f4d97739-5ebc-4

---
