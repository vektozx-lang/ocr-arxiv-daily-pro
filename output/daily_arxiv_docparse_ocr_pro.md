# OCR arXiv Daily Pro — 2026-09-30

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-09-29 09:10 - 2026-09-30 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: bc3cf5b7-32db-4

---

## 📄 论文详情

### 1. Exploring In-Context Learning for Handwritten Text Recognition

- **ArXiv ID**: [2609.37195v1](https://arxiv.org/abs/2609.37195v1)
- **作者**: Eric Ayllon, Abel Gandia, Jorge Calvo-Zaragoza
- **发布时间**: 2026-09-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.37195v1](https://arxiv.org/pdf/2609.37195v1)
- **相关度评分**: 10/10

#### 英文摘要

Handwritten Text Recognition (HTR) systems have become an indispensable tool for the digitization of historical documents. Not only do they cut down time and cost, but they also allow democratizing access and processing of their contents by generating their transcripts. However, literature in HTR currently focuses mostly on specialized models that require large amounts of annotated samples to achieve satisfactory performance. We explore the use of In-Context Learning with pre-trained Vision-Language Models (VLMs) to create a transcription pipeline without updating the model's parameters. We then evaluate this pipeline across multiple collections and models, and demonstrate that general-purpose VLMs can be effectively taught how to transcribe handwritten text from images. To assess how our observations may translate to practical applications, we evaluate the performance in a Cross-Domain (CD) scenario, where context examples are drawn from a different collection than the query image. Results in both the controlled In-Domain (ID) scenario and the realistic CD scenario follow the same patterns. First, as context size grows, the error range is expected to narrow towards the average performance. Thus, larger context sizes sacrifice the performance of the oracle-best sampling for lower expected error rates. The results obtained show that, without any parameter updates, this methodology has strong potential to compete with traditional HTR in the presence of domain shift. Moreover, we show and argue that some context samplings work better than others and suggest more effort should be put into finding an ideal sampling method in future work.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 4409cbf2-8fb5-4

---

### 2. PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence

- **ArXiv ID**: [2609.37712v1](https://arxiv.org/abs/2609.37712v1)
- **作者**: GuangJian Team, Kaili Huang, Yongshuo Zhang, Bingtao Fu, Changjiang Jiang...
- **发布时间**: 2026-09-29
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.37712v1](https://arxiv.org/pdf/2609.37712v1)
- **相关度评分**: 10/10

#### 英文摘要

Optical Character Recognition (OCR) is evolving from plain-text transcription toward general visual intelligence, requiring models to recognize, localize, and reason over textual information in complex visual environments. However, existing OCR systems often excel at only some tasks and struggle to balance recognition, parsing, and reasoning across scenarios. In this report, we present PolyOCR, a family of unified OCR foundation models of varying scales. PolyOCR combines a shared instruction-following framework with a large-scale data engine that converts heterogeneous visual resources into quality-verified OCR supervision. We introduce Competence-Guided Policy Optimization, which combines verifier-based Group Relative Policy Optimization with on-policy distillation through sample-wise routing based on teacher reliability and the teacher--student competence gap. We also introduce OCRBench v2.1, our revision of OCRBench v2 with manually verified annotation corrections and task-aligned scoring metrics. Extensive experiments across OCRBench v2.1, CC-OCR, in-house KIE Benchmark, OmniDocBench v1.6 and MDPBench demonstrate that PolyOCR achieves state-of-the-art or highly competitive performance.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 571258da-df0f-4

---

### 3. Which papyrus HTR is good enough? Character-error-rate tolerance of four papyrological tasks on Greek texts

- **ArXiv ID**: [2609.37755v1](https://arxiv.org/abs/2609.37755v1)
- **作者**: Anton Repushko, Elena Chepel
- **发布时间**: 2026-09-29
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.37755v1](https://arxiv.org/pdf/2609.37755v1)
- **相关度评分**: 10/10

#### 英文摘要

Purpose: Most Greek papyri remain unpublished and undigitised; a handwritten text recognition (HTR) pipeline that transcribes them automatically would let scholars discover documents and literary works that have so far gone unread. Recognition systems for Ancient Greek papyri are in statu nascendi, and how accurate they must be for a given papyrological task has not been examined. To answer this and set a benchmark for Greek papyrus HTR, we test a range of character error rates (CER) against four papyrological tasks, using published editions as ground truth. Methods: From 63,846 current editions of Greek texts in papyri.info, we imitate a letters-only "perfect HTR" output by removing the editorial layer, then degrade it with a seeded algorithm to exact CERs of 1 - 50%, with lost lines and four error-shape variants. On these data we train small models (TF-IDF, fastText, a character CNN, ByT5-small) for document type, dating and documentary-versus-literary classification, and apply eight keyword search methods. We compare models trained on clean text with models retrained at a specific CER level, and evaluate across CERs. Results: Tolerance differs by task. With clean-trained models, documentary-versus-literary classification retains 90% of its metric up to 20% CER; document type up to 7.5%; subtypes and search up to 5%; dating only up to 3%. Retraining on text containing character errors largely eliminates the sharp degradation that otherwise sets in above 15% CER. Models generally tolerate concentrated damage in a long document better than small errors spread across a short text. Conclusion: The study provides a CER target for each of the four tasks and shows that models trained on noisy text make current, imperfect text recognition useful for them.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: d688dd1b-e63e-4

---

### 4. ReMem: Rethinking Perception and Memory in Long-Context Recommendation Agents

- **ArXiv ID**: [2609.37311v1](https://arxiv.org/abs/2609.37311v1)
- **作者**: Haohao Qu, Yongcheng Jing, Chun Hin Chan, Shanru Lin, Wenqi Fan...
- **发布时间**: 2026-09-29
- **分类**: cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2609.37311v1](https://arxiv.org/pdf/2609.37311v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent Recommendation Agents (RecAgents) offer a promising alternative by shifting recommendation to an active, user-side paradigm, where generative agents autonomously perceive external platforms, reason over user preferences, and execute decisions. However, existing RecAgents still suffer from two critical limitations: brittle item perception based on noisy and heterogeneous item pages, and inefficient long-context reasoning over extended user histories and multi-step interaction traces. To address these challenges, we propose a novel recommendation agent framework, termed as ReMem, that combines OCR-based multimodal perception with time-evolving dynamic memory. Instead of parsing raw HTML, ReMem observes item pages through screenshots and extracts structured multimodal information via an OCR tool, enabling a more humanoid and platform-agnostic perception mechanism. To support long-horizon preference modeling, ReMem further introduces a chunk-wise sequential memory update strategy, where the agent selectively maintains a fixed-size memory of informative historical interactions while processing arbitrarily long contexts with linear inference complexity and bounded context length. This design allows the agent to preserve evolving user preferences without relying on external memory modules or disrupting the standard autoregressive generation process. To enhance the dynamic memory instruction, we further develop a multi-memory GRPO variant, which propagates the final-answer advantage to all intermediate conversations that contribute to the final response. Extensive experiments on three datasets demonstrate that ReMem consistently outperforms state-of-the-art baselines, achieving an average improvement of 5.16\% across three recommendation agent tasks, namely searching, ranking, and judging.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 078e8886-952b-4

---

### 5. Decompose Radicals, Then Reward: Fine-Grained Inspection for Accurate Chinese Text Rendering

- **ArXiv ID**: [2609.37569v1](https://arxiv.org/abs/2609.37569v1)
- **作者**: Yazhen Xie, Xingsong Ye, Zhineng Chen
- **发布时间**: 2026-09-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.37569v1](https://arxiv.org/pdf/2609.37569v1)
- **相关度评分**: 10/10

#### 英文摘要

Rendering accurate Chinese text remains challenging for text-to-image models. Existing OCR-based reinforcement-learning rewards compare decoded transcripts with target strings. Such rewards overlook the compositional nature of Chinese writing: an ideograph consists of reusable components arranged through explicit spatial relations, yet OCR evaluates it as an atomic character. Consequently, visually different radical-level errors may receive equally coarse feedback, encouraging glyphs that merely resemble the target instead of faithfully reproducing its internal structure. We employ Ideographic Description Sequences (IDS), which comprise spatial operators and character components, and train an expert IDS recognizer to transcribe rendered Chinese text into this representation. Building on this recognizer, we introduce IDSpect, which deterministically decomposes the target text into IDS tokens and aligns crop-level visual IDS predictions with the target sequence. Globally unique token credit makes this comparison robust to the order of detected text regions. Combined with a whole-character semantic reward, IDSpect supplies fine-grained credit with component and spatial-relation without changing the image generator or adding inference-time cost. Experiments with GRPO post-training of Qwen-Image demonstrate that IDSpect achieves leading structural quality and semantic alignment on LongText and GenTextEval.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 854faa87-5510-4

---

### 6. MSTypography: Multi-character Semantic Typography via Balancing Word Legibility and Object Recognizability

- **ArXiv ID**: [2609.37141v1](https://arxiv.org/abs/2609.37141v1)
- **作者**: Xinye Yang, Xinding Zhu, Kai Fang, Xinyi Ren, Mengjian Li...
- **发布时间**: 2026-09-29
- **分类**: cs.CV, cs.GR
- **PDF**: [https://arxiv.org/pdf/2609.37141v1](https://arxiv.org/pdf/2609.37141v1)
- **相关度评分**: 10/10

#### 英文摘要

Semantic typography is a design technique where the visual representation of a word conveys its semantic meaning, while maintaining its legibility. Existing digital typography methods mainly focus on single-character scenarios. They suffer from a lack of legibility constraints and insufficient local deformation when extended to multi-character words, as the intricate structures among multiple characters are hardly preserved during the typography process. In this paper, we propose a global-to-local typography framework for multi-character scenarios. It performs mask-driven silhouette approximation at the global level, while semantic-guided refinement at the local level, with a culling step in between to improve efficiency. To preserve word legibility, we designed structural losses (including explicit collision constraints and implicit Jacobian singular value constraints) and an OCR constraint for character-level readability. To enhance the object recognizability, we leverage semantic guidance with diffusion priors, which drives the character glyph toward the target concept while preserving its structural integrity. To the best of our knowledge, this is the first multi-character semantic typography method that effectively balances word legibility and object recognizability. Evaluations on five representative languages (English, Chinese, Japanese, Korean, Arabic) demonstrate superiority over SOTA methods. Codes will be open-sourced.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fc222811-2313-4

---

### 7. Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation

- **ArXiv ID**: [2609.36598v1](https://arxiv.org/abs/2609.36598v1)
- **作者**: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu...
- **发布时间**: 2026-09-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.36598v1](https://arxiv.org/pdf/2609.36598v1)
- **相关度评分**: 10/10

#### 英文摘要

A video can exhibit convincing motion and photorealism yet fail immediately when visual text collapses. Unlike generic scene content, visual text is unforgiving in video generation: minor stroke corruption, temporal instability, or editing errors instantly break legibility and realism. Existing benchmarks overlook this challenge by treating text as incidental or using static OCR metrics that ignore temporal dynamics. We introduce VidScribe, a unified diagnostic benchmark spanning four generation regimes: writing from language (T2V), transferring text identity from a reference (R2V), sustaining text under dynamics (I2V), and localized text editing (V2V). VidScribe contains 803 human-verified samples across a 12-axis conditionally orthogonal factor space covering Intrinsic Text Properties, Physical Imaging Conditions, and Temporal Behavior. For reliable evaluation, we build a track-grounded, gated suite with 11 shared metrics and 2 task-specific probes under strict measurability conditions. Benchmarking 11 commercial and open-source systems shows that video text capability is non-monolithic, with content recognition decoupled from stroke-level glyph correctness. Performance is highly task-asymmetric: I2V sustains text most reliably, whereas V2V editing is the primary bottleneck. Counter-intuitively, degradation concentrates on a small subset of text-centric structural and temporal factors rather than adverse imaging conditions. Further probes show that visual references improve glyph and typographic fidelity rather than content accuracy, while localized editing fails to isolate target text without corrupting undeclared source text. Beyond evaluation, VidScribe also provides an actionable training signal, where benchmark-aligned preference optimization measurably improves visual text generation. https://huggingface.co/datasets/Vicky0720/VidScribe.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: fd3267d5-9480-4

---

### 8. Learning What to Remember: Long-horizon Counterfactual Memory Optimization

- **ArXiv ID**: [2609.37930v1](https://arxiv.org/abs/2609.37930v1)
- **作者**: Jiaming Tang, Mingyan Liu, Armin Sarabi
- **发布时间**: 2026-09-30
- **分类**: cs.CL, cs.LG
- **PDF**: [https://arxiv.org/pdf/2609.37930v1](https://arxiv.org/pdf/2609.37930v1)
- **相关度评分**: 10/10

#### 英文摘要

Persistent textual memory allows language models to carry information across long interactions, but learning what to remember is fundamentally a credit-assignment problem. A memory rewrite may only become useful many steps later, while much of the observed utility may be inherited from information already stored before the rewrite. We introduce Memory Gain Policy Optimization (MGPO), which isolates the incremental value of each memory rewrite by crediting it for its marginal contribution to current and future downstream utility. This turns delayed memory utility into a direct learning signal for optimizing what information should persist. We study MGPO on document-level information extraction, where structured supervision makes the effects of individual memory updates directly measurable. MGPO improves extraction while reducing average memory length by nearly 80% relative to the initial memory policy before optimization. The learned memory policy also supports reuse and transfer across domains, downstream models without further training. These results show that effective memory learning depends not only on preserving useful information, but on identifying which memory updates create lasting incremental value.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 515073c7-d551-4

---

### 9. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

- **ArXiv ID**: [2609.38177v1](https://arxiv.org/abs/2609.38177v1)
- **作者**: Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim...
- **发布时间**: 2026-09-30
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.38177v1](https://arxiv.org/pdf/2609.38177v1)
- **相关度评分**: 10/10

#### 英文摘要

Reasoning about the 3D world from multi-view images remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While modern MLLMs handle single-image inputs effectively, they struggle to integrate evidence across viewpoints into a coherent 3D understanding. A growing body of work attempts to close this gap by injecting 3D awareness into MLLMs, either by boosting fine-grained pixel-level cross-view correspondence or by fusing features from 3D geometry foundation models, yet a substantial gap to human reasoning persists. In this work, we revisit human spatial reasoning, which suggests that rather than relying on fine-grained geometry cues, humans roughly identify common objects across views, infer the relative geometry between viewpoints, and assemble a coarse 3D layout of the scene. Inspired by this process, we introduce Imagine3D-LLM, an MLLM that learns to assemble a similar compact 3D representation of the scene and conditions its answer on this representation. Concretely, we append a small set of learnable summary tokens after the image tokens, decode them into a compact 3D Gaussian Splatting representation supervised by a photometric reconstruction loss, and train jointly with the standard next-token prediction objective. Notably, although only the summary tokens receive direct reconstruction supervision, this objective also induces stronger cross-frame correspondence within the LLM's underlying image features, suggesting that learning to reconstruct propagates 3D-aware signals throughout the model. As a result, Imagine3D-LLM consistently outperforms prior approaches across multiple spatial reasoning and 3D understanding benchmarks, suggesting that imagining the scene can be more effective than being told its pixel-wise geometry.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 74418154-e979-4

---

### 10. LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation

- **ArXiv ID**: [2609.38146v1](https://arxiv.org/abs/2609.38146v1)
- **作者**: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao...
- **发布时间**: 2026-09-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.38146v1](https://arxiv.org/pdf/2609.38146v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce LIFT, a unified image-to-video generation framework that complements camera control with Layout-In-FuTure control, enabling users to specify what should appear in a future view and where it should appear. This addresses a practical need in controllable video generation: given an initial image, users often care not only about how the camera moves, but also about what the scene should look like at key future moments, especially the final frame. Existing camera controls specify viewpoint trajectories, while text prompts provide only coarse semantic guidance; neither precisely determines the content and spatial layout of future views. This limitation becomes particularly pronounced under large viewpoint changes, where the camera reveals regions that are not visible in the first frame. LIFT therefore uses the last-frame layout as an explicit control signal for the desired future scene. Since learning from such sparse layout guidance is substantially more challenging than conditioning on dense per-frame layouts, we introduce on-policy self-distillation (OPSD) to transfer the control capability of a dense-layout teacher to a last-frame-layout student. We further curate LIFT-Vista, a dataset featuring large viewpoint changes with camera and temporally consistent layout annotations. Experiments show that LIFT improves video quality, future-layout controllability, and camera controllability over other methods.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 8aa81f63-46f6-4

---

### 11. LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning

- **ArXiv ID**: [2609.38137v1](https://arxiv.org/abs/2609.38137v1)
- **作者**: Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen, Xi Ye
- **发布时间**: 2026-09-30
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.38137v1](https://arxiv.org/pdf/2609.38137v1)
- **相关度评分**: 10/10

#### 英文摘要

Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic matching, together with strategic and adaptive reasoning over global and local context. Much of the context is semantically relevant but only a small subset is useful at each step, creating both a challenging search problem and different accuracy--cost tradeoffs across processing strategies. For example, one task requires identifying every person satisfying several conditions using evidence scattered across documents; strategically checking the most selective condition first can narrow the search before verifying the remaining conditions. We evaluate multiple families of frontier language models with four state-of-the-art harnesses. Our benchmarks remain challenging even for strong model--harness combinations: the best reaches 68\% macro-average accuracy across four evaluation suites. More importantly, we find that the same underlying model can exhibit markedly different efficiency under different harnesses. Our results establish efficiency as an important axis for long-context evaluation and provide a testbed for developing harnesses that process context strategically rather than exhaustively.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 50a22976-1a32-4

---

### 12. CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer

- **ArXiv ID**: [2609.38136v1](https://arxiv.org/abs/2609.38136v1)
- **作者**: Teng Zhou, Yunhao Chen
- **发布时间**: 2026-09-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2609.38136v1](https://arxiv.org/pdf/2609.38136v1)
- **相关度评分**: 10/10

#### 英文摘要

Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference appear in the generated output. Although prior data-driven and training-free methods can reduce leakage, they often face a leakage-degradation dilemma: stronger content suppression may weaken style fidelity, while richer style preservation may reintroduce unwanted reference content. We identify this dilemma across the full style-transfer pipeline, including feature separation, feature-space grounding, and diffusion generation. To address these issues, we propose CLeaR, a training-free framework for content-leakage-resistant style transfer. CLeaR first uses Orthogonal Subspace Projection to define content-reduced style targets in each vision foundation model (VFM) feature space. It then performs Ensemble Inversion, which optimizes a shared pixel-space style anchor satisfying style constraints across multiple VFMs. Finally, Energy-Guided Calibration maintains style alignment during diffusion sampling by steering the denoising trajectory toward the ensemble-defined style manifold. We further provide a theoretical analysis showing that the style-anchor estimation error decreases with the number of VFMs. Experiments on StyleBench demonstrate that CLeaR improves style alignment, reduces content leakage, and achieves better LLM-as-Judge evaluation compared with existing methods. The code is available at \href{https://github.com/0606zt/CLeaR}{https://github.com/0606zt/CLeaR}.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0035522d-e24f-4

---

### 13. Effective Dense Retrieval using Only In-Context Examples

- **ArXiv ID**: [2609.38099v1](https://arxiv.org/abs/2609.38099v1)
- **作者**: Nour Jedidi, Abdul Basit Ali, Hang Li, Jimmy Lin
- **发布时间**: 2026-09-30
- **分类**: cs.IR, cs.CL
- **PDF**: [https://arxiv.org/pdf/2609.38099v1](https://arxiv.org/pdf/2609.38099v1)
- **相关度评分**: 10/10

#### 英文摘要

Turning decoder-only large language models (LLMs) into strong dense retrievers typically requires some form of retriever training. In this paper, we ask whether LLMs can instead be prompted to produce effective representations for dense retrieval given only a few in-context examples. To answer this, we introduce RICE (Representations from In-Context Examples), a simple "training-free" approach that extracts high-quality dense representations from LLMs. To do so, RICE conditions the LLM on examples that provide a shared context for query and document encoding. Our results demonstrate that RICE embeddings can substantially improve the accuracy of prompt-based LLM embeddings, establishing it as a simple method to build LLM-based dense retrievers that do not require training. We release our code at https://github.com/nourj98/RICE.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 5110dfda-4bb9-4

---

### 14. Gender bias across LLMs is common and highly heterogenous

- **ArXiv ID**: [2609.38036v1](https://arxiv.org/abs/2609.38036v1)
- **作者**: Edoardo Bolzoni, Valerio Capraro
- **发布时间**: 2026-09-30
- **分类**: cs.CL, cs.AI, cs.CY
- **PDF**: [https://arxiv.org/pdf/2609.38036v1](https://arxiv.org/pdf/2609.38036v1)
- **相关度评分**: 10/10

#### 英文摘要

Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and moral judgment of abuse or torture against a woman or a man to prevent a catastrophic outcome (Study 2). In Study 1, two of ten models attributed masculine-stereotyped phrases to female writers more often than the reverse, while three models showed the opposite pattern. In Study 2, several models converged on a male-disadvantaging asymmetry that was directionally consistent with a documented human tendency to protect female targets from harm, though the specific conditions under which this asymmetry emerged varied by model; three other models, by contrast, showed no variation across conditions. These results indicate that gender-related biases are common in LLMs. Their direction and magnitude, however, are highly heterogeneous, to the point that some models behave in diametrically opposite ways to others. Bias auditing should therefore be treated as an ongoing, multi-vendor process, rather than a one-time assessment.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 88a221b3-b04a-4

---

### 15. Generated Query Expansion Still Helps Strong Sparse Retrieval: A Controlled Study with SPLADE-v3

- **ArXiv ID**: [2609.37911v1](https://arxiv.org/abs/2609.37911v1)
- **作者**: Ryan C. Barron, Cade W. Trotter, Maksim E. Eren, Kim Ø. Rasmussen, Liz D. Miller...
- **发布时间**: 2026-09-30
- **分类**: cs.IR, cs.AI
- **PDF**: [https://arxiv.org/pdf/2609.37911v1](https://arxiv.org/pdf/2609.37911v1)
- **相关度评分**: 10/10

#### 英文摘要

Scientific queries are often brief, while relevant papers use specialized vocabulary. Generated query expansion can bridge this mismatch, but earlier work suggests that its value shrinks as the underlying retriever becomes stronger. We test the four generated formats of term lists, a pseudo-document, multiple pseudo-references, and corpus-steered text all together with SPLADE-v3 on NFCorpus, TREC-COVID, and SciDocs. Every condition searches the same frozen document index and follows the same query-side integration rule and 256-dimension budget, isolating the effect of the added content. All twelve method-collection comparisons improve aggregate nDCG@10, with best relative gains of 4.81%, 8.92%, and 9.47%. Eleven remain significant after Holm correction. The gain persists in 103 of 114 interpolation settings, including every setting that assigns at least 30% of the mixture weight to the original query. Shuffled-text and non-contextual lexical-bag controls also remain above baseline in all 24 aggregate comparisons, showing that the added vocabulary carries most of the benefit. A corpus-induced typed concept graph, by contrast, produces no consistent gain, and its relation, depth, validation, random, and gating controls do not rescue it. Generated vocabulary can therefore complement a strong learned sparse retriever, provided that the original query remains strongly represented.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0482e782-4e58-4

---
