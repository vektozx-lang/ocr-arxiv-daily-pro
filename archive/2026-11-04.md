# OCR arXiv Daily Pro — 2026-11-04

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-03 09:10 - 2026-11-04 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cfc25517-1f2e-4

---

## 📄 论文详情

### 1. OCR in the Foundation Model Era: From Specialist Models to Unified Models

- **ArXiv ID**: [2611.04874v1](https://arxiv.org/abs/2611.04874v1)
- **作者**: Zhiheng Li, Zongyang Ma, Jiaxian Chen, Cheng Cui, Yi Liu...
- **发布时间**: 2026-11-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.04874v1](https://arxiv.org/pdf/2611.04874v1)
- **相关度评分**: 10/10

#### 英文摘要

Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era. We define OCR through faithful transcription: within a specified visual scope, OCR should completely reconstruct the text, notation, and document structure observable in the source image, and every textual, notational, or structural element in the output must be verifiable from visual evidence in that image. We trace the development from specialist OCR models toward unified models, examining joint text detection and recognition, structured sequence generation, and the use of pretrained vision-language models (VLMs). We organize contemporary OCR systems into five coexisting families: modular toolkits and task-specific models, specialized document VLMs, hybrid workflows, general-purpose VLMs, and commercial products and managed services. We compare their architectures, data, and training, examining hallucination and omission, insufficient spatial grounding, and inference cost in generative OCR. We review evaluation from character and scene text recognition to parsing individual structural elements and full-page transcription, highlighting gaps in consistent output definitions, attribution of performance to individual components, and coverage of real capture conditions and visible content and structure. Finally, we summarize the challenges facing OCR and discuss directions for future research. We continuously track related work at https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 97f62a05-9701-4

---

### 2. FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing

- **ArXiv ID**: [2611.04303v1](https://arxiv.org/abs/2611.04303v1)
- **作者**: Zhixian Li, Xingsong Ye, Yongkun Du, Yunyan Xiao, Yanglin Huang...
- **发布时间**: 2026-11-03
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.04303v1](https://arxiv.org/pdf/2611.04303v1)
- **相关度评分**: 10/10

#### 英文摘要

In-image machine translation (IIMT) replaces text in an image with its translation while preserving the surrounding visual context. Existing task-specific models achieve convincing performance but require massive paired training images before and after translation. As advanced text-to-image (T2I) models have reached a practically usable level of multilingual text generation, we argue that this capability can be transferred to IIMT and present FlowTranslator. It is a training-free IIMT framework that first employs an OCR model and an LLM to generate the translation prompt, which is injected into the T2I-based diffusion model. To optimize the accurate and natural generation of translated text, we introduce two trajectory controls: Region Coupling Release (RCR) partially decorrelates target-branch noise inside the text region early in the trajectory, while Coupling Expansion (CE) amplifies the emerging edit displacement mid-trajectory. Under the EasyOCR read-back protocol, FlowTranslator achieves average PRIM BLEU and COMET scores of 20.6 and 57.2, respectively, substantially outperforming the strong training-based baseline UniTranslator. On the more challenging and realistic whole-image ScenePair photographs translated into Chinese, it reaches 40.1\% exact-match accuracy and surpasses existing editing systems, some of which only address the text-rendering stage rather than the complete IIMT task. These results establish flow-based editing as a strong, fully training-free baseline for IIMT.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d0b79041-501c-4

---

### 3. OpenBrain: An Auditable Generated-Label Release for Whole-Brain MRI Parcellation

- **ArXiv ID**: [2611.05348v1](https://arxiv.org/abs/2611.05348v1)
- **作者**: Qizhen Lan, Yu-Chun Hsu, Yuxiang Wei, Lijing Zhu, Zenan Sun...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05348v1](https://arxiv.org/pdf/2611.05348v1)
- **相关度评分**: 10/10

#### 英文摘要

Automatic tools can now generate whole-brain MRI parcellations at cohort scale, but generated-label releases often provide little evidence about which cases are reliable enough to reuse. We introduce OpenBrain, a confidence-aware release of 35,838 provenance-verified OpenNeuro T1w cases from 607 source datasets. OpenBrain is organized as an auditable case-record release rather than a directory of standalone segmentation files: each record links a primary parcellation, two committee parcellations, source/license provenance, raw QC-7 measurements, percentile risks, a combined risk score R, and a confidence tier. QC-7 is a reference-free reliability panel over label geometry, image-label consistency, and committee disagreement, so users can filter, weight, audit, or re-threshold generated labels without rerunning inference. We evaluate this released evidence under a frozen protocol. Across external cohorts, lower QC-7 risk corresponds to higher generated-label quality; in fixed-budget training, lower-risk selections improve paired macro Dice over random selection by +3.2 to +3.7 percentage points. OpenBrain also exposes raw axes, committee outputs, provenance, and datasheet documentation, so confidence claims remain inspectable after download. It does not turn generated labels into manual annotations or clinical-grade segmentations. Its contribution is a large open generated-parcellation substrate, a reusable case-level risk-evidence layer, and an external validation protocol for release-time QC. Dataset: https://huggingface.co/datasets/lanqz7766/OpenBrain. Code: https://github.com/lanqz7766/openbrain.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f9912718-cb52-4

---

### 4. Personas Are Not People: Identity as State, Not Attribute

- **ArXiv ID**: [2611.05292v1](https://arxiv.org/abs/2611.05292v1)
- **作者**: Tamunotonye Harry, Yuanyuan Feng
- **发布时间**: 2026-11-04
- **分类**: cs.CL, cs.AI, cs.CY
- **PDF**: [https://arxiv.org/pdf/2611.05292v1](https://arxiv.org/pdf/2611.05292v1)
- **相关度评分**: 10/10

#### 英文摘要

Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is instructed to act out. Every such system assumes that a person's identity is a stable attribute that behaves the same way in every situation the simulation presents. We show that this assumption is not a harmless simplification. Three decades of personality research find the opposite. How a given person behaves varies more across contexts than people vary from one another. Drawing on identity economics, which describes how different situations activate different identities and norms within the same person, we separate behavior into three parts, which are stable traits, the identity a context calls up, and the situation itself. We then prove, under two stated assumptions, that any simulation built on fixed personas, no matter how detailed the personas or how large the underlying model, cannot reproduce the part of a population's behavior that is specific to it and its circumstances. We propose a new evaluation criterion based on this result and a person-in-context design that can meet it in principle. We test one version on a naturalistic Reddit personality corpus and on a published clinical-trial recruitment survey of a community with documented distrust of medical institutions. The design does produce context-dependent behavior when tested directly, but in neither setting does it fully match the real population, and we show where it falls short. The consequence for practice is a risk that synthetic-population evaluations misrepresent the groups whose behavior is most shaped by context, a distortion that richer personas cannot correct.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: deb5e1ef-b670-4

---

### 5. Robust Reconstruction of Power Lines from Incomplete Mobile and Aerial LiDAR Data

- **ArXiv ID**: [2611.05197v1](https://arxiv.org/abs/2611.05197v1)
- **作者**: Mohamed Gaha, Damos Ayobo Abongo, Philippe Massicotte, Eya Ben Kacem, Wael Jaafar...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05197v1](https://arxiv.org/pdf/2611.05197v1)
- **相关度评分**: 10/10

#### 英文摘要

Accurate vegetation-encroachment assessment and risk mitigation require electric utilities to accurately locate and characterize distribution-network assets, including poles and power lines, and distinguish among medium-voltage, low-voltage, neutral, and telecommunication lines. Mobile and aerial Light Detection and Ranging (LiDAR) point clouds provide detailed 3D representations of these assets and their surroundings. However, power-line detection and reconstruction remain challenging because conductor returns are often sparse, incomplete, noisy, or occluded by vegetation. These challenges are especially significant in distribution networks, where lower pole heights and complex line configurations place conductors close to trees. In addition, mobile and aerial LiDAR datasets differ substantially in point density, viewing geometry, spatial coverage, and occlusion patterns. We propose a robust and automated reconstruction method combining scaled density-based clustering, robust polynomial fitting, and iterative fragment merging to recover individual conductors under severe data incompleteness and occlusion. Following semantic classification, the same reconstruction pipeline processes both mobile and aerial LiDAR data without modality-specific code or parameter tuning. The method is evaluated through degradation experiments, benchmarking, parameter sensitivity analysis, and large-scale validation. On the aerial dataset, it achieves 96.87% precision, 96.66% recall, a 96.76% F$_1$-score, and a geometric RMSE of 0.127 m. On the mobile dataset, where conductor-level reference annotations were unavailable, it achieves a point-to-model RMSE of 0.045 m and a reconstruction coverage of 95.27%. Source code, documentation, and evaluation data are publicly available at https://github.com/varen-project.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d9d3776e-c1b5-4

---

### 6. DPAGait: Dynamic Pose-Knowledge-Aware Network for Robust Gait Recognition in the Wild

- **ArXiv ID**: [2611.04950v1](https://arxiv.org/abs/2611.04950v1)
- **作者**: Zenan Lin, Junduan Huang, Kun Liu, M. Saad Shakeel, Wenxiong Kang
- **发布时间**: 2026-11-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.04950v1](https://arxiv.org/pdf/2611.04950v1)
- **相关度评分**: 10/10

#### 英文摘要

Gait biometrics aims at identity recognition by appearance or pose features captured during unconstrained human walking. Existing methods predominantly rely on binary silhouette images, inherently characterized by low information entropy, and fail to fully utilize the dynamic information in gait sequences, limiting their ability to handle cross-time variations effectively. Consequently, these methods encounter significant challenges in the wild. They are susceptible to variations in clothing, carried objects, and viewpoints, as well as dynamic environmental conditions, all of which lead to substantial degradation in recognition accuracy and robustness. To overcome these challenges, we propose a pose-knowledge-aware approach specifically designed for robust gait recognition in the wild. First, we propose a novel Dynamic Pose-Parsing enhanced Silhouette gait representation paradigm that substantially enhances the information entropy and effectively captures fine-grained behavioral cues by integrating pose-parsing cues with traditional silhouettes. Subsequently, we develop a dual-branch Dynamic Pose-Knowledge-Aware Gait network. The framework consists of two complementary branches: (1) a 2D dynamic pose-aware branch that extracts pose-enhanced features from our proposed DPPS representations, and (2) a 3D Skinned Multi-Person Linear branch that leverages the 3D SMPL model to capture rich and comprehensive 3D dynamic pose information. Finally, the features are integrated to facilitate accurate and robust gait recognition. Extensive experiments on four challenging in-the-wild gait datasets demonstrate the effectiveness and generalizability of the proposed DPPS representation. The complete framework is further evaluated on SUSTech1K, CCPG, and Gait3D, where SMPL information is available or can be consistently estimated, achieving competitive performance under diverse real-world conditions.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2400cbcf-a538-4

---

### 7. EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering

- **ArXiv ID**: [2611.04913v1](https://arxiv.org/abs/2611.04913v1)
- **作者**: Guoning Chen, Zhexun Hu, Yifan Wei, Yixuan Weng, Bin Li...
- **发布时间**: 2026-11-03
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.04913v1](https://arxiv.org/pdf/2611.04913v1)
- **相关度评分**: 10/10

#### 英文摘要

Long instructional videos are increasingly used in medical education, industrial training, and procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may be missing, ASR noisy, OCR sparse, and decisive actions briefly shown without narration. Existing VideoQA systems typically return labels or free-form text, making answer support difficult to inspect. We study Long Video Moment Question Answering (LVMQA), where a system returns timestamped answer-supporting evidence. We propose EP-LVMQA, an evidence-preserving coarse-to-fine framework comprising an Uncertainty-Aware Multimodal Evidence Timeline, a Coarse Evidence Planner, and an Evidence-Conditioned Fine Localizer. An evidence card transfers planner scores, matched cues, source-confidence proxies, modality-specific evidence, neighboring context, and a temporal prior between the latter two modules. On MedVidQA, EP-LVMQA achieves 26.1 R1@0.5 and 31.8 mIoU, improving the strongest non-ours results by 6.3 and 5.1 points. It raises Suff.@2 and Ver.@2 to 25.4 and 22.6, gains of 9.5 and 8.8 points. Under matched low-quality perturbations, average relative degradation is reduced from the strongest non-ours value of 14.6% to 11.1%. On Ego4D-NLQ and QVHighlights, EP-LVMQA remains broadly comparable to established task-specific localization methods.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4206f331-014c-4

---

### 8. DreamX: Video Diffusion Model is a Universal Latent Action Learner

- **ArXiv ID**: [2611.05377v1](https://arxiv.org/abs/2611.05377v1)
- **作者**: Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim...
- **发布时间**: 2026-11-04
- **分类**: cs.CV, cs.AI, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.05377v1](https://arxiv.org/pdf/2611.05377v1)
- **相关度评分**: 10/10

#### 英文摘要

Learning a universal action representation from video requires modeling dynamics that are consistent across different executions of the same action yet invariant to changes in embodiment and appearance. Existing latent action models infer actions from visual transitions, but their representations often entangle the underlying action with irrelevant visual variations, limiting transfer across embodiments. We introduce DreamX, which repurposes a pretrained video diffusion model as a universal latent action learner. Our approach extracts compact latent actions from the video model's rich spatiotemporal features, compressing each latent video frame by $\boldsymbol{300\times}$ ($\boldsymbol{1{,}200 \rightarrow 4}$ tokens). In addition, by leveraging the video model's generative prior, these latent actions capture action-relevant dynamics disentangled from visual appearance. The resulting latent space serves as a shared action interface across embodiments (human and robot), environments, and action parameterizations. On LARY-Bench, DreamX achieves state-of-the-art performance among latent action models. Moreover, actions encoded in one setting remain effective in another: the latent space supports any-to-any video transfer and zero-shot action transfer across diverse embodiments and environments. Furthermore, this shared interface also enables policy learning in a compact latent action space, reducing the computational cost of video-diffusion-based policies.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8af8dd1a-3b8a-4

---

### 9. Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments

- **ArXiv ID**: [2611.05361v1](https://arxiv.org/abs/2611.05361v1)
- **作者**: Zhipeng Zhong, Matthew Coombes, Cunjia Liu
- **发布时间**: 2026-11-04
- **分类**: cs.CV, cs.RO
- **PDF**: [https://arxiv.org/pdf/2611.05361v1](https://arxiv.org/pdf/2611.05361v1)
- **相关度评分**: 10/10

#### 英文摘要

Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner surveys. We present a LiDARbased reference-generation pipeline for evaluating the zero-shot performance of feed-forward visual-geometry models alongside conventional structure-from-motion (SfM) methods. The pipeline reuses camera images, LiDAR scans, and reference poses from existing multi-sensor localization datasets to generate per-view depth maps and visible reference point clouds. To address visibility errors in accumulated LiDAR scans, we introduce the LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and automatic scale selection in Hidden Point Removal(HPR). Experiments on TartanAirV2 and TartanGround show that, compared with Poisson surface reconstruction, which is an approach suited to completed scan surveys, the combined HPR and LDGVS filtering retains approximately three times the point density at comparable absolute relative error. We also apply the pipeline to the BotanicGarden dataset to systematically compare depth estimation and 3D reconstruction methods. Feedforward methods produce dense depth predictions efficiently, but their 3D reconstructions can contain duplicated structures. Conventional SfM generally produces more coherent geometry, but its reconstructions remain sparse and more prone to failure in challenging vegetated scenes. The benchmark toolkit and datasets will be released.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 92d3ecca-26cb-4

---

### 10. GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs

- **ArXiv ID**: [2611.05359v1](https://arxiv.org/abs/2611.05359v1)
- **作者**: Qi Yang, Yingzhan Xu, Kai Zhang, Li Zhang
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05359v1](https://arxiv.org/pdf/2611.05359v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves preprocessing, 3D-to-2D mapping, and practical video compression configuration of GS compression. First, for preprocessing, energy-adaptive inter-frame spherical harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed to produces a compact and stable temporal SH AC feature space. It can reduce the data volume of following mapping and practical compression, as well as less complexity while eliminating redundant information. Second, for 3D-to-2D mapping, prior-based Inter-MiniPLAS (P-MiniPLAS) is designed to generate smooth 2D feature maps through prior-based weighting factor inference and small scale remapping. Compared with vanilla Parallel Linear Assignment Sorting (PLAS) and Morton scan, P-MiniPLAS ensures the generated 2D maps are more suitable for the video codec while maintaining a low level of computational complexity. Third, for practical compression, content-aware generalized compression (CA-GC) is developed to use a non-uniform bit-depth split for coordinate map generation, and a coding unit size selection is introduced for efficient compression complexity control, which fully exploits the performance of video codecs without involving normative changes. Experiments demonstrate that GSCV++ reports over 20\% in intra- and 60\% in inter-prediction rate-distortion gains compared with state-of-the-art (SOTA) methods. GSCV++ also achieves faster 2D map generation, encoding, and decoding than other SOTA methods using the same type of video codecs. Ablation studies verify the effectiveness and robustness of the proposed modules and provide insights for subsequent research.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 63b1bd15-2d2c-4

---

### 11. Wonder 4: A Mixture-of-Experts Recipe for Image Quality Enhancement

- **ArXiv ID**: [2611.05294v1](https://arxiv.org/abs/2611.05294v1)
- **作者**: Yunan Wu, Bin Sun, Partha Acharjee, Xiaoyu Wang
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05294v1](https://arxiv.org/pdf/2611.05294v1)
- **相关度评分**: 10/10

#### 英文摘要

A real photograph is often blurry, grainy, compressed, scratched, and low-resolution at the same time. Each defect has its own severity and its own place in the image. The corrections for these defects conflict with each other. Exist- ing models describe the whole image with one description, so they cannot say where each correction belongs. To solve this problem, we present Wonder 4, a mixture-of-experts (MoE) model for image quality enhancement. It corrects several defects of a real photograph at the same time, each in the region where it occurs. Every block of the model holds a mixture of N = 13 experts. A router, trained with the model, sends every image patch to k = 5 of them. No degradation classifier, mask, prompt, detector, or task label is used. Another issue is that standard MoE training, taken from language models, pushes every expert toward equal use. Equal use applies every correction everywhere, even where it is not needed. We replace this rule with a bias that only sets a minimum share of use. Across all patches, an expert used less than this minimum gets higher router scores until it is selected again. An expert above the minimum is not changed, so no expert is forced to be used as often as the others. The bias needs no extra loss. The method adds no extra module and no extra processing step. We evaluate Wonder 4 on DIV2K and Flickr2K, against five published methods and three open-weight pipelines. It reaches the best LPIPS, DISTS, and NIQE on all three test settings (DIV2K x4, DIV2K x8, and Flickr2K x4).

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7577ef64-09ad-4

---

### 12. Anchored Rank-Adversarial Fine-Tuning Pretrained Visual Place Recognition Models

- **ArXiv ID**: [2611.05286v1](https://arxiv.org/abs/2611.05286v1)
- **作者**: Mostafa Kira, Bader Rasheed, Manuel Mazzara
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05286v1](https://arxiv.org/pdf/2611.05286v1)
- **相关度评分**: 10/10

#### 英文摘要

Visual place recognition (VPR) localises a camera by retrieving similar geo-tagged images, and current foundation-model VPR models are accurate across cities, seasons and illumination, but not robust to adversarial perturbations: under a white-box attack on the ranking at an imperceptible budget of 1/255, SuperVLAD and BoQ keep at most 0.2% top-1 recall (R@1) on four benchmarks. We propose anchored rank-adversarial fine-tuning (ARAFT), which fine-tunes a released model with a listwise rank loss on each adversarial query's hardest positive and an anchor to the clean descriptor of the frozen pretrained model. Checkpoints are selected under a clean-accuracy budget fixed in advance, and the full trade-off is reported. Within five validation R@1 points of clean cost, plain adversarial training has no admissible checkpoint, whereas ARAFT raises robust R@1 from zero to 47.3 on SuperVLAD and 55.3 on BoQ; plain adversarial training exceeds this only at about three times the clean cost. Against unbudgeted plain adversarial training on the test sets, ARAFT matches its robust R@1 at 2/255 with about ten more clean R@1 points. At 4/255, plain adversarial training is 6-9 robust R@1 points ahead, while ARAFT still keeps its ten-point clean advantage. Developed on SuperVLAD, ARAFT transfers to BoQ without re-tuning, and its robustness holds against stronger optimisers, with no sign of gradient masking.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c5880d10-ca0d-4

---

### 13. YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction

- **ArXiv ID**: [2611.05280v1](https://arxiv.org/abs/2611.05280v1)
- **作者**: Shengyu Wang, Tengyue Nong, Junming Liu, Haosong Peng, Siyu Li...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05280v1](https://arxiv.org/pdf/2611.05280v1)
- **相关度评分**: 10/10

#### 英文摘要

Unified Multimodal Models (UMMs) integrate visual understanding, generation, and editing within a single unified framework. However, existing unified multimodal datasets and benchmarks remain dominated by single-turn tasks. Even in recent multi-turn datasets, many turns can be solved independently without tracking information across turns. Consequently, they provide limited supervision and evaluation for multimodal stateful interaction, which requires models to understand, maintain, update, and faithfully realize evolving dialogue states across turns. To address this gap, we introduce YANAMI, the first large-scale multimodal dialogue dataset and benchmark for stateful interaction, comprising YANAMI-400K and YANAMI-Bench. YANAMI-400K contains 400K multi-turn multimodal dialogues, with more than 2M images and 2.6M dialogue turns. The dialogues span four representative scenarios: Multi-Image Fusion, Image Editing, World Modeling, and Visual Reasoning, and require models to continuously track, preserve, and revise evolving multimodal dialogue states across turns. YANAMI-Bench comprises 400 multi-turn dialogues for systematically evaluating multimodal stateful interaction. It jointly evaluates Dialogue State Understanding and Visual Realization, characterizing the gap between models' ability to understand evolving dialogue states and their ability to faithfully realize them in visual outputs. Experiments show that fine-tuning BAGEL on YANAMI-400K improves image editing, generation, and multimodal stateful interaction by 10.3%, 2.0%, and 13.23%, respectively, while preserving its general visual understanding capabilities. Evaluations on YANAMI-Bench further reveal that existing UMMs still struggle to maintain, update, and visually realize evolving multimodal dialogue states.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2b1aa54f-6eaf-4

---

### 14. Möbius: A Unified Motion-Language Model Bridging Understanding and Generation

- **ArXiv ID**: [2611.05279v1](https://arxiv.org/abs/2611.05279v1)
- **作者**: Jiazhi Shu, Chengfeng Zhao, Jinyi Wang, Yubo Zhao, Zhiyang Dou...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05279v1](https://arxiv.org/pdf/2611.05279v1)
- **相关度评分**: 10/10

#### 英文摘要

We aim to build a truly unified motion model that can understand, generate, and edit human motion within a single framework. Existing motion UMMs remain only partially unified: motion understanding is handled by a language model, while generation is often delegated to a separate diffusion module operating over learned motion latents. We introduce Möbius, which brings the entire diffusion process into the same multimodal representation space used for motion understanding. Clean motion, noisy motion, and text jointly participate in shared attention, while role-specific parameters process understanding and generation streams. Importantly, Möbius operates directly on continuous frame-level raw motion, requiring neither discrete tokenization nor a pretrained motion VAE. This simple formulation naturally supports motion captioning, text-to-motion generation, temporal completion, and instruction-guided editing within a single model. On HumanML3D, Möbius achieves state-of-the-art performance among unified motion models. Scaling to 1.7B parameters and 1,700 hours of motion data further demonstrates that our framework is both effective and scalable.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f0f2f3ce-7ef6-4

---

### 15. Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems

- **ArXiv ID**: [2611.05275v1](https://arxiv.org/abs/2611.05275v1)
- **作者**: Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.05275v1](https://arxiv.org/pdf/2611.05275v1)
- **相关度评分**: 10/10

#### 英文摘要

Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental question: how can an AI system dynamically select and coordinate the most capable candidate for each task while balancing performance and computational cost? In this work, we present Route Anything, a unified framework for studying model and policy routing across general-purpose AI systems. We develop a unified theoretical foundation that characterizes optimal routing under quality--cost trade-offs and establishes how the information available to a router determines its attainable performance. To systematically investigate routing across diverse capabilities, we first construct an omni-modal trajectory matrix spanning 25 benchmarks across language understanding, image, video, and speech generation, coding and workplace agents, and robotic manipulation, comprising 374,401 scored runs from 452 candidate configurations. Building on this framework, we train and test different routers to investigate the potential of omni-modal model routing, the capabilities of learned routers, and the conditions under which routing improves efficiency. Our results reveal substantial opportunities for capability orchestration: per-input oracle routing outperforms the best fixed candidate by 5.4 points, and learned routers outperform it by 0.3 points across 16 benchmarks, by 2.1 points on video generation, and by 1.1 points on robot manipulation while using 24% less policy time. More importantly, routing raises efficiency by 8.82x on average compared with the reference model.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4a0004a7-8fc5-4

---
