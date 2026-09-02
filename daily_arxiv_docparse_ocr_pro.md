# OCR arXiv Daily Pro — 2026-09-02

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-01 09:10 - 2026-09-02 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

## 📄 论文详情

### 1. On the Design Fundamentals of Pixel Text Representation Learning

- **ArXiv ID**: [2609.01147v1](https://arxiv.org/abs/2609.01147v1)
- **作者**: Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang, Yu Rong, Hong Cheng...
- **发布时间**: 2026-09-01
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.01147v1](https://arxiv.org/pdf/2609.01147v1)
- **相关度评分**: 10/10

#### 英文摘要

Text-rich visual inputs require models that can read, retrieve, and compress language directly in pixel space, yet existing pixel-text encoders struggle with fixed resolution pretraining, visual shortcut learning, weak visual grounding, and multilingual visual text understanding. In this work, we investigate the fundamental design principles required for robust visual text representation learning. Through systematic controlled ablations, we identify four critical components: variable image resolutions and rendered font sizes provide spatial proxies for high-resolution document generalization; natural image-text pairs are indispensable for grounding and prevent text-only collapse; layout-aware rendering helps prevent pixel-level shortcuts; and a two-stage multilingual curriculum enables effective cross-lingual alignment. By integrating these principles into a scalable training recipe, we train Pixel Linguist II, a native-resolution vision encoder trained with on-the-fly rendering, unified contrastive grounding, and a multilingual curriculum over 280M training examples. Pixel Linguist II sets new state-of-the-art results on English, cross-lingual, and multilingual Visual STS and ViDoRe, while also enabling better MLLM downstream evaluation. Notably, Pixel Linguist II remains robust under 80\% visual token compression, showing great promise for optical context compression. Our code and resources are available at https://github.com/Pixel-Linguist/Pixel-Linguist-II.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 2. Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics

- **ArXiv ID**: [2609.01575v1](https://arxiv.org/abs/2609.01575v1)
- **作者**: Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin, Olga Tsymboi, Anatolii Potapov...
- **发布时间**: 2026-09-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.01575v1](https://arxiv.org/pdf/2609.01575v1)
- **相关度评分**: 10/10

#### 英文摘要

Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents curated by a Difficulty-Aware pipeline for layout diversity, fact-extractability, and cross-model consistency. Fitting on a single H100 and serving heterogeneous workflows via prompting, the model leads all deployable (non-reasoning) baselines up to an order of magnitude larger. A quality-adjusted cost analysis, with confirmation and correction costs calibrated from production telemetry, shows it reduces expected costs by over 80% against the human baseline and by more than 50% against the best competing open-source model, while larger baselines remain economically unviable.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 3. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

- **ArXiv ID**: [2609.01316v1](https://arxiv.org/abs/2609.01316v1)
- **作者**: Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, Yong Zhuang, Ozan Irsoy
- **发布时间**: 2026-09-01
- **分类**: cs.IR, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.01316v1](https://arxiv.org/pdf/2609.01316v1)
- **相关度评分**: 10/10

#### 英文摘要

Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing that shifts multimodal reasoning to index time. During ingestion, a multimodal LLM converts rendered pages into verified textual fields that are indexed with BM25F and optionally fused with dense retrieval, enabling text-centric serving over multimodally grounded evidence. On ViDoRe V3, MIDR Hybrid achieves 0.6219 average nDCG across five English domains, a 23.0% relative gain over BM25, remaining competitive with ColQwen2.5. On two French-document domains, enrichment bridges English queries and French page text, lifting BM25 from 0.1532 to 0.5448 nDCG and outperforming ColQwen2.5. Across all seven domains, MIDR leads ColQwen2.5 on four while using approximately 9x smaller index memory and approximately 2x lower query latency. These results establish index-time multimodal reasoning as a compelling accuracy-deployment alternative to serving-time visual late interaction.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 4. Joint Training Is Not Enough: Conditioned Cross-Granularity Training for Multimodal Document Understanding

- **ArXiv ID**: [2609.00756v1](https://arxiv.org/abs/2609.00756v1)
- **作者**: Chengguang Gan, Yunhao Liang, Hanjun Wei, Qinghao Zhang, Shiwen Ni
- **发布时间**: 2026-09-01
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.00756v1](https://arxiv.org/pdf/2609.00756v1)
- **相关度评分**: 10/10

#### 英文摘要

The Mutual Reinforcement Effect (MRE) asks whether a fine, span-level and a coarse, document-level task help each other when one model handles both. We test it in multimodal document understanding on three corpora, two of receipts and one of scanned business forms, comparing single-task, joint and conditioned training, which puts one granularity's gold output in the other's prompt during training only. We build Doc-MRE, an annotation layer pairing gold field extraction (point) with four document-level facets (line), from a three-judge LLM committee under a pre-registration, validated by blind re-annotation. One predicate, fixed in advance: at a shared recipe, a regime reinforces if it beats the matched single-task model on both granularities. Mixed joint training, the arrangement prior MRE work assumes, reinforces on no corpus at the main scale: it is below both single-task models on CORD and trades one granularity for the other on the two others, as single-task tuning does. Conditioned training reinforces on two of the three, CORD (+0.5 point, +4.8 line) and the forms corpus (+7.2 point, +11.0 line), resolvably on the coarse side and directionally on the fine one, and trades on WildReceipt; at that recipe no alternative measurably beats it on either side anywhere. Two byte-identical-prompt controls separate content from format: shuffled conditioning destroys the coarse-side skill but costs the fine side far less, and a neutral-content control reproduces the whole fine-side gain on WildReceipt, which is therefore prompt structure but buys nothing resolvable on the other two. On the forms corpus conditioning buys collapse avoidance: mixed training and the neutral control both assign the majority semantic label to all 50 test documents; only conditioning recovers the gold distribution. Probes find the information decodable under every regime with no resolvable increase under conditioning.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 5. Can Scene Text Recognition Read Rare Compositions?

- **ArXiv ID**: [2609.00816v1](https://arxiv.org/abs/2609.00816v1)
- **作者**: Genpei Zhang
- **发布时间**: 2026-09-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.00816v1](https://arxiv.org/pdf/2609.00816v1)
- **相关度评分**: 10/10

#### 英文摘要

Scene text recognition is reported as 89--97% accurate on the six standard benchmarks, and the problem is widely treated as saturated. We present an alternative reading. When the same test images are stratified jointly by ground-truth word rarity and character n-gram novelty against a reference corpus, accuracy at the rare-word x rare-trigram corner of the resulting 5x5 grid drops 10--18 pt below the q3/q3 centre across nine English specialised recognisers, and the same direction (corner below centre) holds on all 13 of 13 (language, model) pairs we test across four writing systems (Latin, Han, Han+kana, Arabic). The drop is not a capacity bottleneck. A 6x vision-backbone scale-up (CLIP4STR-Base 158M -> CLIP4STR-Huge 1.0B, OpenCLIP ViT-H/14 LAION-2B) leads every benchmark in aggregate accuracy yet leaves the stress corner unchanged (86.9 -> 86.5, within paired-bootstrap noise). Four converging probes--layer-wise probing, confidence-when-wrong, attention re-balancing, and a cross-script commit-vs-abstain error split--localise the failure to the autoregressive decoder's lexical prior. We then ask how much of the gap existing techniques recover. Of 16 non-architectural mitigations, the largest mean q5/q5 gain is +1.3 pt and none clears the paired-bootstrap noise floor; the only intervention that does is the architectural shift from autoregressive to CTC decoding (SVTRv2, +2.5 pt, p=0.02, n=474). A confidence-routed AR-CTC ensemble adds a directionally consistent +0.6 pt that stays within noise, and its dominant learned coefficient is each model's own minimum-softmax confidence--independently echoing the mechanism above. No configuration we test improves both the compositional corner and aggregate accuracy. The rare-input long tail thus points to architectural change rather than added capacity.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 6. LatentPress: Context Compression Beyond Text and Vision

- **ArXiv ID**: [2609.01507v1](https://arxiv.org/abs/2609.01507v1)
- **作者**: Zhengze Zhou, Hejian Sang
- **发布时间**: 2026-09-02
- **分类**: cs.LG, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.01507v1](https://arxiv.org/pdf/2609.01507v1)
- **相关度评分**: 10/10

#### 英文摘要

Compressed context is usually carried as human-readable text or as rendered images that must be decoded, even when its consumer is a language model. We introduce LatentPress, which writes conversational histories and long documents into a third representation: continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference. A small reader-matched writer compresses $4$-$16\times$ while training only an adapter (4.2M-26.2M parameters, $\sim\!0.1\%$ of the decoder). On LongMemEval, LatentPress reaches $0.504$ accuracy at $7.70\times$ compression versus $0.490$ for uncompressed evidence, outperforming text summaries (0.184) and OCR-based compression (0.426 to 0.312). On LongBench-QA, in-domain writers match or exceed raw-context reading at $4$-$8\times$ compression, while $16\times$ trails raw. Writing takes 43ms per conversation, roughly an order of magnitude faster than text summarization or OCR reconstruction, and reading is $5$-$9\times$ faster than raw context or cached OCR. We validate the interface under two transfer settings, zero-shot from UltraChat to LongMemEval memory QA and from LongMemEval-derived QA to unseen LongBench document domains, establishing direct soft tokens as a practical machine-facing context interface beyond text and vision. The implementation of the experiments could be found at: https://github.com/xuyd16ai/context_softtoken_compress .

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 7. MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence

- **ArXiv ID**: [2609.01235v1](https://arxiv.org/abs/2609.01235v1)
- **作者**: Walid Saidi
- **发布时间**: 2026-09-01
- **分类**: cs.CR, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.01235v1](https://arxiv.org/pdf/2609.01235v1)
- **相关度评分**: 10/10

#### 英文摘要

MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request receipts, ordered disclosure, and three mutation terminal types. The released protocol contains 18 versioned object schemas, 39 recall vectors, 15 mutation vectors, and 37 closed recall failure reasons. Independent Node and Python implementations agree on verdict and primary reason for all 72 structural and cryptographic terminals; a production-conformance corpus agrees on 42/42 cases across 28 required classes. A clean Node v26.8.1 installation reaches first-boot, restart, and scheduler readiness with no experimental memories. A separately scoped 120-unit Canary experiment supports only explicit-marker traversal. Every public table regenerates from a self-hashed aggregate, and an independent verifier reconstructs the statistics and claim boundaries. Historical V1 empirical results remain historical. MutMem V2 supports claims about portable integrity, authorization, traceability, conformance, and reproducibility under stated assumptions; it does not establish semantic truth, universal robustness, or independent replication.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 8. SpatialGuard: Harness-Guided Verifiable Spatial Reasoning for Text-to-Image Generation

- **ArXiv ID**: [2609.01582v1](https://arxiv.org/abs/2609.01582v1)
- **作者**: Ziyun Qian, Zizhi Chen, Yizhou Liu, Mingyang Sun, Dingkang Yang...
- **发布时间**: 2026-09-02
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.01582v1](https://arxiv.org/pdf/2609.01582v1)
- **相关度评分**: 10/10

#### 英文摘要

Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned methods improve controllability, but often lack an optimizable and verifiable spatial intermediary before visual sampling. As a result, object relations, occlusion, visibility, and camera constraints can decay during multi-round generation. This paper presents SpatialGuard, a structured layout-guided framework for complex 3D spatial text-to-image generation. SpatialGuard parses prompts into image synthesis-oriented 3D layouts through a Spatial Layout Architect, realizes them as visual conditions and candidate images through a Visual Realizer, and uses a Visual Alignment Critic to validate consistency among prompt, layout, and image. To keep constraints stable across iterations, SpatialGuard introduces a Layout Harness that organizes rule constraints, tool invocation, shared knowledge, and feedback loops around the editable layout state. This design turns complex spatial generation from implicit prompt following into a verifiable process of planning, realization, validation, and repair. Comprehensive experiments show that SpatialGuard achieves state-of-the-art performance in complex 3D spatial layout generation and improves spatial faithfulness over existing text-to-image and layout control baselines.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 9. A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains

- **ArXiv ID**: [2609.01563v1](https://arxiv.org/abs/2609.01563v1)
- **作者**: Ema Salkić, Alexander Fichtl, Philipp Ulrich, Hans Ehm, Marta Bonik...
- **发布时间**: 2026-09-02
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.01563v1](https://arxiv.org/pdf/2609.01563v1)
- **相关度评分**: 10/10

#### 英文摘要

Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linking each item to its category, sources, and related events, then merges duplicates and ranks them with a three-layer mechanism combining an algorithmic formula, an LLM relevance adjustment, and expert validation. Applied to five companies across the value chain, the pipeline produces 76,207 scored items, of which an independent check finds 92.6% valid. The automated rankings match expert judgment at an average Spearman correlation of 0.55 for risks and 0.72 for opportunities, and the resulting matrices identify trade restrictions as the dominant cross-company risk.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 10. When Tokenization is Secretly Output Supervision

- **ArXiv ID**: [2609.01386v1](https://arxiv.org/abs/2609.01386v1)
- **作者**: Tanja Baeumel, Josef van Genabith, Simon Ostermann
- **发布时间**: 2026-09-01
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.01386v1](https://arxiv.org/pdf/2609.01386v1)
- **相关度评分**: 10/10

#### 英文摘要

Tokenization in language models is treated by default as an input preprocessing decision. We argue that this framing is incomplete: in autoregressive models, tokenizer granularity determines what the model must resolve in a single forward pass, and therefore the supervision signal it receives. This affects both the difficulty of the learning problem and the representations that emerge inside the model. We test this in a controlled experiment on numeric reasoning with a novel decoupling of input and output tokenization. As the output supervision view predicts, differences in task performance, training dynamics, and model internals are induced by output tokenization and largely invariant to input tokenization. This may matter in practice, because models with different tokenization strategies differ not only in input representation but in the task they were trained on. Comparisons between models may thus partly reflect task definition rather than ability. A survey of 120 recent *CL papers on numeric reasoning confirms that this is rarely acknowledged: only about 10% report the numeric tokenization of the models they evaluate, while 69% compare across tokenization, and thus supervision, regimes without reporting it. While prior work documents that tokenization consistently affects model performance, there is no principled account of why. We argue that framing tokenization as output supervision provides that account.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 11. VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models

- **ArXiv ID**: [2609.01325v1](https://arxiv.org/abs/2609.01325v1)
- **作者**: Zhiqi Huang, Vivek Datla, Zhichao Xu, Puxuan Yu, Vivek Srikumar...
- **发布时间**: 2026-09-01
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.01325v1](https://arxiv.org/pdf/2609.01325v1)
- **相关度评分**: 10/10

#### 英文摘要

Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of maliciously crafted documents into the corpus to distort ranking behavior. We propose VerTox, the first framework to formulate corpus poisoning as a verifiable reward-guided reinforcement learning (RLVR) problem. By explicitly coupling ranking distortion with factual corruption through specialized reward shaping, we fine-tune compact LLMs into adversarial generators. Experiments demonstrate that our method achieves near-perfect attack success rates, producing adversarial documents that frequently rank higher than target documents across major neural ranking architectures, as well as a proprietary commercial embedding model. The generated adversarial documents are fluent and exhibit low perplexity, making them difficult to detect. Furthermore, by explicitly encouraging factual corruption, our adversarial documents significantly degrade the performance of a downstream RAG application.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 12. Agentic Multimodal Models for Environmental Hyperspectral Unmixing

- **ArXiv ID**: [2609.01289v1](https://arxiv.org/abs/2609.01289v1)
- **作者**: Michał Cholewa, Luca Ciampi, Nicola Messina, Przemysław Głomb, Giuseppe Amato
- **发布时间**: 2026-09-01
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.01289v1](https://arxiv.org/pdf/2609.01289v1)
- **相关度评分**: 10/10

#### 英文摘要

Hyperspectral unmixing is a key task in remote sensing that aims to decompose mixed pixels in hyperspectral images into their constituent material signatures, or endmembers, and their fractional abundances. Conventional modular approaches estimate the scene composition through successive model-order estimation, endmember extraction, and abundance estimation stages, whose errors can lead to redundant or ambiguous candidate components and ultimately affect the recovered decomposition. We introduce an algorithm-agnostic, large vision-language model (LVLM)-driven agentic framework that refines the outputs of such pipelines rather than replacing their underlying numerical algorithms. Starting from an initial decomposition, the agent iteratively gathers complementary spectral and spatial evidence through dedicated tools, including spectral-library retrieval and abundance-map visualization, and modifies the active endmember set through merge and discard operations followed by abundance re-estimation. We apply the same refinement procedure to several modular pipelines combining different model-order, extraction, and abundance-estimation methods, and evaluate it on HYDICE Urban, Jasper Ridge, and Stonewall Playa. Experiments show that the proposed agent consistently improves endmember cardinality and generally improves the recovered spectral signatures and abundance maps across heterogeneous modular pipelines, while remaining competitive with integrated end-to-end unmixing methods, including CNN-AE, uDAS, and R-CoNMF. These results highlight the potential of tool-using LVLM agents to combine spectral and spatial evidence for algorithm-agnostic refinement of physically grounded hyperspectral unmixing decompositions. Code is publicly available at https://anonymous.4open.science/r/agentic-hu.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 13. Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR

- **ArXiv ID**: [2609.01354v1](https://arxiv.org/abs/2609.01354v1)
- **作者**: Esther Xin
- **发布时间**: 2026-09-01
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.01354v1](https://arxiv.org/pdf/2609.01354v1)
- **相关度评分**: 10/10

#### 英文摘要

Reinforcement learning with verifiable rewards (RLVR) and standard benchmark evaluation both rely on an automatic verifier that turns a free text answer into a binary reward. Prior work reports that one evaluation harness accepts only about 94% of its own ground truth answers, blaming LaTeX parsing. That is an aggregate: it does not say which answer forms consume the error budget. We supply the decomposition. We apply metamorphic testing to the verifier rather than the model, generating certified equivalent answer variants, that is, rewrites that preserve mathematical meaning by construction, so that any rejection is a provable false negative needing no human adjudication. We then measure rejection per answer category across four widely used verifiers over 307,420 verdicts. We find three things. (1) Self validation ranges from 53.8% to 95.2% on identical inputs, a spread of 41.3 points. The published figure describes one implementation, not the task; two configurations of the same library disagree on 49.9% of pairs. (2) The residual is not spread across parsing categories but concentrated in whitespace and punctuation, which account for 93.0% of in contract failures for the default LaTeX configuration. A trailing period or newline dominates the budget. (3) Separating rejection from execution failure shows that verifiers with similar aggregate error fail for opposite reasons, and that a reference numeric cascade accepts off by one wrong answers as a step function of magnitude, from 0% below 10^4 to 100% at or above, because its relative tolerance is scale invariant.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 14. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System

- **ArXiv ID**: [2609.01607v1](https://arxiv.org/abs/2609.01607v1)
- **作者**: Penghao Wu, Haiwen Diao, Weichen Fan, Lewei Lu, Dahua Lin...
- **发布时间**: 2026-09-02
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.01607v1](https://arxiv.org/pdf/2609.01607v1)
- **相关度评分**: 10/10

#### 英文摘要

While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal to the other: generation enriches the visual features learned for understanding, while understanding strengthens vision--language alignment for generation. However, when both objectives are forced through the same computation path, one tends to dominate. A task-decoupled architecture that specializes conflicting visual computation while preserving semantic interaction avoids this asymmetric degradation. At the task level, through three case studies, we find positive bidirectional transfer when understanding and generation tasks rely on shared knowledge. At the system level, we show that an end-to-end UMM outperforms a matched planner--executor pipeline on complex tasks that explicitly require both image understanding and generation. Together, these results show that the value of UMMs extends beyond a unified interface: appropriate specialization, shared task knowledge, and end-to-end optimization can turn coexistence into synergy.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---

### 15. UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture

- **ArXiv ID**: [2609.01598v1](https://arxiv.org/abs/2609.01598v1)
- **作者**: Asees Kaur, Suzanne S. Sindi, Erica M. Rutter
- **发布时间**: 2026-09-02
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.01598v1](https://arxiv.org/pdf/2609.01598v1)
- **相关度评分**: 10/10

#### 英文摘要

Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep learning approaches such as U-Net achieve strong general-purpose segmentation performance but often produce fragmented or discontinuous predictions in fine vascular regions, since they do not explicitly enforce structural connectivity. Region growing algorithms preserve spatial context and topological continuity, but are highly sensitive to seed point initialization and can be computationally expensive. We propose UI-VISA (U-Net Initialized Vascular Image Segmentation Architecture), a hybrid pipeline that combines the complementary strengths of both approaches. UI-VISA uses U-Net's foreground predictions as informed seed points for a CNN-guided region growing algorithm, which then iteratively refines the segmentation by enforcing local connectivity and recovering fine vessel details that U-Net alone tends to miss or over-predict. We evaluate UI-VISA against standalone U-Net and a prior region-growing-based method (VISA) using 5-fold cross-validation on 26 DSA images. UI-VISA achieves the highest mean Dice and clDice scores across folds, and a paired Wilcoxon signed-rank test shows the improvement in clDice is statistically significant ($p=0.023$), consistent with the method's design goal of preserving vascular connectivity, while the improvement in Dice does not reach significance ($p=0.104$).

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid","type":"authentication_erro

---
