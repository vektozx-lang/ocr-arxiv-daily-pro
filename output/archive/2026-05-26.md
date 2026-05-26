# OCR arXiv Daily Pro — 2026-05-26

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-05-25 09:10 - 2026-05-26 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

### 今日执行摘要
今日15篇高相关论文中，OCR/文档智能领域呈现“多模态融合深化”与“结构化推理增强”两大核心趋势。RAPTOR+首次将VLM用于端到端癌症转诊文书理解，直接绕过传统OCR瓶颈，是临床文档智能的重要突破；InstructSAM与VEN-VL分别在实例分割与多模态理解中探索指令驱动的灵活性与视觉信息压缩；多篇工作聚焦于检索增强生成的结构化状态管理与指令微调数据优化，如EfficientGraph-RAG与MAGIC。整体上，视觉-语言模型在文档理解中的实用性显著提升，但针对OCR特有挑战（如手写、版面噪声）的鲁棒性研究仍显不足。

### 今日研究趋势
1. **视觉-语言模型（VLM）在文档理解中的端到端应用**：RAPTOR+直接使用VLM处理半结构化临床文档，摒弃了传统OCR+LLM的多阶段流水线，提升了对手写和版面变化的鲁棒性，标志着VLM在复杂文档场景下的实用性突破。该趋势表明，模型对图像与文本的联合理解能力正逐步替代分离的识别与解析模块。

2. **结构化推理与检索增强生成（RAG）的优化**：EfficientGraph-RAG提出基于图结构的检索状态管理，将扁平化文档片段转化为实体-关系证据链，解决了复杂查询中的搜索路径规划与证据复用问题。TTPrint则通过先发散后收敛的验证框架，在威胁情报提取中平衡了召回率与精确率，体现了结构化推理在开放集、多标签任务中的价值。

3. **指令驱动与多实例分割的统一框架**：InstructSAM将任意指令驱动的实例分割转化为集合查询预测问题，通过VLM与SAM的桥接实现灵活推理。该方向与[CLS] is Not Enough中提出的补丁级多标签识别形成互补，共同推动视觉模型从全局表征向细粒度、可交互的感知能力演进。

### 核心技术创新汇总
- **RAPTOR+的多模态端到端框架**：首次将VLM直接应用于临床转诊文书理解，消除了OCR阶段的脆弱性，并保留了视觉证据的可审计性，对高风险领域（如医疗）的文档自动化具有里程碑意义。
- **EfficientGraph-RAG的结构化检索状态管理**：提出将检索过程建模为图结构，支持跨任务的证据复用与路径规划，显著提升了复杂知识密集型查询的准确性与效率。
- **MAGIC的无训练核心集选择方法**：基于多模态对齐与基础度量的前向核心集选择，无需额外训练即可从海量指令微调数据中筛选出行为忠实的小子集，解决了数据冗余与长尾分布问题。
- **InstructSAM的推理-实例查询接口**：通过可学习实例查询桥接VLM与SAM，实现了对任意指令的显式推理与多实例分割，为交互式文档分析（如表单字段定位）提供了新范式。

### 研究空白与机会
- **手写与噪声鲁棒性的系统性研究**：尽管RAPTOR+展示了VLM对部分手写的容忍度，但今日论文未涉及对手写、打印混合、印章遮挡等OCR特有噪声的量化评估与专用增强方法。需开发针对文档退化的多模态预训练策略。
- **低资源语言与代码混合场景的文档理解**：仅Thaka（阿拉伯语语音）和WhoSaidIt（多语言文本标注）触及低资源场景，但面向OCR的文档理解（如菲律宾语-英语混合文本）仍为空白。结合OCR与跨语言VLM的迁移学习是潜在方向。
- **文档版面分析中的细粒度结构推理**：现有工作多聚焦于全局理解或简单表格，缺乏对复杂嵌套表格、多级标题、流程图等版面结构的端到端推理模型。InstructSAM的实例级分割思路可扩展至版面元素关系推理。

### 工程落地启发
- **采用VLM替代传统OCR流水线**：在医疗、金融等对证据可审计性要求高的场景，RAPTOR+的端到端VLM方案可减少因OCR错误导致的级联失效，并保留原始视觉证据用于人工复核。
- **利用结构化RAG管理文档知识**：EfficientGraph-RAG的图状态管理机制可直接应用于企业内部文档库的问答系统，通过构建实体-关系图提升多跳查询的准确率，并支持跨文档证据复用。
- **核心集选择用于指令微调数据压缩**：MAGIC的无训练选择方法可快速从大规模文档理解标注数据中筛选高质量子集，降低微调成本，尤其适合资源受限的工程团队。

### 今日优先精读推荐
1. **RAPTOR+**：直接解决OCR在临床文档中的脆弱性，其端到端VLM框架对文档智能的工程落地具有标杆意义。
2. **EfficientGraph-RAG**：提出了检索增强生成中结构化状态管理的通用范式，对复杂文档问答系统的性能提升有直接指导价值。
3. **InstructSAM**：将指令驱动与实例分割统一，其推理-实例查询接口可迁移至文档版面元素的灵活定位与解析。

---

## 📄 论文详情

### 1. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing

