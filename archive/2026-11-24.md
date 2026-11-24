# OCR arXiv Daily Pro — 2026-11-24

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-23 09:10 - 2026-11-24 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ec8d5ced-2b

---

## 📄 论文详情

### 1. Towards an Armenian Epigraphic Corpus

- **ArXiv ID**: [2611.30603v1](https://arxiv.org/abs/2611.30603v1)
- **作者**: Chahan Vidal-Gor{è}ne, Arpine Avetisyan, Edita Matevosyan, Seda Kirakosyan, Victoria Khurshudyan...
- **发布时间**: 2026-11-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.30603v1](https://arxiv.org/pdf/2611.30603v1)
- **相关度评分**: 10/10

#### 英文摘要

The Divan hay vimagrut'yan (1960-2017), the printed corpus of Armenian inscriptions, comprises nearly 7,600 records; a growing number of the inscriptions they describe, damaged or destroyed in recent decades, survive only in its pages. Armenian epigraphy nevertheless lacks a digital resource of the kind available for Greek, Latin or Georgian. This paper presents the Corpus Inscriptionum Armenicarum Electronicum, which turns the ten volumes of the Divan into an open digital corpus. Layout detection, OCR and a vision-language model produce a first structured reading of each record, which specialists then check on a proofreading platform. First corrections show that letters are read reliably and that residual errors concentrate in the editorial signs. The corpus is designed as a lasting platform for documenting Armenian inscriptions and as a source of silver data in Classical and Middle Armenian for language models and computational linguistics.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 91184160-c1

---

### 2. PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models

- **ArXiv ID**: [2611.30304v1](https://arxiv.org/abs/2611.30304v1)
- **作者**: Shuxuan Li, Jialiang Kang, Yanghao Zhou, Ziye Zhu, Zhilin Zhao...
- **发布时间**: 2026-11-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.30304v1](https://arxiv.org/pdf/2611.30304v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) can localize through their text interface, grounding open-vocabulary objects, complex referring expressions, text lines and layout regions with strong semantic understanding. They write the boxes one after another as a single sequence, although the instances of a query, unlike the words of a sentence, form an unordered set with no sequential dependence. The number of decoding steps therefore grows with the number of instances, which makes dense scenes the most expensive. Decoding the instances in parallel avoids this growth, but streams that cannot see each other duplicate some instances and miss others. We propose \method, which writes a single point into each query as a spatial anchor and asks for the matching instance nearest to that point within a local radius, or \none. Given the image, the anchored queries are independent, so they are decoded in parallel as leaves of a prefix tree that shares the image and the query, and the model is trained on the same tree. Coarse-to-fine anchors refine only the regions where instances are found, duplicate suppression keeps one box per instance, and set-level reinforcement learning optimizes the set F1. Only the prompt and the attention mask change, not the architecture. On three different VLMs and 12 benchmarks covering detection, OCR, layout and referring, \method is at most 5.5 F1 below sequential decoding trained on the same data, while its speedup grows with instance density and reaches 21.9$\times$ on dense scenes.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: abe5d272-a0

---

### 3. When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs

- **ArXiv ID**: [2611.30130v1](https://arxiv.org/abs/2611.30130v1)
- **作者**: Ziqing Ge
- **发布时间**: 2026-11-23
- **分类**: cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.30130v1](https://arxiv.org/pdf/2611.30130v1)
- **相关度评分**: 10/10

#### 英文摘要

Rendering long text as images lets a vision-language model (VLM) read a document with fewer input tokens, and evaluations often count mainly these prefill tokens. We show that for reasoning models this accounting is incomplete. Across five models and two long-context benchmarks, reading the rendered document makes the model think longer: decode length grows by 1.5-3.5x on the four general-purpose VLMs tested, and under typical output pricing this decode tax makes image input more expensive than text for two of the five models on QuALITY. Unrecoverable information loss is not sufficient to explain the tax at moderate compression: Qwen's OCR of the same images recovers 98.7% of words, and feeding Kimi-K3 its own transcription as text restores text-mode reasoning length and accuracy. Whether compression pays off reduces to an exchange rate, (1-1/c)/(r-1), that must exceed the workload's price-weighted ratio of output to input tokens; this accounting decomposition shows why Kimi-K3 and DeepSeek-V4.1-Flash can benefit and Qwen and GLM cannot. None of the training-free signals we test predicts the tax before generation. As a practical heuristic, an image-first policy that sends only inputs with a per-input compression ratio of at least 1.6 to images and falls back to text once image-mode reasoning costs as much as the input's prefill saving cuts the bill by 6-14% on Kimi-K3 and DeepSeek-V4.1-Flash at an accuracy cost of 0.3-1.2 points; on QuALITY, asking for a reasoning budget on both paths is a stronger lever.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d1fc5db4-eb

---

### 4. Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory

- **ArXiv ID**: [2611.31239v1](https://arxiv.org/abs/2611.31239v1)
- **作者**: Chen Wang, Jiahui Huang, Riccardo de Lutio, Alex Trevithick, Bryan Chu...
- **发布时间**: 2026-11-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.31239v1](https://arxiv.org/pdf/2611.31239v1)
- **相关度评分**: 10/10

#### 英文摘要

Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based video generation methods preserve what they have already seen, but have no anchor beyond it, where the camera drifts from its path and a text prompt can name objects but not place them. Layout-conditioned methods provide such an anchor and precise control over what appears where, but rely on layouts that are typically authored by hand. Both limitations arise because, beyond what was captured, nothing anchors the video model unless a human authors one. To overcome both, we propose Lyris, a long video generation framework that never leaves the video model without an anchor: a persistent point-cloud memory where the scene has been observed or generated, and a 3D layout that a vision-language model authors where it has not. Our key insight is that the interface between the two models can be surprisingly coarse. A layout of one labeled 3D box per object is simple enough for a vision-language model to author (and for a user to edit), yet expressive enough for a video model to follow once rendered along the camera path. We demonstrate walkthroughs of over three minutes and 50 meters from a single photo, passing through doorways into rooms it never shows. When evaluated on minute-long round trips across four datasets, Lyris outperforms state-of-the-art methods by a wide margin, reducing camera error by 3.8x and improving consistency upon return by 22% on average.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 39a61d45-f2

---

### 5. Parsing Visual Latents for Multimodal Spatial Reasoning

- **ArXiv ID**: [2611.31021v1](https://arxiv.org/abs/2611.31021v1)
- **作者**: Zhuoying Yang, Yichen Guo, Kathy Jia, Zichang Su, Ayesha Kashif...
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.31021v1](https://arxiv.org/pdf/2611.31021v1)
- **相关度评分**: 10/10

#### 英文摘要

Spatial reasoning across multiple views requires inferring the 3D relations between objects and the camera from 2D observations, which depends on cross-view correspondence and scene geometry that vision-language models (VLMs) do not reliably extract. Pretrained vision encoders already capture this information in their latent features, with CLIP linking objects to image regions, DINOv3 matching semantics across views, and VGGT encoding multi-view geometry. However, VLMs do not benefit from these features when we present them directly in context as grayscale feature images. We therefore propose LatentParse, a training-free framework that parses latent features into explicit spatial evidence for VLMs. In LatentParse, an analyst VLM probes the features of all three encoders with predefined tools that locate objects, track them across views, and measure motion between views. It then distills the results into a concise text report, which is provided together with the images to the VLM to answer the question. We evaluate LatentParse on MMSI-Bench, MV-RoboBench and SPAR-Bench, where it improves all five VLMs over the photo-only baseline by 0.7-2.4 percentage points on average. On MMSI-Bench, it raises Qwen3.8-27B from 34.4% to 39.5%, with the largest improvements of 19.2 percentage points on the camera-related questions. These results suggest that latent features become useful for spatial reasoning once they are parsed into relation evidence, without training. Code is available at https://github.com/Harvard-AI-and-Robotics-Lab/LatentParse.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 62082671-8c

---

### 6. The AMPEL Platform: An Open-Source Project for Developing Hospital-Wide Clinical Decision Support Systems under EU-Regulation

- **ArXiv ID**: [2611.30990v1](https://arxiv.org/abs/2611.30990v1)
- **作者**: Alexander Twrdik, Daniel Steinbach, Martin Federbusch, Clemens Malkawi, Maria Schmidt...
- **发布时间**: 2026-11-24
- **分类**: cs.CY, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.30990v1](https://arxiv.org/pdf/2611.30990v1)
- **相关度评分**: 10/10

#### 英文摘要

As incentives to digitize more and more aspects of medical healthcare are gaining traction, additional medical data is becoming available. A major goal is to use this data to gain further insights, support medical staff, and ultimately improve patient care. This demands sophisticated solutions that can handle current and future vast amounts of data, all without disrupting well-established workflows of care takers. Additionally, the solution must fulfill the documentation and risk-management obligations of the Medical Device Regulation (MDR), which governs whether a device may be used in patient care in Europe. In this context, we introduce the AMPEL platform, an open-source solution for creating clinical decision support systems (CDSS) that fulfil the requirements of the MDR. Centered around a message broker (Kafka), it adopts an event-driven, distributed architecture, allowing for scaling and efficient processing of medical data as it gets generated. Relying on platform-specific events to implicitly describe the platform's interfaces makes it both extensible and agnostic to the hospital information system in use. With these events being defined in the Protocol Buffers format, medically evaluated algorithms can be independently implemented in a variety of programming languages and easily linked to the platform, extending its analytic capabilities as desired. The platform features a basic UI and alert functionality that can be used to gain medical staff's attention and present analysis results in a traceable and explainable fashion. We further show in a use case how the platform was used to build LAMPE, a CDSS developed and operated at University of Leipzig Medical Center. It demonstrates how the platform solution can be used in a complex and already established environment, while acknowledging current limitations and outlining planned developments to overcome these.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 88bb4588-82

---

### 7. Modern Self-Supervised Vision Transformers Are Pareidolic

- **ArXiv ID**: [2611.31238v1](https://arxiv.org/abs/2611.31238v1)
- **作者**: Zihang Lin, Huaiyuan Qin, Liangli Zhen, Qing Guo, Jun Liu...
- **发布时间**: 2026-11-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.31238v1](https://arxiv.org/pdf/2611.31238v1)
- **相关度评分**: 10/10

#### 英文摘要

In human perception, pareidolia is the tendency to perceive a meaningful pattern, such as a face, in a random or ambiguous stimulus.We find a similar phenomenon in modern self-supervised Vision Transformers (ViTs): on white noise, which contains neither objects nor spatial structure, a few directions of their features still form spatially coherent patterns across the patches, imposed by the features themselves.We call this behavior pareidolia, and the span of these directions the pareidolic subspace.On natural images, it holds most of the feature variance in DINOv2 and DINOv3 but little in DINO.This excess explains why DINOv2 and DINOv3, despite stronger dense features, fall far behind DINO in object emergence, the hallmark ability of self-supervised ViTs to identify the patches of an object on their own.Our experiments further show that scaling down their pareidolic subspaces steadily restores their ability to discover objects, so their object emergence is hindered rather than lost.These findings naturally lead to a training-free calibration: Pareidolia Subspace Calibration(PSC) measures the pareidolic subspace only on a noise input and then calibrates the features of natural inputs by scaling its directions down to the variance level of the remaining directions.Across diverse object emergence tasks, PSC improves DINOv2 and DINOv3 by up to 31.7 CorLoc on object discovery, 30.2 maxF on saliency detection and 59.9~$\mathcal{J}$ on video object segmentation.To identify the cause of pareidolia, we trace it block by block and find that it forms in the middle blocks of every self-supervised model we examine but stays strong to the last block only in models trained with a patch-level loss; controlled training confirms that an image-level loss alone lets it fade.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 24ca8343-3a

---

### 8. Let Vision-Language Models Generate Images through Their Representations

- **ArXiv ID**: [2611.31237v1](https://arxiv.org/abs/2611.31237v1)
- **作者**: JB Kim, Byungwoo Jeon, Kyungmin Lee, Hyeonmo Kang, Cheonbok Park...
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.31237v1](https://arxiv.org/pdf/2611.31237v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the heterogeneous visual representations used for understanding and generation. To address this challenge, we introduce Integral, which converts a pretrained vision-language model into a unified multimodal model by constructing a shared visual representation space across the two capabilities. Integral implements this design through two complementary components. Abstraction Fusion constructs shared visual tokens by aggregating hierarchical representations from the frozen vision encoder, while Block-wise MoT introduces a lightweight generative stream that interacts with the vision-language model only at block boundaries. Our approach effectively preserves the pretrained understanding capability while extending it to strong visual generation. Controlled comparisons further demonstrate that sharing visual representations between understanding and generation substantially improves generative learning compared with using a separate visual representation space, despite comparable reconstruction fidelity. These results suggest that representations learned by pretrained vision-language models already provide an effective foundation for visual generation.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c0e3e446-fb

---

### 9. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming

- **ArXiv ID**: [2611.31233v1](https://arxiv.org/abs/2611.31233v1)
- **作者**: Hani Alomari, Md Atabuzzaman, Chris Thomas
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.31233v1](https://arxiv.org/pdf/2611.31233v1)
- **相关度评分**: 10/10

#### 英文摘要

CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect. Yet removing it post hoc degrades retrieval on every CLIP checkpoint we test. We introduce a paired statistic that identifies directions where the two towers agree more on hard negatives than on matched pairs. Mildly attenuating these directions improves retrieval while largely preserving the gap. We arrive at this correction through weight-space programming: guided by the statistic, an LLM agent inspects both towers and writes closed-form weight edits without backpropagation. Free to edit any component, the agent improves COCO test retrieval on all 13 CLIP checkpoints and edits an output projection in 12 of the 13. We distill and refine its recurring correction into TowerBridge, a closed-form recipe motivated by a first-order analysis of the hard-negative margin. Computed in seconds from 25,000 labelled pairs, it requires no model-specific tuning and leaves the architecture and inference cost unchanged. TowerBridge improves COCO test retrieval by 16.8 RSUM and Flickr30k test retrieval by 6.6 on average across all 21 evaluated CLIP checkpoints, including 8 unseen by the agent, while limiting any drop in ImageNet zero-shot accuracy to 0.5 points. It also reduces hubness on all 21 checkpoints and improves retrieval on 4 of 5 dual encoders from other families.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 91d3c923-65

---

### 10. Self-Supervised Dataset Distillation via Mutual Information Maximization

- **ArXiv ID**: [2611.31225v1](https://arxiv.org/abs/2611.31225v1)
- **作者**: Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei, Jiale Cai, Bissan Ghaddar...
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.31225v1](https://arxiv.org/pdf/2611.31225v1)
- **相关度评分**: 10/10

#### 英文摘要

Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations. To bridge this gap, we introduce Mutual Information Prototype Alignment (MIPA), an efficient SSL dataset distillation approach that optimizes synthetic images to preserve augmentation-invariant information. Specifically, MIPA treats synthetic images as learnable prototypes and uses a frozen encoder to assign real samples to them based on feature similarity. A synthetic dataset that preserves such augmentation invariance should yield stable prototype assignments across multiple augmented views of the same real image. MIPA encourages this by maximizing mutual information between cross-view assignments while avoiding trivial solutions in which all real samples are assigned to only a few synthetic prototypes. Evaluations on image classification benchmarks show that synthetic data generated by MIPA yield higher-quality representations than existing distillation approaches while reducing time and storage demands during distillation.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 57999b0e-83

---

### 11. CTLink: A Text-Prompted Segmentation Model for Linking Radiology Report Findings to 3D Chest CT Scans

- **ArXiv ID**: [2611.31222v1](https://arxiv.org/abs/2611.31222v1)
- **作者**: Mohammed Baharoon, Sung Eun Kim, Mahmoud Hussain Alabbad, Lucas Bijnens, Ali Piracha...
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.31222v1](https://arxiv.org/pdf/2611.31222v1)
- **相关度评分**: 10/10

#### 英文摘要

Radiology reports describe findings in text only, without visually marking them on the scan, so readers cannot directly see which abnormality each reported finding refers to. We introduce CTLink, a text-prompted 3D segmentation model that segments findings described in a chest CT report. CTLink was trained on 4123 noncontrast chest CT scans with 9547 segmented report findings, including ReXGroundingCTv2, a newly annotated dataset of 1134 scans and 1895 findings with every instance of each finding segmented. On the 200 ReXGroundingCT validation scans, CTLink achieved a hit rate of 0.816, an instance F1 score of 0.456, and a mean Dice score of 0.400, compared with 0.533, 0.175, and 0.234 for VoxTell, a publicly available text-prompted segmentation model (P < .001 for all). On the test set of the MICCAI 2026 ReXGrounding challenge, an ensemble of seven CTLink models achieved the highest hit rate (0.782) and instance F1 score (0.386) of all 48 participating teams. On 50 test scans segmented twice by independent radiologists, CTLink matched or exceeded inter-rater agreement. Diffuse non-focal findings remained the main limitation, partly because their extent is outlined inconsistently even between radiologists. The CTLink model weights are available at https://huggingface.co/rajpurkarlab/CTLink, and the dataset at https://huggingface.co/datasets/rajpurkarlab/ReXGroundingCT.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 794139ef-1a

---

### 12. LeJEPA Features Are Not Isotropic, and Should Not Be

- **ArXiv ID**: [2611.31216v1](https://arxiv.org/abs/2611.31216v1)
- **作者**: Richeek Das, Pratik Chaudhari
- **发布时间**: 2026-11-24
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.31216v1](https://arxiv.org/pdf/2611.31216v1)
- **相关度评分**: 10/10

#### 英文摘要

The SIGReg term in LeJEPA regularizes features to have an isotropic Gaussian distribution. Our first result is to show that this regularizer, in practice, cannot achieve its goal. We design a modified regularizer to enforce the objective better. This leads to slightly improved performance. For example, on ImageNet-100, our modified regularizer reaches the final accuracy of SIGReg in 1.3$\times$ fewer epochs. Our second result argues that self-supervised encoders should not have isotropic Gaussian features. We show that the alignment term in LeJEPA conflicts with SIGReg, because it couples the magnitude of the features with their directions. In contrast, isotropic Gaussian features would entail independent magnitude and directions. Features obtained with LeJEPA are, in fact, not isotropic. So LeJEPA has two issues. Its regularizer is weak, and the isotropic Gaussian target is too strict. Our third result is about reformulating the isotropic Gaussian regularizer to enforce only the marginal distributions of the magnitude and direction, without enforcing independence. This leads to a simple regularization term, PolarReg, that can be optimized reliably across many different datasets, batch sizes and embedding dimensions without any hyper-parameter changes. On ImageNet-1k, our technique matches the accuracy of LeJEPA and its variants in 4.7$\times$ fewer epochs. It improves the final accuracy by 1.8 points.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1f06a1e0-1e

---

### 13. WorldLatent: A Unified 4D Latent Space for World Perception and Generation

- **ArXiv ID**: [2611.31209v1](https://arxiv.org/abs/2611.31209v1)
- **作者**: Jingxi Chen, Yujia Chen, Cornelia Fermuller, Yiannis Aloimonos, Wen-Sheng Chu...
- **发布时间**: 2026-11-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.31209v1](https://arxiv.org/pdf/2611.31209v1)
- **相关度评分**: 10/10

#### 英文摘要

Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving rise to powerful foundation models for natural language. In contrast, 4D spatiotemporal vision lacks a common representational protocol: perception (such as depth and camera estimation) and generation are either handled by separate one-way pipelines or bolted together from unaligned single-modality spaces. In this work, we introduce WorldLatent, a framework that formulates a unified 4D latent space as a common protocol for both world perception and generation. Rather than relying on fragmented, task-specific models or stacked single-modality representations, our framework proposes a multimodal VAE architecture that compresses and fuses complex 4D visual appearance, geometry, and dynamics into a single structured latent representation. Within this formulation, perception and generation operate as complementary denoising processes over the same latent space, enabling one generative model to learn both capabilities simultaneously within a single training loop. Experiments across representative 4D benchmarks verify that our fused latent protocol achieves specialist-level zero-shot 4D perception, coherent 4D generation, and controllable editing from a single model. By demonstrating that diverse 4D tasks can be seamlessly unified under a shared representational protocol, our work provides a scalable foundation for general-purpose 4D spatial intelligence.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ab3b5d5b-2d

---

### 14. ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents

- **ArXiv ID**: [2611.31198v1](https://arxiv.org/abs/2611.31198v1)
- **作者**: Rui Sun, Junhua Huang, Luca Zancato, Md Mofijul Islam, Kai-Wei Chang
- **发布时间**: 2026-11-24
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.31198v1](https://arxiv.org/pdf/2611.31198v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with insufficient tools by fashioning new ones from familiar parts and reusing them across tasks. Inspired by this, we propose ToolSmith, an automatic tool-generation framework that grows and reuses modules on top of a lean base tool library. We evaluate ToolSmith on three in-domain multimodal search benchmarks and ten out-of-domain benchmarks under a VLM-as-a-Judge protocol. ToolSmith consistently improves over the base library across deployed agents of varying scales, with larger backbones reaping greater gains, demonstrating the scalability of the approach. Our code and data are available at https://threesr.github.io/toolsmith/.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 14e356fb-39

---

### 15. On-Policy Codec Distillation for Efficient All-in-One Video Generation

- **ArXiv ID**: [2611.31184v1](https://arxiv.org/abs/2611.31184v1)
- **作者**: Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha, Matheus Gadelha, Zezhou Cheng
- **发布时间**: 2026-11-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.31184v1](https://arxiv.org/pdf/2611.31184v1)
- **相关度评分**: 10/10

#### 英文摘要

Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Consequently, conditioning quickly dominates the computation cost. Yet most of these tokens carry redundant spatiotemporal information. Our key insight is that identifying what is genuinely new is exactly the problem that classical video codecs have long solved. Thus, we first introduce a codec-based token pruning method that discards redundant tokens. Then, we propose an on-policy self-distillation (OPSD) strategy to train a DiT adapter capable of learning the codec pruning pattern well without quality degradation. Together, they form On-Policy Codec Distillation (CodecOPSD). We scale CodecOPSD to 16 condition modalities on our own video diffusion model, where it prunes 66% of the condition tokens on average with almost no quality drop. Therefore, denoising becomes 2x faster, and the cache memory shrinks by up to 73% in KV cache mode. CodecOPSD also extends to other state-of-the-art pretrained image and video generative models, where its benefit grows further with more conditions, longer frames, and higher resolution.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9b811927-50

---
