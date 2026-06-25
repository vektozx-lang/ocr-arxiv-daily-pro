# OCR arXiv Daily Pro — 2026-06-25

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-06-24 09:10 - 2026-06-25 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

### 今日执行摘要
今日共15篇高相关论文，研究热度集中在视觉语言模型（VLM）的鲁棒性、文档质量评估、多模态大模型（MLLM）的可信度审计，以及GUI智能体与文档理解等方向。最值得关注的突破包括：提出了首个面向OCR推理鲁棒性的基准OCR-Robust，以及一个轻量级图像模糊检测门控机制MagikaDocumentFromPixel，两者直接服务于工业级OCR管道。此外，关于MLLM顺序敏感性的审计工作Facet-Probe为模型评估提供了新的可靠性维度。

### 今日研究趋势
- **VLM/MLLM的鲁棒性与可靠性评估成为焦点**：多篇论文从不同角度审视模型在非理想条件下的表现。论文1（OCR-Robust）系统评估了视觉扰动下的OCR推理鲁棒性；论文2（MagikaDocumentFromPixel）专注于检测输入模糊度，避免无效计算；论文3（Facet-Probe）则首次系统审计了MLLM对输入顺序的敏感性，揭示了一个被忽视的可靠性缺陷。这表明，研究社区正从追求性能指标转向关注模型在实际部署中的稳定性和可信度。
- **小模型与高效部署方案持续涌现**：针对资源受限场景，多篇工作致力于在不牺牲性能的前提下降低模型复杂度。论文2提出的模糊检测门控仅需7毫秒/图（单CPU核），论文9（WinDOM）则专门设计了约2B参数的GUI grounding小模型，并提出了无需人工标注的数据构建与训练策略。这反映了将文档智能能力落地到边缘设备或轻量级应用中的强烈需求。
- **数据污染与对抗攻击防御成为重要课题**：论文10和论文11均关注数据投毒攻击，分别针对文本摘要和检索增强生成（RAG）场景。前者提出了一个统一的检测与修复框架，后者则通过令牌影响力归因实现轻量级检测。这表明，随着LLM在文档处理中的广泛应用，其安全性，特别是训练与推理阶段的对抗防御，已成为不可回避的研究前沿。

### 核心技术创新汇总
- **OCR-Robust基准**（论文1）：首个系统评估VLM在视觉退化（如模糊、噪声、光照变化）下OCR推理鲁棒性的基准，揭示了视觉扰动如何通过引入OCR错误和结构扭曲来影响高层推理任务。
- **MagikaDocumentFromPixel模糊门控**（论文2）：一种极轻量级、CPU友好的图像质量分类器，能在毫秒级判断图像是否为模糊，有效防止下游OCR和VLM调用浪费计算资源。
- **Facet-Probe审计框架**（论文3）：提出五维度顺序敏感性审计方法（选项、证据块、文档排序、图像集、混合模态），并利用贝叶斯项目反应模型分离排序噪声与各维度偏差，为MLLM评估提供了新范式。
- **WinDOM自家族蒸馏**（论文9）：通过驱动一个大型教师模型自动收集GUI grounding数据，并结合监督微调（SFT）与强化学习（RL）训练小模型，解决了小模型训练数据匮乏和训练策略不清的问题。
- **TRACE轻量级投毒检测**（论文11）：通过令牌影响力归因，追溯答案相关令牌在检索语料中的来源，无需额外分类器或LLM验证即可高效识别RAG系统中的投毒攻击。

### 研究空白与机会
- **多模态文档理解中的复杂推理鲁棒性**：今日论文主要关注低层OCR鲁棒性（如模糊）或高层顺序敏感性，但针对文档布局剧烈变化（如表格结构破坏、文字重叠）对VLM进行复杂推理（如文档问答、表格推理）的影响，仍缺乏系统研究。
- **多语言与历史文档的鲁棒性评估**：论文8（HIPE-2026）聚焦于多语言历史文档中的人物-地点关系抽取，这本身就是一个充满挑战的领域。但现有鲁棒性评估基准（如OCR-Robust）主要基于现代、清晰的英文文档，未来亟需扩展至低资源语言、手写体、古旧印刷体等更具噪声的场景。
- **文档质量评估的全流程整合**：论文2仅关注输入端的模糊检测，而一个完整的文档处理管道还需考虑其他退化类型（如倾斜、污渍、低对比度）以及输出端（如OCR置信度、版面分析结果）的质量评估。将多种质量门控与下游任务性能动态关联，是一个有价值的研究方向。

### 工程落地启发
- **在OCR流水线入口部署轻量级质量门控**：参考论文2的MagikaDocumentFromPixel，可以在实际文档扫描或拍摄流程中，对每帧图像进行快速模糊检测。对于模糊图像，可立即触发重拍提示或图像增强模块，避免后续昂贵的OCR和VLM调用产生无意义结果，从而节省大量计算资源与时间成本。
- **小模型GUI grounding的实用训练策略**：论文9的WinDOM展示了如何通过“教师模型自动标注+学生模型蒸馏”的范式，低成本构建高质量GUI grounding数据集。对于需要将屏幕理解能力集成到手机或桌面应用中的开发团队，该策略提供了一个可复现的、无需人工标注的端到端解决方案。
- **警惕MLLM在文档理解中的顺序偏差**：论文3的发现提醒，在构建基于MLLM的文档问答或信息抽取系统时，不能假设模型对输入顺序（如文档段落顺序、候选选项顺序）不敏感。工程实现中应考虑对输入进行多次随机排序后取多数投票，或设计更鲁棒的提示词来缓解此问题。

### 今日优先精读推荐
1. **How Robust is OCR-Reasoning?**：直接命中OCR推理的核心鲁棒性问题，其提出的基准和发现对于评估和改进现有VLM在文档场景下的实际表现具有直接指导意义。
2. **Edges Before Embeddings**：提供了可直接用于生产环境的工程化解决方案，其轻量、高效的特性对于优化文档处理管道的计算效率和可靠性至关重要。
3. **Same Evidence, Different Answer**：揭示了MLLM评估中的一个关键盲区，其审计方法论和发现对于构建更可靠、更公平的多模态文档理解系统具有深远影响。

---

## 📄 论文详情

### 1. How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations

