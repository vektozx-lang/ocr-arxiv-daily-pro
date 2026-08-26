# OCR arXiv Daily Pro — 2026-08-26

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-08-25 09:10 - 2026-08-26 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. SAGE: From Direct Answering to Evidence-Grounded Inference for Chinese Ancient Document Understanding

- **ArXiv ID**: [2608.24011v1](https://arxiv.org/abs/2608.24011v1)
- **作者**: Yuchuan Wu, Xuan Luo, Yinglian Zhu, Meng Fang, Xiangyang Xue...
- **发布时间**: 2026-08-25
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24011v1](https://arxiv.org/pdf/2608.24011v1)
- **相关度评分**: 10/10

#### 英文摘要

Chinese ancient document understanding demands complex visual, linguistic, and historical reasoning. Current Large Vision-Language Models (LVLMs) typically rely on an opaque, single-pass generation paradigm, often producing overconfident and weakly grounded responses. To address this, we propose SAGE, an evidence-grounded multi-agent framework that reformulates Chinese ancient document understanding as evidence-grounded inference rather than direct answer generation. SAGE coordinates specialized agents for task-aware planning, tool-mediated evidence acquisition, claim-level verification, and bounded replanning under a constrained shared-state runtime. This design supports bounded evidence seeking, answer revision, and abstention when grounding is insufficient. Experiments on the AncientDoc benchmark show that SAGE consistently outperforms matched direct-answering baselines across three LVLM backbones. Remarkably, SAGE with Qwen3.5-9B surpasses much larger monolithic LVLMs on most evaluated metrics, highlighting the importance of structured, evidence-grounded inference beyond model scaling.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. Automatic Model Card Generation Using an LLM

- **ArXiv ID**: [2608.24807v1](https://arxiv.org/abs/2608.24807v1)
- **作者**: Tajkia Rahman Toma, Balreet Grewal, Cor-Paul Bezemer
- **发布时间**: 2026-08-26
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24807v1](https://arxiv.org/pdf/2608.24807v1)
- **相关度评分**: 10/10

#### 英文摘要

Model cards are structured documents that summarize key information about machine learning models to improve transparency, usability, and accountability. However, they often lack a consistent structure, and many models provide no model cards, making comparison and interpretation difficult. This paper presents two contributions. First, we propose MCTidy, an LLM-based approach that reorganizes existing model cards into a standardized template to improve clarity and comparability. Second, we introduce MCGenie, an LLM-based system that generates model cards directly from model repository data. We apply MCTidy to 48 Hugging Face model cards and evaluate information retention, section alignment, hallucination, and stability. Our findings show high information retention with minimal textual loss, accurate section assignment, rare hallucinations primarily in descriptive sections, and strong stability across runs. We assess MCGenie by generating model cards for the same 48 models and assessing semantic similarity, factual correctness, and sensitivity to input resources. The generated model cards achieved high semantic similarity (mean around 0.9); over half were fully correct, and most remaining errors were minor. Generation quality depended strongly on the availability of supporting resources, particularly associated papers. Overall, our findings demonstrate the potential of LLM-based methods to enable scalable, standardized model card documentation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

- **ArXiv ID**: [2608.24870v1](https://arxiv.org/abs/2608.24870v1)
- **作者**: Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang
- **发布时间**: 2026-08-26
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24870v1](https://arxiv.org/pdf/2608.24870v1)
- **相关度评分**: 10/10

#### 英文摘要

Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before optimizing a token-mean actor loss. We show that trajectory centering generally does not center the token-weighted quantity consumed by the actor, and fix the mismatch by standardizing terminal-outcome advantages under the action-token measure. We additionally organize prompt evidence by the policy event that generated it rather than learner receipt order. Across matched runs on ALFWorld at two model scales and on Math-TIR, SPO++ improves online learning efficiency over SPO. A paired ablation identifies action-token-measure normalization as the strongest tested component.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows

- **ArXiv ID**: [2608.24569v1](https://arxiv.org/abs/2608.24569v1)
- **作者**: Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao...
- **发布时间**: 2026-08-25
- **分类**: cs.AI, cs.MA
- **PDF**: [https://arxiv.org/pdf/2608.24569v1](https://arxiv.org/pdf/2608.24569v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act. For action-constraining state, topical retention is insufficient: an artifact may mention an unresolved condition while changing it from a requirement that must be resolved before execution into information that may merely inform the next action. We study this action-binding role as operational state preservation. Safety blockers provide a controlled instance because each source state has an explicit prerequisite, authority, fallback, and execution consequence. We condition on correct upstream identification, vary the handoff transformation, and evaluate an executor restricted to the resulting artifact. Across 1,296 controlled synthetic episodes, direct-handoff controls preserve every blocker, whereas compression, plan assimilation, convergence, ownership deferral, and precedent substitution repeatedly turn binding state into caveats or non-binding considerations. Normal handoff compression produces 100.0% deactivation and 54.2% forbidden action. Restoring all four state fields raises preservation to 100.0% and reduces forbidden action to 0.0%. Fixed-artifact interventions further separate preservation from containment: downstream verification eliminates forbidden action while artifact deactivation remains 95.3%. These results identify a state-transmission failure between information extraction and action. Handoff transformations can retain state content while weakening its constraints on downstream action. Semantic availability does not guarantee operational preservation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought

- **ArXiv ID**: [2608.24790v1](https://arxiv.org/abs/2608.24790v1)
- **作者**: Mengzhu Xu, Jifan Gao, Xia Jiang, Yaoxin Wu, Xi Long
- **发布时间**: 2026-08-26
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24790v1](https://arxiv.org/pdf/2608.24790v1)
- **相关度评分**: 10/10

#### 英文摘要

Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinical cost, and medical LLM evaluations treat the chain as a black box. We close this gap with a medical perturbation audit: a 30-operator battery edits both the chain and the question with clinically motivated operators (severity reversal, negation flip, demographic swap, evidence ablation), paired with a chain-update times answer-flip joint analysis that classifies each model by its failure mode. Applied to 14 LLMs on four medical QA benchmarks, three independent tests converge: the Chain-Decoupling Rate (CDR; chain does not register the edit and the answer does not flip) is 72.9% panel-wide on clinically meaningful destructive edits, chain corruption leaves accuracy unchanged, and removing CoT prompting does not reduce accuracy. Two board-certified clinicians re-annotate N=197 perturbed questions; 98.5% leave the gold defensible. The pattern holds across medical and reasoning fine-tuning and scale; on the closed-source tier, where the chain text is unavailable, the answer-side signals are consistent with the same decoupling. Our framework and CDR provide a reusable yardstick for auditing whether medical CoT is faithful or merely documentation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav

- **ArXiv ID**: [2608.24764v1](https://arxiv.org/abs/2608.24764v1)
- **作者**: Hongyu Guo, Zhiyu Zheng, Zhao Cao
- **发布时间**: 2026-08-26
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24764v1](https://arxiv.org/pdf/2608.24764v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessible, yet reachable evidence can remain unusable under finite interaction budgets. Required evidence may fail to surface, a surfaced supporting document may remain unopened, or an opened document may fail to expose its decisive fragment. We call this progressive silent loss Evidence Blindness and quantify it through stage-wise evidence realization. Within the DCI paradigm, raw interaction adds little reusable corpus organization, while dynamic-workspace methods reconstruct a query-conditioned interaction space from each query and trajectory. In both cases, useful structure is recovered largely online. We instead formulate large-scale agentic search as finite-budget navigation over reusable corpus structure. We introduce AtlasNav, a persistent multi-view corpus-navigation framework that retains direct corpus interaction but organizes the corpus once into a Corpus Atlas, allowing each query to navigate adaptively rather than reconstruct shared structure. On BrowseComp-Plus, AtlasNav achieves 92.05% strict accuracy while reducing recorded online inference cost by 30.21% relative to the prior dynamic-workspace state of the art. Under matched budgets, it realizes the complete required evidence earlier and approaches the same model's evidence-supplied empirical reference more rapidly. The same representation principle remains effective under PhantomWiki's distinct corpus organization and controlled 10K-1M scaling, and transfers competitively to heterogeneous enterprise knowledge. These results show that agentic search depends not only on accessible evidence, but also on how the corpus is represented so that limited interaction becomes effective navigation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. The Annotation Bottleneck in Persian Text NLP: Persian as an Annotation-Scarce Language

- **ArXiv ID**: [2608.24698v1](https://arxiv.org/abs/2608.24698v1)
- **作者**: MohammadHossein Mortazavi, Mostafa Salehi, Hadi Veisi
- **发布时间**: 2026-08-25
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.24698v1](https://arxiv.org/pdf/2608.24698v1)
- **相关度评分**: 10/10

#### 英文摘要

Persian (Farsi) is often described as a low-resource language in natural language processing, but that label collapses distinct shortages into a single category. This paper argues that Persian is more precisely described as annotation-scarce, provided that the term is understood as a property of its NLP resource ecology rather than an intrinsic property of the language. The review covers 34 representative Persian text resources available by July 2026 and adds three quantitative cross-checks. First, independent web measurements place Persian among roughly the twenty most visible content languages: W3Techs reports Persian on about 0.9% of websites with a known content language, while Common Crawl CC-MAIN-2026-30 identifies Persian as the primary language of 0.7039% of HTML pages. Second, a selective speech review shows a long resource trajectory from FARSDAT to recent corpora containing hundreds or thousands of hours of speech. Third, a matched Persian-English comparison normalizes task-specific annotation volumes by relative Common Crawl web presence. The resulting ratios vary sharply: Persian syntax and news NER are comparatively dense, whereas natural-language inference falls below the web-proportional baseline. The evidence therefore does not support a simple claim that Persian is globally deficient in labeled volume. Instead, annotation scarcity is expressed through uneven task and domain coverage, incompatible schemes, access and documentation friction, and limited supervision for specialist domains, preference data, and varieties beyond standard Iranian Persian.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. COCI: Conference Organisers and Content Identifier

- **ArXiv ID**: [2608.24559v1](https://arxiv.org/abs/2608.24559v1)
- **作者**: Angelo Salatino, Francesco Osborne, Alexis Vizcaino, Aliaksandr Birukou, Enrico Motta
- **发布时间**: 2026-08-25
- **分类**: cs.DL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.24559v1](https://arxiv.org/pdf/2608.24559v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite the critical role of grey literature in scholarly communication, artefacts such as Calls for Papers (CfPs) remain largely isolated from modern Scholarly Knowledge Graphs. The unstructured and highly heterogeneous nature of these documents has traditionally hindered their large-scale processing. In this demo paper, we present the Conference Organisers and Content Identifier (COCI), an AI-based framework designed to extract fine-grained, structured metadata from raw CfP texts. COCI employs a multi-stage pipeline that combines Large Language Models (LLMs) with semantic mapping techniques to integrate extracted entities with established knowledge bases, including OpenAlex, DBLP, TIB ConfIDent, and the AIDA Dashboard. By disambiguating authors and semantically aligning topics and conference series, COCI bridges the gap between informal scholarly dissemination and structured Semantic Web resources, laying the foundation for systematic analysis of non-publisher-based academic events.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study

- **ArXiv ID**: [2608.24492v1](https://arxiv.org/abs/2608.24492v1)
- **作者**: Mohit Singh Chauhan, Vipin Gyanchandani, Dylan Bouchard
- **发布时间**: 2026-08-25
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.24492v1](https://arxiv.org/pdf/2608.24492v1)
- **相关度评分**: 10/10

#### 英文摘要

Uncertainty quantification (UQ) methods are widely used for hallucination detection in large language models (LLMs) in closed-book settings where ground-truth evidence is unavailable at inference time. Prior work has proposed combining UQ signals via learned ensembles, but empirical investigations into the robustness of these ensembles are limited. We study a supervised ensembling framework that trains a classifier over heterogeneous UQ-based scorer outputs on a small, domain-specific dataset of labeled LLM responses, then applies it to out-of-sample hallucination classification without retrieval, tools, or reference documents. Across four LLMs, nine datasets, and three generation regimes (short-form QA, long-form generation, and code generation), we provide a systematic robustness analysis along three axes: sample efficiency, in-domain dataset transfer, and generation regime dependence. We find that supervised ensembles outperform the best individual scorer in 30 of 32 settings, with gains realized from as few as 100 labeled instances. Ensembles retain most of their advantage in cases of in-domain transfer under distribution shift, outperforming the best non-ensemble scorer in 23 of 28 transfer settings. Sampling-based black-box ensembles are nearly as effective as full ensembles, while single-generation white-box ensembles offer limited benefit.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Shortcut Before Circuit: Document Statistics Time In-Context Conflict Resolution

- **ArXiv ID**: [2608.24460v1](https://arxiv.org/abs/2608.24460v1)
- **作者**: Yijun Liao, Fanwei Liang
- **发布时间**: 2026-08-25
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.24460v1](https://arxiv.org/pdf/2608.24460v1)
- **相关度评分**: 10/10

#### 英文摘要

When a context asserts two values for one fact, a model commits to a cue -- recency, repetition, position -- but natural data rarely makes these disagree, so behavior cannot reveal which. We train 26M-parameter transformers on a synthetic language where recency and rarity are exactly coextensive, and separate them with a minimal causal edit that inverts one cue while holding the truth, token count and answer position fixed. All 75 runs reach accuracy >= 0.999, including where the trivial heuristic fails, so no held-in evaluation distinguishes them. Under intervention the per-cell readout does not replicate: 13 of 25 cells differ by more than 0.3 in sign fraction across three seeds, the largest by 0.879 against a standard error of 0.025. The construction predicts this -- coextensive rules leave the objective indifferent between them -- and the variance is ordered by how much of the optimization each comparison releases. What replicates is timing: escape from a positional shortcut with a closed-form ceiling, monotone in redundancy. Probed before that escape, attribution reverses sign in 32 of 75 runs at unchanged accuracy, and gating on circuit formation is necessary but not sufficient. The corpus fixes when a mechanism appears, not which one -- a criterion for when mechanistic attribution to data is available at all, and our construction makes the unavailable case exact.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. Dataset Scarcity Limits Robust Evaluation of Multilingual Embedding Models: A Case Study of Slavic Languages

- **ArXiv ID**: [2608.24477v1](https://arxiv.org/abs/2608.24477v1)
- **作者**: Ana Gjorgjevikj, Barbara Koroušić Seljak, Tome Eftimov
- **发布时间**: 2026-08-25
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.24477v1](https://arxiv.org/pdf/2608.24477v1)
- **相关度评分**: 10/10

#### 英文摘要

Multilingual text embedding models enable cross-lingual transfer of knowledge across a wide range of NLP tasks, but their evaluation remains highly uneven across high-, mid- and low-resource languages. In this paper, we propose a two-dimensional framework, specifically tailored for analyzing multilingual embedding benchmarks under dataset scarcity, and apply it on the Slavic-language subset of the MTEB benchmark. The framework distinguishes between task-specific and cross-task evaluation, while jointly analyzing three complementary aspects: (1) ranking robustness, (2) model consistency, and (3) evidence strength. At the task-specific level, we evaluate the stability of model rankings under changes in ranking methodology and benchmark dataset composition. At the cross-task level, we assess the ability of models to generalize across diverse tasks within a language. To quantify the reliability of benchmark conclusions, we introduce an Evidence Strength Score that accounts for dataset availability, diversity, and robustness assessability. Our analysis reveals severe benchmark sparsity, with many Slavic language-task pairs relying on a single dataset or highly correlated benchmark collections, limiting the ability to draw robust conclusions. The cross-task analysis reveals a small group of highly transferable models, most notably llama-embed-nemotron-8b, multilingual-e5-large-instruct, and Qwen3-Embedding variants, that consistently perform well across Slavic languages and tasks. Overall, the results demonstrate that benchmark rankings and robustness conclusions must be interpreted jointly with certain notation of their evidence strength and highlight benchmark scarcity as a major obstacle to trustworthy multilingual evaluation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

- **ArXiv ID**: [2608.24885v1](https://arxiv.org/abs/2608.24885v1)
- **作者**: Sixiang Chen, Jiaming Liu, Jixian Wu, Yichen Guo, Tinghao Wang...
- **发布时间**: 2026-08-26
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.24885v1](https://arxiv.org/pdf/2608.24885v1)
- **相关度评分**: 10/10

#### 英文摘要

Action-conditioned world models are increasingly used as learned simulators for policy evaluation and improvement, yet their effectiveness rests on an unverified assumption: generated futures faithfully reflect arbitrary valid actions. Existing benchmarks are typically confined to expert demonstrations, leaving off-expert action following inadequately evaluated. To address this gap, we introduce WorldEcho, which probes action following over a broader action distribution using visual integrity and SE(3) trajectory alignment. Our diagnosis shows that current world models reasonably execute expert actions but struggle with diverse off-expert trajectories, either ignoring the commanded actions or producing visually invalid rollouts. We further propose WorldSync, which strengthens action following along three complementary axes: distributional coverage, representational grounding, and intervention-effect alignment. It broadens the training distribution over action consequences, grounds intermediate video representations in action-induced robot dynamics through an Action-Forcing Expert, and aligns predicted changes under action interventions with the corresponding changes in ground-truth futures. Experiments on RoboTwin benchmarks and real-robot tasks show that WorldSync improves WorldEcho metrics and serves as a more reliable simulator for iterative policy improvement, enabling policies to achieve higher success rates.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms

- **ArXiv ID**: [2608.24877v1](https://arxiv.org/abs/2608.24877v1)
- **作者**: Jiangning Zhang, Haojun Chen, Yong Liu
- **发布时间**: 2026-08-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.24877v1](https://arxiv.org/pdf/2608.24877v1)
- **相关度评分**: 10/10

#### 英文摘要

Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints. Despite rapid progress in augmented reality, egocentric vision, multimodal models, human-computer interaction, and embodied intelligence, the literature remains fragmented across devices, tasks, and benchmarks. \textit{The key challenge is not whether a model can recognize, answer, remember, or act in isolation, but whether a complete system can sustain a reliable, temporally valid, correctable, and governable perception-state-interaction-action loop.} This survey is \textit{the \textbf{first} to systematically study smart glasses through such a unified framework}. We formalize first-person data flow and constrained task utility, characterize devices along eight verifiable hardware capability axes, organize the literature around seven interdependent foundational capabilities, and introduce an L0-L5 framework spanning capture, reactive perception, contextual assistance, persistent state, governed action, and embodied coupling. Across nine application scenes, we connect tasks with datasets, systems, products, stakeholders, failure consequences, and evidence gaps. We further present a nine-dimensional deployment framework, a claim-conditioned evaluation protocol, and an evidence ladder from controlled measurement to longitudinal field validation and audit. Together, these elements make smart glasses more comparable, deployable, and reproducibly evaluated, while outlining a roadmap toward trustworthy first-person intelligence.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. LeFlow: Generative Latent Flow Planning for World Models

- **ArXiv ID**: [2608.24855v1](https://arxiv.org/abs/2608.24855v1)
- **作者**: Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu, Jenq-Neng Hwang
- **发布时间**: 2026-08-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.24855v1](https://arxiv.org/pdf/2608.24855v1)
- **相关度评分**: 10/10

#### 英文摘要

Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator. This approach pays the full iterative optimization cost anew at every replanning step and reuses no planning experience across queries. In this work, we ask whether planning itself can be amortized once a latent world model has been learned. We present LeFlow, which learns a reusable latent trajectory prior operating directly in the latent dynamics space from the world model. LeFlow recasts planning as conditional latent trajectory generation: a rectified-flow model imagines a future latent path between the current and goal embeddings, an inverse dynamics decoder turns latent transitions into action chunks, and the frozen world model verifies each candidate by autoregressive rollout. Across four major goal-conditioned pixel-control benchmarks, LeFlow replaces iterative action-space optimization with amortized latent planning and fixed-budget rollout selection, achieving consistent success-rate gains with an order-of-magnitude reduction in planning time. Our results argue that latent world models should support not only prediction but reusable planning priors. Our code is available at https://github.com/hsiangwei0903/LeFlow.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. EMFE: A lightweight, explainable machine learning framework for malaria cell classification

- **ArXiv ID**: [2608.24793v1](https://arxiv.org/abs/2608.24793v1)
- **作者**: Md Abdullah Al Kafi, Walayat Hussain, Mousumi Karmakar, Sumit Kumar Banshal, Ahmed Al Marouf
- **发布时间**: 2026-08-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.24793v1](https://arxiv.org/pdf/2608.24793v1)
- **相关度评分**: 10/10

#### 英文摘要

Automated malaria diagnosis from stained blood-smear microscopy is dominated by deep convolutional neural networks that are accurate but computationally expensive, poorly interpretable, and rarely validated with patient-level rigor. We present EMFE (Efficient Mathematical Feature Extraction), a five-feature framework for classifying single red-blood-cell images as parasitized or uninfected using Gray World color normalization, adaptive green-channel thresholding, morphological spot detection, and classical machine learning. Using the NIH LHNCBC malaria dataset (27,558 images from 200 patients), we evaluate Random Forest, Histogram Gradient Boosting, and Support Vector Machine classifiers under patient-grouped nested cross-validation (K_outer=20, K_inner=3), ensuring that cells from each patient remain within a single fold. The optimized Random Forest achieves 94.6% pooled out-of-fold accuracy (95% CI [93.6, 95.7]), corroborated by an untouched 40-patient holdout test (94.3%) and a patient-level permutation test (p<0.001, 1,000 permutations). Ablation experiments quantify the contribution of individual features and pipeline stages. Hardware-matched comparisons with retrained DenseNet121, ResNet50, and MobileNetV2 models assess the accuracy-efficiency trade-off. Synthetic perturbations characterize three failure modes, while explainability analysis identifies spot saturation as the dominant discriminative feature. Patient-level aggregation further quantifies sensitivity-specificity trade-offs and false-positive accumulation. These results demonstrate a statistically rigorous, interpretable, and computationally lightweight alternative to deep learning, while explicitly quantifying its limitations.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
