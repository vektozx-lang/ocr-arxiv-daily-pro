# OCR arXiv Daily Pro — 2026-11-13

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-12 09:10 - 2026-11-13 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 186d5283-79

---

## 📄 论文详情

### 1. Validation-Guided Prompt Selection for Differential Morphing Attack Detection

- **ArXiv ID**: [2611.17176v1](https://arxiv.org/abs/2611.17176v1)
- **作者**: Raghavendra Ramachandra, Hailin Li
- **发布时间**: 2026-11-13
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17176v1](https://arxiv.org/pdf/2611.17176v1)
- **相关度评分**: 10/10

#### 英文摘要

Differential morphing attack detection (D-MAD) compares a trusted live capture with a document image that may contain a facial morph. We investigate whether labelled validation data can improve a frozen-parameter vision-language evaluator through prompt selection rather than model fine-tuning. Version~1 generates 50 candidate prompts and selects the top-ranked instruction using a security-oriented loss that prioritises missed morph attacks (MACER) while accounting for bona fide classification errors (BSCER), response failures, parse failures, and decision inconsistency. Version~2 recursively revises prompts using aggregate validation feedback. On a subject-disjoint test set of 160 pairs spanning LMA, MIPGAN-2, and PIPE, the selected Version~1 prompt achieves a (19.17\%) morph attack classification error rate (MACER), with (0.00\%) observed bona fide sample classification error rate (BSCER), compared with (70.00\%) MACER for a controlled manual prompt. The paired (50.83) percentage-point difference has a (95\%) subject-bootstrap interval of ([43.33,58.33]). Recursive revision does not surpass the best Generation~0 validation loss; the reported revised descendant obtains (31.67\%) test MACER. All 23 attacks missed by Version~1 are landmark-based (LMA) morphs. Overall, the results show that prompt formulation can substantially influence frozen-parameter VLM-based D-MAD performance, while also highlighting the challenge of recursive prompt refinement under a compact 10-subject validation setting.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 03422265-f9

---

### 2. SPADE: Soft Prompts for Ai-text DEtection

- **ArXiv ID**: [2611.16929v1](https://arxiv.org/abs/2611.16929v1)
- **作者**: Alex Jiang, Didier Schwab, Chuyuan Li
- **发布时间**: 2026-11-12
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.16929v1](https://arxiv.org/pdf/2611.16929v1)
- **相关度评分**: 10/10

#### 英文摘要

The easy access to Large Language Models (LLMs) has made AI-generated texts on the web increasingly ubiquitous, making AI-text detection a crucial task. Prompts greatly influence the generation process, but existing detectors focus solely on the generated texts --- supervised methods learn from labeled texts only, and zero-shot methods rely on the text's probability distributions --- ignoring the underlying generation process, which limits their robustness in open-world scenarios. We introduce SPADE: Soft Prompts for Ai-text DEtection, a novel framework for detecting AI-generated text that transfers better across datasets. Specifically, we measure the prompt's influence and use it as a discriminative signal. We characterize the prompt's influence by introducing a Pointwise Mutual Information (PMI) term that captures how much a prompt explains a text. Based on this quantity, SPADE trains one soft prompt per class to amplify the separation, and predicts the class whose prompt best explains the candidate text. Extensive experiments on several benchmarks against various detectors demonstrate the robustness and effectiveness of our method, achieving state-of-the-art (SOTA) performance on out-of-distribution (OOD) datasets.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 770f5a14-06

---

### 3. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research

- **ArXiv ID**: [2611.17332v1](https://arxiv.org/abs/2611.17332v1)
- **作者**: Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai...
- **发布时间**: 2026-11-13
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.17332v1](https://arxiv.org/pdf/2611.17332v1)
- **相关度评分**: 10/10

#### 英文摘要

Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace addresses both gaps as a public platform for Recording, Reviewing, and Referencing Architecture Researc}: each proposal is recorded with its experiments and reasoning, reviewed by the community, and referenced by later work. To evaluate ideas before costly large-scale training, ArchSpace leverages scaling laws to predict model loss at larger scales from smaller experiments, a practice widely adopted in industry. We provide initial references that make the platform usable: Qwen3.5 and OLMo3 baselines, fitted scaling laws, and a reusable training recipe. Ideas validated through this review can in turn become new baselines, and ArchSpace thereby aims to broaden the range of ideas that shape the next generation of models.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f58f434e-db

---

### 4. Data Archive for 2D and 3D Electrical Impedance Tomography with moderate conductivity contrast phantoms

- **ArXiv ID**: [2611.17225v1](https://arxiv.org/abs/2611.17225v1)
- **作者**: S. J. Hamilton, A. Hauptmann, A. Hänninen, V. Kolehmainen, J. Niskanen...
- **发布时间**: 2026-11-13
- **分类**: eess.IV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.17225v1](https://arxiv.org/pdf/2611.17225v1)
- **相关度评分**: 10/10

#### 英文摘要

This document describes open Electrical Impedance Tomography (EIT) measurement data that were collected from biomedical imaging inspired phantoms with moderate conductivity contrasts. The data were collected with the KIT4 and KIT5 EIT measurement devices at the University of Eastern Finland, and are intended for EIT image reconstruction algorithm development and testing. The data from thoracic imaging inspired cylindrical and chest-shaped phantoms are suitable for 2D algorithms, and the data from an intracerebral hemorrhage imaging inspired head-shaped phantom with resistive skull are suitable for 3D algorithms. In addition to the measurement data, computational meshes and example reconstruction codes are provided and sample reconstructions included.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0efe10a6-ea

---

### 5. Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration Sensitivity

- **ArXiv ID**: [2611.17035v1](https://arxiv.org/abs/2611.17035v1)
- **作者**: Kuancheng Ye
- **发布时间**: 2026-11-13
- **分类**: stat.ML, cs.CL, cs.CR
- **PDF**: [https://arxiv.org/pdf/2611.17035v1](https://arxiv.org/pdf/2611.17035v1)
- **相关度评分**: 10/10

#### 英文摘要

Watermark detectors decide whether one document came from a watermarked language model. Auditors often need a different number: the share of a corpus that did. We study this share for Gumbel-max and green-list (KGW) watermarks when every document may have been edited by an unknown amount. Without restrictions on the edits, the upper end of the identified set is 1. Combining a known least-favourable next-token distribution with a sequential coupling, we derive a power envelope indexed by three budgets: a retention floor, an entropy budget, and a budget for in-place substitutions, which for Gumbel-max make edited positions look less watermarked than human text. The envelope gives an identified set that is sharp for the alternatives it dominates, finite-sample bounds on the realized share of a fixed corpus with either the exact null or a null calibrated on an independent human sample, and confidence sequences for streams. In Gumbel-max simulations where the envelope binds, the bounds cover, and the threshold that maximizes the gap between envelope and null is generally as tight as twelve thresholds. On text from OPT-1.3B and Qwen3-1.7B, 12,000 fresh human documents scored under three keys show no robust departure from the exact null, and all bounds covered in resampling trials from finite pools of documents with random edits, substitutions and paraphrases; at a share of 0.2 the exact-null bound is about [0.14,0.38]. These results are fragile in two ways we make precise. LLM-paraphrased KGW pools fall below the envelope, yet at 2000 documents the bounds still covered in these trials. A simulated null error of 0.01, comparable to the largest deviation we observed at our thresholds, is likewise harmless at 2000 documents but breaks exact-null coverage at 100,000; a null calibrated on an independent human sample keeps coverage there, but needs a large reference sample to stay narrow.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 46a1af59-27

---

### 6. TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention

- **ArXiv ID**: [2611.16897v1](https://arxiv.org/abs/2611.16897v1)
- **作者**: Hung Nguyen, Quang Qui-Vinh Nguyen, Khoi Nguyen
- **发布时间**: 2026-11-12
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.16897v1](https://arxiv.org/pdf/2611.16897v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce TokenStream, an optimization-based framework that composes independently learned subject identities in text-to-video generation without a reference-video training dataset or joint optimization of each new subject combination. Learning from a single reference image makes subject appearance difficult to separate from static-image bias, while merging independently trained adapters can mix identities. Token-wise LoRA (ToRA) restricts low-rank updates to the cross-attention value projections of subject-associated text tokens, providing a separate adaptation path for each subject. A T2V-guided stream copies queries and keys from the frozen base model during early denoising to reuse its layout and motion priors while retaining personalized values. We also introduce Multi-DB, a 30-subject, 122-prompt benchmark with appearance-free prompts and varied interactions. On Multi-DB at 1.3B, TokenStream improves identity preservation from 0.422 for DreamBooth to 0.467 and textual alignment from 0.652 to 0.688.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9a7f63ce-db

---

### 7. What Limits Thermal Infrared Drone Detection? A Cross-Dataset Benchmark Analysis

- **ArXiv ID**: [2611.16724v1](https://arxiv.org/abs/2611.16724v1)
- **作者**: Tamara R. Lenhard, Jan Kels, Tobias Koch
- **发布时间**: 2026-11-12
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.16724v1](https://arxiv.org/pdf/2611.16724v1)
- **相关度评分**: 10/10

#### 英文摘要

Thermal infrared (IR) imaging enables drone detection with reduced dependence on ambient illumination, supporting continuous surveillance beyond the limitations of visible-spectrum sensing. However, substantial and often undocumented variability in camera systems, processing pipelines, and annotation practices across public IR drone datasets complicates the assessment of detector performance and cross-domain generalization. To examine these sources of variability and their implications for drone detection, we systematically characterize existing IR datasets and establish an artifact taxonomy reflecting their origins across the acquisition and processing pipeline, encompassing optical and sensor effects, tone mapping and image enhancement, and recording-related artifacts. Focusing on long-wave IR data, we investigate the impact of training data composition and model characteristics on YOLO-based detection performance, generalization, and condition-dependent failure modes. Our results demonstrate that detection performance is governed more strongly by training data composition than by YOLO generation or model capacity, while cross-dataset generalization exhibits pronounced asymmetries. Even the best-performing configuration fails to detect over 40\% of drones, with elevated miss rates for very small targets, cluttered urban backgrounds, and thermal crossover, highlighting the shortcomings of existing datasets.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5a1433bb-e7

---

### 8. Lara Mini Base: Language Diversity as a Resource, Not a Trade-off

- **ArXiv ID**: [2611.16956v1](https://arxiv.org/abs/2611.16956v1)
- **作者**: Translated, Maria Pia Adinolfi, Isabelle Andrieu, Grazia Fiorella Anfuso, Melania Annunziata...
- **发布时间**: 2026-11-12
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.16956v1](https://arxiv.org/pdf/2611.16956v1)
- **相关度评分**: 10/10

#### 英文摘要

General-purpose language models are trained mostly on English: over open models we review, at most, non-English pretraining data makes up only a 12% share. Models built for European languages give them far more, but score well below general-purpose models of the same size. A common concern is that, in small models, languages compete for capacity. We present Lara Mini base, a model trained from scratch on 6T tokens in English and 44 other languages, which together cover all 24 official languages of the European Union. As training progresses, the 44 other languages together come to outweigh English. To give these languages enough capacity at low cost, Lara Mini base uses a mixture of experts architecture with 7.2B total and 0.6B active parameters. Among open base models with up to 2B active parameters, it achieves the highest average score across standard English, multilingual, math, and code benchmarks, ahead of models trained on 4 to 6 times as many tokens. Its margin is largest on multilingual benchmarks in the languages it supports and on math benchmarks. It supports contexts of up to 128k tokens. We find that our MoE architecture reduces capacity competition between languages. For a single user on one GPU, without quantization, it generates text at least 1.8 times faster than any model with a higher average score. We release the weights of Lara Mini base under the CC BY-NC-SA 4.0 license. In addition, we will release T-HellaSwag, a higher-quality machine translation of the commonsense reasoning benchmark HellaSwag into 110 language variants.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9a839875-5e

---

### 9. Back to Pixels: Lifting Latent Video Diffusion into Pixel Space

- **ArXiv ID**: [2611.17336v1](https://arxiv.org/abs/2611.17336v1)
- **作者**: Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu...
- **发布时间**: 2026-11-13
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17336v1](https://arxiv.org/pdf/2611.17336v1)
- **相关度评分**: 10/10

#### 英文摘要

Frontier video generation models work in a VAE latent space that compresses video in both space and time. This compression made training tractable, but now limits high-resolution, controllable, and interactive generation -- doubling resolution quadruples token count, conditions apply to groups of frames rather than individual ones, and each response must wait for the rest of its multi-frame block. We present PixVid, a simple yet effective method that lifts a pretrained latent video model to directly generate every frame in pixel space. PixVid keeps the diffusion transformer and replaces the VAE decoder with a convolutional head that renders its outputs into pixels. We find that predicting clean video rather than velocity, together with a larger noise shift, is key to quality. Finetuned from Wan2.1-14B, PixVid is competitive with the latent baseline within $\sim 1.3$M training clips. Working framewise in pixels, it generates at $2\times$ higher resolution with the same per-frame token count, keeps depth-conditioned video editing aligned under fast motion, and responds to each action at the next frame. Project page: https://chenshuo20.github.io/PixVid/

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: da41d07e-10

---

### 10. Unbundling Multimodal Vision Encoding

- **ArXiv ID**: [2611.17334v1](https://arxiv.org/abs/2611.17334v1)
- **作者**: Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis...
- **发布时间**: 2026-11-13
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.17334v1](https://arxiv.org/pdf/2611.17334v1)
- **相关度评分**: 10/10

#### 英文摘要

How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and compute, comparing them cannot isolate the effect of each choice. We disentangle these choices via a controlled framework where we pretrain all models from scratch on common data and compare them on visual question answering and language benchmarks at matched lifetime compute. We find that the visual prior is not necessary; an encoder trained jointly from scratch is on par with a pretrained one, without a separate training stage. What matters instead is dedicated vision capacity: an encoder-free model trails on visual understanding even when its backbone is enlarged by the encoder's parameter count. Yet that capacity need not precede multimodal fusion, as vision-only modules added in-fusion to early backbone layers perform comparably to a pre-fusion encoder and can lower time to first token. These results also hold across backbone sizes, when encoder pretraining is treated as free, and when starting from a pretrained language model. Overall, our findings favor dedicated vision capacity trained jointly with the backbone and placed early within it.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: cf4f15e3-b7

---

### 11. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

- **ArXiv ID**: [2611.17331v1](https://arxiv.org/abs/2611.17331v1)
- **作者**: Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang...
- **发布时间**: 2026-11-13
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17331v1](https://arxiv.org/pdf/2611.17331v1)
- **相关度评分**: 10/10

#### 英文摘要

Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the fast-weight MLP of TTT to learn the cross-view attention mapping explicitly from its input-output pairs, rather than replacing attention entirely, achieving the same rendering efficiency as TTT while delivering substantially higher quality. The second key addresses a modality misalignment between context prefilling and novel-view rendering: we disentangle context tokens into camera-only context rendering tokens to serve as TTB input, and context ground-truth tokens with image content to serve as the TTB mapping target, ensuring the baked MLPs are relieved of the modality generalization challenge between context and novel-view processing. Our method achieves up to **23x** rendering speedup with quality on par with the state-of-the-art across several benchmarks. Project page: https://test-time-baking.github.io

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b94cd308-d9

---

### 12. ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation

- **ArXiv ID**: [2611.17330v1](https://arxiv.org/abs/2611.17330v1)
- **作者**: Guangyuan Sui, Yunzhong Hou, Chi Harold Liu
- **发布时间**: 2026-11-13
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17330v1](https://arxiv.org/pdf/2611.17330v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision language navigation (VLN) is very challenging for Unmanned Aerial Vehicles (UAVs) since small errors in 3D motion prediction can lead to navigation errors and collisions. Unable to fathom execution outcomes in 3D environments, existing methods often struggle to predict accurate navigation waypoints from language instructions. To solve this, we introduce the Prototypical Visual Imagination framework, shortened as ProtoVis-Nav, which forces the model to imagine an outcome-associated local visual representation for the intended next UAV movement. Specifically, we predict feature prototypes and use their linear combination to estimate the visual feature of the target region. In this manner, the VLN model first imagines the local visual representation of the next intended location, and then uses predicted prototypes as context for generating the final action, promoting alignment between visual context and waypoint outputs. Extensive experiments demonstrate the effectiveness of the ProtoVis-Nav framework and show substantial improvements over existing baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6e885751-41

---

### 13. K2V: Generative Keyframing For Physically Plausible Video Generation

- **ArXiv ID**: [2611.17324v1](https://arxiv.org/abs/2611.17324v1)
- **作者**: Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla, Ayush Tewari
- **发布时间**: 2026-11-13
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17324v1](https://arxiv.org/pdf/2611.17324v1)
- **相关度评分**: 10/10

#### 英文摘要

Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. This is because, in a classical video generation setting, all physical reasoning must take place simultaneously and exclusively within the diffusion process.We propose to resolve these issues by redistributing the task of physical reasoning onto a language model-backed keyframe generation module, which allows for explicit reasoning in language, and fine-grained control over the appearance of the video at important moments in the video. We then condition a video generation model with these keyframes, reducing the role of the diffusion model to the simpler task of interpolating between physically-correct intermediate states, rather than inferring an entire sequence with diffusion. Results demonstrate that our approach significantly outperforms existing approaches, achieving state-of-the-art performance on the Physics-IQ Verified benchmark and PhyGenBench.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f725d48c-ec

---

### 14. BrickFlow: Connectivity-Guided Brick Reconstruction

- **ArXiv ID**: [2611.17321v1](https://arxiv.org/abs/2611.17321v1)
- **作者**: Peter Kulits, Cordelia Schmid
- **发布时间**: 2026-11-13
- **分类**: cs.CV, cs.GR
- **PDF**: [https://arxiv.org/pdf/2611.17321v1](https://arxiv.org/pdf/2611.17321v1)
- **相关度评分**: 10/10

#### 英文摘要

Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a set-conditioned SE(3) flow model on procedurally generated assemblies. We then finetune this model to inject image conditioning, using 1% as much data. However, while the learned flow captures global structure, it does not enforce connectivity. To address this, we introduce an analytic connectivity-field guidance to pull predictions toward connected assemblies at test time. Through this, we demonstrate improved build quality with model size, pretraining, and guidance. We make our models and data available for research purposes at https://kulits.github.io/BrickFlow/

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 601c4718-1a

---

### 15. Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

- **ArXiv ID**: [2611.17318v1](https://arxiv.org/abs/2611.17318v1)
- **作者**: Ethan Lin, Yang Song
- **发布时间**: 2026-11-13
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.17318v1](https://arxiv.org/pdf/2611.17318v1)
- **相关度评分**: 10/10

#### 英文摘要

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bounding boxes, and camera trajectories paired with video. Shared scene coordinates link observations across views and time; editable source scenes enable additional camera paths and controlled object changes. We describe the data representation and construction workflow, and discuss applications in floor-plan-conditioned 3D generation, geometric reconstruction, instance-level perception, camera-conditioned video generation, shared world modeling, and scene editing. Controlled camera and scene variations support spatial perception and world-model research. The public project page provides videos and an interactive colored point-cloud preview.

#### 深度分析（中文）

LLM 调用失败: litellm.AuthenticationError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4dd848f4-9a

---
