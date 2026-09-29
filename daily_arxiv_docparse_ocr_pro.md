# OCR arXiv Daily Pro — 2026-09-29

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-28 09:10 - 2026-09-29 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bc7873f0-8033-4

---

## 📄 论文详情

### 1. Handwritten Text Recognition Lives in the High-Pixel Variance Subspace

- **ArXiv ID**: [2609.35473v1](https://arxiv.org/abs/2609.35473v1)
- **作者**: Carlos Garrido-Munoz, Jorge Calvo-Zaragoza
- **发布时间**: 2026-09-28
- **分类**: cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.35473v1](https://arxiv.org/pdf/2609.35473v1)
- **相关度评分**: 10/10

#### 英文摘要

In self-supervised pretraining for Handwritten Text Recognition (HTR), pixel reconstruction methods outperform contrastive methods, unlike in natural-image classification. We argue that this difference follows from where discriminative signal lies in pixel space: for HTR, it is concentrated in high-variance directions and largely absent from low-variance ones. This predicts that objectives preserving high-variance pixel content will transfer best. We test six SSL methods from three families (pixel-grounded MIM, JEPA, and contrastive) under matched encoder, data, and evaluation protocols on six handwriting benchmarks across five languages. With full labels, pixel-groundrounded SSL achieves the lowest CER on every benchmark and both frozen probes, exposes per-position character information that other families recover only through the readout, and is the only family to benefit from pretraining on real handwriting. Pixel-grounded representations are also more label efficient. Across datasets, encoder alignment with the high-variance pixel subspace predicts CER within every method. With a pretrained LLM decoder, a frozen pixel-grounded encoder is competitive with fully fine-tuned supervised baselines; full fine-tuning achieves the lowest mean CER and ranks first or second on every benchmark. These results show that the value of pixel reconstruction depends on where discriminative signal lies in the input.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a521021a-ef16-4

---

### 2. Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG

- **ArXiv ID**: [2609.35304v1](https://arxiv.org/abs/2609.35304v1)
- **作者**: Antonios Georgakopoulos, Paul Groth, Lise Stork
- **发布时间**: 2026-09-28
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.35304v1](https://arxiv.org/pdf/2609.35304v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal knowledge graphs (KGs) integrate information from text, figures, tables, and other modalities into a unified structured representation, with the promise that richer evidence enables better inference. In GraphRAG systems built over such graphs, it is commonly assumed that retrieving evidence from more modalities at inference time improves downstream performance. Yet, redundant or overlapping multimodal evidence may distract language models in question answering (QA), and whether each modality contributes equally across questions, models, and tasks remains poorly understood. In this work, we study how modality-aware retrieval affects downstream inference in a multimodal GraphRAG pipeline, using document visual question answering (DocVQA) as a testbed. We extend an existing KG-based QA framework to be modality-aware, leveraging the graph structure to track which modality supports which facts and to selectively filter evidence at the edge level. This enables us to investigate whether providing all available multimodal evidence at inference time benefits QA, and to evaluate the contribution and cooperation of modalities across question, task, and model characteristics. Through a controlled analysis within a state-of-the-art multimodal GraphRAG pipeline, five multimodal LLMs and two DocVQA benchmarks, we find that tables and text provide the strongest contributions, and that combining modalities frequently produces redundancy rather than synergy, particularly for pairs involving textual information. Positive cooperation appears mainly between non-text modalities and depends on question intent and task type. Our findings argue for selective, modality-aware retrieval in the design of more effective GraphRAG systems, where modalities are filtered according to the downstream task rather than retrieved uniformly.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8f991ffc-f738-4

---

### 3. When VLMs Trust Context: Evaluating Scene Text Recognition under Misleading Context

- **ArXiv ID**: [2609.34781v1](https://arxiv.org/abs/2609.34781v1)
- **作者**: Yuxing Cheng, Yuan Wu, Yi Chang
- **发布时间**: 2026-09-28
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.34781v1](https://arxiv.org/pdf/2609.34781v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) can read text in natural scenes, but their predictions may be influenced by the surrounding context. When the printed text conflicts with what the scene suggests, a model may return a more plausible word instead of the shown text. We introduce SceneFaith, a benchmark of 781 generated scene images for studying this behavior. Each output is classified as Literal, Canonical, or Other, separating faithful transcription from context-consistent rewriting and ordinary recognition errors. Across 15 models from seven families, all models show rewriting on clear images, with rates ranging from 8.45\% to 58.51\%. Controlled experiments further show that surrounding context matters: removing surrounding scene information reduces rewriting and improves literal accuracy, while changing the scene around the same text patch can also change model outputs. Moreover, weakening the target text with blur increases rewriting. These results show that reliable scene-text recognition requires VLMs to balance visual character evidence with contextual information, preserving clear text while using context mainly when the visual evidence is uncertain.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 9faa0bc9-3337-4

---

### 4. When Harness Beats Scale, and When Reading Beats Both

- **ArXiv ID**: [2609.34366v1](https://arxiv.org/abs/2609.34366v1)
- **作者**: Ivan Bondarenko, Nikolay O. Nikitin
- **发布时间**: 2026-09-28
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.34366v1](https://arxiv.org/pdf/2609.34366v1)
- **相关度评分**: 10/10

#### 英文摘要

We describe our system for DocSem, the document-grounded quantitative reasoning shared task at DocInsights 2026, and analyze why it succeeded on labeled data and failed on the test set. The pipeline pairs hybrid block retrieval with Program-of-Thoughts (PoT) generation executed in a sandboxed interpreter, self-consistency sampling, and entity enrichment from chunk-level knowledge graphs. On our held-out split, application architecture moved the metrics far more than model scale did: PoT added 0.282 joint accuracy to a compact 7B model but at most 0.005 to a 72B model, and a 27B model with the full harness matched the 72B (0.884 vs.\ 0.873) at roughly 2.7$\times$ fewer parameters and a quarter of the CO$_2$. We read this through a distinction between world knowledge, which scales steeply with parameters, and language knowledge, which scales gently, and show that structured-output training makes a compact model harness-ready rather than merely small. On the raster, watermarked test PDFs the same system collapsed to 13.58\% joint (rank 149 of 163); a controlled re-rendering of the validation set reproduces the OCR half of the collapse while bounding what the simulation misses. Auditing the physical nature of evaluation inputs precedes architecture, and the leaderboard's bimodality is consistent with reading quality, not reasoning, having separated the field.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bedac01d-89ad-4

---

### 5. ConvCue: Complementary Visual Inductive Biases for Vision-Language Models

- **ArXiv ID**: [2609.34196v1](https://arxiv.org/abs/2609.34196v1)
- **作者**: Zixuan Lan, Shichu Sun
- **发布时间**: 2026-09-28
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.34196v1](https://arxiv.org/pdf/2609.34196v1)
- **相关度评分**: 10/10

#### 英文摘要

Modern vision-language models (VLMs) achieve strong performance across a broad range of multimodal tasks, yet still struggle with visual questions that require fine-grained discrimination and spatial understanding. These limitations motivate investigating whether supplementary visual representations can improve existing VLMs without replacing their native visual encoders. Pretrained convolutional networks offer a candidate feature source, motivated by their local connectivity and spatial weight sharing. We introduce CONVCUE, which augments the native visual representations of a pretrained VLM with final-stage features from a parallel, frozen pretrained CNN. A learnable adapter maps convolutional features to the native visual feature dimension, while gated cross-attention allows the original visual tokens to retrieve information from the CNN features. The enhanced tokens are passed through the original visual-to-language projector, and the model is adapted through a two-stage training procedure. We evaluate CONVCUE on Qwen3-VL-2B, Qwen3-VL-4B, and LLaVA-OneVision-7B across 13 multimodal benchmarks covering visual question answering, document and chart understanding, and multimodal reasoning. CONVCUE improves average benchmark performance over both the original models and matched two-stage fine-tuning controls on all three backbones. On Qwen3-VL-4B, it improves over the original model on all 13 benchmarks and raises the average score from 75.00 to 78.82 relative to the matched fine-tuning control. These results show that pretrained convolutional representations, when integrated through learned adaptation and fusion, can improve the visual understanding of existing VLMs without replacing their original visual encoders.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a2cb61b9-fa12-4

---

### 6. From Static to Dynamic: On-Policy Distillation from Image to Video Diffusion Models

- **ArXiv ID**: [2609.34371v1](https://arxiv.org/abs/2609.34371v1)
- **作者**: Bingqing Jiang, Li Luo, Zichao Yu, Yujin Han, Zhaolong Su...
- **发布时间**: 2026-09-28
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.34371v1](https://arxiv.org/pdf/2609.34371v1)
- **相关度评分**: 10/10

#### 英文摘要

On-policy distillation (OPD) specializes pretrained video diffusion models through teacher supervision along the student's own generation trajectory. Although large video models are natural teachers, developing specialized video experts can require costly video data and training, while querying them incurs substantially higher latency than querying image experts. More readily available and cheaper to query, image experts offer a cost-effective alternative, particularly for largely temporal-agnostic capabilities such as aesthetics and OCR that admit frame-level supervision. However, heterogeneous image and video latent spaces prevent direct supervision of intermediate student states, while image experts lack cross-frame motion supervision, making temporal consistency vulnerable to frame-level improvements. In this paper, we propose MILD, a Motion-Preserving Image-to-Video Latent Distillation framework that transfers specialized image expertise while preserving pretrained video dynamics. MILD uses a learnable linear connector that aligns student latent states and predicted updates with those of image experts, enabling supervision transfer across heterogeneous latent spaces. We further constrain image-guided corrections around the pretrained student's predictions to preserve video dynamics and incorporate an optical-flow-based motion reward to improve motion quality and temporal consistency. Across specialized image experts and multiple video-student backbones, our method consistently outperforms video-teacher OPD baselines, with further studies demonstrating effective transfer across connector designs and heterogeneous architectures. These results establish image-to-video distillation as an effective route to improving video generation by drawing on the diverse and evolving capabilities of the image-generation ecosystem.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d337db22-3c53-4

---

### 7. MiCo: Mutual Information Coverage Optimization through Semantic Erasure Modeling for Efficient MLLM Inference

- **ArXiv ID**: [2609.34330v1](https://arxiv.org/abs/2609.34330v1)
- **作者**: Tinghao Wang, Yichen Guo, Qizhe Zhang, Yuan Zhang, Weimin Ouyang...
- **发布时间**: 2026-09-28
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.34330v1](https://arxiv.org/pdf/2609.34330v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal large language models (MLLMs) have demonstrated impressive performance in multimodal understanding, but processing large numbers of visual tokens results in high computational costs. While many methods have been proposed to reduce the number of visual tokens, most of them rely on heuristics and are prone to discarding substantial visual information during pruning, leading to degradation in model performance. In this work, by using a semantic erasure model, we derive a general mutual information coverage objective from task log-loss and propose MiCo, a training-free two-stage pruning method. MiCo first uses visual signals to select a representative candidate pool before visual tokens enter the language model, then performs task-aware subset selection within it. At each stage, suitable observable proxies instantiate the derived objective as a monotone submodular coverage function, which MiCo greedily optimizes under the token budget. MiCo is evaluated on diverse MLLMs ranging from 7B to 13B parameters across a broad range of image and video benchmarks spanning general visual reasoning, fine-grained OCR and grounding, hallucination detection, and long-video understanding. MiCo consistently achieves the best performance across nearly all evaluated models under all pruning ratios. On LLaVA-NEXT-13B, MiCo uses only 5.6% visual tokens, retains 97.5% of baseline performance, and achieves a 3.8-fold inference speedup. Our experiments demonstrate the effectiveness of MiCo and our mutual information coverage objective for visual token pruning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bcd39d4d-6b01-4

---

### 8. Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales

- **ArXiv ID**: [2609.35765v1](https://arxiv.org/abs/2609.35765v1)
- **作者**: András Kovács, Alexander Conroy, Daniel Hershcovich, Jens Bjerring-Hansen
- **发布时间**: 2026-09-29
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.35765v1](https://arxiv.org/pdf/2609.35765v1)
- **相关度评分**: 10/10

#### 英文摘要

Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and translation. We investigate this problem through biblical intertextuality in Karen Blixen's Seven Gothic Tales. Drawing on the commentary to a critical edition, we construct a benchmark of 189 annotated references and evaluate retrieval against all 31,170 verses of historically plausible Danish Old and New Testament translations. We compare TF-IDF and BM25 with multilingual and Danish sentence encoders, examine the effect of linguistic normalization, and fine-tune a Danish encoder using hard negatives and five-fold cross-validation. We analyze performance across automatically derived lexical-overlap strata representing quotations, paraphrases, and allusions. Linguistically normalized BM25 provides a strong zero-shot baseline, attaining an overall R@10 of 0.365 and retrieving every quotation within its ten highest-ranked verses. The best zero-shot dense model achieves a comparable overall score of 0.360 while performing better on allusions. Fine-tuning DFM-large raises its overall R@10 from 0.265 to 0.508 and more than doubles its performance on allusions, from 0.138 to 0.339. However, evaluation against editorial annotations alone understates the model's scholarly usefulness: a literary scholar judged seven of 30 selected rank-one predictions counted as false positives to be meaningful additional references. These findings show both the potential and the epistemic limits of computational intertextual retrieval. Rather than treating scholarly annotations as exhaustive or model outputs as discoveries, we propose retrieval models as heuristic co-readers that recover documented references and generate candidates for expert-led close reading.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8c68c701-b5a6-4

---

### 9. Rubric-Calibrated Preferences: Cross-Query Calibration of LLM Judgments via Item Response Theory

- **ArXiv ID**: [2609.35739v1](https://arxiv.org/abs/2609.35739v1)
- **作者**: Fabian David Schmidt, Donato Crisostomi, Carlos Lassance, Nils Reimers
- **发布时间**: 2026-09-29
- **分类**: cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.35739v1](https://arxiv.org/pdf/2609.35739v1)
- **相关度评分**: 10/10

#### 英文摘要

Rerankers decide which documents users and LLMs see, yet their standard metric, nDCG, relies on human relevance labels that are costly, sparse, noisy, and discretely graded. As rerankers approach each other in quality, nDCG on these labels therefore increasingly fails to separate them. LLM judges could supply dense labels. Relative judgments within one query tell even close candidates apart, yet their scores share no scale across queries. Absolute grades share one scale but are too coarse to distinguish documents of similar relevance. We propose Rubric-Calibrated Preferences (RCP), which combine both kinds of judgment. A listwise Bradley-Terry tournament orders each query's documents, and a rubric of yes/no criteria of increasing stringency provides an absolute standard. Item Response Theory (IRT), which scores test-takers based on their answers to common questions, then uses the shared criteria to put all queries' tournament scores on one scale. RCP's retrieval metric, RCP-nDCG, replaces nDCG's discrete labels with the resulting calibrated relevance probabilities. Against blind grades from 46 external annotators, calibration raises the correlation between a query's mean score and its mean human grade from 0.538 to 0.795. The probabilities rank a useful document above a non-useful one with probability 0.910 (AUC, chance 0.5), versus 0.651 for the benchmark labels. When the annotators' grades prefer one of two rerankers and exactly one metric agrees, that metric is RCP-nDCG in 72.4% of 185 comparisons (chance about 53%). On TREC-DL, RCP-nDCG sides with NIST assessors' grades on every reranker pair that these grades separate significantly. RCP-nDCG also resolves many of nDCG's ties and separates 1.9 times as many reranker pairs on NanoBEIR. Rubric calibration thus turns relative LLM judgments into dense relevance labels that are comparable across queries and agree with human judgment.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 3ac077bc-a2c2-4

---

### 10. A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion

- **ArXiv ID**: [2609.35703v1](https://arxiv.org/abs/2609.35703v1)
- **作者**: Fred Xu, Thomas Markovich, Florence Regol, Yizhou Sun
- **发布时间**: 2026-09-29
- **分类**: cs.LG, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.35703v1](https://arxiv.org/pdf/2609.35703v1)
- **相关度评分**: 10/10

#### 英文摘要

Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate models and objectives. We model uncertain node embeddings as random graph signals: graph Fourier filters capture structural variation, and a scalar orthogonal-polynomial chaos coordinate captures latent stochastic variation. The resulting doubly-spectral stochastic (DSS) expansion supplies task-matched readouts from one representation: the mean coefficient encodes class evidence for the energy-based OOD score, the higher-order coefficients encode structured logit variation, and quadrature averaging over the chaos coordinate defines the single predictive distribution used for prediction and calibration. A capacity theorem shows that, under a full-rank feature assumption, a restricted subfamily matches the chaos coefficients of any Gaussian-latent random graph signal, with exponentially decaying truncation error under a growth condition; the task-level claims are established empirically. DSS-GNN has two deployment modes: standalone, or as a residual branch beside a deterministic encoder (DSS-Hybrid). Standalone DSS-GNN achieves the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction; DSS-Hybrid achieves the best AUROC on most node-OOD settings, competitive cross-graph OOD detection, and the strongest shifted accuracy on all 7 GOOD concept-shift benchmarks under standard empirical risk minimization (ERM). Cross-evaluating both modes on all three tasks shows that each remains effective on the other's tasks, with documented exceptions, and yields explicit deployment guidance.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4d9220e9-e6f5-4

---

### 11. QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations

- **ArXiv ID**: [2609.35685v1](https://arxiv.org/abs/2609.35685v1)
- **作者**: Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda, Naomi Couriel, Yelena Mejova...
- **发布时间**: 2026-09-29
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.35685v1](https://arxiv.org/pdf/2609.35685v1)
- **相关度评分**: 10/10

#### 英文摘要

Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudication interface where reviewers accept either side, build field-level hybrids, or flag items for re-annotation. A campaign manager assigns documents to multiple annotators with configurable redundancy, computes agreement at document and span level, auto-merges unanimous documents, and exports the corrected layer in the original file format, so that it can replace the original annotation files directly. Applied to a 4,457-record humanitarian benchmark and an LLM extraction stream, the system fully auto-merged 8% of documents, applied automatic policy decisions to a further 1,513 records, and concentrated human attention on 3,131 candidate conflicts, a mean of 5.4 per reviewed document.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 09ac34df-1c65-4

---

### 12. Revisiting Risky Tackle Detection with Vision Transformers

- **ArXiv ID**: [2609.35562v1](https://arxiv.org/abs/2609.35562v1)
- **作者**: Syed Ahsan Masud Zaidi, Lior Shamir, Scott Dietrich
- **发布时间**: 2026-09-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.35562v1](https://arxiv.org/pdf/2609.35562v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper is a Track 2 reproducibility companion to an ICPR 2026 study on risky tackle detection in American football prac- tice videos. The original work fine-tuned a Video Vision Transformer (ViViT) on 733 clips labeled with the SATT-3 rubric. It used focal loss, Taguchi L18 augmentation, and 5-fold cross-validation. It reported risky- class recall of 0.67 and risky-class F1 of 0.59. This companion documents the released artifact and traces those numbers to specific scripts, fold out- puts, and aggregation files. The reproduced headline is run_15. It com- bines Gaussian noise with static brightness decrease and uses no rotation and no flip. Its fold-mean risky recall is 0.667 and its fold-mean risky F1 is 0.588. These values match the published headline after rounding. The ablation shows that brightness is the dominant factor. Its risky-recall main-effect range is 0.055, which is larger than the ranges for rotation, flip, and noise. Without augmentation, ViViT reaches risky recall of 0.545 and does not exceed the C3D baseline of 0.583. The raw clips show iden- tifiable student athletes, so they cannot be redistributed. The artifact provides a public sample for pipeline checks and a controlled route for full-data review.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 844bbb93-b9ca-4

---

### 13. RareDx: Controlled Knowledge Integration and Graph-Grounded Policy Optimization for Rare-Disease Diagnosis

- **ArXiv ID**: [2609.35549v1](https://arxiv.org/abs/2609.35549v1)
- **作者**: Bo Zhang, Yuchen Wang, Dongbai Li, Matthew Yu Heng Wong, Qingkai Zeng...
- **发布时间**: 2026-09-29
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.35549v1](https://arxiv.org/pdf/2609.35549v1)
- **相关度评分**: 10/10

#### 英文摘要

Rare-disease diagnosis is a long-tail reasoning problem: phenotypes are incomplete, individual disorders are sparsely documented, and relevant evidence is distributed across ontologies, gene annotations, and biomedical text. Language models consequently favor common conditions, miss rare candidates, or produce plausible but invalid names. We introduce RareDx, which couples controlled evidence use with knowledge-graph-grounded policy optimization. RareDx-Harness normalizes heterogeneous records into one ranked-diagnosis task and compares direct inference, static retrieval, adaptive tools, and structured phenotype-gene-disease reasoning over a shared knowledge layer. The training pipeline combines Top-10 post-training with RareDx-KGPO, our knowledge-graph-grounded policy optimization method. Its reward projects predictions into a canonical disease graph and integrates curated graded relevance, ontology proximity, biomedical similarity, and phenotype consistency. Vocabulary and output-budget constraints prevent dense partial credit from rewarding fabricated or overlong differentials. Across eight benchmarks, the complete RareDx system centered on Qwen3.5-9B reaches 38.34 macro Hit@10, 1.60 points above GPT-5.5 under the archived protocol; a disjoint validation-selection audit retains a 6.80-point routing gain over Direct on held-out cases. The 27B system reaches 23.53/36.56/40.76 at Hit@1/5/10. Controlled ablations show that retrieval is not uniformly helpful and that controlled routing is central to the gain. These results indicate that structured medical knowledge can turn a compact model into a competitive diagnostic ranker across heterogeneous long-tail settings in clinical practice.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1d5d9630-a1aa-4

---

### 14. Beyond Token Scale: Chunk-Level Sparse Autoencoders for Reliable Semantic Feature Discovery

- **ArXiv ID**: [2609.35521v1](https://arxiv.org/abs/2609.35521v1)
- **作者**: Xu Wang, Yifan Yang, TingHao YU, Difan Zou
- **发布时间**: 2026-09-29
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.35521v1](https://arxiv.org/pdf/2609.35521v1)
- **相关度评分**: 10/10

#### 英文摘要

Sparse autoencoders (SAEs) expose features that help us understand and steer language models, but faithful reconstruction does not guarantee informative concepts. Token-level objectives reward lexical and formatting details alongside semantic content, all competing for a limited sparse budget. We introduce a family of chunk-level SAEs that encode mean-pooled activations over chunks, each a contiguous span of tokens: Mean-Chunk reconstructs the observed chunk, Cross-Chunk predicts an independently processed neighbor, and Joint-Chunk combines both targets. These designs separate the effect of a larger observation unit from that of predicting information shared across passages. With matched training data, chunk-level SAEs remain powerful interpretability tools while learning reliable semantic features that capture high-level concepts and respond selectively to relevant content. Their strengths are complementary: Mean-Chunk improves high-level feature discovery, reasoning detection beyond surface cues, and steering; Cross-Chunk leads document retrieval and classification transfer while producing selective, persistent features. Changing what an SAE sees and predicts yields reliable semantic features for more meaningful tasks. We demonstrate their practical value through gains across downstream tasks such as retrieval, reasoning detection, and steering.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7dfedabf-a364-4

---

### 15. SolveEdit: Benchmarking Visual Problem Solving in Generative Models

- **ArXiv ID**: [2609.35504v1](https://arxiv.org/abs/2609.35504v1)
- **作者**: Wenjie Shu, Yexin Liu, Harold Haodong Chen, Xuerui Qiu, Zehan Wang...
- **发布时间**: 2026-09-29
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.35504v1](https://arxiv.org/pdf/2609.35504v1)
- **相关度评分**: 10/10

#### 英文摘要

Machine intelligence is often evaluated through abstract reasoning problems, yet many real-world problems are visual, such as arranging objects, repairing layouts, or tracing routes. Solving these problems requires understanding a scene, inferring what must change to achieve a goal, and realizing that change without disturbing unrelated content. However, existing benchmarks mainly evaluate perception, generation, or explicitly specified transformations, leaving goal-driven visual problem solving underexplored. To bridge this gap, we introduce SolveEpIT, a benchmark for visual problem solving through scene transformation. Given an image and a goal, a model must infer a valid transformation from the request, the scene, or a visually expressed rule, then execute it while preserving unrelated content. SoLvEEDrr contains 2,728 cases. Atomic transition contracts specify required and protected conditions, enabling SoLvEScoRE to measure completion and unintended changes without a single reference output. The strongest evaluated model achieves only57.0% SolvEScore. We further introduce SolveEdiT-PLAN, a two-stage visual planner that instantiates the transition before generation. Under matched single-generation evaluation, it improves SoLvEScoRE by 9.1 points on average across three tested generators, including a gain from 57.0% to 71.6% for GPT-Image-2, without modifying the editor.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5c007f22-611b-4

---
