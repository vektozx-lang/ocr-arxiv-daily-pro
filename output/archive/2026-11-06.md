# OCR arXiv Daily Pro — 2026-11-06

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-05 09:10 - 2026-11-06 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d24a1b9c-259c-4

---

## 📄 论文详情

### 1. ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition

- **ArXiv ID**: [2611.08091v1](https://arxiv.org/abs/2611.08091v1)
- **作者**: Ismail El Jamiy, Khadija Msalek, Guillaume Loizelet, Farah Benamara, Nabil Hathout
- **发布时间**: 2026-11-05
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.08091v1](https://arxiv.org/pdf/2611.08091v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite recent progress in handwritten text recognition, medieval Arabic scientific manuscripts remain an open challenge for current vision-language models (VLMs) due to cursive ligatures, variable diacritization, and more importantly the lack of training data. This paper aims to address this gap, by proposing the first annotation guidelines dedicated to the transcription of scientific Arabic manuscripts inspired by textual criticism, a well-established approach to historical text editing. We then propose, ATHAAR, a new dataset manually annotated following this guideline. Unlike previous resources in the field, ATHAAR varies both witnesses of the same text, calligraphic styles, and content to deal with texts but also numerals. Relying on state-of-the-art VLMs, we finally design a set of experiments to study models transfer across scripts, chapters, and treatises. Our findings highlight the limitations of current systems when faced with the specificities of ancient scientific texts.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 06b3ccd0-7d7d-4

---

### 2. ManimCode: Learning Visual Self-Correction for Educational Animation

- **ArXiv ID**: [2611.08294v1](https://arxiv.org/abs/2611.08294v1)
- **作者**: Zhengyang Liang, Lizi Liao
- **发布时间**: 2026-11-06
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08294v1](https://arxiv.org/pdf/2611.08294v1)
- **相关度评分**: 10/10

#### 英文摘要

Manim supports precise, programmatic video generation, but a successfully rendered educational animation can still have visual defects, missing explanations, or incorrect content. Rendering does not directly identify the code changes needed to correct these visual failures, so feedback-driven revision is needed. Existing agentic frameworks use iterative rendering and revision but typically rely on large models, often proprietary. Existing Manim datasets primarily contain final programs and often lack quality verification and the trajectories of feedback and revisions needed to learn this refinement process. We introduce ManimData and ManimCode, a data and training framework for feedback-driven educational animation generation. We construct ManimData through a render-guided pipeline that iteratively generates, executes, reviews, and revises Manim programs with retrieved API documentation. Its 24,034 render-verified, quality-filtered records preserve intermediate programs, execution errors, visual critiques, and corrective revisions. We use role-conditioned supervised fine-tuning on these trajectories to train ManimCode, a single 4B model, to write, review, and revise animation programs. To improve correction of errors that differ from those in the collected trajectories, we then train the Reviser with reinforcement learning on self-generated states, using rendering outcomes and reference-free quality feedback. ManimCode achieves 96.6% and 97.0% render success on ManimData-test and ManimBench, compared with 52.6% and 82.0% for the untrained 4B model under the same inference setup, while also improving video quality scores from 2.48 to 2.94 and from 3.00 to 3.44. Integrating ManimCode into two long-form educational video generation systems increases completed videos from 19/117 to 107/117 and from 53/239 to 239/239, alongside improvements in educational effectiveness and visual quality.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d52ab29d-1910-4

---

### 3. Accepted but Wrong: Silent Failures of LLM Code Repairs after API Migrations

- **ArXiv ID**: [2611.08269v1](https://arxiv.org/abs/2611.08269v1)
- **作者**: Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang
- **发布时间**: 2026-11-06
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.08269v1](https://arxiv.org/pdf/2611.08269v1)
- **相关度评分**: 10/10

#### 英文摘要

After a runtime or API migration, an LLM-repaired procedure can run cleanly yet return wrong results, and a release check on typical test inputs ships it. We report a preregistered study of 73 tasks covering 60 documented changes in CPython, Node.js and SQLite. Every candidate is executed on the real runtimes against withheld contracts. Over the complete repair space, the all-assertions gate on typical inputs released 0.410 of wrong repairs. One edge input written from the release note cut this to 0.065, and to 0.061 on 15 unseen clusters. Three inputs from a blind GPT-5.6-luna writer that never saw the program reached 0.070. Two further frozen stages enlarged the menu to 1491 fragments and then added 233 hard distractors that match the legacy output on typical inputs. The edge input (0.058) and the frontier-model writer (0.058) passed their preregistered tests. Yet 0.168 and 0.153 of the hard wrong programs still passed. Two local-model writers failed their preregistered tests. Across four model families, the edge input cut wrong releases per attempt in all three open-weight families on all three menus, for example from 0.233 to 0.057, without lowering correct completion. Self-tests helped less. A blind AI audit flagged 34 contracts as stricter than their requirements. Dropping the disputed checks changed 0 verdicts, but class-label disputes remain open. No model-written code was executed. Artifacts are available from the authors on request.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 39793e92-05c2-4

---

### 4. Domain-specific information retrieval

- **ArXiv ID**: [2611.08228v1](https://arxiv.org/abs/2611.08228v1)
- **作者**: Suzan Verberne, Florina Piroi, Allan Hanbury
- **发布时间**: 2026-11-06
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.08228v1](https://arxiv.org/pdf/2611.08228v1)
- **相关度评分**: 10/10

#### 英文摘要

Information Retrieval (IR) is much more than ad hoc web search: a large portion of the information seeking activities takes place in specific domains, often addressing work-related tasks. Examples are lawyers finding relevant prior cases for a legal case and academic researchers studying the background material for a paper. In Chapter 2 we outline the most common domain-specific tasks, datasets and applications. Domain-specific IR has a number of challenges that make set it apart from simple web search tasks: they often deal with long documents, long queries and long sessions with specific user needs. We discuss these in Chapter 3. We also address issues related to bias and fairness of models. In Chapter 4, we describe the models and methods developed for domain-specific tasks and data, addressing the specific challenges, including user aspects related to domain-specific IR tasks, dealing with queries, user models, and user interactions. We show that many of the methodological advances in domain-specific IR are transferable to other domains and even to open-domain web search. We conclude with the main takeaways and propose research directions for the near future.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 172e3622-08a3-4

---

### 5. Who Can Evaluate AI Independently? A Framework for Analysing Evaluation Infrastructure

- **ArXiv ID**: [2611.08134v1](https://arxiv.org/abs/2611.08134v1)
- **作者**: Sumaya Nur Adan, Joanna Wiaterek, Nourhan Abdelrhim, Sydney Reis, Robert F. Trager...
- **发布时间**: 2026-11-05
- **分类**: cs.CY, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.08134v1](https://arxiv.org/pdf/2611.08134v1)
- **相关度评分**: 10/10

#### 英文摘要

AI evaluation is increasingly central to AI safety and governance, yet taking part in an evaluation does not by itself confer authority over its design, its execution or the resources it depends on. This paper examines how infrastructure arrangements distribute that authority, and so shape who can evaluate AI systems independently. Drawing on Science and Technology Studies, political economy and applied evaluation standards, we introduce PAAI (Power, Access, Adequacy, Independence), a framework for examining who controls evaluation infrastructure, the terms on which it is available, whether it is adequate to the evaluation's purpose and what autonomy it supports. We apply PAAI to twelve African AI evaluation projects (2022-2025) and to the documented roles of all ten member institutes in the three published joint testing exercises of the international network of AI Safety Institutes. We identify three recurring configurations: extractive collaboration, dependent innovation and constrained independence. African actors often contribute data, language expertise and task design while external institutions retain authority over infrastructure and evaluation frameworks; design authority without infrastructure authority never yielded more than partial independence. The joint testing exercises show a similar division among mostly high-income members: the institutes that led each exercise also ran the models, while Kenya, the network's only African member, moved from annotation to task design with no documented model execution. Participation in evaluation does not by itself produce evaluative authority. For evaluation to serve as a credible governance mechanism, access must come with control over priorities, methods, publication and continuity.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7589270d-3687-4

---

### 6. Create Your Own Work Stack: Deploying Self-hosted AI and Tooling in a Tech Startup

- **ArXiv ID**: [2611.08116v1](https://arxiv.org/abs/2611.08116v1)
- **作者**: Saad Ahmed Bazaz, Talha Amjad, Abdurrehman Subhani, Sohaib Ahmed Bazaz, Abdullah Aamir
- **发布时间**: 2026-11-05
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.08116v1](https://arxiv.org/pdf/2611.08116v1)
- **相关度评分**: 10/10

#### 英文摘要

Self-hosting AI is often presented as a way to reduce inference costs and increase control, but deployment introduces its own costs. We report our experience deploying a hybrid AI stack at Grayhat Developers, a small software company with an AI-intensive development workflow. Our initial motivation was to counter the growing cost of commercial AI usage: Claude/Codex incurred approximately \$325 per month, with more than 25.93 billion recorded tokens. We experimented with local open-source models as replacements for commercial coding agents, but after learning that their performance and inference speed were insufficient, we adopted a hybrid approach in which commercial agents remained responsible for complex tasks while local models handled lower-complexity tasks, organizational information retrieval, and synchronization with self-hosted tools including Outline, Plane, and ERPNext. We estimated that approximately 30--40\% of our commercial AI workload was associated with context transfer, documentation synchronization, task management, and related operational coordination. By moving this work to local models, we estimate that approximately 90\% of this coordination workload could be handled without commercial inference, corresponding to an estimated 27--36\% reduction in overall commercial-AI workload or cost-equivalent usage. Our first internal deployment nevertheless failed to achieve adoption because it introduced UX friction. Replacing it with a centrally configured deployment substantially improved feedback and adoption. We conclude that local inference is most useful not as a wholesale replacement for commercial AI, but as part of a hybrid architecture that assigns tasks according to their capability requirements, cost, context demands, and operational sensitivity.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a005d72c-f960-4

---

### 7. Probabilistic Relevance Decisions for Semantic Retrieval

- **ArXiv ID**: [2611.08014v1](https://arxiv.org/abs/2611.08014v1)
- **作者**: Bahadır Tatar, Cevat Şener
- **发布时间**: 2026-11-05
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.08014v1](https://arxiv.org/pdf/2611.08014v1)
- **相关度评分**: 10/10

#### 英文摘要

Dense similarity supplies reusable corpus representations, while probabilistic relevance decisions offer query-dependent document scoring. We compare dense-only BGE-M3 with TypeSafe Jev Noul and OpenAI Decisions Predicate scores on the official BEIR SciFact test benchmark. The study evaluates 300 official test queries using identical positive-enriched 100-document pools and full-corpus dense retrieval followed by reranking at candidate depths of 50 and 100. Unlike the controlled pools, neither dense prefix receives positive injection. Jev has the highest observed Recall@5 and nDCG@10 under the evaluated conditions. At depth 50, full-corpus nDCG@10 is 0.6413 for BGE-M3, 0.7545 with OpenAI and 0.7805 with Jev. Extending depth from 50 to 100 increases known-positive candidate recall but produces small, uncertain final-effectiveness changes. All four paired-bootstrap depth intervals include zero. Unique-condition API scoring cost approximately doubles, while compatible cached decisions reduce incremental expenditure. OpenAI returns many exact-zero scores, and secondary exact-tie randomization reveals ranking sensitivity without replacing deterministic primary results. Top-100 latency mixes cached and new execution. Historical hybrid latency is a saved-component sum under different execution environments and timer boundaries. These exploratory, unadjusted analyses support relevance decisions as a complement to dense retrieval within this protocol, without establishing general superiority, probability calibration or equivalence between depths.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 43568289-4a2c-4

---

### 8. The Gold Rush in AI4Math, II: What are signatures of AI-assisted Proofs?

- **ArXiv ID**: [2611.08412v1](https://arxiv.org/abs/2611.08412v1)
- **作者**: Yuanchuan Guo, Jiashun Jin, Zheng Tracy Ke, Bingcheng Sui
- **发布时间**: 2026-11-06
- **分类**: cs.AI, stat.AP
- **PDF**: [https://arxiv.org/pdf/2611.08412v1](https://arxiv.org/pdf/2611.08412v1)
- **相关度评分**: 10/10

#### 英文摘要

The growing use of AI in mathematics raises a question: can we detect AI involvement in proofs, separately from AI assistance with writing? Historical arXiv papers, recent papers disclosing substantive AI use, and manuscripts released by OpenAI provide a rich empirical basis for studying this question. However, several challenges remain: lack of matched case-control pairs; potential incompleteness of disclosure; and lack of ready-to-use features designed to capture signals of AI involvement in proofs. To address these challenges, we construct five cohorts comprising 8,281 papers by combining existing manuscripts with those we produced using generative AI. These cohorts span different levels of AI involvement and include matched pairs of papers addressing the same research problems. We then introduce ProofTrace, a framework that represents each paper as a graph of immediate proof support (GIPS) and extracts interpretable features of mathematical organization. Our study yields three discoveries. First, principal-component projections of our features reveal a qualitative gradient of AI involvement, where AI-reworded papers remain close to human papers, the two AI-generated cohorts depart in broadly shared directions, and papers disclosing substantive AI use occupy intermediate positions which shifts toward AI-generated cohorts over time. Second, we identify recurring signatures of AI-generated proofs, such as fewer externally cited results, greater reliance on intermediate conclusions, and altered graph connectivity; many of these signatures persist under controls for research field, manuscript length, or graph size. Finally, in a separate detection experiment, ProofTrace distinguishes human-written papers from those disclosing substantive AI use. Its performance remains stable under AI rewording, whereas the performance of state-of-the-art text-based detectors declines sharply.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2e1b6886-9a73-4

---

### 9. Polarity Classification with Multitask Learning Syntax Augmentation

- **ArXiv ID**: [2611.08323v1](https://arxiv.org/abs/2611.08323v1)
- **作者**: Muhammad Imran, Carlos Gómez-Rodríguez
- **发布时间**: 2026-11-06
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.08323v1](https://arxiv.org/pdf/2611.08323v1)
- **相关度评分**: 10/10

#### 英文摘要

Sentiment Analysis (SA) is a fundamental NLP task concerned with the identification and categorization of subjective information in text. While lexicon-based methods offer transparency, they often struggle with linguistic phenomena such as negation and intensification. Syntactic parsing has been integrated into SA pipelines to address this, but conventional parsers introduce significant computational overhead. Recent work shows that reformulating dependency parsing as a Sequence Labeling (SEL) task can improve efficiency. We propose and compare two strategies for integrating syntactic knowledge into a neural sentiment analysis model under unified Multi-Task Learning (MTL). The first, Standard-MTL, jointly learns dependency parsing (via sequence labeling) and sentiment polarity classification using a shared encoder with two task-specific heads. The second, Contrastive-MTL, provides implicit syntactic guidance through a contrastive auxiliary objective and a syntax-biased attention pooling mechanism, without requiring explicit label prediction. Both rely on syntactic annotations during training and eliminate need for hand-crafted compositional rules or external parsing at inference. We evaluate eleven datasets spanning seven languages---the MARC corpus (English, Spanish, French, German) and seven datasets from SemEval-2022 Task 10 (English, Spanish, Norwegian, Basque, Catalan)---using four established SEL encodings. With the relative encoding, Contrastive-MTL outperforms a syntax-naive baseline on 10 of 11 datasets and surpasses the external rule-based pipeline (SELSP) that parses at inference on all six datasets where the latter applies, while being 1.5--9$\times$ faster at evaluation. Standard-MTL is more dataset- and encoding-dependent. These results show implicit syntactic supervision during training can match or exceed explicit parsing at inference without computational overhead.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2f5d0122-097e-4

---

### 10. Do You Miss the Nights We Spent Crafting Figures? Rethinking Teaser and Framework Figures in the Age of Generative AI

- **ArXiv ID**: [2611.08486v1](https://arxiv.org/abs/2611.08486v1)
- **作者**: Xiaoqi Zhao, Youwei Pang, Kailai Zhou
- **发布时间**: 2026-11-06
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08486v1](https://arxiv.org/pdf/2611.08486v1)
- **相关度评分**: 10/10

#### 英文摘要

Scientific figures give research ideas a visual form through choices of abstraction, composition, and emphasis. Generative AI offers new ways to realize these choices, raising questions about explanatory clarity and purposeful visual expression. We examine these questions through a visual retrospective of 371 motivation and framework figures from 200 papers. The corpus comprises a quota-based main sample of 160 papers spanning four temporal periods and a separate purposive style-contrast sample of 40 papers. A single multimodal judge evaluates six dimensions of communication and design, with three repeated judgments per figure. We attempt source-constrained revisions of all 371 figures, of which 369 pass the recorded fidelity checks. Original-figure ratings show no uniform decline across periods. Revisions increase mean clarity ratings by 0.428 points and decrease aesthetic coherence ratings by 0.111 points on a five-point scale. Gains in the six-dimension average are larger for main-sample motivation figures than for frameworks. Case analyses show that added explanation can clarify comparisons while leaving typographic hierarchy and visual economy unresolved. These model-based findings support researcher-led design, with AI assisting exploration and authors retaining responsibility for explanatory purpose, composition, and scientific relationships. The accompanying atlas and evaluation records are available at https://ntu-ai4x.github.io/Rethinking_Figures/index_en.html.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0161befa-714e-4

---

### 11. Where and Why is Grounded Reasoning Useful?

- **ArXiv ID**: [2611.08485v1](https://arxiv.org/abs/2611.08485v1)
- **作者**: David Yan, Le Xue, Forrest Huang, Qiuyi Zhang, Dustin Tran...
- **发布时间**: 2026-11-06
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08485v1](https://arxiv.org/pdf/2611.08485v1)
- **相关度评分**: 10/10

#### 英文摘要

Grounded reasoning, where a model outputs text coordinates of relevant locations in chain-of-thought reasoning, is a common strategy for solving complex visual reasoning problems. However, the benefits and limitations of grounded reasoning are understudied. We study where and why grounded reasoning is most useful. To do so, we introduce a chain-of-thought analysis method to measure how much a model uses its outputted grounding in its thinking trace and perform a detailed ablation study of a grounded reasoning training recipe. We find that grounded reasoning improves counting but shows no significant gain over baselines without coordinate grounding across a wide range of spatial reasoning and perception benchmarks. Using several synthetic tasks, we show that grounded reasoning is most useful when a task requires undescribable references, which are visual concepts that are difficult to describe in language. However, we observe that many existing visual reasoning benchmarks are solvable with only describable text references. To close this gap, we introduce BrickVision, a new benchmark that requires undescribable visual references to solve.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a93efa05-d468-4

---

### 12. EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling

- **ArXiv ID**: [2611.08477v1](https://arxiv.org/abs/2611.08477v1)
- **作者**: Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li...
- **发布时间**: 2026-11-06
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08477v1](https://arxiv.org/pdf/2611.08477v1)
- **相关度评分**: 10/10

#### 英文摘要

Modern video models possess strong visual priors, yet do not natively represent human action in metric 3D space. We present EgoGeneralist, which adapts pretrained video generators to unify action-conditioned egocentric video generation, pose estimation, and joint action-video generation. Our role-adaptive action renderer provides video-native representations for multidirectional action-video learning, making metric motion usable as both a spatial control signal and a recoverable generation target. Cross-stream action-video coupling establishes close correspondence between metric motion and visual dynamics through lightweight adaptation while preserving the pretrained visual prior. Together, these designs establish a generalist framework spanning five action-video tasks. Despite adaptation only on controlled laboratory recordings, EgoGeneralist generalizes to diverse unseen scenes and interactions with effective action control and visual quality, bridging pretrained visual knowledge and metric 3D human motion.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 33780692-5712-4

---

### 13. Edge-Assisted Crowdsensing for Explainable Cyclist Safety Perception

- **ArXiv ID**: [2611.08441v1](https://arxiv.org/abs/2611.08441v1)
- **作者**: Hongsen Cao, Chia-Yen Chiang, Mona Jaber, Meihui Wang, Yasmin Fathy
- **发布时间**: 2026-11-06
- **分类**: cs.CV, eess.IV
- **PDF**: [https://arxiv.org/pdf/2611.08441v1](https://arxiv.org/pdf/2611.08441v1)
- **相关度评分**: 10/10

#### 英文摘要

Cyclist fatality rates remain high despite policy support for active travel, and autonomous vehicles add complexity to mixed traffic. Neither crash statistics nor multi-model detection pipelines scale to continuous monitoring of perceived safety along a route. We present an edge-assisted crowdsensing system: handlebar cameras supply street-level frames, a vision-language model (VLM) turns each frame into structured traffic attributes through a single prompt, and an explainable boosting machine (EBM) combines them with OpenStreetMap road infrastructure and on-bike kinematics to predict a crowdsourced 1-9 safety score. Extraction belongs at the network edge: the fastest self-hosted model needs 2.49 s per frame and scoring takes 0.4 ms on a CPU. On 1,362 annotated frames from two London routes, the EBM regressor reaches 72.2 percent binary accuracy and a mean absolute error of 1.011 under five-fold cross-validation. It is within one accuracy point of black-box ensembles. Its per-feature shape functions give exact attribution: physical lane separation is worth +0.97 rating points, a painted lane +0.70 and a construction site -0.65. Planners can therefore price an infrastructure change in rating points, and the results enter cost-benefit analysis directly. We also report inter-annotator agreement (alpha = 0.4695), an attribute audit, and a sensitivity analysis linking attribute error to accuracy. With re-encoding, a 20 s sampling interval serves 1,000 riders at 54 Mbit/s at a cost of 1.4 accuracy points, making continuous monitoring practical.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e0cc2544-3297-4

---

### 14. SM4RT: Cascaded Feed-forward Model for 4D Reconstruction

- **ArXiv ID**: [2611.08436v1](https://arxiv.org/abs/2611.08436v1)
- **作者**: Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke
- **发布时间**: 2026-11-06
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08436v1](https://arxiv.org/pdf/2611.08436v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce SM4RT, a multi-task cascade feed-forward model for dynamic scene reconstruction from RGB videos. While existing feed-forward approaches typically address geometry reconstruction and motion estimation separately--and often predict motions in a single coordinate frame that must account for camera movement--SM4RT solves these tasks sequentially by first reconstructing 3D geometry and then bootstrapping motion estimation from the predicted structure. By expressing each pixel's 3D motion in its corresponding camera frame, SM4RT reduces ambiguity arising from camera motion. To address the sparsity of real-world motion labels, SM4RT further incorporates a weakly supervised loss that regularizes unlabeled point motions using labeled point positions at the other time step. We evaluate motion estimation on three dynamic-scene datasets--Kubric, Waymo, and Point Odyssey--and SM4RT achieves the best performance on most metrics compared with prior baselines. We additionally benchmark geometry reconstruction on five dynamic scene datasets and show that SM4RT achieves competitive performance with state-of-the-art methods. Overall, our unified framework demonstrates that combining geometry reconstruction and motion estimation in a cascade not only avoids performance trade-offs but also enhances motion estimation through improved geometric reasoning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 639d433b-1ce4-4

---

### 15. T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models

- **ArXiv ID**: [2611.08413v1](https://arxiv.org/abs/2611.08413v1)
- **作者**: Mohammed Hassan, Zhenyang Chen, Zheng Wang, Zhixin Zhu, Tianlong Chen...
- **发布时间**: 2026-11-06
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.08413v1](https://arxiv.org/pdf/2611.08413v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem from two complementary forms of redundancy: many visual tokens are spatially irrelevant, while attention over the remaining tokens is often misallocated. Based on this observation, we propose T3R, a Training-Free Two-Stage Token Refinement framework. In the first stage, segmentation-guided token pruning removes irrelevant visual patches to reduce computation and eliminate distracting context. In the second stage, saliency-guided attention biasing reallocates attention toward action-critical visual regions and language instructions within the retained tokens. Together, pruning produces a cleaner candidate set, while attention biasing further emphasizes the most decision-relevant evidence, yielding a better accuracy-efficiency frontier than either stage alone. On LIBERO-Spatial, T3R removes 85% of scene-camera visual tokens while essentially matching the unpruned success rate, and improves success by up to 7 percentage points under out-of-distribution object-placement perturbations. The timing comparison attributes 7.8 ms per inference call to pruning and attention-bias application. As input resolution increases, LLM-forward profiling shows up to a 3.3x speedup over the unpruned baseline. Evaluations across LIBERO, SIMPLER, and RoboTwin with three VLA backbones show the strongest accuracy-efficiency benefits in multi-camera settings. These results demonstrate that training-free token refinement is a practical approach to efficient and robust VLA inference.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: aaac9478-cf12-4

---
