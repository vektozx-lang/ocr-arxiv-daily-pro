# OCR arXiv Daily Pro — 2026-11-05

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-11-04 09:10 - 2026-11-05 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 444e0d16-6a6f-4

---

## 📄 论文详情

### 1. AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing

- **ArXiv ID**: [2611.06449v1](https://arxiv.org/abs/2611.06449v1)
- **作者**: Boyu Niu, Yingjie Xiong, Shurui Li, Linhan Pang, Yuntong Zhang...
- **发布时间**: 2026-11-04
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.06449v1](https://arxiv.org/pdf/2611.06449v1)
- **相关度评分**: 10/10

#### 英文摘要

Traditional document parsing systems use Markdown as their output representation, which is effective for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-sensitive documents whose representations must remain editable, inspectable, and reusable, and introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world document, a model must recover executable HTML that preserves its content, organization, and visual appearance. The benchmark contains 1,115 diverse pages with structured annotations and evaluates predictions in two different ways: The objective protocol aligns ground-truth and predicted rendered blocks and measures table fidelity, page-level text error, and a two-dimensional layout consistency; a complementary reference-anchored protocol measures perceived fidelity by aligning LLM judges with human preferences. Across ten primary multimodal systems, the best objective score is 0.8092, while the subjective winner is different, demonstrating that automatic decomposition and human-perceived fidelity capture complementary properties. We further fine-tune a small-parameter expert model and find that task-specific adaptation yields good performance on document-to-HTML reconstruction task. These results position AmbiHTMLBench as a diagnostic testbed for building smarter and more logical document parsing systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b50eb17a-f0d4-4

---

### 2. Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation

- **ArXiv ID**: [2611.06498v1](https://arxiv.org/abs/2611.06498v1)
- **作者**: Georgios Feretzakis, Alexandros Papaspyridis
- **发布时间**: 2026-11-04
- **分类**: cs.CR, cs.IR, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.06498v1](https://arxiv.org/pdf/2611.06498v1)
- **相关度评分**: 10/10

#### 英文摘要

Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margins at the tolerance (the margin law). Margins are small in five corpora and two embedding models, so an idealised tolerance at the level of floating-point noise leaves up to 5.5% of queries exposed (at most 1.2% in any corpus once exact duplicate documents are excluded), and a threshold calibrated from our CPU INT8-FP32 comparison of a small embedding model (at the empirical 0.1% quantile of honest cosines) leaves 98-100% exposed; on a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39. Integrity audits of compressed vector stores fare no better: on a FAISS product-quantisation index over 57,638 documents, tampered vectors that all pass the audit put the attacker's document first for 25% of targets. Verifying quantisation codes instead, with ambiguity decided by the verifier, a calibrated guard band and canonicalisation, accepted every honest vector in our samples on three platforms and left the publisher no choice. We also show that common floating-point and dynamic-INT8 inference pipelines are not bit-reproducible across batch sizes or architectures, and report pre-registered negative results on abstention, context pruning and semantic screening. We release code and data.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: dac7d78a-e2d6-4

---

### 3. Procedural Adversarial Learning

- **ArXiv ID**: [2611.06890v1](https://arxiv.org/abs/2611.06890v1)
- **作者**: Jack Nugent, Jia Deng
- **发布时间**: 2026-11-05
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06890v1](https://arxiv.org/pdf/2611.06890v1)
- **相关度评分**: 10/10

#### 英文摘要

For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires first finding them, but they may not be in a fixed dataset. We study procedural adversarial learning (PAL), a framework of minimax training and adversarial evaluation which searches the input space of a procedural generator for difficult instances. The procedural generator is an interpretable program mapping a low-dimensional vector of control parameters (e.g. layout, lighting, pose) to a rendered image and its label. We introduce the Simple-PAT algorithm, which uses zeroth-order optimization in the procedural generator's parameter space to propose adversarial training samples that are generated on demand. We also create PAL-Dojo, a collection of efficient procedural generators for surface normal estimation, image segmentation, and human pose estimation. Against a cross-model black-box adversary with 50M aggregate queries, Simple-PAT reduces worst-case error by a geometric mean of 3.15x compared to standard training and 2.63x compared to the strongest robust training baseline. Code is available at https://github.com/princeton-vl/procedural-adversarial-learning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 530d00a0-793d-4

---

### 4. Same Layout, Different Count: What Number Words Do Past Ten in Text-to-Image Models

- **ArXiv ID**: [2611.06840v1](https://arxiv.org/abs/2611.06840v1)
- **作者**: Liang Yue, Eric A. Vance
- **发布时间**: 2026-11-05
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.06840v1](https://arxiv.org/pdf/2611.06840v1)
- **相关度评分**: 10/10

#### 英文摘要

Ask SD3.5-Medium for twelve of an object and then, from the same starting noise, for twenty-five. The picture keeps its layout, but the count changes about as much as it would under a new random seed, and in no consistent direction. We study what number words do once a request passes about ten objects, in five open text-to-image models. Holding the object and the starting noise fixed, we change one thing at a time, and people who never see the request count 3,088 of the images. Every model follows the number for small crowds, but only up to a point, its reach: SD3.5-M and FLUX.1-dev stop following it soon after ten, while FLUX.2 [klein] and Qwen-Image follow it loosely up to twenty-five. Beyond SD3.5-M's reach, the coarse part of the starting noise fixes the composition of the picture but not how many objects it holds: redrawing only the noise finer than an eighth of the image keeps the layout as well as a new number does, and already moves the count two-thirds as far. The number word still reaches the denoiser and acts in its first steps, but nothing we tried gives it a clear direction. Shown instead as a noised grid in the starting latent, the count is drawn: people find it in 59% of images, against 4% when it is only told. Past ten, an exact-match score barely separates a model that follows the number loosely from one that ignores it, and a relative-error score can even prefer a constant guess of sixteen. A same-noise test with a few requests per object tells them apart.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1669d239-1d8e-4

---

### 5. Enabling AWS Cloud FPGA Development Using High-Level Vitis HLS

- **ArXiv ID**: [2611.06829v1](https://arxiv.org/abs/2611.06829v1)
- **作者**: David Rostcheck
- **发布时间**: 2026-11-05
- **分类**: cs.AR, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.06829v1](https://arxiv.org/pdf/2611.06829v1)
- **相关度评分**: 10/10

#### 英文摘要

We present a toolchain for development of ML models on AWS EC2 F2 cloud FPGA infrastructure from high-level language, implementing a complete Vitis HLS to HDK bridge to AFI workflow that has been absent from the academic literature despite eight years of AWS FPGA availability. We introduce a four-level methodology (FP32 PyTorch, bit-accurate quantized Python, HLS C-simulation, physical FPGA) to aid in localizing errors, including FPGA-specific circuit errors. Together these tools allow coding agents to effectively implement FPGA designs from user directions, testing and debugging as needed. We document the deployment workflow, timing closure strategies, and practical HLS engineering decisions that proved crucial. We validate using TinyBERT fine-tuned for address Named Entity Recognition, implementing the embedding layer and the first of four encoder layers on the FPGA hardware. Our implementation streams weights from host DRAM, yielding poor performance compared to CPU/GPU implementations; we discuss forward paths.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9b9e3a87-832d-4

---

### 6. Ranking Agreement Does Not Reveal Paragraph-Edit Agreement in Two Released Paper Acceptance Predictors

- **ArXiv ID**: [2611.06789v1](https://arxiv.org/abs/2611.06789v1)
- **作者**: Shaoliang Yang, Jun Wang
- **发布时间**: 2026-11-05
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.06789v1](https://arxiv.org/pdf/2611.06789v1)
- **相关度评分**: 10/10

#### 英文摘要

A fast acceptance classifier could select revisions for a slower evaluator. We ask whether agreement on existing papers supports that use. We compare a classifier of word and document features with two released text-only acceptance predictors fine-tuned from the same language model with three billion parameters. For 198 papers from the International Conference on Learning Representations, we compare model rankings of the original papers and of paragraph rewrites screened automatically for unchanged facts, claim strength, and attribution. The classifier ranks original papers closely with one predictor and moderately with the other, but shows no detectable agreement with either on which rewrites raise scores. The tests specified in advance used reduced numerical precision. Rounding error dominated the small score responses. We therefore rescored the released weights in full 32-bit precision as a post hoc check; edit agreement remained near zero. At this precision, when each predictor chooses among five rewrites per paper, its average raw score is under two points out of 100 higher than with random choice. The evidence covers presentation rewrites and two open predictors from one family; transfer to costly evaluators remains untested. Revision selectors should therefore be checked against the intended evaluator on the revisions they rank.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 701ad37d-3020-4

---

### 7. Beyond accuracy: what AI assurance needs to establish in public services

- **ArXiv ID**: [2611.06655v1](https://arxiv.org/abs/2611.06655v1)
- **作者**: Louise Yorke
- **发布时间**: 2026-11-04
- **分类**: cs.CY, cs.CL
- **PDF**: [https://arxiv.org/pdf/2611.06655v1](https://arxiv.org/pdf/2611.06655v1)
- **相关度评分**: 10/10

#### 英文摘要

Public bodies increasingly rely on AI-produced evidence, including classifications, summaries and assessments. These outputs can inform policy decisions and service delivery, making their reliability a matter of public accountability. Establishing whether this evidence can be relied upon requires testing its outputs and examining how organisations decide whether those tests are sufficient. We combine technical evaluation with analysis of AI governance requirements, informed by measurement theory and management-based regulation. We compare eight GPT-4o configurations classifying 1,200 UK Prime Minister's Questions into 21 policy topics, against human-coded labels and across unchanged repeats. Accuracy ranges from 68.2% to 70.3%, yet 24.3% of questions receive different labels, with changes in topic shares and rankings. Configurations agree more with one another than with human coding: agreement does not guarantee correctness. Under the implemented score-extraction procedure, the proportion flagged for human review ranges from 0.9% to 41.0%. We analyse 37 UK and EU policy documents. Both sets expect testing and oversight, but reporting expectations do not consistently cover changing answers, shared errors, selective evaluation, substantive conclusions or review routing. Some UK guidance explicitly addresses stability. The UK sample emphasises public bodies checking their own use; the EU places substantial testing duties on providers while leaving them important choices about measures and acceptance thresholds. Without appropriate checks, evidence could misrepresent policy issues, redirect attention or resources, and leave errors undetected. Public policy should require organisations to justify reliance through checks beyond aggregate accuracy, clear responsibility, access to expertise and scrutiny of results.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1110553e-273b-4

---

### 8. One Scale, Four Texts: Gaps, Overlaps and Silent Repairs in Published Grading Schemes

- **ArXiv ID**: [2611.06569v1](https://arxiv.org/abs/2611.06569v1)
- **作者**: Elisa Rovai, Fabio Rovai
- **发布时间**: 2026-11-04
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.06569v1](https://arxiv.org/pdf/2611.06569v1)
- **相关度评分**: 10/10

#### 英文摘要

Category systems often reach their users as text, and readers apply them with tacit repairs. We ask what such a text determines once the repairs are removed, using diabetic retinopathy grading, where one international scale circulates in several documents. We transcribe four texts (the English screening definitions of 2025, the international scale as tabulated in 2017 and as published in 2003, and an Italian guideline of 2015) into one rule language over 24 finding variables, and make every point a text leaves open a named precisification. Exhaustive enumeration of 1,425,807,360 finding profiles, re-derived by an SMT solver and spot-checked by an OWL reasoner, shows that every text that assigns actions leaves some eyes without a category under every reading; that the 2017 tabulation has a proliferative class that is empty when read literally and a macular gap that the 2003 text lacks, so that no function maps the 2003 grades onto the 2017 grades; and that on image findings alone the English and Italian texts order some pairs of eyes in opposite ways. On 927 annotated photographs from three public datasets, with retinal thickening assumed absent, the English text and the 2017 tabulation disagree on referral for 26.8% of the eyes of one dataset (DDR) on which both decide, and in a pre-registered experiment classifiers trained on each text's labels side with their own text. Thickening cannot be seen on a colour photograph; left free, every disagreement involving England becomes undecidable, so it rests on what the camera cannot show. In a second pre-registered study, language models that answered without deliberating repaired most gap and overlap items even when told to read literally, while Claude Sonnet 5.5 and Claude Opus 5.5 reported the defects far more often; within two models, deliberation reduced silent repair without removing it.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2755ff94-6216-4

---

### 9. MKD2World: A Typed Spatial MarkDown World Model For Web Agents

- **ArXiv ID**: [2611.06544v1](https://arxiv.org/abs/2611.06544v1)
- **作者**: Zhihao Nan, Sifan Zhou, Yiming Cheng, Jinkai Zheng, Zheng Zhu...
- **发布时间**: 2026-11-04
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06544v1](https://arxiv.org/pdf/2611.06544v1)
- **相关度评分**: 10/10

#### 英文摘要

Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces. Existing state representations fail to jointly capture interface layout, UI semantics, and explicit locations. We introduce Typed Spatial Markdown (TSM), a Markdown-style textual state representation for desktop web interfaces. TSM serializes block-level and atomic-level UI elements according to their spatial relationships, jointly encoding their types, visual semantics, explicit locations, optional control states, and hierarchical membership. To train a screenshot-to-TSM renderer, we construct AtomBlock-WebUI, a dataset with precise annotations at both granularities. By injecting element-type labels into HTML and directly extracting bounding boxes after rendering, we avoid annotation errors caused by post-hoc inference from webpage structures. Building on TSM, we propose MKD2World, a desktop web world model trained in two stages for current-state description and action-conditioned next-state prediction. During inference, the web agent queries MKD2World as needed and performs a ``digest'' step, in which it interprets each predicted state and extracts task-relevant evidence for selecting the best action. Experiments show that MKD2World-9B achieves an EleF1 score of 26.50 on the out-of-domain test set, outperforming GPT-5.6-Sol(14.98) by 11.52 points. Across Online-Mind2Web tasks, MKD2World-9B improves the success rate of the Qwen3.5-35B web agent from 22.94% to 37.61%, achieving competitive performance among leading open-source GUI world models. Code is available at https://github.com/OmniAI-Lab-CUHKSZ/MKD2World.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 31d494cc-8b07-4

---

### 10. NaijaFacts: A Framework for Disentangling Language from Knowledge in Facts about Nigeria

- **ArXiv ID**: [2611.06504v1](https://arxiv.org/abs/2611.06504v1)
- **作者**: Zainab Afolabi, Nikita Kozodoi, Jack Butler, Babs Khalidson
- **发布时间**: 2026-11-04
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2611.06504v1](https://arxiv.org/pdf/2611.06504v1)
- **相关度评分**: 10/10

#### 英文摘要

Multilingual benchmarks for African languages mostly translate generic questions into local languages, measuring linguistic competence but not whether models know facts about Africa. We introduce \naija, a benchmark of factual and statistical questions about Nigeria, authored by native speakers and grounded in authoritative official statistics, with every question available in English, Nigerian Pidgin, \yoruba, Igbo, and Hausa. Answering similar questions for the UK and US yields a country by language matrix that disentangles a language effect (the model knows the fact but degrades in a low-resource language) from a knowledge effect (the fact is absent in every language). Across eight frontier and Nigeria-adapted models, the knowledge effect dominates: English-query accuracy is 49--50\% for the US/UK but 20\% for Nigeria. The language effect is smaller and tracks web representation, degrading from English to \yoruba{} (9 points on Nigeria, up to 24 on US/UK questions). We find scale does not help: the strongest models reach 66--79\% on the UK and the US but none exceed 31\% on Nigerian statistics. Extending to all 54 African countries with our best performing frontier model shows the same profile continent-wide, 96\% on culture and 98\% on politics against 26\% on statistics, so the gap is not specific to Nigeria.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8e0413da-1231-4

---

### 11. From Pixels to Actions - Towards Native Vision-Language-Action Policies

- **ArXiv ID**: [2611.06918v1](https://arxiv.org/abs/2611.06918v1)
- **作者**: Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang...
- **发布时间**: 2026-11-05
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06918v1](https://arxiv.org/pdf/2611.06918v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch convolutional layers and evolve jointly with language throughout the backbone, allowing a flow-matching action expert to draw from instruction-conditioned visual representations at different depths. This simple change reveals a consistent pattern. Native architectures outperform encoder-based counterparts under controlled comparisons; full fine-tuning reduces but does not erase the gap, and additional scale alone cannot recover it. More strikingly, layer-wise probing shows that the action-critical signals often peak well before the final visual representation. Across diverse manipulation settings and distribution shifts, NEO-VLA consequently achieves stronger and more robust control. Together, these results suggest that embodied control benefits from access to visual representations across the computational hierarchy, rather than a fixed encoder output.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7b46b455-1362-4

---

### 12. Perceptive Humanoid Motion from Simulation

- **ArXiv ID**: [2611.06908v1](https://arxiv.org/abs/2611.06908v1)
- **作者**: Siyuan Hu, Abulikemu Abuduweili, Yue Meng, Shipeng Liu, Quentin Leboutet...
- **发布时间**: 2026-11-05
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06908v1](https://arxiv.org/pdf/2611.06908v1)
- **相关度评分**: 10/10

#### 英文摘要

Humanoid robots have the potential to automate a wide range of physical tasks. Progress toward generalist humanoid autonomy, however, remains constrained by a data bottleneck: mapping pixels and free-form language to low-level joint commands requires paired supervision, and no corpus of such data exists at sufficiently large scale. Some approaches rely on human teleoperation and wearable capture devices, which require at least an hour of human time to produce an hour of data. We present HALO, a humanoid autonomy system powered by a pipeline that synthesizes vision-language-motion data across a thousand procedurally generated homes. The corpus scales with compute rather than human labor. HALO acquires a repertoire of physical skills, including sitting on chairs, navigating to named objects, stepping sideways through half-open doors, crouching and crawling beneath tables, and pushing boxes. It orchestrates these skills to solve composite, long-horizon tasks. Without ever seeing a real home during training, HALO transfers zero-shot to the physical world, achieving a 91% success rate across 360 trials in six unmapped real-world environments. See https://apple-aiml-research.github.io/ml-halo/ for code and videos.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: b853fd1f-769d-4

---

### 13. Motion-guided Contrastive Regularization For Latent World Models

- **ArXiv ID**: [2611.06901v1](https://arxiv.org/abs/2611.06901v1)
- **作者**: Yiwen Chen, Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Huaizu Jiang...
- **发布时间**: 2026-11-05
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06901v1](https://arxiv.org/pdf/2611.06901v1)
- **相关度评分**: 10/10

#### 英文摘要

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify static collapse, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because static content is temporally predictable yet diverse across episodes, this failure can persist despite regularizers such as SIGReg. A controlled study on OGBench-Cube shows that introducing randomized backgrounds substantially degrades planning performance while leaving the underlying manipulation task unchanged. To address this problem, we propose motion-guided contrastive regularization. Our approach compares predicted latent transitions with transitions to candidate observations from the same episode, reducing the usefulness of static background identity for distinguishing action outcomes. Optical-flow similarities provide soft contrastive targets, allowing candidates with similar motion to receive similar supervision. Combined with latent prediction and SIGReg, our objective encourages representations to preserve within-episode state distinctions and similarities between related transitions. Our method improves planning success over LeWorldModel (LeWM) from 52% to 78% on OGBench-Cube with randomized backgrounds and from 14% to 54% on LIBERO-Object, while maintaining comparable performance on four other visual-control benchmarks.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7cfbb933-27b2-4

---

### 14. Occlusion for Free: Detecting Occlusion from the Disagreement Between Two Monocular Distance Cues

- **ArXiv ID**: [2611.06899v1](https://arxiv.org/abs/2611.06899v1)
- **作者**: Chibueze Praise Onyenweaku, Toyibat Adele, Sikirulahi Opeyemi Abdulkareem, Obed Honour Eje
- **发布时间**: 2026-11-05
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2611.06899v1](https://arxiv.org/pdf/2611.06899v1)
- **相关度评分**: 10/10

#### 英文摘要

Knowing that a pedestrian is occluded is useful to a robot even when the detector cannot recover the hidden pixels, but occlusion estimators are normally trained on occlusion annotations that deployment settings rarely have. We show that occlusion can be read off two distance estimates a camera-only pipeline already computes. Apparent height is largely unchanged by occlusion, because the detected box still spans the whole person; monocular metric depth is pulled toward the occluder, because the nearest surface inside the box is what a depth map reports. Only their ordering matters, so no focal length, stature, or depth scale is needed, provided the depth model's error is close to a pure gain, a condition that can be checked without labels. The score detects heavy occlusion on KITTI with AUC 0.909 (0.888 over all annotated pedestrians, including those the detector misses), requires no training and no occlusion labels, and is not a proxy for range: within fixed distance bands it holds AUC 0.894-0.925 while true distance alone sits near chance. On synthetic CARLA scenes with measured visibility it reaches 0.819, against 0.644 for distance alone. We arrived here after measuring three standard architectural responses to occlusion, depth fusion, occlusion-simulating augmentation, and attention, none of which improved detection outside its training distribution in the configurations we tested, and after finding that a detector trained on German roads loses half its accuracy on self-annotated street scenes in Lagos, Nigeria. Signals that need no local annotation are worth more in settings that benchmarks do not represent.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fdb58978-0e8e-4

---

### 15. PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories

- **ArXiv ID**: [2611.06870v1](https://arxiv.org/abs/2611.06870v1)
- **作者**: Wanqi Yuan, Nianyi Li
- **发布时间**: 2026-11-05
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2611.06870v1](https://arxiv.org/pdf/2611.06870v1)
- **相关度评分**: 10/10

#### 英文摘要

Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous correspondence and inconsistent trajectories. We introduce a continuous STVSR framework that combines long-context encoding, continuous HR feature lifting, and an endpoint-anchored PixelSpline. Long-range observations provide more reliable endpoint representations, while continuous upsampling constructs detailed appearance features directly on the requested HR grid. PixelSpline explicitly models each pixel's motion as a single continuous trajectory shared by both endpoints. Using this trajectory, our method warps endpoint colors into a coarse intermediate frame and aligns the HR features for residual reconstruction. Experiments across spatial and temporal upsampling settings demonstrate that the proposed framework offers a favorable quality--efficiency trade-off.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bf0abd46-6aac-4

---
