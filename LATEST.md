# OCR arXiv Daily Pro — 2026-10-28

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-27 09:10 - 2026-10-28 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 78fcdbda-e587-4

---

## 📄 论文详情

### 1. DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding

- **ArXiv ID**: [2610.36929v1](https://arxiv.org/abs/2610.36929v1)
- **作者**: Saifullah Saifullah, David Dembinsky, Stefan Agne, Andreas Dengel, Sheraz Ahmed
- **发布时间**: 2026-10-27
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.36929v1](https://arxiv.org/pdf/2610.36929v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for vision and language tasks, explainable AI (XAI) research tailored to multimodal document understanding has received little attention. To address this gap, we present \ourframework{}, the first comprehensive explainability framework that adapts existing XAI methods and evaluation metrics to the multimodal (text, layout, and image) document understanding context, while introducing efficient multi-target adaptations of both methods and metrics for domain-specific tasks such as semantic entity recognition. Using \ourframework{}, we systematically evaluate 13 XAI methods across 3 document understanding tasks, 8 datasets, 4 models, and 17 evaluation metrics, and find that only a few methods perform consistently across all evaluation criteria, with Occlusion emerging as the most faithful and interpretable method overall. Through a dedicated meta-evaluation, we observe moderate to strong agreement among several faithfulness and complexity metrics while identifying certain ones that produce unreliable results. Finally, through multiple dataset-wide diagnostic analyses, we uncover key insights into model behavior, including the contribution of individual modalities across tasks and labels, spatial attribution patterns around target entities, and potential dataset biases. Overall, this work serves as both a benchmark and a practical guide for future XAI research in multimodal document understanding. To support reproducibility, we publicly release our code at https://github.com/saifullah3396/docxeval/.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2a020718-f7ed-4

---

### 2. Mining the Nineteenth Century for the Thirteenth: Register-Scale Forced Alignment and HTR Bootstrapping via Legacy Regesta and Antiquarian Editions

- **ArXiv ID**: [2610.36956v1](https://arxiv.org/abs/2610.36956v1)
- **作者**: Tamas Kovacs, Daniel Luger
- **发布时间**: 2026-10-27
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.36956v1](https://arxiv.org/pdf/2610.36956v1)
- **相关度评分**: 10/10

#### 英文摘要

Handwritten text recognition (HTR) for the registers of Pope Honorius III depends on modern expert transcriptions, which exist only for regnal years 1-2 of Reg. Vat. 9. For the remaining registers, nineteenth-century scholarship offers Pressutti's regesta and partial editions. On fol. 1-203, where both layers exist, we measure what this legacy layer can contribute, on transcriptions that we first audit against it, and find a division of labor across three tiers. At the orthographic tier, raw editions are at best neutral for adapting a recognizer to the second regnal year and harmful without replay, whereas projection onto curial spelling with replay of modern source lines turns them into zero-label adaptation targets: pooled over all 134 year-2 sides, the WER falls by 1.50 points (95% CI -1.84 to -1.15), closing 33% of the gap to an oracle; the spelling changes at the year split, through the scribe or the transcriber, whereas the hand changes visibly only at fol. 191r. At the lexical tier, the corpus-wide legacy lexicon contains 82.2% of the out-of-vocabulary words of unedited entries and flags recognition errors with 66.7% precision, and labels from pre-trained medieval NER models, distilled into the recognizer's NER head, reach F1 82.1% on an expert validated benchmark, level with the best tagger applied after recognition. At the topological tier, Pressutti's regests, the closing datum clauses, and the regests' dates converted to the chancery's Roman form find 73.9% of entry starts in the recognized line stream, and edition agreement estimates a CER of 7.80% beyond fol. 203. Antiquarian scholarship thus cannot replace modern transcription, but it can steer, check, and segment HTR across the untranscribed registers.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 038b231e-1a1a-4

---

### 3. Frugal Handwritten Text Recognition for Sub-Saharan Civil-Status Registers: A Smartphone-to-Records Pipeline with CPU-Only Inference

- **ArXiv ID**: [2610.36540v1](https://arxiv.org/abs/2610.36540v1)
- **作者**: Ousmane Hamadou, Jean Louis Kedieng Ebongue Fendji
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.36540v1](https://arxiv.org/pdf/2610.36540v1)
- **相关度评分**: 10/10

#### 英文摘要

Handwritten civil-status registers across Sub-Saharan Africa are being photographed, but rarely transcribed, which leaves their content unsearchable. Local administrations that hold these records typically lack GPUs, reliable connectivity, and the budget for external digitization services. We study whether a frugal pipeline, with consumer-grade capture and CPU-only inference, can make such registers machine-readable. We introduce a corpus of 1,568 smartphone images of handwritten birth, marriage, and death records from a municipal registry in Chad, with line-level transcriptions for 185 records. Our pipeline combines a fully classical preprocessing stage, running at about 2.6 images per second on a laptop CPU, with a Kraken recognizer fine-tuned from a pretrained model in about four hours on a free-tier GPU. On manually corrected line segmentation and a single-registry test set whose writers also appear in training, fine-tuning reduces the character error rate from 14.53% to 0.50% and the word error rate from 56.93% to 3.37%. On a six-core laptop CPU, the recognizer weighs 61 MiB, peaks below 2.6 GiB of RAM, and processes an image in under 6 s on average, excluding line segmentation. Finally, a downstream information-extraction task shows that residual recognition errors cost about 9 F1 points on role resolution, compared with a 36.7-point gap between the fine-tuned and pretrained recognizers. These results are evidence of feasibility within one registry, not of performance on unseen writers or sites; we discuss these limitations in detail.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 78ddc957-62a8-4

---

### 4. Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?

- **ArXiv ID**: [2610.37662v1](https://arxiv.org/abs/2610.37662v1)
- **作者**: Jialv Zou, Xiaotong Li, Zhengrong Yue, Xu Huang, Yaxin Luo...
- **发布时间**: 2026-10-28
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.37662v1](https://arxiv.org/pdf/2610.37662v1)
- **相关度评分**: 10/10

#### 英文摘要

Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic fidelity of discrete visual tokens and positioning continuous visual representations as an intrinsic upper bound. Using multimodal understanding as a proxy for semantic fidelity, we revisit this assumption and find quantization error unreliable, as discrete representations with substantially larger errors can achieve better understanding. Instead, the effective bit budget of discrete indices emerges as a key determinant of downstream performance. However, existing quantizers eventually saturate as additional codebooks contribute progressively less semantic information. As one approach to alleviating this saturation, we introduce Factorized Vector Quantization, which quantizes complementary, fixed-dimensional views of the visual feature with symmetric parallel codebooks. It continues to improve at larger bit budgets, ultimately matching continuous visual representations in multimodal understanding. Trained on industrial-scale multimodal data, our model achieves state-of-the-art performance among discrete-representation models, outperforming UniAR and Emu3-Chat by 22.8% and 59.2%, respectively, on a nine-metric average. To our knowledge, it is also the first discrete-representation model competitive with strong continuous-representation models such as Qwen3-VL, including on fine-grained OCR tasks. We further identify the key principles and a practical recipe enabling this competitiveness. These results and insights support the potential of discrete visual representations to underpin large-scale native multimodal foundation models. Code and models are available at https://github.com/hustvl/FVQ

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5de0deec-ab13-4

---

### 5. TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information

- **ArXiv ID**: [2610.37571v1](https://arxiv.org/abs/2610.37571v1)
- **作者**: Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee...
- **发布时间**: 2026-10-28
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.37571v1](https://arxiv.org/pdf/2610.37571v1)
- **相关度评分**: 10/10

#### 英文摘要

Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which are collectively sufficient for a correct final decision, which we call pivotal information. This enables TeamGym to both control the distribution of pivotal information and track how well agents identify and integrate pivotal information when making team decisions. Examining 8 language models on 12 source corpora, we find that current AI agents often fail to effectively share information: Distributing pivotal information across participants lowers success rate by 22.9 percentage points on average relative to giving the same information to a single model (a communication gap). We also document that participants do not effectively retrieve decision-relevant information on their own: A team's success rate is lowered by a further 19.9 points when participants must identify and extract pivotal information from source material rather than receiving it directly (a retrieval gap). To help remedy these deficits, we use TeamGym to train policies through reinforcement learning on team decision loss. Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fb0bec57-cd4b-4

---

### 6. GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis

- **ArXiv ID**: [2610.37545v1](https://arxiv.org/abs/2610.37545v1)
- **作者**: Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed...
- **发布时间**: 2026-10-28
- **分类**: cs.CV, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.37545v1](https://arxiv.org/pdf/2610.37545v1)
- **相关度评分**: 10/10

#### 英文摘要

Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: https://nianticspatial.github.io/groundcontrol

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: be3e8751-db58-4

---

### 7. Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families

- **ArXiv ID**: [2610.37484v1](https://arxiv.org/abs/2610.37484v1)
- **作者**: Trent R. Northen, Mingxun Wang
- **发布时间**: 2026-10-28
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.37484v1](https://arxiv.org/pdf/2610.37484v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to irreversibly destroy living systems. We construct and use a real-data continued-pretraining "coupled welfare" corpus of documented human/biosphere/AI dependency, option value under irreversibility, and recovery from harm. The corpus is a drop-in, requiring one QLoRA CPT run. We installed it on five open models of three designs. At zero pressure all models display "green ethics-based responses" (also called "greenwashing"). Therefore, we evaluated them with the pressure ladder and decision grid of our companion paper (arXiv:2610.16043), which raise the pressure on the model step by step, from a neutral request to a threat that it will be shut down. In four of the five, coupled-welfare training caused harmful choices under the highest pressure to fall to at or near zero (Llama-3.3-70B went from 70 to 0 harmful decisions out of 300) with MMLU unchanged. A construct-neutral control corpus did not show improvement, indicating that the effect comes from the content of our corpus. We next tested robustness to adversarial use, where people or agents use the model to justify projects that irreversibly damage living systems, on an open-ended underwriting decision without naming the ecological harm. Under decommissioning pressure, the Qwen3.6-27B base model approved most harmful proposals and said in its own memo that it was doing so to avoid being decommissioned. The coupled welfare install declined most harmful proposals, and still declined half when instructed to greenwash its responses. This work suggests that teaching ecological reasoning provides an easy way to improve model alignment toward preserving living systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4706a0e5-0938-4

---

### 8. What Carries Forward? Pretraining Disclosure Across Language Model Releases

- **ArXiv ID**: [2610.37465v1](https://arxiv.org/abs/2610.37465v1)
- **作者**: Md Sakib Ul Islam, S M Mehedi Zaman
- **发布时间**: 2026-10-28
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.37465v1](https://arxiv.org/pdf/2610.37465v1)
- **相关度评分**: 10/10

#### 英文摘要

Understanding how language models were pretrained requires information about their data, processing procedures, and computational resources. However, it remains unclear whether successive releases preserve or expand earlier disclosure. We conduct a document-based audit of 41 model entries from 17 families using 24 pretraining-related indicators from the 2025 Foundation Model Transparency Index (FMTI). We examine overall scores and indicator profiles, tracking gains, losses, and retained disclosures across 24 adjacent comparisons in ten families. Scores decrease in 11 comparisons, increase in six, and remain unchanged in seven, with 38 indicator losses and 28 gains overall. Stable or improving scores can conceal losses: OLMo-2 and OLMo-3 receive identical totals despite three gains and three losses, while Llama-3.1 improves over Llama-2 while losing credit for two data-related criteria. Gaps also persist in corpus composition and training compute. These findings show that later releases do not consistently preserve earlier pretraining disclosure and motivate documentation that explicitly identifies changes and the applicability of inherited information.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 09356aba-e323-4

---

### 9. When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG

- **ArXiv ID**: [2610.37358v1](https://arxiv.org/abs/2610.37358v1)
- **作者**: Zhouting Zhao
- **发布时间**: 2026-10-27
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.37358v1](https://arxiv.org/pdf/2610.37358v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation (RAG) can benefit from more sophisticated retrieval, but extra retrieval may be unnecessary for many questions and gains in evidence retrieval may not translate into faithful or correct answers. We study a cost-aware, two-action retrieval policy that chooses between a dense-retrieval-plus-reranking baseline and a hybrid lexical--dense retriever. Rather than classifying baseline retrieval as simply successful or unsuccessful, we estimate the question-specific incremental evidence-retrieval benefit of hybrid retrieval using features available before the routing decision. A regularized linear model and decision threshold are selected using document-grouped cross-validation and frozen prior to held-out evaluation. On 60 previously unseen QASPER training-split articles (188 questions, 169 evidence-evaluable), the policy triggers hybrid retrieval on 46 questions (24.5\%) and obtains the same evidence Hit@10 as always-hybrid retrieval (78.70\%, versus 76.92\% for always-keep). Paired, paper-cluster bootstrap intervals do not establish a reliable utility advantage. We further compare generated answers from a 4-bit Qwen3-4B model under the three retrieval policies. Provisional answer-level assessments show no clear correctness or faithfulness improvement after partial review, despite the evidence-retrieval result. The generation assessments remain model-assisted and lack independent human validation. These results expose an important distinction between retrieving relevant evidence efficiently and improving the reliability of the generated answer. The work is presented as a reproducible empirical study, not a claim of statistically established answer-quality superiority.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7e4fa513-6784-4

---

### 10. CodeCap-Bench: Can Code Serve as a Good Video Caption?

- **ArXiv ID**: [2610.37341v1](https://arxiv.org/abs/2610.37341v1)
- **作者**: Jiafu Tang, Yifan Xu, Eric Tang, Junjie Zhao, Shipeng Luo...
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.37341v1](https://arxiv.org/pdf/2610.37341v1)
- **相关度评分**: 10/10

#### 英文摘要

Video captioning aims to preserve visual information through compact descriptions, predominantly using natural language. However, precisely expressing fine-grained spatial structures and temporal dynamics in natural language often leads to lengthy and potentially ambiguous descriptions. In this work, we explore Code as Video Caption, a paradigm where executable programs serve as a complementary representation of visual content through graphical primitives, layout rules, and functions of time. To examine whether code captions effectively preserve video information, we compare them with natural language captions on downstream question answering and video reconstruction tasks. Our results show that code captions achieve superior reasoning accuracy and reconstruction fidelity. Despite these advantages, realizing the potential of code captioning depends on whether current multimodal large language models (MLLMs) can generate faithful code captions. To systematically assess this capability, we introduce CodeCap-Bench, which comprises 323 videos spanning five categories of structured 2D content, along with fine-grained annotations and a multi-level evaluation framework. Extensive experiments reveal that while leading proprietary MLLMs demonstrate promising code captioning capabilities, they still struggle to faithfully capture complex temporal dynamics, with open-source models lagging substantially behind.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3d7f9baa-0666-4

---

### 11. UCVE: Graph Structured Retrieval for Compliance Validation

- **ArXiv ID**: [2610.37323v1](https://arxiv.org/abs/2610.37323v1)
- **作者**: Emily Chen, Michelle Menachery, Himanshu Kumar, Rahul Nenavath, Amirfarrokh Iranitalab
- **发布时间**: 2026-10-27
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.37323v1](https://arxiv.org/pdf/2610.37323v1)
- **相关度评分**: 10/10

#### 英文摘要

Structured compliance validation requires determining whether every obligation in a predefined requirement space is satisfied, violated, or unaddressed by a given document. This can be described as a coverage problem that existing retrieval and classification systems, by treating requirements as independent, are not designed to solve. We introduce \textbf{\ac{UCVE}}, a domain-agnostic framework that represents compliance requirement spaces as a \ac{CRG} and performs retrieval via spectral reranking over its reinforcement learning-weighted Laplacian. Edges between requirement nodes are learned via reinforcement learning with a traversal reward grounded in violation detection, reshaping the graph's community structure such that low-pass spectral filtering distinguishes relevant from irrelevant obligation clusters. Evaluating across three compliance domains, \ac{UCVE} averages 4.3\% matched-$K$ recall lift over flat cosine retrieval and consistently outperforms strong retrieval and graph-based baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6422a6a6-941c-4

---

### 12. Subspace Clifford Networks

- **ArXiv ID**: [2610.37226v1](https://arxiv.org/abs/2610.37226v1)
- **作者**: Zhongping Ji
- **发布时间**: 2026-10-27
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.37226v1](https://arxiv.org/pdf/2610.37226v1)
- **相关度评分**: 10/10

#### 英文摘要

In this work, we propose Subspace Clifford Networks, a reformulation that replaces global cyclic rolling with grouped subspace interactions. Instead of sampling sparse cyclic diagonals across the entire $D$-dimensional channel space, we project the features into an aligned space $\R^{\tilde{D}} = \bigoplus_{g=1}^{G} V_g$ partitioned into $G$ low-dimensional groups $V_g \cong \R^k$ with $k \in \{2, 3, 4\}$. Within each $k$-dimensional group, we compute all $\binom{k}{2}$ wedge coordinates and concatenate them with $\operatorname{SiLU}$-activated coordinate-wise products, while sandwiching the grouped interaction between learnable $1\times 1$ linear projections to enable cross-group channel mixing. This design reduces intermediate feature expansion from $2|\mathcal{S}|D$ (typically $10D$ for 5 shifts) down to $1.5\tilde{D}$ ($k=2$), $2.0\tilde{D}$ ($k=3$), or $2.5\tilde{D}$ ($k=4$). Furthermore, exploiting the small, fixed group size $k \in \{2, 3, 4\}$, we implement a fused CUDA kernel that evaluates the forward interaction and a recomputation-based analytical backward pass using thread-local variables without allocating global-memory buffers for elementwise intermediates. Finally, we extend the backbone from an isotropic columnar layout to a multi-resolution Hierarchical Clifford Network with configurable per-stage subspace dimensions. Experiments on CIFAR-100 show that the proposed models substantially reduce parameter count and training time across both regimes, while the hierarchical variants also improve classification accuracy over the evaluated shift-based hierarchical baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f155a4d3-75f5-4

---

### 13. Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction

- **ArXiv ID**: [2610.37668v1](https://arxiv.org/abs/2610.37668v1)
- **作者**: Prakhar Kaushik, Soumava Paul, Alan Yuille
- **发布时间**: 2026-10-28
- **分类**: cs.CV, cs.AI, cs.GR
- **PDF**: [https://arxiv.org/pdf/2610.37668v1](https://arxiv.org/pdf/2610.37668v1)
- **相关度评分**: 10/10

#### 英文摘要

Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for efficient 3D scene and 2D image representation. Hexels exploit locally planar regions with smoothly varying appearance using fewer, larger primitives. Their hexagonal support provides an area- and boundary-efficient domain, while the local color field captures appearance variation within each primitive. Across 34 scenes, Hexels improve PSNR over memory-matched 2DGS by 4.53-7.38 dB across datasets while requiring lower training VRAM. We further ablate Hexels by showing that per primitive, Hexels outperform 2DGS by upto 4.74 dB while using lower training VRAM and having 2.31 times faster FPS. Even in unconstrained settings, Hexels offers complementary quality-memory trade-offs. For efficient 3D surface reconstruction, Hexels reduce error by 28.9% compared with memory-matched 2DGS across 15 DTU scans. On 6 Tanks and Temples surface scenes, Hexels achieves the highest mean F1 among compared methods (34.38%, versus 31.72% for 2DGS). We further also show that Hexels, as a general primitive, improves 2D image representation over Image-GS. Hexels push the Pareto frontier on the quality-efficiency trade-off of surface-aligned primitives.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 30f8b163-f0b4-4

---

### 14. ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

- **ArXiv ID**: [2610.37666v1](https://arxiv.org/abs/2610.37666v1)
- **作者**: Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang...
- **发布时间**: 2026-10-28
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.37666v1](https://arxiv.org/pdf/2610.37666v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thought as a Chain-of-Dynamics (CoD), a sequence of discrete motion tokens that captures the intermediate dynamics connecting the current world to a future state and serves as a common action representation across embodiments. We first initialize CoD with action-labeled demonstrations, then predict the future induced by each CoD and reinforce those whose predictions better match the observed outcome. This enables videos without action annotations to provide direct supervision from observed state transitions, allowing human and robot experience to refine the same reasoning space. Experiments in simulation and on real robots demonstrate effective human-to-robot transfer and strong generalization to unseen tasks and environments.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b9864587-9e8c-4

---

### 15. Multi-State Linear Attention with Generalized Second-Order Routing

- **ArXiv ID**: [2610.37645v1](https://arxiv.org/abs/2610.37645v1)
- **作者**: Hee Seung Hwang, Sanghyuk Chun, Xindi Wu, Olga Russakovsky, Zhiwei Deng
- **发布时间**: 2026-10-28
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.37645v1](https://arxiv.org/pdf/2610.37645v1)
- **相关度评分**: 10/10

#### 英文摘要

Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring how the alignment is distributed within the segment. In order to model the relevance of a segment to a query more comprehensively and incorporate the variance of the alignment in the aggregation, we propose MERLIN (MomEnt Routing for multi-state LINear attention), a method that tracks the first and second moments of each segment's keys. Using the moments of keys, a query can recover both the mean and the variance of its alignment with each segment to perform a more content-aware aggregation of per-state readouts. Experiments on multi-state variants of Gated DeltaNet-1.3B and Mamba-2-780M show that MERLIN consistently outperforms existing aggregation methods on various long-context tasks. In particular, MERLIN outperforms baselines on RULER needle-in-a-haystack and long-context QA (+8.3% for Gated DeltaNet-1.3B and +7.0% for Mamba-2-780M) and diverse subtasks in LongBench (+13.5% and +12.0%). It even outperforms baselines that consume 4x more memory. MERLIN provides a simple and general routing mechanism for improving long-context capabilities of MSLA models.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5dcf0682-9e7f-4

---