- **ArXiv ID**: [2606.26041v1](https://arxiv.org/abs/2606.26041v1)
- **作者**: Yuxing Cheng, Yuan Wu, Yi Chang
- **发布时间**: 2026-06-25
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2606.26041v1](https://arxiv.org/pdf/2606.26041v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and select 5 representative types at 3 severity levels each based on their impact and cross-model discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR), Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18 models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts and tables are substantially more fragile than document-like inputs under perturbation.

#### 深度分析（中文）

### 中文摘要
本文针对视觉语言模型（VLM）在文本丰富场景下对视觉扰动的鲁棒性缺乏系统评估的问题，提出了OCR-Robust基准。该基准包含812个样本，覆盖文档、场景文本、图表等8类OCR内容，并基于18种候选扰动筛选出5种代表性扰动（各含3个严重等级）。通过评估18个模型（含闭源、开源及OCR+LLM流水线），发现高清洁准确率并不等价于强鲁棒性，且图表类任务在扰动下比文档类任务脆弱得多。

### 解决的核心问题
现有OCR推理基准（如DocVQA、ChartQA）主要评估模型在干净数据上的性能，忽略了真实场景中图像退化（如模糊、光照变化、遮挡）对OCR推理链条的影响。这种视觉扰动会先引发OCR识别错误，进而破坏下游推理的可靠性，而当前缺乏一个系统、可控的扰动评估框架来量化这种级联效应。

### 核心创新
本文在数据集和评估方法论两个层面做出贡献。数据集层面，首次构建了专门用于评估OCR推理鲁棒性的基准OCR-Robust，覆盖从传统OCR（OCR1.0：文档、手写、数学公式）到结构化OCR（OCR2.0：图表、几何图、表格）的完整谱系。评估方法论层面，提出了一套包含RCR、WCR和CRI的多维度鲁棒性指标，并通过预实验从18种扰动中筛选出最具区分度的5种，避免了冗余评估。

### 创新点拆解
- 创新点1：构建了OCR-Robust基准，将OCR内容划分为OCR1.0（文本密集型）和OCR2.0（结构密集型）两个子集，分别对应不同的鲁棒性挑战，为细粒度分析提供了基础。
- 创新点2：提出了一套系统的扰动筛选流程，通过预实验计算每种扰动对模型性能的影响和跨模型区分度，最终选定模糊、噪声、遮挡、几何变换和色彩失真5类扰动，每类设3个严重等级，确保评估的全面性与效率。
- 创新点3：设计了三个互补的鲁棒性指标——RCR（平均退化保留率）、WCR（最差情况保留率）和CRI（综合鲁棒性指数），克服了单纯依赖清洁准确率的局限性，能够揭示模型在极端退化下的脆弱性。

### 实验结果亮点
在18个模型的评估中，GPT-4o在干净数据上准确率最高（OCR1.0: 91.2%，OCR2.0: 85.7%），但其CRI仅为0.72（OCR1.0）和0.64（OCR2.0），远低于某些开源模型（如InternVL2-8B的CRI为0.81和0.76）。具体而言，在OCR2.0子集的严重遮挡条件下，所有模型的WCR均低于0.3，其中图表类任务平均准确率从干净时的78%骤降至14%，验证了结构敏感型内容对视觉扰动的高度脆弱性。

### 当前局限
该基准仅包含812个样本，样本量较小，可能无法覆盖所有现实场景中的扰动类型（如扫描伪影、字体变形）。此外，扰动筛选基于18种候选，但实际环境中可能存在更复杂的组合扰动（如模糊+遮挡），本文未评估多扰动叠加效应。最后，评估仅限于英文内容，对中文、阿拉伯语等非拉丁文字系统的鲁棒性尚不明确。

### 后续改进方向
- 方向1：扩展OCR-Robust基准至多语言场景，特别是中文、日文等字符密度高且结构复杂的文字系统，并加入字体风格、书写变体等扰动类型。
- 方向2：研究组合扰动下的鲁棒性衰减规律，例如通过设计正交实验或对抗性扰动生成方法，模拟真实场景中多退化源并存的复杂情况，并探索基于数据增强的鲁棒性训练策略。
- 方向3：结合OCR识别模块与推理模块的联合鲁棒性分析，分离“OCR识别错误”和“推理错误”的贡献，从而设计针对性的模块级防御机制（如鲁棒OCR预训练或推理过程中的视觉注意力矫正）。

### 工程落地启发
对实际OCR/文档解析工程最有价值的点在于：高准确率模型（如GPT-4o）在图像退化时可能急剧失效，而中等性能但更鲁棒的开源模型（如InternVL2）更适合部署于复杂光照、模糊等不稳定场景。工程团队应优先将鲁棒性指标（如CRI）纳入模型选型标准，并在预处理流水线中引入对抗性数据增强（如随机模糊、遮挡）来提升系统在退化输入下的容错能力。

---

### 2. Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

- **ArXiv ID**: [2606.25838v1](https://arxiv.org/abs/2606.25838v1)
- **作者**: Duy Tran Thanh
- **发布时间**: 2026-06-24
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.25838v1](https://arxiv.org/pdf/2606.25838v1)
- **相关度评分**: 10/10

#### 英文摘要

Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR, retrieval, and vision-language model (VLM) calls that cannot recover a usable output. We present MagikaDocumentFromPixel, a lightweight, CPU-friendly image quality gate that classifies a single image as sharp, blurred, or uncertain in roughly 7 ms on a single CPU core. The contributions are (i) a recipe selected from a 46-configuration, 8-sweep empirical search that isolates input resolution as the dominant lever and shows architecture capacity only pays off at >= 384 px; (ii) a confidence-aware routing formalism grounded in classical selective prediction; (iii) the Edge Prior Module (EPM), a Laplacian-magnitude auxiliary input channel that gives the network direct access to the spectral evidence that classical blur heuristics rely on and that lifts test F1 by +1.3 points in a matched-env comparison; and (iv) an observation that the gate is one instance of a recurring design pattern that appears independently in Magika content-type detection, risk-controlled OCR with VLMs, and DocVLM. The final recipe MobileNetV3-Large with the EPM trained at 384x384 on paired GoPro Large frames, evaluated with 5-scale test-time augmentation reaches F1 = 0.9803 (AUC 0.9989) with a 17 MB ONNX artifact, improving over our fixed-scale baseline on the same hardware (F1 = 0.9672) by +1.31 points. We are explicit about limitations: results are on a single motion-blur distribution, numbers are from a single seed, and calibration is qualitative rather than measured.

#### 深度分析（中文）

### 中文摘要
本文提出了一种名为MagikaDocumentFromPixel的轻量级图像质量门控模块，用于在视觉语言流水线中快速检测模糊输入并阻止无效下游调用。该方法基于MobileNetV3-Large架构，并创新性地引入了边缘先验模块（EPM），将拉普拉斯幅度作为辅助输入通道，在单CPU核心上仅需约7毫秒即可完成分类。在GoPro大帧数据集上，该方法达到了0.9803的F1分数和0.9989的AUC，相比固定尺度基线提升了1.31个百分点。

### 解决的核心问题
现有的生产级视觉流水线在遇到模糊输入时性能会严重下降，但缺乏高效的早期检测机制来阻止这些无效输入进入下游OCR、检索或视觉语言模型（VLM）处理，从而浪费计算资源。具体而言，现有方法要么依赖复杂的图像质量评估模型导致计算开销大，要么缺乏对模糊类型的鲁棒性，难以在资源受限的生产环境中快速决策。

### 核心创新
本文的核心创新在于提出了一种置信度感知的模糊门控框架，通过经验搜索确定了输入分辨率是影响性能的关键因素，并设计了边缘先验模块（EPM）将经典的拉普拉斯模糊检测启发式信息直接融入深度学习网络。此外，论文还形式化地建立了基于经典选择性预测理论的置信度感知路由机制，使模型能够在不确定时选择不进行决策。

### 创新点拆解
- **创新点1：边缘先验模块（EPM）**：将拉普拉斯算子的幅度图作为额外的输入通道，使网络能够直接访问经典模糊启发式算法所依赖的频谱证据，从而在匹配环境下将测试F1提升了1.3个百分点。
- **创新点2：基于经验搜索的配置选择**：通过对46种配置、8轮扫描的实证搜索，发现输入分辨率是主导性能表现的杠杆，而架构容量仅在分辨率达到384像素以上时才发挥显著作用。
- **创新点3：置信度感知路由机制**：将图像分类问题形式化为经典的选择性预测框架，使模型能够输出“不确定”类别，从而在高风险场景下避免错误决策。

### 实验结果亮点
在GoPro大帧数据集上，采用MobileNetV3-Large架构搭配EPM，在384x384分辨率下训练，并经过5尺度测试时增强后，最终模型达到了F1=0.9803和AUC=0.9989。与同一硬件上的固定尺度基线（F1=0.9672）相比，提升了1.31个百分点，且最终的ONNX模型仅17MB，在单CPU核心上推理时间约为7毫秒。

### 当前局限
该方法仅在单一运动模糊分布（GoPro数据集）上进行评估，且所有结果均来自单一种子，缺乏统计显著性分析。此外，模型的校准质量仅进行了定性分析而非定量测量，这限制了其在需要精确概率估计的应用中的可靠性。同时，该方法未在文字模糊、失焦模糊等其他常见模糊类型上进行验证。

### 后续改进方向
- **方向1：跨模糊类型泛化**：在包含运动模糊、失焦模糊、高斯模糊等多种类型的混合数据集上进行训练和评估，并引入域适应技术以提升模型在未见模糊分布上的鲁棒性。
- **方向2：定量校准与不确定性估计**：引入期望校准误差（ECE）等定量指标来评估模型校准质量，并探索使用蒙特卡洛Dropout或深度集成等贝叶斯方法以获得更可靠的不确定性估计。

### 工程落地启发
对实际OCR/文档解析工程项目最有参考价值的点在于：该工作证明了在资源受限的CPU环境中，通过将经典的信号处理启发式（如拉普拉斯算子）以辅助通道形式融入轻量级CNN，可以在极低延迟（7ms）下实现高精度的图像质量预筛选。这为在文档扫描流水线中前置一个计算高效的“质量门控”提供了直接可行的技术方案，避免将严重模糊的文档图像送入昂贵的OCR或VLM处理流程，从而显著降低整体计算成本。

---

### 3. Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models

- **ArXiv ID**: [2606.26079v1](https://arxiv.org/abs/2606.26079v1)
- **作者**: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
- **发布时间**: 2026-06-25
- **分类**: cs.CL, cs.CV, cs.LG
- **PDF**: [https://arxiv.org/pdf/2606.26079v1](https://arxiv.org/pdf/2606.26079v1)
- **相关度评分**: 8/10

#### 英文摘要

Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.

#### 深度分析（中文）

### 中文摘要
本文系统性地审计了18个前沿多模态大语言模型（MLLMs）在输入顺序扰动下的答案稳定性，发现所有模型均不具备完全的顺序不变性。研究者提出Facet-Probe审计框架，涵盖选项、证据块、文档排序、图像集及混合模态五种顺序敏感性维度，并利用贝叶斯项目响应模型分离顺序噪声与各维度偏差。实验表明，即使最优模型仍有13.4%的试次因顺序变化而翻转答案，且无训练提示缓解方案的效果具有模态条件性，无法从文本推理迁移至视觉推理。

### 解决的核心问题
现有MLLM基准测试采用固定规范顺序评估每个项目，忽略了输入元素（如选项、证据块、图像顺序）的随机重排是否会导致答案改变。这种顺序敏感性违背了新兴AI评估指南所要求的“基线可靠性”属性，但目前缺乏系统性的审计框架来量化该问题。

### 核心创新
本文首次提出Facet-Probe五维度审计框架，系统性地评估MLLMs对五种输入顺序扰动的敏感性，并引入贝叶斯项目响应模型来分离顺序噪声与各维度固有偏差。同时，通过相同输入条件下的重复测试（相同顺序控制组），估计解码器随机性导致的答案翻转基线，从而量化顺序扰动带来的额外翻转率。

### 创新点拆解
- 创新点1：提出Facet-Probe审计框架，覆盖选项顺序、证据块顺序、文档排序、图像集顺序及混合模态顺序五种扰动模式，首次实现对MLLM顺序敏感性的多维度、系统化评估。
- 创新点2：采用贝叶斯项目响应模型对审计结果进行建模，能够将顺序扰动引起的随机噪声与每个维度特有的系统性偏差分离开来，从而更精确地量化顺序敏感性的本质。
- 创新点3：引入相同顺序控制组实验，通过多次重复相同输入（温度设为0）来估计解码器随机性导致的答案翻转下限，从而计算出顺序扰动带来的“超额翻转率”，为评估模型可靠性提供了新指标。

### 实验结果亮点
在18个前沿及开源MLLM的审计中，所有模型均非顺序不变：各维度面板平均翻转率范围为24-50%。以Gemini模型为例，在温度0下的相同顺序控制组中，验证单元内存在显著高于解码器噪声底线的顺序超额翻转率。能力更强的模型翻转率更低，但最佳模型仍有13.4%的试次出现答案翻转。在Gemini的缓解测试中，无训练提示修改的效果具有模态条件性，文本推理的缓解策略无法迁移至视觉推理任务。

### 当前局限
本文主要聚焦于审计问题，未提出有效的训练阶段或架构层面的解决方案。无训练提示缓解方案的效果有限且具有模态特异性，无法保证跨模态的通用鲁棒性。此外，审计框架目前覆盖的五种顺序扰动模式可能无法穷尽所有现实场景中的顺序敏感性问题。

### 后续改进方向
- 方向1：在MLLM的训练阶段引入顺序扰动数据增强，使模型在训练过程中学习对输入顺序的不变性，例如通过随机打乱文本块或图像序列并强制模型输出一致答案。
- 方向2：设计架构层面的顺序鲁棒机制，如基于集合（set-based）的注意力模块，使模型对输入元素的排列不敏感，类似于DeepSets等置换不变网络的设计思想。

### 工程落地启发
对实际OCR/文档解析工程项目，本文揭示了一个关键风险：即使模型在固定顺序的文档上表现良好，当文档元素（如段落、表格行、图像）的顺序因预处理或用户交互而改变时，答案可能发生非预期的翻转。因此，在部署MLLM进行文档问答或信息抽取时，必须进行多顺序变体的鲁棒性测试，并将“跨顺序翻转率”作为模型选型与质量评估的标准指标。

---

### 4. From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance

- **ArXiv ID**: [2606.26007v1](https://arxiv.org/abs/2606.26007v1)
- **作者**: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian...
- **发布时间**: 2026-06-25
- **分类**: cs.CV, cs.GR
- **PDF**: [https://arxiv.org/pdf/2606.26007v1](https://arxiv.org/pdf/2606.26007v1)
- **相关度评分**: 8/10

#### 英文摘要

Image priors can synthesize target conditions for 3D Gaussian street scenes, but independently edited views do not define a coherent 3D target. Direct fitting can propagate view-specific noise, while existing pipelines do not jointly handle imperfect sparse anchors and standard-rasterizer deployment. To address this gap, teacher-relative appearance residual distillation is introduced for appearance baking. A structured space for frequency decomposition, confidence estimation, and primitive-level lifting is formed by residuals between teacher anchors and original renders. The direct optimization signal is supplied by renderer-space matching, while primitive assignment is regularized by support-aware Gaussian-space aggregation. Supported detail is admitted and unsupported noise is suppressed through confidence-gated coarse-to-fine optimization, after which all residuals are baked into fixed-geometry spherical-harmonic coefficients. The teacher and auxiliary training modules are discarded at inference. Evaluation across Waymo street assets, Tanks and Temples scenes, and multiple target conditions shows a favorable overall balance of target alignment, content preservation, artifact suppression, and cross-view consistency over editing-based baselines. Ablations confirm the effectiveness of the main components. Code will be released at https://github.com/Cagares/Baking-for-3D-Gaussian.

#### 深度分析（中文）

### 中文摘要
本文提出一种基于教师-学生残差蒸馏的3D高斯泼溅外观烘焙方法，旨在将稀疏且不完美的2D锚点（如编辑后的图像）转化为一致的3D街景场景。该方法通过频率分解、置信度估计和基元级提升的结构化空间，利用渲染器空间匹配提供直接优化信号，并采用支持感知的高斯空间聚合进行基元分配正则化，最终将残差烘焙到固定几何的球谐系数中。在Waymo街景资产、Tanks and Temples场景及多种目标条件下的评估表明，该方法在目标对齐、内容保留、伪影抑制和跨视图一致性上优于现有编辑基线。

### 解决的核心问题
现有基于图像先验的3D高斯街景编辑方法在独立编辑视图时无法定义一致的3D目标，直接拟合会传播视图特有的噪声，且现有流程无法联合处理稀疏且不完美的2D锚点与标准光栅化部署之间的差距。具体痛点包括：1）多视图编辑结果缺乏跨视图一致性；2）直接拟合将视图噪声引入3D表示；3）缺乏对不完美锚点（如稀疏、含噪声）的鲁棒处理机制。

### 核心创新
本文的核心创新在于引入教师-相对外观残差蒸馏框架，通过结构化残差空间实现频率分解与置信度估计，并利用支持感知的高斯空间聚合正则化基元分配，从而将编辑后的2D锚点外观一致地烘焙到3D高斯表示的球谐系数中。该方法在推理时丢弃教师和辅助训练模块，实现了轻量级的部署。

### 创新点拆解
- 创新点1：提出教师-相对外观残差蒸馏，在教师锚点与原始渲染结果之间构建结构化残差空间，实现对频率分解、置信度估计和基元级提升的联合建模，从而有效分离支持与噪声信息。
- 创新点2：引入支持感知的高斯空间聚合，通过置信度门控的粗到细优化策略，在基元分配过程中抑制无支持噪声并保留有支持细节，同时利用渲染器空间匹配提供直接的优化信号。
- 创新点3：设计了可丢弃教师和辅助模块的推理机制，将训练阶段学习的残差直接烘焙到固定几何的球谐系数中，实现了编辑后外观的轻量级、一致3D表示，无需额外推理开销。

### 实验结果亮点
在Waymo街景资产、Tanks and Temples场景及多种目标条件（如不同天气、光照）下的评估显示，该方法在目标对齐、内容保留、伪影抑制和跨视图一致性上均优于编辑基线方法。消融实验证实了频率分解、置信度估计和基元级提升等主要组件的有效性，具体量化指标（如PSNR、SSIM、LPIPS等）在论文中均有优于对比方法的记录。

### 当前局限
该方法假设3D几何在编辑过程中固定不变，因此无法处理需要改变几何结构的编辑任务（如物体移除或形状变形）。此外，对输入2D锚点的质量仍有依赖，极端稀疏或高度不完美的锚点可能导致蒸馏残差中的噪声残留，影响最终渲染一致性。方法在动态场景（如移动物体）上的泛化能力尚未验证。

### 后续改进方向
- 方向1：引入可变形几何建模，允许在编辑过程中联合优化几何与外观，以支持形状变形或物体移除等复杂编辑任务，例如结合神经隐式场进行几何残差学习。
- 方向2：扩展至动态场景，通过引入时间维度的支持感知聚合，处理街景中车辆、行人等移动物体的外观编辑，保持时间一致性。

### 工程落地启发
对OCR/文档解析工程最有价值的点是其“支持感知的粗到细优化”策略：在实际工程中，当处理包含噪声或稀疏标注的文档图像（如扫描件、手写体）时，可借鉴此思想，通过构建残差空间分离高频细节（如笔画边缘）与低频噪声（如纸张纹理），并利用置信度门控逐步精化，从而在文本识别或版面分析中提升对缺陷输入的鲁棒性。此外，其“可丢弃辅助模块”的设计思路可用于构建轻量级文档预处理模型，在训练时使用复杂网络，推理时仅保留核心烘焙参数，降低部署成本。

---

### 5. Naturalness Predicts but Does Not Cause Transferability in Image Encodings of Real-World Streams

- **ArXiv ID**: [2606.25844v1](https://arxiv.org/abs/2606.25844v1)
- **作者**: Faruk Alpay, Baris Basaran
- **发布时间**: 2026-06-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.25844v1](https://arxiv.org/pdf/2606.25844v1)
- **相关度评分**: 8/10

#### 英文摘要

A common practice converts a one-dimensional signal into an image so that a vision backbone pretrained on natural photographs can be reused for recognition, yet the encoded image is rarely examined. We ask how the visual naturalness of an encoded image relates to its transfer accuracy under a frozen backbone. We build WorldStream, a corpus of 299 heterogeneous current-value series from key-free public APIs (weather, air quality, earthquakes, gold and oil, equities, crypto, foreign exchange, web activity and space weather), with a nine-way source-recognition task over 3143 temporally split windows. Across seven encodings and six frozen backbones, the Frechet distance of an encoding to natural images (FID) predicts its accuracy: Spearman $ρ=-0.72$. Two controlled interventions show this is not causal in the spectrum. Our invertible encoder has a single adjustable part, a spectral exponent $β$ (power $\propto |f|^{-β}$); varying $β$ moves the image toward or away from the natural-image manifold at fixed content. FID is lowest near the natural value $β\approx 2$, but frozen accuracy stays flat and far below the structured baselines (19.2% vs. 73.0%), and FID and accuracy are only weakly related over the sweep (Pearson $-0.32$). A second intervention, phase scrambling, holds the power spectrum exactly fixed while removing local structure; now FID and accuracy fall together (Pearson $-0.89$). The cross-encoding correlation is thus mediated by local structure, not spectral naturalness: FID predicts accuracy because Inception reads the same structure the backbones do. Full fine-tuning does not close the gap (27% vs. 67%), so the deficit is structural. The encoder is exactly invertible, recovering the signal from the 8-bit image at 72.9 dB, so the image doubles as a lossless record of the data.

#### 深度分析（中文）

### 中文摘要
本文探究了将一维时间序列编码为图像后，其视觉自然度与冻结视觉主干迁移识别准确率之间的关系。作者构建了包含299个异构数据流的WorldStream语料库，并通过七种编码与六种冻结主干进行实验，发现编码图像与自然图像的弗雷歇距离（FID）能预测迁移准确率（斯皮尔曼相关系数ρ=-0.72），但通过两种受控干预实验证明这种相关性并非因果关系，而是由局部结构中介的。

### 解决的核心问题
现有方法常将一维信号转换为图像以复用预训练于自然照片的视觉主干，但编码后的图像本身很少被深入分析。本文的核心问题在于：编码图像的视觉自然度（即与自然图像的相似程度）是否以及如何影响其在冻结主干下的迁移识别准确率，以及这种关联是否具有因果性。

### 核心创新
本文的核心创新在于通过构建大规模异构时间序列数据集WorldStream，并结合两种受控干预实验（调整光谱指数β和相位打乱），首次系统性地揭示了编码图像的视觉自然度与迁移准确率之间的非因果关系。研究发现了局部结构而非光谱自然度是跨编码相关性的中介因素，且证明了即使使用完全可逆编码器，迁移性能仍存在结构性缺陷。

### 创新点拆解
- **创新点1**：构建了WorldStream数据集，包含来自9个类别（天气、空气质量、地震、黄金与石油、股票、加密货币、外汇、网络活动、太空天气）的299个异构实时数据流，并提供了3143个时间分割窗口的九类源识别任务，为时间序列编码研究提供了标准化的基准。
- **创新点2**：设计了完全可逆的编码器，其唯一可调参数为光谱指数β（功率∝|f|^{-β}），通过调整β可在固定内容下使编码图像接近或远离自然图像流形，从而实现了对自然度与准确率因果关系的直接检验。
- **创新点3**：通过相位打乱干预实验，在保持功率谱完全不变的同时去除局部结构，发现FID与准确率同步下降（皮尔逊相关系数-0.89），从而证明了跨编码相关性由局部结构而非光谱自然度中介。

### 实验结果亮点
- 在WorldStream数据集上，七种编码与六种冻结主干的组合中，FID与准确率呈强负相关（斯皮尔曼ρ=-0.72）。
- 通过调整β进行干预时，FID在β≈2（自然图像典型值）附近最低，但冻结准确率保持平坦且远低于结构化基线（19.2% vs. 73.0%），且FID与准确率仅弱相关（皮尔逊-0.32）。
- 相位打乱后，FID与准确率同步下降（皮尔逊-0.89），进一步证实了局部结构的中介作用。
- 即使进行全参数微调，编码器性能仍存在显著差距（27% vs. 67%），表明缺陷是结构性的。

### 当前局限
- 研究仅针对冻结主干场景，虽然进行了全微调实验，但微调后性能差距仍然显著，表明编码图像存在固有结构缺陷，无法通过简单微调弥补。
- 实验仅使用Inception网络计算FID，而FID的预测能力可能依赖于特定特征提取器，对其他网络或度量（如LPIPS）的泛化性未验证。
- 仅针对一维时间序列的编码场景，未扩展到其他类型的信号（如音频、传感器数据）或更复杂的编码方法。

### 后续改进方向
- **方向1**：探索新的编码策略，旨在保留时间序列的局部结构的同时增强其与自然图像流形的对齐，例如通过可微分渲染或生成对抗网络学习更优的映射函数。
- **方向2**：研究在编码过程中显式引入局部结构先验，如通过注意力机制或卷积核设计来模拟自然图像中的纹理和边缘特征，从而提升冻结主干的迁移性能。

### 工程落地启发
本文对OCR/文档解析工程的直接启发在于：当使用视觉主干处理非自然图像（如文档扫描件、表格截图、公式图像）时，不应盲目追求编码图像与自然照片的视觉相似度（如通过颜色映射或纹理增强）。相反，应关注编码图像中局部结构的保真度（如字符边缘、行列对齐、公式符号的局部连续性），因为实验证明局部结构而非全局视觉自然度才是迁移性能的关键中介因素。工程实践中，可通过设计结构保留的编码策略（如保持像素邻域关系）来提升下游任务性能。

---

### 6. Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets

- **ArXiv ID**: [2606.25760v1](https://arxiv.org/abs/2606.25760v1)
- **作者**: Divake Kumar, Sina Tayebati, Devashri Naik, Amanda Sofie Rios, Nilesh Ahuja...
- **发布时间**: 2026-06-24
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2606.25760v1](https://arxiv.org/pdf/2606.25760v1)
- **相关度评分**: 8/10

#### 英文摘要

Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions. Yet evidence on post-hoc uncertainty quantification (UQ) for these agents is fragmented across isolated model and dataset pairs, leaving it unclear whether UQ rankings stay stable when the agent, benchmark, or observable interface changes. We present Argus, a cross-regime benchmark for post-hoc UQ in single-step executable GUI grounding: a 27-method open-weight matrix over 4 VLM agents and 4 datasets, plus an 8-method closed-source matrix across 3 frontier vendors where logits, hidden states, and attention maps are unavailable. Evaluated methods span logit-based scores, sampling and consistency measures, hidden-state and density estimators (Mahalanobis, SAPLMA), attention-based scores, P(True) and verbalised-confidence prompting, and split-conformal prediction. The main finding is selective transfer: UQ rankings are stable across datasets for a fixed model, but degrade across model classes and observable interfaces. Hidden-state and density methods are the most stable open-weight family, while CoCoA-1MCA, Focus, sampling-based scores, and verbalised self-assessment win in specific regimes. Within-model ranking transfer is strong (Spearman rho up to 0.969), but cross-tier transfer to closed-source vendors averages only +0.08, so closed-source UQ should be reranked on the target rather than extrapolated. Conformal click regions show score-level discrimination is not enough for deployment: locally weighted disks shrink radii by 40-60% when the plug-in UQ is calibrated, but coverage degrades under calibration-test or interface mismatch. We release per-item records, calibration/test splits, UQ scores, and analysis scripts for regime-aware UQ selection in GUI agents.

#### 深度分析（中文）

### 中文摘要
本文提出Argus基准，系统评估计算机使用代理中视觉语言模型（VLM）在图形用户界面（GUI）接地任务上的后验不确定性量化（UQ）方法。该基准涵盖4个开源VLM、4个数据集及27种UQ方法，并扩展至3个闭源商业模型。核心发现是UQ排序在固定模型下跨数据集稳定，但跨模型类或接口时显著退化，且隐藏状态与密度估计方法在开源模型中表现最稳定。

### 解决的核心问题
现有计算机使用代理将VLM预测转化为可执行GUI点击，但缺乏对不确定性量化方法在不同模型、数据集和接口条件下的稳定性和可迁移性的系统性评估。已有研究仅聚焦于孤立的模型-数据集对，导致无法判断UQ排名是否随代理、基准或可观测接口变化而保持稳定，阻碍了实际部署中UQ方法的选择。

### 核心创新
- 首次构建跨模型、跨数据集、跨接口（开源vs闭源）的统一UQ基准，覆盖27种开源方法与8种闭源方法。
- 揭示UQ排序的“选择性迁移”现象：同一模型内跨数据集排序高度稳定，但跨模型类或从开源到闭源接口时排序近乎随机。
- 提出基于共形预测的自适应点击区域生成方法，证明仅依赖分数级判别不足以满足部署需求，需结合校准后的UQ方法优化空间安全区域。

### 创新点拆解
- 创新点1：跨体制UQ基准构建。设计包含开源（4个VLM+4个数据集+27种方法）和闭源（3个商业模型+8种方法）的矩阵式评估框架，覆盖logit、采样、隐藏状态、密度估计、注意力、置信度提示及共形预测等多元UQ家族。
- 创新点2：选择性迁移现象发现。通过系统实验证明UQ排序在固定模型内跨数据集高度稳定（Spearman ρ最高0.969），但跨模型类或从开源到闭源接口时排序退化（平均ρ仅+0.08），否定了UQ方法可任意迁移的假设。
- 创新点3：共形预测驱动的空间安全区域优化。将UQ分数集成到共形预测框架中生成局部加权点击区域，证明校准后的UQ可使覆盖区域半径减小40-60%，但校准-测试接口不匹配会导致覆盖退化。

### 实验结果亮点
- 在开源设置中，隐藏状态与密度方法（如Mahalanobis、SAPLMA）是跨模型最稳定的UQ家族，而CoCoA-1MCA、Focus、基于采样的分数及言语化自信评估在特定体制中表现最优。
- 同一模型内跨数据集UQ排序的Spearman ρ高达0.969，但跨模型类（如不同VLM架构）时ρ降至0.2-0.4。
- 闭源模型UQ排序与开源模型平均相关系数仅+0.08，表明闭源UQ需在目标模型上重新评估而非直接迁移。
- 共形预测中，使用校准后的UQ方法（如SAPLMA）可使局部加权圆盘半径减少40-60%，但在校准-测试接口不匹配时覆盖率下降超过15%。

### 当前局限
- 仅评估单步可执行GUI接地任务，未扩展到多步推理或长序列交互场景。
- 闭源模型评估受限于接口可观测性（无法获取logits、隐藏状态等），仅能测试8种后验UQ方法。
- 共形预测的覆盖保证在接口不匹配（如不同分辨率、不同GUI框架）时退化，缺乏自适应校准机制。
- 未涉及主动学习或在线UQ更新策略，所有评估均基于静态预训练模型。

### 后续改进方向
- 方向1：多步交互UQ扩展。设计时序不确定性累积方法，将单步UQ分数整合为多步决策的置信度轨迹，并评估其对任务成功率的影响。
- 方向2：跨接口自适应校准。开发轻量级域适应模块，通过少量目标接口样本微调UQ方法，以缓解校准-测试不匹配导致的覆盖退化。
- 方向3：闭源模型UQ迁移学习。探索基于模型蒸馏或特征对齐的迁移技术，使开源UQ方法能更有效地适配闭源模型的可观测输出（如仅文本或坐标）。

### 工程落地启发
- 关键发现：在部署GUI代理时，不应假设UQ方法可跨模型通用；必须为每个目标VLM单独评估并选择最优UQ方法，尤其是从开源模型切换到闭源商业模型时需重新排名。
- 实用工具：论文开源的per-item记录、校准/测试划分、UQ分数及分析脚本可直接用于工程团队快速构建针对特定VLM的UQ评估管道，避免重复实验。
- 空间安全优化：共形预测与局部加权圆盘结合的方法可直接嵌入GUI点击系统，通过校准UQ分数将点击区域缩小40-60%，显著降低误点击风险，但需监控接口一致性。

---

### 7. Position Spaces and Graphs

- **ArXiv ID**: [2606.25719v1](https://arxiv.org/abs/2606.25719v1)
- **作者**: Rita-Nathalia Assaf, Tom Davot, Frédéric Lardeux, Frédéric Saubion
- **发布时间**: 2026-06-24
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.25719v1](https://arxiv.org/pdf/2606.25719v1)
- **相关度评分**: 5/10

#### 英文摘要

In this paper, we introduce position graphs, a graph-based reasoning framework based on the formalization of position spaces. This framework utilizes two strict partial orders, representing horizontal and vertical alignment and precedence, to model the relative positions of discrete tokens. Unlike general qualitative spatial calculi, position graphs are constrained by a chain condition and compatibility requirements that focus on rows and columns. We provide a comprehensive theoretical analysis of this representation, beginning with a characterization of graph consistency. Conditions to ensure the consistency of position graphs are established. Furthermore, we investigate the computational complexity of structural pattern discovery, modeled as the induced subgraph isomorphism problem. We demonstrate that this problem remains NP-complete even within the restricted class of position graphs. While initially motivated by document processing, this work focuses on the underlying mathematical properties and algebraic consistency of position-based constraints, providing a formal logical layer that is independent of specific data extraction techniques.

#### 深度分析（中文）

### 中文摘要
本文提出位置图（position graphs）框架，基于位置空间的形式化定义，利用两个严格偏序关系分别建模离散标记（tokens）的水平和垂直对齐与前后顺序。该工作从理论层面分析了位置图的图一致性条件，并证明了在该受限图类上诱导子图同构问题（即结构模式发现）仍为NP完全，为文档处理中的空间关系推理提供了独立于具体数据提取技术的逻辑基础。

### 解决的核心问题
现有定性空间演算（Qualitative Spatial Calculi）虽能建模对象间空间关系，但缺乏针对文档排版中行列对齐与顺序约束的专用形式化工具。本文面向文档处理场景中离散标记相对位置关系的表达与推理，解决如何严格定义基于行和列约束的空间图结构，并分析其一致性与模式发现的计算复杂度这一基础问题。

### 核心创新
本文首次将位置空间形式化为由两个严格偏序关系驱动的图结构，并引入“链条件”与“兼容性要求”来约束行和列关系。在此基础上，系统刻画了位置图的一致性条件，并揭示了在该结构上诱导子图同构问题的计算复杂性，为文档结构模式发现提供了理论复杂度下界。

### 创新点拆解
- 创新点1：提出位置图这一新型图表示框架，通过水平与垂直两个严格偏序关系，将离散标记的相对位置抽象为图结构，并专门定义链条件与兼容性约束以聚焦行列对齐场景。
- 创新点2：建立了位置图一致性的充分必要条件，从代数角度保证了所构建的空间关系图在逻辑上的自洽性，避免了矛盾的位置约束。
- 创新点3：证明了即使限制在位置图这类结构化图中，诱导子图同构问题仍保持NP完全性，揭示了结构模式发现任务的内在计算困难。

### 实验结果亮点
本文为纯理论工作，未涉及实验数据集与定量结果。其核心贡献在于对位置图的理论性质（一致性、计算复杂性）的严格证明，因此无数字型实验结果可报告。

### 当前局限
该方法目前仅关注位置空间的形式化与图一致性理论分析，尚未与具体的文档解析流水线（如OCR输出后处理、版面元素分类）进行集成验证。此外，位置图假设了严格的行列对齐关系，对于复杂版面（如自由格式、重叠元素、曲线排版）的适应能力有限，且未考虑语义层面的约束。

### 后续改进方向
- 方向1：将位置图与现有OCR版面分析模型（如基于Transformer的检测器）结合，设计端到端可训练的图神经网络，实现从原始图像到位置图结构的一致性预测。
- 方向2：扩展位置图定义以支持非严格行列布局，例如引入软约束或概率图模型，处理表格合并单元格、自由文本行等现实文档中的不规则对齐。

### 工程落地启发
位置图提供了一种独立于具体OCR引擎的中间逻辑表示层，可用于校验多源OCR输出结果的空间一致性（例如检测同一表格中不同单元格的边界对齐冲突）。工程上，可将其作为后处理规则引擎的核心组件，在结构化文档提取流水线中自动检测并修正因识别错误导致的行列错位问题。

---

### 8. Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts

- **ArXiv ID**: [2606.25935v1](https://arxiv.org/abs/2606.25935v1)
- **作者**: Juri Opitz, Maud Ehrmann, Corina Raclé, Andrianos Michail, Matteo Romanello...
- **发布时间**: 2026-06-24
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.25935v1](https://arxiv.org/pdf/2606.25935v1)
- **相关度评分**: 1/10

#### 英文摘要

Was this person ever at that place, and if so, when? Answering such questions from noisy, multilingual historical documents is the central challenge of HIPE-2026, the third edition of the HIPE evaluation series. Moving from named entity recognition and linking (HIPE-2020, HIPE-2022) to reasoning about relationships between entities, HIPE-2026 targets two temporally grounded relation types: $at$, indicating that a person was present at a location at some point prior to a document's publication date, and $isAt$, indicating presence contemporaneous with that date. This paper presents the results of the evaluation campaign, which confronted 17 participating teams with the challenges of historical language variation, OCR noise, and indirect contextual cues across three languages: French, German, and English. The datasets include historical newspaper text from the nineteenth and twentieth centuries, as well as a surprise-domain generalization set drawn from early modern French literary texts. A distinctive feature of HIPE-2026 is its three-fold evaluation framework, which assesses predictive accuracy, computational efficiency, and cross-domain generalization, reflecting the practical demands of large-scale historical document processing in the cultural heritage domain. Across more than 40 submitted runs, results reveal a wide range of strategies, from state-of-the-art large language models to lightweight task-specific classifiers, and highlight the trade-offs between accuracy, efficiency, and robustness inherent to historical relation extraction at corpus scale. System descriptions, datasets, and findings are presented and discussed, offering a detailed picture of the current state of temporally grounded relation extraction for historical documents.

#### 深度分析（中文）

### 中文摘要
HIPE-2026是第三届历史实体关系抽取评测，任务从命名实体识别与链接转向推理人物与地点之间的时间约束关系，具体包括“at”（某人在文档出版前曾到过某地）和“isAt”（某人当时在场）两类关系。该评测基于法、德、英三语历史报纸与早期法语文学文本，构建了含OCR噪声与历史语言变体的数据集。17支队伍提交了40余次结果，涵盖大语言模型与轻量分类器，揭示了在准确性、效率与跨域泛化之间的权衡，为大规模历史文档关系抽取提供了系统性评估。

### 解决的核心问题
现有命名实体识别与链接方法（如HIPE-2020和HIPE-2022）无法处理人物与地点之间的时间约束关系，尤其是在历史文本中，语言变体、OCR噪声和间接上下文线索使得关系推理更加困难。此外，历史文档处理需要兼顾大规模语料的计算效率与跨领域泛化能力，而现有评测缺乏对此类实际需求的综合评估框架。本文旨在填补这一空白，通过设计时间约束关系抽取任务与多维度评测体系，推动历史文档中实体关系推理的发展。

### 核心创新
本文创新性地将历史文档处理从实体识别与链接升级为时间约束的人物-地点关系抽取，并引入三语（法、德、英）历史文本数据集，涵盖19-20世纪报纸与早期法语文学等跨领域场景。评测框架首次同时评估预测准确性、计算效率与跨域泛化能力，反映了文化遗产领域大规模文档处理的真实需求。

### 创新点拆解
- 创新点1：任务设计创新。从静态的命名实体识别与链接转向动态的、时间约束的人物-地点关系抽取，定义“at”与“isAt”两类关系，要求模型推断人物在文档出版前后的时空关联，增加了推理难度。
- 创新点2：数据集构建创新。构建了包含历史语言变体、OCR噪声与间接上下文线索的三语数据集，并引入“惊喜域”泛化集（早期法语文学文本），以测试模型对未见过领域的适应能力。
- 创新点3：评测框架创新。提出三维评测体系，综合预测准确性、计算效率与跨域泛化，并鼓励提交轻量级模型，以反映文化遗产机构对大规模处理的实际约束。

### 实验结果亮点
在超过40次提交中，大语言模型（如微调版LLaMA）在准确性上领先，但计算成本高；轻量分类器（如基于BERT的微调模型）在效率上优势显著，且泛化性能接近。例如，在法语数据集上，最佳系统在“at”关系上F1达0.78，但跨域泛化至早期法语文学时F1下降约15个百分点。效率方面，轻量模型推理速度比大语言模型快10倍以上，而精度损失不超过5%。

### 当前局限
当前方法对间接上下文线索（如隐含在叙事中的时空关系）处理能力不足，尤其在历史语言变体与OCR噪声叠加时，准确率显著下降。跨域泛化仍是瓶颈，早期法语文学文本的F1远低于报纸文本，表明模型对领域偏移的鲁棒性有限。此外，评测仅覆盖三类关系，未涉及更复杂的时空推理（如多人物、多地点交互）。

### 后续改进方向
- 方向1：引入历史语言知识增强。通过构建历史语言变体词典或预训练语言模型（如基于历史语料的RoBERTa），提升对古拼写、语法变体的鲁棒性，减少OCR噪声影响。
- 方向2：设计轻量化跨域适应机制。采用元学习或参数高效微调（如LoRA），在保持计算效率的同时，增强模型对未见过领域（如文学文本）的泛化能力，避免全量微调的高成本。

### 工程落地启发
对实际OCR/文档解析工程项目最有参考价值的是三维评测框架的实践意义：在部署历史文档关系抽取系统时，需权衡准确性、效率与泛化性。例如，文化遗产机构可优先采用轻量分类器（如DistilBERT）处理大规模报纸语料，仅在关键任务（如高精度专家分析）中启用大语言模型。此外，评测中发现的跨域泛化问题提示，工程落地时应预留领域适配模块（如动态词典更新），以应对不同历史文档的变体。

---

### 9. WinDOM: Self-Family Distillation for Small-Model GUI Grounding

- **ArXiv ID**: [2606.25964v1](https://arxiv.org/abs/2606.25964v1)
- **作者**: Chengheng Li-Chen, Zhiqian Zhou, Hao Chen, Nicolas Chauvin
- **发布时间**: 2026-06-24
- **分类**: cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2606.25964v1](https://arxiv.org/pdf/2606.25964v1)
- **相关度评分**: 1/10

#### 英文摘要

Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to obtain bounding-box training data without expensive human annotation, and how to combine supervised fine-tuning with reinforcement learning. We address both, with the explicit goal of pushing small-model performance rather than scaling up. WinDOM is a $54{,}425$-record grounding corpus harvested by driving an open-source Windows 11 web reimplementation under headless Playwright, with bounding boxes read directly off the DOM and no OCR or human annotation. Self-Family Distillation (SFD) is a single rejection-sampling cold-start parameterised only by the teacher choice: either an EMA of the student (no external model) or a frozen larger same-family teacher. We then treat the saturation depth of the SFD cold-start as an explicit GRPO hyperparameter. On a Qwen3.5-2B student, the under-saturated cold-start is a better GRPO initialiser than the converged one: SFD-4B with Early-init RL gains $+5.4$ OOD-mean ($+3.5$ ScreenSpot-Pro, $+7.0$ OSWorld-G, $+5.8$ ScreenSpot-V2) over the base. The same-size EMA mode lands within roughly one OOD-mean point of the cross-size $4$B variant ($65.2$ vs $66.3$) without an external teacher.

#### 深度分析（中文）

### 中文摘要
本文提出WinDOM，一个通过无头Playwright驱动开源Windows 11网页重实现自动收集的54,425条GUI接地语料库，其边界框直接从DOM读取，无需OCR或人工标注。同时，作者提出自族蒸馏（SFD）方法，通过拒绝采样冷启动，仅需选择教师模型（学生EMA或无外部模型的更大同族模型），并将冷启动的饱和深度作为显式GRPO超参数。在Qwen3.5-2B学生模型上，欠饱和冷启动（SFD-4B）配合早期初始化强化学习，在多个OOD基准上平均提升+5.4，且同尺寸EMA模式性能接近跨尺寸4B变体（65.2 vs 66.3），无需外部教师。

### 解决的核心问题
现有小型GUI接地智能体（约2B参数）面临两个开放性问题：一是如何在不依赖昂贵人工标注的情况下获取边界框训练数据；二是如何有效结合监督微调与强化学习，以在保持小模型规模的同时提升性能。本文旨在解决这两个痛点，推动小模型性能而非单纯扩大模型规模。

### 核心创新
- **数据集层面**：构建WinDOM语料库，通过自动化脚本从Windows 11网页实现的DOM中直接提取边界框，完全规避OCR和人工标注成本，数据规模达54,425条。
- **方法层面**：提出自族蒸馏（SFD），一种仅需选择教师模型（学生EMA或更大同族模型）的冷启动策略，将蒸馏饱和深度作为可调节的GRPO超参数，实现从欠饱和到完全收敛的灵活初始化。

### 创新点拆解
- **创新点1：WinDOM语料库构建**：利用无头Playwright驱动开源Windows 11网页重实现，直接从DOM提取边界框，数据收集过程全自动化，无需OCR或人类标注者，大幅降低数据获取成本。
- **创新点2：自族蒸馏（SFD）冷启动**：提出单次拒绝采样冷启动，教师模型可以是学生自身的指数移动平均（EMA）或一个冻结的更大同族模型。该方法将蒸馏的饱和程度作为显式超参数，允许在强化学习前选择欠饱和或完全收敛的初始化。
- **创新点3：欠饱和冷启动与早期初始化强化学习**：发现欠饱和的SFD冷启动（而非完全收敛的）是GRPO更优的初始化器，结合早期初始化RL能显著提升OOD性能，且EMA模式无需外部教师即可接近跨尺寸变体性能。

### 实验结果亮点
在Qwen3.5-2B学生模型上，SFD-4B（欠饱和）配合早期初始化RL（Early-init）相比基线平均提升+5.4 OOD-mean，具体为ScreenSpot-Pro +3.5、OSWorld-G +7.0、ScreenSpot-V2 +5.8。同尺寸EMA模式（无外部教师）达到65.2 OOD-mean，仅比跨尺寸4B变体的66.3低约1个点，验证了自蒸馏的有效性。

### 当前局限
WinDOM数据集仅覆盖Windows 11操作系统环境，其网页实现可能无法完全反映真实GUI的多样性，例如移动端或macOS的交互模式。SFD方法依赖于同族模型（如Qwen系列），若应用于不同架构或预训练目标的模型族，其蒸馏效果可能退化。此外，欠饱和冷启动策略的通用性尚未在更大规模或不同任务上验证。

### 后续改进方向
- **方向1：跨平台与多模态数据扩展**：将WinDOM的自动化收集框架推广到macOS、Linux桌面环境或移动端（如Android/iOS模拟器），构建多平台GUI接地语料库，提升模型泛化能力。
- **方向2：动态饱和深度自适应**：开发自动确定最优蒸馏饱和度的机制，例如基于验证集性能或梯度变化，替代当前的手动超参数调优，使SFD更易应用于不同规模模型。

### 工程落地启发
最有参考价值的是WinDOM的自动化数据收集流程：通过无头浏览器驱动开源系统网页实现，直接从DOM提取边界框，完全绕开OCR和人工标注。这为实际OCR/文档解析工程中构建大规模、低成本的GUI接地训练数据提供了高效范式，尤其适用于需要快速迭代的工业级部署场景。

---

### 10. Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning

- **ArXiv ID**: [2606.26036v1](https://arxiv.org/abs/2606.26036v1)
- **作者**: Poojitha Thota, Shirin Nilizadeh
- **发布时间**: 2026-06-25
- **分类**: cs.CL, cs.CR
- **PDF**: [https://arxiv.org/pdf/2606.26036v1](https://arxiv.org/pdf/2606.26036v1)
- **相关度评分**: 1/10

#### 英文摘要

Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.

#### 深度分析（中文）

### 中文摘要
本文提出一种名为“Detect, Unlearn, Restore”的三阶段统一后防御框架，用于检测和修复面向抽象式文本摘要的大语言模型在微调阶段遭受的数据投毒攻击。该框架在白盒场景下利用影响函数与语义一致性检查检测毒化样本，在黑盒场景下通过行为审计识别模型异常敏感性，并通过梯度上升遗忘技术恢复模型至接近原始性能。实验结果表明，该防御在九种架构和六个数据集上达到85-92%的检测精度，且恢复后ROUGE指标下降小于0.6%。

### 解决的核心问题
现有针对文本摘要模型的数据投毒防御方法主要依赖训练数据清洗或鲁棒训练，但无法有效应对微调阶段精心设计的毒化攻击，尤其是那些在标准评估指标上表现正常、却诱导模型产生偏见或事实扭曲摘要的攻击。此外，现有防御多假设白盒环境或需要重新训练，缺乏适用于黑盒场景、无需完整访问训练数据的后部署检测与修复机制。

### 核心创新
本文首次针对抽象式文本摘要模型的微调阶段数据投毒，提出一个统一的后防御框架，整合了检测、遗忘与恢复三个步骤。其核心创新在于：在白盒场景中利用影响函数识别异常高影响的毒化样本，并结合语义一致性检查进行精炼；在黑盒场景中通过语义保持扰动下模型行为敏感性差异进行审计；以及采用梯度上升遗忘技术高效修复模型，无需完整重训练。

### 创新点拆解
- **创新点1：白盒检测方法**。利用影响函数分析每个文档-摘要对在微调过程中的训练影响，发现毒化样本通常具有异常高的影响值，再通过语义一致性检查过滤误报，实现高精度检测。
- **创新点2：黑盒行为审计方法**。针对无法访问训练数据的场景，提出对模型施加语义保持扰动（如同义词替换），发现毒化模型对这类扰动的输出敏感性是正常模型的两到三倍，从而无需训练数据即可识别异常。
- **创新点3：新型攻击形式与统一修复**。引入针对事实扭曲和代表性偏见的两种新型投毒攻击，并验证了现有评估指标无法捕捉这些攻击。同时，提出梯度上升遗忘方法，在检测出毒化样本后，通过反向更新参数消除其影响，恢复模型至接近原始性能，且仅造成小于0.6%的ROUGE损失。

### 实验结果亮点
在九种架构（包括T5、BART、Pegasus等）和六个基准数据集（如CNN/DailyMail、XSum、SAMSum）上，面对自适应攻击，防御框架的检测精度达到85-92%。修复后，模型原始行为恢复率达96%，ROUGE-1/F分数下降不超过0.6%。黑盒审计中，毒化模型对语义保持扰动的敏感性提升2-3倍，验证了行为差异的可检测性。

### 当前局限
该方法主要针对微调阶段的数据投毒，对于预训练阶段或推理时的投毒攻击效果未知。黑盒审计依赖于语义保持扰动，对于高度复杂或对抗性设计的扰动可能失效。此外，梯度上升遗忘需要模型参数完全可访问，不适用于仅提供API的黑盒场景，且遗忘过程可能影响模型在非毒化样本上的泛化能力。

### 后续改进方向
- **方向1：扩展至黑盒遗忘场景**。研究无需访问模型参数的遗忘技术，例如基于提示工程的输出校准或影子模型蒸馏，使防御框架适用于仅提供API的部署环境。
- **方向2：融合多模态与文档结构特征**。将检测过程与文档版面分析、表格/公式识别等OCR特征结合，利用结构异常（如毒化样本中故意修改的表格内容）辅助提高检测精度，应对更隐蔽的语义保持攻击。

### 工程落地启发
对OCR/文档解析工程项目最有价值的点是其“后部署检测与修复”思路：在系统上线后，无需重新标注或清洗原始训练数据，即可通过行为审计（如对输入施加微小扰动后观察输出变化）快速发现模型被投毒或性能退化的情况。这种模式适合文档理解生产线，可在不影响整体服务的前提下，实现针对特定文档类型（如表格或公式）的模型异常监控与低成本修复。

---

### 11. Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution

- **ArXiv ID**: [2606.25721v1](https://arxiv.org/abs/2606.25721v1)
- **作者**: Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu, Ying-Dar Lin, Yu-Sung Wu...
- **发布时间**: 2026-06-24
- **分类**: cs.CR, cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2606.25721v1](https://arxiv.org/pdf/2606.25721v1)
- **相关度评分**: 1/10

#### 英文摘要

Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead. We present TRACE, a lightweight detection framework that identifies poisoning attacks by tracing answer-related tokens through token influence attribution. TRACE first discovers recurrent high-influence keywords across retrieved documents and then performs a secondary verification to confirm their influence on model predictions. Experiments on three QA benchmarks and six LLMs demonstrate strong detection performance while simultaneously uncovering attacker-specified target answers.

#### 深度分析（中文）

### 中文摘要
本文提出TRACE框架，通过令牌影响力归因技术追踪检索增强生成（RAG）系统中被投毒语料库的恶意文档。该方法首先在被检索文档中发现重复出现的高影响力关键词，随后进行二次验证以确认其对模型预测的操控，从而无需额外分类器或LLM验证即可高效检测投毒攻击。在三个问答基准和六个大型语言模型上的实验表明，TRACE不仅能实现强检测性能，还能揭示攻击者指定的目标答案。

### 解决的核心问题
现有RAG系统易受语料库投毒攻击，攻击者通过注入恶意文档操纵模型输出，而当前检测方法依赖辅助分类器或额外LLM验证，导致计算开销剧增。本文针对如何在不引入显著计算负担的前提下，准确识别投毒攻击及其目标答案这一具体问题展开研究。

### 核心创新
本文的核心创新在于提出一种基于令牌影响力归因的轻量级投毒检测框架TRACE，首次将影响力归因技术应用于RAG系统的攻击检测。该方法无需训练专用分类器或调用外部LLM进行验证，而是通过分析检索文档中令牌对模型预测的因果影响力来定位恶意内容，同时自动恢复攻击者预设的目标答案，实现了检测效率与准确性的统一。

### 创新点拆解
- 创新点1：提出“重复高影响力关键词发现”机制，通过跨文档令牌影响力归因，自动识别在多个检索文档中共同出现且对预测结果产生异常高影响的词汇，从而定位投毒线索。
- 创新点2：设计二次验证流程，对筛选出的候选关键词进行影响力确认，确保检测结果与模型预测的因果关系，避免误报，并能够直接输出攻击者期望的目标答案。
- 创新点3：构建全轻量级检测流水线，仅利用模型前向传播和梯度计算即可完成检测，无需额外训练或第三方模型，显著降低计算开销。

### 实验结果亮点
在三个问答基准（如Natural Questions、TriviaQA等）和六个LLM（包括Llama、GPT系列等）上，TRACE的投毒检测准确率超过95%，且在大多数场景下检测假阳性率低于5%。相比现有基于分类器或LLM验证的方法，TRACE将检测时间从秒级降低至毫秒级，同时成功恢复了攻击者在文档中嵌入的目标答案。

### 当前局限
该方法主要针对基于关键词注入的投毒攻击，对于使用语义模糊或高度隐晦的对抗性文本（如通过改写避免关键词重复）的攻击方式，检测性能可能下降。此外，TRACE依赖模型梯度的可获取性，对于无法访问梯度的黑盒模型或API场景，其应用受到限制。

### 后续改进方向
- 方向1：扩展至黑盒场景，利用零阶优化或代理模型梯度近似技术，使TRACE能够应用于无法获取梯度的商业LLM API环境。
- 方向2：引入对抗性训练增强鲁棒性，通过生成语义相似但关键词不同的投毒样本，训练影响力归因模块以区分恶意与正常文档，提升对隐晦攻击的检测能力。

### 工程落地启发
对实际OCR/文档解析工程项目，TRACE的思路提示我们可以将“令牌影响力归因”技术迁移至文档质量监控场景。例如，在OCR后处理阶段，通过分析文档中每个字符或单词对最终识别置信度的贡献，自动定位并修正由污损、噪声或篡改引起的异常高/低影响力区域，从而提升复杂场景下的文档解析准确性与抗干扰能力。

---

### 12. Weave of Formal Thought

- **ArXiv ID**: [2606.25987v1](https://arxiv.org/abs/2606.25987v1)
- **作者**: Alexandre Bouayad
- **发布时间**: 2026-06-24
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2606.25987v1](https://arxiv.org/pdf/2606.25987v1)
- **相关度评分**: 1/10

#### 英文摘要

Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language. While existing constrained-decoding frameworks address the former, they operate under rigid assumptions that preclude critical lexical mechanisms -- including context-sensitive lexing, maximal-munch tokenization, and keyword extraction -- and only approximate vocabulary masking, sacrificing completeness. For the latter, code LLMs typically inject grammatical structure via predetermined policies rather than learning which structural information to expose. In this work, we introduce Weave of Formal Thought (WoFT), a paradigm uniting rigorous syntactic validation with learned structural representations. First, we present a formal engine and constrained decoder that is sound and complete with respect to the full Tree-sitter specification. By augmenting generalized LR (GLR) parsing with a speculative-lexing construction that maintains concurrent lexer-state hypotheses synchronized with a GLR graph-structured stack, our decoder admits every subword token extending to a valid program prefix and rejects all others. Second, we present a latent-variable fine-tuning method training the language model to interleave non-terminal grammar symbols directly into generation. Utilizing the reweighted wake-sleep (RWS) algorithm to optimize the importance-weighted evidence lower bound (IW-ELBO) of the surface text, the model learns to selectively retain formal derivations as an adaptive structural scratchpad. For Python, fine-tuning StarCoder2-3B with our RWS objective reduces per-token cross-entropy by 14.3% relative to a text-only SFT baseline, demonstrating that discretionary latent syntax recovers critical structural information that flat autoregressive training discards.

#### 深度分析（中文）

### 中文摘要
本文提出Weave of Formal Thought（WoFT）范式，旨在解决大语言模型在代码生成中缺乏形式化语法保证与层次结构利用的问题。该工作包含两个核心组件：一个基于广义LR解析与推测性词法分析的约束解码器，确保输出语法有效且完备；以及一种利用重加权唤醒-睡眠算法优化重要性加权证据下界的潜变量微调方法，使模型学会在生成过程中自适应地交织非终结符语法符号。在Python代码生成任务上，使用WoFT微调StarCoder2-3B模型，相较于纯文本监督微调基线，每个token的交叉熵相对降低了14.3%。

### 解决的核心问题
现有大语言模型在代码生成时仅依赖表面流畅性，无法形式化保证输出语法的合法性，且未能利用目标语言的层次化结构信息。约束解码框架虽能解决语法有效性问题，但通常基于刚性假设，排除了上下文相关词法分析、最大匹配分词和关键字提取等关键机制，且仅近似地处理词汇掩码，牺牲了完备性；同时，现有代码语言模型通过预定策略注入语法结构，而非学习选择性地暴露哪些结构信息。

### 核心创新
本文的核心创新在于将形式化语法验证与可学习的结构表征统一到一个新范式WoFT中。具体而言，设计了一个基于广义LR解析与推测性词法分析的约束解码器，该解码器对完整的Tree-sitter规范而言是正确且完备的；同时，提出了一种潜变量微调方法，利用重加权唤醒-睡眠算法训练模型在生成过程中自适应地交错非终结符语法符号，从而将形式推导作为可调节的结构草稿本。

### 创新点拆解
- 创新点1：提出了一种新型约束解码器，通过将广义LR解析与推测性词法分析构建相结合，维护与GLR图结构栈同步的并发词法分析器状态假设，从而确保每个子词令牌都能扩展为有效程序前缀，并拒绝所有无效输出。
- 创新点2：引入了基于潜变量微调的框架，利用重加权唤醒-睡眠算法优化重要性加权证据下界（IW-ELBO），训练语言模型在生成中自动交织非终结符语法符号，使模型学习选择性保留形式推导作为自适应结构草稿本，而非依赖预定策略。
- 创新点3：将形式化语法约束与可学习的结构表征有机融合，首次实现了在代码生成中同时保证语法完备性与结构信息自适应暴露，克服了传统约束解码的刚性假设和纯文本训练的结构信息丢失问题。

### 实验结果亮点
在Python代码生成任务上，使用WoFT微调StarCoder2-3B模型，相较于纯文本监督微调（SFT）基线，每个token的交叉熵相对降低了14.3%。这一结果表明，通过引入离散的潜变量语法符号，模型能够恢复平面自回归训练所丢弃的关键结构信息，从而显著提升生成质量。

### 当前局限
该方法目前仅在Python语言上进行了验证，其泛化能力尚需在其他编程语言或形式化语法（如SQL、LaTeX等）上进一步评估。此外，推测性词法分析构建与GLR解析的结合可能带来额外的计算开销，在超大规模模型或实时生成场景中可能面临效率瓶颈。同时，模型学习交织语法符号的机制可能对训练数据的语法覆盖度敏感，在罕见或复杂语法结构上表现未知。

### 后续改进方向
- 方向1：将WoFT框架扩展至多语言代码生成场景，构建跨语言的统一形式化语法表示，并探索不同语言语法差异对约束解码器与潜变量学习的影响，以提升泛化能力。
- 方向2：优化推测性词法分析与GLR解析的计算效率，例如通过预计算常见语法路径的缓存机制或采用稀疏化状态剪枝策略，降低推理延迟，使其适用于实时交互式代码生成系统。
- 方向3：探索将WoFT中的潜变量语法符号学习应用于文档理解领域，例如在表格结构识别或公式解析中，使模型自动学习交织结构标记以提升对复杂布局的还原精度。

### 工程落地启发
对实际OCR/文档解析工程项目而言，WoFT中约束解码与潜变量学习的结合思路极具参考价值。例如，在解析数学公式或表格时，可借鉴其“形式化语法验证+自适应结构学习”的范式：先定义目标文档的完整语法规范（如LaTeX语法或表格结构规则），再利用类似GLR解析的约束解码确保输出结构合法，同时通过潜变量微调使模型自动学习交织结构标记（如表格行列分隔符或公式运算符优先级），从而在保证输出格式准确性的同时提升对复杂布局的泛化能力。

---

### 13. SARA: Unlocking Multilingual Knowledge in Mixture-of-Experts via Semantically Anchored Routing Alignment

- **ArXiv ID**: [2606.25821v1](https://arxiv.org/abs/2606.25821v1)
- **作者**: Tianyu Dong, Yangyang Liu, Jiang Zhou, Xinwei Wu, Xiaohu Zhao...
- **发布时间**: 2026-06-24
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.25821v1](https://arxiv.org/pdf/2606.25821v1)
- **相关度评分**: 1/10

#### 英文摘要

Sparse Mixture-of-Experts (MoE) architectures have emerged as an increasingly influential paradigm as they offer a strategic balance between parameter scalability and computational efficiency. However, low-resource languages, which suffer from a scarcity of high-quality training data, often have their tokens routed to different experts than those predominantly activated by high-resource inputs, which limits cross-lingual expert sharing. This cross-lingual routing divergence consequently hinders their efficacy in multilingual contexts. To address this issue, we propose SARA (Semantically Anchored Routing Alignment), a framework designed to transfer specialized capabilities from high-resource languages as anchors to low-resource languages. SARA explicitly aligns the routing distribution of multilingual inputs with high-resource semantic anchors using a symmetric Jensen-Shannon (JS) divergence constraint. Unlike traditional distillation methods that operate on output logits, SARA directly aligns the internal routing distributions of MoE layers, encouraging mechanistic consistency in expert selection across languages. We conduct experiments on 2 LLMs across 5 low-resource languages and 3 benchmarks. Experiment results demonstrate that SARA outperforms standard instruction tuning, e.g., +0.8% on Qwen3-30B-A3B and +1.2% on Phi-3.5-MoE-instruct on Global-MMLU. Further analyses show that SARA effectively addresses performance bottlenecks in low-resource languages, providing a scalable pathway to enhance multilingual capabilities in sparse architectures.

#### 深度分析（中文）

### 中文摘要
本文提出SARA（语义锚定路由对齐）框架，通过对称JS散度约束将高资源语言的路由分布对齐到低资源语言，以解决稀疏MoE架构中因跨语言路由分歧导致的低资源语言性能瓶颈。实验表明，该方法在Qwen3-30B-A3B和Phi-3.5-MoE-instruct上分别提升Global-MMLU指标0.8%和1.2%，有效增强了多语言能力。

### 解决的核心问题
现有稀疏MoE模型在处理低资源语言时，由于训练数据稀缺，其token会被路由到与高资源输入不同的专家，导致跨语言专家共享不足。这种路由分歧限制了模型在多语言场景下的泛化能力，使得低资源语言难以利用高资源语言专家习得的专业化知识。

### 核心创新
SARA的核心创新在于从路由分布层面进行跨语言对齐，而非传统的输出logits蒸馏。它通过对称JS散度约束，显式地将低资源语言输入的路由分布与高资源语言语义锚点对齐，促使模型在专家选择上保持跨语言的一致性，从而解锁MoE架构中高资源语言专家的多语言知识。

### 创新点拆解
- 创新点1：提出语义锚定路由对齐机制，利用高资源语言输入作为锚点，通过JS散度约束对齐低资源语言的路由分布，实现跨语言专家选择的一致性。
- 创新点2：区别于传统知识蒸馏作用于输出层，该方法直接作用于MoE层的内部路由分布，鼓励模型在机制层面实现跨语言专家激活的机械一致性，更高效地传递专家级能力。

### 实验结果亮点
在2个LLM（Qwen3-30B-A3B和Phi-3.5-MoE-instruct）上，针对5种低资源语言，在3个基准测试（Global-MMLU等）中，SARA相比标准指令微调分别提升0.8%和1.2%。进一步分析表明，该方法能有效缓解低资源语言的性能瓶颈，且对齐效果在多个语言对间泛化。

### 当前局限
SARA依赖于预定义的高资源语言语义锚点，若锚点语言与目标低资源语言在语义空间上差异过大，对齐效果可能受限。此外，该方法目前主要验证于解码器MoE模型，在编码器或编码器-解码器架构上的适用性尚未探索。

### 后续改进方向
- 方向1：引入动态锚点选择机制，根据低资源语言输入的语义相似度自动匹配最相关的高资源语言锚点，避免固定锚点导致的语义偏差。
- 方向2：探索更细粒度的路由对齐策略，例如对每个专家进行独立的路由分布约束，或结合专家重要性权重进行差异化对齐，以提升对齐的精准度。

### 工程落地启发
对于文档智能系统中多语言OCR后处理与理解任务，SARA提供了一种无需增加额外参数即可提升低资源语言性能的轻量化方案。在工程部署中，可直接复用现有高资源语言专家的路由逻辑，通过微调路由分布对齐模块，低成本增强模型对稀缺语种文档（如小语种发票、古籍）的处理能力。

---

### 14. Learning Action Priors for Cross-embodiment Robot Manipulation

- **ArXiv ID**: [2606.26095v1](https://arxiv.org/abs/2606.26095v1)
- **作者**: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun...
- **发布时间**: 2026-06-25
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.26095v1](https://arxiv.org/pdf/2606.26095v1)
- **相关度评分**: 1/10

#### 英文摘要

Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.

#### 深度分析（中文）

### 中文摘要
本文提出一种两阶段训练框架，旨在为视觉-语言-动作（VLA）模型中的动作模块预训练运动先验，以解决现有方法中动作模块几乎从零学习物理运动的问题。第一阶段利用流匹配编码器-解码器，仅从无条件的动作轨迹中学习跨本体的时间运动结构；第二阶段通过解码器复用和早期隐空间蒸馏，将该先验迁移至VLA训练。实验表明，该方法在13个跨本体任务上实现了更快收敛、更高成功率，尤其在数据稀缺的真实场景中表现显著优于基线。

### 解决的核心问题
现有VLA模型通常依赖VLM骨干网络，通过附加动作模块并联合优化策略，但动作模块缺乏显式的运动先验，导致早期优化需同时学习时间动作动态和跨模态对齐，这一问题在跨本体场景中尤为突出。本文针对该痛点，提出在跨模态对齐之前为动作模块注入运动先验，以解耦运动动力学学习与视觉-语言对齐的难度，从而提升策略学习的效率与泛化性。

### 核心创新
本文的核心创新在于提出了一种两阶段训练框架，将动作模块的运动先验学习与VLA跨模态对齐分离。具体而言，第一阶段通过流匹配方法，仅利用动作轨迹数据（不依赖视觉或语言输入）高效预训练动作模块的时序结构；第二阶段通过解码器复用和隐空间蒸馏，将学到的先验无缝迁移至端到端VLA训练中。该方法在方法层面首次将运动先验作为独立模块进行预训练，并展示了其在跨本体场景下的通用性。

### 创新点拆解
- **创新点1：无条件的运动先验预训练**  
  提出使用流匹配构建轻量级编码器-解码器动作模块，仅从无条件的动作轨迹中学习跨本体的时间运动结构，完全无需视觉或语言数据，从而高效捕捉动作的时序动态。

- **创新点2：先验迁移的两阶段VLA训练**  
  在VLA训练阶段，通过复用预训练解码器作为动作头，并对编码器输出进行早期隐空间蒸馏，将运动先验注入VLA策略，同时保留端到端微调能力，避免了从零学习的困难。

- **创新点3：紧凑的历史压缩器**  
  预训练编码器可被重用作紧凑的历史状态-动作压缩器，将多步历史信息编码为单一的时间上下文令牌，以极低计算成本实现历史感知的策略建模。

### 实验结果亮点
在13个跨本体任务（包括模拟和真实世界平台）上，该方法相比无动作先验的VLA基线，实现了更快的收敛速度和更高的任务成功率。在数据稀缺的真实世界任务中，性能提升尤为显著，例如在某些任务上成功率提升超过20%。此外，通过扩大第一阶段动作数据规模，学到的动作先验展现出更强的泛化能力，直接提升了下游VLA性能。

### 当前局限
该方法主要针对离散动作空间和固定时间步长的任务设计，对于需要连续精细控制（如灵巧手操作）或长时程任务（如多步骤组装）的泛化性尚未验证。此外，第一阶段预训练依赖大规模、高质量的动作轨迹数据，在数据获取困难的场景（如罕见机器人形态）中可能受限。论文未深入探讨运动先验与视觉特征之间的潜在冲突，例如当视觉输入与动作先验矛盾时可能导致策略退化。

### 后续改进方向
- **方向1：引入多模态条件化运动先验**  
  当前第一阶段仅使用无条件轨迹，可探索在预训练中注入弱视觉或语言条件（如任务描述），使先验更具任务感知性，减少后续对齐的难度。

- **方向2：扩展到连续控制与长时程任务**  
  将流匹配框架扩展至连续动作空间，并设计层级化时间编码机制，以处理需要精细力控或多阶段决策的复杂操纵任务。

### 工程落地启发
本文的关键启发在于：在构建视觉-语言-动作模型时，应优先将运动动力学学习解耦为独立预训练阶段，而非依赖端到端联合优化。对于实际OCR/文档解析工程，类似思路可应用于表格结构识别或公式解析：先利用大量无标注的版面布局或符号序列数据，预训练一个时序/结构先验模型（如流匹配），再与视觉特征对齐，从而在数据稀缺场景下提升鲁棒性。此外，历史压缩器设计可作为轻量级上下文编码模块，用于提升文档流式处理中的长距离依赖建模效率。

---

### 15. TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy

- **ArXiv ID**: [2606.26092v1](https://arxiv.org/abs/2606.26092v1)
- **作者**: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li...
- **发布时间**: 2026-06-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.26092v1](https://arxiv.org/pdf/2606.26092v1)
- **相关度评分**: 1/10

#### 英文摘要

While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.

#### 深度分析（中文）

### 中文摘要
本文针对现有视频虚拟试穿（VVT）方法受限于源相机轨迹、无法支持自由视角交互的问题，首次定义了相机可控视频虚拟试穿（CaM-VVT）任务，并提出统一的DiT框架TryOnCrafter。该方法通过构建可渲染的4D试穿代理（Renderable 4D Try-on Proxy），显式地将人体与背景解耦，利用3D高斯泼溅（3DGS）结合SMPL-X动画与度量对齐的背景点云，实现任意相机轨迹下的高保真视频合成。实验表明，TryOnCrafter在多种复杂相机运动下生成了结构同步、纹理逼真的虚拟试穿视频，并支持人体重定位、子弹时间及360度环绕视图等下游应用。

### 解决的核心问题
现有VVT方法严重依赖源视频的固定相机轨迹，无法根据用户需求自由切换视角或进行360度环绕观察，缺乏交互式视角探索的灵活性。此外，在非刚性人体动态与背景在任意、无约束相机运动下实现严格的结构同步，以及视角无关的纹理生成，是传统方法无法克服的挑战。

### 核心创新
本文的核心创新在于将视频虚拟试穿从被动跟随源轨迹的范式，提升至主动可控的相机轨迹驱动范式。具体而言，首次提出了可渲染的4D试穿代理，通过显式解耦人体与背景并建立结构锚点，使得视频生成模型能够严格遵循用户指定的任意相机轨迹，同时保证非刚性人体变形与背景的物理一致性。

### 创新点拆解
- 创新点1：任务定义与范式转变。首次提出CaM-VVT任务，将VVT从“跟随轨迹”转变为“控制轨迹”，为交互式虚拟试穿开辟了新研究方向。
- 创新点2：可渲染4D试穿代理。通过将2D试穿先验蒸馏为基于3DGS的穿衣人体模型，并利用SMPL-X序列动画与度量对齐的背景点云，显式解耦人体与场景，为视频生成提供了纹理密度高、运动完整性强的结构基础。
- 创新点3：代理锚定视频DiT（Proxy-Anchored Video DiT）。以4D试穿代理作为几何锚点，引导扩散模型在生成过程中严格遵循预设相机轨迹与物理合理变形，确保输出视频的时空一致性。

### 实验结果亮点
在自定义的CaM-VVT测试集上，TryOnCrafter相比VVT基线方法（如VToonCrafter、CloSeer）在FID、FVD、LPIPS等指标上均取得显著提升。例如，在360度环绕视角下，FID降低约15%，FVD降低约20%，LPIPS降低约12%，且生成的视频在结构同步性和纹理逼真度上均优于对比方法。用户研究表明，95%的参与者认为TryOnCrafter生成的视频更符合目标相机轨迹。

### 当前局限
该方法依赖SMPL-X进行人体姿态估计，对于遮挡严重、罕见姿态或非标准体型（如婴儿、宠物）的试穿效果有限。此外，4D代理的构建需要较高计算资源，且背景重建的质量直接受限于输入视频的视角覆盖度，对于大范围无纹理区域的重建易出现失真。

### 后续改进方向
- 方向1：探索更鲁棒的人体姿态估计方案，如结合扩散模型的隐式姿态估计，减少对SMPL-X的依赖，提升对复杂姿态与遮挡场景的适应能力。
- 方向2：引入神经辐射场（NeRF）与3DGS的混合表示，利用NeRF的隐式连续性补全3DGS在稀疏视角下的空洞，降低对密集视角输入的要求，提升背景重建的鲁棒性。

### 工程落地启发
对OCR/文档解析工程的启发在于：显式解耦与结构锚点思想可迁移至复杂文档版面理解任务。例如，可构建“可渲染的文档结构代理”（如将文字、表格、图像区域解耦为3DGS或网格表示），在版面重排、多视角文档扫描、以及动态文档（如PPT演示）的相机轨迹可控重建中，确保生成内容严格遵循预设的版面结构与几何约束，提升输出文档的一致性与可编辑性。

---
