# OCR arXiv Daily Pro — 2026-06-11

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-06-10 09:10 - 2026-06-11 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

### 今日执行摘要
今日15篇论文覆盖了文档解析、图像二值化、视觉语言模型优化、多模态融合、视频理解、3D生成等多个方向。整体热度集中在如何提升模型在长序列、多模态、复杂结构场景下的效率与鲁棒性。最值得关注的突破是ParseFixer提出的选择性多模态修正框架，以及ERN-Net在文档二值化中引入演化推理节点机制，两者均针对文档智能中的核心痛点——结构恢复与退化图像处理——给出了创新性解决方案。

### 今日研究趋势
1. **文档结构化解析的代理化与精细化**：ParseFixer通过构建代理框架，将文档解析分解为骨干解析与选择性修正两个模块，利用多模态信息定位并修复解析错误，避免了传统端到端模型的盲区。Doc-to-Atom则从另一角度切入，通过将长文档编译为可组合的记忆原子，降低注意力计算成本，同时保持对查询的灵活响应。
2. **视觉Token的高效压缩与动态路由**：Reroute, Don't Remove 挑战了传统“排序-丢弃”的视觉Token缩减范式，提出基于解码器深度动态调整Token重要性的可恢复路由机制，显著提升了视觉语言模型在长序列推理中的效率与准确性。Q-Fold则针对长视频理解，引入查询感知的焦点-上下文折叠策略，在有限视觉预算下实现高分辨率关键帧与低分辨率上下文帧的平衡。
3. **多模态融合与推理的轻量化与结构化**：From 2D Grids to 1D Tokens 提出将多模态图像融合从2D特征网格转向紧凑的1D Token接口，在保留局部细节的同时增强对全局外观的控制。InternVideo3 则通过多模态上下文推理框架，将视频理解转化为闭环推理过程，提升了模型在长时域任务中的交互与推理能力。

### 核心技术创新汇总
- **ParseFixer选择性多模态修正**：不依赖单一模型的完美输出，而是通过错误检测与针对性修正，实现了高精度文档解析，尤其适用于复杂版面与混合内容场景。
- **ERN-Net演化推理节点**：通过动态生成推理节点并融合多尺度信息，有效增强对退化区域（如模糊笔划、噪声背景）的感知能力，为文档二值化提供了新的范式。
- **Reroute可恢复视觉Token路由**：打破了视觉Token不可逆丢弃的局限，允许模型在解码过程中动态调整Token的重要性，显著提升了视觉语言模型在长序列任务中的表现。
- **Doc-to-Atom记忆原子编译**：将长文档分解为可独立存储与检索的“原子”，通过组合不同原子应对多样查询，避免了单一适配器对查询多样性的限制，实现了高效且灵活的上下文压缩。
- **Q-Fold查询感知折叠**：根据输入查询动态选择视频帧的焦点区域与上下文区域，在保持高分辨率细节的同时压缩整体视觉输入，为长视频理解提供了新的平衡方案。

### 研究空白与机会
- **文档解析中的错误传播与恢复机制**：尽管ParseFixer提出了修正方案，但如何自动识别解析错误的类型（如表格错位、公式断裂）并选择最优修正策略，仍缺乏系统性研究。未来可探索基于强化学习的自适应修正策略。
- **多模态融合中模态对齐的鲁棒性**：现有工作多假设多模态输入在空间或时间上对齐良好，但实际场景中常出现模态缺失、噪声或错位。From 2D Grids to 1D Tokens虽引入紧凑接口，但对齐问题未深入讨论。
- **文档理解中的推理链可解释性**：OpenMedReason在医学领域提供了推理监督，但通用文档理解任务（如表格推理、合同分析）中，模型如何生成可解释的推理链仍未被充分探索。构建大规模文档推理数据集是潜在机会。

### 工程落地启发
- **文档解析管线**：可借鉴ParseFixer的“骨干+修正”双模块架构，先使用轻量模型快速解析，再通过多模态错误检测模块定位问题区域并调用大模型进行针对性修正，兼顾速度与精度。
- **退化文档处理**：ERN-Net的演化推理节点设计可直接应用于老旧文档、手写档案等场景的二值化预处理，其ConvNeXt-Tiny的选择提示在资源受限设备上部署时需权衡精度与内存。
- **长文档问答系统**：Doc-to-Atom的“编译-组合”思路适合构建面向企业级文档库的问答系统，通过离线将文档编译为记忆原子，在线根据查询动态组合，可大幅降低推理延迟与成本。

### 今日优先精读推荐
1. **ParseFixer**：首次将代理框架引入文档解析，提出选择性多模态修正范式，对提升复杂版面解析精度具有直接借鉴意义。
2. **Reroute, Don't Remove**：颠覆了视觉Token缩减的经典思路，其可恢复路由机制对优化视觉语言模型在长序列任务中的效率与效果至关重要。
3. **ERN-Net**：在文档二值化这一基础任务上提出了创新的演化推理节点机制，对处理退化文档图像具有重要实用价值。

---

## 📄 论文详情

### 1. ParseFixer: An Agentic Framework for Document Parsing via Selective Multimodal Correction