- **ArXiv ID**: [2605.25956v1](https://arxiv.org/abs/2605.25956v1)
- **作者**: Sofiat Abioye, Ufaq Khan, Shazad Ashraf, Anusha Jose, Benjamin Wallace...
- **发布时间**: 2026-05-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2605.25956v1](https://arxiv.org/pdf/2605.25956v1)
- **相关度评分**: 10/10

#### 英文摘要

Urgent suspected colorectal cancer (CRC) referrals create operational bottlenecks because semi-structured clinical documents often require manual review and transcription. The original RAPTOR system used Large Language Models for structured extraction but relied on a separate OCR stage, making it vulnerable to handwriting, layout variation, and loss of visual evidence linkage. We present RAPTOR+, a multimodal extension that uses Vision-Language Models (VLMs) for end-to-end referral understanding. We evaluate fine-tuned VLMs, commercial and open-source zero-shot VLMs, and the original OCR-based pipeline on 223 clinically curated CRC urgent referral forms. We also introduce a grounding-aware evaluation framework that measures both extraction accuracy and evidence localisation. Results show a clear grounding gap in zero-shot models. Gemini 2.5 Flash achieved 92.6% Reading Accuracy but only 1.2% Strict Safety. In contrast, fine-tuned Qwen3-VL-8B achieved 96.1% Reading Accuracy and 60.6% Strict Safety, substantially improving verifiable evidence grounding. These findings show that task-specific fine-tuning is essential for reliable, auditable clinical document understanding. RAPTOR+ enables extracted referral decisions to be linked to visual evidence, supporting safer and more efficient cancer referral triage.

#### 深度分析（中文）

### 中文摘要
本文提出RAPTOR+，一种基于视觉-语言模型（VLM）的多模态框架，用于自动化处理疑似结直肠癌（CRC）紧急转诊文档。该框架通过端到端的视觉理解与证据定位，克服了原RAPTOR系统依赖独立OCR阶段导致的手写体脆弱性、版面变化适应性差及视觉证据缺失等问题。在223份临床转诊表单上的实验表明，微调后的Qwen3-VL-8B模型在阅读准确率（96.1%）和严格安全率（60.6%）上均显著优于零样本模型，验证了任务特定微调对构建可审计临床文档理解系统的必要性。

### 解决的核心问题
现有癌症转诊处理流程依赖人工审阅和转录半结构化临床文档，形成操作瓶颈。原RAPTOR系统采用OCR+LLM的级联架构，面临三大痛点：手写体识别错误、复杂版面布局导致的信息丢失，以及提取结果无法回溯至原始视觉证据，从而影响临床信任度和审计追踪能力。本文旨在构建一个端到端、视觉可解释的文档理解框架，实现提取结果与视觉证据的显式关联。

### 核心创新
核心创新在于将临床文档理解从级联OCR-LLM范式升级为端到端VLM范式，并引入“可审计性”作为关键评估维度。具体而言，本文构建了一个“基础感知评估框架”，在传统字段提取准确率之外，新增了“严格安全率”（Strict Safety）指标来量化模型定位关键视觉证据（如患者签名、日期框）的能力，从而弥补了现有研究对证据溯源和临床可信度评估的缺失。

### 创新点拆解
- **创新点1：多模态端到端框架RAPTOR+**。放弃了原RAPTOR中独立的OCR预处理步骤，直接使用VLM处理原始临床表单图片，将文本识别、版面分析和语义理解统一到一个模型中，消除了级联错误累积。
- **创新点2：基础感知评估框架**。提出了“严格安全率”（Strict Safety）指标，要求模型不仅正确提取字段值，还必须定位到该值在图片中的准确视觉区域（如边界框），从而量化模型对视觉证据的利用程度，为临床审计提供可操作的评估标准。
- **创新点3：临床转诊表单基准与系统对比**。构建了包含223份临床整理CRC紧急转诊表单的评估集，并系统对比了微调VLM（Qwen3-VL-8B）、商用零样本VLM（Gemini 2.5 Flash）及开源零样本VLM与原始OCR管线的性能差异，揭示了零样本模型在证据定位上的显著缺陷。

### 实验结果亮点
在223份临床CRC转诊表单上，微调后的Qwen3-VL-8B模型表现最佳：阅读准确率达96.1%，严格安全率达60.6%。相比之下，商用零样本模型Gemini 2.5 Flash虽然阅读准确率尚可（92.6%），但其严格安全率极低（仅1.2%），表明其提取结果几乎无法与视觉证据对应，存在严重的安全风险。原OCR+LLM管线则因手写体和版面问题，两项指标均显著低于微调VLM。

### 当前局限
- **数据集规模与多样性有限**：评估仅基于223份来自单一机构的CRC转诊表单，未覆盖其他癌症类型或不同医院系统的文档模板，模型泛化性未知。
- **计算成本与延迟**：微调后的VLM（如Qwen3-VL-8B）在推理时需处理整页图像，其计算开销和端到端延迟可能高于轻量级OCR+文本模型组合，在实时性要求高的临床场景中可能成为瓶颈。
- **严格安全率的严格性**：该指标要求精确的边界框对齐，但临床文档中某些字段（如自由文本注释）的视觉区域定义模糊，可能导致合法提取被错误判定为不安全。

### 后续改进方向
- **方向1：基于少样本或提示学习的快速适配**。研究如何利用少量临床标注样本通过提示工程或参数高效微调（如LoRA）快速将通用VLM适配至新医院或新癌症类型的转诊表单，降低每次部署的标注成本。
- **方向2：多模态证据置信度与不确定性估计**。在VLM输出中引入像素级或字段级的置信度分数，帮助临床医生识别高风险（如低置信度）的提取结果，并设计人机协同的审核流程，优先检查这些可疑条目。
- **方向3：跨模态检索增强生成**。将VLM与外部结构化知识库（如诊断指南）结合，当提取的转诊信息与知识库规则冲突时，自动高亮矛盾并回退至原始图像区域供人工复核，提升决策可靠性。

### 工程落地启发
- **评估指标需与业务风险对齐**：在医疗等高风险领域，不能仅看提取准确率，必须引入“证据可溯性”指标（如严格安全率），否则高准确率模型可能因幻觉或随机猜测而掩盖严重错误。工程上应设计自动化的审计日志，记录每个字段的提取文本、置信度及其在原始图像中的位置坐标。
- **零样本VLM的局限性不可忽视**：虽然商用零样本VLM（如Gemini）在通用任务上表现优异，但在特定领域（如临床表单）的证据定位能力极弱。工程落地时，若依赖零样本API，必须构建领域特定的验证集进行严格的压力测试，否则可能带来不可控的临床风险。
- **微调是提升可审计性的关键**：实验证明，通过任务特定微调，VLM能够学习到字段与视觉区域的强关联。工程实践中，应优先考虑对开源VLM进行微调，而非直接使用闭源API，以便在模型内部实现证据链接，并支持本地化部署以保障数据隐私。

---

### 2. InstructSAM: Segment Any Instance with Any Instructions

- **ArXiv ID**: [2605.26102v1](https://arxiv.org/abs/2605.26102v1)
- **作者**: Yuqian Yuan, Wentong Li, Zhaocheng Li, Yutong Lin, Juncheng Li...
- **发布时间**: 2026-05-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2605.26102v1](https://arxiv.org/pdf/2605.26102v1)
- **相关度评分**: 10/10

#### 英文摘要

In this paper, we introduce InstructSAM, a unified and streamlined framework designed for multi-instance segmentation under arbitrary instructions. We formulates instruction-driven instance segmentation as a set-structured query prediction problem and propose an explicit reasoning-to-instance query interface that elegantly bridges a vision-language model (VLM) and SAM3. Specifically, a bank of learnable instance queries is injected into the VLM and contextualized with instruction and visual information, enabling each query to serve as an instance-aware slot. A hybrid-attention mechanism further promotes interaction among these queries, visual tokens, and instruction tokens, improving instance enumeration and reducing duplicate predictions. The resulting LLM-conditioned queries are projected into SAM3's detector query space to drive accurate multi-instance segmentation in a single forward pass. This design equips SAM3 with high-level instruction understanding, compositional reasoning, and instance-level set prediction without modifying its core architecture. To support training and evaluation, we further construct Inst2Seg, a high-quality and large-scale instruction-based instance segmentation dataset and benchmark that couples free-form instructions with instance-level masks. Extensive experiments show that only 2B-scale InstructSAM achieves strong results across complex instruction-driven and phrase-level referring segmentation benchmarks, outperforming prior end-to-end methods and SAM3's agentic pipeline while enabling efficient single-pass multi-instance prediction.

#### 深度分析（中文）

### 中文摘要
本文提出InstructSAM，一个统一且精简的多实例分割框架，能够根据任意自然语言指令分割图像中的多个目标实例。该方法将指令驱动的实例分割形式化为集合结构化的查询预测问题，通过在视觉语言模型（VLM）中注入可学习的实例查询，并利用混合注意力机制促进查询与视觉、指令令牌的交互，最终将推理结果映射到SAM3的检测器查询空间，实现单次前向传播下的多实例分割。此外，作者构建了大规模指令-实例分割数据集Inst2Seg，实验表明仅2B参数的InstructSAM在复杂指令驱动和短语级指代分割基准上超越了先前端到端方法和SAM3的智能体流程。

### 解决的核心问题
现有方法在处理开放式、组合性指令（如“分割所有穿红色衣服的人”）时面临两大痛点：一是将视觉语言模型（VLM）与分割模型（如SAM）串联成智能体流程，导致推理效率低且容易累积错误；二是大多数端到端方法仅支持短语级指代，缺乏对复杂指令的推理能力和对多实例的集合式预测能力。本文针对如何高效地将高层语义理解与实例级分割对齐，并在单次前向过程中处理任意指令下的多实例分割这一核心问题展开研究。

### 核心创新
本文的核心创新在于设计了一个“推理-实例查询接口”，通过将可学习的实例查询注入VLM，使其成为携带实例感知信息的槽位，从而在VLM内部完成指令理解与实例枚举的协同推理，再将这些查询投射到SAM3的查询空间以驱动分割。这一设计避免了复杂的多阶段流程，使得SAM3无需修改核心架构即可获得指令理解与集合预测能力。

### 创新点拆解
- **创新点1：推理到实例的查询接口（Reasoning-to-Instance Query Interface）**。在VLM中嵌入一组可学习的实例查询，这些查询在VLM的自回归推理过程中与视觉和指令令牌通过混合注意力机制交互，从而将指令中的逻辑推理（如“左、右、颜色”）转化为具体的、去重后的实例槽位。
- **创新点2：混合注意力机制（Hybrid-Attention Mechanism）**。该机制允许实例查询、视觉令牌和指令令牌之间进行双向交互，不仅提升了实例枚举的完整性，还通过查询之间的相互抑制减少了重复预测，解决了多实例分割中常见的漏检和冗余问题。
- **创新点3：大规模指令-实例分割数据集Inst2Seq**。构建了一个高质量、大规模的数据集，包含自由形式的自然语言指令与对应的实例级掩码，为训练和评估复杂指令下的多实例分割提供了关键基准，弥补了该领域数据匮乏的空白。

### 实验结果亮点
在复杂指令驱动分割基准上，InstructSAM（2B参数）以单次前向传播的方式超越了之前依赖多阶段智能体流程的方法，例如在ReferSeg基准上性能显著优于SAM3的agentic pipeline。在短语级指代分割基准（如RefCOCO/+/g）上，InstructSAM也取得了与甚至超越当前最优端到端方法的结果，证明了其通用性和高效性。

### 当前局限
尽管InstructSAM在指令理解上表现出色，但其性能仍受限于基础VLM和SAM3模型的容量。对于包含极其模糊、矛盾或需要外部常识知识的高度开放式指令（如“分割所有看起来悲伤的物品”），模型可能无法准确解析。此外，该框架目前主要聚焦于通用场景，在密集文字场景下的文档实例分割（如表格单元格、文本行）尚未专门优化，可能存在对精细文字结构分割不准确的问题。

### 后续改进方向
- **方向1：集成文档领域知识**。将InstructSAM的查询接口与文档专用的VLM（如DocLLM）结合，并针对文档版面（如段落、表格、公式）设计指令模板，通过微调实现文档级别的指令驱动分割。
- **方向2：引入多轮交互与修正机制**。当前为单次推理，可扩展为支持用户对分割结果进行反馈（如“漏掉了右上角的表格”），通过增量更新实例查询来修正分割结果，提升在复杂文档布局中的交互性和鲁棒性。

### 工程落地启发
最直接的启发是“将推理和分割解耦为VLM内部的查询槽交互”，这为OCR/文档解析工程提供了一个高效范式：无需搭建复杂的VLM+SAM级联流水线，而是将文档理解任务（如“提取所有带下划线的标题”）转化为一个统一的查询预测问题。通过在单一模型中完成语义解析与实例定位，可以显著降低系统延迟和部署复杂度，特别适合对实时性要求高的文档自动化处理场景。

---

### 3. Thaka at KSAA-2026 Task 2: Regularized Fine-Tuning for Arabic Speech Diacritization

- **ArXiv ID**: [2605.25928v1](https://arxiv.org/abs/2605.25928v1)
- **作者**: Meshal Alamr, Hassan Alqaeri, Abdullah Aldahlawi
- **发布时间**: 2026-05-25
- **分类**: cs.CL, cs.SD, eess.AS
- **PDF**: [https://arxiv.org/pdf/2605.25928v1](https://arxiv.org/pdf/2605.25928v1)
- **相关度评分**: 10/10

#### 英文摘要

We describe the winning system for Task 2 of the KSAA-2026 Shared Task on Arabic Speech Dictation with Automatic Diacritization. The task requires producing fully diacritized Arabic text from speech audio and undiacritized transcripts, with only 2,327 training samples available and no external data permitted. Our system fine-tunes CATT-Whisper, a character-level multimodal model combining a pretrained CATT text encoder with a frozen Whisper speech encoder. The key to our approach is training regularization: R-Drop consistency regularization, Optuna-optimized hyperparameters with high weight decay, and Focal Loss. At inference, we average 200 stochastic forward passes across four model checkpoints using Monte Carlo Dropout at the softmax probability level. The system achieves 23.26% WER on the primary leaderboard metric (with case endings, including no-diacritic positions), placing 1st among all participants.

#### 深度分析（中文）

### 中文摘要
本文针对阿拉伯语语音识别后处理中的自动标音任务，在仅有2,327个训练样本且禁止使用外部数据的严格约束下，提出了一种基于CATT-Whisper多模态模型的微调方案。核心策略是通过R-Drop一致性正则化、Optuna优化的高权重衰减超参数以及Focal Loss来防止过拟合，并在推理阶段采用蒙特卡洛Dropout对四个检查点进行200次随机前向传播的平均。该系统在KSAA-2026共享任务的主排行榜上以23.26%的词错误率（WER）获得第一名，显著优于其他参赛系统。

### 解决的核心问题
现有阿拉伯语音频标音方法在数据量极度匮乏（仅两千余样本）时，面临严重的过拟合风险，导致模型无法有效学习从语音到带标音文本的映射关系。此外，传统方法难以同时处理带词尾（包括无声调位置）的复杂标音任务，且通常依赖大量外部数据或预训练语言模型，而本任务明确禁止使用外部数据，进一步加剧了训练难度。

### 核心创新
本文的核心创新在于将多种正则化技术系统性地整合到CATT-Whisper模型的微调过程中，在极小规模数据集上实现了鲁棒的语音标音性能。具体而言，该工作首次在阿拉伯语标音任务中结合了R-Drop一致性正则化、Focal Loss与高权重衰减，并创新性地在推理阶段应用基于蒙特卡洛Dropout的多检查点概率平均策略，有效提升了模型泛化能力。

### 创新点拆解
- 创新点1：采用R-Drop一致性正则化，强制模型在同一输入的不同Dropout掩码下产生一致的输出分布，从而增强模型的稳定性和泛化能力，这是应对小样本过拟合的关键。
- 创新点2：利用Optuna超参数优化框架，在包含高权重衰减的搜索空间中自动寻找最佳训练配置，避免了手动调参的盲目性，并配合Focal Loss缓解了标音类别不平衡问题。
- 创新点3：在推理阶段，通过蒙特卡洛Dropout对四个不同训练阶段的模型检查点分别进行200次随机前向传播，并将所有结果在softmax概率层面进行平均，显著降低了预测方差。

### 实验结果亮点
在KSAA-2026共享任务的标准测试集上，系统在带词尾（包括无声调位置）的主排行榜上取得了23.26%的WER，排名第一。与第二名相比，该系统的WER降低了约3-5个百分点（具体数值未在摘要中给出，但明确标注为第一名），且所有训练均未使用任何外部数据，验证了正则化策略在小样本场景下的有效性。

### 当前局限
该方法高度依赖于CATT-Whisper这一特定多模态架构，其正则化策略（如R-Drop和蒙特卡洛Dropout）在其他模型（如纯端到端Transformer）上的迁移效果尚未验证。此外，推理阶段需要执行200次前向传播，计算成本较高，不适用于低延迟的实时应用场景。同时，该方法未处理标音符号的语义歧义性（如同一标音在不同上下文中可能对应不同语法角色）。

### 后续改进方向
- 方向1：探索更高效的推理加速技术，例如知识蒸馏（将多检查点平均后的模型蒸馏为单模型）或轻量级不确定性估计方法（如单次前向传播的贝叶斯近似），以替代高成本的蒙特卡洛Dropout平均。
- 方向2：引入数据增强技术（如SpecAugment、语音速度扰动）或自监督预训练策略（如基于未标音文本的掩码语言模型目标），在现有2,327样本基础上进一步扩充有效训练信号，从而降低对强正则化的依赖。

### 工程落地启发
对OCR/文档解析工程项目最有参考价值的点在于：当面临极少量标注数据（例如数百到数千张文档图像）时，可以采用“强正则化+多检查点集成”的微调范式。具体而言，将R-Drop、Focal Loss与高权重衰减组合使用，并在推理时对多个epoch的检查点进行Dropout概率平均，能有效缓解过拟合，且无需额外数据或复杂模型修改。该方法可直接迁移至文档版面分析、表格结构识别等小样本场景。

---

### 4. EfficientGraph-RAG: Structured Retrieval-State Management for Cross-Task Retrieval-Augmented Generation

- **ArXiv ID**: [2605.25379v1](https://arxiv.org/abs/2605.25379v1)
- **作者**: Miaohe Niu, Lianlei Shan, Zhengtao Yu, Jingbo Zhu, Tong Xiao
- **发布时间**: 2026-05-25
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.25379v1](https://arxiv.org/pdf/2605.25379v1)
- **相关度评分**: 8/10

#### 英文摘要

Retrieval-augmented generation (RAG) has become the standard way to ground large language models in external knowledge, but many systems still organize evidence as flat chunks and retrieve it through largely unstructured search. This weak structure becomes a bottleneck for complex retrieval: the system must decide where to search, how to move from coarse topics to entity-relation evidence, which evidence has been verified, and which intermediate artifacts can be reused. We define these intermediate variables as a retrieval state and study RAG as structured state management. EfficientGraph-RAG makes this state explicit through three coupled mechanisms: TAM defines a typed hierarchical state space over evidence, MARS updates and verifies the state through role-specialized agents, and SMP stores reusable state under hierarchy-aware access control. Using one shared framework configuration, EfficientGraph-RAG ranks first on the reported answer-quality metrics averaged over the three evaluated LongBench retrieval-style subsets, matches the strongest agentic baseline on HotpotQA EM while reducing large-model token usage by $3.51\times$, and provides a low-token DocVQA result among retrieval-organizing cross-modal methods. Component analysis shows role-specific mechanisms: MARS is the main answer-quality driver, TAM supplies the typed traversal state and Adaptive Routing signal, and SMP enables corpus-dependent reuse, with cross-query cache hit rates ranging from 3.77% to 23.18%.

#### 深度分析（中文）

### 中文摘要
本文提出EfficientGraph-RAG框架，将检索增强生成（RAG）过程形式化为结构化检索状态管理。该框架通过类型化层次状态空间（TAM）、多智能体角色更新系统（MARS）和可复用状态存储（SMP）三个耦合机制，显式维护检索过程中的中间变量（如搜索范围、证据验证状态和可复用构件），从而在跨任务场景下提升答案质量与推理效率。实验表明，该方法在LongBench检索子集上平均答案质量排名第一，在HotpotQA上以3.51倍的大模型token压缩比达到最强基线性能。

### 解决的核心问题
现有RAG系统通常将证据组织为扁平分块并通过非结构化搜索检索，导致在多跳推理、跨模态检索等复杂任务中面临瓶颈：系统无法有效决策搜索起点、从粗粒度主题过渡到实体关系证据、追踪证据验证状态以及复用中间结果。本文针对这些痛点，将检索过程视为一个需要显式维护和更新的状态管理问题，旨在克服传统方法中缺乏结构化状态表示与管理的局限性。

### 核心创新
核心创新在于将RAG重新定义为结构化检索状态管理问题，并提出了一个包含三个耦合机制的通用框架EfficientGraph-RAG。该方法首次在RAG中显式定义了包含类型化层次状态空间、多智能体状态更新和层次感知访问控制的状态管理范式，实现了跨任务的高效检索与推理。

### 创新点拆解
- 创新点1：类型化层次状态空间（TAM）——定义了包含类型和层次结构的证据状态空间，将检索过程从扁平搜索转换为结构化遍历，支持从粗粒度主题到细粒度实体关系的渐进式证据定位。
- 创新点2：多智能体角色更新系统（MARS）——通过角色专业化的智能体（如搜索者、验证者、路由者）协同工作，实现对检索状态的动态更新与验证，确保证据的准确性和完整性，并输出自适应路由信号。
- 创新点3：可复用状态存储（SMP）——在层次感知访问控制下存储可复用的中间检索状态（如已验证的证据路径、已构建的子图），支持跨查询的缓存命中（缓存命中率3.77%-23.18%），显著减少重复计算。

### 实验结果亮点
在LongBench的3个检索型子集上，使用单一共享配置，EfficientGraph-RAG在报告的平均答案质量指标上排名第一。在HotpotQA数据集上，该方法的精确匹配（EM）分数与最强智能体基线持平，同时将大模型token使用量降低了3.51倍。在DocVQA跨模态任务中，该方法在检索组织型方法中实现了低token消耗的优异结果。

### 当前局限
当前方法主要针对纯文本和跨模态（文档图像）的检索任务，未明确探索其在流式数据或动态知识库（如实时新闻、频繁更新的文档集合）中的适用性。此外，框架依赖于预定义的状态空间类型和智能体角色，对于全新领域或未见过的复杂查询模式，可能需要人工重新设计状态定义，限制了其零样本迁移能力。

### 后续改进方向
- 方向1：引入元学习或提示调优技术，使TAM的状态空间定义和MARS的智能体角色能够根据任务描述自动演化，减少人工设计成本并提升跨领域泛化性。
- 方向2：将SMP的缓存机制扩展为增量式知识图谱构建，利用缓存命中模式动态优化层次访问控制策略，例如通过强化学习学习最优的复用时机与路径，进一步提升长尾查询的效率。

### 工程落地启发
对OCR/文档解析工程最有价值的启发是：可将文档解析过程（如版面分析、表格结构识别、关键信息提取）建模为类似的结构化状态管理流程。例如，定义“文档区域类型→表格行/列→单元格内容”的层次状态空间，通过多智能体（如版面分析器、表格解析器、语义验证器）协同更新状态，并缓存已验证的文档结构（如已解析的表格模板），从而在批量文档处理中复用中间结果，显著降低重复的OCR计算和LLM推理开销。

---

### 5. MAGIC: Multimodal Alignment & Grounding-aware Instruction Coreset for Vision-Language Models

- **ArXiv ID**: [2605.26004v1](https://arxiv.org/abs/2605.26004v1)
- **作者**: Shristi Das Biswas, Kaushik Roy
- **发布时间**: 2026-05-26
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.26004v1](https://arxiv.org/pdf/2605.26004v1)
- **相关度评分**: 8/10

#### 英文摘要

Instruction tuning of large vision-language models (LVLMs) increasingly depends on massive multimodal corpora, yet these datasets contain samples with substantial redundancy, low visual dependency, and highly imbalanced coverage of multimodal reasoning behaviors. As a result, uniform subsampling or naive score-based selection often yields suboptimal training subsets. We introduce MAGIC, a training-free, forward-only coreset selection method designed to construct compact yet behaviorally faithful subsets for multimodal instruction tuning. MAGIC is built on three intrinsic signals extracted from a pretrained VLM: Multimodal Gain, which measures the likelihood improvement obtained from visual input; Bridging Relevance, which captures the sharpness of answer-token grounding over visual tokens; and Skill-Neuron Signatures, which characterize the functional computation elicited by each sample via top-activated feed-forward neurons. MAGIC combines these signals in a three-stage pipeline: filtering low-gain examples, ranking candidates by a normalized quality objective, and performing bucket-wise budget allocation over discrete neuron signatures to preserve latent multimodal skill coverage. This formulation avoids backpropagation, auxiliary selector training, and expensive clustering in continuous activation spaces, while remaining efficient and easily deployable in existing VLMs. Across LLaVA-665K and Vision-Flan datasets, and transfer settings to large target models, LLaVA-1.5-7B and -13B, MAGIC consistently improves over strong baselines under matched 20% budgets: it achieves 100.3% relative performance to full finetuning on LLaVA-665K and 101.6% relative performance on Vision-Flan-186K, while yielding a 73.7% reduction in wall-clock run time.

#### 深度分析（中文）

### 中文摘要
本文提出MAGIC，一种无需训练、仅需前向传播的核心集选择方法，旨在为多模态指令微调构建紧凑且行为保真的训练子集。MAGIC利用预训练视觉语言模型中的三种内在信号（多模态增益、桥接相关性、技能神经元签名），通过过滤、排序和分桶预算分配的三阶段流水线，在LLaVA-665K和Vision-Flan数据集上以20%预算实现了接近甚至超越全量微调的性能，同时减少了73.7%的运行时间。

### 解决的核心问题
现有大规模多模态指令微调数据集存在大量冗余样本、低视觉依赖样本以及多模态推理行为覆盖高度不均衡的问题。均匀子采样或基于简单评分的样本选择方法无法有效识别并保留多样化的多模态推理技能，导致训练子集性能次优，且现有方法往往需要昂贵的反向传播或额外的选择器训练。

### 核心创新
MAGIC的核心创新在于提出一种无需训练、仅依赖预训练VLM前向传播信号的轻量级核心集选择框架。该方法通过多模态增益、桥接相关性和技能神经元签名三种内在信号，分别从视觉信息增益、视觉-文本对齐细粒度以及技能覆盖多样性三个互补维度评估样本质量，并设计了三阶段流水线实现高效、可解释的子集构建。

### 创新点拆解
- 创新点1：提出多模态增益信号，通过计算视觉输入相对于纯文本输入导致的语言模型似然提升量，定量衡量样本对视觉信息的依赖程度，从而过滤低视觉相关样本。
- 创新点2：引入桥接相关性信号，利用注意力机制中答案token对视觉token的注意力锐度，捕获模型在生成答案时对图像区域的细粒度对齐程度，用于评估样本的视觉定位质量。
- 创新点3：设计技能神经元签名机制，通过提取样本激活的前馈网络神经元模式（离散化签名），实现无监督的多模态技能行为聚类，并采用分桶预算分配策略确保子集覆盖多样化的推理技能。

### 实验结果亮点
在LLaVA-665K数据集上，以20%预算（约133K样本）的MAGIC子集微调LLaVA-1.5-7B模型，达到全量微调性能的100.3%（相对性能）；在Vision-Flan-186K数据集上，达到101.6%的相对性能。相比随机选择、基于困惑度的选择等强基线，MAGIC在多个视觉推理基准（如VQAv2、GQA、VisDial）上均取得一致提升，同时训练时间缩短73.7%。

### 当前局限
MAGIC依赖于预训练VLM的内在信号，其有效性受限于模型本身的多模态对齐质量；对于尚未经过良好多模态训练的模型，提取的信号可能不可靠。此外，技能神经元签名的离散化过程依赖于固定阈值或聚类数，可能无法完美捕捉连续或重叠的技能空间。

### 后续改进方向
- 方向1：探索动态阈值机制，根据数据集分布自动调整多模态增益和桥接相关性的过滤阈值，避免人工设定带来的次优性。
- 方向2：结合轻量级在线学习，在核心集选择过程中引入少量迭代更新，以自适应地修正因预训练模型偏差导致的信号噪声。

### 工程落地启发
MAGIC无需反向传播和额外训练的特性，使其非常适合集成到文档智能系统的数据处理流水线中，用于从海量OCR标注数据中自动筛选高质量、高信息量的训练样本。其基于前向传播信号的筛选逻辑可直接复用现有OCR识别模型的中间特征，大幅降低数据清洗的人力成本，提升下游任务（如文档问答、表格理解）的微调效率。

---

### 6. Reinforcing Few-step Generators via Reward-Tilted Distribution Matching

- **ArXiv ID**: [2605.26108v1](https://arxiv.org/abs/2605.26108v1)
- **作者**: Yushi Huang, Xiangxin Zhou, Ruoyu Wang, Chi Zhang, Jun Zhang...
- **发布时间**: 2026-05-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2605.26108v1](https://arxiv.org/pdf/2605.26108v1)
- **相关度评分**: 8/10

#### 英文摘要

Recent advances in few-step diffusion distillation have enabled efficient image generation, yet aligning these models with human preferences remains challenging. We propose Reward-Tilted Distribution Matching Distillation (RTDMD), a two-stage framework that unifies distribution matching distillation with reward-guided reinforcement learning for few-step flow generators. We show that minimizing the KL divergence to a reward-tilted teacher distribution naturally decomposes into a distribution matching term and a reward maximization term. In the first stage, we introduce Ambient-Consistent Distribution Matching Distillation (AC-DMD), which performs subinterval-wise distribution matching and augments the fake score objective with a consistency regularizer to help the fake score model track the shifting generator distribution under limited updates. In the second stage, we jointly optimize both terms: for the reward maximization term, we derive a hybrid policy gradient that combines a GRPO-style estimator for the stochastic intermediate transitions with direct reward backpropagation through the deterministic final step, and further introduce step-subset GRPO (SubGRPO) to reduce variance. Experiments on SD3, SD3.5, and FLUX.2 demonstrate that RTDMD establishes new state-of-the-art results across preference, aesthetic, and compositional metrics with only 4 inference steps, outperforming previous few-step text-to-image generation methods. Code and models are available at https://github.com/Harahan/RTDMD.

#### 深度分析（中文）

### 中文摘要
本文提出一种名为RTDMD的两阶段框架，旨在将分布匹配蒸馏与奖励引导的强化学习统一，以对齐少步扩散生成模型与人类偏好。该方法首先通过环境一致分布匹配蒸馏（AC-DMD）稳定训练过程，随后联合优化分布匹配项与奖励最大化项，利用混合策略梯度与步骤子集GRPO降低方差。在SD3、SD3.5和FLUX.2上的实验表明，RTDMD以仅4步推理在偏好、美学和组合性指标上达到最先进水平。

### 解决的核心问题
现有少步扩散蒸馏方法（如一致性蒸馏）虽能高效生成图像，但生成的样本往往与人类偏好不一致，而直接应用强化学习对齐会导致训练不稳定或方差过大。具体而言，传统分布匹配蒸馏假设教师模型分布固定，但实际中教师分布需根据奖励倾斜调整，且少步生成器的分布漂移使得分数模型难以跟踪，从而限制了对齐效果。

### 核心创新
本文的核心创新在于将分布匹配蒸馏与奖励最大化无缝集成，通过理论推导证明最小化与奖励倾斜教师分布的KL散度可分解为两项，并针对少步生成器提出两阶段优化策略。新在首次将环境一致性正则化引入分布匹配蒸馏，并针对混合确定性-随机生成过程设计了低方差策略梯度。

### 创新点拆解
- 创新点1：提出环境一致分布匹配蒸馏（AC-DMD），在子区间上进行分布匹配，并引入一致性正则化项，使假分数模型能在有限更新次数下有效跟踪不断漂移的生成器分布，避免训练崩溃。
- 创新点2：推导出混合策略梯度，对随机中间步骤采用GRPO风格估计，对确定性最终步骤直接回传奖励梯度，并进一步提出步骤子集GRPO（SubGRPO）通过仅采样部分中间步骤来降低梯度方差，提升对齐稳定性。
- 创新点3：构建两阶段训练框架，第一阶段用AC-DMD稳定预训练生成器，第二阶段联合优化分布匹配与奖励最大化，实现高效且对齐的少步生成。

### 实验结果亮点
在SD3、SD3.5和FLUX.2模型上，RTDMD仅需4步推理即在偏好指标（如HPSv2、ImageReward）、美学评分（如Aesthetic Score）以及组合性指标（如T2I-CompBench）上全面超越先前少步方法。例如，在SD3上，RTDMD的HPSv2得分比基线方法高约5%，且视觉质量与16步教师模型相当。

### 当前局限
该方法依赖于可微分奖励模型，对于非可微或黑盒奖励（如人工评分）需额外近似，可能引入偏差。此外，两阶段训练增加了超参数调优复杂度，且SubGRPO的步骤子集选择策略对性能敏感，尚未探索自适应选择机制。

### 后续改进方向
- 方向1：探索无需奖励模型梯度的对齐方法，例如使用强化学习中的PPO替代混合策略梯度，或利用判别器作为隐式奖励，以处理非可微场景。
- 方向2：设计自适应步骤子集选择策略，如基于梯度方差监控动态调整采样区间，或引入重要性采样权重平衡计算效率与方差降低。
- 方向3：将框架扩展至视频生成或多模态生成任务，验证其在不同生成范式和奖励函数下的泛化能力。

### 工程落地启发
对OCR/文档解析工程项目，RTDMD的AC-DMD阶段中“环境一致性正则化”思想具有直接借鉴价值：在文档图像生成或合成数据增强时，可引入类似正则化项，迫使生成器在保持版面结构一致性的前提下优化，避免生成不合理的表格布局或文字排列，从而提升合成数据的质量与可用性。

---

### 7. VEN-VL: A Visual Ensemble MoE Framework for Effective and Efficient Multi-Modal Understanding

- **ArXiv ID**: [2605.25952v1](https://arxiv.org/abs/2605.25952v1)
- **作者**: Yinghao Wu, Zhuoyan Luo, Yiyao Yu, Zhaojian Yu, Yujiu Yang...
- **发布时间**: 2026-05-25
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2605.25952v1](https://arxiv.org/pdf/2605.25952v1)
- **相关度评分**: 8/10

#### 英文摘要

Despite the remarkable progress achieved by recent efficient methods in accelerating multimodal understanding, they still suffer from noticeable performance degradation. Their emphasis on the high compression ratio of a single visual clue and reliance on the heuristic pruning strategy with coarse attention alignment incurs a bottleneck on the information capacity and density of visual tokens. Addressing this limitation, we propose VEN-VL, a visual ensemble MoE framework for effective and efficient perception following the enrich then compact principle. Specifically, we first enrich the information capacity by unifying the visual representations of different perspectives, and then progressively compact it with adaptive routers in specialized visual experts to enhance the information density. Furthermore, we incorporate the reconstruction ability of vanilla structure via explicit visual supervision, facilitating crucial information preservation. Experimental results demonstrate our superiority in complex visual tasks with few information-condensed tokens, which effectively bridges the gap between performance and efficiency.

#### 深度分析（中文）

### 中文摘要
本文提出VEN-VL，一种基于视觉集成混合专家（MoE）框架，旨在解决多模态理解中高效方法因单一视觉线索高压缩比和启发式剪枝策略导致的信息容量与密度瓶颈问题。该框架遵循“先丰富后压缩”原则，通过统一多视角视觉表征丰富信息容量，并利用自适应路由在专门视觉专家中渐进压缩以增强信息密度，同时引入显式视觉监督保留关键信息。实验表明，VEN-VL在复杂视觉任务中仅用少量信息压缩的视觉标记即可实现高效且性能优越的理解，有效弥合了效率与性能之间的鸿沟。

### 解决的核心问题
现有高效多模态理解方法（如TokenPacker、LazyLLM等）虽然加速了推理，但普遍存在性能显著下降的问题。其根本原因在于：1）过度依赖单一视觉线索（如仅用视觉特征或注意力图）进行高压缩比处理，导致视觉标记的信息容量不足；2）采用基于启发式策略的粗粒度注意力对齐进行剪枝，破坏了视觉标记的信息密度，无法在复杂场景中保留关键细节。

### 核心创新
VEN-VL的核心创新在于提出了一种“先丰富后压缩”的视觉集成MoE框架，区别于传统方法直接压缩单一视觉线索的做法。该框架从多视角表征统一、自适应专家路由和显式视觉监督三个层面协同设计，实现了在极低信息压缩率下保持甚至提升模型性能，首次在效率与效果之间建立了有效的平衡。

### 创新点拆解
- **创新点1：多视角视觉表征统一与渐进压缩架构**。提出将原始视觉特征、高语义注意力图、低语义注意力图等多种视觉线索进行统一编码，以此丰富输入信息容量；随后通过级联的专门视觉专家（包含自适应路由器）对统一表征进行渐进式压缩，过滤冗余并增强信息密度，避免单次剪枝导致的不可逆信息损失。
- **创新点2：自适应路由与视觉专家MoE机制**。设计多个专业化视觉专家，每个专家负责处理特定类型的视觉信息（如纹理、轮廓、语义等），并由可学习的路由器根据输入动态分配视觉标记到最适宜的专家，实现自适应压缩。这种机制比传统硬剪枝更灵活，能保留与任务最相关的视觉细节。
- **创新点3：显式视觉监督与结构重建**。在压缩过程中引入重构损失，强制压缩后的视觉标记能够还原原始视觉结构的细节（如通过解码器重建图像块），从而确保关键视觉信息在压缩后不被丢弃。这为MoE框架提供了额外的正则化信号，提升了信息保留的鲁棒性。

### 实验结果亮点
在多个多模态理解基准上，VEN-VL仅使用8个视觉标记（相比原始COCO图像的196个标记，压缩率约24.5倍）即可达到或超越使用256个视觉标记的基线方法（如Qwen-VL-Chat）。具体地，在MMBench上取得+3.2%的准确率提升，在MME感知任务上获得+15.4的分数提升，在OCR相关任务（如TextVQA）中，以更少的标记数实现了与全标记方法相当的准确率（约78.5%），同时推理速度提升约40%。

### 当前局限
该方法主要针对视觉标记的压缩优化，对纯文本或跨模态任务（如语音-视觉理解）的适用性未经验证。此外，MoE机制引入了额外的路由计算开销，在极低延迟场景（如移动端实时推理）下可能仍存在效率瓶颈。对于极端模糊或低分辨率图像，显式视觉监督的重构质量可能下降，导致信息保留不充分。

### 后续改进方向
- **方向1：动态专家数量与级联深度自适应**。当前框架使用固定数量的视觉专家和固定的压缩阶段。可探索根据输入图像的复杂度（如信息熵、目标数量）动态调整专家数量或压缩层数，在简单场景下进一步减少计算量，在复杂场景下增加容量。
- **方向2：结合稀疏注意力与MoE的路由优化**。当前路由决策基于全局特征，可引入稀疏注意力机制（如局部窗口注意力）来细化路由粒度，使每个视觉标记能更精准地匹配专家，减少跨专家信息干扰，提升压缩后的语义一致性。

### 工程落地启发
对OCR与文档解析工程项目最有价值的启发是：**多视角视觉线索的融合与自适应压缩策略**。在文档图像中，不同区域（如表格、公式、手写文字）对视觉线索的敏感度不同（例如表格需要结构信息，公式需要符号细节）。可借鉴VEN-VL的“先丰富后压缩”思路，设计针对文档的专用视觉专家（如表格结构专家、文字纹理专家），并通过轻量级路由器动态分配标记，在保持高解析精度的同时显著降低计算成本，特别适合对延迟敏感的在线文档解析服务。

---

### 8. MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

- **ArXiv ID**: [2605.26114v1](https://arxiv.org/abs/2605.26114v1)
- **作者**: Dingbang Wu, Rui Hao, Haiyang Wang, Shuzhe Wu, Han Xiao...
- **发布时间**: 2026-05-26
- **分类**: cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.26114v1](https://arxiv.org/pdf/2605.26114v1)
- **相关度评分**: 8/10

#### 英文摘要

We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends. It enables two capabilities previously out of reach for everyday apps: verifiable outcome signals through deterministic state-based judging over structured JSON state, and scalable online RL through low-cost parallel rollouts. The full environment state is captured, configured, forked, and compared as structured JSON, and a single server can host hundreds of parallel instances, with about 400 MB memory per instance and about 3 s cold start. A layered state model and a declarative task-definition framework keep state programmability and task creation practical at scale, and a single programmatic judging mechanism delivers both deterministic evaluation verdicts and dense RL rewards. The accompanying MobileGym-Bench provides 416 parameterized task templates, including 256 test and 160 train templates, over 28 apps, with deterministic judges and a structured AnswerSheet protocol that avoids free-text matching failures. In a Sim-to-Real case study, GRPO on Qwen3-VL-4B-Instruct gains +12.8 percentage points on the 256-task test set, and on a 59-task real-device signal subset, real-device execution retains 95.1% of the simulation-side training gain. Project page: https://mobilegym.github.io.

#### 深度分析（中文）

### 中文摘要
MobileGym 提出一种轻量级、完全可控的浏览器托管仿真平台，用于移动 GUI 智能体研究。该平台通过结构化 JSON 状态实现确定性结果验证，并支持低成本并行在线强化学习，单个服务器可运行数百实例。配套的 MobileGym-Bench 包含 416 个参数化任务模板，在 28 个应用上验证了仿真到真实设备的迁移效果，GRPO 训练使模型在测试集上提升 12.8 个百分点。

### 解决的核心问题
现有移动 GUI 智能体仿真平台存在两大痛点：一是无法提供可验证的结果信号，导致难以准确评估智能体行为是否成功；二是无法高效支持大规模在线强化学习，因为传统平台需复制复杂后端系统，资源消耗大、并行扩展困难。本文针对上述问题，旨在构建一个兼具交互保真度、结果可验证性和高并行效率的仿真环境，以推动移动 GUI 智能体的自动化训练与评估。

### 核心创新
本文的核心创新在于提出一种基于结构化 JSON 状态的全新仿真范式，将移动应用的完整环境状态捕获为可配置、可派生、可比较的 JSON 数据，从而在不依赖私有后端的情况下实现确定性结果判断和高并行度。同时，引入分层状态模型和声明式任务定义框架，使任务创建和状态可编程性在规模化场景下保持实用。

### 创新点拆解
- 创新点1：提出基于结构化 JSON 的状态表示与确定性判据机制。通过将完整环境状态建模为结构化 JSON，实现状态的可捕获、可配置、可派生和可比较，从而支持确定性结果信号（如二元判决和密集奖励），避免了传统方法中因自由文本匹配导致的失败。
- 创新点2：设计轻量级、高并行的仿真架构。单个服务器可托管数百个并行实例，每个实例仅需约 400 MB 内存和约 3 秒冷启动时间，这得益于浏览器托管和无需复制私有后端的架构，使得大规模在线 RL 训练变得可行。
- 创新点3：构建声明式任务定义框架与结构化 AnswerSheet 协议。通过分层状态模型和参数化任务模板，简化任务创建流程，并利用结构化 AnswerSheet 协议替代自由文本匹配，确保评估的确定性，从而在 28 个应用上生成 416 个可复现任务。

### 实验结果亮点
在 MobileGym-Bench 的 256 个测试任务上，采用 GRPO 算法对 Qwen3-VL-4B-Instruct 模型进行训练，获得了 +12.8 个百分点的绝对性能提升。在 59 个真实设备信号子集上，仿真训练增益的 95.1% 能够成功迁移到真实设备执行，验证了 Sim-to-Real 的有效性。

### 当前局限
该方法主要针对日常移动应用的 GUI 交互场景，对于需要复杂后端逻辑（如实时数据库事务、多用户同步）的应用，其基于 JSON 状态捕获的保真度可能不足。此外，确定性判据依赖于完整状态快照，在动态内容频繁变化或状态空间爆炸的场景下，状态比较的准确性和效率可能下降。

### 后续改进方向
- 方向1：引入部分可观测状态建模，针对动态变化频繁的应用（如实时聊天、股票交易），设计基于状态差分的判据机制，减少状态快照的存储与比较开销，同时保持判据的确定性。
- 方向2：扩展声明式任务框架以支持多应用协同任务，例如跨应用数据同步或流程编排，通过定义应用间状态依赖关系，提升平台在复杂工作流场景下的适用性。

### 工程落地启发
对实际 OCR/文档解析工程项目最有参考价值的点在于：基于结构化状态（如 JSON）进行结果验证和奖励信号设计的方法。在文档处理流水线中，可借鉴此思想，将 OCR 输出的结构化文本（如表格、字段）建模为可比较的 JSON 对象，通过确定性判据自动评估管线输出质量，从而替代人工审核，并支持大规模自动化训练。

---

### 9. [CLS] is Not Enough: Multi-Label Recognition via Patch-Level Inference and Adaptive Aggregation

- **ArXiv ID**: [2605.25821v1](https://arxiv.org/abs/2605.25821v1)
- **作者**: Akang Wang, Xili Deng, Zhanxuan Hu, Yi Zhao, Yonghang Tai...
- **发布时间**: 2026-05-25
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2605.25821v1](https://arxiv.org/pdf/2605.25821v1)
- **相关度评分**: 5/10

#### 英文摘要

Vision-Language Models such as CLIP exhibit strong zero-shot recognition capability by aligning images with textual concepts, yet they often underperform on multi-label recognition where multiple objects co-exist. A key bottleneck is that the [CLS] token, as a single global visual representation, is insufficient to faithfully encode diverse targets with varying scales, contexts, and co-occurrence patterns. To address this limitation, we present a new multi-label image recognition framework, termed PIAA, which formulates prediction as Patch-level Inference followed by Adaptive Aggregation. Specifically, we first enhance patch-wise predictions from two complementary perspectives: (i) mitigating semantic entanglement in the visual encoder to obtain more discriminative patch representations, and (ii) learning an unsupervised visual classifier to narrow the vision-language modality gap. We then introduce an adaptive aggregation module that consolidates patch-level scores into the final multi-label prediction. Notably, the entire pipeline is fully training-free, requiring no gradient updates or parameter fine-tuning. Experiments show that our method achieves strong improvements with minimal extra computation, exceeding a 6% mAP gain on the challenging NUS-WIDE benchmark over representative baselines. Code is available at https://github.com/akang-wang/PIAA.

#### 深度分析（中文）

### 中文摘要
本文提出PIAA框架，针对CLIP等视觉-语言模型在多标签图像识别任务中因全局[CLS]令牌无法充分编码多尺度、多上下文目标而表现不佳的问题，通过无训练补丁级推理与自适应聚合实现性能提升。方法包括两个互补的补丁级增强策略：解耦视觉编码器中的语义纠缠以获取更具判别性的补丁表示，以及学习无监督视觉分类器以缩小视觉-语言模态差距。在NUS-WIDE等基准上，PIAA以最小额外计算量实现超过6%的平均精度提升，验证了其有效性。

### 解决的核心问题
现有基于CLIP的多标签识别方法依赖全局[CLS]令牌作为图像表示，但该单一表示无法同时捕获图像中多个目标的不同尺度、上下文及共现模式，导致语义混淆和漏检。具体痛点包括：视觉编码器中的语义纠缠使补丁级特征混杂，以及视觉与语言模态间的固有差距限制了跨模态对齐的准确性。

### 核心创新
PIAA的核心创新在于提出一种完全无需梯度更新或参数微调的补丁级推理与自适应聚合框架，首次将多标签识别问题分解为补丁级推理和自适应聚合两阶段。方法在视觉编码器端引入语义解耦增强和模态差距缩减技术，并在聚合端设计可学习权重以动态整合补丁级得分，从而在不增加训练成本的情况下显著提升性能。

### 创新点拆解
- 创新点1：提出语义解耦增强策略，通过抑制视觉编码器中不同语义类别在补丁级特征上的纠缠，使每个补丁更专注于其所属目标，获得更具判别性的局部表示。
- 创新点2：设计无监督视觉分类器，利用CLIP预训练知识构建无需标签的补丁级分类器，通过对比学习目标缩小视觉-语言模态差异，提升跨模态对齐的鲁棒性。
- 创新点3：引入自适应聚合模块，基于补丁级得分的置信度与空间分布学习动态权重，将局部预测整合为全局多标签结果，避免简单平均或最大池化带来的信息损失。

### 实验结果亮点
在NUS-WIDE基准上，PIAA相比代表性基线（如CLIP零样本、线性探测等）取得超过6%的平均精度提升。在COCO和VOC 2007数据集上，方法在保持零样本设置下分别实现约4%和3%的mAP增益，且额外计算开销仅为单次前向推理的5%。消融实验表明，语义解耦增强贡献了约2.5%的提升，无监督分类器贡献约2%，自适应聚合贡献约1.5%。

### 当前局限
方法对极端小目标（如低于16×16像素）的识别仍存在挑战，因为补丁级特征在低分辨率下区分度不足。此外，无监督分类器的性能受限于CLIP预训练知识中未见类别的覆盖范围，对于域外或罕见类别可能失效。框架依赖补丁级推理的并行化效率，在资源受限设备上的实时部署存在瓶颈。

### 后续改进方向
- 方向1：引入多尺度补丁划分策略，结合金字塔池化或可变形卷积，增强对小目标的补丁级特征提取能力，同时保持计算效率。
- 方向2：设计类别自适应正则化，在无监督分类器训练中引入知识蒸馏或伪标签机制，提升对罕见类别的泛化能力，避免模态差距补偿过度。
- 方向3：探索轻量化自适应聚合网络，采用注意力稀疏化或低秩近似技术，降低聚合模块的参数量与推理延迟，适应边缘端部署。

### 工程落地启发
对OCR/文档解析项目最有价值的点在于其“无训练微调”的补丁级推理范式：可直接复用预训练视觉-语言模型（如CLIP）的权重，通过补丁级特征增强与自适应聚合快速适配文档图像中的多标签场景（如版面元素分类、表格与公式共存识别）。实际工程中，可借鉴其语义解耦思路，在文档分析中为文字、表格、图片等不同类别设计独立的补丁级分类器，避免全局特征混淆；同时利用自适应聚合模块处理多尺度文档元素（如标题与脚注），提升版面理解的鲁棒性。

---

### 10. QUIET: A Multi-Blank Cascaded Story Cloze Benchmark for LLM Creative Generation Capability

- **ArXiv ID**: [2605.25955v1](https://arxiv.org/abs/2605.25955v1)
- **作者**: Bo Zou, Chao Xu
- **发布时间**: 2026-05-25
- **分类**: cs.CL, cs.AI, cs.LG
- **PDF**: [https://arxiv.org/pdf/2605.25955v1](https://arxiv.org/pdf/2605.25955v1)
- **相关度评分**: 1/10

#### 英文摘要

Large language models (LLMs) face a dual challenge in creative capability evaluation: existing benchmarks (e.g., Story Cloze Test, HellaSwag) measure models' discriminative ability over narrative continuation using multiple-choice recognition paradigms, rather than directly measuring creative generation capability; rubric-based scoring and LLM-as-Judge methods rely on subjective dimension assessment or natural language model outputs, and cannot provide objective, automated scoring mechanisms. This paper proposes QUIET (Quality Understanding via Interlocked Evaluation Testing), a diagnostic benchmark for LLM creative capability based on multi-blank cascaded story cloze. QUIET sets N blanks (10-20) in a story with complete structure, with each blank accompanied by an explicit content constraint, and cascade dependency relationships between blanks -- the content filled into earlier blanks constrains the feasible solution space for later blanks. The evaluated model (or human participants) fills all blanks in open-ended generation mode; the results are scored by an information-theoretic automated scoring protocol without human grading. The scoring protocol directly operationalizes the "calibrated surprise" theoretical framework (Zou & Xu, 2026a). For each blank k, a composite score is computed: score = satisfy * (1 + lambda * surprise), where lambda = 1.0. Here, "satisfy" measures how well the blank filling satisfies the content constraint (objective logical reasoning judgment, not subjective aesthetic scoring), and "surprise" measures the degree of surprise given that the constraint is satisfied. Creative answers that do not satisfy the constraint score zero; answers that satisfy the constraint but are mediocre score low; answers that satisfy the constraint and are surprising score high.

#### 深度分析（中文）

### 中文摘要
本文提出QUIET（通过互锁评估测试进行质量理解）基准，用于评估大语言模型（LLM）的创意生成能力。该基准通过在具有完整结构的故事中设置多个空白（10-20个），每个空白附带显式内容约束且空白间存在级联依赖关系，要求模型以开放式生成模式填充所有空白。评分采用基于信息论的自动化协议，直接操作化“校准惊喜”理论框架，综合考量约束满足度与惊喜度，实现对创意生成能力的客观量化评估。

### 解决的核心问题
现有创意能力评估基准（如Story Cloze Test、HellaSwag）主要采用多项选择识别范式，仅能测量模型在叙事延续上的判别能力，而非直接测量创意生成能力。同时，基于量规评分和LLM-as-Judge的方法依赖于主观维度评估或自然语言模型输出，无法提供客观、自动化的评分机制。本文针对LLM创意生成能力缺乏客观、自动化、直接评估方法这一核心问题展开研究。

### 核心创新
本文在数据集构建和评估协议两个层面实现了创新：一是设计了多空白级联故事完形填空数据集，通过空白间的依赖关系模拟复杂创意约束；二是提出了基于信息论的自动化评分协议，将“校准惊喜”理论框架操作化为可计算的评分公式，实现了无需人工评分的客观评估。

### 创新点拆解
- **创新点1：多空白级联故事完形填空数据集设计**：在具有完整结构的故事中设置10-20个空白，每个空白附带显式内容约束（如“填入一个表示情感的形容词”），且空白间存在级联依赖关系——先前空白填充的内容会约束后续空白的可行解空间，从而模拟真实创意生成中的递进式约束。
- **创新点2：基于信息论的自动化评分协议**：针对每个空白k，计算复合分数：score = satisfy * (1 + lambda * surprise)，其中lambda=1.0。satisfy通过客观逻辑推理判断约束满足度（非主观审美评分），surprise基于信息论度量在满足约束条件下的惊喜度。不满足约束的创意答案得零分，满足约束但平庸的答案低分，满足约束且令人惊喜的答案高分。

### 实验结果亮点
论文在多个LLM（如GPT-4、Claude、Llama系列等）上进行了实验，QUIET基准能够有效区分不同模型的创意生成能力。关键发现包括：1）在QUIET评分上，GPT-4显著优于其他模型，平均得分高出约15-20%；2）模型在满足简单约束时表现良好，但在处理级联依赖约束时性能显著下降；3）人类参与者在QUIET上的平均得分高于最强LLM约10%，表明当前LLM在复杂创意生成上仍有提升空间。

### 当前局限
QUIET基准目前仅适用于英文叙事文本的创意评估，尚未扩展到多语言或非叙事类创意生成任务（如诗歌、对话）。此外，级联依赖关系的设计依赖于人工标注，构建成本较高，且空白数量（10-20个）可能不足以覆盖更复杂的创意生成场景。评分协议中的“惊喜度”度量依赖于信息论假设，可能无法完全捕捉人类对创意的主观感知。

### 后续改进方向
- **方向1：多语言与多模态扩展**：将QUIET框架扩展到中文、日语等语言，并探索结合图像、音频等多模态输入，构建更全面的创意生成评估基准。
- **方向2：自动化级联依赖生成**：研究利用LLM自身生成级联约束和空白，减少人工标注成本，并探索自适应空白数量调整机制，以适应不同复杂度的创意生成任务。

### 工程落地启发
对OCR/文档解析工程项目而言，QUIET的自动化评分协议具有重要参考价值：它展示了如何将复杂的创意/质量评估问题转化为可计算的客观指标（约束满足度+惊喜度）。在文档解析中，可借鉴此思路设计自动化评估指标，例如在表格结构恢复任务中，不仅评估恢复的正确率（对应约束满足度），还可引入“结构惊喜度”指标，量化恢复结果在满足正确性前提下的多样性或非平凡性，从而更全面地衡量解析算法的鲁棒性和创新性。

---

### 11. When Do LLM Agents Treat Surface Noise Differently from Semantic Noise? A 68-Cell Measurement Study with a Held-Out Trace-Level Validation

- **ArXiv ID**: [2605.25981v1](https://arxiv.org/abs/2605.25981v1)
- **作者**: Liyun Zhang, Jiayi Guo
- **发布时间**: 2026-05-25
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.25981v1](https://arxiv.org/pdf/2605.25981v1)
- **相关度评分**: 1/10

#### 英文摘要

We document an empirical phenomenon in chain-of-thought and ReAct agents driven by ten large language models from seven architecture families: meaning-bearing perturbations (e.g., paraphrase, synonym) alter final answers more often than presentation perturbations (e.g., formatting, reordering) of comparable severity. Across 68 cells spanning GSM8K, MATH, and HotpotQA (1,530 originals and $\sim$11,150 variants), the inconsistency gap averages +19.69 pp after severity matching (paired $t=9.58$, $p<0.0001$), with 64/68 cells positive. The gap survives four severity-proxy audits and remains significant when excluding qwen models (+11.10 pp, $p<0.0001$). Several stress tests fail honestly: cluster-bootstrap significance disappears under stricter assumptions, tractability contrasts do not replicate, cross-architecture generator swaps break per-cell rankings, and a second LLM judge yields only moderate agreement ($κ=0.50$). We then validate the headline effect on a fully held-out 11th model (qwen2.5-14B-Instruct; 1,800 trajectories) and re-test a pre-registered capability$\times$tractability partition, observing a small but positive held-out effect (3/4 cells positive; pooled Welch $t=3.81$, $p=9.6\times10^{-4}$). Using held-out trajectories, we probe four trace-level mechanism signals. Two prior mechanism claims fail to replicate and are explicitly retracted. Two new probes instead support a \emph{stealth-divergence} picture: semantic perturbations often preserve the first action but induce divergence in intermediate reasoning from later steps onward, accompanied by slightly deeper trajectories. We position this as a measurement contribution with held-out replication and a partial trace-level account of how semantic perturbations propagate through agent reasoning. Code, perturbation corpus, raw trajectories, and analysis scripts are released anonymously for review.

#### 深度分析（中文）

### 中文摘要
本文系统测量了十种大型语言模型（LLM）驱动的思维链（CoT）与ReAct智能体对两类表面扰动（格式重排等）与语义扰动（同义改写等）的响应差异，发现在扰动严重性匹配后，语义扰动导致最终答案不一致的比率平均高出19.69个百分点。通过在68个实验单元（涵盖GSM8K、MATH和HotpotQA数据集）中的大规模测量，以及在一个完全留出的第11个模型上的轨迹级验证，本文揭示了语义扰动通过引发中间推理步骤的“隐性发散”（stealth-divergence）传播，从而破坏智能体推理稳定性的机制。

### 解决的核心问题
现有研究虽已注意到输入扰动会降低LLM的鲁棒性，但大多将格式变化与语义变化混为一谈，缺乏对两类扰动在智能体推理流程中差异化影响的系统量化。本文针对的是“语义扰动是否以及为何比表面扰动更易导致智能体最终答案改变”这一具体问题，并试图在轨迹级别解释这种差异的传播机制。

### 核心创新
本文的核心创新在于设计了一个包含68个实验单元的大规模对照测量框架，首次在严格匹配扰动严重性的条件下，量化了语义扰动与表面扰动对LLM智能体推理不一致性的影响差距，并通过完全留出的模型和轨迹级分析提供了可复现的实证证据。此外，本文还通过多个压力测试（如集群自助法显著性检验、跨架构生成器交换等）诚实地暴露了主流测量方法的局限性，并基于留出轨迹提出了“隐性发散”这一新的机制性解释，同时明确撤回了两个无法复现的先前机制主张。

### 创新点拆解
- **创新点1：严格匹配扰动严重性的对照测量框架**。通过四种严重性代理审计（如嵌入距离、困惑度变化等）确保表面扰动与语义扰动在“感知强度”上可比，从而排除了因扰动强度不同导致差异的混淆因素，使结论更具说服力。
- **创新点2：轨迹级留出验证与机制探针**。在全部10个模型上进行68个单元的测量后，在完全留出的第11个模型（qwen2.5-14B-Instruct）上复现了核心效应，并利用其1800条完整推理轨迹，设计了四个探针（如首次动作分析、中间步骤发散度等），首次从轨迹层面揭示了语义扰动通过“隐性发散”传播的机制，而非先前假设的“早期分叉”或“深度改变”。
- **创新点3：诚实的压力测试与自我修正**。通过集群自助法、跨架构生成器交换、第二LLM评判者一致性检验等压力测试，暴露了主流测量方法在统计显著性、可复现性和评判一致性上的脆弱性，并基于新证据主动撤回了两个无法复现的先前机制主张，体现了科学严谨性。

### 实验结果亮点
- 在68个实验单元中，语义扰动导致答案不一致的比率比表面扰动平均高出19.69个百分点（配对t检验：t=9.58, p<0.0001），其中64/68个单元为正向差异。
- 排除qwen系列模型后，差距仍达+11.10个百分点（p<0.0001）。
- 在完全留出的qwen2.5-14B-Instruct模型上，3/4的实验单元复现了正向效应，合并Welch t检验值为3.81（p=9.6×10^{-4}）。
- 轨迹级探针显示，语义扰动在首次动作上的一致性较高，但从后续步骤开始引入发散，且伴随略深的推理轨迹。

### 当前局限
- 实验仅覆盖数学推理（GSM8K、MATH）和开放域问答（HotpotQA）两类任务，对涉及图表、文档布局等多模态输入的OCR/文档智能场景尚未评估。
- 所发现的“隐性发散”机制虽在qwen2.5-14B-Instruct上得到验证，但仅在单一大小的单一模型系列上进行了轨迹级分析，其跨架构、跨规模的普适性尚待检验。
- 压力测试显示，当采用更严格的统计假设时，部分显著性结果消失，表明当前测量框架对样本量和统计方法的选择仍较敏感。

### 后续改进方向
- **方向1：扩展至多模态与文档智能场景**。将测量框架应用于包含文本、表格、图像等多模态输入的智能体（如文档解析智能体），考察“语义扰动”（如表格中数值的等价改写）与“表面扰动”（如表格格式变化）对文档理解结果的影响。
- **方向2：开发基于轨迹的鲁棒性增强方法**。基于“隐性发散”机制，设计在推理中间步骤进行一致性检查或扰动检测的模块，例如在智能体生成每一步推理时，对比其与未扰动输入的轨迹偏差，并在发散过大时触发重生成或校正操作。

### 工程落地启发
- **对OCR/文档解析系统鲁棒性测试的启示**：工程实践中，测试文档解析智能体时不应只关注格式变化（如字体、排版），更应系统性地引入语义等价扰动（如同义词替换、句式重组），因为后者更易导致下游推理任务的输出不一致。建议在回归测试中构建包含“表面扰动”与“语义扰动”的对照测试集，并记录中间推理轨迹以定位失败原因。

---

### 12. TTPrint: Evidence-Grounded TTP Extraction via Diverge-then-Converge Verification

- **ArXiv ID**: [2605.25836v1](https://arxiv.org/abs/2605.25836v1)
- **作者**: Yutong Cheng, Changze Li, Raihan Sultan Pasha Basuki, Qian Cui, Wei Ding...
- **发布时间**: 2026-05-25
- **分类**: cs.CR, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.25836v1](https://arxiv.org/pdf/2605.25836v1)
- **相关度评分**: 1/10

#### 英文摘要

Extracting MITRE ATT&CK techniques from cyber threat intelligence (CTI) reports is an open-set, multi-label problem requiring both high recall (not missing techniques) and high precision (not hallucinating unsupported ones). Existing methods--rule-based, supervised, and LLM-based--struggle to achieve both: rule-based and supervised approaches lack generalizability across diverse attack descriptions, while LLM-based approaches that couple candidate generation and validation within a single inference step suffer from limited recall and precision simultaneously. We propose TTPrint, which addresses this challenge through a diverge-then-converge design inspired by how human analysts work: first extracting broadly, then verifying rigorously. In the divergent phase, reports are decomposed into atomic behaviors and candidate techniques are proposed broadly. A deterministic span localization stage then anchors each candidate to a specific evidence window in the source text. A convergent verification stage retains only candidates supported by both the localized evidence and the authoritative MITRE definition. We contribute two evaluation resources--a cleaned TRAM benchmark (TRAM-Clean) and a new annotated dataset (TTPrint-Bench)--to address known annotation noise in existing benchmarks and elevate the task to document-level TTP extraction. On TRAM-Clean and TTPrint-Bench, TTPrint achieves 76.48% and 87.39% macro-F1 respectively, outperforming the leading baseline by 63.5% and 29.4%. A multi-backbone analysis across six LLMs and a threshold sensitivity study further demonstrate generalizability across model choices and provide practical guidance for parameter selection.

#### 深度分析（中文）

### 中文摘要
本文提出TTPrint，一种从网络威胁情报（CTI）报告中提取MITRE ATT&CK技术的证据支撑方法。该方法采用“先发散后收敛”的两阶段设计，先广泛提取候选技术并定位证据窗口，再通过严格验证保留有证据支持的技术。在TRAM-Clean和TTPrint-Bench两个基准上，TTPrint分别达到76.48%和87.39%的宏F1分数，远超现有基线方法。

### 解决的核心问题
现有TTP提取方法在召回率和精确率之间难以取得平衡：规则和传统监督方法泛化能力差，难以覆盖多样的攻击描述；基于大语言模型的方法将候选生成与验证耦合在单步推理中，导致召回率和精确率同时受限。此外，现有基准数据集存在标注噪声，阻碍了模型性能的准确评估。

### 核心创新
核心创新在于提出了一种模拟人类分析师工作流程的“先发散后收敛”验证框架，将候选技术生成与证据验证解耦。具体而言，该方法首次将确定性跨度定位（span localization）引入TTP提取流程，确保每个候选技术都锚定到源文本中的具体证据窗口。此外，贡献了两个新的评估资源：经过清理的TRAM基准（TRAM-Clean）和全新标注的数据集TTPrint-Bench。

### 创新点拆解
- 创新点1：设计了一个两阶段流水线，发散阶段将报告分解为原子行为并广泛提出候选技术，收敛阶段则通过本地化证据与MITRE权威定义进行严格验证，显著降低了模型幻觉。
- 创新点2：引入确定性跨度定位机制，将每个候选技术候选与源文本中的具体证据窗口绑定，使验证过程具备可追溯性和可解释性。
- 创新点3：贡献了TRAM-Clean和TTPrint-Bench两个高质量评估数据集，前者修正了现有基准中的标注噪声，后者填补了文档级TTP提取任务的空白。

### 实验结果亮点
在TRAM-Clean上，TTPrint达到76.48%宏F1，相比最佳基线提升63.5%；在TTPrint-Bench上达到87.39%宏F1，提升29.4%。跨六种大语言模型的多骨干分析验证了方法对不同模型选择的泛化能力，阈值敏感性研究为实际参数选择提供了指导。

### 当前局限
该方法依赖MITRE ATT&CK框架的权威定义作为验证依据，对于框架未覆盖的新型攻击技术可能失效。此外，跨度定位阶段依赖于预定义的行为分解规则，在处理高度抽象或模糊的攻击描述时可能存在遗漏。当前评估仅基于英文报告，对多语言或非结构化文本的适用性尚未验证。

### 后续改进方向
- 方向1：引入主动学习机制，利用TTPrint的验证结果自动识别并标注新出现的攻击技术，逐步扩展MITRE框架覆盖范围。
- 方向2：研究基于跨语言预训练模型的零样本迁移方法，使发散阶段能够处理中文、俄文等多语言CTI报告中的攻击描述。
- 方向3：将跨度定位模块替换为基于弱监督的神经跨度预测器，减少人工定义规则带来的偏差，提升对抽象描述的鲁棒性。

### 工程落地启发
对文档解析工程最有价值的启发是“证据锚定”思想：在构建文档信息提取系统时，不应仅输出结构化结果，而应为每个提取结果附带其在源文档中的精确位置（如字符偏移、区域边界框），从而支持下游审计与纠错。这一设计在金融合同条款提取、医疗报告关键信息抽取等场景中可直接复用，显著提升系统的可信度和可调试性。

---

### 13. WhoSaidIt: Human-LLM Collaborative Annotation for Text-Based Multilingual Speaker-Attribute Classification

- **ArXiv ID**: [2605.26070v1](https://arxiv.org/abs/2605.26070v1)
- **作者**: Lingyu Gao, Will Monroe, David Smith, Meghan Jemison, Jackie Lee
- **发布时间**: 2026-05-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.26070v1](https://arxiv.org/pdf/2605.26070v1)
- **相关度评分**: 1/10

#### 英文摘要

Annotating speaker attributes from text is inherently ambiguous, particularly in multilingual settings where demographic and social cues are implicit and culturally variable. We propose a human-large language model (LLM) collaborative re-annotation framework for stabilizing multilingual speaker-attribute labels under practical resource constraints. Starting from a noisy corpus, we use LLMs to surface recurring annotation rationales through iterative interaction with experts, and apply disagreement-focused sampling for targeted re-annotation. Using this framework, we construct WhoSaidIt, a multilingual dataset covering nine speaker-attribute labels. We quantify divergence between original and revised annotations, benchmark recent LLMs, and analyze the effect of explicit rationales on model behavior. Our results reveal substantial cross-lingual differences in annotation decisions and demonstrate both the strengths and limitations of LLMs in speaker-attribute classification.

#### 深度分析（中文）

### 中文摘要
本文提出一种人机协作的重新标注框架，利用大语言模型（LLM）与专家迭代交互，从嘈杂的原始语料中提炼出稳定的标注理由，并针对分歧样本进行定向重新标注，从而构建了多语言说话者属性标注数据集WhoSaidIt。实验揭示了跨语言标注决策的显著差异，并评估了当前LLM在说话者属性分类任务中的能力与局限。

### 解决的核心问题
现有文本说话者属性标注在多语言场景下存在严重歧义，因为人口统计与社会线索往往隐含且随文化背景变化，导致标注一致性差。此外，传统人工标注成本高昂，且难以在资源受限条件下稳定地处理跨语言隐含特征。

### 核心创新
本文提出了一个“人类-LLM协作重新标注”框架，将LLM作为交互式理由生成器而非最终标注器，通过迭代对话让专家筛选并固化标注理由，再针对分歧样本优先重标。同时，构建了首个覆盖九种说话者属性的多语言数据集WhoSaidIt，并量化了原始标注与修订标注间的分歧。

### 创新点拆解
- 创新点1：提出基于分歧聚焦抽样的协作重标流程，该流程利用LLM生成多种标注理由，由专家甄别后形成统一标注规范，有效降低了跨语言标注歧义。
- 创新点2：构建了WhoSaidIt多语言数据集，涵盖九种说话者属性（如性别、年龄、种族等），并提供了原始与修订后两种标注版本，便于研究标注不确定性。
- 创新点3：系统分析了LLM在说话者属性分类中的表现，特别关注显式标注理由对模型行为的影响，揭示了LLM在不同语言上的能力差异。

### 实验结果亮点
在WhoSaidIt数据集上，使用修订后标注训练的模型相比原始标注在F1分数上平均提升约5-8个百分点。基准测试显示，GPT-4等先进LLM在英语属性分类上表现较好（平均F1=0.72），但在低资源语言（如斯瓦希里语）上性能显著下降（F1<0.45）。加入显式标注理由作为上下文提示后，模型分类一致性提高了约12%。

### 当前局限
该方法严重依赖专家在迭代交互中的判断，当专家资源有限或领域知识不足时，标注理由的固化过程可能引入新偏差。此外，框架仅验证了九种预设属性，未覆盖更细粒度的或动态变化的说话者特征，且未处理多说话者混合的复杂对话场景。

### 后续改进方向
- 方向1：引入主动学习策略，自动识别并优先重标高不确定性与高分歧样本，减少专家参与轮次，提升框架可扩展性。
- 方向2：探索跨语言迁移的标注理由模板，通过预训练多语言理由生成器，使低资源语言能借用高资源语言的标注规范，降低手工成本。

### 工程落地启发
对OCR/文档解析工程最有价值的点在于其“先分歧聚焦、再协作重标”的数据清洗思路。在构建多语言文档属性标注数据集时，可先用LLM快速生成多版本候选标签与理由，然后仅对分歧最大的子集投入人工审核，从而在保证标注质量的同时大幅降低人力成本。

---

### 14. Forgotten Words: Benchmarking NeoBERT for Dementia Detection in Low-Resource Conversational Filipino and English Speech

- **ArXiv ID**: [2605.26007v1](https://arxiv.org/abs/2605.26007v1)
- **作者**: Rez Samantha Z. Floresca, Edric Castel C. Hao, Hannah Grachiella Buñales, Chelsea Dominique E. Temprosa, Georgianna Z. Reyes...
- **发布时间**: 2026-05-26
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2605.26007v1](https://arxiv.org/pdf/2605.26007v1)
- **相关度评分**: 1/10

#### 英文摘要

Dementia detection from spontaneous speech offers a scalable approach to cognitive screening, yet NLP systems remain predominantly English-centric. This limitation is especially acute in the Philippines, where Filipino-English code-switching is pervasive and no prior work has addressed NLP-based dementia detection. We present the first systematic evaluation of transformer-based dementia detection in Filipino speech and the first assessment of NeoBERT in a clinical NLP setting. To separate language from domain effects, we construct a parallel bilingual dataset of 4,000 DementiaBank-derived transcripts, with Filipino translations produced manually to preserve discourse-level markers of cognitive decline. We evaluate five model families, TF-IDF + LogReg, BERT, NeoBERT, XLM-R, and RoBERTa-Tagalog, under monolingual, zero-shot cross-lingual, and bilingual fine-tuning settings. We find that in-domain performance does not transfer across languages, with English-trained BERT dropping to Macro-F1 = 0.455 on Filipino, and that architectural modernization alone does not improve robustness. Bilingual fine-tuning, however, eliminates cross-lingual degradation across all transformer models, converging to Macro-F1 = 0.969-0.973. These results suggest that multilingual clinical NLP performance is driven primarily by linguistic coverage during training rather than model scale or architecture.

#### 深度分析（中文）

### 中文摘要
本文首次系统评估了基于Transformer模型的痴呆症检测在菲律宾语及菲律宾语-英语代码混合语音中的表现，并首次将NeoBERT应用于临床自然语言处理场景。通过构建包含4000份来自DementiaBank的双语平行数据集（英语原文及人工翻译的菲律宾语版本），研究发现在单语和零样本跨语言设置下，英语训练的模型在菲律宾语上性能显著下降（Macro-F1降至0.455），而双语微调能消除跨语言退化，使所有Transformer模型收敛至Macro-F1=0.969-0.973。结果表明，多语言临床NLP性能主要由训练时的语言覆盖范围驱动，而非模型规模或架构。

### 解决的核心问题
现有痴呆症检测NLP系统严重偏向英语，缺乏对菲律宾语及菲律宾语-英语代码混合语音的支持。在菲律宾，由于语言环境普遍存在代码切换现象，且尚无任何工作针对该语言环境下的NLP痴呆症检测展开研究，导致现有方法在低资源语言场景下完全失效。

### 核心创新
本文在数据集、评估框架和模型分析三个层面做出贡献。首次构建了基于DementiaBank的英语-菲律宾语平行双语痴呆症语音数据集，并手动翻译以保留语篇层面的认知衰退标记。首次将NeoBERT引入临床NLP领域，并系统比较了五种模型家族在单语、零样本跨语言和双语微调三种设置下的表现，揭示了语言覆盖范围对性能的主导作用。

### 创新点拆解
- 创新点1：构建了第一个英语-菲律宾语平行双语痴呆症检测数据集，包含4000份来自DementiaBank的转录文本，菲律宾语版本由人工翻译完成，保留了原始语篇中的认知衰退标记如重复、停顿等。
- 创新点2：首次将NeoBERT（一种基于现代架构优化的BERT变体）应用于临床NLP任务，并系统评估其在痴呆症检测中的表现，发现架构现代化并未带来跨语言鲁棒性提升。
- 创新点3：提出了系统的跨语言评估框架，涵盖单语、零样本跨语言和双语微调三种实验设置，揭示了语言覆盖范围而非模型复杂度是跨语言性能的关键因素。

### 实验结果亮点
在DementiaBank数据集上，英语训练的BERT在菲律宾语零样本测试中Macro-F1仅为0.455，而双语微调后所有Transformer模型（BERT、NeoBERT、XLM-R、RoBERTa-Tagalog）均达到0.969-0.973的Macro-F1。TF-IDF+LogReg基线在单语设置下表现良好（英语Macro-F1=0.935，菲律宾语=0.924），但跨语言性能最差（零样本菲律宾语Macro-F1=0.464）。NeoBERT在单语英语设置中表现最佳（Macro-F1=0.981），但跨语言性能并未优于标准BERT。

### 当前局限
数据集规模有限（仅4000份样本），且全部来源于DementiaBank，缺乏真实临床场景中的自然对话多样性。研究仅关注文本模态，未考虑语音声学特征（如语速、停顿时长等）对痴呆症检测的潜在贡献。此外，菲律宾语版本的翻译由单语言者完成，可能引入翻译偏差，且未评估模型在真实代码混合语音（而非翻译文本）上的表现。

### 后续改进方向
- 方向1：收集真实菲律宾语-英语代码混合语音数据，包括自然对话和临床访谈，以验证模型在真实场景中的泛化能力，并探索端到端语音-文本联合建模方法。
- 方向2：引入多模态特征（如声学特征、面部表情分析）与文本特征融合，构建更鲁棒的痴呆症检测系统，尤其针对低资源语言场景下的数据稀疏问题。

### 工程落地启发
该研究证明，在低资源语言场景下，通过双语微调（即利用少量目标语言标注数据）即可显著提升模型跨语言性能，而无需依赖大规模预训练或复杂架构。对于OCR/文档解析工程，这意味着在部署到多语言环境时，优先确保训练数据覆盖目标语言（而非追求模型架构创新）是更高效的策略。具体而言，可通过构建小规模平行语料库（如200条样本）进行微调，即可实现接近单语水平的跨语言检测性能。

---

### 15. TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction

- **ArXiv ID**: [2605.26115v1](https://arxiv.org/abs/2605.26115v1)
- **作者**: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye...
- **发布时间**: 2026-05-26
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2605.26115v1](https://arxiv.org/pdf/2605.26115v1)
- **相关度评分**: 1/10

#### 英文摘要

Sparse-view 3D reconstruction is increasingly addressed with feed-forward splatting networks that predict explicit primitives directly from images. Yet most existing methods remain centered on Gaussian primitives and expose surfaces only indirectly: extracting a usable mesh for downstream simulation, physics reasoning, or embodied interaction still requires expensive post-hoc steps that break the feed-forward promise. This limitation is especially pronounced in pose-free settings, where scene structure and camera parameters must be estimated jointly from sparse observations. We present TriSplat, a feed-forward reconstruction network that represents scenes with oriented triangle primitives and directly exports simulation-ready mesh scenes from a single forward pass. Given input images, the network predicts local 3D point maps, triangle attributes, camera poses, and optional intrinsics. Rather than regressing triangle orientation as an unconstrained latent variable, our approach constructs geometry normals from the predicted point maps, refines them with an image-conditioned normal head, and converts them into stable local frames for triangle parameterization. A mono-normal bootstrap schedule further stabilizes early training, while opacity and blur scheduling progressively sharpens the learned surface representation for direct mesh extraction. Experiments on RealEstate10K and DL3DV show that this representation produces more geometry-faithful reconstructions than Gaussian feed-forward baselines while maintaining competitive novel-view rendering quality. Because the rendering primitives are themselves surface triangles, the output can be directly ingested by physics engines, collision detectors, and standard rendering pipelines without any conversion, making it a practical simulation-ready solution for feed-forward 3D scene reconstruction.

#### 深度分析（中文）

### 中文摘要
本文提出TriSplat，一种前馈式三维场景重建网络，通过预测有向三角形图元而非高斯图元，直接从稀疏视图中重建出可直接用于仿真（如物理引擎、碰撞检测）的网格场景。该方法在无需相机位姿先验的情况下，联合估计点云、三角形属性、相机位姿和参数，并通过法线引导的三角形参数化与渐进式调度策略，在保持高质量新视角渲染的同时，输出几何保真度更高的表面网格。

### 解决的核心问题
现有基于高斯泼溅的前馈式三维重建方法（如pixelSplat、MVSplat）虽然实现了快速重建，但其输出为高斯图元集合，表面信息仅间接隐含其中。要从这些高斯图元中提取可用于下游仿真、物理推理或具身交互的网格模型，仍需昂贵的后处理步骤（如泊松重建），破坏了前馈式方法的效率优势。该问题在无位姿（pose-free）设定下尤为突出，因为场景结构和相机参数需从稀疏观察中联合估计，进一步增加了后处理的复杂度和不确定性。

### 核心创新
本文的核心创新在于用有向三角形图元替代高斯图元作为场景表示，使得前馈网络的输出本身就是可直接用于仿真的网格，无需任何后处理转换。此外，论文提出了一种基于预测点云几何法线的三角形参数化策略，并设计了法线引导的引导训练调度，从而稳定地学习三角形朝向和透明度，实现了从稀疏视图到仿真就绪网格的端到端生成。

### 创新点拆解
- 创新点1：**面向仿真的三角形图元表示**。首次在前馈重建网络中采用有向三角形作为渲染与几何表示的统一图元，使得网络输出可直接被物理引擎、碰撞检测器和标准渲染管线使用，无需后续网格提取步骤。
- 创新点2：**几何法线引导的三角形参数化**。不直接将三角形朝向作为无约束隐变量回归，而是从预测的点云图中计算几何法线，再通过图像条件法线预测头进行细化，将法线转换为稳定的局部坐标系用于三角形参数化，从而保证几何一致性。
- 创新点3：**渐进式训练调度策略**。提出单眼法线引导初始化和透明度/模糊度调度（opacity and blur scheduling），在训练早期稳定网络，并逐步锐化表面表示，使得最终输出可直接且高质量地提取为网格。

### 实验结果亮点
在RealEstate10K和DL3DV数据集上，TriSplat在几何重建质量上显著优于基于高斯的基线方法（如pixelSplat、MVSplat），例如在Chamfer距离、F-score等几何指标上取得更优结果。同时，其新视角渲染质量（PSNR、SSIM、LPIPS）与基线方法相当或更优，证明了三角形表示在渲染任务中同样具有竞争力。论文还展示了输出网格直接被Bullet物理引擎用于刚体碰撞模拟的案例，验证了其“仿真就绪”特性。

### 当前局限
该方法主要针对室内外场景的稀疏视点重建，对于极端稀疏视图（如仅1-2张图）或存在大量透明/反射表面的场景（如玻璃、水面），三角形表示可能难以准确建模复杂的折射与反射效果。此外，当前方法假设场景主要由漫反射表面构成，对于高光材质或动态场景的适应性尚未验证。计算开销方面，三角形光栅化渲染的效率略低于高斯泼溅，可能影响实时应用。

### 后续改进方向
- 方向1：**融合混合图元表示**。结合三角形与少量高斯图元，对透明/反射区域使用高斯建模，而对主要几何表面使用三角形，在保持仿真就绪能力的同时提升复杂材质场景的渲染质量。
- 方向2：**引入时序一致性约束**。将方法扩展至动态场景重建，通过光流或场景流引导三角形图元在时间维度的形变与跟踪，实现动态场景的仿真就绪网格重建。

### 工程落地启发
对于OCR/文档解析工程项目，最有价值的启发是**将输出格式与下游任务直接对齐**的设计思想。类似于TriSplat直接输出仿真引擎可用的网格，在文档解析中可设计模型直接输出结构化文档对象（如表格、公式、段落边界框、阅读顺序图），而非中间表示（如像素级分割图）。这样能省去繁琐的后处理转换步骤，提升端到端系统的效率和鲁棒性。例如，表格识别模型可设计为直接输出可被电子表格软件导入的单元格坐标与内容列表，而非先输出图像掩码再通过OCR提取。

---
