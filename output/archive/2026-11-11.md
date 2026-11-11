# OCR arXiv Daily Pro — 2026-11-11

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-10 09:10 - 2026-11-11 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2741a3fc-9e

---

## 📄 论文详情

### 1. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference

- **ArXiv ID**: [2611.14469v1](https://arxiv.org/abs/2611.14469v1)
- **作者**: Guorui Lu, Qinyu Chen
- **发布时间**: 2026-11-11
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.14469v1](https://arxiv.org/pdf/2611.14469v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are complementary: cropping highlights small targets and local details, whereas whole-image compression better preserves context for large targets or distributed evidence. Based on this observation, we propose C$^2$-Routing, which adaptively selects cropping or compression according to the input image and question. Since both strategies may still discard key information, we further design a safety gate that uses the predicted joint correctness distribution under original and reduced inputs to guide fallback and protect accuracy. To accommodate consumer GPU resource constraints, all training and evaluation experiments run on RTX 3090 GPUs. To measure gains beyond token capping, we use full-image baselines with the same cap of 1,024 visual tokens. We conduct extensive evaluation on three VLMs and 18 datasets spanning local details, global scenes, scene text, and documents. With the visual budget already capped, C$^2$-Routing further reduces end-to-end FLOPs by 36.53% and visual tokens by 42.36% on average, with a mean relative task-score decrease of only 0.77%.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 60b8953c-9a

---

### 2. Post-OCR Correction of Mixed-Script Uzbek Text: Byte-Level ByT5 with an Empirical Homoglyph Noise Matrix

- **ArXiv ID**: [2611.13609v1](https://arxiv.org/abs/2611.13609v1)
- **作者**: Mannon Ochilov, Oybek Narzullayev, Bahodir Zaripov
- **发布时间**: 2026-11-10
- **分类**: cs.CL, cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.13609v1](https://arxiv.org/pdf/2611.13609v1)
- **相关度评分**: 10/10

#### 英文摘要

In Uzbek official and technical documents, a large share of OCR errors is caused not by poor image quality but by characters that are visually identical across the two alphabets in use. Because the script transition is still under way, Cyrillic and Latin appear on the same page and often within a single sentence, and in our measurements the density of homoglyph errors on such pages is close to five times higher than in single-script text. We study this problem in a setting where the corpus of engineering-geological and ICT infrastructure reports may not leave the organisation, so every stage was executed on local hardware. The proposed system combines a byte-level ByT5 model with a noise generator whose sampling weights are estimated from 359 manually classified error events, together with a Levenshtein-bounded conservative decoding rule. On a Gold set of 5,204 line pairs it lowers the character error rate from 0.0578 to 0.0369, restores 91.3% of the homoglyphs and introduces only 84 new errors.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c841b0dd-26

---

### 3. Word-Level Alignment of OCR and Ground Truth under Zoning and Reading-Order Errors

- **ArXiv ID**: [2611.13752v1](https://arxiv.org/abs/2611.13752v1)
- **作者**: Fonseca Cacho, Jorge Ramón
- **发布时间**: 2026-11-10
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.13752v1](https://arxiv.org/pdf/2611.13752v1)
- **相关度评分**: 10/10

#### 英文摘要

OCR post-processing needs OCR text aligned word by word with its ground truth. Data sets rarely provide that mapping, and a monotone aligner can lose its place when zoning errors permute the reading order. We revisit this problem, the Zoning Problem of our 2019 paper, with a protocol that tests correctness under such permutations. We apply OCR-side reading-order permutations with construction-time word-level gold and score correct-match F1, cascade length and recovery. We compare the 2019 location-aware aligner, a re-anchoring extension of it, a RETAS-style baseline (RETAS-lite), a multi-region aligner that combines unique-word and unique n-gram anchors with chunk-to-window assignment, genalog's RETAS and the original Java RETAS. Experiments use synthetic character noise with block moves, paragraph swaps and column interleaving, historical newspaper reading-order permutations, geometry-derived gold for Tesseract OCR, and a small word-box set. Synthetic tests show where local tracking fails after large displacements and where unique-anchor methods collapse when unique anchors are scarce. On our synthetic boilerplate page the 2019 method had the highest F1 among those tested. Historical newspaper and geometry-derived evaluations carry the limitations of approximate gold and the article-order convention. The first multi-region version has a quadratic scaling cost. Local tracking remains fragile under large reading-order changes; the tested anchor-based methods handle many of those cases but fail when unique anchors are scarce. Approximate gold, the article-order convention, missing residual annotation, and the lack of modern multi-column word-level ground truth remain limitations.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3a78291e-71

---

### 4. From Show Programs to Linked Data

- **ArXiv ID**: [2611.14037v1](https://arxiv.org/abs/2611.14037v1)
- **作者**: Clarisse Bardiot, Bernard Jacquemin, Jacob Hart, George Bruseker, Antonios Lagarias...
- **发布时间**: 2026-11-10
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2611.14037v1](https://arxiv.org/pdf/2611.14037v1)
- **相关度评分**: 10/10

#### 英文摘要

Many heritage institutions hold extensive collections of show programs. Too numerous to be cataloged individually, they remain difficult to access and are still largely undigitized. This paper presents a workflow for transforming such documents into structured, interoperable data by combining vision-language models (VLMs), a custom extension of the Linked Art ontology for the performing arts, and different approaches for automatic semantic data annotation. Using the Festival d'Avignon programs (1947--present), preserved at the Biblioth{è}que nationale de France, as a case study, we demonstrate how VLMs achieve more than 98% text transcription accuracy from heterogeneous heritage document images and how constraining large language model generation through a knowledge graph significantly reduces hallucinations in semantic annotation. We argue that this workflow opens new possibilities for large-scale, interoperable performing arts historiography, including the creation of catalogues raisonn{é}s for performing artists, a form of scholarship common in visual arts but absent in performing arts studies.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e9c96340-cf

---

### 5. AutoThreshold: Joint Confusion-Profile Learning for Adaptive Mask Binarization

- **ArXiv ID**: [2611.14279v1](https://arxiv.org/abs/2611.14279v1)
- **作者**: Shaokai Wu, Xunchu Zhou, Pinzhi Wang, Bo Dong, Xiao Cui...
- **发布时间**: 2026-11-11
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.14279v1](https://arxiv.org/pdf/2611.14279v1)
- **相关度评分**: 10/10

#### 英文摘要

A single validation-tuned threshold can become brittle when dense-score distributions shift. We introduce AutoThreshold, a post-hoc policy that predicts the joint mass of positive and negative pixels over score bins. This target directly parameterizes threshold-indexed confusion counts, avoiding products of independently estimated prevalence and class-conditional rates. Softmax normalization and cumulative decoding yield coherent, monotone confusion profiles; a plug-in decoder then selects a threshold for any $F_β$ objective without retraining the head. Across three independently trained Kvasir pipelines transferred to four polyp datasets, Joint exceeds continuous Otsu by $0.0080 \pm 0.0046$ external macro Dice, with positive gains in 3/3 runs. On the reference pipeline, three head seeds achieve $0.6324 \pm 0.0027$, 0.0085 above Otsu; direct-utility Ridge achieves 0.6342, with the paired difference interval spanning zero. The same Joint checkpoints outperform Otsu for $F_{0.5}$, Dice, and $F_2$. On developmental KITTI Road leave-one-corruption-family-out evaluation, Joint improves over scalar regression by 0.0082 [0.0064, 0.0101], while direct utility is 0.0022 higher. These results establish joint confusion prediction as a useful, metric-retargetable inductive bias, without claiming Bayes-optimal $F_β$ decisions.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c9ad9a69-cd

---

### 6. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- **ArXiv ID**: [2611.14492v1](https://arxiv.org/abs/2611.14492v1)
- **作者**: Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta...
- **发布时间**: 2026-11-11
- **分类**: cs.AI, cs.LG, cs.MA
- **PDF**: [https://arxiv.org/pdf/2611.14492v1](https://arxiv.org/pdf/2611.14492v1)
- **相关度评分**: 10/10

#### 英文摘要

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind each step, merges these conditions across runs into a compact rule document, and generates an executable workflow from it. Only this last stage depends on the platform, so rule documents can be compiled for different orchestration platforms. On $79$ procedures from our production platform, ReTrace workflows reach $93.8\%$ completion, against $96.8\%$ for the agent, at $24\%$ lower cost per task. On $τ^2$-Bench, they reach $75.8\%$ task success (agent: $80.6\%$) and run in $1.3$s instead of $170$s; three rounds of repair on training failures lift $k{=}2$ workflows from $66.7\%$ to $81.2\%$. On eight SOP-Bench procedures, ReTrace without repair trails few-shot generation ($80.6\%$ vs. $83.6\%$), but repair from labeled training failures lifts it to $87.8\%$ at $0.40$s per task, compared to $85.5\%$ in $46.6$s for the agent.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5f0da5a9-2a

---

### 7. From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models

- **ArXiv ID**: [2611.14365v1](https://arxiv.org/abs/2611.14365v1)
- **作者**: Guoqiang Liang, Yiqi Lin, Yanzhe Chen, Kevin Yuchen Ma, Mike Zheng Shou
- **发布时间**: 2026-11-11
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.14365v1](https://arxiv.org/pdf/2611.14365v1)
- **相关度评分**: 10/10

#### 英文摘要

Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bolting on dedicated encoders and decoders. We argue that signal injection is instead a distribution-alignment problem: how well a representation matches the prior of the pretrained VDMs during denoising. Using the relative reconstruction error of a frozen VDM denoiser as a probe, we find that conventional spatial encodings sit far off this prior, whereas frequency-domain packing yields latents that the denoiser corrects far less. Motivated by this diagnostic result, we propose MetaWAM, which folds all robot signals into a single unified meta-frame: each signal is assigned to a disjoint frequency-domain channel band and lifted to the spatial latent by an inverse DCT, yielding a decodable interface aligned with the pretrained VDM prior without any added module or architectural change. A fixed band layout together with slot-aware routing lets the same meta-frame support policy, world-model, and value prediction over a shared set of robot variables. On RoboCasa, MetaWAM reaches 68.9% success while collapsing the per-signal frames into one and cutting inference latency by 39%, and attains 85.0% success on three real-world Franka tasks. Code and models are available at https://github.com/showlab/MetaWAM

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0972ab71-96

---

### 8. Ninety-Six Ways to Measure a Scribe: Fragmented Evaluation of Ambient Scribes in Healthcare

- **ArXiv ID**: [2611.14284v1](https://arxiv.org/abs/2611.14284v1)
- **作者**: Amama Mahmood, Shiye Cao, Laura Fleig, Junan Jiang, Theodore Jensen...
- **发布时间**: 2026-11-11
- **分类**: cs.HC, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.14284v1](https://arxiv.org/pdf/2611.14284v1)
- **相关度评分**: 10/10

#### 英文摘要

Ambient artificial intelligence (AI) scribes have moved rapidly from experimental pilots to enterprise-wide deployment across health systems, promising reduced documentation burden and improved clinician experience. While research evaluating these tools has expanded quickly, there are no agreed-upon protocols or standardized metrics for assessing their performance, making it difficult to compare findings or cumulatively synthesize evidence across studies. Across 54 recent evaluation studies, we identify ten evaluation dimensions and 40 distinct metrics, operationalized in 96 different ways-35 of them (36%) used by only a single study. Assessment is dominated by documentation efficiency and time, measured in 44 of 54 studies. The other dimensions appear at broadly similar rates (16-24 studies each), and safety and clinical outcome least consistently of all. Ripple effects on the broader care system, such as impact on patients' care outcomes, redistribution of work, changes in billing and coding intensity, and downstream use of notes by other clinicians are rarely assessed. Moreover, the metrics used rely heavily on self-report and are fragmented and inconsistently operationalized, which limits comparability and hinders synthesis across studies. As an effort to support more rigorous and cumulative evaluation, in this paper we review the study designs, data sources, and metrics commonly used to evaluate ambient AI scribes in healthcare settings, discuss the limitations of current evaluation practice, and argue for a more holistic approach grounded in a standardized, multi-dimensional set of metrics.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0df8b2a5-eb

---

### 9. MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese

- **ArXiv ID**: [2611.14036v1](https://arxiv.org/abs/2611.14036v1)
- **作者**: Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti
- **发布时间**: 2026-11-10
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.14036v1](https://arxiv.org/pdf/2611.14036v1)
- **相关度评分**: 10/10

#### 英文摘要

Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and target-guided scraping from X with items imported from OLID-BR, a large language model triage stage whose prompt and decoding parameters are released, and manual annotation by three annotators following a written guide. Inter-annotator reliability reaches a Fleiss' kappa of 0.788 over 816 items. Under a single fixed protocol we compare four classical classifiers (Multinomial and Bernoulli Naive Bayes, a linear SVM and a random forest) with fine-tuned BERTimbau Base and Large. The classical models cluster between 0.651 and 0.676 macro-F1 and are precision-oriented but recall-poor. The transformers reach 0.833 macro-F1 and accuracy (Wilson 95% CI for accuracy [0.77, 0.88]), a gap of roughly 16 points, while Base and Large are indistinguishable on the test set despite a 2.6x difference in training cost. We argue that the value of the resource lies less in its headline scores than in the auditability of its pipeline, and we state three limits that users must reckon with: the artificial class balance, whose effect on precision under realistic prevalence we quantify; the association between provenance and label, which the released source field makes measurable; and the selection bias induced by lexicon-guided sampling and automatic triage. The corpus, annotation guide, models and experimental scripts are publicly available.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 89232fba-dc

---

### 10. Program-Aided Patchable Skill Evolution

- **ArXiv ID**: [2611.14019v1](https://arxiv.org/abs/2611.14019v1)
- **作者**: Jiahao Wang, Yuqi Xiong, Qing Yang, Zhipeng Xu, Zhenghao Liu...
- **发布时间**: 2026-11-10
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.14019v1](https://arxiv.org/pdf/2611.14019v1)
- **相关度评分**: 10/10

#### 英文摘要

Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution trajectories and evolving skills based on downstream task feedback. However, existing methods primarily represent skills as natural language documents, intertwining procedural logic with descriptive knowledge and making skills difficult to maintain and evolve. To address this limitation, we propose PASE (Program-Aided Patchable Skill Evolution), a program-aided framework that iteratively evolves skills by associating them with executable programs. Unlike prior approaches that encode trajectory-derived experience primarily in natural language, PASE separates reusable procedural logic into editable programs, enabling targeted updates to executable components while reducing the need to repeatedly revise natural language skills. Extensive experiments across diverse models and benchmarks demonstrate that PASE consistently outperforms all baselines, by achieving over 2.8% improvements. Further analyses show that PASE exhibits greater evolutionary stability and generalisation capability, highlighting the critical role of programmatic knowledge in skill evolution. We will release all data and code via GitHub.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ab92b7b5-51

---

### 11. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR

- **ArXiv ID**: [2611.14518v1](https://arxiv.org/abs/2611.14518v1)
- **作者**: Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, Florin C. Ghesu, Sasa Grbic...
- **发布时间**: 2026-11-11
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.14518v1](https://arxiv.org/pdf/2611.14518v1)
- **相关度评分**: 10/10

#### 英文摘要

DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9e6d214f-b0

---

### 12. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

- **ArXiv ID**: [2611.14498v1](https://arxiv.org/abs/2611.14498v1)
- **作者**: Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón, Alexandre Hyafil, Srikanth Ramaswamy...
- **发布时间**: 2026-11-11
- **分类**: cs.CV, q-bio.NC
- **PDF**: [https://arxiv.org/pdf/2611.14498v1](https://arxiv.org/pdf/2611.14498v1)
- **相关度评分**: 10/10

#### 英文摘要

Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We compare it against CNNs, RAFT, and continuous-time recurrent neural networks without detailed connectome constraints (sCTRNN, CTRNN) on a collision-detection task within a differentiable 3D rendering pipeline. FlyNet is adversarially vulnerable but, relative to its compute, more robust to common video corruptions than RAFT, while using up to five orders of magnitude fewer FLOPs. The CTRNNs remain more robust than FlyNet across almost all tested perturbations, suggesting that connectome constraints benefit efficiency, through their low edge count, over robustness. Recurrence improves robustness to white-box attacks in RAFT and temporal context improves robustness to common corruptions. FlyNet's position and velocity representations degrade under adversarial textures but recover under counterfactual textures that restore correct classification while staying equally far from training, ruling out unfamiliar textures as the cause of failure. The reverse-phi illusion similarly disrupts these representations and inverts the same low-level motion statistic as the adversarial textures. Optimizing this input statistic alone, without access to the network, suffices to induce classification failure, attributing both perturbations to the same circuit vulnerability. Connectome-constrained models can thus surface adversarial failure mechanisms as testable hypotheses about biological perceptual vulnerabilities.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a14ded94-a6

---

### 13. RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval

- **ArXiv ID**: [2611.14496v1](https://arxiv.org/abs/2611.14496v1)
- **作者**: Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan, Gustau Camps-Valls, Swalpa Kumar Roy
- **发布时间**: 2026-11-11
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.14496v1](https://arxiv.org/pdf/2611.14496v1)
- **相关度评分**: 10/10

#### 英文摘要

Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parameters (and up to 398M). We introduce RS-JEPA, a compact joint-embedding predictive framework built on a Vision Mamba encoder shared by both sensors. Since a state-space encoder reads an image as an ordered sequence of patches, we propose scan-path views, which treat two reading orders of the same image as two views with identical pixels and predict the hidden patches in one order from the visible patches in the other.To keep this prediction challenging, we propose Adversarial View Coupling (AVC), which learns the hardest split of the visible patches, and a neighbourhood consensus loss that aligns the scene similarities of both sensors. Extensive experiments on SAR-optical (BEN-14K, CBRSIR-VS) and PAN-MS (DSRSID) benchmarks demonstrate that RS-JEPA achieves the highest F1@5 among twelve re-implemented methods (72.92, 80.35 and 94.43) with a retrieval network of only 3.88M parameters (14.57M in training, 8-16times fewer than prior JEPA retrievers). Like prior methods, RS-JEPA trains on co-registered pairs. Our results highlight reading order as a source of self-supervised views. code: https://github.com/Tanishq251/RSJEPA.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a88b3bb2-3d

---

### 14. Mechanistic Interpretability Needs a Logic of Inference

- **ArXiv ID**: [2611.14483v1](https://arxiv.org/abs/2611.14483v1)
- **作者**: Zhimin Hu, Chen Jiang, Hanbo Xie, N. Apurva Ratan Murty, Sashank Varma
- **发布时间**: 2026-11-11
- **分类**: cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.14483v1](https://arxiv.org/pdf/2611.14483v1)
- **相关度评分**: 10/10

#### 英文摘要

Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of scientific inquiry. Recent progress in mechanistic interpretability (MI) has made it possible to identify neurons, features, circuits, population structures, and dynamical patterns associated with model behavior. As these tools improve, attention is shifting from what can be observed inside a model to how those observations support mechanistic explanations. We examine the parallel efforts of neuroscience and MI to address this question and identify recurring inferential bottlenecks when inferring mechanisms from complex neural systems. We propose five principles and organize them into a recursive logic for a more rigorous procedure of mechanistic inference. These principles provide a framework that supports scientific discovery in two senses: it helps turn local interpretability findings into cumulative knowledge of mechanisms within models, and it makes those mechanisms sufficiently precise to generate testable hypotheses about domains beyond the models. Evidence beyond MI is ultimately required to establish what model mechanisms reveal about the world.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e2ba4cbd-4c

---

### 15. BoviShift: A Six-Year Multi-Attribute Audit of Visual Cattle Phenotyping Across Animals and Time

- **ArXiv ID**: [2611.14476v1](https://arxiv.org/abs/2611.14476v1)
- **作者**: Mobasshir Bhuiya Shagor, Nilambar Halder Tonmoy, Md Saef Ullah Miah
- **发布时间**: 2026-11-11
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.14476v1](https://arxiv.org/pdf/2611.14476v1)
- **相关度评分**: 10/10

#### 英文摘要

Computer vision offers a scalable, non-contact means of estimating livestock traits, but correlated images and video frames make reliable evaluation difficult. Image-random splitting can place views of the same animal in both training and test sets, while deployment further requires transfer to animals captured in future years. We introduce BoviShift, a corpus reconstructed from six consecutive annual cohorts of an operational cattle marketplace collected from 2021 to 2026. It contains 2{,}657 cattle, 10{,}610 still images, and 2{,}566 walk-around videos across nine recorded breed categories. We evaluate three splitting strategies through four configurations: image-random and pooled cattle-disjoint splits over the same development cohorts, followed by separate future-2025 and locked future-2026 evaluations. Using a fixed ResNet-50 multi-task baseline, we assess weight, age, height, breed, and coat color. Differences between image-random and cattle-disjoint splitting are task-dependent rather than a universal leakage penalty. Future-cohort behavior is also attribute- and cohort-specific: breed declines relative to pooled evaluation; mean weight and age performance fails to beat constant baselines in 2025; height remains above baseline; and color transfers well to 2025 but degrades in 2026. Multi-task training improves all five point estimates in a single-seed ablation, still-view aggregation helps selectively, and zero-shot video-frame aggregation exposes a still-to-video domain gap. To our knowledge, BoviShift is the longest-spanning cattle-vision resource combining consecutive annual cohorts with physical and visual attributes.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1e0d8ea0-3e

---
