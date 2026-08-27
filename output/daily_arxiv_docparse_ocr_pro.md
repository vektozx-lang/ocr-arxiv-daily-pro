# OCR arXiv Daily Pro — 2026-08-27

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-08-26 09:10 - 2026-08-27 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans

- **ArXiv ID**: [2608.26091v1](https://arxiv.org/abs/2608.26091v1)
- **作者**: Nabaraj Subedi, Shuvo Dip Datta, Ahmed Abdelaty, Shivanand Venkanna Sheshappanavar
- **发布时间**: 2026-08-27
- **分类**: cs.IR, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2608.26091v1](https://arxiv.org/pdf/2608.26091v1)
- **相关度评分**: 10/10

#### 英文摘要

Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D plans; however, OCR-based automation strips away the geometry and layout essential for interpreting these plans. We present a Visual-First Multimodal Retrieval-Augmented Generation (RAG) framework called PlanSightRAG. It indexes and reasons directly over plan imagery, integrates a ColNomic-3B multi-vector retrieval, an agentic Planner-Retriever-Auditor-Synthesizer, and MaxSim heatmaps as an evidence trail. We introduce a 4,056-pair benchmark from five state Departments of Transportation (DOT) standard plans (1,898 pages). PlanSightRAG achieves 91.47% Recall@5 on zero-shot retrieval, while on a held-out Michigan DOT corpus, it achieves 91.40%. On synthetic, parametrically-generated compliance drawings, our Qwen2.5-VL-72B pipeline reaches 100% verdict accuracy only when supplied a pre-resolved rule threshold, a controlled ceiling that a non-VLM OCR baseline already reaches at 76.4%. Finally, we demonstrate autonomous visual rule-grounding by extracting numeric limits directly from a specification corpus without any human-supplied rules.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. DocPC: Document-Level Visual Retrieval via Representative Page Composition

- **ArXiv ID**: [2608.25434v1](https://arxiv.org/abs/2608.25434v1)
- **作者**: Chengsong You, Junwei Zhou, Nan Du
- **发布时间**: 2026-08-26
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.25434v1](https://arxiv.org/pdf/2608.25434v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual document retrieval has advanced by encoding page screenshots with vision-language models, bypassing OCR pipelines. However, existing methods remain page-centric, misaligned with real-world scenarios requiring complete document retrieval. A naive page-then-document aggregation suffers from linear indexing cost and degraded retrieval when relevance spans multiple pages. We propose DocPC, a document-level visual retrieval framework based on Representative Page Composition: selecting representative pages and composing them into a single grid image for document-level indexing, reducing indexed images, vectors, and storage by 10.1x and end-to-end indexing time by roughly 7.7x. To handle multi-positive supervision prevalent at the document level, we combine multi-positive contrastive learning with sparsely scheduled listwise optimization. We also introduce DocViRe, a benchmark with multi-positive relevance annotations. DocPC-ColQwen achieves NDCG@5 of 44.09 on DocViRe, outperforming the strongest page-level baseline at 38.91 while reducing storage by 10.1x. Code is available at https://anonymous.4open.science/r/DocPC-Document-Level-Visual-Retrieval-via-Representative-Page-Composition-1D52. Data is available at https://huggingface.co/datasets/anonymous-7219/docpc.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. Unveiling Spectral Mechanisms in Training-Free LLM Text Detection

- **ArXiv ID**: [2608.25944v1](https://arxiv.org/abs/2608.25944v1)
- **作者**: Haitong Luo, Xuying Meng, Weiyao Zhang, Wenji Zou, Shengfeng Lou...
- **发布时间**: 2026-08-27
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.25944v1](https://arxiv.org/pdf/2608.25944v1)
- **相关度评分**: 10/10

#### 英文摘要

The rapid advancement of Large Language Models (LLMs) makes it increasingly difficult to distinguish human writing from machine-generated text. Training-free detection offers a scalable solution, yet common confidence-based metrics mainly measure average token probabilities and often miss the signal fluctuations that characterize human writing, which we call "generative vitality". Spectral analysis offers a way to capture this vitality, but its mechanism and practical boundaries remain underexplored. In this paper, we analyze spectral detection from both theoretical and empirical perspectives. We connect spectral energy to variance in proxy log-probability trajectories and explain how broader human token choices create the fluctuations used by frequency-domain indicators. We further show that the strength of this signal depends on text length and sampling range: spectral evidence is clearest for long, continuous, constrained generation, while short, fragmented, mixed, and edited settings require complementary confidence and fluctuation views. These findings clarify when frequency-domain detection works and provide guidance for future multi-dimensional detector design.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. PANDA - Prototype-Anchored Alignment for Partially Unpaired Multimodal Learning, with Applications to Alzheimers MRI and TCGA Pathology

- **ArXiv ID**: [2608.25970v1](https://arxiv.org/abs/2608.25970v1)
- **作者**: Sheethal Bhat, Mahfuzur Rahman Chowdhury, Paula Andrea Perez-Toro, Stephan Wunderlich, Rose Dawn Bharat...
- **发布时间**: 2026-08-27
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.25970v1](https://arxiv.org/pdf/2608.25970v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal medical prediction often faces incomplete pairing: auxiliary modalities with complementary signal are available for only a subset of subjects (or none) and cannot be assumed at deployment. We introduce PANDA (Prototype Anchored Data Alignment), a two-stage framework that transfers auxiliary information to a primary-modality model without auxiliary inputs at inference. Stage 1 learns a shared embedding from the paired subset and estimates class prototypes from auxiliary modalities; Stage 2 trains the primary encoder on all subjects using cross-entropy plus alignment to the frozen prototypes. Because supervision is defined at the class-prototype level, PANDA accommodates arbitrary pairing rates, including zero subject overlap. We evaluate PANDA on two applications. On a 1,021-subject multi-scanner ADNI cohort, we perform AD/CN classification with three auxiliary modalities at distinct pairing rates: tabular scores (44.8%), FDG-PET (18.7%), and external handwriting kinematics (0% overlap). Relative to the same-backbone MRI-only baseline, PANDA attains AUC 0.868 +-0.020 (+7.9pp) and reduces 1.5T CN false positives by 24.3pp; on a fully trainable Conv5-FC3 backbone it reaches AUC 0.893 (best overall). A pairing-rate ablation shows that the joint anchor remains within seed noise from 75% to 5% pairing. On TCGA-Lung survival prediction from whole-slide images with RNA-seq as auxiliary data, PANDA improves over WSI-only on 2-year OS (AUC +3.5pp) and Cox PH (C-index +9.0pts) and outperforms full-fusion training, which underperforms WSI-only, while requiring no RNA at inference; wide confidence intervals on this smaller cohort keep the gains below conventional significance. Overall, PANDA provides a deployment-oriented mechanism for leveraging incomplete auxiliary modalities to improve primary-modality prediction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs

- **ArXiv ID**: [2608.25986v1](https://arxiv.org/abs/2608.25986v1)
- **作者**: Zongyu Wu, Yilong Wang, Xiaochen Wang, Minhua Lin, Zhichao Xu...
- **发布时间**: 2026-08-27
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2608.25986v1](https://arxiv.org/pdf/2608.25986v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages structured knowledge to provide (M)LLMs with high-quality external information. Building on these works, recent studies have explored multimodal knowledge graphs (MMKGs) as knowledge bases for GraphRAG. This enables Graph RAG to integrate knowledge across multiple modalities, thereby further enhancing its performance. However, existing MMKG-based RAG methods generally follow a common pipeline in which different modalities are largely processed independently before being fusion. As a result, textual context is only used to a limited extent during visual information extraction and subsequent multimodal knowledge fusion. This brings a semantic gap between images and text which limits the multimodal GraphRAG performance. To address this issue, we propose a novel framework for constructing a Context-Enhanced MMKG (CEMMKG) to better support multimodal GraphRAG. The proposed CEMMKG enriches each image with complementary textual context at both local and global scopes. Local context goes beyond the surrounding text by incorporating sentences that are semantically related to the image, while global context provides a summary of the entire passage. We further introduce a multi-granularity design for the local context, allowing it to capture semantically relevant information at different levels of detail. Extensive experiments on the selected vision-centric dataset validate that CEMMKG is effective in leveraging contextual information to improve MMKG-based RAG performance. Moreover, its effectiveness across different MMKG-based RAG methods demonstrates its broad applicability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation

- **ArXiv ID**: [2608.25936v1](https://arxiv.org/abs/2608.25936v1)
- **作者**: Justin Robert, Raheel Qader
- **发布时间**: 2026-08-26
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.25936v1](https://arxiv.org/pdf/2608.25936v1)
- **相关度评分**: 10/10

#### 英文摘要

On-policy distillation trains a language model on its own generations while a teacher scores them token by token. It combines the dense supervision of imitation learning with the on-policy sampling of reinforcement learning. But it requires a second, larger model to act as teacher. On-Policy Self-Distillation (OPSD) removes that cost. The teacher is the model itself, conditioned on privileged information the student will not have at test time, such as a reference solution, a plan, or environment feedback. The teacher is no stronger than the student, only better informed. Early results were promising, with accuracy comparable to reinforcement learning at a fraction of the generated tokens. But the same asymmetry that produces the signal also biases it. One failure mode now dominates the field: collapse, the progressive narrowing of the set of reasoning paths the model can produce. Collapse is not specific to OPSD, though privileged information aggravates it. This review treats collapse as a symptom governed by three levers: (i) where the signal is applied, that is, how tokens are weighted; (ii) what the teacher is shown, that is, the nature of the privileged information; and (iii) when the signal changes, that is, the teacher's dynamics and the decay of guidance. We restrict our scope to mathematical reasoning, where the method originated and where its failure modes are best documented. We report no new experiments. The contribution is structural: a shared vocabulary for phenomena named differently across papers, and a clear line between what is settled and what is still disputed.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Formal, Executable and Explainable Runtime Monitoring of Spoken Air Traffic Control Operational Procedures

- **ArXiv ID**: [2608.25926v1](https://arxiv.org/abs/2608.25926v1)
- **作者**: Roberto Luvini, Giacomo Longo, Alessandro Armando, Enrico Russo
- **发布时间**: 2026-08-26
- **分类**: cs.AI, cs.CL, eess.AS
- **PDF**: [https://arxiv.org/pdf/2608.25926v1](https://arxiv.org/pdf/2608.25926v1)
- **相关度评分**: 10/10

#### 英文摘要

Air traffic control procedures are executed through spoken exchanges between controllers and pilots. These interactions are essential to the safety of air transportation: failures in their execution can create severe operational hazards, as evidenced by past fatal accidents. Assessing whether an instruction has been followed requires relating what was said to the aircraft concerned, its state, and the obligations that pilots must meet. We present a runtime verification framework that monitors such procedures by checking controller-pilot exchanges, surveillance data, and onboard observations. The framework parses radio communications into events linked to the entities they concern and merges them with surveillance and onboard observations into a time-stamped trace. The ICAO-derived obligations as formalized as temporal formulas with explicit time bounds and evaluated over execution traces. Every violation is reported along with the breached obligations and the observations that support the verdict. With real traffic, the complete pipeline reaches an F1 of 0.85 against blind human-annotated violations; in 1,495 synthetic situations derived from two public corpora, the monitor logic returns the expected verdict in every case. In two historical accidents reconstructed from official investigation reports, the monitor identifies the same procedural deviations documented by the investigators.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. Loss-Based Active Learning for Neural Abstractive Summarization

- **ArXiv ID**: [2608.25881v1](https://arxiv.org/abs/2608.25881v1)
- **作者**: Michail Ioannou, Tatiana Passali, George Michalopoulos, Grigorios Tsoumakas
- **发布时间**: 2026-08-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.25881v1](https://arxiv.org/pdf/2608.25881v1)
- **相关度评分**: 10/10

#### 英文摘要

Fine-tuning abstractive summarization models requires high-quality annotated data. However, obtaining such corpora is expensive and time-consuming, as it requires human annotators to read and comprehend long documents to create accurate summaries. Active learning mitigates this issue by selecting only the most informative instances for annotation, allowing models to achieve competitive results with significantly fewer labels. However, the application of active learning to summarization remains under-explored, and existing studies often suffer from instability and significant computational bottlenecks. To overcome these challenges, we propose LOBSTER (LOss-BaSed acTivE leaRning), a novel active learning framework designed specifically for abstractive summarization. LOBSTER improves performance by prioritizing unlabeled instances semantically similar to the model's current high-loss training examples, enabling the model to explicitly correct its specific weaknesses. Our empirical evaluation across three benchmark datasets and two summarization backbone models demonstrates that LOBSTER consistently matches or outperforms current state-of-the-art approaches while achieving a query selection speedup of up to 665x.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training

- **ArXiv ID**: [2608.25826v1](https://arxiv.org/abs/2608.25826v1)
- **作者**: Qiankai Xu, Qiguang Chen, Zixin Su, Wenhao Huang, Yue Gao...
- **发布时间**: 2026-08-26
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2608.25826v1](https://arxiv.org/pdf/2608.25826v1)
- **相关度评分**: 10/10

#### 英文摘要

A recent line of synthetic-data work reconstructs the thinking behind existing text rather than rewriting the text itself, but it operates on short web passages, recovers only local thoughts, and leaves the structure of whole documents untouched. Scientific papers are written to a clear and largely uniform structure and make a natural substrate for lifting this paradigm to the document level. We present a pipeline that unfolds each paper into a multi-turn generation trajectory in which a teacher model reconstructs the writing process of the whole paper: a writing request, a global plan, and pre-writing deliberation for each section. All section texts and the abstract are kept verbatim from the source paper. We apply the pipeline to quality-filtered arXiv papers and obtain a corpus for continued pre-training (CPT) that is roughly twice the size of the source text. The same reverse construction extends to instruction data and evaluation. Treating real paper text as the answer yields an SFT dataset. Anchoring tasks in held-out papers yields PAW-Bench, an academic-writing benchmark whose tasks carry their own rubrics and checklists. In controlled experiments CPT on our corpus followed by supervised fine-tuning on public datasets improves writing benchmarks broadly while preserving general reasoning and improving long-document reading. The writing gain persists even when every model is fine-tuned on a dedicated writing SFT dataset. Mixing our SFT data into that recipe lifts academic writing further.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Learning from waste: Machine Learning for health risk prediction and computer vision-based sorting in Ghana

- **ArXiv ID**: [2608.25759v1](https://arxiv.org/abs/2608.25759v1)
- **作者**: Hilda Adwubi Osei, Catherine Tenewaa Osei, Desdemona Yaa Asobayire
- **发布时间**: 2026-08-26
- **分类**: cs.LG, cs.CV, cs.CY
- **PDF**: [https://arxiv.org/pdf/2608.25759v1](https://arxiv.org/pdf/2608.25759v1)
- **相关度评分**: 10/10

#### 英文摘要

The inappropriate disposal of solid waste remains a significant public health and environmental concern worldwide, including in Ghana. Poor sanitation and improper waste management practices contribute to substantial economic costs and avoidable deaths annually. In 2022, a field study in Atonsu, Kumasi, Ghana, reported a community-perceived relationship between household waste disposal and illness patterns, but only through descriptive analysis without quantitative validation. This study extends that investigation using two data-driven approaches. First, a Random Forest classifier was developed to predict illness categories using waste disposal practices and demographic survey data. On a held-out group of respondents who reported illness (N=69), the model obtained a macro F1 score of 0.63, with disposal method emerging as the most important substantive predictor of illness type. Second, a MobileNetV2 image classification model enabled automated waste sorting via visual recognition, achieving 88.2% accuracy and a macro F1 score of 0.87 on the test set (N=415). The vision-based approach offers an affordable, camera-driven alternative to complex multi-sensor systems, making it highly suitable for resource-constrained settings. Taken together, the findings provide quantitative evidence for a community health relationship previously documented only qualitatively. They demonstrate the potential for automated waste-sorting in low-resource environments. Importantly, the results illustrate that technological performance alone does not guarantee public health improvements; effective institutional support and implementation are equally necessary.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. D3ER: Supporting Multi-Modal Recommendation via Disentangle and Distillation-based Dynamic Ensemble

- **ArXiv ID**: [2608.25737v1](https://arxiv.org/abs/2608.25737v1)
- **作者**: Bingnan Wang, Yi Li, Xiongxin Tang, Fanjiang Xu, Jiangmeng Li
- **发布时间**: 2026-08-26
- **分类**: cs.IR, cs.MM
- **PDF**: [https://arxiv.org/pdf/2608.25737v1](https://arxiv.org/pdf/2608.25737v1)
- **相关度评分**: 10/10

#### 英文摘要

Incorporating items' information shared among multiple modalities into a fused representation, multi-modal recommendation (MR) has demonstrated documented success than canonical unimodal recommendation. Although several attempts have been made to extract the discriminative information unique in each modality, existing methods suffer from a core limitation: the joint learning of modal-homogeneity discriminative information (HOI) and modal-heterogeneity discriminative information (HEI) tends to weaken their individual effectiveness. To remedy this deficiency, we propose a novel method, dubbed Disentangle and Distillation-based Dynamic Ensemble for multi-modal Recommendation (D3ER). We introduce gradient boosting into MR for the first time to formalize the optimization objective for alternately learning HOI and HEI. This design enables models dedicated to each type of information to focus on their proficient samples, thereby promoting specialized optimization. Furthermore, to mitigate the inherent high storage cost and risk of local optima in gradient boosting, we enhance our framework with knowledge distillation and a global correction regularization. Experiments on prevalent real-world datasets confirm the superiority of our proposed method on MR.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale

- **ArXiv ID**: [2608.25735v1](https://arxiv.org/abs/2608.25735v1)
- **作者**: Peichun Hua, Danyang Chen, Junan Zhang, Haifeng Sun, Jingyu Wang...
- **发布时间**: 2026-08-26
- **分类**: cs.CR, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2608.25735v1](https://arxiv.org/pdf/2608.25735v1)
- **相关度评分**: 10/10

#### 英文摘要

Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that the user is authorized to receive. Existing cryptographic approaches either make this costly by processing the entire corpus for every query, or sacrifice quality for efficiency by scanning a few clusters. We repurpose learned deep hashing as a private filter: a randomized binary code points the provider to a short candidate list, while encrypted reranking and oblivious key transfer protect the precise query and final selection. This shortlist short-circuits full-corpus cryptographic search without sacrificing retrieval quality: with 200-500 candidates, it closely matches full-corpus retrieval across five zero-shot corpora spanning 25K to 5.4M documents. On the full 2.68M-passage NQ corpus over a 10-Gbps link, our protocol only adds 0.73 seconds, or 10 percent, to a 128-token Qwen3-32B RAG pipeline. The released code satisfies directional metric differential privacy (DP) and substantially reduces embedding-inversion and property-inference leakage, demonstrating that a carefully learned shortlist can make private dense retrieval both accurate and practical.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond Native Orthography

- **ArXiv ID**: [2608.25904v1](https://arxiv.org/abs/2608.25904v1)
- **作者**: Muge Zhang, Aaron Jencks, Krishna Badikela, Yulia Tsvetkov, Sachin Kumar
- **发布时间**: 2026-08-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2608.25904v1](https://arxiv.org/pdf/2608.25904v1)
- **相关度评分**: 10/10

#### 英文摘要

Multilingual language models transfer knowledge across languages through shared subword vocabulary, a mechanism that breaks down when related languages use different writing systems. Prior work addresses this via script equalization (romanization or IPA transcription), but direct comparisons are rare; the focus has been on encoder-only models, with most work adapting existing pretrained models. We systematically compare different input representations in autoregressive multilingual pretraining, comparing orthographic text, IPA, and romanization in a controlled setup across three scales (467M, 709M, and 1.03B) on eight languages in four typologically motivated pairs. Across a wide range of downstream tasks on seen and unseen languages, romanized pretraining yields the strongest cross-lingual transfer, and the advantage over text widens with scale. IPA improves over text in most settings but trails romanization. Surprisingly, finetuning a text-pretrained model on romanized data hurts performance on languages already covered by the base model, only marginally helping when the model lacks script coverage. Our results indicate that for multilingual models spanning typologically diverse scripts, to obtain maximum benefits, romanization should be treated as a core design choice applied at pretraining rather than a post hoc fix.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. Skill Issue: Are Skills Language-Invariant in LLMs?

- **ArXiv ID**: [2608.25832v1](https://arxiv.org/abs/2608.25832v1)
- **作者**: Bobby Cheng, Adam Gaber, Zhengyuan Liu, Catherine Arnett, Omer Goldman...
- **发布时间**: 2026-08-26
- **分类**: cs.CL, cs.AI, cs.GT
- **PDF**: [https://arxiv.org/pdf/2608.25832v1](https://arxiv.org/pdf/2608.25832v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language models access knowledge inconsistently across languages, but to what extent do they differ in their skill sets when interacting with different languages? This work quantifies cross-lingual skill inconsistency orthogonally from knowledge and general benchmark performance. We do this via multilingual self-play: two instances of the same model compete in a text-based game, each interacting through a different language interface. Since the model, opponent, rules, state space, and available actions remain fixed, this setting isolates the effect of language on the model's realized behavior. We build a multilingual extension to TextArena and evaluate three open-weight models across eight languages and six games covering spatial reasoning, imperfect information, resource allocation, and repeated interaction. We find that the same model can exhibit markedly different playing strength across languages, with systematic variation in win--loss margins, invalid actions, and strategic tendencies. Detailed analyses reveal language-specific failures in spatial reasoning, card-conditioned decisions, and optimal move selection. In some settings, changing only the intermediate reasoning language recovers much of the lost performance, suggesting that language can affect different stages of the decision process. These results show that skill discrepancies are a measurable major roadblock in the development of truly multilingual models. Better understanding these discrepancies can help us design models that perform more equitably across languages.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning

- **ArXiv ID**: [2608.26105v1](https://arxiv.org/abs/2608.26105v1)
- **作者**: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji...
- **发布时间**: 2026-08-27
- **分类**: cs.CV, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2608.26105v1](https://arxiv.org/pdf/2608.26105v1)
- **相关度评分**: 10/10

#### 英文摘要

Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language. Yet progress remains bottlenecked by the lack of scalable training tasks, reliable feedback, and controlled comparisons across generative substrates. In this work, we introduce VBVR-Pro, a closed-loop testbed that makes native visual reasoning through generation trainable, verifiable, optimizable, and experimentally controllable. 1) Task scaling. VBVR-Pro turns visual reasoning into a controlled task space of 300 procedurally generated tasks. Models trained on VBVR-Pro show strong transfer beyond the proposed suite across seven external visual reasoning benchmarks such as RISE-Video, MME-CoF-Pro, and BabyVision. 2) Verifiable rewards. VBVR-Pro provides verifiable reward scorers for task-grounded evaluation. Through a systematic study of leading MLLMs as judges, we identify recurring failure modes of the prevalent VLM-as-a-judge paradigm. In contrast, the proposed scorers are grounded in deterministic, task-specific rules, achieve fine-grained alignment with human judgments. Importantly, they serve as reliable reward signals for large-scale multi-task reinforcement learning and demonstrate stronger post-RL performance across visual reasoning tasks. 3) Mechanism study. VBVR-Pro enables controlled modality studies across more than 30 image, video, and interleaved generators. Our analysis shows that video generation remains strongest for tasks requiring persistent spatiotemporal state tracking, while interleaved generation provides a compute-efficient alternative. Critically, ablations and probing suggest the presence of vision-native trajectories that are crucial to visual reasoning. We release all data, models, scorers, and code.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
