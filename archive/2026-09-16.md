# OCR arXiv Daily Pro — 2026-09-16

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-15 09:10 - 2026-09-16 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. Tables Decoded: DELTA for Structure, TARQA for Understanding

- **ArXiv ID**: [2609.17458v1](https://arxiv.org/abs/2609.17458v1)
- **作者**: Jahanvi Rajput, Dhruv Kudale, Saikiran Kasturi, Utkarsh Verma, Ganesh Ramakrishnan
- **发布时间**: 2026-09-16
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.17458v1](https://arxiv.org/pdf/2609.17458v1)
- **相关度评分**: 10/10

#### 英文摘要

Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rely on vision- language models (VLMs) operating on table images, we propose a more scalable and effective alternative based on structured textual representations. These representations are easier to process, align more naturally with LLMs, and eliminate the need for language-specific visual encoders, making them particularly suitable for multilingual documents. We present DELTA, which separates physical structure recognition, logical structure recognition, and OCR to extract both layout and content accurately. DELTA outputs tables in Optimised Table Structure Language (OTSL), a compact and unified format that encodes cell arrangements and textual content. On table structure recognition (TSR), DELTA achieves TEDS- Structure scores comparable with state-of-the-art methods across FinTabNet, PubTabNet, and PubTables-1M. We further establish its robustness on non-English tables through our curated Hindi benchmark, TORQUE. Building on this, we introduce TARQA, an LLM fine-tuned on OTSL sequences. Our approach yields gains of 9.3 p.p. on WTQ (TabQA) and 9.2 p.p. on FinTabNetQA (TabVQA), respectively. On TORQUE, our method ranks second among all VLMs and DELTA + LLM variants. We release our code, models, and benchmark at: https://github.com/Tihiitborg/Tables-Decoded

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. Measuring Annotation Efficiency for Handwritten Devanagari Recognition: Sample-Complexity Curves for Four Pretraining Regimes

- **ArXiv ID**: [2609.16859v1](https://arxiv.org/abs/2609.16859v1)
- **作者**: Manglesh Kumar Pandey, Sumit Kumar Banshal
- **发布时间**: 2026-09-15
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.16859v1](https://arxiv.org/pdf/2609.16859v1)
- **相关度评分**: 10/10

#### 英文摘要

To train handwritten text recognition systems we need word images and their corresponding transcriptions, and these transcriptions are produced manually. For a script that can be read by only a small number of specialists, this manual transcription is a limitation, because the trained models are supposed to save the time of those same specialists. A relevant question therefore arises: how many transcriptions are needed before a recogniser becomes useful, and how much of that cost can pretraining remove? In this study the answer is measured directly for handwritten Devanagari. We keep the recogniser, optimiser and evaluation protocol the same and change only the number of real transcribed words used for fine-tuning across nine budgets from 10 to 4,000 and four initialisation regimes, with six seeds at every point. The resulting curves are then converted into annotation-equivalent terms. A CER of 0.50 is reached by supervised synthetic pretraining using only 81 transcribed words, whereas random initialisation requires 355, which gives a label multiplier of 4.40 [3.56, 4.99]. There is a zero-shot reference point as well: with no real transcribed words at all, this pretraining is worth about 136 of them. This advantage gets smaller as the target accuracy improves, and at the most demanding target we measure, it cannot be distinguished from no saving at all. A fourth arm in which only the encoder is transferred separates the effect of the pretraining method from that of transfer scope, and masked image modelling is observed to transfer negatively over a bounded range of budgets. We emphasise that the scarcity in this study is constructed by subsampling a large corpus.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. Lexplorer: Navigating the Complexity of Legal Document Landscapes

- **ArXiv ID**: [2609.17366v1](https://arxiv.org/abs/2609.17366v1)
- **作者**: Daniel Fürst, Titus Pünder, Maximilian T. Fischer, Corinna Coupette
- **发布时间**: 2026-09-16
- **分类**: cs.HC, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.17366v1](https://arxiv.org/pdf/2609.17366v1)
- **相关度评分**: 10/10

#### 英文摘要

As technological and social innovations create novel regulatory challenges, legal systems grow in complexity - increasing the need for interfaces that enable effective interactions with legal document collections. Through interviews with legal scholars (n=15), we find that supporting legal work requires going beyond retrieval-centered legal-information-system paradigms. Hence, we propose Lexplorer, a flexible interface for exploring, navigating, and analyzing legal documents, based on a taxonomy capturing user intents. Distinguishing text and data views for one, few, and many documents, Lexplorer enables context-sensitive interactions with evolving collections of interconnected legal texts, facilitating Adaptive Meaning Construction in law. We evaluate Lexplorer with legal scholars (n=20) in the context of European Union law, validating our elicited requirements, intent taxonomy, and prototype design. Resulting from a close collaboration between visual-analytics researchers and legal scholars, our work also provides nuanced insights into the process required to design interactive systems for expert domains driven by implicit methodological knowledge.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. Where Should a Document Live: Context, Representations, or Parameters?

- **ArXiv ID**: [2609.17346v1](https://arxiv.org/abs/2609.17346v1)
- **作者**: Nathanaël Carraz Rakotonirina, Momchil Hardalov, Gonzalo Iglesias, Adrià de Gispert
- **发布时间**: 2026-09-15
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.17346v1](https://arxiv.org/pdf/2609.17346v1)
- **相关度评分**: 10/10

#### 英文摘要

To answer questions outside of their pre-training data, large language models (LLMs) need access to new information, which can be presented in the context window as documents, encoded into the model's parameters, or injected as latent representations. However, each of these methods comes with different efficiency, cost, and performance trade-offs, with no single winner. We present a controlled comparison of representation-based (KV-cache based) and parametric (fine-tuning-based) adaptation methods on five knowledge-intensive benchmarks. We show that in the oracle setting, Cartridges (KV) are the most accurate injection method at nearly every storage budget, outperforming parametric methods by 10 points. Compaction (KV) matches Cartridges only at low compression rates, lagging behind the parametric methods by 10 points at rates higher than $50\times$. In the more realistic multi-document retrieval scenario, Cartridges are the only method that matches in-context learning (ICL), leading the parametric methods by 29 points and Compaction by 15 points. Nonetheless, Cartridges are also the only method, besides full fine-tuning and large MLP adapters, that suffers from catastrophic forgetting, i.e., a 6% performance degradation on control benchmarks, with 13% in coding.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Extracting ontology-compliant knowledge from scientific text describing irradiated materials using large language models

- **ArXiv ID**: [2609.17291v1](https://arxiv.org/abs/2609.17291v1)
- **作者**: Marco Luca Sbodio, Marcos Martínez Galindo, Vanessa Lopez, Blanca Biel, Pablo Canca...
- **发布时间**: 2026-09-15
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.17291v1](https://arxiv.org/pdf/2609.17291v1)
- **相关度评分**: 10/10

#### 英文摘要

The quest for new materials increasingly relies on predictive models and comprehensive simulations that span scales from atomic to macroscopic levels. However, essential data necessary for these models and simulations are often embedded in scientific literature as unstructured text, limiting reusability and posing challenges for researchers seeking to leverage existing knowledge effectively. While extracting structured data from unstructured text using large language models is gaining popularity, traditional methods typically generate key-value pairs data with straightforward schemas. In contrast, we introduce eolas, a modular pipeline that uses large language models to automatically transform scientific documents into knowledge graphs aligned with a specified ontology. We demonstrate eolas effectiveness in extracting useful information for scientists studying materials designed to endure the extreme temperatures and radiation levels found in fusion reactors. While a human expert might spend between thirty to ninety minutes extracting relevant data from an article, eolas can generate high-quality knowledge graphs in just a few minutes. These are presented in a tabular format with faceted navigation for easy human validation. Additionally, we introduce the first benchmark dataset designed to assess large language models capabilities in constructing knowledge graphs within the domain of irradiated materials. The analysis of 168 experiments using our dataset, various large language models and prompting techniques provides key insights that we summarize into practical guidelines for effectively extracting knowledge graphs aligned with an input ontology.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. Exploring 2D backbone effects for indoor semantic occupancy prediction

- **ArXiv ID**: [2609.17257v1](https://arxiv.org/abs/2609.17257v1)
- **作者**: Shizhang Fanga, Wanling Yea, Qi Zheng
- **发布时间**: 2026-09-15
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.17257v1](https://arxiv.org/pdf/2609.17257v1)
- **相关度评分**: 10/10

#### 英文摘要

Semantic occupancy prediction gives an embodied agent a voxel-level account of where space is free, occupied, and semantically meaningful. In RGB-D pipelines such as EmbodiedScan, the image encoder is often left as a default module, even though its features are the visual evidence later sampled into the 3D grid. We study this design choice directly. A central finding is that changing the 2D backbone improves occupancy accuracy more than several carefully designed occupancy architectures or modules. We keep the main RGB-D projection, depth branch, and occupancy head fixed, and replace only the image backbone. The compared encoders are CLIP-ResNet, CLIP-ViT, BLIP2, and DINOv2. Under the controlled setting, the measured mIoU changes substantially: DINOv2 obtains 30.55\%, BLIP2 obtains 29.49\%, CLIP-ViT obtains 24.33\%, and CLIP-ResNet obtains 17.41\%. The stronger encoders also exceed the original EmbodiedScan ResNet-50 baseline without modifying the downstream 3D fusion pipeline. Class-level results give a more detailed picture: DINOv2 is stronger on many layout and structural categories, whereas BLIP2 remains close on several object-centered classes. CLIP-ViT improves clearly over CLIP-ResNet, showing that the way CLIP features are exposed as dense tokens matters for voxel lifting. These results indicate that the image backbone is not a secondary engineering detail in embodied semantic occupancy, but a major source of variation in the final 3D prediction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering

- **ArXiv ID**: [2609.17043v1](https://arxiv.org/abs/2609.17043v1)
- **作者**: Kevin Mo, Nathan Mo, Richard Zhu
- **发布时间**: 2026-09-15
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.17043v1](https://arxiv.org/pdf/2609.17043v1)
- **相关度评分**: 10/10

#### 英文摘要

Multi-hop question answering requires combining information from multiple documents to answer complex questions. These systems have grown increasingly capable, yet when they fail, the error is typically attributed to not finding the right documents. Whether this holds at the level of individual reasoning steps remains largely unexamined. We investigate this across three standard multi-hop QA benchmarks and find that failures decompose into two distinct modes: retrieval failures, where the needed passage was not retrieved, and extraction failures, where the passage was retrieved but the needed fact could not be extracted - a phenomenon we term the fact-grounding gap. Extraction failures account for nearly half of all per-hop deficiencies and are invisible to standard retrieval metrics. They remain unresolved by every retrieval intervention we test, establishing a ceiling for retrieval-only improvements. The gap's severity varies across benchmarks and question types, but extraction failures appear on every dataset we measure. Our findings reveal that retrieval failures and extraction failures are fundamentally different bottlenecks requiring different solutions - a distinction absent from current evaluation practice.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. HUMAID-NER: A Disaster Tweet Dataset for Joint Named Entity Recognition and Event Classification via Uncertainty-Weighted Multitask Learning

- **ArXiv ID**: [2609.16964v1](https://arxiv.org/abs/2609.16964v1)
- **作者**: Aijaz Ali, Nazish Basir, Sarfaraz Nawaz, Danish Nazir Arain, Haris Ali
- **发布时间**: 2026-09-15
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.16964v1](https://arxiv.org/pdf/2609.16964v1)
- **相关度评分**: 10/10

#### 英文摘要

Rapid extraction of structured information from social media is important for humanitarian response, yet existing disaster tweet resources mainly provide document-level category labels without span-level entity annotations. We introduce HUMAID-NER, the first named entity recognition dataset built on the HumAID benchmark, containing 60,000 English disaster tweets annotated in BIO format across ten operationally motivated entity types and yielding approximately 175,000 labelled entity spans. Annotations are generated through a reproducible three-stage hybrid pipeline combining a spaCy transformer model, disaster-domain EntityRuler patterns, and structured regular expressions with priority-based overlap resolution. We also propose a joint multitask learning framework that performs disaster-specific named entity recognition and humanitarian event classification using a shared RoBERTa-large encoder. To reduce task conflict during joint training, the model uses homoscedastic uncertainty weighting with learnable task parameters and a two-stage training schedule that freezes the lower 18 of 24 encoder layers in the second stage. On the HUMAID-NER validation set, the proposed system achieves NER span micro-F1 of 0.841 and classification macro-F1 of 0.761 simultaneously. A real-time web dashboard demonstrates end-to-end deployment. The dataset, models, and pipeline code are released to support reproducibility and future crisis informatics research.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. VOR-Bench: A Human Perception-Driven Benchmark for Video Object Removal

- **ArXiv ID**: [2609.16878v1](https://arxiv.org/abs/2609.16878v1)
- **作者**: Haonan Huang, Tianrui Qiu, Xianghao Zang, Yinan Du, Zhixiang He...
- **发布时间**: 2026-09-15
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.16878v1](https://arxiv.org/pdf/2609.16878v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite its crucial role in video object removal (VOR), existing evaluation paradigms face two critical limitations: questionable references and a misalignment between tradi- tional metrics and human preference. To address these challenges, we introduce VOR- Bench, which advances VOR evaluation through three integrated components. First, we present the VOR Dataset (VORD), the first benchmark dataset providing both paired edited videos and graffiti masks. Its unique strength lies in a diverse data spectrum, which encompasses model-generated, tool-rendered, and camera-captured data, ensuring robust assessment across real-world scenarios. Second, we develop rMPAF, a realistic Motion- capable Paired-video Acquisition Framework. By combining the strengths of image- based object removal and fine-tuned video generation models, rMPAF automatically generates realistic, motion-coherent paired videos. Finally, we propose three evaluation dimensions and introduce VOR-MDSM, the first perception-driven VLM-based scoring model specifically designed for mask-guided VOR. It bridges the gap between arithmetic metrics and human perception by covering the essential visual attributes and matching nuanced human judgment. Extensive experiments demonstrate that VOR-Bench yields evaluation results that align closely with human perception, achieving a remarkable cor- relation (\r{ho} > 0.9) with subjective assessments. We will release VOR-Bench along with its documentation to ensure full reproducibility.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. Multi-modal Knowledge Preserving Adapter for Embedding Backward Compatibility

- **ArXiv ID**: [2609.16875v1](https://arxiv.org/abs/2609.16875v1)
- **作者**: Jaeseok Byun, Gukyeong Kwon, Han-Kai Hsu, Meher Gitika Karumuri, Zhikang Zhang...
- **发布时间**: 2026-09-15
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.16875v1](https://arxiv.org/pdf/2609.16875v1)
- **相关度评分**: 10/10

#### 英文摘要

Upgrading embedding models typically requires expensive database re-indexing, as new query embeddings are incompatible with existing database embeddings. While Backward Compatible Training (BCT) mitigates this by enforcing compatibility during training, existing approaches often require updating the backbone model. This is impractical because of significant training cost, the risk of performance regression, and limited access to proprietary model weights. We introduce Multi-modal Knowledge Preserving Adapter (MKP-Adapter), the first adapter-only BCT approach for Multi-modal Large Language Models (MLLMs) that requires no backbone updates. We identified that the primary challenge in adapter-only BCT is preserving the knowledge of the new embeddings while enforcing backward compatibility. Hence, we propose a multi-level preservation loss that maintains the geometric structure of the embedding spaces throughout BCT. Furthermore, a focal re-weighting strategy is integrated to prioritize learning from challenging samples. Experiments demonstrate that our method achieves strong backward compatibility across diverse multi-modal benchmarks (image, text, visual document, and video retrieval tasks) and model types. Notably, MKP-Adapter is trained solely on pre-extracted embeddings and requires only negligible additional latency relative to the original backbone forward pass, highlighting its efficiency.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. Target-Language Generation in Multilingual Models: Activation Steering and Optimal Control

- **ArXiv ID**: [2609.16967v1](https://arxiv.org/abs/2609.16967v1)
- **作者**: James A. Michaelov, Carmen Amo Alonso, Tyler A. Chang, Roger P. Levy
- **发布时间**: 2026-09-15
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.16967v1](https://arxiv.org/pdf/2609.16967v1)
- **相关度评分**: 10/10

#### 英文摘要

Ensuring that multilingual language models generate coherent text in a specific target language is a major issue in multilingual language modeling. We develop an optimal control method for target-language text generation as well as a framework for evaluating the quality of generated text in terms of language adherence, linguistic coherence, and semantic coherence. We find that the proposed method performs at least as well as the prominent difference-in-means activation steering method for the majority of models tested, with substantially less hyperparameter tuning required.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control

- **ArXiv ID**: [2609.17521v1](https://arxiv.org/abs/2609.17521v1)
- **作者**: Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng...
- **发布时间**: 2026-09-16
- **分类**: cs.CV, cs.AI, cs.GR
- **PDF**: [https://arxiv.org/pdf/2609.17521v1](https://arxiv.org/pdf/2609.17521v1)
- **相关度评分**: 10/10

#### 英文摘要

Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes. Yet existing controllable methods either require the full control schedule before generation starts, or use pixel-space signals that dictate object positions rather than physical dynamics. To address these limitations, we propose PhysStream, an autoregressive model for physics-grounded image-to-video synthesis that incorporates structured scene memory---positional maps and object tracking maps derived online from previously generated frames---and supports fine-grained motion control via sparse velocity-increment signals that encode physical quantities, letting the model learn the underlying dynamics. We train our model in two stages: a bidirectional model is first finetuned with motion-control conditioning, then a causal autoregressive model is trained with additional structured scene memory, further improving physical consistency. PhysStream enables interactive, mid-generation control over multi-object tabletop rigid-body scenes---a capability not supported by prior methods---reducing motion distribution distance (FVMD) by 33% and trajectory error by 12% over the strongest baselines on synthetic benchmarks, and is preferred by human evaluators in over 85% of in-the-wild comparisons. Please check our website for more details: https://czzzzh.github.io/PhysStream

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Det-LIME: Detector-Aware, Multi-Instance Local Interpretable Model-Agnostic Explanations for Automated Marine Mammal Detection

- **ArXiv ID**: [2609.17479v1](https://arxiv.org/abs/2609.17479v1)
- **作者**: Jiayi Zhou, David W. Johnston, Brinnae Bent
- **发布时间**: 2026-09-16
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.17479v1](https://arxiv.org/pdf/2609.17479v1)
- **相关度评分**: 10/10

#### 英文摘要

Despite the rapid uptake of black-box object detectors in marine mammal research and monitoring, explainability techniques are rarely integrated into conservation workflows. Furthermore, most classification-oriented explainability tools are ill-suited to detection tasks involving imagery of social organisms or those with colonial life histories, as they ignore multiple detections within a scene and produce single-instance outputs that blur evidence across individuals. These methods also generate low-resolution, often biologically irrelevant visuals, limiting their utility for debugging, targeted data augmentation, and refined data collection. We proposed Det-LIME, a detector-aware, multi-instance adaptation of Local Interpretable Model-Agnostic Explanations (LIME) that produced instance-specific, box-aligned explanations by combining per-detection weighting, a proximity kernel that emphasizes regions near each box, and Intersection-over-Union-based matching to track the same instance across perturbations. We evaluated Det-LIME on aerial drone imagery for harbor seal detection, with an additional seabird case study to assess generality, and compared it with vanilla LIME, Stabilized LIME, Deterministic LIME, and gradient-based attribution methods. Using the Attribution Ratio and Max Saliency Hit Rate metrics, we showed that Det-LIME consistently improved multi-instance attribution. In practice, these higher-resolution, instance-aware explanations provide insight into model outputs and support post-processing, debugging, and actionable improvements in modeling and data collection or augmentation.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis

- **ArXiv ID**: [2609.17450v1](https://arxiv.org/abs/2609.17450v1)
- **作者**: Weronika Jakubowska, Maciej Zięba, Przemysław Spurek
- **发布时间**: 2026-09-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.17450v1](https://arxiv.org/pdf/2609.17450v1)
- **相关度评分**: 10/10

#### 英文摘要

Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry and holes in the reconstructed scene. Existing methods often rely on generative models to complete such regions. However, many of these artifacts are small gaps near depth boundaries and do not require generating new scene content. In order to eliminate expensive process of generating image we introduce ORCA, an occlusion-aware method for reconstructing and completing explorable 3D scenes from a single image. ORCA first introduces 3D structure into a Gaussian-anchor representation using monocular depth while preserving the original camera-ray correspondence. During scene exploration, missing regions are handled based on their size and structure. Small disocclusions are repaired using RGB-D information already available in the reconstruction, while generative inpainting is reserved for larger regions that cannot be reliably recovered from the scene. New Gaussian anchors are added and optimized locally without modifying the existing representation. By reducing unnecessary reliance on generative inpainting, ORCA limits generation-induced hallucinations and better preserves the content and structure of the original scene. On DIV2K, ORCA improves novel-view quality over VistaDream across all reported metrics, increasing MUSIQ from 61.60 to 68.71 and CLIP-IQA from 0.474 to 0.574. These results show that many novel-view artifacts can be repaired effectively by reusing information already present in the reconstructed scene.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. BrainFocus: EEG-Guided ROI Selection for Efficient Vision-Language Models

- **ArXiv ID**: [2609.17443v1](https://arxiv.org/abs/2609.17443v1)
- **作者**: Yihui Peng, Guorui Lu, Qinyu Chen
- **发布时间**: 2026-09-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.17443v1](https://arxiv.org/pdf/2609.17443v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) achieve strong visual question answering (VQA) performance, but processing large cluttered images is computationally expensive when only a small region is relevant. Electroencephalography (EEG) signals, which capture human neural responses to visual stimuli, can provide a human-derived semantic cue about the region of interest (ROI). However, EEG-guided visual category decoding remains imperfect, making direct ROI routing unreliable. In this work, we propose BrainFocus, a reliable EEG-guided efficient VLM framework for VQA. An EEG classifier predicts a target category, and a YOLO detector localizes the matching ROI. The VLM receives the cropped ROI only when both predictions pass confidence thresholds; otherwise, it processes the full image. For evaluation, we build on EEG-ImageNet to construct a 40-class benchmark comprising generated cluttered images and real object-centric images, with target-ROI annotations and 600 English visual question-answer pairs. Across Qwen3.5-VL 2B, 4B, and 9B models, BrainFocus improves VQA accuracy by 4.14-9.87 percentage points (pp) on cluttered scenes while reducing input tokens and total tokens by 23.2%-39.4% and 23.2%-39.3%, and end-to-end floating-point operations (FLOPs) by 23.2%-39.5%. These results demonstrate that EEG can guide efficient VLM inference even when its semantic decoding is imperfect.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
