# OCR arXiv Daily Pro — 2026-11-19

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-18 09:10 - 2026-11-19 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 875de2f5-5d

---

## 📄 论文详情

### 1. Generalization of Text Line Segmentation for HTR in Historical Documents

- **ArXiv ID**: [2611.24726v1](https://arxiv.org/abs/2611.24726v1)
- **作者**: Gayan H. Pathirage, Stephan M. Unter, Simon Corbillé, Elisa H. Barney Smith
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24726v1](https://arxiv.org/pdf/2611.24726v1)
- **相关度评分**: 10/10

#### 英文摘要

In this paper we investigate the generalization capability of state-of-the-art object detection models (Hi-SAM, YOLO, and RT-DETR) for the automatic segmentation of text lines in historical documents. Generalization is needed because it is not practical for museums and archives to produce large amounts of labeled samples for each new collection. We also evaluate the few-shot setting by fine-tuning the networks with only a small number of training samples per target dataset. To this end, we use nine different datasets that differ significantly in visual layout and language. Additionally, we discuss why mean average precision (mAP), a classic evaluation metric for object detection, is insufficient for assessing the quality of a text line segmentation model. Depending on the dataset, our CRNN models achieve character error rates (CER) ranging from 2.48% to 7.07% per page for the segmented text lines. This is sufficient for reading comprehension and simple text searches. Finally, we quantify the resource and time requirements of training and inference in different use case settings. This forms the basis for more informed decisions about model and hardware choices based on available resources.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b716a5cf-76

---

### 2. When Figures Disagree with Text: Evaluating Autonomous Visual Evidence Verification in Scientific Papers

- **ArXiv ID**: [2611.24353v1](https://arxiv.org/abs/2611.24353v1)
- **作者**: Guijia Zhang, Hongbo Qiu, Jiajun Zha, Guohao Cai, Hao Zheng...
- **发布时间**: 2026-11-18
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.24353v1](https://arxiv.org/pdf/2611.24353v1)
- **相关度评分**: 10/10

#### 英文摘要

Scientific figures carry evidence for the claims that cite them, so reviewing a paper means checking that a figure agrees with the text, and not only describing what the figure shows. Benchmarks of figure-text verification typically hand the model the figure, the claim, or the knowledge that an inconsistency exists, which leaves untested whether a model can find the figure worth checking in a complete paper, relate a visual element to the claim it conflicts with, and recognize the conflict. We study this autonomous setting on 31 full manuscripts, each carrying a reviewer-documented figure-text inconsistency from PRISMM-Bench that is hidden from the model. Six multimodal models review each PDF under a neutral prompt, and we then add one input at a time to the same manuscripts. Of 1,445 open-ended reviews, 60.6% mention the flawed figure, yet a grading rubric accepts only 3.3% as diagnosing its contradiction; a blind audit finds the rubric lenient, so we read these as rubric-accepted rates and compare conditions rather than absolute values. In a separate controlled run, naming the figure, without stating that it is flawed, raises rubric-accepted diagnosis from 4.3% to 20.4%, while a consistency instruction and coarse visual cues do not. When the contradiction is visible only in the rendered figure, text-only review yields no accepted diagnosis, while review of the rendered pages with the figure named reaches 15.8%. A baseline that lets the model choose which figures to check, ranked by centrality, stays at 4.8%. Deciding what to verify is thus a large part of the difficulty, and the selection rule we tested does not resolve it. Multimodal document understanding should be evaluated on whether a model can propose what to verify, not only answer questions about a figure it is handed.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7ae71e44-55

---

### 3. SEE: Unlocking the Hidden Perception of Frozen VLMs

- **ArXiv ID**: [2611.23962v1](https://arxiv.org/abs/2611.23962v1)
- **作者**: Alin-Ionut Popa, Tuo Zhang, Dimitrios Dimitriadis
- **发布时间**: 2026-11-18
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.23962v1](https://arxiv.org/pdf/2611.23962v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) grasp the overall content of an image but often miss the fine details a question hinges on, such as a small object in a large photo or a number in a dense infographic. Yet even when their answer is wrong, the region they point to often contains the evidence. We introduce Self-Elicited Evidence (SEE), a training-free method that lets a frozen VLM look again where it points. When the initial answer has low confidence, SEE prompts the model to propose regions where the details may appear, answers the question on these enlarged crops, and aggregates the answers with the original prediction through confidence-weighted voting. The model also answers with its own transcript, which helps on text-rich images. SEE needs no detector or OCR engine. Across five backbones, SEE improves every small-object benchmark by 2.3-13.1 points and outperforms five training-free baselines on small objects. With SEE, Qwen3.5-4B surpasses the direct answer of Qwen3.5-9B and matches the 6 times larger Qwen3.5-27B.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: faddd907-e7

---

### 4. Coverage Governs Accuracy: When to Expand the Lexicon and When to Fall Back in Low-Resource Manchu OCR

- **ArXiv ID**: [2611.23900v1](https://arxiv.org/abs/2611.23900v1)
- **作者**: Ruixin Yu, Zifan Wang, Mingxin Ding, Xiaoxin Sun, Dongjie Wang...
- **发布时间**: 2026-11-18
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.23900v1](https://arxiv.org/pdf/2611.23900v1)
- **相关度评分**: 10/10

#### 英文摘要

Character-level OCR for low-resource Manchu often produces near-miss spelling errors. Lexicon-constrained decoding can correct such errors with lexical knowledge, but a fixed dictionary cannot cover the many unseen word forms produced by agglutinative word formation. We study whether morphological expansion alleviates this limitation, and how the expansion size and confidence fallback affect recognition. We segment the training transcriptions with a dictionary-based stem list, extract roots and suffix chains from them, generate about 510k candidates, select the expansion size through frequency ranking on the validation set, and decompose accuracy under hard lexicon constraints into the product of coverage and in-lexicon precision. Across three CRNN training seeds, adding 250k candidates to a base dictionary of about 29k words raises the type accuracy on unseen combinations of seen roots from 63.6% to 86.3%, and overall token accuracy from 82.4% to 84.2%. Adding all candidates lowers overall token accuracy to 81.5%, showing that the coverage gain comes with a loss of in-lexicon precision. A further comparison shows that the base dictionary with confidence fallback performs best overall among the CRNN systems tested, reaching 76.1% type and 85.5% token accuracy and outperforming the expanded lexicon both with and without fallback. A Transformer recognizer shows similar trends. These results indicate that morphological expansion relieves the constraint of a fixed dictionary, but a larger lexicon does not guarantee better recognition; in the present low-resource Manchu OCR setting, a selective combination of reliable lexical constraints and open recognition is more effective.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a3d3b85b-f0

---

### 5. Mapping the AI Supply Chain: Dependencies, Vulnerabilities, and Market Concentration in the AI Ecosystem

- **ArXiv ID**: [2611.24927v1](https://arxiv.org/abs/2611.24927v1)
- **作者**: Sarah H. Cen, Lindsey A. Gailmard, Joohan Kim, Rishi Bommasani, Daniel E. Ho...
- **发布时间**: 2026-11-19
- **分类**: cs.CY, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.24927v1](https://arxiv.org/pdf/2611.24927v1)
- **相关度评分**: 10/10

#### 英文摘要

AI systems are built across many organizations that contribute models, data, compute, capital, talent, and other assets. While the layers of the AI stack are relatively well understood, the relationships between actors and components across layers remains sparsely documented. In this work, we focus on the organizations that make up the AI supply chain: the complex network of actors that contribute to the development and deployment of AI. We motivate the examination of the organizational AI supply chain---highlighting concerns about concentration, power, chokepoints, cascading failures, fragmented accountability, and risk---then describe our pipeline for mapping the AI supply chain. Our pipeline yields our main contribution: a multilayered, large-scale dataset of actors and relationships in the AI ecosystem, annotated with dates, descriptions, types, tags, and more. This work takes a step toward systematically mapping and measuring the AI supply chain and its properties, cataloging how models, data, chips, infrastructure, capital, and even talent flow between organizations. This data enable critical examinations of industry relationships and yield insights into the political economy of AI development and concentration. We provide several illustrative analyses, including studying the most central actors, analyzing network concentration, and identifying communities and chokepoints. While our dataset is fairly comprehensive, it is also necessarily incomplete: public documents omit private deals, and coverage is shaped by search design. Together, the approach, data, and findings aim to serve as a resource for studying the AI ecosystem. The dataset is publicly available at https://huggingface.co/datasets/sarahcen/ai-supply-chain and can be explored interactively at https://aisupplychains.org/.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0a2b332c-d1

---

### 6. Choosing What to Observe: Budget-Paired Counterfactual Audits for Credible Evaluation of Visual Agents

- **ArXiv ID**: [2611.24867v1](https://arxiv.org/abs/2611.24867v1)
- **作者**: Ruiqi Liu, Jinming Li, Mo Wang, Yang Lu, Yanlan Kang
- **发布时间**: 2026-11-19
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.24867v1](https://arxiv.org/pdf/2611.24867v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual agents that read dense documents must ration a finite observation budget across candidate regions, yet answer accuracy conflates where an agent looks, how it adapts to the reads that remain, and how it an?swers once observation stops. We introduce budget-paired counterfactual audits, an evaluation protocol that holds public evidence and region bindings fixed while perturbing only the remaining budget or de?clared task parameters, and credits every acquired history with exact continuation values. The resulting accounting decomposes lost expected accuracy into stepwise acquisition loss and terminal decision loss, separating planning from fixed-role heuristics. Across forty paired routing anchors, five open-weight

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e9c3937e-88

---

### 7. Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling

- **ArXiv ID**: [2611.24849v1](https://arxiv.org/abs/2611.24849v1)
- **作者**: Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole, William Stern
- **发布时间**: 2026-11-19
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.24849v1](https://arxiv.org/pdf/2611.24849v1)
- **相关度评分**: 10/10

#### 英文摘要

Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scalable judges for automatic relevance labeling. Specifically, ExecJudges uses a frontier LLM to turn assessment guidelines into executable programs, which rely only on lexical matching, standard NLP libraries like parsers, and pool statistics. An ExecJudges-L variant also uses examples of human labels if available. We evaluate ExecJudges on seven TREC collections by comparing the produced labels with trained NIST assessors, frontier LLM judges, and recently proposed per-topic classifiers. Our results show that ExecJudges agrees with NIST assessors at the level of the Claude Sonnet 5.5 LLM judges on TREC DL 2019-2021. With a small number of human labels per topic, the ExecJudges-L variant agrees with NIST more than per-topic classifiers with the same labels on all seven collections, and either exceeds the agreement of LLM judges provided the same labels or is within about 0.05 of it in Krippendorff's alpha. The labels rank the official TREC DL runs with Kendall's tau of 0.87 to 0.94, and writing the programs incurs a one-time cost of $0.17 to $0.49 per topic, with no additional costs for grading. Our results suggest that ExecJudges offers a reproducible, inspectable, efficient and cost-effective alternative to LLM judges for labeling deep result pools for system evaluation or ranking improvements.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f31db9cc-ec

---

### 8. ShoWorld: Shape-Faithful Multi-Hypothesis Occupancy World Model

- **ArXiv ID**: [2611.24457v1](https://arxiv.org/abs/2611.24457v1)
- **作者**: Zhiqiang Yan, Guangfa Wang, Yuan Wu, Jian Yang, Gim Hee Lee
- **发布时间**: 2026-11-18
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24457v1](https://arxiv.org/pdf/2611.24457v1)
- **相关度评分**: 10/10

#### 英文摘要

Occupancy world models struggle to forecast moving objects due to motion uncertainty and shape distortion. A single trajectory can average plausible futures into an implausible path, and repeated re-voxelization can erode or inflate object shape even under correct motion. We introduce ShoWorld to address these challenges through separate motion and shape representations. The motion forecaster predicts probabilistic trajectories conditioned on scene layout, nearby agents and the future ego trajectory. Each hypothesis is rendered into occupancy and fused according to its probability to retain alternative futures. The shape component predicts sub-voxel points with occupancy probabilities and offsets from local geometry. These points move rigidly with the object, and voxel occupancy follows the probability that at least one occupied point falls within it. This representation reduces shape distortion under motion. ShoWorld achieves state-of-the-art results on Occ3D-nuScenes. With ground-truth occupancy and ego trajectory, it improves mIoU and IoU by 6.56 and 9.16 points overall and by 6.06 and 5.53 points on dynamic classes.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1b05b540-80

---

### 9. UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation

- **ArXiv ID**: [2611.24941v1](https://arxiv.org/abs/2611.24941v1)
- **作者**: Jingzhi Bao, Xiaohe Ma, Hong Li, Yuanming Hu, Xiaoguang Han
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24941v1](https://arxiv.org/pdf/2611.24941v1)
- **相关度评分**: 10/10

#### 英文摘要

Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view framework that moves beyond appearance matching by integrating physical knowledge into multi-view diffusion-based PBR generation. UltraTex first jointly predicts albedo and world-space shading normals to generate more detailed albedo maps, and then predicts metallic-roughness (MR) maps conditioned on the generated albedo, reference image, and material semantic priors. To inject material semantics, a lightweight adapter transforms hidden-layer features of a vision-language model (VLM) into intrinsic material representation tokens, providing part-level knowledge anchors for MR estimation. To model material-light interaction, photometric representation alignment guides intermediate diffusion features toward ground-truth material renderings under controlled lighting. This makes metallic and roughness variations observable through highlight intensity, specular sharpness, and local reflectance contrast, providing stronger guidance for fine-grained material prediction without explicit lighting supervision. Extensive experiments show that UltraTex generates high-quality textures and outperforms existing open-source and commercial methods in visual fidelity, material accuracy, and physical plausibility.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0e9e5c13-78

---

### 10. $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

- **ArXiv ID**: [2611.24940v1](https://arxiv.org/abs/2611.24940v1)
- **作者**: Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong...
- **发布时间**: 2026-11-19
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24940v1](https://arxiv.org/pdf/2611.24940v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight instead predicts the future directly in the visual token space in which its VLM perceives the present. Coupling a foresight expert and a continuous action expert with the VLM in a mixture-of-transformers, $Z$-sight jointly denoises future spatial tokens and actions at inference without pixel reconstruction or external encoders. Trained on human video and robot trajectories, $Z$-sight achieves 81.9% success on SIMPLE (+9.6 points over the strongest baseline) and 73.3% across six Unitree G1 tasks (+20.0 points) at 110 ms per chunk, while remaining competitive on tabletop benchmarks.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8cc9903a-e4

---

### 11. Unified Law for Visual Tasks (The Four Laws of Computer Vision)

- **ArXiv ID**: [2611.24917v1](https://arxiv.org/abs/2611.24917v1)
- **作者**: Sen Fang, Yalin Feng, Yancheng Zhang, Yanxin Zhang, Zonglin Lyu...
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24917v1](https://arxiv.org/pdf/2611.24917v1)
- **相关度评分**: 10/10

#### 英文摘要

In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Our starting point is an inspiration and hypothesis: if the world information is encoded into image, which we call World Snapshots, then image processing is world processing, and image generation is World Snapshot generation. Furthermore, if all visual and visualization tasks can be reformulated as generation tasks, then a unified method, World Snapshot Models (WSMs), can perform the vast majority of visual tasks, much as large language models have largely unified natural language processing. This paper validates these laws across more than 1,000 trained and evaluated visual tasks (defined by distinct input-output mappings) and presents a unified training framework for future visual-task research and applications.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 76789a7c-18

---

### 12. PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration

- **ArXiv ID**: [2611.24915v1](https://arxiv.org/abs/2611.24915v1)
- **作者**: Zhaocheng Yu, Kui Jiang, Jing Cao, Yiang Chen, Xiaocheng Feng...
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24915v1](https://arxiv.org/pdf/2611.24915v1)
- **相关度评分**: 10/10

#### 英文摘要

Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on task-dependent yet overlapping channel responses in the shared model. An offline task-prior search uses activation and gradient statistics to group channels with similar response profiles, then searches task-specific modulation coefficients over non-representative channels while leaving representative channels unmodulated. The resulting prior bank enables explicit action selection and composition without additional restoration backbones or task-specific adapter modules. A state-conditioned policy learns to compose these actions using Group Relative Policy Optimization. Its objective separately normalizes fidelity and perceptual feedback within groups of trajectories sampled for the same input, and combines terminal evaluation with return-to-go derived from stepwise quality changes. Experiments on synthetic composite-degradation and real-world multi-task benchmarks show improvements over the evaluated all-in-one baselines and restoration quality competitive with multi-model agents. PrismRestore achieves these results with a single restoration backbone and faster inference than the evaluated agentic baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 471c8480-9b

---

### 13. ShadowTransfer: A Geographic Transfer Benchmark for Overhead Shadow Detection

- **ArXiv ID**: [2611.24904v1](https://arxiv.org/abs/2611.24904v1)
- **作者**: Shagun Mittal, Raymond A. Yeh, Satish Ukkusuri
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24904v1](https://arxiv.org/pdf/2611.24904v1)
- **相关度评分**: 10/10

#### 英文摘要

Overhead aerial imagery feeds dense-prediction pipelines that are routinely trained in one geographic region and deployed in another, yet no benchmark measures how shadow detection models transfer across regions. Existing overhead shadow datasets either lack a geographic transfer protocol or rely on automatically generated labels. We introduce ShadowTransfer, a benchmark of 4,500 human-verified shadow masks across three U.S. cities at two native resolutions, paired with a leave-one-city-out evaluation protocol. Under vanilla training, holding out the test city costs 3.5 to 7.8 mIoU across four architectures, the gap remains significant when the training set grows from 225 to 900 images, and six of eight adaptation methods degrade more than vanilla training on average. We propose a three-probe framework that diagnoses where and how the transfer breaks: the failure operates in feature space, beyond the reach of pixel-histogram matching, shows up as a confidence collapse on shadow pixels while background confidence stays intact, and is recoverable by retraining different architectural components depending on the model: encoder for some, decoder for others. These findings replicate on INRIA building footprints, suggesting they describe geographic transfer beyond shadows. Guided by the diagnosis, we build Spectral Information Bottleneck (SIB), a plug-in module with one component per finding. Across the 9 (architecture, held-out city) cells, SIB has the smallest mean gap to the within-city upper bound of the ten methods we evaluate (6.42 mIoU), level with FDA. The benchmark, LOCO protocol, code, and trained models are released to support reproducible evaluation of geographic transfer in overhead dense prediction.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a4d60b36-66

---

### 14. NereidVLA: Learning to Understand and Navigate the Underwater World

- **ArXiv ID**: [2611.24864v1](https://arxiv.org/abs/2611.24864v1)
- **作者**: Chenjie Zhao, Zhiliang Zhu, Quan Chen, Yuquan Xue, Xingxue Shi...
- **发布时间**: 2026-11-19
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.24864v1](https://arxiv.org/pdf/2611.24864v1)
- **相关度评分**: 10/10

#### 英文摘要

Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories. We present NereidVLA, a vision-language-action model that transfers marine spatial knowledge to language-conditioned 3D navigation. We first train Sea2Know on approximately two million marine examples to learn target grounding, spatial relations, and scene structure without paired robot-motion supervision. We then adapt it using expert trajectories executed under simulated underwater vehicle dynamics. Given RGB histories and a language instruction, NereidVLA predicts discrete motion tokens that decode into local 3D trajectories for closed-loop tracking. Evaluation combines an independent six-dimensional underwater navigation understanding benchmark with offline prediction and closed-loop navigation. Under matched navigation training and execution settings, marine spatial pretraining increases simulation success from 72.4% to 84.4%. Without fine-tuning on the real test environment, NereidVLA achieves 78.75% success in laboratory-pool robot trials, compared with 47.50% for InternVLA-N1. These results show that marine spatial supervision can support downstream motion learning and physical underwater navigation.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bf1f5743-5e

---

### 15. Gaspard: Expressive unified speech and gesture synthesis with continuous autoregressive flow-matching and decoupled classifier-free guidance

- **ArXiv ID**: [2611.24862v1](https://arxiv.org/abs/2611.24862v1)
- **作者**: Téo Guichoux, Théodor Lemerle, Catherine Pelachaud, Nicolas Obin
- **发布时间**: 2026-11-19
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.24862v1](https://arxiv.org/pdf/2611.24862v1)
- **相关度评分**: 10/10

#### 英文摘要

Human communication involves highly coordinated multimodal signals such as speech and co-speech gestures. Existing approaches for generating both modalities commonly follow a cascaded pipeline, where speech is generated first and subsequently used to drive gesture generation; speech generation is therefore independent of gestures. We introduce Gaspard, a unified speech--gesture generation model based on continuous autoregressive generation with next-step flow-matching predictions, and trained on Seamless Interaction, a large-scale multimodal dataset. The heterogeneous temporal properties of speech and gesture motivate modality-specific prediction heads and decoupled classifier-free guidance over the two generation streams. This guidance rebalances the influence of speech and gesture at inference time, improving expressivity while mitigating dynamics collapse in continuous autoregressive gesture generation. Objective and perceptual evaluations show that Gaspard is a strong gesture generation model against unimodal baselines and that it produces highly synchronous speech and gestures compared to a matched cascaded system.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 607dd879-d3

---