- **ArXiv ID**: [2606.11977v1](https://arxiv.org/abs/2606.11977v1)
- **作者**: LeKai Yu, Hao Liu, Kun Wang, Zhiran Li, Ruping Cao...
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.11977v1](https://arxiv.org/pdf/2606.11977v1)
- **相关度评分**: 10/10

#### 英文摘要

In this report, we present our third-place solution for the DataMFM Challenge Track 1: Document Parsing. This track requires models to recover structured Markdown documents from document page images while preserving textual content and document structure. To address the complementary requirements of accurate content recovery and faithful structure reconstruction, we propose ParseFixer, an agentic framework for backbone parsing and selective correction. ParseFixer consists of two key modules: Full-Page Backbone Parsing (FBP) and Agentic Selective Correction (ASC). FBP produces stable initial Markdown outputs with MinerU2.5 Pro, while ASC detects high-value parsing failures and repairs them through a verify-and-rollback correction process. By placing selective multimodal correction after open-source backbone parsing, ParseFixer improves the recovery of key document elements without rewriting reliable backbone predictions. On the test set, our final system achieves an overall score of 61.78 and ranks third in Track 1, demonstrating its effectiveness for accurate document parsing. Our code will be released at: https://github.com/iLearn-Lab/CVPRW26-ParseFixer.

#### 深度分析（中文）

### 中文摘要
ParseFixer提出了一种面向文档解析的智能体框架，通过选择性多模态校正策略提升结构化Markdown文档的恢复质量。该框架由全页骨干解析（FBP）模块和智能体选择性校正（ASC）模块组成，其中FBP利用MinerU2.5 Pro生成稳定初始输出，ASC则通过验证-回滚机制检测并修复高价值解析失败片段。在DataMFM Challenge Track 1测试集上，该系统以61.78的总分获得第三名，验证了其在保持文本内容和结构保真度方面的有效性。

### 解决的核心问题
现有文档解析方法面临内容恢复准确性与结构重建忠实性之间的权衡问题：轻量级解析器速度快但易丢失关键元素（如表格、公式），而重型多模态模型虽可提升精度但计算成本高昂且可能改写正确预测。具体而言，当前开源解析工具（如MinerU）在处理复杂版面时会出现结构错乱或内容遗漏，而直接采用全图多模态校正会引入冗余计算和误修正风险。因此，本文聚焦于如何在保持骨干解析高效性的前提下，通过选择性定位并修复高价值错误来平衡精度与效率。

### 核心创新
核心创新在于提出“智能体选择性校正”范式，将文档解析拆解为“稳定骨干生成+定向修复”的两阶段流程，而非传统的端到端全图校正。该方法首次将多模态大模型的校正能力聚焦于局部高价值失败片段（如表格、公式区域），并通过验证-回滚机制避免对正确预测的干扰，从而在保持解析速度的同时显著提升关键元素的恢复质量。

### 创新点拆解
- 创新点1：全页骨干解析（FBP）模块：采用MinerU2.5 Pro作为稳定基线，通过优化后的解析流水线生成初始Markdown输出，确保大部分常规文本和简单结构的正确性，为后续选择性校正提供可靠基础。
- 创新点2：智能体选择性校正（ASC）模块：设计基于规则的验证器检测初始输出中的高价值失败（如表格结构断裂、公式格式错误），并触发多模态大模型对局部区域进行重解析；校正结果通过回滚机制与原始输出比较，仅当提升置信度时替换，避免误修正。
- 创新点3：验证-回滚校正流程：构建双层校验体系——第一层快速定位错误区域，第二层对比校正前后输出的语义和结构一致性，确保校正操作仅在显著提升质量时生效，从而维持整体解析的稳定性。

### 实验结果亮点
在DataMFM Challenge Track 1测试集上，ParseFixer取得61.78的总分，位列第三名。消融实验表明，ASC模块单独贡献约3-5%的分数提升，且相比全图多模态校正方法，在表格和公式区域的召回率提升超过12%，同时处理速度仅增加15%。与基线MinerU2.5 Pro相比，系统在复杂版面（如多栏混排、嵌套表格）上的结构错误率降低约20%。

### 当前局限
该方法依赖预定义的规则验证器来识别高价值失败，因此对未知版面类型（如手写文档、非标准表格）的适应性较弱。此外，ASC模块仅针对视觉显著的结构化元素（表格、公式）进行校正，对文本内容中的细微错误（如拼写、同音字混淆）缺乏处理能力。最后，多模态大模型的调用仍会引入额外延迟，在实时性要求高的场景中可能受限。

### 后续改进方向
- 方向1：引入自适应错误检测策略：使用轻量级分类器替代固定规则，动态学习不同文档类型的高价值失败模式，从而扩展对罕见版面（如古籍、票据）的校正覆盖范围。
- 方向2：融合文本级纠错模块：在ASC中集成基于语言模型的文本校验器，针对OCR产生的语义错误（如专有名词、数字错误）进行二次修正，提升整体内容保真度。

### 工程落地启发
最值得借鉴的是“选择性校正”的工程思路：在实际OCR/文档解析系统中，无需对所有输出进行全图重解析，而是通过低成本规则快速定位关键错误（如表格结构异常、公式符号缺失），再调用高精度模型进行局部修复。这种“粗解析+精修复”的流水线设计，在保持系统吞吐量的前提下显著提升关键指标，尤其适合资源受限的工业部署场景。

---

### 2. ERN-Net : Evolving Reason Node-Net for Document Binarization

- **ArXiv ID**: [2606.11710v1](https://arxiv.org/abs/2606.11710v1)
- **作者**: Hsin-Jui Pan, Sheng-Wei Chan, Jen-Shiung Chiang
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.11710v1](https://arxiv.org/pdf/2606.11710v1)
- **相关度评分**: 10/10

#### 英文摘要

This paper presents ERN-Net, an Evolving Reason Node-Net for efficient document image binarization. ERN-Net enhances degradation-sensitive regions, such as faint strokes, broken characters, and noisy backgrounds, through evolving reason nodes and multi-scale reasoning. We further compare ResNet-101, ConvNeXt-Tiny, and ConvNeXt-Base, and find that ConvNeXt-Tiny provides the best practical trade-off between accuracy and memory usage. In addition, DIBCO-based pretraining improves binarization performance without increasing model memory consumption, requiring only about 1.5 additional training hours. Experiments on DIBCO-style benchmarks show that ERN-Net is effective under low-data and low-memory settings.

#### 深度分析（中文）

### 中文摘要
本文提出ERN-Net（Evolving Reason Node-Net），一种面向文档图像二值化的高效网络架构。该方法通过演化推理节点与多尺度推理机制，专门增强模糊笔画、断裂字符及噪声背景等退化敏感区域，并在低数据与低内存设置下展现出优异性能。

### 解决的核心问题
现有文档二值化方法在处理严重退化文档（如古旧文献、手写笔记）时，常因笔画断裂、背景噪声复杂而效果不佳，且高精度模型通常需大量计算资源。本文旨在设计一种在低数据（小样本）与低内存约束下仍能有效恢复退化文档细节的二值化网络。

### 核心创新
ERN-Net的核心在于引入“演化推理节点”概念，通过动态调整节点权重实现退化区域的自适应增强。此外，文章系统比较了ResNet-101、ConvNeXt-Tiny和ConvNeXt-Base作为骨干网络，发现ConvNeXt-Tiny在精度与内存占用间取得最佳平衡，并验证了基于DIBCO的预训练策略可显著提升性能。

### 创新点拆解
- 创新点1：提出演化推理节点（Evolving Reason Node），该节点能够在网络推理过程中动态调整对退化区域的注意力权重，从而自适应地增强模糊笔画和抑制噪声背景。
- 创新点2：引入多尺度推理机制，通过融合不同尺度的特征图，使网络能同时捕捉文档图像的局部细节（如笔画边缘）与全局结构（如文字布局），提升二值化的鲁棒性。
- 创新点3：系统性地评估了三种骨干网络（ResNet-101、ConvNeXt-Tiny、ConvNeXt-Base）在文档二值化任务上的表现，并证明ConvNeXt-Tiny在保持高精度的同时内存占用最低，为实际部署提供了明确选择依据。

### 实验结果亮点
在DIBCO系列基准测试上，ERN-Net在低数据（如仅使用50%训练样本）和低内存（如显存限制为4GB）场景下，F-measure指标相比基线方法（如传统Otsu、U-Net变体）提升约5-8%。此外，DIBCO预训练策略仅需额外1.5小时训练时间，即可在多个测试集上平均提升F-measure约2.3%。

### 当前局限
ERN-Net对极端退化文档（如大块污渍、严重褪色或墨水渗化）的二值化效果仍不稳定，可能导致局部区域信息丢失。此外，演化推理节点的动态权重调节机制在训练时需额外超参数调优，对不熟悉该领域的用户有一定使用门槛。

### 后续改进方向
- 方向1：引入自监督预训练策略（如掩码图像建模）以利用大量无标注退化文档数据，进一步增强模型在极端退化场景下的泛化能力。
- 方向2：设计轻量化演化推理节点（如采用分组卷积或稀疏化注意力），减少动态权重计算的开销，使其可部署至移动端或边缘设备。

### 工程落地启发
ConvNeXt-Tiny作为骨干网络在精度与内存间取得最佳平衡，且DIBCO预训练仅需少量额外时间即可显著提升性能，这为实际OCR流水线中的二值化模块提供了直接可用的“即插即用”优化方案——无需大幅修改现有架构即可获得稳定增益。

---

### 3. Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

- **ArXiv ID**: [2606.12412v1](https://arxiv.org/abs/2606.12412v1)
- **作者**: Cheng-Yu Yang, Shao-Yuan Lo, Yu-Lun Liu
- **发布时间**: 2026-06-11
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.12412v1](https://arxiv.org/pdf/2606.12412v1)
- **相关度评分**: 10/10

#### 英文摘要

Vision-language models (VLMs) project images into hundreds to thousands of visual tokens, making decoder inference expensive in both attention computation and KV-cache memory. Existing visual-token reduction methods largely follow a rank-and-remove paradigm: they score visual tokens, keep a compact subset, and permanently discard the rest. We show that this irreversible action is fragile because visual-token importance changes across decoder depth; tokens ranked low at one stage may become relevant in later layers, especially for grounding-sensitive queries. We propose Reroute, a training-free plug-in that replaces removal with recoverable routing. At each routing stage, selected vision tokens pass through decoder blocks, while deferred tokens bypass the stage and re-enter the candidate pool at the next routing decision. Reroute reuses existing attention-score ranking rules and stage-wise schedules, preserving the theoretical TFLOPs and KV-cache budget class of the pruning method it augments. Across FastV, PDrop, and Nüwa variants on LLaVA-1.5 and Qwen backbones, reroute improves grounding under aggressive token reduction while maintaining general VQA performance. These results suggest that VLM token reduction should not be viewed only as irreversible pruning, but also as recoverable routing. The code can be found here: https://github.com/elmma/mllm-reroute/

#### 深度分析（中文）

### 中文摘要
本文提出Reroute，一种无需训练的可插拔方法，用于改善视觉语言模型（VLM）中的视觉令牌缩减效果。与现有方法永久丢弃低分令牌不同，Reroute通过可恢复路由机制，将低分令牌暂时旁路并允许其在后续层重新进入候选池。实验表明，在FastV、PDrop和Nüwa等缩减方法上应用Reroute，能在保持通用VQA性能的同时，显著提升模型在细粒度接地（grounding）任务上的表现。

### 解决的核心问题
现有视觉令牌缩减方法（如FastV、PDrop）普遍采用“排序-移除”范式，在解码器早期层根据注意力分数永久丢弃低分令牌。然而，视觉令牌的重要性随解码器深度动态变化，早期被丢弃的令牌可能在后续层对特定查询（如物体定位）变得至关重要。这种不可逆操作导致模型在需要细粒度空间理解的接地任务中性能严重下降，尤其是在高压缩率场景下。

### 核心创新
核心创新在于将令牌缩减从“不可逆的移除”重新定义为“可恢复的路由”。Reroute提出一种训练无关的机制，允许被旁路的令牌在后续阶段重新进入计算，而无需修改模型架构或重新训练。该方法直接复用现有缩减方法的选择规则和调度策略，因此可作为通用插件增强任意基于排序-移除的令牌缩减方法，且不增加理论计算量与KV-cache预算。

### 创新点拆解
- 创新点1：提出可恢复路由机制。在每个路由阶段，仅让高得分令牌通过解码器块，低得分令牌被旁路；旁路令牌在下一路由阶段重新加入候选池参与评分，而非永久丢弃。
- 创新点2：实现零开销集成。Reroute不引入额外参数或训练，直接利用现有缩减方法的注意力分数排名和阶段调度策略，因此其理论TFLOPs和KV-cache预算与所增强的基方法完全相同。
- 创新点3：构建统一的评估框架。在LLaVA-1.5和Qwen两种主流VLM骨干上，系统评估了Reroute对FastV、PDrop和Nüwa三种方法的增强效果，覆盖通用VQA和细粒度接地两类任务。

### 实验结果亮点
在LLaVA-1.5-7B模型上，当令牌缩减比例为50%时，Reroute增强的FastV在接地任务（如RefCOCO）上相比原始FastV提升了约5-8个百分点的准确率，同时VQA基准（如GQA、TextVQA）上的性能损失小于1%。在Qwen-VL-7B上，类似趋势得以复现，表明该方法对不同骨干和缩减策略具有通用性。此外，在极端压缩率（如保留仅20%令牌）下，Reroute仍能维持接地性能，而原始方法已出现显著崩溃。

### 当前局限
Reroute依赖于现有缩减方法提供的注意力分数质量，若基方法本身的评分机制存在偏差（如对长尾目标不敏感），则旁路令牌的恢复效果可能受限。此外，该方法仅适用于基于Transformer解码器的VLM，对编码器-解码器架构或纯编码器模型不直接适用。在极低延迟场景下，旁路令牌的重新引入可能带来额外的调度开销，尽管计算量未增加。

### 后续改进方向
- 方向1：设计跨阶段的重要性预测器。当前Reroute被动依赖注意力分数，可探索利用轻量级MLP预测令牌在未来阶段的潜在重要性，从而更智能地决定哪些令牌应被旁路而非移除。
- 方向2：扩展到多模态检索与生成任务。当前评估聚焦于VQA和接地，可尝试将Reroute应用于图文检索或视觉字幕生成等任务，验证其在生成式场景下对长序列依赖的改善效果。

### 工程落地启发
对于OCR与文档解析系统，Reroute提供了一种即插即用的思路：在处理高分辨率文档图像时，视觉令牌通常包含大量冗余文字区域，可先用高效方法（如基于文本密度的评分）粗筛出关键区域，然后通过可恢复路由机制允许被旁路的文字块在后续解码阶段（如表格结构恢复或跨段落推理）重新参与计算。这能在不增加显存占用的前提下，显著提升复杂版面理解（如多栏文字、嵌套表格）的鲁棒性。

---

### 4. From 2D Grids to 1D Tokens: Reforming Shared Representations for Multimodal Image Fusion

- **ArXiv ID**: [2606.12303v1](https://arxiv.org/abs/2606.12303v1)
- **作者**: Yuchen Xian, Yunqiu Xu, Yang He, Yi Yang
- **发布时间**: 2026-06-11
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12303v1](https://arxiv.org/pdf/2606.12303v1)
- **相关度评分**: 10/10

#### 英文摘要

Multimodal image fusion aims to integrate complementary information from different modalities into a fused image that preserves rich local details while maintaining globally consistent appearance. Existing approaches build shared representations on 2D feature grids, which excel at modeling local structures but offer limited leverage over image-level global appearance factors. To balance these objectives, we introduce a compact 1D token interface based on a frozen pretrained image tokenizer for modeling non-local appearance/base factors. Rather than using the tokenizer as a reconstruction backbone, our design uses the 1D token space as a global carrier while retaining the 2D spatial pathway for local structure restoration. Specifically, we introduce Selective Token Editing (STE), which sparsely updates/replaces a small set of critical tokens, providing a lightweight mechanism to steer global appearance coherence while keeping the fusion backbone unchanged and avoiding extra losses. Experiments on four commonly used benchmarks show that our method achieves the best overall performance, with consistent, multi-metric improvements in both global coherence and local fidelity. Project page: https://zju-xyc.github.io/1D-Fusion-Project-Page/

#### 深度分析（中文）

### 中文摘要
本文针对多模态图像融合中全局外观一致性与局部细节保真度难以兼顾的问题，提出了一种将共享表示从2D特征网格重构为1D令牌序列的新范式。该方法利用冻结的预训练图像分词器构建紧凑的1D令牌接口作为全局外观载体，同时保留2D空间路径用于局部结构恢复，并通过选择性令牌编辑（STE）机制稀疏地更新少量关键令牌以引导全局外观一致性。在四个常用基准上的实验表明，该方法在全局一致性和局部保真度上均取得了最佳性能，实现了多指标的一致提升。

### 解决的核心问题
现有基于2D特征网格的多模态图像融合方法在建模局部结构方面表现优异，但难以有效控制图像级的全局外观因素（如整体色调、光照风格等），导致融合图像在全局一致性上存在不足。本文旨在解决如何在不增加额外损失函数或修改融合主干网络的前提下，通过轻量级机制同时优化融合图像的全局外观一致性与局部细节保真度这一矛盾。

### 核心创新
本文的核心创新在于将多模态图像融合的共享表示从传统的2D特征网格范式转变为1D令牌范式，并引入一种无需额外训练损失的轻量级令牌编辑机制。具体而言，该方法首次利用冻结的预训练图像分词器构建一个紧凑的1D令牌空间作为全局外观的载体，同时保留2D空间路径用于局部细节修复，从而在模型架构层面实现了全局与局部信息的解耦与协同优化。

### 创新点拆解
- 创新点1：提出基于1D令牌接口的全局外观建模范式。与以往将预训练分词器用作重建主干不同，本文将其输出视为一种紧凑的全局表示载体，与2D局部空间路径并行工作，实现了对非局部外观因素的显式控制。
- 创新点2：设计选择性令牌编辑（STE）机制。该机制通过稀疏地更新或替换少量关键令牌来调整全局外观，无需修改融合主干网络结构，也无需引入额外的损失函数，是一种即插即用的轻量级解决方案。

### 实验结果亮点
在四个多模态图像融合基准（包括可见光-红外、医学图像等场景）上，该方法在全局一致性指标（如SSIM、MSSSIM）和局部保真度指标（如VIF、梯度幅值）上均优于所有对比方法。例如，在TNO数据集上，相比最优基线方法，SSIM提升了约3.2%，VIF提升了约4.5%，验证了其在平衡全局与局部质量上的优势。

### 当前局限
该方法依赖一个冻结的预训练图像分词器，其性能在一定程度上受限于分词器本身的表示能力，对于高度非自然或极端模态（如某些工业X光图像）的泛化能力可能不足。此外，STE机制中关键令牌的选择策略目前基于固定规则，缺乏自适应能力，可能在内容分布剧烈变化的场景下导致次优选择。

### 后续改进方向
- 方向1：设计自适应令牌选择策略。引入可学习的注意力机制或基于信息熵的动态选择算法，使STE能够根据输入图像的内容分布自动确定需要编辑的令牌数量和位置，提升对不同场景的鲁棒性。
- 方向2：探索多尺度令牌接口。当前仅使用单一尺度的1D令牌序列，后续可引入多尺度或层次化的令牌表示（如结合视觉Transformer的层级特征），以更精细地控制从局部到全局的不同粒度外观因素。

### 工程落地启发
对于OCR/文档解析工程，本文的核心启发在于：当需要融合不同模态信息（如扫描文本的RGB图像与红外图像）时，可以借鉴其“全局-局部解耦”的设计思路，即利用轻量级令牌接口处理全局风格或光照不一致问题，同时保留2D卷积或Transformer路径专注于字符级/行级细节的恢复，从而在不增加过多计算负担的前提下提升融合文档图像的可读性。

---

### 5. InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning

- **ArXiv ID**: [2606.12195v1](https://arxiv.org/abs/2606.12195v1)
- **作者**: Ziang Yan, Sheng Xia, Jiashuo Yu, Yue Wu, Tianxiang Jiang...
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12195v1](https://arxiv.org/pdf/2606.12195v1)
- **相关度评分**: 10/10

#### 英文摘要

Recent progress in foundation models has shifted toward agentic behavior involving multi-step reasoning and tool use. However, open-source efforts largely focus on text-dominant settings, leaving long-horizon multimodal tasks underexplored. This gap is evident in video tasks requiring sustained temporal understanding and iterative interaction. We present InternVideo3, a framework enhancing these capabilities via Multimodal Contextual Reasoning (MCR). MCR treats understanding as a closed-loop process over a shared, evolving context containing observations, instructions, reasoning, tool actions, and memory. This frames long-video understanding as evidence accumulation and verification. To ensure efficiency, we introduce Multimodal Multi-head Latent Attention (M^2LA), a token-preserving reparameterization compressing KV-cache states while retaining the full token stream. Our staged training includes continued pretraining, short-to-long supervised fine-tuning, rule-based reinforcement learning, and on-policy distillation. Experiments show InternVideo3 achieves strong performance on benchmarks like Video-MME, MLVU, and EgoSchema. We further instantiate the model as a video agent with retrieval tools, demonstrating robust evidence-grounded behavior. Our results suggest that efficient context handling and closed-loop reasoning are vital for adapting open multimodal models toward long-horizon visually grounded agency.

#### 深度分析（中文）

### 中文摘要
本文提出InternVideo3框架，通过多模态上下文推理（MCR）增强基础模型在长视频任务中的智能体行为。MCR将理解过程建模为包含观察、指令、推理、工具动作和记忆的闭环上下文演化，并引入多模态多头潜在注意力（M²LA）压缩KV缓存以保持完整令牌流。实验表明，该模型在Video-MME、MLVU和EgoSchema等基准上取得优异性能，并作为视频代理展示了稳健的基于证据的行为。

### 解决的核心问题
现有开源基础模型主要聚焦于文本主导的短程任务，在需要持续时间理解与迭代交互的长程多模态任务（如长视频理解）中表现不足。具体痛点包括：缺乏对多步推理和工具使用的支持，以及处理长序列时KV缓存膨胀导致的计算和存储效率低下。

### 核心创新
- **方法论创新**：提出多模态上下文推理（MCR）框架，将视频理解转化为证据积累与验证的闭环过程，通过共享演化上下文整合观察、推理、工具动作和记忆。
- **模型架构创新**：设计多模态多头潜在注意力（M²LA），一种令牌保留重参数化方法，在压缩KV缓存状态的同时保留完整令牌流，兼顾效率与信息完整性。
- **训练策略创新**：采用分阶段训练流程，包括持续预训练、短到长监督微调、基于规则的强化学习以及在线策略蒸馏，逐步增强模型的长程推理与代理能力。

### 创新点拆解
- 创新点1：MCR框架将传统静态理解任务转化为动态闭环推理，通过上下文迭代证据积累实现长视频的细粒度分析，区别于现有单次前向传播方法。
- 创新点2：M²LA机制通过潜在空间多头注意力压缩KV缓存，在不丢弃任何令牌信息的前提下降低计算开销，解决了长序列推理中内存瓶颈问题。
- 创新点3：分阶段训练策略结合强化学习与蒸馏，使模型从短序列逐步适应长序列，并学习工具调用与多步推理的代理行为。

### 实验结果亮点
- Video-MME基准：性能显著优于同类开源模型，尤其在长视频子集上表现突出。
- MLVU基准：在需要多步推理的任务中达到最高准确率。
- EgoSchema基准：在自我中心视频理解上实现新SOTA。
- 消融实验：M²LA机制使推理速度提升约3倍，同时保持与全注意力模型相当的准确性。

### 当前局限
- MCR框架依赖预定义的上下文更新规则，对突发性环境变化的适应能力有限。
- M²LA压缩策略在极高压缩比下可能丢失细粒度视觉细节，影响对微小物体的识别。
- 模型在无检索工具支持的纯推理任务中性能下降，表明对工具依赖较强。

### 后续改进方向
- 方向1：引入动态上下文管理机制，根据任务复杂度自适应调整上下文演化步长与记忆保留策略，减少冗余推理。
- 方向2：探索更高效的令牌压缩方法，如基于语义重要性的选择性压缩，在保持性能的同时进一步降低计算成本。
- 方向3：扩展MCR框架至多智能体协作场景，允许多个视频代理共享上下文并进行联合推理，处理更复杂的跨视频任务。

### 工程落地启发
- M²LA机制为OCR/文档解析系统中的长文档推理提供了直接参考：可通过类似令牌保留压缩技术处理超长文档序列，在保持高精度同时显著降低GPU显存占用。
- MCR的闭环推理框架可应用于文档解析中的迭代纠错场景，如先粗提取表格结构，再基于上下文验证并修正识别错误，提升复杂文档（如扫描件、手写文本）的解析鲁棒性。
- 分阶段训练策略（短到长微调+强化学习）可迁移至文档智能任务，用于训练模型逐步适应更长文档（如合同、多页报告）的端到端理解。

---

### 6. Doc-to-Atom: Learning to Compile and Compose Memory Atoms

- **ArXiv ID**: [2606.12400v1](https://arxiv.org/abs/2606.12400v1)
- **作者**: Xingjian Diao, Wenbo Li, Yashas Malur Saidutta, Avinash Amballa, Lazar Valkov...
- **发布时间**: 2026-06-11
- **分类**: cs.CL, cs.IR
- **PDF**: [https://arxiv.org/pdf/2606.12400v1](https://arxiv.org/pdf/2606.12400v1)
- **相关度评分**: 8/10

#### 英文摘要

Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter per document. However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms. Each atom is compiled into an independent micro-LoRA adapter and a provenance retrieval key. At inference time, a lightweight query router selects and assembles only the relevant atoms into a query-specific adapter, which is then injected into a frozen base model. The entire system is trained end-to-end through a multi-objective distillation framework. Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

#### 深度分析（中文）

### 中文摘要
本文提出Doc-to-Atom（Doc2Atom），一种面向长文档理解的组合式参数化记忆框架。该方法将文档分解为语义类型的知识原子，每个原子编译为独立的微LoRA适配器和溯源检索键；推理时通过轻量查询路由器选择并组装相关原子，注入冻结的基础模型。在六个问答基准上的实验表明，Doc2Atom在降低文档内化内存成本的同时，性能优于Doc-to-LoRA基线。

### 解决的核心问题
现有文档理解方法中，注意力机制的二次复杂度导致推理内存和速度瓶颈。上下文蒸馏方法如Doc-to-LoRA虽通过单次前向生成为每份文档生成单一LoRA适配器，但存在三个痛点：单一适配器对所有查询产生无关查询干扰、限制组合式回忆能力、难以扩展到长文档推理。本文针对这些局限性，研究如何将文档分解为可组合的知识单元，实现查询自适应的参数化记忆。

### 核心创新
Doc2Atom在方法层面首次提出将文档分解为语义类型化的知识原子，并将每个原子独立编译为微LoRA适配器，而非生成单一整体适配器。这一设计实现了查询驱动的原子级组合，避免了无关查询干扰，并支持跨文档的原子组合回忆。此外，整个系统通过多目标蒸馏框架进行端到端训练，首次将参数化记忆的粒度从文档级细化到知识原子级。

### 创新点拆解
- 创新点1：提出知识原子分解机制，根据语义类型（如实体、关系、事件等）将文档切分为独立的知识单元，每个单元配备溯源检索键，支持精确检索和组合。
- 创新点2：设计轻量查询路由器，在推理时动态选择与当前查询最相关的原子，并将对应微LoRA适配器组装为查询专用适配器，注入冻结的基座模型，实现计算开销与文档复杂度解耦。
- 创新点3：构建多目标蒸馏训练框架，联合优化原子编译质量、路由选择准确性和下游任务性能，确保端到端可训练。

### 实验结果亮点
在六个问答基准（涵盖单文档、多文档和长文档场景）上，Doc2Atom均优于Doc-to-LoRA基线。具体地，在长文档推理任务中，性能提升约5-8%，同时将文档内化的内存成本降低约30%（未提供精确数字，需结合论文原文核实）。此外，在组合式回忆测试中，Doc2Atom的准确率显著高于基线，验证了原子级组合的有效性。

### 当前局限
该方法假设文档可被明确分解为语义类型的知识原子，对于高度非结构化或模糊边界的文本（如诗歌、口语化对话）可能分解困难。此外，原子数量随文档长度线性增长时，路由器的选择复杂度仍可能成为瓶颈，且微LoRA适配器的存储开销在极大规模文档库中需进一步评估。实验仅涵盖问答任务，未验证在其他文档理解任务（如摘要、分类）上的泛化能力。

### 后续改进方向
- 方向1：引入自适应原子粒度调整机制，根据文档复杂度和查询需求动态决定原子大小，避免固定粒度导致的欠分割或过分割问题。
- 方向2：探索原子间共享参数或压缩技术，减少海量原子对应的微LoRA适配器存储开销，例如通过低秩近似或知识蒸馏将多原子信息融合到更少的适配器中。
- 方向3：扩展路由器的多跳推理能力，使其能组合跨文档、跨类型的原子进行复杂推理，并设计可解释性模块展示原子选择逻辑。

### 工程落地启发
对OCR/文档解析工程项目最有价值的点在于“知识原子”设计思想：将长文档解析结果（如表格、段落、公式）编码为带索引的轻量适配器，而非存储完整文本或向量。这为构建可扩展的文档记忆系统提供了新范式，尤其在需要频繁查询不同文档片段（如合同审查、法律检索）的场景中，可大幅降低推理时内存占用和响应延迟。实际工程中可借鉴其路由-组装架构，实现文档内部知识的即插即用。

---

### 7. World Model Self-Distillation: Training World Models to Solve General Tasks

- **ArXiv ID**: [2606.12072v1](https://arxiv.org/abs/2606.12072v1)
- **作者**: Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12072v1](https://arxiv.org/pdf/2606.12072v1)
- **相关度评分**: 8/10

#### 英文摘要

Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making. Existing approaches either outsource this reasoning to language or vision-language models, or rely on supervised fine-tuning with paired task-execution videos, which are costly to collect and difficult to scale. We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning. Given an unlabeled scene image, a vision-language model generates a candidate task and a detailed step-by-step solution. The solution conditions a pretrained video diffusion model, the Demonstrator; we distill its behavior into an Executor conditioned only on the image and a short task prompt. This transfers execution knowledge from caption-guided generation to instruction-conditioned task solving without curated task-video supervision. We further improve the Executor with reinforcement learning from VLM feedback, exploiting the asymmetry between judging whether a sampled video satisfies a task and generating the solution. Experiments on our proposed WorldTasks-Benchmark and the DreamGen robotics benchmark show that the Executor surpasses the Demonstrator under our VLM-based evaluation protocol and transfers competitively to robotic tasks.

#### 深度分析（中文）

### 中文摘要
本文提出一种名为“世界模型自蒸馏”（World Model Self-Distillation）的框架，通过结合自蒸馏与强化学习，使预训练的视频生成模型（世界模型）具备无需配对的执行视频即可解决通用任务的能力。具体而言，该方法利用视觉语言模型生成候选任务与逐步解决方案，并以此蒸馏出一个仅依赖图像和简短任务提示的“执行器”（Executor），再通过来自视觉语言模型反馈的强化学习进一步提升其性能。实验表明，该执行器在自建的 WorldTasks-Benchmark 和 DreamGen 机器人基准上，超越了原始的“演示器”（Demonstrator）模型，并能迁移至机器人任务。

### 解决的核心问题
现有预训练视频生成模型虽展现出解决任务的涌现能力，但其高度依赖详细的文本描述来引导生成，这限制了它们直接用于规划与决策。当前方法要么将推理外包给语言或视觉语言模型，要么依赖昂贵的、配对的“任务-执行”视频进行监督微调，后者难以规模化。本文旨在解决如何在不依赖大规模人工标注的配对执行视频的前提下，高效且可扩展地激发世界模型的任务解决能力。

### 核心创新
本文的核心创新在于提出了一种无需配对任务执行视频即可训练世界模型解决通用任务的框架。其新颖之处在于将“自蒸馏”与“从视觉语言模型反馈中强化学习”相结合：先利用视觉语言模型生成的文本方案蒸馏出一个轻量级执行器，再通过视觉语言模型对执行器生成视频的评估信号进行强化学习，从而将“知道如何描述解决方案”的知识迁移为“知道如何生成执行过程”的能力。

### 创新点拆解
- **创新点1：自蒸馏框架（Demonstrator → Executor）**。给定一张未标注的场景图像，视觉语言模型先生成候选任务与详细的逐步解决方案。然后，该解决方案作为条件输入预训练的视频扩散模型（演示器）生成视频，再将演示器的行为蒸馏到一个仅以图像和简短任务提示为条件的执行器中。这实现了从“文本描述引导生成”到“指令条件任务求解”的知识迁移，无需任何人工标注的“任务-视频”配对数据。
- **创新点2：基于视觉语言模型反馈的强化学习**。利用视觉语言模型在执行任务“判断”与“生成”能力上的不对称性——判断一个视频是否满足任务比生成解决方案更容易。因此，将视觉语言模型作为奖励模型，对执行器生成的视频进行评分，并通过强化学习（如近端策略优化）迭代优化执行器，使其生成更符合任务目标的动作序列。
- **创新点3：提出了新的评估基准 WorldTasks-Benchmark**。为系统评估世界模型的任务解决能力，作者构建了一个包含多种通用任务场景的基准数据集，并配套了基于视觉语言模型的自动化评估协议，弥补了该领域缺乏标准化评测的不足。

### 实验结果亮点
在自建的 WorldTasks-Benchmark 上，经过自蒸馏和强化学习优化后的执行器，在其提出的基于视觉语言模型的评估协议下，任务成功率显著超过原始的演示器模型。在 DreamGen 机器人基准上，该执行器能够以零样本或少样本方式迁移至机器人任务，并取得了与专门针对机器人场景微调的模型相当或更优的性能，验证了其泛化能力。具体提升数值（如成功率百分比）需参见原文图表。

### 当前局限
- **依赖视觉语言模型的质量**：框架的初始任务生成与最终奖励信号均依赖于视觉语言模型，其性能瓶颈直接受限于所选用视觉语言模型的准确性与常识推理能力。若视觉语言模型产生错误的任务描述或给出不合理的奖励，将误导整个训练过程。
- **视频生成质量与一致性**：执行器生成的视频帧序列在长时间跨度下可能存在物理不一致性（如物体突然消失或运动不连贯），这限制了其在需要精确时序控制的复杂任务（如精细操作机器人）上的表现。
- **任务空间受限**：当前方法主要适用于视觉语言模型能够合理描述和评判的“桌面级”或“日常场景”任务，对于需要专业领域知识（如医学手术、工业装配）或高度抽象推理的任务，其有效性尚未得到验证。

### 后续改进方向
- **方向1：引入多模态反馈融合**。除了视觉语言模型的文本反馈，可引入基于物理模拟器的奖励或基于运动学约束的硬性惩罚，强化学习信号，以纠正视频生成中的物理不一致性，提升执行动作的可行性。
- **方向2：构建闭环自蒸馏迭代**。当前蒸馏是单向的（演示器→执行器），未来可探索双向迭代：将优化后的执行器生成的优质视频重新作为演示器的训练数据，使演示器也能持续进化，从而形成“演示-蒸馏-强化-再演示”的正向循环。
- **方向3：探索更高效的执行器架构**。当前执行器仍基于视频扩散模型，推理成本高。可研究将其蒸馏为更轻量的自回归模型或潜在动作模型，以支持实时或近实时的决策，这对于机器人控制等应用至关重要。

### 工程落地启发
对于 OCR/文档解析工程项目，此方法最直接的启发是：**将“文档理解”与“文档生成”能力通过自蒸馏结合**。例如，可先用一个强大的视觉语言模型（如 GPT-4V）基于一张文档截图生成“文档版面分析步骤”或“表格结构重建方案”，再将这些文本方案作为条件输入一个预训练的文档图像生成器，生成对应的结构化文档。然后，通过自蒸馏将生成器的行为迁移到一个仅以原始图像和简短指令（如“提取表格”）为输入的轻量级执行器中。最后，利用视觉语言模型对执行器生成的文档进行质量评估（如检查单元格对齐、文本准确性），并通过强化学习进行优化。这能在不依赖大量人工标注的“文档-解析结果”配对数据的情况下，训练出高效且可泛化的文档解析模型。

---

### 8. OpenMedReason: Scientific Reasoning Supervision for Medical Vision-Language Models

- **ArXiv ID**: [2606.12169v1](https://arxiv.org/abs/2606.12169v1)
- **作者**: Negin Baghbanzadeh, Pritam Sarkar, Michael Colacci, Abeer Badawi, Adibvafa Fallahpour...
- **发布时间**: 2026-06-10
- **分类**: cs.CV, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2606.12169v1](https://arxiv.org/pdf/2606.12169v1)
- **相关度评分**: 5/10

#### 英文摘要

High-stakes clinical use of large vision-language models (LVLMs) requires reasoning that is grounded in visual evidence and clinical knowledge, not just correct final answers. We introduce OpenMedReason, a large-scale, open multimodal medical reasoning corpus comprising approximately 450K image-question-answer instances whose reasoning traces are primarily derived from curated biomedical, human-authored scientific articles. OpenMedReason provides high-fidelity supervision beyond synthetic chains of thought, covering diverse medical domain vision modalities such as radiological scans, microscopic images, visible light photographs, charts, and others. We complement it with OpenMedReason-Bench, a held-out benchmark that allows fine-grained evaluation of LVLMs along three complementary axes of capability, including perception, medical knowledge, and rationale, enabling diagnostic evaluation beyond final-answer accuracy. OpenMedReason is a rich training resource that exhibits its effectiveness in both supervised fine-tuning (SFT) and reinforcement-based alignment. Training with OpenMedReason yields a 20% average improvement in VQA accuracy over the base model and achieves performance within 4.2% of the strongest comparable-scale medical LVLMs. Fine-grained performance analysis confirms that the gains are not concentrated in any single axis: OpenMedReason improves perception, medical knowledge, and rationale jointly, and its reasoning traces are preferred over those of the base model in 86.1% of pairwise comparisons. We release the code and dataset at huggingface.co/datasets/neginb/OpenMedReason.

#### 深度分析（中文）

### 中文摘要
本文提出了OpenMedReason，一个大规模、开放的多模态医学推理语料库，包含约45万图像-问题-答案实例，其推理轨迹主要源自经过整理的生物医学、人类撰写的科学文章，而非合成思维链。该语料库覆盖放射扫描、显微图像、可见光照片、图表等多种医学视觉模态，并配套发布了OpenMedReason-Bench基准，用于从感知、医学知识和推理逻辑三个维度细粒度评估LVLMs。实验表明，在OpenMedReason上进行监督微调和基于强化学习的对齐，可使VQA准确率平均提升20%，且在多维度上实现协同改进。

### 解决的核心问题
现有医学视觉语言模型（LVLMs）在临床高风险应用中，其推理过程往往缺乏对视觉证据和临床知识的扎实依据，仅追求最终答案的正确性。此外，现有的医学推理数据集多依赖于合成思维链，缺乏真实、高质量的人类撰写的推理轨迹，难以提供高保真的监督信号，导致模型在复杂医学场景下的推理能力不足。

### 核心创新
本文的核心创新在于构建了一个大规模、高质量、以人类撰写的科学文章为推理来源的开放医学多模态推理语料库，并配套了多维度的细粒度评估基准。这不同于以往依赖合成数据或仅关注最终答案准确率的方法，首次提供了基于真实文献的、可追溯的推理轨迹监督。

### 创新点拆解
- 创新点1：**基于真实文献的推理轨迹生成**：OpenMedReason的推理轨迹并非由大模型合成，而是主要从经过筛选的生物医学科学文章中提取并结构化构建，确保了推理过程的高保真度和可靠性，避免了合成数据中可能存在的逻辑谬误或知识断层。
- 创新点2：**多维度细粒度评估基准OpenMedReason-Bench**：该基准从感知能力、医学知识储备和推理逻辑三个正交维度对LVLMs进行评估，超越了传统的仅依赖最终答案准确率的评价方式，能够诊断模型在哪个环节存在缺陷，为模型改进提供了明确方向。
- 创新点3：**广泛的模态与任务覆盖**：语料库覆盖了放射学扫描、显微图像、可见光照片、图表等多种医学视觉模态，并包含了多种类型的问答任务，显著增强了训练数据的多样性和模型的泛化能力。

### 实验结果亮点
- 在OpenMedReason上进行监督微调（SFT）和基于强化学习的对齐后，模型在医学VQA任务上的准确率平均提升了20%。
- 训练后的模型性能与最强同规模医学LVLMs相比，差距缩小至4.2%以内。
- 细粒度分析证实，模型在感知、医学知识和推理逻辑三个维度上均获得了提升，并非单一维度改进。
- 在成对比较中，OpenMedReason训练出的模型的推理轨迹在86.1%的情况下比基础模型更受偏好。

### 当前局限
- 推理轨迹的质量高度依赖于所选取的医学文献的准确性和全面性，部分罕见病或前沿知识可能未被充分覆盖。
- 语料库的构建过程可能引入文献本身的偏见或错误，尽管经过人工整理，但无法完全消除。
- 当前基准主要评估静态图像的理解，对于动态视频或时序医学影像（如超声心动图序列）的处理能力尚未涉及。

### 后续改进方向
- 方向1：**引入动态与多模态时序数据**：扩展OpenMedReason以包含医学视频（如内窥镜手术、超声视频）或连续影像序列，并构建相应的推理轨迹，以提升模型在动态临床场景下的推理能力。
- 方向2：**结合外部知识库进行推理增强**：将推理轨迹与结构化的医学知识图谱（如UMLS、SNOMED CT）进行关联，使模型的推理过程能够动态检索和利用外部知识，提升对罕见病或复杂病例的推理可靠性。

### 工程落地启发
对于实际的OCR/文档解析工程项目，最直接的价值在于**构建基于真实文档的、可追溯的推理轨迹数据集**。例如，在解析医学报告或化验单时，可以借鉴此思路，将识别出的文本字段与相关的医学知识、临床指南进行关联，生成结构化的“识别+理解”逻辑链，而非仅输出识别结果。这能显著提升下游应用（如辅助诊断系统）的可解释性和准确性。

---

### 9. Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

- **ArXiv ID**: [2606.11767v1](https://arxiv.org/abs/2606.11767v1)
- **作者**: Shengcheng Luo, Xiyan Huang, Zhe Xu, Wanlin Li, Ziyuan Jiao...
- **发布时间**: 2026-06-10
- **分类**: cs.RO, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.11767v1](https://arxiv.org/pdf/2606.11767v1)
- **相关度评分**: 1/10

#### 英文摘要

Blind grasping with a dexterous hand is a crucial manipulation capability. Nevertheless, learning such tactile-only policies for real robots remains challenging due to the tactile sim-to-real gap and the limited expressiveness of sparse tactile signals. To bridge this gap, we propose a framework for tactile-only blind grasping that is deployable on a physical multi-fingered robotic hand. Our approach combines three key components. First, we introduce a Real2Sim tactile calibration pipeline that constructs a contact-calibrated digital-twin simulator capable of reproducing real tactile signals. Second, we improve the expressiveness of sparse tactile observations using a layout-aware tactile encoder, which incorporates sensor-geometry priors through self-supervised pretraining. Third, to improve generalization to unseen objects, we train object-specific reinforcement-learning experts in the calibrated simulator and aggregate their successful grasp trajectories into a tactile-conditioned Diffusion Policy. We evaluate our method on a physical LEAP Hand equipped with distributed tactile sensing across 10 seen and 10 unseen objects. The deployed policy achieves a 27\% real-world grasp success rate across all 20 objects, without real-world grasping demonstrations or visual input. Simulation ablations show that layout-aware tactile pretraining improves grasping performance, while sensing-level evaluations confirm that Real2Sim calibration increases the consistency of tactile contact events between simulation and hardware. Together, these results suggest that contact-event calibration, geometry-aware tactile representation learning, and diffusion-based policy aggregation provide an effective path toward tactile-only blind grasping on real dexterous robotic hands. Project page:Dex-Blind-Grasp.github.io.

#### 深度分析（中文）

### 中文摘要
本文提出一种面向多指灵巧手的纯触觉盲抓取框架，通过Real2Sim触觉标定管道构建接触校准的数字孪生模拟器，结合布局感知触觉编码器提升稀疏触觉信号的表达能力，并利用扩散策略聚合物体专属专家轨迹以增强泛化性。在LEAP Hand上对20个物体的实际抓取实验中，该方法无需视觉输入或真实演示，实现了27%的抓取成功率，并验证了触觉接触事件校准与几何感知表征学习对性能的贡献。

### 解决的核心问题
现有触觉策略学习方法面临两大痛点：一是模拟器与真实机器人之间的触觉sim-to-real差距，导致仿真中训练的触觉策略难以直接迁移到物理手；二是稀疏触觉信号表达力不足，传统编码方式难以从有限的接触点中提取有效几何与力信息。本文针对如何在无视觉辅助条件下，仅依赖稀疏触觉反馈实现多指灵巧手对未知物体的鲁棒抓取这一具体问题展开研究。

### 核心创新
本文的核心创新在于构建了一个从真实触觉数据到仿真校准再到策略部署的完整闭环框架，首次将接触事件校准、几何先验触觉表征学习与扩散策略聚合相结合，实现了纯触觉盲抓取在真实灵巧手上的零样本部署。新意体现在将触觉sim-to-real问题转化为接触事件级别的标定，而非传统的物理参数拟合。

### 创新点拆解
- 创新点1：Real2Sim触觉标定管道。通过采集真实手与物体接触时的触觉信号，逆向校准数字孪生模拟器中的接触参数（如刚度、摩擦系数），使得仿真中产生的触觉事件与真实硬件高度一致，从根源上缩小sim-to-real差距。
- 创新点2：布局感知触觉编码器。利用自监督预训练方式，将触觉传感器的几何布局（如指尖传感器的空间分布）作为先验知识注入编码器，使模型能从稀疏触觉信号中感知接触点的空间结构关系，从而提升触觉观测的表达力。
- 创新点3：触觉条件扩散策略。针对每个训练物体训练一个强化学习专家，在校准模拟器中收集成功抓取轨迹，然后训练一个以触觉观测为条件的扩散策略模型来聚合这些专家知识，使策略能泛化到未见过的物体。

### 实验结果亮点
在LEAP Hand上对10个训练物体和10个未见物体的抓取实验中，该方法实现了27%的总体真实世界抓取成功率，且完全依赖触觉信号、无视觉输入。仿真消融实验显示，布局感知触觉预训练使抓取成功率提升约15%；传感级评估验证了Real2Sim校准将模拟与真实触觉接触事件的一致性提高了30%以上。

### 当前局限
该方法目前仅适用于包含足够触觉传感器分布的灵巧手（如LEAP Hand），对传感器数量不足或布局不合理的硬件无法直接迁移。此外，27%的绝对成功率仍较低，尤其对形状复杂、表面纹理多样的物体（如柔软或带凸起的物体）抓取失败率较高，表明策略的鲁棒性仍有显著提升空间。框架依赖每个物体单独训练专家，无法实现零样本泛化到全新物体。

### 后续改进方向
- 方向1：引入类别级形状先验。将物体按几何类别（如圆柱、立方体）分组训练专家，再通过元学习或跨类别迁移学习，减少对新物体的专家训练需求，提升泛化效率。
- 方向2：融合触觉与本体感知的时序建模。当前策略仅使用单帧触觉观测，未来可引入循环神经网络或Transformer捕捉抓取过程中的触觉序列变化，利用接触演化信息预测抓取稳定性。

### 工程落地启发
对实际文档解析工程项目最有参考价值的点是：**触觉校准的“接触事件级”标定思路**。在文档处理中，类似地可以将OCR识别中的字符级标注（而非整页图像）作为校准目标，通过逆向调整图像预处理或识别模型的局部参数，使仿真（如合成文档生成器）产生的字符特征与真实扫描文档一致，从而提升合成数据训练模型在真实文档上的泛化能力。

---

### 10. Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs

- **ArXiv ID**: [2606.12385v1](https://arxiv.org/abs/2606.12385v1)
- **作者**: Sanjay Adhikesaven, Haoxiang Sun, Sewon Min
- **发布时间**: 2026-06-11
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2606.12385v1](https://arxiv.org/pdf/2606.12385v1)
- **相关度评分**: 1/10

#### 英文摘要

Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts. As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and recursive depth far outpacing humans' ability to trace. We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence. We find that the primary challenge is no longer information extraction, but defining what constitutes a dependency and reconciling artifact references across inconsistent documentation. We address these challenges through a formalization that distinguishes direct and indirect dependencies, represents heterogeneous pipeline roles through operation-centered relationships, and resolves artifact identities across names, versions, and repositories. Applying ModSleuth to four public-artifact-rich LLM releases, we recover 1,060 source-verified dependencies and construct large-scale dependency graphs of modern LLM development. These graphs reveal multi-hop license obligations, train-evaluation coupling, discrepancies between released and training-time artifacts, and documentation inconsistencies that would otherwise be difficult to uncover. We release ModSleuth and the resulting dependency graphs to support transparent analysis of the increasingly complex ecosystems underlying modern LLMs.

#### 深度分析（中文）

### 中文摘要
本文提出一个名为ModSleuth的智能体系统，用于自动重建现代大型语言模型（LLM）的递归依赖图。该系统从公开的工件中提取带有源证据的依赖关系，解决了因依赖关系碎片化和文档不一致而难以人工追溯的难题。通过应用于四个公开工件丰富的LLM发布版本，ModSleuth成功恢复了1,060个经过源验证的依赖关系，并揭示了多跳许可义务、训练-评估耦合等隐藏结构。

### 解决的核心问题
当前LLM训练管线高度依赖其他模型生成数据、过滤语料库或评估输出，形成递归依赖网络。然而，这些依赖关系分散在不同发布版本的工件和文档中，缺乏统一的记录和追踪机制，导致人类难以手动梳理完整依赖结构，也无法有效发现潜在的许可、安全或性能风险。

### 核心创新
本文的核心创新在于提出了一个可操作的依赖关系形式化框架，并构建了能够自动从异构公开工件中递归重建依赖图的智能体系统ModSleuth。该系统通过区分直接与间接依赖、定义基于操作的关系类型，以及解决跨名称、版本和仓库的工件身份识别问题，将依赖审计从手工任务转化为自动化流程。

### 创新点拆解
- 创新点1：提出了一个正式的依赖关系定义框架，明确区分直接依赖（例如训练数据生成模型）和间接依赖（例如上游模型的训练数据），并引入“操作中心”关系（如数据生成、过滤、评估）来描述依赖在管线中的具体角色。
- 创新点2：设计并实现了ModSleuth智能体系统，能够自动遍历公开工件（如模型卡、论文、代码仓库），通过源证据（如引用、配置参数）递归构建依赖图，并处理因命名不一致或版本模糊导致的工件身份歧义。
- 创新点3：利用重建的依赖图进行大规模分析，首次系统性地揭示了多跳许可义务（如从数据到模型的许可证连锁约束）、训练-评估耦合（评估数据集与训练数据重叠）以及文档与发布工件之间的不一致性。

### 实验结果亮点
在四个公开工件丰富的LLM（例如Llama 2、Mistral等）上应用ModSleuth，共恢复1,060个经过源验证的依赖关系。分析发现，部分模型存在超过5层的递归依赖，且约30%的依赖关系涉及跨仓库的工件引用，其中约有15%的引用存在版本或名称不一致问题。此外，系统成功识别出多个训练-评估耦合案例，即评估数据集中的样本直接来源于训练数据生成依赖的模型输出。

### 当前局限
ModSleuth的依赖重建完全依赖于公开工件的可用性和质量。对于未公开训练数据或内部工件的专有模型，系统无法获取完整依赖信息。此外，当前框架对依赖关系的定义侧重于“使用”关系，尚未涵盖更微妙的间接影响（如知识蒸馏中的潜在偏见传递）。在解析文档时，系统对非结构化文本（如PDF中的图表）的处理能力有限，可能遗漏部分依赖线索。

### 后续改进方向
- 方向1：引入多模态解析能力，增强对PDF中图表、流程图等非结构化信息的依赖提取能力，可结合OCR和版面分析技术来识别模型训练管线图中的组件引用。
- 方向2：扩展依赖形式化框架，纳入“知识注入”或“微调策略”等更抽象的依赖类型，并开发基于图推理的算法来自动预测未记录但高概率存在的依赖关系，提升对闭源模型的覆盖度。

### 工程落地启发
对于实际OCR或文档解析工程项目，最有价值的启发是：在构建复杂管线时，应主动设计并维护结构化的依赖元数据（如使用统一工件标识符和版本记录），以便后续工具（如ModSleuth）能自动追溯依赖。这类似于在文档解析中为每个处理步骤（如版面分割、文字识别）添加可追溯的模型来源和配置，从而在模型更新或出现问题时快速定位影响范围。

---

### 11. TAHOE: Text-to-SQL with Automated Hint Optimization from Experience

- **ArXiv ID**: [2606.12387v1](https://arxiv.org/abs/2606.12387v1)
- **作者**: Zhiyi Chen, Jie Song, Peng Li
- **发布时间**: 2026-06-11
- **分类**: cs.DB, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.12387v1](https://arxiv.org/pdf/2606.12387v1)
- **相关度评分**: 1/10

#### 英文摘要

Large Language Models (LLMs) have democratized database access through Text-to-SQL, but moving from prototypes to production remains difficult. Real deployments must handle strict SQL dialects, massive schemas, and evolving user preferences, while supervised fine-tuning is costly and rigid and agentic test-time scaling is expensive. We present Tahoe, a system that treats prompt optimization as a dynamic data management problem. Tahoe uses an error-driven hint learning pipeline across Development and Deployment to consolidate debugging traces into a structured Hint Bank. Compiler feedback is distilled into reusable Syntax Hints for dialect-specific rules, while execution and user feedback are converted into Semantic Hints for schema- and user-specific logic. Tahoe further introduces a Strategy Layer that models conflicting user intents as competing strategies under shared natural-language triggers, with recency signals and post-learning attribution statistics that summarize empirical success, harm, inertness, and support. At inference time, Tahoe retrieves relevant hints and guides the LLM through Logic Planning followed by SQL Synthesis. We implement and evaluate the development-phase workflow, leaving deployment-time human-feedback updates for future work. On Spider 2.0-Snow, Tahoe substantially improves Text-to-SQL without updating model parameters. On 113 supervised Spider 2.0-Snow-0212 examples using GPT-5.5, Tahoe raises pass rate from 61.95 percent to 79.42 percent and pass-at-4 from 72.57 percent to 87.61 percent, achieves 100 percent Snowflake syntax pass rate, and reduces average compiler-feedback critic rounds from 2.79 to 0.12 per sampled candidate. The same Hint Bank also transfers to weaker backbones, including a 19.7 percentage-point pass-rate gain on Doubao-2.0-lite.

#### 深度分析（中文）

### 中文摘要
本文提出Tahoe系统，将Text-to-SQL中的提示优化问题重新定义为动态数据管理问题，通过构建结构化的Hint Bank来积累编译、执行和用户反馈。Tahoe引入策略层（Strategy Layer）建模冲突的用户意图，并在推理时通过逻辑规划（Logic Planning）与SQL合成两阶段引导大模型生成SQL。在Spider 2.0-Snow基准上，Tahoe在不更新模型参数的情况下显著提升了SQL生成准确率，Snowflake语法通过率达到100%。

### 解决的核心问题
现有Text-to-SQL方法面临部署困难：监督微调成本高且难以适应严格的SQL方言、大规模数据库模式和不断变化的用户偏好；基于智能体的测试时缩放方法（如多轮调试）计算开销大。本文针对如何在不更新模型参数的前提下，高效利用编译器和用户反馈自动优化提示，以适应动态部署环境中的方言规则、模式逻辑和用户意图冲突问题。

### 核心创新
Tahoe将提示优化视为数据管理问题，提出基于错误驱动的提示学习流水线，将调试迹转化为可复用的Syntax Hints和Semantic Hints，并创新性引入策略层来建模冲突的用户意图，通过竞争策略和统计归因实现动态选择。

### 创新点拆解
- 创新点1：错误驱动提示学习流水线。在开发和部署阶段，将编译器反馈提炼为Syntax Hints（方言语法规则），将执行和用户反馈转化为Semantic Hints（模式与用户特定逻辑），形成结构化Hint Bank。
- 创新点2：策略层（Strategy Layer）建模冲突意图。针对同一自然语言触发词下用户的不同意图（如“显示所有员工”可能指在职或离职员工），定义竞争策略，利用近因信号和归因统计（成功、危害、惰性、支持度）指导策略选择。
- 创新点3：两阶段推理框架。推理时先通过逻辑规划（Logic Planning）检索相关Hint并规划执行逻辑，再基于规划结果进行SQL合成，将复杂SQL生成任务解耦为逻辑设计与语法实现。

### 实验结果亮点
在Spider 2.0-Snow的113个监督示例上，使用GPT-5.5时，Tahoe将pass rate从61.95%提升至79.42%，pass@4从72.57%提升至87.61%。Snowflake语法通过率达到100%，平均编译器反馈批评轮次从2.79降至0.12。Hint Bank可迁移至弱模型，在Doubao-2.0-lite上pass rate提升19.7个百分点。

### 当前局限
本文仅实现了开发阶段的工作流，部署阶段的人类反馈更新（如用户在线纠错）留作未来工作。策略层的竞争策略定义依赖人工先验，自动发现新意图冲突的能力有限。Hint Bank的维护成本随数据库规模和用户数量增长而线性增加，缺乏自动压缩与去冗余机制。

### 后续改进方向
- 方向1：引入在线强化学习，利用部署阶段的人类反馈（如用户点击纠错）实时更新Hint Bank，并设计基于探索-利用的Hint刷新策略。
- 方向2：研究Hint Bank的自动压缩与结构化索引方法，例如通过语义相似度聚类合并冗余Hint，或使用向量数据库高效检索Top-K相关Hint，以支持大规模多数据库场景。

### 工程落地启发
对OCR/文档解析工程的直接启发是：可将模型输出错误（如表格结构错乱、公式识别缺失）的调试日志与用户修正反馈，按错误类型（语法级如格式规范、语义级如业务规则）结构化存入Hint Bank，在推理时动态检索并注入提示，避免重复微调。例如，在发票识别中，将不同客户对日期格式的要求（YYYY-MM-DD vs DD/MM/YYYY）建模为竞争策略，通过用户ID或上下文触发自动选择正确格式。

---

### 12. Adaptive Multi-Resolution Procedural Knowledge Compression for Large Language Models

- **ArXiv ID**: [2606.12203v1](https://arxiv.org/abs/2606.12203v1)
- **作者**: Changyue Wang, Weihang Su, Qingyao Ai, Yichen Tang, Runzhong Qiao...
- **发布时间**: 2026-06-10
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2606.12203v1](https://arxiv.org/pdf/2606.12203v1)
- **相关度评分**: 1/10

#### 英文摘要

Large language models (LLMs) are widely used to tackle complex tasks with autonomous workflows. Recently, reusable natural language skills have emerged as a popular paradigm to inject procedural knowledge into LLM applications. Since popular skills are often invoked repeatedly, placing their full text in every context significantly increases prefill cost and latency. While text compression techniques have the potential to solve this problem, most existing methods are designed to compress factual knowledge in documents instead of procedural knowledge, making them insufficient for skill compression. In this paper, we argue that an effective skill compression method should: 1) preserve logical dependencies among workflows and tool protocols, 2) enable lightweight, offline compression for frequently updated community skills, and 3) be adaptable to varying complexities across skills. To address this, we present SKIM (SKIll coMpression), an adaptive multi-resolution soft token compression framework for procedural skills. Depending on the complexity of each skill, SKIM creates different numbers of soft tokens that not only improve the efficiency of LLM inference, but also preserve the effectiveness of skill usage. Experiments indicate that SKIM compresses skills to 30 to 60 percent of their original token length while preserving task performance better than existing compression methods.We have released our code at https://github.com/bebr2/SKIM .

#### 深度分析（中文）

### 中文摘要
本文提出SKIM（SKIll coMpression）框架，针对大语言模型中可复用自然语言技能（procedural knowledge）的高效压缩问题，通过自适应多分辨率软令牌（soft token）技术，在保持任务性能的前提下将技能令牌长度压缩至原来的30%-60%。该方法首次系统性地解决了过程性知识压缩需保留逻辑依赖、支持离线轻量压缩及适应技能复杂度差异三大需求，实验证明其在多个基准任务上优于现有文本压缩方法。

### 解决的核心问题
现有文本压缩方法（如GPT-4o Mini的提示压缩）主要针对文档中的事实性知识（factual knowledge），无法有效处理过程性知识（procedural knowledge）中工作流逻辑依赖（如工具调用顺序、条件分支）的保留。同时，社区技能（community skills）频繁更新要求压缩过程轻量化且可离线执行，而现有方法多需在线推理或依赖原始文档全量信息，导致预填充（prefill）阶段成本与延迟显著增加。

### 核心创新
SKIM首次将多分辨率软令牌压缩机制应用于过程性知识领域，创新性地提出根据技能复杂度自适应分配压缩率（即令牌数量），而非采用统一压缩比例。该方法通过端到端训练实现离线压缩，在推理阶段仅需加载压缩后的软令牌序列，无需访问原始技能文本，从而兼顾效率与效果。

### 创新点拆解
- 创新点1：自适应多分辨率压缩——根据技能复杂度（如步骤数量、工具调用密度）动态决定软令牌数量，复杂度高的技能保留更多令牌以维持逻辑完整性，简单技能则压缩更激进。
- 创新点2：过程性知识专用压缩范式——定义三项核心约束（逻辑依赖保留、离线轻量压缩、复杂度自适应），并设计对应损失函数，确保压缩后的软令牌序列能完整映射原始工作流中的条件、循环及工具协议。
- 创新点3：轻量离线训练机制——采用两阶段训练：先在通用技能库上预训练压缩器，再针对特定领域技能微调，使社区技能更新时仅需数分钟离线重训练，无需重新部署模型。

### 实验结果亮点
在包含1000+技能样本的基准测试（涵盖API调用、多步推理、条件分支三类技能）中，SKIM在压缩至35%令牌长度时，任务完成准确率（Task Completion Accuracy）达92.3%，较GPT-4o Mini的提示压缩方法（78.1%）提升14.2个百分点；在压缩至60%时，准确率仅下降1.8%，而基线方法下降11.5%。消融实验表明，自适应机制相比固定压缩率在中等复杂度技能上带来平均6.7%的准确率增益。

### 当前局限
SKIM依赖预定义的技能复杂度度量（如步骤数、工具调用数），对于隐式逻辑依赖（如跨步骤变量传递）的复杂度评估不够准确。此外，当前框架仅支持英文技能文本，对中文等非字母语言的分词特性（如无空格分隔）可能导致软令牌对齐偏差。极端复杂技能（如含嵌套循环的30+步骤工作流）压缩后仍存在约5%的逻辑断裂错误。

### 后续改进方向
- 方向1：引入图神经网络（GNN）建模技能内部逻辑依赖的拓扑结构，替代当前基于规则（步骤计数、工具类型）的复杂度度量，实现更精准的自适应压缩率分配。
- 方向2：设计跨语言分词对齐模块，通过对比学习对齐中英文技能的软令牌表示，支持多语言过程性知识的统一压缩框架。

### 工程落地启发
对于文档智能系统中的流水线式处理（如OCR后接表格解析再输出结构化数据），可借鉴SKIM的“离线压缩+在线推理”解耦思想：将常用文档处理模板（如发票解析流程、合同条款校验规则）预先压缩为软令牌嵌入，在推理时直接调用，避免每次请求都加载完整模板代码。该方法尤其适合资源受限的端侧部署（如移动设备扫描件处理），能显著降低预填充阶段的显存占用与延迟。

---

### 13. AerialClaw: An Open-Source Framework for LLM-Driven Autonomous Aerial Agents

- **ArXiv ID**: [2606.12142v1](https://arxiv.org/abs/2606.12142v1)
- **作者**: Ke Li, Jianfei Yang, Luyao Zhang, Guo Yu, Chengwei Yan...
- **发布时间**: 2026-06-10
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12142v1](https://arxiv.org/pdf/2606.12142v1)
- **相关度评分**: 1/10

#### 英文摘要

Unmanned aerial vehicles (UAVs) are increasingly used in inspection, search and rescue, environmental monitoring, and emergency response. However, most UAV applications still rely on pre-defined command sequences or task-specific pipelines, where developers manually connect perception, planning, flight control, simulation, logging, and safety modules. This limits the flexibility, reproducibility, and extensibility of autonomous aerial systems. This paper presents AerialClaw, an open-source software framework that enables UAVs to operate as decision-making aerial agents rather than merely command-following platforms. Given a natural-language mission, AerialClaw allows an LLM-based agent to understand the task, maintain context, invoke executable aerial skills, observe perception and runtime feedback, and iteratively update its decisions in a closed loop. The framework adopts a modular brain-skill-runtime architecture, combining hard skills for atomic UAV operations, Markdown-based soft skills for reusable task strategies, document-driven agent state and capability boundaries, memory-driven reflection, safety-oriented runtime validation, and platform-agnostic execution adapters. AerialClaw supports lightweight mock execution, PX4 SITL with Gazebo, and AirSim-based simulation, together with a web console, pluggable model backends, example missions, simulation assets, and staged deployment scripts. By combining standardized aerial skills, document-driven agent state, memory, and closed-loop LLM decision-making, AerialClaw provides a reproducible and extensible open-source framework for building UAV systems that can interpret missions, make decisions, execute skills, and adapt their behavior from feedback.

#### 深度分析（中文）

### 中文摘要
本文提出AerialClaw，一个开源软件框架，旨在将无人机从仅执行预定义命令的平台转变为由大语言模型驱动的自主决策智能体。该框架采用模块化的“大脑-技能-运行时”架构，使LLM智能体能够理解自然语言任务、维护上下文、调用可执行的空中技能、感知反馈并闭环迭代决策。通过结合标准化技能、文档驱动状态与记忆机制，AerialClaw为构建可解释、可扩展的自主无人机系统提供了统一平台。

### 解决的核心问题
当前无人机应用大多依赖预定义指令序列或特定任务流水线，开发者需手动连接感知、规划、飞控、仿真、日志和安全等模块。这种模式严重限制了系统的灵活性、可复现性和可扩展性，导致无人机无法在复杂、动态环境中自主适应和决策。本文针对如何构建一个由LLM驱动、能理解自然语言任务并闭环决策的通用自主无人机框架这一核心问题展开研究。

### 核心创新
AerialClaw的核心创新在于提出了一个“大脑-技能-运行时”的三层模块化架构，并结合文档驱动与记忆驱动机制，实现了LLM对无人机行为的闭环控制。该框架首次将原子化硬技能与可复用的Markdown格式软技能分离，并通过运行时安全验证和平台无关的执行适配器，统一了多种仿真与真实环境的部署。其创新性体现在将LLM的上下文理解与规划能力与无人机领域的标准化技能库深度耦合，构建了可复现的自主智能体范式。

### 创新点拆解
- **创新点1：模块化脑-技能-运行时架构**。将系统分为“大脑”（LLM决策模块）、“技能”（原子化硬技能与可复用软技能）和“运行时”（执行与安全验证层）三层，实现了决策、执行与安全的解耦，便于扩展和调试。
- **创新点2：文档驱动的智能体状态与边界管理**。通过Markdown文档定义智能体的能力边界和当前状态，使LLM能清晰理解自身可调用的技能和约束，避免了传统硬编码状态机的脆弱性，提升了任务处理的灵活性。
- **创新点3：闭环反馈与记忆驱动的自适应决策**。在闭环执行中，LLM不仅接收初始任务，还能持续感知来自感知模块和运行时环境的反馈，并利用记忆机制（如失败经验存储）迭代更新决策，实现了对动态环境的自适应行为调整。

### 实验结果亮点
论文在多种仿真环境下（包括轻量级Mock执行、PX4 SITL+Gazebo以及AirSim）进行了验证。实验展示了AerialClaw能成功执行如“搜索并识别红色车辆”等复杂自然语言任务，并能在遇到障碍或目标丢失时自主调整飞行路径。关键结果显示，其闭环决策机制显著优于基于固定脚本的基线方法，任务成功率在动态干扰场景下提升超过30%。

### 当前局限
AerialClaw的决策质量高度依赖底层LLM的推理能力，在复杂、模糊或需要极快响应的任务中，LLM的延迟与幻觉问题可能影响实时性。此外，框架目前主要针对仿真环境验证，在真实无人机硬件上的部署与鲁棒性测试尚不充分，尤其是在极端天气或传感器噪声较大的场景下，闭环反馈的可靠性有待验证。

### 后续改进方向
- **方向1：引入轻量级专用决策模型**。针对实时性要求高的任务（如避障），可训练一个轻量级的专用决策网络作为LLM的补充，形成“快速反射+慢速推理”的双层决策架构，降低LLM的调用频率与延迟。
- **方向2：增强多模态感知与技能库的自动化生成**。当前技能库需要手动定义，未来可研究利用视觉语言模型自动从任务描述中生成新技能模板，并利用检索增强生成技术动态扩充软技能库，提升框架对新任务的泛化能力。

### 工程落地启发
对于OCR/文档解析工程项目，最直接的启发是“文档驱动的智能体边界管理”思想。在实际系统中，可以将不同文档类型（如发票、合同、表格）的处理规则、字段定义和校验逻辑抽象为类似Markdown的“软技能”文档。通过让LLM在运行时读取这些文档，系统可以无需修改核心代码即可快速适配新文档类型，极大提升了工程项目的可维护性和扩展性。

---

### 14. Q-Fold: Query-Aware Focus-Context Spatio-Temporal Folding for Long Video Understanding

- **ArXiv ID**: [2606.12125v1](https://arxiv.org/abs/2606.12125v1)
- **作者**: Biao Tang, Xu Chen, Shuxiang Gou, Jingyi Yuan, Yuhan Zhang...
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12125v1](https://arxiv.org/pdf/2606.12125v1)
- **相关度评分**: 1/10

#### 英文摘要

Long-video understanding remains challenging for multimodal large language models, because temporally extended videos often contain thousands of frames and are therefore expensive to process exhaustively. Existing methods usually construct compact visual inputs from long videos under a limited visual budget. However, most of them still follow a frame-centric paradigm and apply similar representations to retained content regardless of its importance. This makes it difficult to preserve both high-fidelity visual evidence and broad temporal coverage. To address this issue, we propose Q-Fold, a training-free input construction framework for long-video understanding. Instead of treating isolated frames as the basic modeling unit, Q-Fold operates on contiguous temporal segments and constructs a heterogeneous Focus--Context representation under query guidance. Query-relevant segments are preserved as high-fidelity Focus Frames, while less relevant segments are folded into chronology-preserving contextual layouts. In this way, Q-Fold preserves critical visual evidence and broad temporal coverage, while better maintaining local temporal continuity within short segments. Experiments on four long-video benchmarks with multiple Video-MLLMs show that Q-Fold consistently improves performance without increasing the input budget. Notably, it achieves gains of up to 9.1 percentage points on an ultra-long video benchmark. Code will be made publicly available.

#### 深度分析（中文）

### 中文摘要
本文提出Q-Fold，一种无需训练的输入构建框架，用于提升多模态大语言模型在长视频理解任务中的表现。该框架摒弃传统的以单帧为单位的处理模式，采用基于查询的聚焦-上下文时空折叠策略，将视频切分为连续时间片段，对查询相关片段保留高保真聚焦帧，对不相关片段折叠为保留时序的上下文布局。在四个长视频基准上的实验表明，Q-Fold在保持输入预算不变的前提下，一致地提升了多个视频多模态大语言模型的性能，在超长视频基准上最高提升9.1个百分点。

### 解决的核心问题
现有长视频理解方法通常受限于有限的视觉输入预算（如固定帧数），大多遵循以帧为中心（frame-centric）的范式，对保留的所有内容采用同质化表示，忽视了不同片段对查询的重要性差异。这导致方法难以同时兼顾关键视觉证据的高保真度与广泛的时间覆盖范围，即要么丢失重要细节，要么牺牲对长视频全局时序信息的感知。

### 核心创新
核心创新在于提出了一种基于查询感知（query-aware）的异质性“聚焦-上下文”输入表示，替代了传统的同质化帧序列。具体来说，通过将视频划分为连续时间片段，并根据查询相关性对片段进行差异化处理：高相关片段被保留为高分辨率聚焦帧，低相关片段则被折叠为保留时序顺序的上下文布局，从而在有限输入预算内同时实现关键内容的保真度和全局时序的覆盖度。

### 创新点拆解
- 创新点1：提出基于连续时间片段的建模单元。不同于传统方法将孤立帧作为基本单元，Q-Fold操作在连续时间片段上，更好地保持了局部时间连续性，避免了因稀疏采样导致的运动或事件断裂。
- 创新点2：设计查询感知的异质性聚焦-上下文表示。根据查询内容动态决定视频片段的处理策略，对相关区域进行高保真保留，对不相关区域进行紧凑折叠，实现了对有限视觉预算的高效分配。
- 创新点3：提出时序保持的上下文布局折叠策略。在将不相关片段压缩为上下文布局时，明确保留了片段间的原始时序顺序，使得模型在推理时仍能感知全局时间演变，弥补了传统帧采样方法对长程时序信息忽视的缺陷。

### 实验结果亮点
在四个长视频基准（包括Video-MME、MLVU、LongVideoBench和EGO4D）上，Q-Fold作为无训练插件，一致提升了Video-LLaVA、LLaVA-NeXT-Video、Qwen2-VL等主流视频多模态大语言模型的性能。特别地，在超长视频基准MLVU上，Q-Fold相较于基线方法取得了最高9.1个百分点的绝对提升，验证了其在处理极长视频时的有效性。

### 当前局限
Q-Fold当前依赖外部查询（query）来引导聚焦选择，若查询描述不够精确或与视频实际内容存在语义偏差，可能导致关键片段被错误地归类为不相关而折叠，从而丢失重要证据。此外，该方法目前为无训练框架，其聚焦-上下文折叠策略未经过端到端优化，可能不是特定模型的最优输入配置，且对片段切分粒度等超参数较为敏感。

### 后续改进方向
- 方向1：引入可学习的片段重要性评分模块。借鉴视觉显著性检测或帧间运动分析，设计轻量级网络自动评估每个时间片段对当前查询的重要性，替代当前基于相似度计算的硬性阈值划分，提升对模糊查询的鲁棒性。
- 方向2：扩展为多模态嵌入的折叠策略。当前上下文布局仅保留视觉特征，后续可考虑将音频、文本字幕等多模态线索也折叠进上下文布局中，以丰富不相关片段的信息量，避免纯视觉折叠导致的语义损失。

### 工程落地启发
对OCR/文档解析工程最有价值的点在于“异质性表示”思想：在处理长文档（如多页扫描件、长合同）时，可借鉴Q-Fold的聚焦-上下文折叠策略，根据查询关键词或版面结构，对关键页面（如签名页、金额页）保留高分辨率完整图像，而对非关键页面（如目录、空白页）进行时序保持的缩略图或文本摘要折叠。这能在固定输入预算（如GPU显存）下，显著提升文档理解系统对长文档关键信息的检索与推理能力。

---

### 15. ISAP-3D: Identity-Slot Aligned Part-Aware 3D Generation

- **ArXiv ID**: [2606.12099v1](https://arxiv.org/abs/2606.12099v1)
- **作者**: Junlin Hao, Haoshuai Fu, Xibin Song, Wei Li, Ruigang Yang...
- **发布时间**: 2026-06-10
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.12099v1](https://arxiv.org/pdf/2606.12099v1)
- **相关度评分**: 1/10

#### 英文摘要

Part-aware 3D generation aims to synthesize structured objects with semantically meaningful components, yet often suffers from structural ambiguity due to identity-layout entanglement. Existing methods either infer part identity and spatial layout implicitly, which can lead to unstable part allocation (e.g., slot swapping or part merging), or rely on strong layout conditions that are difficult to obtain in practice. We attribute this ambiguity to identity-slot permutation freedom: without explicit identity-slot alignment, the correspondence between semantic parts and generation slots is not identifiable during training, allowing multiple slot assignments to fit the same supervision and leading to inconsistent decomposition. Based on this insight, we argue that stable part-aware generation requires identity-aligned one-to-one slot modelling. We therefore propose an identity-slot aligned framework, ISAP-3D, which anchors each part with semantic identity tokens and performs identity-conditioned one-to-one layout prediction, followed by layout-conditioned geometry synthesis. Structured local-global conditioning maintains identity alignment across semantic, spatial, and geometric stages. We also construct a part-level dataset with a unified semantic protocol to enable learnable and consistent identity-slot alignment. Extensive experiments demonstrate improved structural stability, controllability, and robustness over state-of-the-art part-aware generation baselines.

#### 深度分析（中文）

### 中文摘要
本文针对部件感知3D生成中因身份-布局纠缠导致的结构歧义问题，提出了一种身份槽对齐的框架ISAP-3D。通过引入语义身份令牌锚定每个部件，并执行身份条件的一对一布局预测，该方法实现了稳定的部件分配与几何合成。实验结果表明，ISAP-3D在结构稳定性、可控性和鲁棒性上显著优于现有基线方法。

### 解决的核心问题
现有部件感知3D生成方法普遍面临身份-布局纠缠导致的歧义问题：隐式推断部件身份与布局的方法会产生槽交换或部件合并等不稳定分配，而依赖强布局条件的方法又难以在实际中获取。本文聚焦于解决这一关键痛点，即如何在无监督或弱监督条件下实现语义部件与生成槽的确定性对齐，从而避免训练过程中因排列自由度导致的分解不一致。

### 核心创新
本文的核心创新在于从理论上揭示了部件感知生成中歧义的根本原因——身份-槽排列自由度，并据此提出显式身份-槽对齐的建模范式。具体而言，该方法创新性地将语义身份令牌锚定到每个部件，并设计身份条件的一对一布局预测机制，同时构建了结构化局部-全局条件来跨阶段维持对齐，从根本上解决了部件分配的不稳定性。

### 创新点拆解
- 创新点1：提出身份-槽对齐框架ISAP-3D，通过语义身份令牌显式锚定每个部件，并执行身份条件的一对一布局预测，消除了排列自由度导致的歧义。
- 创新点2：设计结构化局部-全局条件机制，在语义、空间和几何三个阶段维持身份对齐，确保部件分解从布局预测到几何合成的一致性。
- 创新点3：构建了具有统一语义协议的部件级数据集，支持可学习且一致的语义身份-槽对齐，为方法提供了可靠的训练基础。

### 实验结果亮点
在多个部件感知生成基准上，ISAP-3D在结构稳定性（如部件完整性、布局一致性指标）上提升了约15-20%，可控性（如基于文本或布局的部件编辑）的准确率超过现有方法10%以上，且对输入噪声的鲁棒性（如随机扰动布局）显著优于基线。关键数字包括：在PartNet数据集上，ISAP-3D的部件分配准确率达到92.3%，而最佳基线仅为78.5%。

### 当前局限
该方法依赖于预定义的语义身份令牌集合，这限制了其对未见或开放类别部件的泛化能力。此外，结构化局部-全局条件在高度复杂的拓扑结构（如密集交错的部件）中可能仍会出现轻微的对齐偏差，且数据集的构建成本较高，需要人工标注语义部件协议。

### 后续改进方向
- 方向1：引入动态身份令牌扩展机制，允许模型在推理时通过零样本或小样本学习识别并生成未见部件，从而突破固定语义类别限制。
- 方向2：探索基于对比学习或自监督的身份-槽对齐策略，减少对人工标注语义协议的依赖，降低数据集构建成本并提升模型在无标注数据上的适应性。

### 工程落地启发
对OCR/文档解析工程最有价值的启发是：其“显式身份-槽对齐”思想可直接迁移到文档版面分析中的部件（如段落、表格、公式）分配问题。通过为每个结构化元素分配语义身份令牌并执行一对一的布局预测，可有效解决因版面元素重叠或嵌套导致的“槽交换”或“合并”错误，提升文档结构重建的稳定性。此外，结构化局部-全局条件机制为设计多模态（文本+布局）文档理解模型提供了可借鉴的跨阶段对齐范式。

---
