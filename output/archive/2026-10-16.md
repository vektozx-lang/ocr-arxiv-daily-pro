# OCR arXiv Daily Pro — 2026-10-16

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-10-15 09:10 - 2026-10-16 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 7f8bdaac-4b4f-4

---

## 📄 论文详情

### 1. Making every stage of medical device document assessment with large language models deterministic

- **ArXiv ID**: [2610.21300v1](https://arxiv.org/abs/2610.21300v1)
- **作者**: Ryosuke Suzuki
- **发布时间**: 2026-10-15
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2610.21300v1](https://arxiv.org/pdf/2610.21300v1)
- **相关度评分**: 10/10

#### 英文摘要

To show that a medical device complies with regulation, experts judge whether documents and records meet each requirement and record the judgment for others to verify. For each assessment item that experts define, large language models could prepare a preliminary assessment: a label such as Satisfied or Not satisfied, a reason and quoted evidence. We sent fourteen commercial deployments of such models (seven models from three providers, through six routes) the same request repeatedly, with the deterministic sampling settings each accepted; every deployment returned differing assessments for at least one request, and in twelve the label changed. Reducing reasoning where the interface allows it did not reduce the variation, and prompts of retrieved passages removed it only for the smallest models. The same open-weight model was reproducible or not depending only on how it was served. A pipeline we built to be deterministic at every stage -- text extraction and optical character recognition (OCR), chunking, embedding, indexing, retrieval and inference -- returned byte-identical output at each stage across reruns, interruptions, edits, machines of one graphics processing unit (GPU) model and days, for blood glucose meter and infusion pump documents. OCR, embedding and approximate retrieval varied when their own serving was not made invariant, and outputs changed with the GPU model and with the inference engine's scheduling settings, which therefore belong in the recorded configuration. End-to-end determinism is achievable and gives a testable basis for audit and change control.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 193d360f-81cc-4

---

### 2. P2TPO: Structure-Aligned Page-to-Token Credit Assignment for Full-Page Document Parsing

- **ArXiv ID**: [2610.21979v1](https://arxiv.org/abs/2610.21979v1)
- **作者**: Yong Zu, Ninghua Yang, Zezhong Tan, Xinhong Ma, Ziqiang Dong...
- **发布时间**: 2026-10-15
- **分类**: cs.LG, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.21979v1](https://arxiv.org/pdf/2610.21979v1)
- **相关度评分**: 10/10

#### 英文摘要

End-to-end full-page document parsing must preserve the content and structure of heterogeneous elements, yet otherwise accurate outputs can contain local errors and omissions. A single page-level advantage does not explicitly identify which elements differ in quality across sampled outputs or where their errors occur. We introduce Page-to-Token Policy Optimization (P2TPO), a structure-aligned credit-assignment framework that operates on full-page policy trajectories. Reference-element alignment first associates block-level quality contrasts with generated spans. Unified Anchor Pricing (UAP) incorporates matched and missing element outcomes and provides feedback relative to a fixed quality ceiling when sampled outputs receive identical but imperfect scores for a reference element. Within matched blocks, Span Credit Redistribution (SCR) redistributes existing block credit according to aligned correct and erroneous spans, using boundary proxies for within-block omissions while preserving the total block-derived advantage across its tokens. Under a fixed-weight additive page utility, we show that element-indexed contrasts retain local quality differences that page-level aggregation can cancel out. In the main experimental comparison, P2TPO outperforms all evaluated policy optimization baselines in seed-averaged scores on each of the six document parsing benchmarks. Additional experiments demonstrate gains across model scales and initializations.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 15c1f2eb-08a0-4

---

### 3. ZoomCap: Evidence-Routed Visual Zooming for Recoverable Visual Information Transfer

- **ArXiv ID**: [2610.21320v1](https://arxiv.org/abs/2610.21320v1)
- **作者**: Hao Shi, Jiafeng Wang, Yuzhuo Fu, Tao Zhang, Jian Bai...
- **发布时间**: 2026-10-15
- **分类**: cs.CV, cs.CL, cs.MM
- **PDF**: [https://arxiv.org/pdf/2610.21320v1](https://arxiv.org/pdf/2610.21320v1)
- **相关度评分**: 10/10

#### 英文摘要

Detailed captions transfer visual information into vision-language model supervision, but quality is easily conflated with length: long single-pass outputs still miss small objects, text, and spatial relations or promote uncertain observations into confident claims. We formulate fine-grained captioning as recoverable visual information transfer, in which a teacher acquires missing evidence under a finite observation budget and converts it into reusable supervision. ZoomCap uses a draft caption to route conditional knowledge retrieval, OCR-sensitive reading, coverage-gap recovery, and adaptive visual zooming, allocating deeper crops only to the most complex eligible region, deriving spatial relations from grounded geometry, and fusing non-duplicate evidence. We also introduce FactCycle, which scores caption-derived atomic claims on two blind anchors--source image (truthfulness) and reconstruction (realizability)--separating fabrication from generator loss claim by claim; human and multi-judge comparisons complement this fact-level view. Against Qwen3.5-397B-A17B captions, ZoomCap achieves an 81.9% human tie-adjusted preference score with a teacher over 10x smaller, and FactCycle counts 52.4 transferred claims per image vs. 31.5 for ScaleCap. The evidence also transfers: in continual pre-training, ZoomCap-450K improves the 11-benchmark average by 1.31-2.38 points over the strongest competing corpus and Ling-Tiny-VL-v3 gains 1.4 points on a production document/OCR monitor suite (1.5 on perception) at 60B tokens; in medical pre-training, 2.64M ZoomCap-captioned images improve five VQA benchmarks by 3.04 points (vs. 1.76 for same-image Gemini-3.1-Pro captions).

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 10f80d97-a3cf-4

---

### 4. Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG

- **ArXiv ID**: [2610.21318v1](https://arxiv.org/abs/2610.21318v1)
- **作者**: Eunchan Jo, Seounghyun Jang, Sangwoo Mo
- **发布时间**: 2026-10-15
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.21318v1](https://arxiv.org/pdf/2610.21318v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal document retrieval-augmented generation (RAG) has focused largely on retrieval, yet its answers depend on how well a vision-language model reads the retrieved pages. We find that evidence in retrieved pages remains underused even when the correct pages are retrieved. On SciEGQA oracle pages, five prior methods give the generator 0.7K to 2.7K visual tokens per query on average under a common image processor, yet raising the page-only budget from 1K to 32K improves accuracy by 15.22 points. At a fixed 16K budget, adding ground-truth crops improves accuracy by 3.75 points over page-only input. We study what the generator needs from retrieved pages through two requirements: Loud, making full use of visual token capacity, and Clear, refining the page so that its evidence becomes prominent. For Loud, increasing either the visual token budget or visual fidelity, the image resolution those tokens preserve, improves accuracy with the other held fixed, and full-page scaling outperforms repetition and tiling at matched budgets. For Clear, suppressing surrounding content improves accuracy without enlarging selected regions, and adding OCR of these regions to page images outperforms either input alone. We implement both as Loud and Clear (LoC), which combines higher-resolution pages with OCR from query-relevant regions without ground-truth annotations or additional training. LoC outperforms eight prior methods on SciEGQA, ViDoRe-v3, and MMLongBench-Doc, improving over the strongest, ColQwen3, by 8.88, 3.09, and 4.22 points with the same retriever and generator. It also outperforms its page-only variant under the same visual token budget. These results locate a bottleneck beyond retrieval: how the retrieved pages are given to the generator.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 27fd7773-162f-4

---

### 5. DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding

- **ArXiv ID**: [2610.21327v1](https://arxiv.org/abs/2610.21327v1)
- **作者**: Zhuowen Liang, Xiaotian Lin, Yuyu Luo, Haixun Wang, Nan Tang
- **发布时间**: 2026-10-15
- **分类**: cs.AI, cs.CL, cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.21327v1](https://arxiv.org/pdf/2610.21327v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggle with cross-modal reasoning in a single pass. Existing document agents further introduce multi-step interaction, but some still rely on predefined workflows or coarse-grained actions, limiting the flexibility and granularity of document reasoning. We introduce DocPilot, an agentic document framework that supports expressive orchestration and makes complex document solving learnable by small language models (SLMs). DocPilot orchestrates evidence seeking through page-level navigation and fine-grained evidence localization, and integrates local visual inspection, code-based numerical reasoning, and cross-modal reasoning for multimodal understanding. To transfer these capabilities to small models, we propose curriculum-based agentic training that progresses from single-ability learning to adaptive orchestration through supervision from data-grounded reasoning traces and executable interaction trajectories. Across MMLongBench-Doc, DocBench, FinRAGBench-V, and MADQA, DocPilot achieves strong gains with frontier VLM backbones, while DocPilot-4B delivers competitive performance against substantially larger models, demonstrating strong effectiveness and generalization across diverse long-document reasoning settings. The code is available at https://github.com/HKUSTDial/DocPilot.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 652741a8-76d2-4

---

### 6. Training Reasoning Models to Generate Diverse Scientific Ideas

- **ArXiv ID**: [2610.22324v1](https://arxiv.org/abs/2610.22324v1)
- **作者**: Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty...
- **发布时间**: 2026-10-16
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.22324v1](https://arxiv.org/pdf/2610.22324v1)
- **相关度评分**: 10/10

#### 英文摘要

One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being grounded in the input documents. To optimize for this, we propose training with a set-level reinforcement learning objective. In our setup, in a single generation, the model writes K structured idea cards grounded in the source papers, and the set is scored jointly, where each idea's quality is weighted by its distance from the ideas written before it. This teaches the model to steer each new idea away from its predecessors. We show that our trained 8B model achieves higher creative utility (a measure combining quality and diversity) than Claude Opus 4.8 and GPT-6 Astra on our contamination-free benchmark. In a pilot human study with four experts, our sets are judged as promising as Claude Opus 4.8's and contain marginally more unique ideas. When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: a0ed58d9-4b89-4

---

### 7. MJev-Spatial: System One Spatial Intelligence via Native Attention Matching

- **ArXiv ID**: [2610.22276v1](https://arxiv.org/abs/2610.22276v1)
- **作者**: Luozheng Qin, Yuhan Zhu, Changhai Zhou, Qian Qiao, Jun Gao...
- **发布时间**: 2026-10-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.22276v1](https://arxiv.org/pdf/2610.22276v1)
- **相关度评分**: 10/10

#### 英文摘要

Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive decoding and answer parsing even though the output space is compact: one of a few options, a scalar, or a 2D point. In light of this, we introduce MJev-Spatial, a System 1 multimodal decision model that tackles all three types of spatial understanding tasks within a unified classification framework. Specifically, MJev-Spatial treats each candidate as a class and scores it using the backbone's pretrained query and key projections, without adding parameters. The candidates are the given options for choice tasks, or value bins and image regions refined through coarse-to-fine classification for numerical and point prediction, respectively. At inference, each classification decision takes a single forward pass and generates no answer tokens. To train on heterogeneous spatial data efficiently, we supervise all coarse-to-fine stages jointly with teacher forcing in one forward pass, and combine this with length-aware global batching and cross-GPU load balancing, raising training throughput by 30.8% over the original batching strategy. Built on Qwen3.5-4B and trained on 12.3M question-answer pairs converted from existing spatial datasets, MJev-Spatial achieves the highest overall score (65.64%) among eight tested models, ranks first on seven of twelve benchmarks, and outperforms its unmodified autoregressive base model on all twelve, while running 2.5 times faster than the fastest autoregressive baseline and 5.6 times faster than the base model.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 209e5af0-7a03-4

---

### 8. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries

- **ArXiv ID**: [2610.22273v1](https://arxiv.org/abs/2610.22273v1)
- **作者**: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar...
- **发布时间**: 2026-10-16
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.22273v1](https://arxiv.org/pdf/2610.22273v1)
- **相关度评分**: 10/10

#### 英文摘要

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: c4ad978d-cef8-4

---

### 9. Beyond Downstream QA: Rethinking How We Evaluate Agent Memory

- **ArXiv ID**: [2610.22209v1](https://arxiv.org/abs/2610.22209v1)
- **作者**: Sebastian-Antonio Toma, Jean de Kernier, Mike Ply, Oliviu Matei
- **发布时间**: 2026-10-16
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2610.22209v1](https://arxiv.org/pdf/2610.22209v1)
- **相关度评分**: 10/10

#### 英文摘要

Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives where incorrect responses blame correct memory for retrieval failures. We introduce FEB-30, a benchmark of 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion: documents are generated from known fact trajectories, yielding deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts (documents, emails, conversations), enabling direct inspection of the memory store after each ingestion step. Applying FEB-30 to a representative memory system, we demonstrate that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition reveals that the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time, a failure entirely invisible to extrinsic evaluation, and that failure modes differ systematically by category and difficulty. We release the benchmark, document generation pipeline, and scoring framework to support reproducible evaluation of agent memory systems.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 0fc75d0b-1e36-4

---

### 10. Documenting Trofinetide Treatment Phenotypes in Rett Syndrome with a Dual-LLM Consensus Pipeline

- **ArXiv ID**: [2610.22062v1](https://arxiv.org/abs/2610.22062v1)
- **作者**: Daniel Palacios, Guantong Qi, Mikael Guzman Karlsson, Shawntel K. David, Mohammed Sameeruddin...
- **发布时间**: 2026-10-15
- **分类**: q-bio.QM, cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.22062v1](https://arxiv.org/pdf/2610.22062v1)
- **相关度评分**: 10/10

#### 英文摘要

Objective: Trofinetide, approved in 2023 as the first Rett syndrome treatment, lacks scalable real-world monitoring because chart review is labor-intensive. We developed a dual large language model (LLM) consensus pipeline to extract 18 treatment-response phenotypes, comprising 4 adverse effects, 13 Rett clinical features, and medication refusal, from clinical notes. Materials and Methods: We analyzed 26,763 notes from 108 patients with confirmed sustained trofinetide exposure at Texas Children's Hospital. The pipeline filters notes by keyword, classifies each through two LLMs requiring consensus, and aggregates a patient-by-timepoint matrix. Architecture and prompt were selected on a diarrhea development set, then frozen and applied to the other 17 phenotypes with the phenotype definition substituted, as an out-of-sample test. The reported prompt comparison scores 183 expert-labeled cells. Results: A prompt requiring diarrhea to be active and severe performed best (84.2 $\pm$ 0.0% accuracy; F1 = 0.674), 47 percentage points above regular-expression matching ($p < 0.0001$). Expert reviewers judged six of the pipeline's calls per phenotype, three positive and three negative, and agreed with 90.2% (92/102). The 13 Rett clinical features are manifestations of the disorder itself rather than adverse effects of trofinetide. Gross and fine motor impairment, language/communication, and stereotypy were documented present in 92-100% of patients at every visit. Discussion: In-context LLM extraction captured multi-domain treatment responses. The outcome is documented presence at each visit, not a direction-of-change judgment. Conclusion: Coupling in-context LLM reasoning with a consensus architecture offers a scalable alternative to keyword and regular-expression extraction for real-world evidence, adapting to new phenotypes and medications through configuration alone.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: ec13796a-ba77-4

---

### 11. Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual Appropriateness

- **ArXiv ID**: [2610.22249v1](https://arxiv.org/abs/2610.22249v1)
- **作者**: Yihang Peng, Yi Jing, Dewen Liu, Weihan Meng, Ying Liu
- **发布时间**: 2026-10-16
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2610.22249v1](https://arxiv.org/pdf/2610.22249v1)
- **相关度评分**: 10/10

#### 英文摘要

Recurring expressions in model-written text are often treated as signatures of machine authorship, yet most of them serve legitimate functions. Whether such an expression is a tic depends on whether the model knows when it is called for. This judgment of appropriateness, central to communicative competence, remains largely unexamined for language models. We study it through the Mandarin corrective construction bushi X, ershi Y ("not X, but Y"). Drawing on Gricean pragmatics and corrective negation, we introduce a decision tree that classifies uses as substantive, optional, or defective by testing whether the context makes X a live alternative and whether rejecting X is informative. Five commercial models use the construction 2.5 to 9.2 times as densely as a human reference. Of 307 annotated uses, only 1.30% are defective while 52.8% are optional, that is, correct but unneeded, so models fall short in appropriateness far more often than in correctness. Several reward models favor the construction even over quality-matched variants, an LLM judge favors it even where the context does not license it, and both supervised fine-tuning and preference optimization tend to raise its frequency in open-weight models. We hope this work encourages the development of models attentive to the appropriateness of their expressions.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 6e55cb9b-bf63-4

---

### 12. RAG-RST: Retrieved Exemplars as In-Context Discourse Schema for RST Parsing

- **ArXiv ID**: [2610.22150v1](https://arxiv.org/abs/2610.22150v1)
- **作者**: Mohammadreza Sediqin, Shlomo Engelson Argamon
- **发布时间**: 2026-10-16
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2610.22150v1](https://arxiv.org/pdf/2610.22150v1)
- **相关度评分**: 10/10

#### 英文摘要

In Rhetorical Structure Theory (RST), each edge of a discourse tree carries a nuclearity label, marking which span holds the central content, and a relation drawn from a closed inventory of functional categories. Neither label is a surface property: the same two clauses can be Elaboration or Background depending on rhetorical intent, and the boundary between them is fixed by annotation convention rather than by lexical cues. Predicting these labels therefore requires a formal discourse schema, and exposure to discourse-rich pretraining text does not supply it: given only a target EDU pair, a strong LLM recovers nuclearity at 0.794 F1 and relation at 0.738 F1. We propose RAG-RST, a retrieval-augmented framework that supplies this schema as in-context demonstration rather than through parameter updates, raising nuclearity to 0.846 F1 and relation to 0.788 F1 with no training. Two configurations are compared: a precomputed strategy that labels all EDU pairs before parsing, and a dynamic strategy that retrieves at each reduce step, so that the exemplars reaching the generator depend on the reductions the parser has already committed to. Both outperform existing RST parsers across span, nuclearity, relation, and full tree metrics, with the dynamic variant consistently strongest. Two properties of the retrieved schema emerge: its utility is bounded in number, saturating and then declining beyond fifty exemplars, and it depends on structural position. Both indicate that a formal linguistic schema can be supplied to a foundation model as a demonstration rather than trained into its parameters.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 64c32bc5-b0c5-4

---

### 13. Gen4P: Video Generators are 4D Perceivers

- **ArXiv ID**: [2610.22371v1](https://arxiv.org/abs/2610.22371v1)
- **作者**: Yitong Xia, Zeren Jiang, Chuanxia Zheng
- **发布时间**: 2026-10-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.22371v1](https://arxiv.org/pdf/2610.22371v1)
- **相关度评分**: 10/10

#### 英文摘要

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See https://gen4p.github.io for more visual results.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 955fdb0b-3110-4

---

### 14. Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation

- **ArXiv ID**: [2610.22370v1](https://arxiv.org/abs/2610.22370v1)
- **作者**: SeungJu Cha, Ye-Chan Kim, HyunGee Kim, Sungho Koh, Dong-Jin Kim
- **发布时间**: 2026-10-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.22370v1](https://arxiv.org/pdf/2610.22370v1)
- **相关度评分**: 10/10

#### 英文摘要

Token merging has emerged as an effective training-free strategy for accelerating diffusion models by reducing redundant token computation while minimizing generation degradation. A key challenge is determining which tokens can be safely merged and which should be preserved for subsequent computation. Existing method addresses this by preserving prompt-aligned foreground regions, thereby protecting semantically relevant structures. However, this text-relevance criterion overlooks background objects, local details that are not explicitly mentioned in the prompt, leading to degraded structural coherence. In this work, we propose Dynamics-aware Token Merging (DaTMe), a training-free framework that grounds token merging in the underlying diffusion dynamics. Our key insight is that token importance should reflect whether a token remains unresolved during denoising and whether it carries structural information. To this end, DaTMe constructs a dynamics- aware importance map from the Tweedie denoised estimate. The map combines a temporal signal, measuring inter-step changes in the predicted clean image, with a structural signal, capturing local high-frequency content such as boundaries and fine details. Using this map, DaTMe adaptively assigns tokens into merging roles under a given compression ratio: important tokens are preserved as anchors, while tokens that are both temporally stabilized and structurally homogeneous are selected as safe merge candidates. Experiments on PixArt-a and FLUX demonstrate that DaTMe maintains visual fidelity across the entire image, highlighting diffusion dynamics as an effective token-level merging decision in efficient generation. Our code is available at https://github.com/SeungJuCha/DaTMe.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 864fe7f3-a642-4

---

### 15. SoftCache: Adaptive Step Size Caching for Diffusion Transformers

- **ArXiv ID**: [2610.22369v1](https://arxiv.org/abs/2610.22369v1)
- **作者**: Shimon Malnick, Nadav Orenstein, Ohad Fried, Shai Avidan
- **发布时间**: 2026-10-16
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2610.22369v1](https://arxiv.org/pdf/2610.22369v1)
- **相关度评分**: 10/10

#### 英文摘要

Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. Training-free caching accelerates them by reusing activations from recent evaluations instead of recomputing them. Dynamic caching methods decide when to refresh by accumulating a cheap probe of the network input into a staleness signal and spending a fresh evaluation once it crosses a threshold. They perform hard caching: the signal is a binary switch between refresh and reuse, and every step, fresh or cached, advances by the prescribed step size. We observe that the signal carries much more than this switch. How far it sits below the threshold, its headroom, predicts the error induced by reuse. We propose SoftCache, which performs soft caching: instead of a binary switch, the headroom sets how far each cached step goes. Where the headroom is large, the sampler jumps past several scheduled nodes, and as a refresh nears, its steps shrink back toward the original step. These adaptive jumps may land between the scheduled nodes, taking the sampler off its fixed grid. SoftCache requires no training and adds no per-backbone settings: on FLUX for images and on HunyuanVideo and Wan2.1 for video, at speedups from $3.5\times$ to $6.9\times$, it is ahead of every baseline on all four fidelity metrics.

#### 深度分析（中文）

LLM 调用失败: litellm.BadRequestError: DeepseekException - {"error":{"message":"Authentication Fails, Your api key: ****e78f is invalid (request_id: 1004fad2-51ec-4

---
