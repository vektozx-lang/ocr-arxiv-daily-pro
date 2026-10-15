# OCR arXiv Daily Pro — 2026-10-15

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-14 09:10 - 2026-10-15 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1da909b3-0845-4

---

## 📄 论文详情

### 1. Read, Parse, Describe: Unified Document Parsing with Visual Element Description Generation

- **ArXiv ID**: [2610.20335v1](https://arxiv.org/abs/2610.20335v1)
- **作者**: Yuheng Chen, Yufan Chen, Zhuojun Cai, Ruiping Liu, Junwei Zheng...
- **发布时间**: 2026-10-14
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.20335v1](https://arxiv.org/pdf/2610.20335v1)
- **相关度评分**: 10/10

#### 英文摘要

Document understanding systems are typically evaluated as separate components via layout analysis, optical text recognition, reading-order prediction, and image captioning. This separation leaves scientific figures, captions, and visual semantics weakly connected, and fails to measure whether a model can produce a single page-level parse that is both structurally faithful and semantically accessible. We introduce Read-Parse-Describe, a unified dataset for document parsing with visual element description generation. Given a page image, models are required to output an ordered list of layout elements containing bounding boxes, semantic labels, reading-order indices, recognized textual content, and alternative text descriptions for visual elements. The benchmark is built from 2,402 documents, comprising 18,163 continuous pages, 125,218 layout elements, and 11,338 visual instances. Besides, we further propose a plug-and-play space-awareness enhancer that reuses multi-layer visual features and injects grid-aware spatial guidance into vision-language tokens for layout-aware generation. Experiments across end-to-end VLMs and pipeline parsers show that existing systems still struggle to jointly recover reading order and visual semantics, while our enhanced model achieves strong joint performance. These results highlight the need to move beyond isolated document parsing modules toward unified models that jointly read, parse, and describe complex documents. The new dataset and code will be made publicly available at https://github.com/yufanchen96/RPD

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 144ded6c-a90a-4

---

### 2. Likelihood Is Not Authorship: Can We Reliably Measure Human Contribution in AI-Assisted Writing?

- **ArXiv ID**: [2610.19767v1](https://arxiv.org/abs/2610.19767v1)
- **作者**: Hasan Amin, Zhuoran Lu, Ming Yin
- **发布时间**: 2026-10-14
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.19767v1](https://arxiv.org/pdf/2610.19767v1)
- **相关度评分**: 10/10

#### 英文摘要

AI-text detection generally asks whether a machine wrote a text. As AI becomes an increasingly integral and accepted part of writing, the more relevant question is no longer whether AI was used, but how much of the text reflects human contribution. A prominent line of work estimates this by measuring how predictive a person's prompt is of the final text. We show that this measure can be easily manipulated. We introduce SPECIFICITY PADDING that simply asks the model to copy a few random IDs from the prompt, and that alone makes a title-only request look more human than one that supplies the article's key ideas. A context-swap audit then holds each document fixed, and only shows or hides the IDs to the evaluator. The score of the unchanged text swings by a third to half of its scale, and it rises for every document we test, on news and scientific abstracts, across varied LLMs from 3.8B to 753B parameters. The same articles can average 85\% human or 15\% human depending only on which prompt is on record, and even with no prompt at all, the output-only variant rewards the random strings themselves. An exact identity, the credit ledger, explains why. The score is a surprisal-weighted average over the text, so rare strings that the context makes copyable collect the credit, whatever they mean. A two-point bound marks a deeper limit. If the prompt could have been machine-written, every transcript-only method must, in the worst case, miss by half the contribution at stake. Likelihood-based scores alone cannot reliably establish human contribution without evidence of what the person added and how the text was produced.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a32373d9-71be-4

---

### 3. Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR

- **ArXiv ID**: [2610.20461v1](https://arxiv.org/abs/2610.20461v1)
- **作者**: Nguyen Nguyen, Yongyi Zang
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.20461v1](https://arxiv.org/pdf/2610.20461v1)
- **相关度评分**: 10/10

#### 英文摘要

Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER keeps the score of a whole transcription, where it tracks readers as well as semCER or better, and semCER breaks that score down into named edits. The charges track readers' ratings edit by edit in English, Vietnamese, and Chinese and put the edits readers rate most severe near the top of a sorted list. On pairs drawn where CER and semCER disagreed, readers side with semCER more often than with normalized CER in English and Chinese, and equally often in Vietnamese. Across 16 languages, the judge charges a wrong diacritic or tone mark almost nothing in Spanish but nearly a wrong letter's severity in Telugu. Where we can count real words, a general VLM's wrong letter forms one far above chance while a classical pipeline's stays near it. We release the 61 million judged edits, the aggregated reader ratings, and the distilled scorer at https://github.com/nguyenx2t/semcer.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: f9356f52-f4ac-4

---

### 4. TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering

- **ArXiv ID**: [2610.19551v1](https://arxiv.org/abs/2610.19551v1)
- **作者**: Yiyang Chen, Guo-Hua Wang, Yaoli Liu, Qing-Guo Chen, Zhao Xu...
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.19551v1](https://arxiv.org/pdf/2610.19551v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-to-image models increasingly generate readable Chinese text that still contains local rendering defects, such as a character with an extra or missing stroke or a malformed component. Such errors are invisible to OCR and vision-language models, which are trained for recognition and are therefore invariant to the very structural deviations that define a rendering error. We formalize text rendering verification as a target-conditioned problem: given a target character and an image crop, decide whether the crop is a correct rendering of that character. Our verifier TEXTVERIFIER feeds the text tower a character's Ideographic Description Sequence (IDS) rather than a single-character symbol, and is trained on 12.7M crop-IDS pairs plus label-free "same-character, different-quality" hard pairs sampled from the training trajectory of a text-region inpainting model. To evaluate this ability we build TEXTRENDERBENCH-ZH, the first per-character benchmark for generated Chinese text, annotating position, identity, and correctness for 7,358 characters. TEXTVERIFIER reaches an F1 of 0.844, far above OCR confidence (0.526), a general VLM (0.329), and TextPecker (0.590). Used as a per-character reward for Flow-GRPO post-training, it further reduces rendering errors, showing that its score can both detect and correct errors.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 2b563e64-a3cc-4

---

### 5. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation

- **ArXiv ID**: [2610.20603v1](https://arxiv.org/abs/2610.20603v1)
- **作者**: Xiaoli Xu, Zhengtao Wu, Zhengze Xu, Tao Liu, Yongchao Du...
- **发布时间**: 2026-10-15
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.20603v1](https://arxiv.org/pdf/2610.20603v1)
- **相关度评分**: 10/10

#### 英文摘要

We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout Thinker Optimization (LTO) aligns the rewriter with both caption and rendered-image quality via alternating domain-specific policy optimization. SKU-DiT, trained under Reinforce-Distill-Reinforce (RDR) progressive training, conditions jointly on the white-background product image, the trademark crop, and the structured layout to hold subject fidelity, trademark integrity, and character-level text accuracy together. The framework runs in production at a scale of millions of main images per day with a latency of a few seconds per image, which we believe makes it among the first systems of this kind to operate at commercial scale. We also release CommerceGen-Bench, a benchmark of hard cases collected from live traffic across all product categories. On it, our framework achieves the highest overall scores among the evaluated open-source baselines on both editing tracks, with and without prompt enhancement. It also matches much larger closed-source models, and beats several of them at Instruction Following and Product Integration - the two properties that determine whether an image can be published.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 358d0a20-b24a-4

---

### 6. Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models

- **ArXiv ID**: [2610.20479v1](https://arxiv.org/abs/2610.20479v1)
- **作者**: Harsh Kumar
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.20479v1](https://arxiv.org/pdf/2610.20479v1)
- **相关度评分**: 10/10

#### 英文摘要

Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move when English test items are merely reworded, test every language shift item by item, and check that the test catches shifts we inject on purpose. In all 70 model-language pairs the stereotype score falls below its English level, and for Hindi, Korean and Swahili the drop clearly exceeds what rewording English produces; most of it comes from StereoSet items. Judging every translation, we find that imperfect ones drop more, but faithful translations alone drop nearly as much. Still, a lower average does not show that a model is fairer. An item's English score predicts its translated score far less well than its reworded score (correlation 0.23, 0.27 on faithful translations, vs. 0.48), while scores stay as far from neutral, models agree on translated items, and within Hindi or Spanish a translated item's score correlates with its own rewording at 0.84 and 0.82. The average cannot distinguish lower bias from a different pattern of item-level scores. We also document three common pipeline errors that silently erase bias signal, and release our code.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7002acfc-2072-4

---

### 7. Cascaded Retrieval with Cross-Modal Query Refinement for Efficient Visual Document Search

- **ArXiv ID**: [2610.20367v1](https://arxiv.org/abs/2610.20367v1)
- **作者**: Diana Turmakhan, Aseem Srivastava, Vivek Gupta, Iryna Gurevych, Thamar Solorio
- **发布时间**: 2026-10-14
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.20367v1](https://arxiv.org/pdf/2610.20367v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieving information from visually rich documents requires matching queries against pages that contain complex evidence in tables, figures, and layout-dependent structures. Current vision-language retrievers address this but incur query-time costs that grow with corpus size and are impractical to scale. We propose SCOUT, a cascaded two-track retrieval framework that separates retrieval performance from exhaustive search. The visual track first uses a lightweight parent retriever to filter the corpus to a compact candidate pool, then applies a stronger multi-vector reranker only to those candidates. In parallel, a semantic track retrieves over hierarchical page and document summaries generated offline to provide a signal complementary to visual matching. The outputs are fused through cross-modal query refinement, which uses semantic scores to adjust the visual query representation before final ranking. We evaluate SCOUT on 4 major benchmarks against 6 baselines and observe a significant query-time latency improvement up to 80.7x (28.8x on average) relative to the best baseline, while exceeding state-of-the-art retrieval performance by up to 7.8% NDCG across all benchmarks.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 87c13306-2786-4

---

### 8. Latent Compaction with Test-Time Training

- **ArXiv ID**: [2610.20582v1](https://arxiv.org/abs/2610.20582v1)
- **作者**: Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.20582v1](https://arxiv.org/pdf/2610.20582v1)
- **相关度评分**: 10/10

#### 英文摘要

Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entries using reconstruction importance, teacher attention, and key-space diversity. Training first fits attention outputs and log-normalizers to those of the full cache, with reconstruction-selected entries held fixed. It then jointly optimizes the entire cache through end-to-end distillation from the full-cache model. Model weights remain frozen throughout, and training uses only generic prompts about the document, without access to downstream questions or answers. Experiments on RULER, LongBench, and Phonebook Lookup demonstrate substantial gains over budget-matched compression baselines. On a RULER, for example, our method achieves 96.7% accuracy at 32$\times$ compression, compared with 40.0% for KVZip+. The method also transfers across model scales and families, with retrieval gains on both Qwen3 and MiniCPM5. These results show that treating the KV cache as a neural network and optimizing it with test-time training can preserve retrieval accuracy under aggressive compression. The code is released at https://www.github.com/THUNLP/latent-compaction

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 300656d4-1100-4

---

### 9. Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge

- **ArXiv ID**: [2610.20570v1](https://arxiv.org/abs/2610.20570v1)
- **作者**: Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto
- **发布时间**: 2026-10-15
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.20570v1](https://arxiv.org/pdf/2610.20570v1)
- **相关度评分**: 10/10

#### 英文摘要

Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. We document three DPO attempts, all negative, including a case where the training reward margin reaches 1.0 while free generation does not change at all, and show that safety came from a dedicated safety-SFT (LLM-jp AnswerCarefully style), refined over three iterations until closing the safety-helpfulness frontier. A controlled scan of the fraction of general data in the safety-SFT mix (10% to 60%) reveals a non-monotonic over-refusal curve with a knee point at 40-50%. The final model is compared against four external PT-BR models on the same items, with Wilson confidence intervals and paired McNemar tests with Holm-Bonferroni correction: the lower bound of its safety interval (94.1%) lies above the upper bound of all four baselines. We also report a methodological finding for LLM-judge evaluation: on two of six safety items in MT-Bench-PT, the judge categorically refuses to assign a score regardless of the evaluated response, silently reducing the effective N of that category in every prior report of the project. We complement this with an n-gram decontamination check and a Chinchilla-anchored compute-budget table that attributes the gap in general capability to pre-training scale rather than alignment methodology. All code, raw data, logs, and scripts that produce every reported number are publicly released.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 97b56050-5b87-4

---

### 10. PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis

- **ArXiv ID**: [2610.20538v1](https://arxiv.org/abs/2610.20538v1)
- **作者**: Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Zhangyue Yin...
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.20538v1](https://arxiv.org/pdf/2610.20538v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, producing interactive artifacts even from a text description or a screenshot alone. Yet their data and training remain closed, and open progress is held back by the quantity and quality of available data and by the pipelines and methods for producing it. Quality is the harder of the two, since a sample must be correct as a program, well built, and above all visually right once rendered. No existing signal covers all three. Execution often returns just a pass or fail, code similarity does not map to the visual output, and task-specific verifiers do not generalize. To push open progress further, we start from the data side with PrismaForge, a hierarchical data pipeline centered on a synthesized rubric that decomposes these factors into checkable criteria. The same rubric serves as both filter and reward: it curates the supervised corpus, then drives reinforcement learning on visual-coding tasks. Leveraging PrismaForge for data synthesis and filtering, we build PrismaCoder-2M, the most diverse open dataset for multimodal code intelligence and the largest to date. On the model side, we train PrismaCoder-9B and PrismaCoder-35B on this data and release both. They lead the open state of the art by a wide margin and rival leading proprietary systems. Our analyses further show that the proposed rubric-based pipeline improves multimodal coding performance across model backbones. We release our code and data at https://qiushisun.github.io/PrismaCoder-Home/.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: e977a38b-27dc-4

---

### 11. From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence

- **ArXiv ID**: [2610.20417v1](https://arxiv.org/abs/2610.20417v1)
- **作者**: Jiahong Qian
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.20417v1](https://arxiv.org/pdf/2610.20417v1)
- **相关度评分**: 10/10

#### 英文摘要

Audits of large language model (LLM) extraction from full-length documents report severe unreliability, leaving two questions open: what the failures actually consist of, and whether confidence signals can turn unreliable output into usable output. We run a preregistered, fully frozen evaluation of two new-generation low-cost LLMs (DeepSeek-V4-Flash, GLM-5.3-Flash) with a flagship-tier control (GPT-6.1-Sol) on a public corpus of 354 incident campaigns (315 unique reports, 630 model-report evaluations), scoring extraction quality against gold, confidence calibration, and robustness to single-sentence perturbations. Three findings emerge. (1) Unreliability persists across tiers: micro precision is 0.03-0.34 and verbalized calibration error (ECE) 0.53-0.94 across both splits; the gap does not close at the flagship tier. (2) The dominant failure is not hallucination: a full mention census plus a three-tier annotation of 360 sampled candidates (two independent LLM annotators from vendors outside the evaluated set, Cohen's kappa = 0.79 on the preregistered acceptance line, fully disclosed) back-projects to 65.6% background mentions and 19.9% gold-scope gaps, with only 1.2% unsupported candidates. (3) Confidence ranks but does not verify: zero-cost self-consistency-frequency tiering passes a preregistered top-30% precision-gain bar in all six test-split model-type cells (4/6 on train), the zero-cost text-frequency x SC frequency combination wins 3, ties 2, loses 1 across cells, yet relation-level counterfactuals on all 45 targets show that a single misattribution sentence flips high-confidence judgments in 95.6-100% of cases, and even a background sentence explicitly marked as unrelated still binds a fake vulnerability in up to 26.7% of them. We conclude with a deployment boundary: confidence tiering may set review priorities, never truth.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 04119446-0224-4

---

### 12. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents

- **ArXiv ID**: [2610.20344v1](https://arxiv.org/abs/2610.20344v1)
- **作者**: Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu...
- **发布时间**: 2026-10-14
- **分类**: cs.SE, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.20344v1](https://arxiv.org/pdf/2610.20344v1)
- **相关度评分**: 10/10

#### 英文摘要

Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a two-stage benchmark that evaluates long-horizon harness engineering directly. In Stage 1, a build model operating inside a fixed builder harness receives an interface-only contract skeleton and a development document that consolidates behavior across twelve frontier harnesses, and then constructs a complete candidate harness in an isolated container. In Stage 2, the frozen candidate harness runs in containers separate from the construction environment, one per test case, and is driven end to end by a scripted mock model. We score each test case using four observable channels, namely the requests sent to the model, the files on disk, the process exit code, and the command output; positive controls rule out vacuous passes. Across nineteen frontier models, each evaluated with three independent builds on 328 test cases, GPT-6 Astra achieves the highest pass rate at 53.05%, while the weakest model reaches 27.44%, a gap of roughly twenty-six percentage points. Even the strongest model fails nearly half of the test cases, and failures cluster around how cross-cutting functionality is split across modules. To our knowledge, Doc2Harness provides the first deterministic benchmark for measuring long-horizon harness engineering.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: be4e9a38-451d-4

---

### 13. Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis

- **ArXiv ID**: [2610.20319v1](https://arxiv.org/abs/2610.20319v1)
- **作者**: Yinzhen Huang, Jiahe Xie, Yitong Sun, Ruochen Zhang, Xingxing Wei
- **发布时间**: 2026-10-14
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.20319v1](https://arxiv.org/pdf/2610.20319v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, yet their susceptibility to backdoor attacks remains a formidable challenge. While existing defenses have evolved from visual-centric patch cues to unsupervised internal attention statistics, they are fundamentally constrained by a reliance on static snapshots and attack-specific heuristics. Given the intricate interplay between dual modalities, the vast design space for multimodal triggers allows diverse threats, such as textual injections, sub-perceptual noises, and coordinated cross-modal triggers, to easily circumvent such rigid priors, particularly when attack types are unknown in real-world applications. In this paper, we rethink backdoor detection by shifting the diagnostic paradigm from static observations to dynamic output evolution. We observe that a successful attack inevitably hijacks the model's decoding trajectory, skewing internal modal contributions during generation while maintaining an abnormal output invariance despite input perturbations. To capture this behavior, we propose EVO-Detect, a unified detection framework that monitors the dynamic evolution of internal signals during early decoding steps through two complementary channels: Attention Flow and Logits Flow. The attention branch measures how image-text attention allocation evolves during early generation, whereas the logits branch quantifies the sensitivity of the output distribution to modal perturbations through interventional ablations. We then convert these trajectories into compact sample-level metrics and normalize them against negative-control signatures so that natural perturbations are less likely to be mistaken for backdoor evidence. Extensive evaluations show that our approach substantially outperforms state-of-the-art baselines such as BYE and TCAP across diverse attack families.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4cc9af8f-7425-4

---

### 14. Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics

- **ArXiv ID**: [2610.20261v1](https://arxiv.org/abs/2610.20261v1)
- **作者**: Junze Zhu, Weihao Chen, Zhiyang Zhou, Zhen Wu, Xinyu Dai
- **发布时间**: 2026-10-14
- **分类**: cs.LG, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.20261v1](https://arxiv.org/pdf/2610.20261v1)
- **相关度评分**: 10/10

#### 英文摘要

Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the runtime semantics behind that action implicit. We introduce Harness Policy Distillation (HPD), which makes these runtime control semantics an explicit training target alongside actions to align the harness policy. HPD replays reference trajectories through the harness to recover the runtime semantics that are implicit in ordinary trajectory data, and represents them as control documents at each model-call boundary. These documents provide privileged information for a teacher to generate actions, while harness verification ensures that the resulting targets are executable under the runtime contract. We jointly train a shared model on the runtime semantics recovered from control-state privileged information and native history, thereby internalizing these semantics into the model policy. At deployment, the trained model uses the original harness interface without requiring the control document or any additional supplement. On TRAJECT-Bench with the Pi harness, Qwen3-8B trained with HPD reaches 22.98% autonomous task success and 49.23% runtime compliance, against 3.09% and 19.90% for the unadapted model. Harness-verified teacher actions substantially improve the native deployment policy, while joint control-state supervision provides further gains in task completion and runtime compliance. HPD turns executable runtime semantics into dense supervision for learning harness-compatible actions at each decision boundary.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a54629d1-1e42-4

---

### 15. Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance

- **ArXiv ID**: [2610.20220v1](https://arxiv.org/abs/2610.20220v1)
- **作者**: Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao...
- **发布时间**: 2026-10-14
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.20220v1](https://arxiv.org/pdf/2610.20220v1)
- **相关度评分**: 10/10

#### 英文摘要

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show it can be made dramatically more efficient. Pushing this efficiency to its extreme, we reduce trajectory supervision to a single sample, the strictest setting possible, and find that it causes severe quality collapse. We trace this to the teacher's trajectory geometry: the high-noise regime, governing semantic layout and motion, and the low-noise regime, governing fine texture exhibit fundamentally different curvature and optimization behavior, so a single monolithic student cannot jointly fit both, causing severe representation interference. Motivated by this, we propose Glance Forcing, a lightweight distillation framework that decouples the denoising trajectory into two complementary slow and fast experts, each guided by a tailored, stage-specific objective, while keeping the pretrained teacher entirely frozen. This decoupling further reveals a general mechanism underlying few-step distillation: PF-ODE distillation mainly straightens the few-step trajectory geometry, while the subsequent distribution-matching stage independently governs distributional quality. Using only one PF-ODE trajectory, Glance Forcing already surpasses the fully-trained state-of-the-art baseline, raising the VBench Total score from 84.04 to 84.22 while cutting trajectory-collection cost from thousands of GPU-hours to about one A100-GPU-hour, with markedly larger gains in dynamic degree, VisionReward, and instruction-following, and consistent preference from human raters over strong baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 607e4574-98fd-4

---
