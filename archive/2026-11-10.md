# OCR arXiv Daily Pro — 2026-11-10

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-09 09:10 - 2026-11-10 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f321e549-dead-4

---

## 📄 论文详情

### 1. Multi-Modal Agricultural Document Understanding at the DAGRI Task

- **ArXiv ID**: [2611.11886v1](https://arxiv.org/abs/2611.11886v1)
- **作者**: Zhefan Wang, Da Li, Keping Bi, Nanqing Dong
- **发布时间**: 2026-11-09
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.11886v1](https://arxiv.org/pdf/2611.11886v1)
- **相关度评分**: 10/10

#### 英文摘要

Agricultural documents, such as prefectural technical reports and crop calendars, are critical knowledge resources. However, their complex table layouts, significant variations in document length, and dense multi-modal elements pose substantial challenges for automated understanding. To address these issues, the NTCIR-19 DAGRI (Data Analytics for aGRicultural Information) task introduced three subtasks focusing on different dimensions of document intelligence. In the Table Information Extraction (TableIE) task, we developed a multi-stage pipeline combining structure-preserving parsing via MinerU, region-adaptive segmentation for long documents, and a dual-modal (vision-text) extraction strategy for complex work schedules. This approach achieved first place with an exact match score of 0.6566. For Multi-Table Multi-Hop Question Answering (MTMH-QA) over interrelated JSON tables, we adopted an agentic search framework utilizing DCI-Agent to iteratively explore directories via bash commands, reinforced by a cross-model validation mechanism. This yielded a revised accuracy of 0.8444, initially ranked first. In the Figure and Table Question Answering (FiT-QA) task, which requires comprehending single large composite images, we implemented a dual-modal VLM pipeline enhanced by deterministic answer normalization, securing the highest BLEU score. Together, our system effectively addresses regional structural variations, dynamic cross-file evidence discovery, and multi-modal alignment, providing a robust framework for complex agricultural document understanding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1063564f-fafd-4

---

### 2. A Lattice-Based HMM Approach to Aruz Scansion of Ottoman Poetry

- **ArXiv ID**: [2611.12691v1](https://arxiv.org/abs/2611.12691v1)
- **作者**: Mehmet Emre Tiryaki
- **发布时间**: 2026-11-10
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.12691v1](https://arxiv.org/pdf/2611.12691v1)
- **相关度评分**: 10/10

#### 英文摘要

Ottoman Divan poetry is composed in aruz, a quantitative meter based on the weights of syllables. The meter is sensitive to specific characters recorded in the original writing in the Arabic script. This work is concerned with automatic meter finding and scansion alignment for Ottoman Divan poetry, especially on modern Turkish spelling without the special diacritics that scholarly transliterations of Ottoman preserve. We define two tasks on this input, first identifying the meter used in the poem, and second aligning the meter's weights with the syllabification of the poem, identifying the flaws and freedoms the poet has taken along the way. We build a corpus of 52,000 lines split by poet, with scansion annotations for 500 test lines, and a robustness benchmark generated at the deviation rates measured on real web and OCR copies. Our model is a hidden Markov model over the positions of each meter, decoded over a lattice of every candidate path, and trained by EM from the printed meter, without scansion labels. On a held-out set it scans 77.6% of the test lines fully correctly, against 26.8% for the available rule-based scanner, 55.0% for a neural tagger trained with the same supervision and 63.6% for Claude Opus 5.5 few-shot. The code is open-sourced and the tool is released on the web.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 013ce870-d5a4-4

---

### 3. A four-step validation protocol for radiomic survival analysis in small cohorts: a body composition case study

- **ArXiv ID**: [2611.12682v1](https://arxiv.org/abs/2611.12682v1)
- **作者**: Mariela Talavera-Muñoz, Cecilia Diana-Albelda, Miguel Antonio Sampedro-Nuñez, Victor Rodriguez-Laval, Jesus Bescos...
- **发布时间**: 2026-11-10
- **分类**: eess.IV, cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.12682v1](https://arxiv.org/pdf/2611.12682v1)
- **相关度评分**: 10/10

#### 英文摘要

Gastroenteropancreatic neuroendocrine tumors (GEP-NET) lack prognostic biomarkers, and computed tomography (CT)-based body composition radiomics at the third lumbar vertebra (L3) is a promising candidate. Small cohorts make high-dimensional radiomic models prone to overfitting and single-split evaluations variable and optimistic. This methodological study proposes a four-step validation protocol for radiomic survival analysis in small cohorts: (1) false discovery rate (FDR)-corrected feature selection, (2) a dual-path comparison of prior feature selection versus embedded regularization, (3) repeated nested cross-validation (CV) and (4) a negative control with Gaussian noise features. In 78 GEP-NET patients, 535 radiomic features from five L3 compartments were used to evaluate five survival models with Harrell's concordance index (C-index), time-dependent area under the curve (AUC) and integrated Brier score (IBS). Step 1 selected at least one feature in 18% of outer folds under noise (nominal level 20%) versus 84% with radiomic features. The dual-path comparison showed no consistent difference between strategies. Repeated nested CV reduced variability across seeds (41% median reduction in C-index standard deviation), but not enough to distinguish models. The nested CV C-index exceeded chance by 0.07-0.15 with radiomic features but not clearly under noise (0.40-0.42 with prior feature selection, 0.47-0.55 with embedded regularization). Frequently selected features tentatively linked greater subcutaneous fat, skeletal muscle compactness and texture to better prognosis. These findings suggest a modest prognostic signal in L3 radiomics, with considerable uncertainty that the protocol quantifies. The protocol may transfer to other small-cohort radiomic survival studies. Code: https://github.com/marielatalaveram/radiomics-survival-validation-protocol.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0b090c0e-1f04-4

---

### 4. Path-Level Structural and Semantic Alignment for Hierarchical Multi-Label Text Classification

- **ArXiv ID**: [2611.12420v1](https://arxiv.org/abs/2611.12420v1)
- **作者**: Xindi Wang, Aifen Xiong, Baiyang Wang, Xuri Ge, Robert Mercer...
- **发布时间**: 2026-11-09
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.12420v1](https://arxiv.org/pdf/2611.12420v1)
- **相关度评分**: 10/10

#### 英文摘要

Hierarchical multi-label text classification (HMTC) requires models to capture both structural dependencies among labels and the fine-grained semantics of labels at different hierarchy levels. Existing methods often model hierarchy through prediction constraints or representations of individual labels and local relations. Structural and semantic supervision, however, are usually formulated separately. We instead use complete root-to-node label paths as a shared unit for both. Our framework introduces two auxiliary training objectives while retaining a standard multi-label classifier at inference. PathSimNCE aligns document representations with hierarchical paths using hierarchy-aware contrastive targets. These targets provide graded supervision for structurally related paths while preserving explicit supervision for the ground-truth paths. The complementary semantic objective uses LLM-generated, document-conditioned descriptions of the same positive paths. It thereby provides context-specific label semantics beyond static label representations. Experiments on three benchmarks show consistent improvements: structural alignment is particularly beneficial in deeper hierarchies, while semantic alignment provides additional gains for fine-grained labels.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8ea5991d-6844-4

---

### 5. AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace

- **ArXiv ID**: [2611.12393v1](https://arxiv.org/abs/2611.12393v1)
- **作者**: Shiqi Chen, Daniel Madrigal Diaz, Wei-Ning Chen, Gbola Afonja, Fangkai Yang...
- **发布时间**: 2026-11-09
- **分类**: cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.12393v1](https://arxiv.org/pdf/2611.12393v1)
- **相关度评分**: 10/10

#### 英文摘要

As LLM agents become more autonomous, they are increasingly expected to run as always-on assistants on a user's behalf, identifying work to be done and completing it without being asked. Yet existing benchmarks usually give the agent its task, whereas in knowledge work the requests sit in the user's workspace and the agent must first recognise which obligations exist. We study proactive task discovery and execution, in which an agent must infer a user's pending tasks from their workspace and complete them in the systems where the work lives. This setting poses two challenges. For the agent, the tasks are buried in a large volume of mail, chat, documents and records. For evaluation, a benchmark needs a simulated organisation whose people, events and documents are mutually consistent, so that tasks arise realistically and their correct outcomes are known. We introduce AutoBuddy-Bench, a simulator that addresses these challenges. It models an organisation's employees, projects, business systems and event history as a temporal graph, renders it into realistic workspace artefacts, derives ground-truth tasks from the events that create obligations, and computes each task's outcome from the world state; execution is judged by the agent's changes to the workspace. To evaluate current LLMs, we build AutoBuddy, a reference agent with interchangeable backbone LLMs: it identifies tasks from the workspace, grounding each in its source records, and executes each in a separate session with write access. Varying only the backbone, we find a systematic shift in where tasks are lost: weaker models fail mainly at discovery, intermediate models identify tasks but often stop short of carrying them out, and the strongest models fail mainly during execution, most often on business-system operations. Discovery precision is only weakly related to execution quality, suggesting the two are distinct capabilities.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1f40df90-b163-4

---

### 6. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning

- **ArXiv ID**: [2611.12886v1](https://arxiv.org/abs/2611.12886v1)
- **作者**: Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei
- **发布时间**: 2026-11-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.12886v1](https://arxiv.org/pdf/2611.12886v1)
- **相关度评分**: 10/10

#### 英文摘要

Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the observation state, rather than only the output distribution, as an object of alignment. First, Ground-Drop-GRPO (GD-GRPO) trains spatial and temporal specialists with evidence-aware rewards and stochastic removal of the original visual input, encouraging them to acquire grounded evidence and use the returned observations. Second, Observation-Gated-MOPD (OG-MOPD) replaces deficient tool actions with canonical ones mid-rollout and resumes distillation from the repaired observation. The two stages complement each other, as learning to rely on tool-returned observations can help the policy benefit from observation repair. Neither stage requires a task-specific SFT cold start. Extensive experiments over 14 image and video benchmarks demonstrate that Reframe outperforms both Mix-RL and vanilla MOPD. Ablation results show that GD-GRPO increases observation dependence and tool gain compared with outcome-based GRPO.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8f87e94f-4959-4

---

### 7. World In-Context Learning for Agentic Robot Manipulation

- **ArXiv ID**: [2611.12885v1](https://arxiv.org/abs/2611.12885v1)
- **作者**: Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang...
- **发布时间**: 2026-11-10
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.12885v1](https://arxiv.org/pdf/2611.12885v1)
- **相关度评分**: 10/10

#### 英文摘要

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at https://github.com/ArcheOne-AI/RoboScript

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b2ab1882-1e5d-4

---

### 8. Guiding Data Allocation for Robust Subpopulation Generalization

- **ArXiv ID**: [2611.12884v1](https://arxiv.org/abs/2611.12884v1)
- **作者**: Zhaoying Pan, Yipei Wang, Shenyu Lu, Xiaoqian Wang
- **发布时间**: 2026-11-10
- **分类**: cs.LG, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.12884v1](https://arxiv.org/pdf/2611.12884v1)
- **相关度评分**: 10/10

#### 英文摘要

Machine learning models often achieve high average accuracy in the training data while performing poorly on test data due to subpopulation shift. A common data-centric solution is to enforce balanced subgroup proportions, but full balance can be costly, infeasible, and not always necessary. In this work, we study whether balanced training data is the unique optimal configuration for robust subpopulation generalization. We extend a Gaussian feature-model framework to theoretically characterize the performance landscape across general training subgroup distributions. We show that multiple configurations, including substantially imbalanced ones, can perform comparably to the balanced one. We further derive gradient-based directions for adjusting subgroup proportions to improve adjusted accuracy and worst-group accuracy more efficiently. These findings suggest that strategically allocating data offers a more flexible and principled path to robust performance than simple balancing. The code is available at https://github.com/zhaoyingpan/subpop-data-allocation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 36ffac36-3eb3-4

---

### 9. Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs

- **ArXiv ID**: [2611.12883v1](https://arxiv.org/abs/2611.12883v1)
- **作者**: Zhaoying Pan, Shenyu Lu, Jun Hui Wong, Junyi Chai, Xiaoqian Wang
- **发布时间**: 2026-11-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.12883v1](https://arxiv.org/pdf/2611.12883v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow visual or textual evidence. Building on this, we introduce a lightweight, training-free intervention that biases these heads toward a designated trusted modality at inference time. The identified heads are stable across calibration set sizes and generalize across settings, and steering them enables effective bidirectional control of modality reliance across diverse benchmarks. Our findings identify an effective control mechanism to align MLLM predictions with task-specified modality priorities. The code is available at https://github.com/zhaoyingpan/modality-arbitration.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c7334320-7b8b-4

---

### 10. Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos

- **ArXiv ID**: [2611.12879v1](https://arxiv.org/abs/2611.12879v1)
- **作者**: Rustin Soraki, Matthew Wallingford, Ryan Aby, Brandon Chee, Jason Ren...
- **发布时间**: 2026-11-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.12879v1](https://arxiv.org/pdf/2611.12879v1)
- **相关度评分**: 10/10

#### 英文摘要

To interact with an object, we need to anticipate both how it will move and how our hands should move with it. Human videos capture these relationships across everyday activities, offering a natural source for learning to predict future interactions. Learning from them requires recovering motion from completed interactions and using it to anticipate what could happen next. We present $\textit{Grasping-the-Future}$, a unified generative model of joint 3D hand-object motion, including wrist motion, finger articulation, and object position and orientation. Through masked spatiotemporal completion and flow matching, we train a single model for several prediction tasks: forecasting future interactions, predicting hand motion given object motion or vice versa, generating both trajectories toward a desired final object pose, and completing partially observed interactions. We explicitly model hand-object relations and incorporate contact constraints to help preserve grasp relationships during motion. To obtain 3D supervision from internet videos, we develop a scalable pipeline that combines pretrained perception models with joint geometric optimization to reconstruct completed interactions. We combine these recovered trajectories with annotated interaction datasets as training data for all tasks. We demonstrate strong performance across all tasks, outperforming released forecasters on datasets with 3D annotations. Moreover, we show geometric and physical plausibility of the predicted trajectories by retargeting them to a robotic embodiment. Videos are available at https://grasping-the-future.github.io.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c14c5359-2451-4

---

### 11. Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks

- **ArXiv ID**: [2611.12875v1](https://arxiv.org/abs/2611.12875v1)
- **作者**: Hao Gu, Jin Yao, Zezhou Cheng
- **发布时间**: 2026-11-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.12875v1](https://arxiv.org/pdf/2611.12875v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point correspondences provided by a user, Click3R injects geometric constraints into the 3D reconstruction networks through a lightweight point correspondence adapter, enabling the model to resolve ambiguities in challenging scenarios such as repetitive textures, symmetric structures, large viewpoint changes, or textureless regions. To evaluate interactive reconstruction, we curate a challenging benchmark specifically designed to expose failure modes of existing feed-forward 3D reconstruction methods. Experiments show that Click3R reduces reconstruction error with as few as a single correspondence click, improving performance on both standard and our curated benchmarks. Our results highlight that sparse human interaction provides an effective and practical mechanism for correcting geometric reconstruction errors.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cdee391e-e200-4

---

### 12. SWAM: Scaling World Action Models with Cross-Modal Alignment

- **ArXiv ID**: [2611.12870v1](https://arxiv.org/abs/2611.12870v1)
- **作者**: Yu Zhou, Xinyuan Xia, Xuankun Yang, Yinghao Yang, Wendi Chen...
- **发布时间**: 2026-11-10
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.12870v1](https://arxiv.org/pdf/2611.12870v1)
- **相关度评分**: 10/10

#### 英文摘要

World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However, introducing action learning may impair this alignment. Principled guidance on data and supervision design for maintaining language-video alignment during action learning remains limited. To investigate this, we curate a pool of approximately 47,000 hours of general videos, egocentric videos, UMI demonstrations, and robot demonstrations. Building on this, we systematically study how language-video supervision, language-video-action supervision, and the joint use of these two forms affect WAM performance. In particular, we examine how language annotation quality affects pretrained language-video capabilities, and how action supervision from UMI and robot demonstrations extends these capabilities to language-video-action modeling. To better scale the model, we further conduct detailed studies on joint training recipe and model architecture. Under a fixed training budget, mixing egocentric videos and UMI demonstrations improves control generalization. Model architecture affects how effectively these experiences are used, while scaling pretraining under the selected configuration brings further gains. The resulting recipe, post-trained on RoboTwin Clean demonstrations only, achieves success rates of 88.10% and 61.56% under Easy (Clean-to-Clean) and Hard (Clean-to-Random) conditions, respectively. Our model achieves 40.00% SR across three real-world tasks, compared with 23.33% for the strongest baseline, indicating better generalization under unseen conditions. We release the curated data, training code, and model weights.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: dff408b4-d092-4

---

### 13. AI-based characterization of lymphoid structures and the tumor microenvironment reveals lower mature tertiary lymphoid structures, lymph-node follicles, and plasma cells after neoadjuvant therapy in lung squamous cell carcinoma

- **ArXiv ID**: [2611.12855v1](https://arxiv.org/abs/2611.12855v1)
- **作者**: Arne Schmidt, Justin Nieder, Cornelius Boehm, Julika Ribbat-Idel, Marius Teodorescu...
- **发布时间**: 2026-11-10
- **分类**: cs.CV, q-bio.QM
- **PDF**: [https://arxiv.org/pdf/2611.12855v1](https://arxiv.org/pdf/2611.12855v1)
- **相关度评分**: 10/10

#### 英文摘要

Mature, germinal centre-bearing tertiary lymphoid structures (TLS) and mature lymph node follicles (secondary lymphoid structures, SLS) sustain the plasma cell response that shapes outcome and immunotherapy benefit in lung cancer. How this loco-regional axis differs between neoadjuvant-treated and therapy-naive tumors is poorly defined. We analyzed H&E whole-slide images of resected tumors and paired proximal and distal lymph nodes from matched neoadjuvant-treated (neoLUSC, n=20) and therapy-naive (naivLUSC, n=20) lung squamous cell carcinoma (LUSC) patients. Aignostics Atlas H&E Tissue Analysis (HETA) models quantified cell densities per tissue compartment and cell-cell co-localization; a dedicated deep-learning model validated against pathologist annotations detected TLS and SLS and graded their maturity. Prognostic value was tested in an independent cohort (n=458; 46 treated). In neoLUSC tumors, stromal plasma cell density was 72% (p=0.004) and stromal lymphocyte density 48% (p=0.015) lower than in naivLUSC; macrophages and granulocytes did not differ significantly. Total and immature TLS did not differ, whereas mature TLS in the tumor (p=0.034) and mature SLS in the tumor-distal lymph node (p=0.003) were lower in neoLUSC patients. Peri-TLS plasma cell density correlated with tumor lymphocyte density in naivLUSC (rho=0.54, p=0.017) but not in neoLUSC tumors (rho=0.07). In the validation cohort, stromal plasma cell density (HR 0.69, p=0.011) and lymphocyte-plasma cell co-localization (HR 0.66, p=0.004) were associated with longer survival, and neoadjuvant status with shorter survival (HR 1.50, p=0.026). Neoadjuvant therapy is thus associated with fewer mature lymphoid structures and weaker coupling of the humoral compartment to the tumor rather than uniformly lower immune readouts. The stromal plasma cell/co-localization axis is a candidate prognostic biomarker.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 11ee5658-63cd-4

---

### 14. What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching

- **ArXiv ID**: [2611.12852v1](https://arxiv.org/abs/2611.12852v1)
- **作者**: Tianze Luo, Haofeng Huang, Yuan Yao
- **发布时间**: 2026-11-10
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.12852v1](https://arxiv.org/pdf/2611.12852v1)
- **相关度评分**: 10/10

#### 英文摘要

Latent Diffusion Models dominate generative modeling but face two-stage training complexity and the inherent reconstruction limits of pre-trained autoencoders. Pixel-space Flow Matching offers a simplified end-to-end alternative yet often encounters training difficulties when using the standard $v$-prediction objective. Recent research attributes this difficulty to the off-manifold nature of noised targets, motivating a shift toward $x$-prediction. In this paper, we investigate this explanation through patch-wise Principal Component Analysis (PCA) and identify a bandwidth bottleneck. The velocity in minor components is largely determined by the raw noisy input, requiring deep backbones to preserve information that competes with principal-component modeling. Through controlled experiments and representation analysis, we further examine why $x$-prediction remains effective: its parameterization provides a raw-input bypass, while its learned input representation can spontaneously concentrate on principal directions. Under low-rank observations, our analysis of the induced flow characterizes $x$-prediction as an implicit conditional-mean decoder, reconstructing discarded components from the retained information. These observations motivate the Raw-injected Transformer (RiT), which combines a lightweight raw-conditioned decoder with an output-side shortcut to separate semantic modeling from raw-state propagation. Our method restores effective $v$-prediction and achieves competitive performance on ImageNet $256\times256$, providing a perspective on the interaction between prediction objectives and architectural bandwidth.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bb4f813e-fb11-4

---

### 15. 2D Gum-Net: Unsupervised Dense Elastic Image Registration via Symmetric Correlation and Spectral Pooling

- **ArXiv ID**: [2611.12805v1](https://arxiv.org/abs/2611.12805v1)
- **作者**: Aarya Bhave, Anushka Ajay Bhave
- **发布时间**: 2026-11-10
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.12805v1](https://arxiv.org/pdf/2611.12805v1)
- **相关度评分**: 10/10

#### 英文摘要

Dense non-rigid registration, the recovery of a pixel-wise deformation field that warps one image into geometric agreement with another, is fundamental across medical imaging, structural biology, and correspondence estimation, yet learning-based approaches face a severe bottleneck: ground-truth deformation fields are notoriously difficult to obtain for real data. We present 2D Gum-Net, an end-to-end architecture that predicts dense elastic deformation fields fully unsupervised. We transfer the Geometric Unsupervised Matching Network (Gum-Net), originally developed for 3D subtomogram alignment in cryo-electron tomography, to 2D elastic registration: all three modules are redesigned in 2D, and the rigid transformation head is replaced by a Dense Spatial Transformer that regresses a sparse control-point grid, lifted to a full-resolution field $Φ$ by bicubic interpolation. Downsampling uses DCT spectral pooling, implemented as frozen-basis matrix multiplications ($\approx 50\times$ GPU speedup), preserving the fine, quasi-periodic structure that max and average pooling destroy. We evaluate on contact-based fingerprints, a challenging testbed for this task: locally self-similar ridge patterns make correspondence maximally ambiguous, skin pressed against a sensor generates authentic large-displacement elastic distortion, and minutiae act as precise landmarks through which an independent matcher externally verifies the topological correctness of predicted fields. Trained purely on synthetic impressions and evaluated zero-shot on real benchmarks, our method improves structural correlation by up to 15.7% on FVC2004 and raises genuine match scores under an independent matcher while leaving imposter scores essentially unchanged. This suggests that the predicted deformations restore true structure without fabricating correspondences.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 18e2c539-20d8-4

---
