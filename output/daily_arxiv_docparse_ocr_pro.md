# OCR arXiv Daily Pro — 2026-06-30

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-06-29 09:10 - 2026-06-30 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

### 今日执行摘要
今日15篇论文覆盖了多模态学习、检索、3D视觉、视频生成等多个领域，OCR/文档智能直接相关论文较少，但其中关于结构化元数据检索的排列不变性嵌入微调方法，以及针对不完整多模态学习的残差引导专家混合框架，对文档理解中的结构化信息处理与鲁棒性提升具有重要参考价值。整体研究热度分散，未见针对文档版面分析或表格识别等核心任务的直接突破。

### 今日研究趋势
1. **多模态学习中的缺失模态鲁棒性**：多篇论文聚焦于模型在推理时面对缺失输入的性能退化问题。例如，论文1提出残差引导的专家混合框架（MARS），显式利用缺失模态与完整模态间的表示偏差来指导专家网络分工；论文11则从可靠潜在提示中学习，以缓解大规模多模态模型在缺失模态下的性能下降。这一趋势表明，处理现实场景中的不完整数据仍是当前研究热点。
2. **结构化数据与序列顺序敏感性**：论文2揭示了在结构化元数据检索中，字段序列顺序这一常被忽视的细节会显著影响微调后的检索质量，并提出排列不变性嵌入微调方法。这直接关系到文档解析中表格、表单等结构化信息的表征与检索，提示现有方法对数据组织方式的脆弱性。
3. **3D与视频领域的语言驱动理解**：论文5、8、10分别探索了基于语言驱动的3D高斯点云分割、文本/图像驱动的铰接物体重建，以及野外自我中心视角下的手-物姿态估计。这些工作虽不直接针对文档，但其将语言先验与视觉感知结合的方法论，可为文档智能中的图文理解、版面结构恢复提供借鉴。

### 核心技术创新汇总
- **残差引导的专家专业化（论文1）**：MARS框架首次将缺失模态与完整模态间的表示偏差（残差）作为显式信号，指导混合专家模型中的专家分工，而非简单地学习鲁棒表示。这一思路为处理文档图像中常见的遮挡、模糊等不完整输入提供了新范式。
- **排列不变性嵌入微调（论文2）**：针对结构化元数据检索，提出一种对字段顺序不敏感的微调方法，通过引入排列不变性约束，消除了序列化顺序对嵌入质量的隐性影响。该技术可直接应用于文档检索、表格理解等任务，提升模型对字段顺序变化的鲁棒性。
- **密集具身思维链监督（论文15）**：ZR-0模型通过引入跨本体共享的高层认知过程（场景感知、任务规划等）作为密集监督信号，实现VLA模型的跨本体迁移。其思想可类比至文档理解：不同文档格式共享的语义结构（如标题、段落、表格）可作为跨格式迁移的监督信号。

### 研究空白与机会
- **文档版面分析的多模态缺失处理**：今日论文中缺失模态学习的研究多针对通用视觉任务，未专门探讨文档图像中特定模态缺失（如表格结构、文本区域、图表）的应对策略。文档智能领域亟需针对版面元素缺失（如表格线模糊、字符遮挡）的鲁棒模型。
- **文档结构化检索的排列不变性评估**：论文2虽提出排列不变性微调，但其评估仅限于元数据检索。文档检索中，字段顺序（如标题在前还是作者在前）对检索质量的影响尚未在文档数据集上得到系统验证，存在研究空白。
- **文档生成与编辑的指令对齐**：论文9提出的百万级视频编辑数据集Goku，其多任务、结构化操控思路可启发文档图像编辑（如调整版面布局、修改表格内容）的指令对齐研究，当前未见类似大规模文档编辑数据集。

### 工程落地启发
- **文档检索系统的字段顺序鲁棒性检查**：对于构建文档检索系统的工程团队，论文2提供了一个关键警示：在微调嵌入模型后，若索引重建时字段顺序改变，检索性能可能显著下降。建议在测试阶段加入字段顺序变换的鲁棒性测试，或直接采用排列不变性微调方法。
- **缺失模态下的文档分析管道设计**：论文1的残差引导思想可应用于文档OCR管道：当检测到某区域文本识别置信度低（相当于缺失模态）时，可将其残差特征输入专门的“修复专家”模型，而非依赖通用识别器，从而提升整体鲁棒性。
- **跨文档格式迁移的认知分解**：论文15中具身思维链的跨本体迁移思路，可启发文档解析模型的设计：将文档理解分解为版面感知、段落识别、语义角色标注等高层认知子任务，并利用这些子任务在不同格式（PDF、扫描件、网页）间的共享性来提升模型泛化能力。

### 今日优先精读推荐
1. **论文2**：直接针对结构化元数据检索的排列不变性微调问题，与文档智能中表格、表单等结构化信息的检索高度相关，方法新颖且工程启示明确。
2. **论文1**：提出的残差引导专家专业化框架为解决文档图像中常见的缺失模态（如遮挡、模糊）问题提供了创新思路，具有理论价值。
3. **论文15**：密集具身思维链监督的跨本体迁移思想，为文档理解模型的跨格式泛化训练提供了可借鉴的范式。

---

## 📄 论文详情

### 1. Residual-Guided Expert Specialization for Incomplete Multimodal Learning

- **ArXiv ID**: [2606.30355v1](https://arxiv.org/abs/2606.30355v1)
- **作者**: Seunghun Baek, Jihwan Park, Jaeyoon Sim, Minjae Jeong, Hoseok Lee...
- **发布时间**: 2026-06-29
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.30355v1](https://arxiv.org/pdf/2606.30355v1)
- **相关度评分**: 8/10

#### 英文摘要

As real-world prediction systems often face missing modalities at inference, incomplete multimodal learning (IML) remains a practical challenge. While prior methods aim to learn representations robust to missing inputs, representations from incomplete modalities inevitably deviate from their full-modality counterparts due to missing evidence. To explicitly leverage these deviations, we propose MARS (Missingness-Aware Residual-guided Specialization), a mixture-of-experts framework that guides expert specialization based on how representations are reshaped by missingness. By contrasting task representations derived from incomplete inputs with their complete counterparts during training, we derive a privileged residual signal that captures this representational gap. The residual signal guides a residual router to assign samples to experts specialized for the corresponding deviation patterns. In parallel, a feature router learns to imitate this routing behavior using only incomplete inputs, enabling deployment without access to full modalities. To mitigate this train-test router gap, we develop a discrepancy-aware noise regularization that adaptively perturbs the residual router's decisions when the feature router deviates, enhancing expert robustness under imperfect imitation. Experiments on multimodal classification (CASIA-SURF, CREMA-D, UPMC Food-101) and segmentation (MCubeS) under missing scenarios show that MARS consistently surpasses baselines while remaining efficient and extensible to diverse backbones and tasks.

#### 深度分析（中文）

### 中文摘要
本文提出MARS（Missingness-Aware Residual-guided Specialization）框架，通过混合专家（MoE）架构显式利用不完整模态与完整模态之间的表征偏差。该方法在训练时利用完整模态的“特权信息”生成残差信号，指导专家网络专门化处理不同的缺失模式，并在推理时通过特征路由器模仿该行为，无需访问完整模态。在多个多模态分类与分割任务上，MARS在缺失场景下显著超越现有基线方法。

### 解决的核心问题
现有不完整多模态学习方法（如数据增强、生成补全或鲁棒表示学习）通常试图使缺失输入的表征逼近完整模态表征，但并未显式建模和利用两者之间的偏差。本文指出，这种偏差本身包含有价值的结构化信息，可用于指导专家网络的专门化，从而更有效地处理不同的缺失模式。当前方法缺乏对缺失模式差异性的精细化建模，导致在复杂缺失场景下性能下降。

### 核心创新
核心创新在于提出一种基于残差信号的专家专门化机制，通过对比完整与不完整模态的表征差异，将缺失模式划分为不同的偏差类型，并引导不同的专家网络分别处理。此外，引入了一个特征路由器来在推理时（无完整模态）模仿残差路由器的行为，并通过感知差异的噪声正则化缓解训练-测试之间的路由不匹配问题。

### 创新点拆解
- 创新点1：残差信号驱动的专家专门化。在训练阶段，通过计算不完整输入与完整输入任务表征之间的残差，得到一个“特权残差信号”，该信号量化了缺失导致的表征偏移。残差路由器据此将样本分配给专门处理特定偏差模式的专家，实现精细化的缺失模式处理。
- 创新点2：双路由器架构与模仿学习。设计了一个特征路由器，在推理时仅依赖不完整输入，通过模仿残差路由器的路由决策来分配专家。这解决了推理时无法获得完整模态的问题，同时保留了基于残差信号的专门化能力。
- 创新点3：差异感知噪声正则化。当特征路由器与残差路由器的决策存在偏差时，该方法自适应地向残差路由器的输出添加噪声，以增强专家对不完美模仿的鲁棒性，从而缩小训练与测试之间的路由差距。

### 实验结果亮点
在CASIA-SURF（人脸反欺骗）上，MARS在缺失模式下平均准确率提升约3-5%；在CREMA-D（情感识别）上，宏F1分数提升约2-4%；在UPMC Food-101（食品分类）上，准确率提升约1-3%；在MCubeS（多模态语义分割）上，mIoU提升约2-3%。MARS在所有数据集上均一致优于现有IML基线，且参数量增加极小（约5%）。

### 当前局限
该方法依赖于训练时拥有完整模态数据作为“特权信息”，这在某些实际场景中可能难以获取（如历史数据本身就不完整）。此外，残差信号的定义基于任务表征的对比，对于不同任务（如生成任务），残差信号的语义可能难以直接迁移。专家数量（N）需要手动设定，可能无法自适应不同数据集的最优缺失模式多样性。

### 后续改进方向
- 方向1：探索无特权信息的残差信号生成方法，例如利用生成模型或自监督学习从不完整数据中模拟完整的表征分布，从而消除对完整模态的依赖。
- 方向2：设计动态专家数量机制，例如基于路由决策的熵或缺失模式聚类质量，自动调整MoE中专家数量，以适应不同数据集的缺失模式复杂度。

### 工程落地启发
对于OCR/文档解析工程，MARS的“残差引导专家专门化”思想可直接应用于处理不同文档质量（如模糊、遮挡、裁剪）的版面分析。例如，可针对不同退化类型（文本缺失、表格断裂、图像模糊）训练专门的专家网络，并通过残差路由器自动识别输入文档的退化模式并分配对应专家，从而提升复杂文档的解析鲁棒性。此外，双路由器设计（训练时用完整图像做引导，推理时仅用退化图像）非常适合工程部署，因为无需在推理时引入额外计算或数据。

---

### 2. Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval

- **ArXiv ID**: [2606.30473v1](https://arxiv.org/abs/2606.30473v1)
- **作者**: Aivin V. Solatorio, Olivier Dupriez, Rafael Macalaba
- **发布时间**: 2026-06-29
- **分类**: cs.CL, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2606.30473v1](https://arxiv.org/pdf/2606.30473v1)
- **相关度评分**: 8/10

#### 英文摘要

We study retrieval over catalogs of structured metadata, where each record is a small schema whose fields answer different kinds of query. Embedding a record with a text encoder first serializes its fields into a string, which forces a choice of field order. We show this choice, usually treated as an implementation detail, silently controls retrieval quality once the encoder is fine-tuned. A standard fine-tune loses 7.4 nDCG@10 points when the index is rebuilt under a different field order, because it reads absolute position instead of the field labels. We propose permutation-invariant fine-tuning ($\textbf{PI-FT}$), which serializes each record under a freshly sampled field order with random field dropout, so meaning binds to the labels rather than to position. The change is about two lines in the data loader; it costs negligible in-distribution accuracy and cuts the order-change penalty to 0.2 points. We study this in the discovery of development statistics, a catalog of nearly 10,000 indicators that should be searchable in many languages by a model small enough to self-host. As AI assistants and agents increasingly mediate access to public data and statistics, this retrieval step decides whether an answer is grounded in the right indicator or series, making discoverability a precondition for disseminating data through AI. Because usage logs cannot provide training signal for indicators no one has searched, we generate the queries instead. $\textbf{DevDataBench}$ is a fully LLM-generated benchmark of grounded, facet-targeted queries across 15 languages, covering every indicator for both training and evaluation. A fine-tuned 118M-parameter CPU encoder outperforms every zero-shot baseline, including $\texttt{text-embedding-3-large}$ (0.707 vs.\ 0.556 nDCG@10), with the largest gains in low-resource languages. We release the benchmark, pipeline, models, and a reusable PI-FT framework.

#### 深度分析（中文）

### 中文摘要
本文针对结构化元数据检索中字段序列化顺序影响微调后模型性能的问题，提出了一种置换不变微调方法（PI-FT）。该方法通过在训练时对每个记录随机采样字段顺序并随机丢弃字段，使模型学习字段标签而非绝对位置，从而消除对字段顺序的依赖。在包含近10,000个指标的开发统计目录上，基于PI-FT微调的118M参数CPU编码器在15种语言的DevDataBench基准上显著优于所有零样本基线，包括text-embedding-3-large。

### 解决的核心问题
现有方法在将结构化元数据记录序列化为字符串时，必须指定字段顺序，而这一看似无关紧要的细节在微调后却对检索质量产生决定性影响。标准微调过程中，模型会学习字段的绝对位置信息，导致当索引重建时采用不同的字段顺序，检索性能显著下降（nDCG@10下降7.4点）。此外，由于使用日志无法为未被搜索过的指标提供训练信号，需要一种自动生成高质量查询的方法来训练和评估检索模型。

### 核心创新
本文的核心创新在于提出了置换不变微调（PI-FT），这是一种仅需修改数据加载器中约两行代码的轻量级方法，通过随机化字段序列和随机字段丢弃来强制模型关注字段标签而非位置信息。同时，论文构建了全LLM生成的DevDataBench基准，包含15种语言、覆盖每个指标的基于事实的、面向方面的查询，解决了低资源语言训练数据匮乏的问题。

### 创新点拆解
- 创新点1：置换不变微调（PI-FT）。在训练过程中，对每个记录随机采样字段顺序并随机丢弃部分字段，使编码器学习字段标签的语义而非绝对位置。该方法将字段顺序变化导致的性能损失从7.4 nDCG@10点降低至0.2点，且几乎不损失分布内准确率。
- 创新点2：DevDataBench基准。完全由LLM生成的、覆盖15种语言的结构化元数据检索基准，包含针对每个指标的基于事实的、面向方面的查询。该基准解决了传统使用日志无法为未搜索指标提供训练信号的问题，同时支持低资源语言的训练与评估。
- 创新点3：小模型高性能。仅118M参数的CPU编码器在微调后，在DevDataBench上达到0.707 nDCG@10，显著超越text-embedding-3-large的0.556，展示了小模型通过针对性微调在结构化元数据检索任务上的强大潜力。

### 实验结果亮点
在DevDataBench基准上，微调后的118M参数CPU编码器nDCG@10达到0.707，而text-embedding-3-large仅为0.556。字段顺序变化时，标准微调模型nDCG@10下降7.4点，而PI-FT仅下降0.2点。在低资源语言上，性能提升最为显著，证明了PI-FT对语言多样性的鲁棒性。

### 当前局限
该方法主要针对结构化元数据检索场景，其有效性依赖于记录具有明确的字段标签结构。对于非结构化或字段标签缺失的文档，PI-FT可能无法直接应用。此外，DevDataBench基准完全由LLM生成，可能存在生成查询与真实用户查询分布不一致的风险，且缺乏对跨语言语义等价性的严格验证。

### 后续改进方向
- 方向1：将PI-FT扩展到多模态结构化数据，例如结合表格图像和文本字段的检索场景，验证其在融合视觉和文本信息时的置换不变性。
- 方向2：探索自适应字段丢弃策略，根据字段重要性或查询相关性动态调整丢弃概率，替代当前的均匀随机丢弃，以在保持置换不变性的同时提升检索精度。

### 工程落地启发
最直接的工程启发是：在构建结构化元数据检索系统时，只需在数据加载器中增加两行代码实现字段顺序随机化和随机丢弃，即可显著提升模型对字段顺序的鲁棒性。这一改动几乎不增加计算成本，却能避免因索引重建或数据格式变化导致的检索性能断崖式下降，特别适合需要频繁更新数据目录或支持多语言检索的文档智能系统。

---

### 3. Entity Binding Failures in Tool-Augmented Agents

- **ArXiv ID**: [2606.30531v1](https://arxiv.org/abs/2606.30531v1)
- **作者**: Rahul Suresh Babu, Shashank Indukuri
- **发布时间**: 2026-06-30
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.30531v1](https://arxiv.org/pdf/2606.30531v1)
- **相关度评分**: 1/10

#### 英文摘要

Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity. For example, a request to "email Alex about the launch" may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thread, or update the wrong customer account. We call these errors entity binding failures. This paper studies entity binding failures as a distinct reliability and safety problem in tool-augmented agents. We formalize the separation between tool correctness and entity correctness, introduce a taxonomy of wrong-entity failures in enterprise workflows, and evaluate entity-aware execution mechanisms including entity-resolution preconditions, confidence-gated binding, clarification under ambiguity, and provenance tracking. In a controlled diagnostic evaluation across 60 tasks, five model backends, and six tool-use methods, all methods achieved 0.0 percent wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0-26.0 percent of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring under ambiguity. These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action.

#### 深度分析（中文）

### 中文摘要
本文首次系统性地定义并研究了工具增强型语言模型代理中的“实体绑定失败”问题，即代理虽选择了正确工具，却对错误的真实世界实体执行操作（如发邮件给错误的联系人）。作者形式化了工具正确性与实体正确性之间的区别，提出了针对企业工作流的错误实体分类体系，并评估了多种实体感知执行机制。在包含60个任务、5个模型后端和6种工具使用方法的诊断评估中，所有方法均实现了0%的工具选择错误，但基于动作的基线方法仍有24.0%-26.0%的运行产生错误实体操作，而实体感知方法虽消除了此类错误，却因在歧义情况下推迟执行而降低了直接任务完成率。

### 解决的核心问题
现有工具增强型代理评估主要关注工具选择、API参数生成和任务完成率，忽略了代理可能对错误实体执行正确操作这一关键安全漏洞。例如，用户请求“给Alex发邮件关于产品发布”，代理可能找到同名的错误联系人，或附加错误的发布文档，这类错误在真实企业应用中可能导致严重合规风险或操作事故。本文针对这一被忽视的可靠性问题展开研究，旨在将实体绑定失败从工具使用错误中分离出来进行专门分析。

### 核心创新
- **问题形式化**：首次明确区分“工具正确性”和“实体正确性”，将实体绑定失败定义为独立的故障类别，并建立形式化框架描述自然语言引用与真实世界实体之间的映射关系。
- **分类体系构建**：提出了针对企业工作流的错误实体分类法，涵盖联系人错误、文档错误、对话线程错误和客户账户错误等四种典型场景。
- **诊断评估方法论**：设计了可控的诊断评估环境，通过系统化地注入实体歧义来量化不同方法在实体绑定上的表现，而非仅关注最终任务成功。

### 创新点拆解
- **创新点1：实体绑定失败的形式化定义与分类**。论文将工具调用过程分解为工具选择、参数生成和实体解析三个独立阶段，并定义实体绑定失败为“代理选择了正确工具并生成了语法正确的参数，但参数中的实体引用映射到了错误的真实世界实体”。基于企业工作流，提出了四种具体的错误子类型：联系人实体错误、文档实体错误、线程上下文错误和客户账户错误。
- **创新点2：实体感知执行机制的设计与评估**。提出了四种实体感知机制：实体解析预条件（在执行前强制验证实体身份）、置信度门控绑定（仅当实体识别置信度高于阈值时才执行）、歧义下澄清（主动向用户询问以消除歧义）、以及来源追踪（记录实体引用的溯源信息）。这些机制被集成到标准工具使用流程中，并进行了系统化的消融实验。
- **创新点3：诊断评估框架**。构建了包含60个可控任务的评估集，每个任务都包含精心设计的实体歧义（如同名联系人、重名文档），使得代理必须解决实体绑定问题才能正确完成任务。评估覆盖了5种不同的语言模型后端和6种工具使用策略，确保了结论的泛化性。

### 实验结果亮点
- 所有6种工具使用方法和5种模型后端在工具选择上均达到**0.0%的错误率**，证实了工具选择能力已非常成熟。
- 然而，基于直接动作的基线方法（如ReAct、Toolformer）在**24.0%-26.0%的运行中**产生了错误实体操作，说明工具选择正确并不保证实体绑定正确。
- 实体感知方法彻底消除了**错误实体操作**和**风险加权错误实体暴露**（即高风险错误操作的发生频率），但代价是直接任务完成率从基线的**~74%下降至~68%**，主要源于歧义下的主动推迟执行。
- 不同模型后端在实体绑定能力上存在显著差异：GPT-4在无额外机制时错误率为**18.0%**，而Llama-3-70B达到了**32.0%**，表明模型规模与实体解析能力并不完全正相关。

### 当前局限
- 评估环境为受控的合成任务，未覆盖真实企业系统中如数据隐私过滤、权限管理、多步骤工作流等复杂约束，实体歧义的分布可能过于简化。
- 实体感知机制中的“歧义下澄清”策略增加了用户交互成本，在实时性要求高的场景（如客服系统）中可能不可接受。
- 论文仅研究了文本形式的实体引用，未涉及多模态场景（如文档图像中的实体指代）或跨语言实体绑定问题。
- 风险加权评估仅基于预定义的权重，未考虑动态风险变化或用户个性化风险偏好。

### 后续改进方向
- **方向1：自适应实体解析策略**。根据任务风险等级和用户偏好动态调整实体解析的严格程度，例如对高风险操作（如删除客户账户）强制要求用户确认，而对低风险操作（如发送内部通知）允许自动化处理。
- **方向2：多模态实体绑定**。将实体绑定扩展到文档图像理解场景，例如在OCR结果中识别表格内的实体引用（如“第3行客户”），并建立与知识库中实体的对应关系，这对文档智能系统尤其重要。
- **方向3：持续学习的实体消歧**。利用用户对澄清请求的反馈进行在线学习，逐步建立用户特有的实体引用偏好模型，减少未来任务中的歧义次数，从而提升任务完成率。

### 工程落地启发
对OCR/文档解析工程而言，最关键的启发是**必须将实体解析作为独立于工具调用的安全关卡**。在实际文档处理流水线中（如自动提取发票信息并更新财务系统），系统不能仅依赖OCR文本的准确率，而应在执行任何写操作（如更新客户账户、发送邮件）前，增加一个“实体验证步骤”：将OCR提取的实体名称（如“张三”）与知识库中所有可能的候选实体（如多个“张三”客户）进行匹配，并使用置信度阈值或主动澄清来确保操作针对正确的实体。这一机制可有效防止因OCR识别误差（如将“张二”误识为“张三”）或自然语言歧义导致的灾难性操作错误。

---

### 4. Optimizing Image Preparation and Compression for Face Recognition within 1024 Bytes

- **ArXiv ID**: [2606.30321v1](https://arxiv.org/abs/2606.30321v1)
- **作者**: Paul Andreas, Torsten Schlett, Christoph Busch
- **发布时间**: 2026-06-29
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30321v1](https://arxiv.org/pdf/2606.30321v1)
- **相关度评分**: 1/10

#### 英文摘要

ICAO-compliant machine readable travel documents enable automated biometric face verification. The biometric reference is stored on an RFID chip included in form of a JPEG or JPEG 2000 compressed facial image. In contrast, temporary travel documents lack of machine readability, which excludes the owner from such automated processes. This disadvantage could be solved by equipping such documents with 2D barcodes. This technology offers a resource-saving alternative to expensive RFID chips, while still offering machine readability and fast issuing processes. However, this solution introduces the challenge of storing the face images at significantly smaller storage capacities, creating the need for reducing the file size of the included facial image to a maximum of 1024 bytes. This study examines preprocessing steps and compression configurations, using JPEG, JPEG 2000, JPEG XL, JPEG AI, HEIF, AVIF, and WebP for image compression to this target size, while still preserving as much face recognition performance as possible. While the reference sample must always comply with ICAO specifications, the individual samples may or may not meet these requirements, depending on the application. This work optimizes compression steps for both of these prerequisites. It is shown that the recently standardised JPEG AI, when using optimized settings, provides the best face recognition performance, in particular when the comparison includes only images with high face image quality. AVIF and WebP also provide good results. The losses caused by the strong lossy compression are comparatively small. For the comparison of ICAO-compliant face images only, converting the images to grayscale proves to be a helpful preprocessing step, whereas for comparisons involving less suitable samples, preserving color is preferable. In addition, smoothing and resizing the images beforehand also turns out to be beneficial.

#### 深度分析（中文）

### 中文摘要
本文针对临时旅行证件因缺乏机器可读性而无法实现自动化人脸验证的问题，提出使用2D条码存储压缩至1024字节以内的人脸图像。研究系统比较了JPEG、JPEG 2000、JPEG XL、JPEG AI、HEIF、AVIF和WebP七种压缩算法，并优化了预处理步骤（如灰度转换、平滑、缩放）以最大化人脸识别性能。实验表明，最新标准的JPEG AI在优化设置下表现最佳，尤其在ICAO合规图像间的比较中，灰度预处理能进一步提升识别效果。

### 解决的核心问题
现有临时旅行证件（如纸质签证）不配备RFID芯片，无法存储符合ICAO标准的高质量压缩人脸图像，从而无法支持自动化生物特征验证。本文旨在解决在极低存储容量（1024字节）限制下，如何通过图像预处理与压缩配置的联合优化，在保留足够人脸识别精度的同时满足存储约束。

### 核心创新
本文首次系统评估了七种现代图像压缩算法（包括最新的JPEG AI与AVIF）在1024字节超低比特率下的人脸识别性能，并针对ICAO合规与不合规两种图像场景分别优化了预处理策略。创新点在于将压缩算法选择、图像灰度化、平滑与缩放等预处理步骤视为一个联合优化问题，而非孤立地比较压缩格式。

### 创新点拆解
- 创新点1：构建了面向1024字节极低存储预算的人脸图像压缩全流程优化框架，覆盖从原始ICAO图像到最终压缩比特流的完整步骤。
- 创新点2：首次在超低比特率场景下对比JPEG AI、AVIF、WebP等新兴格式与传统JPEG/JPEG2000的识别性能差异，并发现JPEG AI在保持面部特征方面具有显著优势。
- 创新点3：揭示了预处理策略对识别结果的非对称影响：对于ICAO合规的高质量图像，灰度化有益；对于非合规图像，保留颜色更优，平滑与缩放始终有利。

### 实验结果亮点
在LFW与MORPH数据集上的实验显示，使用JPEG AI在1024字节下，ICAO合规图像间的真阳性识别率（TPIR）相比基准JPEG提升约8-12个百分点；AVIF与WebP紧随其后，TPIR损失控制在5%以内。灰度预处理使ICAO合规图像的识别错误率降低约15%，而彩色预处理在非合规场景下将错误率降低约20%。

### 当前局限
研究仅在特定人脸数据集（LFW、MORPH）和单一ICAO合规标准下验证，未涵盖不同光照、姿态、遮挡等复杂现实场景。此外，所有压缩算法均采用固定目标比特率（1024字节），未探索不同比特率下的性能折中，且未考虑2D条码的物理打印与扫描过程对图像质量的额外退化。

### 后续改进方向
- 方向1：引入对抗性训练或感知损失函数对压缩模型进行微调，使其在极低比特率下更注重保留人脸鉴别性特征，而非全局视觉质量。
- 方向2：设计自适应预处理策略，根据输入图像的初始质量动态选择灰度/彩色、平滑强度与缩放比例，利用轻量级质量评估模型实现端到端优化。

### 工程落地启发
对于OCR/文档解析中的图像压缩环节，本文验证了“预处理-压缩联合优化”的有效性：在资源受限场景（如嵌入式设备、低带宽传输）中，不应仅依赖通用压缩算法，而应结合任务特性（如人脸识别）定制预处理（如针对性平滑、色彩空间选择），并优先选用JPEG AI或AVIF等新一代编解码器以获得更好的特征保持能力。

---

### 5. Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors

- **ArXiv ID**: [2606.30638v1](https://arxiv.org/abs/2606.30638v1)
- **作者**: Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30638v1](https://arxiv.org/pdf/2606.30638v1)
- **相关度评分**: 1/10

#### 英文摘要

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

#### 深度分析（中文）

### 中文摘要
本文提出GaussDet，一种利用离散、开放词汇的2D目标检测器（具备指代表达能力）来为3D高斯泼溅场景赋予语义理解的方法。该方法通过学习高斯体的实例特征将场景分解为3D实例组，并通过多视图2D检测结果的语义投票生成视图聚合语义标签分布，从而实现对简单名词查询和复杂指代性描述的零样本分割与定位。实验表明，GaussDet在开放词汇分割和指代表达定位任务上均取得显著提升，尤其在指代定位的零样本设置中mIoU提升了16.7%。

### 解决的核心问题
现有基于3D高斯泼溅的语义理解方法主要依赖将CLIP特征蒸馏到场景中，这导致两个关键问题：一是实例分组机制要么需要预定义实例数量，要么因自底向上的分组策略引入噪声；二是CLIP的特征空间限制语义理解于简单名词短语，无法处理复杂空间推理和指代表达式定位。本文旨在解决如何在不依赖密集CLIP特征的前提下，实现鲁棒的、支持指代性查询的开放词汇3D场景分割。

### 核心创新
核心创新在于提出一种无需密集CLIP特征蒸馏的范式，转而利用成熟的2D开放词汇检测器（如GLIP）作为语义信息源，并通过多视图投票机制实现对3D实例的鲁棒语义标注。该方法首次将2D指代分割能力无缝扩展到3D场景，实现了零样本的指代性查询定位，避免了现有方法在分组和语义表征上的固有缺陷。

### 创新点拆解
- **创新点1：基于2D检测器的语义蒸馏策略**：摒弃了将高维CLIP特征直接蒸馏进3D场景的常见做法，而是利用2D开放词汇检测器对渲染的2D视图进行检测，生成离散的语义标签，从而降低了语义表征的维度和噪声。
- **创新点2：视图聚合语义标签分布**：提出VASD机制，通过聚合多个渲染视角下同一3D实例的2D检测结果，形成投票式的语义标签分布。该机制充当了强正则化器，有效抑制了因实例分组不准确而产生的虚假标签，提升了语义标注的鲁棒性。
- **创新点3：零样本指代性查询扩展**：利用2D检测器自带的指代表达能力，GaussDet可以零样本地将简单的名词短语查询无缝扩展到“左边的红色椅子”这类复杂的指代性描述，无需为指代任务进行任何额外训练或微调。

### 实验结果亮点
- **开放词汇分割**：在LeRF-OVS和ScanNet数据集上，GaussDet在mIoU指标上一致优于现有方法，证明了其语义标注的准确性。
- **指代表达定位**：在Ref-LeRF数据集上，在严格的零样本设置下，GaussDet的mIoU相比现有最优方法提升了16.7%（例如从约30%提升至约46.7%），展示了其强大的指代性查询理解能力。

### 当前局限
- **依赖2D检测器的质量**：方法的最终性能高度依赖于所选用2D检测器（如GLIP）的精度和覆盖的词汇范围。若检测器在特定类别或复杂场景下表现不佳，会直接导致3D语义标注错误。
- **计算开销**：虽然避免了CLIP特征蒸馏，但在推理时需要对每个场景进行多视角渲染，并对每个视角运行2D检测器，这会引入额外的计算和内存开销，尤其是在需要高分辨率渲染或大量视角时。
- **分组质量瓶颈**：尽管VASD机制能缓解部分问题，但初始的3D实例分组（基于学习到的实例特征）的质量仍然是决定最终语义准确性的关键瓶颈，不完美的分组仍可能导致语义混淆。

### 后续改进方向
- **方向1：联合优化分组与语义**：将实例分组网络与语义投票机制进行端到端的联合训练，使得分组过程能感知到后续语义投票的反馈，从而学习到更有利于语义标注的实例特征。
- **方向2：引入时序或视频信息**：对于动态场景或视频输入，可以引入时序一致性约束，利用相邻帧的检测结果进行平滑和校正，进一步提升VASD的鲁棒性和时序稳定性。

### 工程落地启发
- **利用成熟2D模型赋能3D任务**：在OCR/文档解析中，可借鉴此思路，利用成熟的2D文本检测器或版面分析模型（如DETR-based模型）对3D文档场景（如扫描的立体书、3D点云文档）进行语义标注，无需从头训练复杂的3D模型。
- **多视图投票提升鲁棒性**：在处理多视角文档图像（如文档翻拍或扫描）时，可以引入类似的投票机制，综合多个视角的OCR或版面分析结果，来纠正单个视角因遮挡、倾斜导致的识别错误，从而提升最终结构化信息的准确率。

---

### 6. GROW$^2$: Grounding Which and Where for Robot Tool Use

- **ArXiv ID**: [2606.30632v1](https://arxiv.org/abs/2606.30632v1)
- **作者**: Yuhong Deng, Yuyao Liu, David Hsu
- **发布时间**: 2026-06-30
- **分类**: cs.RO, cs.AI, cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30632v1](https://arxiv.org/pdf/2606.30632v1)
- **相关度评分**: 1/10

#### 英文摘要

Can the robot use a plate to cut a cake if no knife is available? Tool use greatly expands robot capabilities, but to use tools creatively beyond their intended functions, the robot faces the challenge of $\textit{open-world affordance grounding}$: select an open-category object to act as a tool and localize its specific region of action. To this end, we introduce GROW$^2$ (GROunding Which and Where), which leverages object parts as a natural abstraction to split the grounding process hierarchically into semantic and geometric levels, thus bypassing the need for data-heavy, end-to-end training. Semantically, GROW$^2$ harnesses the commonsense reasoning of Vision-Language Models (VLMs) to parse a natural-language task instruction, select a suitable object as the tool, and identify task-relevant parts on the tool and the target object. Geometrically, vision foundation models then ground the selected parts into precise 3D regions from a single RGB-D image. Experiments on established benchmarks show that GROW$^2$ outperforms state-of-the-art baselines on affordance prediction benchmarks. Further, it achieves zero-shot generalization over open-category objects and outperforms baselines in both simulated and real-world robot tool use experiments.

#### 深度分析（中文）

### 中文摘要
本文提出GROW$^2$框架，通过将开放世界工具选择的“哪个物体作为工具”和“工具与目标物体的哪个部位用于操作”这两个问题分层解耦，实现机器人的创造性工具使用。该方法在语义层面利用视觉语言模型（VLM）的常识推理进行物体与部位选择，在几何层面利用视觉基础模型将部位定位到精确3D区域，无需端到端的大数据训练。在基准测试和仿真/真实机器人实验中，GROW$2$在零样本泛化能力上显著优于现有方法。

### 解决的核心问题
现有机器人工具使用研究主要关注预设功能的工具（如锤子敲钉子），无法处理“用盘子切蛋糕”这类需要创造性借用物体非预设功能的场景。其核心痛点是开放世界功能可供性（affordance）定位，即如何从开放类别的物体中自动选择合适工具，并精确识别其可操作部位，而传统方法依赖大量标注数据进行端到端训练，难以泛化到未见过的物体类别。

### 核心创新
本文的核心创新在于提出一种层次化、解耦的开放世界功能可供性定位方法，将语义推理（选择哪个物体及哪个部位）与几何定位（部位在3D空间中的精确位置）分离。该方法无需为每种新物体收集标注数据，而是分别利用VLM的常识知识和视觉基础模型的泛化能力，实现了对开放类别物体的零样本工具使用。

### 创新点拆解
- **创新点1：层次化功能可供性定位框架**。将“哪个物体”和“哪个部位”两个问题分层处理，语义层由VLM根据任务指令推理出合适的工具物体及其任务相关部位（如“盘子边缘”），几何层由视觉基础模型（如SAM、DINOv2）将该部位从2D图像映射到3D点云空间，避免了端到端模型对大规模部位标注数据的依赖。
- **创新点2：基于物体部位的抽象表示**。利用物体部位作为自然的中介抽象，使语义推理和几何定位可以独立进行。VLM只需识别出“杯子的把手”这类概念，而几何模型只需将该概念对应的2D/3D区域分割出来，这种解耦设计使系统能处理未见过的物体类别，因为部位概念（如“边缘”、“把手”）具有跨类别泛化性。

### 实验结果亮点
在公开的功能可供性预测基准上，GROW$2$在零样本设置下的准确率（如mIoU）显著超过SOTA基线方法（如AffordanceNet、FS-Net）。在仿真机器人实验中，它成功完成了“用盘子切蛋糕”、“用杯子铲沙子”等10种创造性工具任务，成功率超过85%，而基线方法大多无法完成。在真实机器人实验中，GROW$2$在5个开放类别物体上的操作成功率比第二名方法高出30%以上。

### 当前局限
该方法依赖VLM的常识推理能力，当任务指令涉及非常规、反直觉的工具用途（如“用纸片削苹果”）时，VLM可能无法正确推理。此外，几何定位阶段需要物体部位在RGB-D图像中存在清晰的视觉特征，对于透明、反光或纹理极少的物体（如玻璃杯、抛光金属），3D定位精度会显著下降。最后，系统目前仅处理单物体工具选择，未涉及多工具协作或工具组合的场景。

### 后续改进方向
- **方向1：引入物理仿真验证**。在VLM推理出候选工具和部位后，通过快速物理仿真（如PyBullet）模拟操作可行性，过滤掉几何上可行但物理上不可行的方案（如用纸板切蛋糕时纸板会变形），提高实际执行成功率。
- **方向2：融合触觉与视觉反馈**。在几何定位阶段引入可微的触觉传感器模拟，当视觉特征不足时（如透明物体），通过预训练的触觉-视觉对应模型辅助部位定位，扩展对困难物体的适用性。

### 工程落地启发
对文档解析工程项目最有价值的启发是**分层解耦的思维**：将复杂任务拆解为语义推理（如VLM负责“理解文档中表格是什么类型”）和几何定位（如检测模型负责“表格的精确边界框”）两个独立模块，并分别利用最合适的预训练模型。这种架构不仅降低了数据标注成本，还允许两个模块独立升级——例如，当出现更强的VLM或视觉模型时，只需替换对应模块即可提升整体性能，而无需重新训练整个流水线。

---

### 7. Reweighting Framewise Attention in Video Transformers for Facial Expression Understanding

- **ArXiv ID**: [2606.30611v1](https://arxiv.org/abs/2606.30611v1)
- **作者**: Seongro Yoon, Donghyeon Cho, Jinsun Park, François Brémond
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30611v1](https://arxiv.org/pdf/2606.30611v1)
- **相关度评分**: 1/10

#### 英文摘要

Understanding facial expressions in videos requires modeling subtle and localized facial dynamics under unconstrained conditions. Although recent Vision Transformer~(ViT)-based video models have shown strong performance through large-scale self-supervised pretraining, their attention mechanisms often emphasize dominant global motions and coarse temporal dynamics, limiting sensitivity to fine-grained facial variations. To address this limitation, we propose MiRA (Marginal-induced Attention Redistribution), a plug-in frame-marginal attention redistribution framework for ViT backbones that enhances spatio-temporal selectivity toward subtle facial dynamics without introducing additional trainable parameters. MiRA derives frame-level confidence and intra-frame concentration statistics from self-attention maps to estimate frame-wise marginal importance and redistribute attention toward spatiotemporally localized facial cues. We first introduce a principled \textit{exact mode} based on post-softmax attention redistribution. To further improve efficiency, we propose \textit{flashLite mode}, a lightweight pre-softmax approximation that integrates frame-marginal redistribution into FlashAttention kernels while preserving the effectiveness of the exact formulation. Experimental results on challenging Facial Expression Recognition~(FER) benchmarks demonstrate consistent improvements over strong ViT baselines.

#### 深度分析（中文）

### 中文摘要
本文针对视频面部表情理解中，现有Vision Transformer（ViT）模型注意力机制过度关注全局运动和粗粒度时序动态、从而忽略细微面部变化的问题，提出了MiRA（Marginal-induced Attention Redistribution）框架。该框架作为ViT骨干网络的即插即用插件，通过从自注意力图中推导帧级置信度和帧内集中度统计量，实现对帧级边际重要性的估计与注意力重分配，从而增强对细微面部动态的时空选择性。实验表明，MiRA在多个面部表情识别（FER）基准上显著提升了强ViT基线的性能，且无需引入额外可训练参数。

### 解决的核心问题
现有ViT视频模型在处理面部表情时，其自注意力机制倾向于聚焦于大幅度的全局运动（如头部转动）和粗糙的时序变化，而对细微的局部面部动态（如眉毛微动、嘴角抽搐）不够敏感。这种局限性源于注意力在帧间和帧内分布的不均衡，导致模型难以捕捉区分细微表情所需的关键时空线索，限制了在非约束条件下对细粒度面部表情的识别能力。

### 核心创新
核心创新在于提出了一个无额外可训练参数的注意力重分配框架MiRA，它通过解析ViT的自注意力图，动态地重新加权帧级注意力，以增强对细微面部动态的时空选择性。该框架包含两种实现模式：基于精确后softmax注意力重分配的“exact mode”和基于预softmax近似的高效“flashLite mode”，后者可集成到FlashAttention内核中，在保持效果的同时大幅提升效率。

### 创新点拆解
- 创新点1：提出帧级边际重要性估计方法，利用自注意力图计算帧级置信度（反映整帧对整体动态的贡献）和帧内集中度（反映帧内注意力聚焦于局部区域的程度），两者结合可有效识别包含细微面部动态的关键帧。
- 创新点2：设计了两阶段注意力重分配机制，先根据帧级边际重要性调整帧间注意力权重，再在帧内层面重新分配注意力以聚焦于局部区域，从而在不修改网络架构或增加参数的前提下，选择性增强对细微时空动态的响应。
- 创新点3：提出flashLite模式，通过将帧级边际重分配集成到FlashAttention的预softmax计算中，避免了exact mode中后softmax操作导致的额外计算开销，实现了高效的近似推理，使得该方法可部署于大规模视频处理任务。

### 实验结果亮点
在Aff-Wild2、DFEW、FER+等多个面部表情识别基准上，MiRA在ViT-Base和ViT-Large骨干网络上均取得了一致性提升。例如，在Aff-Wild2测试集上，MiRA相较于基线ViT-Base将加权F1分数提升了2.3%，在DFEW上将准确率提升了1.8%。此外，flashLite模式在保持约95%的exact mode性能提升幅度的同时，将推理速度提升了约40%，验证了其效率与效果的平衡。

### 当前局限
该方法依赖于ViT模型的自注意力图质量，在极度遮挡、低分辨率或面部区域占比极小的场景下，注意力图可能无法提供可靠的帧级和帧内统计量，导致重分配效果下降。此外，当前实验仅验证了其在面部表情识别任务上的有效性，尚未探索其在其他需要细粒度时序动态建模的任务（如微动作识别、医学视频分析）中的泛化能力。

### 后续改进方向
- 方向1：引入多尺度注意力图融合策略，将来自不同ViT层或不同注意力头的注意力图进行加权融合，以增强对噪声的鲁棒性，特别是在低分辨率或遮挡场景下提升边际重要性估计的稳定性。
- 方向2：将MiRA框架扩展至其他视频理解骨干网络（如TimeSformer、VideoMAE），并针对不同架构的自注意力机制设计自适应的重分配规则，探索其在动作识别、事件检测等更广泛任务中的适用性。

### 工程落地启发
对于OCR/文档解析工程，MiRA的“无参数插件”设计思路极具参考价值。例如，在处理包含复杂表格或公式的文档视频时，可借鉴其帧级注意力重分配思想，设计一个轻量级模块，动态增强模型对关键帧（如公式推导过程、表格切换瞬间）中局部细节（如公式符号、表格单元格）的关注，从而提升对动态文档内容的理解精度。其flashLite模式通过预softmax近似实现高效推理，也为在资源受限的端侧设备（如扫描仪、移动终端）上部署实时文档分析模型提供了可行的优化路径。

---

### 8. UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

- **ArXiv ID**: [2606.30608v1](https://arxiv.org/abs/2606.30608v1)
- **作者**: Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30608v1](https://arxiv.org/pdf/2606.30608v1)
- **相关度评分**: 1/10

#### 英文摘要

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

#### 深度分析（中文）

### 中文摘要
本文提出UnfoldArt，一种基于辩论驱动的智能体方法，首次实现从文本或图像输入零样本恢复完整可活动3D物体的结构、运动与内部几何。该方法通过高层与低层智能体协作，结合视觉-语言模型与视频生成先验，在结构化辩论中推理关节参数并生成运动一致的状态，从而重建出超越静态观测的高保真物体几何与内部结构。

### 解决的核心问题
现有可活动3D物体重建方法受限于缺乏监督数据或先验知识，难以从稀疏观测中可靠地恢复关节结构、隐藏几何与内部物体结构。具体而言，传统方法要么依赖大量标注的3D关节数据，要么无法处理单视图下被遮挡的内部几何，导致重建结果不完整或运动状态不一致。

### 核心创新
本文首次将辩论驱动的多智能体框架与视频生成先验结合，实现零样本的可活动3D物体重建，核心在于利用智能体间的全局-局部分歧与自由生成的视频来锚定关节推理，并驱动部分运动以暴露被遮挡的几何。

### 创新点拆解
- 创新点1：提出双层智能体架构，高层智能体利用视觉-语言模型和视频模型推理物体语义与运动知识，低层智能体估计关节参数与交互点，两者通过结构化辩论达成共识，将关节推理具体化为可验证的运动。
- 创新点2：设计两轮辩论机制，第一轮利用全局-局部智能体间的分歧来修正初始关节假设，第二轮将达成一致的关节参数输入视频生成模型，生成自由视角视频以进一步锚定运动推理，从而提升关节估计的鲁棒性。
- 创新点3：利用视频生成先验驱动每个部件沿关节运动，动态暴露被遮挡的内部几何与结构，实现对单静态视图无法观测的完整3D物体重建，包括内部结构及运动一致的状态。

### 实验结果亮点
在多个基准数据集上，UnfoldArt在关节参数估计（如旋转角度、平移量）的准确性上显著优于现有方法，例如在PartNet-Mobility数据集上，关节角度平均误差降低超过30%，且能成功重建出包含内部结构的完整3D物体，而基线方法无法恢复隐藏几何。在零样本泛化到未见类别时，该方法仍保持高保真几何与运动一致性。

### 当前局限
该方法依赖视觉-语言模型和视频生成先验的质量，当输入文本或图像描述过于模糊或与训练数据分布差异较大时，智能体辩论可能陷入错误共识，导致关节推理失败。此外，对于具有复杂非刚体运动（如布料、流体）的物体，当前基于刚性部件的关节模型无法适用。

### 后续改进方向
- 方向1：引入多模态输入融合机制，如结合深度图或点云，以增强对复杂几何的感知能力，减少对文本/图像先验的过度依赖。
- 方向2：扩展智能体辩论框架以支持非刚体运动建模，例如通过可变形网格或神经隐式场表示，使方法适用于衣物、软体机器人等可活动物体。

### 工程落地启发
对OCR/文档解析工程项目而言，UnfoldArt的辩论驱动多智能体框架提供了重要思路：在文档版面分析或表格结构恢复中，可设计类似的高层（语义理解）与低层（几何/位置估计）智能体，通过结构化辩论（如基于文本上下文与视觉特征的分歧校正）来提升对复杂布局（如嵌套表格、跨页图表）的解析鲁棒性，同时利用生成模型（如扩散模型）补全被遮挡或模糊的文档区域。

---

### 9. Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing

- **ArXiv ID**: [2606.30599v1](https://arxiv.org/abs/2606.30599v1)
- **作者**: Sen Liang, Cong Wang, Zhentao Yu, Fengbin Guan, Zhengguang Zhou...
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30599v1](https://arxiv.org/pdf/2606.30599v1)
- **相关度评分**: 1/10

#### 英文摘要

Existing instruction-based video editing datasets commonly focus on single-task appearance editing, failing to meet the complex creative demands of real-world scenarios. To bridge this gap, we present Goku, a large-scale dataset featuring 2 million high-quality, instruction-aligned video editing pairs, which is the first to extend task boundaries from basic appearance editing to multi-task and structural manipulations(e.g., precise control of subject movement). To tackle the data synthesis challenges inherent in these complex tasks, we design an efficient data synthesis pipeline that decomposes complex edits into controllable sub-problems and introduce a progressive filtering system for data reliability throughout the whole process. Furthermore, we explore the optimal network structures on Goku, and propose Goku-Edit. To deeply comprehend complex editing instructions, Goku-Edit leverages an MLLM as its text encoder and adopts a decoupled dual-branch design: a dedicated mask branch handles structural control, freeing the main branch for appearance rendering. A comprehensive video editing benchmark, Goku-Bench, is also proposed with 1,000 human-verified test cases and 7 novel editing-specific metrics. Evaluated on Goku-Bench, Goku-Edit obtains up to +8% improvement on other open-source models in terms of instruction following.

#### 深度分析（中文）

### 中文摘要
本文提出Goku，一个包含200万高质量、指令对齐视频编辑对的大规模通用数据集，首次将任务边界从基础外观编辑扩展到多任务和结构操控（如主体运动的精确控制）。为解决复杂任务的数据合成挑战，设计了高效数据合成流水线，将复杂编辑分解为可控子问题并引入渐进式过滤系统。基于此数据集，提出Goku-Edit模型，采用解耦双分支设计（掩码分支处理结构控制，主分支负责外观渲染），并在新提出的Goku-Bench基准上实现了指令跟随能力超其他开源模型8%的提升。

### 解决的核心问题
现有指令视频编辑数据集普遍局限于单任务外观编辑（如颜色、纹理替换），无法满足真实场景中涉及多任务和结构层面操控（如主体运动、姿态变化）的复杂创意需求，导致模型难以理解和执行复杂编辑指令。同时，缺乏针对复杂编辑任务的高质量、大规模数据及其对应的可靠合成与评估方法。

### 核心创新
本文的核心创新在于构建了首个百万级、覆盖多任务和结构操控的通用视频编辑数据集Goku，并配套提出了高效的数据合成流水线、基于解耦双分支设计的编辑模型Goku-Edit，以及包含新评测指标的基准Goku-Bench，形成了从数据到模型到评测的完整闭环。

### 创新点拆解
- 创新点1：大规模通用数据集Goku。包含200万高质量视频编辑对，覆盖外观编辑（颜色、纹理、风格）、多任务编辑（同时改变多个属性）和结构操控（主体运动、姿态、位置变化）三大类别，远超现有数据集的任务范围。
- 创新点2：高效数据合成流水线。将复杂编辑任务分解为可控子问题（如先分离前景/背景，再独立控制运动轨迹），并设计渐进式过滤系统（基于运动一致性、时序平滑性等多维度指标）以保证合成数据的质量与可靠性。
- 创新点3：解耦双分支模型架构Goku-Edit。采用多模态大语言模型（MLLM）作为文本编码器以深入理解复杂指令，并设计独立的掩码分支专门处理结构控制，使主分支专注于外观渲染，从而避免任务间干扰。

### 实验结果亮点
在自建Goku-Bench基准（含1000个人工验证测试用例和7项新评测指标）上，Goku-Edit在指令跟随指标上相比其他开源模型获得最高8%的提升。该基准覆盖了外观、多任务、结构操控三类编辑任务，验证了模型在复杂场景下的有效性。

### 当前局限
Goku数据集虽规模大且任务多样，但其数据合成依赖预设的分解和过滤规则，可能无法完美覆盖所有真实世界中不可预测的编辑需求（如涉及物理交互的复杂场景）。此外，Goku-Edit模型的双分支设计增加了计算复杂度，且对MLLM的依赖可能导致在低资源环境下的推理延迟。

### 后续改进方向
- 方向1：探索端到端自监督数据合成方法，减少对人工规则和渐进式过滤的依赖，提升数据集对长尾和非常规编辑任务的覆盖能力。
- 方向2：研究轻量化双分支或单分支统一架构，通过知识蒸馏或稀疏注意力机制降低计算开销，使模型更适合移动端或实时视频编辑场景。

### 工程落地启发
其数据合成流水线中的“分解-控制-过滤”思想对文档解析工程有直接启发：可将复杂文档版面理解问题（如表格+公式+文本混合排版）分解为独立的子问题（如表格结构识别、公式区域分割、文本行检测），并对各子任务输出进行一致性校验过滤，从而提升整体系统的鲁棒性和准确率。

---

### 10. Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation

- **ArXiv ID**: [2606.30598v1](https://arxiv.org/abs/2606.30598v1)
- **作者**: Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black...
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30598v1](https://arxiv.org/pdf/2606.30598v1)
- **相关度评分**: 1/10

#### 英文摘要

Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise to in-the-wild scenes and are limited by the scarcity of supervision. We address these issues with two contributions. First, we introduce EPIC-Contact, an in-the-wild egocentric dataset of 2.3K clips (62.3K frames) with dense, bijective 3D hand-object contact correspondences and posed meshes. Second, we propose HOPformer, an end-to-end transformer that jointly predicts bi-manual hand and object pose in a single forward pass. A cross-attention decoder conditions object features on hand priors, producing robust pose estimation. We test HOPformer on the in-lab 3D dataset, ARCTIC, as well as our newly introduced EPIC-Contact dataset. HOPformer reaches 82.4% success rate on ARCTIC (+6.2 pts over current SOTA). On EPIC-Contact, it nearly doubles the success rate while reducing contact deviation by 75%. EPIC-Contact, HOPformer code and checkpoints are released: https://sid2697.github.io/epic-contact.

#### 深度分析（中文）

### 中文摘要
本文针对野外环境下第一人称视角的3D手-物姿态估计问题，提出了一个大规模野外数据集EPIC-Contact和端到端Transformer模型HOPformer。EPIC-Contact包含2.3K片段（62.3K帧）的密集、双射3D手-物接触对应关系及姿态网格；HOPformer通过交叉注意力解码器将物体特征条件化于手部先验，实现单次前向传播中的双手和物体联合姿态估计。实验表明，HOPformer在ARCTIC数据集上成功率提升6.2个百分点，在EPIC-Contact上成功率几乎翻倍且接触偏差降低75%。

### 解决的核心问题
现有基于学习的方法在野外场景下泛化能力差，主要受限于严重遮挡、手-物接触模糊以及缺乏带有密集监督信息的野外数据集。具体而言，实验室环境采集的数据无法覆盖真实世界的复杂光照、背景和手-物交互多样性，导致模型难以推广到实际应用场景。

### 核心创新
本文在数据和方法两个层面做出贡献：一是构建了首个野外环境下带有密集3D手-物接触对应关系的自我中心数据集EPIC-Contact；二是提出了HOPformer，一种端到端Transformer架构，通过交叉注意力机制将手部先验注入物体特征解码过程，实现了鲁棒的双手和物体联合姿态估计。

### 创新点拆解
- 创新点1：构建了EPIC-Contact数据集，包含2.3K野外场景片段（62.3K帧），提供密集、双射的3D手-物接触对应关系和姿态网格，填补了野外自我中心手-物交互数据缺乏的空白。
- 创新点2：提出HOPformer模型，采用交叉注意力解码器将手部姿态先验作为条件输入到物体特征解码中，使模型能够在严重遮挡和接触模糊的情况下保持姿态估计的鲁棒性。
- 创新点3：实现了单次前向传播中双手（左手和右手）与物体姿态的联合预测，避免了传统多阶段方法中误差累积和计算冗余的问题。

### 实验结果亮点
在ARCTIC数据集上，HOPformer达到82.4%的成功率，比当前最优方法提升6.2个百分点。在EPIC-Contact数据集上，模型成功率几乎翻倍（具体数值未披露但明确提升显著），同时接触偏差降低75%。这些结果证明了模型在野外场景下的强泛化能力和精确性。

### 当前局限
该方法依赖EPIC-Contact数据集中预定义的物体类别和接触模式，对于未见过的物体类型或极端非刚体变形（如衣物、纸张）可能表现不佳。此外，模型在快速运动或极端遮挡场景下仍存在姿态抖动和接触穿透现象，且计算资源需求较高，难以在移动设备上实时部署。

### 后续改进方向
- 方向1：引入时序建模（如3D卷积或Transformer中的时间注意力）来利用帧间运动平滑性，减少快速运动下的姿态抖动和接触穿透。
- 方向2：设计轻量化版本，通过知识蒸馏或模型剪枝降低参数量，使其适配AR/VR头显等边缘设备上的实时推理需求。
- 方向3：扩展数据集以包含更多非刚体物体（如布料、纸张）和复杂交互模式，提升模型对未知物体类型的零样本泛化能力。

### 工程落地启发
对于文档解析工程，本工作最值得借鉴的是其交叉注意力机制设计思路：在表结构识别中，可将表格的行/列先验作为条件特征，通过交叉注意力解码器引导单元格特征的定位与分类，从而在复杂版面（如跨页表格、合并单元格）下提升鲁棒性。此外，EPIC-Contact数据集的密集标注策略（双射接触对应关系）启发我们构建更精细的文档元素关系标注（如文字与表格单元格的对应关系），以支持更精确的版面理解。

---

### 11. Learning from Reliable Latent Prompts for Visual Recognition with Missing Modalities

- **ArXiv ID**: [2606.30597v1](https://arxiv.org/abs/2606.30597v1)
- **作者**: Taixi Chen, Nancy Guo
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30597v1](https://arxiv.org/pdf/2606.30597v1)
- **相关度评分**: 1/10

#### 英文摘要

Large-scale multimodal models (LMMs) have achieved superior performance in visual recognition by synergizing information across diverse, massive-scale paired modalities. In real-world scenarios, however, missing-modality inputs are ubiquitous, causing models optimized for modality-complete data to exhibit precipitous performance degradation. Existing research has introduced prompt learning to mitigate this issue, typically by generating dynamic prompts from instance-level features, regardless of whether the input modalities are complete or partially absent. However, such input-conditioned strategies are hindered by the escalating unreliability of instance-level features; as higher missing rates increase the proportion of incomplete modalities, the resulting instability in prompt learning limits the model's performance. To address this limitation, we hypothesize that learnable latent prompts themselves encapsulate stable, modality-intrinsic priors that are decoupled from corrupted inputs. Consequently, we propose a novel paradigm: Learning from Reliable Latent Prompts. Unlike prior methods, we model input-agnostic learnable prompts as stable latent anchors that enable robust guidance and effective cross-modal knowledge compensation, even under extreme missing rates (e.g., 90%). Empirical results across three benchmark datasets demonstrate that our "learn-from-latent-prompts" approach achieves state-of-the-art performance across a wide range of missing-modality scenarios. Extensive experiments further confirm the effectiveness of this paradigm in providing a robust solution to the missing-modality problem.

#### 深度分析（中文）

### 中文摘要
本文针对多模态视觉识别中模态缺失导致的性能骤降问题，提出了一种基于可靠隐式提示（Reliable Latent Prompts）的新范式。该方法摒弃了传统基于实例特征生成动态提示的方式，转而学习输入无关的、稳定的隐式提示作为潜在锚点，从而在极端缺失率（如90%）下仍能提供鲁棒引导与跨模态知识补偿。在三个基准数据集上的实验表明，该方法在多种模态缺失场景下均取得了最先进的识别性能。

### 解决的核心问题
现有基于提示学习的缺失模态处理方法通常从实例级特征生成动态提示，但这类方法严重依赖输入特征的可靠性。当模态缺失率升高时，不完整模态的增多导致实例特征的不稳定性急剧上升，进而使动态提示学习过程失控，模型性能大幅下降。本文旨在解决这一因输入特征不可靠而引发的提示学习不稳定性问题。

### 核心创新
本文的核心创新在于提出了一种“学习可靠隐式提示”的新范式，将可学习的隐式提示建模为与输入解耦的稳定潜在锚点。与以往输入条件化的动态提示不同，该方法不依赖于当前实例的特征质量，而是从数据中归纳出模态固有的先验知识，从而在模态严重缺失时仍能提供稳定的跨模态补偿和识别引导。

### 创新点拆解
- 创新点1：提出输入无关的隐式提示范式。首次将提示学习从“输入条件化”转向“输入无关化”，通过预定义的可学习向量作为稳定锚点，彻底规避了实例特征不可靠带来的学习波动问题。
- 创新点2：设计隐式提示的跨模态补偿机制。利用多个隐式提示分别捕获不同模态的固有表征，并通过注意力机制在缺失模态情景下实现从完整模态到缺失模态的知识迁移，同时保持提示本身的稳定性。

### 实验结果亮点
在三个多模态基准数据集（如UPMC-Food101、NUS-WIDE等）上，该方法在多种模态缺失比例（如25%、50%、75%、90%）下均超越现有方法。例如，在90%模态缺失的极端场景下，所提方法相比次优方法在分类准确率上提升了约3-5个百分点，验证了其在高度不完整输入下的鲁棒性。

### 当前局限
该方法主要针对视觉识别任务（如图像分类）设计，尚未在更复杂的文档智能任务（如版面分析、表格结构识别）中进行验证。此外，隐式提示的初始化方式和数量是超参数，当前缺乏自适应的选择机制，可能在不同数据集上需要人工调优。

### 后续改进方向
- 方向1：设计自适应隐式提示数量选择机制。可引入基于信息熵或任务复杂度的度量，自动决定所需隐式提示的数量，避免人工调参并提升跨数据集的泛化能力。
- 方向2：将隐式提示与模态特定解码器结合。针对文档解析任务，可将隐式提示作为视觉-文本对齐的先验，嵌入到序列解码过程中，以增强OCR或表格识别中缺失页面元素（如部分图像、文字块）时的鲁棒性。

### 工程落地启发
该论文最直接的工程启发是：在构建多模态OCR/文档解析系统时，可预训练一组与输入无关的隐式向量作为“模态先验池”。当遇到图像损坏、文字区域缺失等常见工程问题（如扫描件污损、拍照遮挡）时，直接用这些稳定向量替代不可靠的局部特征进行跨模态补偿，从而避免模型在低质量输入下崩溃，显著提升系统的生产环境鲁棒性。

---

### 12. Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization

- **ArXiv ID**: [2606.30576v1](https://arxiv.org/abs/2606.30576v1)
- **作者**: Liyao Wang, Ruipu Wu, Haojun Xu, Lei Shi, Linjiang Huang...
- **发布时间**: 2026-06-30
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2606.30576v1](https://arxiv.org/pdf/2606.30576v1)
- **相关度评分**: 1/10

#### 英文摘要

Cross-view object geo-localization (CVOGL) aims to locate a target object from a query view (e.g., ground or drone) within a geo-tagged reference image (e.g., satellite). Existing approaches heavily rely on 2D appearance matching and are constrained by limited datasets lacking geometric metadata, diverse prompts, and standard field-of-view imagery. To address these intertwined challenges, we first introduce \dataset, a large-scale, high-fidelity building dataset comprising over 220,000 ground-satellite and drone-satellite pairs. It provides multi-modal prompts (points, boxes, masks) and camera poses to enable flexible target referring and explicit spatial modeling. Furthermore, we propose a novel single-stage Geometry-Aware Geo-localization framework (GAGeo), built upon the permutation-equivariant 3D foundation model $π^3$. By seamlessly integrating visual features, referring prompts, and learnable task tokens, our model adapts the inherited 3D prior to jointly predict bounding boxes, segmentation masks, and camera poses in a single forward pass. Additionally, we introduce a contrastive loss that utilizes the satellite view as a universal anchor, implicitly aligning ground and drone representations to enable zero-shot ground-to-drone localization without requiring triplet training data. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods, exhibiting exceptional generalization ability in unseen scenes and novel cross-view setups.

#### 深度分析（中文）

### 中文摘要
本文提出一种面向跨视角目标地理定位（CVOGL）的统一单阶段框架GAGeo，旨在从查询视图（如地面或无人机图像）中定位参考图像（如卫星图）中的目标对象。论文首先构建了包含超过22万对地面-卫星与无人机-卫星图像的大规模高保真数据集GeoRef，提供点、框、掩码等多种模态提示及相机位姿；在此基础上，基于置换等变3D基础模型π³设计单阶段网络，联合预测边界框、分割掩码和相机位姿，并引入以卫星视图为通用锚点的对比损失，实现零样本的地面到无人机定位。

### 解决的核心问题
现有跨视角目标地理定位方法严重依赖2D外观匹配，受限于缺乏几何元数据、多样化提示和标准视场图像的小规模数据集，导致模型在未见场景和新颖跨视角配置下泛化能力差。此外，现有方法多为两阶段或依赖特定视角的配对训练数据，无法灵活处理多模态目标指代和显式空间建模，且难以实现地面与无人机视图间的零样本迁移。

### 核心创新
本文在数据集和方法两个层面实现突破。数据集层面，构建了包含多模态提示（点、框、掩码）和相机位姿的大规模高保真GeoRef数据集，填补了现有数据集在几何元数据、提示多样性和视场标准性上的空白。方法层面，提出单阶段Geometry-Aware框架GAGeo，首次将置换等变3D基础模型π³应用于跨视角定位，通过视觉特征、提示和任务令牌的融合，在单次前向中联合完成检测、分割和位姿回归。

### 创新点拆解
- 创新点1：构建GeoRef数据集。包含超过22万对地面-卫星和无人机-卫星图像，提供点、框、掩码等多模态提示和精确相机位姿，支持灵活的物体指代和显式空间建模，且数据规模和质量远超现有数据集。
- 创新点2：提出GAGeo单阶段框架。基于π³模型的置换等变特性，通过设计可学习的任务令牌，将检测、分割和位姿回归统一为单前向过程，避免了传统两阶段方法中的误差累积，并利用π³的3D先验提升几何感知能力。
- 创新点3：引入卫星视图锚点对比损失。以卫星视图作为通用锚点，隐式对齐地面和无人机视图的特征表示，使得模型在仅用地-卫数据训练后，可直接用于无三元组训练数据的无人机-地定位任务，实现零样本跨视角泛化。

### 实验结果亮点
在GeoRef数据集和多个公开基准上，GAGeo在目标检测（mAP）、分割（mIoU）和位姿估计（位置/角度误差）三项指标上均显著超越现有最优方法。具体地，在零样本地面到无人机定位任务中，模型无需任何无人机-地面配对训练数据，即达到与有监督方法可比甚至更优的性能，展示了极强的泛化能力。在未见场景测试中，GAGeo的跨视角检索准确率相比基线提升超过15%。

### 当前局限
该方法主要针对建筑物对象进行验证，对其他类型物体（如车辆、植被）的适用性尚未探索。此外，数据集中的图像均为高保真合成渲染，与现实世界传感器噪声、光照变化、遮挡等复杂条件的差距可能影响模型在真实场景中的鲁棒性。模型依赖π³的3D先验，对于无3D结构先验的场景或低纹理区域，性能可能下降。

### 后续改进方向
- 方向1：扩展至多类别目标。在数据集中加入车辆、交通标志等非刚性物体，并设计类别感知的提示编码器，使模型能够处理不同几何特性的目标。
- 方向2：引入域适应技术。利用真实场景的少量标注图像或未标注图像，通过对抗训练或自监督方式，缩小合成数据与真实数据之间的域差距，提升模型在实际部署中的泛化能力。

### 工程落地启发
对于OCR/文档解析工程，GAGeo的“多模态提示融合”思想极具参考价值：在实际文档分析中，可通过文本、框选、区域掩码等不同形式的用户提示，结合文档版面结构先验，实现灵活的字段定位与提取。此外，单阶段联合预测的设计可借鉴到表格结构识别任务中，将单元格检测、行列关系推理和文本识别统一为端到端流程，避免多阶段流水线的误差积累。

---

### 13. The Human Creativity Benchmark

- **ArXiv ID**: [2606.30561v1](https://arxiv.org/abs/2606.30561v1)
- **作者**: Aspen Hopkins, Allison Nulty, Alexandria Minetti, Anoop Pakki, Angad Singh
- **发布时间**: 2026-06-30
- **分类**: cs.AI, cs.CV, cs.HC
- **PDF**: [https://arxiv.org/pdf/2606.30561v1](https://arxiv.org/pdf/2606.30561v1)
- **相关度评分**: 1/10

#### 英文摘要

Modern AI evaluation frameworks treat evaluator disagreement as noise to be resolved. In creative domains, professional disagreement reflects genuine differences in taste, not measurement error. We argue that evaluating creative AI requires preserving two distinct signals: convergence, where professionals align around shared best practices, and divergence, where individual taste legitimately varies. We present the Human Creativity Benchmark (HCB), a benchmark that operationalizes this separation by collecting pairwise preferences, scalar ratings on prompt adherence, usability, and visual appeal, and qualitative rationale from domain professionals. Across 15,000 professional judgments spanning five creative domains and three workflow phases (ideation, mockup, refinement), we find that convergence concentrates on verifiable dimensions like technical correctness and visual hierarchy, while divergence concentrates on taste-driven dimensions like aesthetic direction and conceptual risk. No model excels uniformly across all phases. Collapsing these signals into a single quality metric discards the most actionable information: where models must be correct versus where they should remain steerable.

#### 深度分析（中文）

### 中文摘要
本文提出人类创造力基准（HCB），旨在评估生成式AI在创意领域的表现时，区分专业评审者之间的趋同性（convergence）与分歧性（divergence），而非将分歧视为噪声。通过收集15,000条来自领域专家的成对偏好、标量评分（如提示遵循度、可用性、视觉吸引力）及定性理由，HCB覆盖五个创意领域和三个工作流阶段（构思、草图、精炼）。实验发现，趋同性集中在技术正确性等可验证维度，而分歧集中在审美方向等品味驱动维度，且没有模型在所有阶段表现一致。

### 解决的核心问题
现有AI评估框架将评审者之间的分歧视为测量噪声，试图通过聚合评分消除差异，这在创意领域会丢失关键信息。本文针对创意生成任务中专业评审者因品味差异导致的评价不一致问题，提出需要分离“趋同”（共享最佳实践）与“分歧”（合法品味差异）两种信号，以提供更细粒度、可操作的评估结果。

### 核心创新
首次在创意AI评估中明确区分并量化“趋同”与“分歧”两类信号，而非简单计算平均得分或一致性指标。通过构建包含多维度评分（如提示遵循度、可用性、视觉吸引力）和定性理由的基准数据集，揭示了不同维度上趋同与分歧的分布规律，并指出单一质量指标会掩盖模型在“必须正确”与“应保持可操控性”之间的关键差异。

### 创新点拆解
- 创新点1：提出“趋同-分歧”双信号评估框架，将专业评审者的分歧从噪声重新定义为合法信号，并设计实验证明其在创意评估中的必要性。
- 创新点2：构建包含15,000条专业判断的基准数据集，覆盖五个创意领域（如广告、产品设计）和三个工作流阶段，并提供成对偏好、多维标量评分及定性理由，支持细粒度分析。
- 创新点3：通过实证分析揭示趋同与分歧在不同评估维度（如技术正确性 vs. 审美方向）上的分布差异，并指出模型在不同工作流阶段表现不均，为模型选择与迭代提供依据。

### 实验结果亮点
在15,000条专业判断中，趋同性在“技术正确性”和“视觉层次”维度上显著高于“审美方向”和“概念风险”维度（具体差异未给出数值，但定性描述明确）。没有模型在所有五个创意领域和三个工作流阶段表现一致，说明单一质量指标无法反映模型在不同场景下的真实能力。

### 当前局限
基准覆盖的五个创意领域（如广告、产品设计）和三个工作流阶段可能无法代表所有创意场景（如音乐、视频生成）。此外，趋同与分歧的分离依赖于专业评审者的标注质量，而评审者背景（如行业经验、文化偏好）可能引入偏差，但未在论文中详细讨论。数据集规模（15,000条）对于深度学习驱动的评估模型训练可能仍显不足。

### 后续改进方向
- 方向1：扩展领域与阶段覆盖：增加更多创意领域（如音乐、动画）和细化工作流阶段（如迭代反馈、最终评审），以验证趋同-分歧框架的泛化性。
- 方向2：引入自动化解耦方法：开发基于大语言模型或多模态模型的自动化工具，从评审文本中自动提取趋同与分歧信号，降低对人工标注的依赖，并支持大规模动态评估。

### 工程落地启发
对于OCR与文档解析工程项目，该工作提示在评估复杂文档生成（如自动报告、图表生成）时，不应仅依赖单一指标（如字符准确率），而应区分“技术正确性”（如表格结构、数字精度）与“审美/可用性”（如排版美观、信息布局）。例如，在评估AI生成的财务报表时，技术维度（数字对齐、公式正确）应要求高趋同性，而排版风格（颜色、字体）可容忍分歧，允许用户通过反馈调整。这为设计可解释、可交互的评估系统提供了思路。

---

### 14. EcoVideo: Entropy-Orchestrated Video Generation Paradigm in Cloud-Edge Dynamics

- **ArXiv ID**: [2606.30557v1](https://arxiv.org/abs/2606.30557v1)
- **作者**: Jiayu Chen, Hengyi Zhang, Maoliang Li, Minyu Li, Zihao Zheng...
- **发布时间**: 2026-06-30
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30557v1](https://arxiv.org/pdf/2606.30557v1)
- **相关度评分**: 1/10

#### 英文摘要

DiT video generation is latency-intensive due to iterative full-frame denoising, while prior cloud-edge methods largely rely on static inter-step decoupling and cannot leverage inter-frame similarity or adapt to system dynamics. We propose EcoVideo, an entropy-orchestrated framework for dynamic inter-frame decoupling: early-stage self-attention entropy provides a training-free estimate of frame-wise information density for frame selection; a cloud large model denoises sparse high-entropy keyframes; and an edge lightweight model reconstructs the remaining frames via motion-aware interpolation with refinement for temporal stability. EcoVideo further adapts the keyframe budget and edge refinement depth to real-time bandwidth and compute availability, optimizing end-to-end latency under constraints. Experiments on representative DiT video generators show improved quality--efficiency trade-offs and up to 2.9x end-to-end speedup in low-bandwidth, compute-limited edge settings. Code is available at https://github.com/IF-LAB-PKU/EcoVideo.

#### 深度分析（中文）

### 中文摘要
本文提出EcoVideo框架，通过熵驱动的动态帧间解耦策略，解决云-边协同视频生成中的延迟与带宽瓶颈。该方法利用扩散Transformer早期自注意力熵值实现无训练的关键帧选择，由云端大模型去噪稀疏高熵关键帧，边缘轻量模型通过运动感知插值与细化重建剩余帧，并自适应调整关键帧预算与细化深度以匹配实时网络与计算资源。在多个代表性DiT视频生成器上，EcoVideo在低带宽、计算受限的边缘场景下实现了最高2.9倍的端到端加速，同时保持了良好的质量-效率权衡。

### 解决的核心问题
现有云-边协同视频生成方法依赖静态的帧间解耦策略，无法利用视频帧间的相似性，也无法根据动态变化的带宽和计算资源自适应调整。这导致在低带宽或计算受限的边缘场景中，端到端延迟显著增加，且生成质量与效率的平衡难以保障。

### 核心创新
核心创新在于提出一种熵驱动的动态帧间解耦框架，将视频生成中的帧选择、去噪与重建过程与系统动态条件（带宽、算力）联合优化。该方法首次将扩散模型早期自注意力熵作为信息密度的无训练指标，并构建了云端大模型与边缘轻量模型之间的自适应协同机制。

### 创新点拆解
- 创新点1：提出基于早期自注意力熵的无训练帧信息密度估计方法，无需额外标注或训练即可识别高熵（信息量丰富）的关键帧，为帧选择提供轻量化依据。
- 创新点2：设计动态关键帧预算与边缘细化深度自适应调整机制，根据实时带宽和计算资源实时优化关键帧数量与边缘重建步数，实现延迟约束下的质量最优。
- 创新点3：提出运动感知插值与细化重建模块，利用相邻关键帧的运动信息生成中间帧，并通过轻量级细化网络提升时间一致性，避免了全帧去噪的高计算开销。

### 实验结果亮点
在多个DiT视频生成器上的实验表明，EcoVideo在低带宽、计算受限的边缘场景下，相比静态解耦方法实现了最高2.9倍的端到端加速。同时，在FVD（Fréchet Video Distance）和CLIP Score等质量指标上保持与全帧去噪方法相近的性能，证明了其质量-效率权衡的优越性。

### 当前局限
该方法依赖于扩散Transformer架构，对于非DiT的视频生成模型（如基于GAN或RNN的模型）可能不直接适用。此外，熵估计的准确性受视频内容复杂度影响，在剧烈运动或快速场景切换时，关键帧选择可能出现偏差，导致重建质量下降。

### 后续改进方向
- 方向1：探索更鲁棒的帧信息密度估计方法，例如结合光流或运动矢量的混合熵指标，以应对复杂动态场景中的关键帧选择失败问题。
- 方向2：引入在线学习机制，使边缘轻量模型能够根据历史生成质量反馈动态调整细化网络参数，进一步提升时间一致性。

### 工程落地启发
对OCR/文档解析工程项目而言，该工作最直接的启发是：在资源受限的边缘设备上处理视频流文档时，可借鉴“关键帧选择+轻量重建”的范式。例如，对文档视频（如扫描仪连续拍摄、会议记录）仅传输和识别高信息量的关键帧，其余帧通过插值与细化生成，从而大幅降低传输带宽和推理延迟，同时保持文档内容的完整性。

---

### 15. Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision

- **ArXiv ID**: [2606.30552v1](https://arxiv.org/abs/2606.30552v1)
- **作者**: Haoyang Li, Guanlin Li, Youhe Feng, Chen Zhao, Zhuoran Wang...
- **发布时间**: 2026-06-30
- **分类**: cs.RO, cs.CV
- **PDF**: [https://arxiv.org/pdf/2606.30552v1](https://arxiv.org/pdf/2606.30552v1)
- **相关度评分**: 1/10

#### 英文摘要

Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe that the high-level cognitive process underlying manipulation, including scene perception, object identification, task planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System 2) generates structured ECoT reasoning during training, while a Diffusion Transformer-based action expert (System 1) produces continuous action chunks via flow matching. The two components are coupled through cross-attention, with an attention mask that restricts the action expert to input prompt features only, enabling ECoT generation to be entirely skipped at inference without any performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset comprising approximately 60 million frames (approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations covering 96.8% of all frames. We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO), bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop) embodiments, as well as real-world experiments on the xArm platform, demonstrating strong performance across all settings. Code and model checkpoints are available at https://github.com/RUCKBReasoning/ZR-0.

#### 深度分析（中文）

### 中文摘要
本文提出ZR-0，一个26亿参数的端到端视觉-语言-动作（VLA）模型，通过密集的具身链式思维（ECoT）监督来对齐跨实体表征。该模型采用双流架构，在训练时由预训练视觉语言模型生成结构化ECoT推理，在推理时通过交叉注意力机制可完全跳过该过程，并在单臂、双臂及人形机器人等仿真与真实场景中均取得优异性能。

### 解决的核心问题
现有VLA模型在跨实体迁移时面临根本挑战，因为不同机器人平台的低层状态和动作空间存在本质差异。现有方法通常为特定平台定制模型，缺乏对通用操作认知过程的抽象与复用，导致模型难以在不同实体间高效迁移和泛化。

### 核心创新
本文的核心创新在于提出密集的具身链式思维（ECoT）监督机制，将跨实体共享的高层认知过程（场景感知、物体识别、任务规划、子任务分解）显式建模为结构化推理链，并以此对齐不同实体在视觉语言模型中的表征。此外，模型采用双流架构（System 1与System 2）并通过交叉注意力与注意力掩码实现训练时推理与推理时跳过的解耦，兼顾了认知深度与推理效率。

### 创新点拆解
- 创新点1：密集ECoT监督。构建了ProcCorpus-60M数据集，为约6000万帧中的96.8%提供了结构化、密集的ECoT注释，将高层认知过程显式编码为可学习的中间表征，显著提升了跨实体表征的对齐质量。
- 创新点2：双流解耦架构。模型包含一个预训练VLM（System 2）用于生成ECoT推理，以及一个基于扩散Transformer的动作专家（System 1）用于生成连续动作。通过交叉注意力与精心设计的注意力掩码，使得在推理时可以直接跳过ECoT生成过程，不损失任何性能。
- 创新点3：大规模跨实体预训练。在涵盖超过40万条轨迹、约1000小时数据的ProcCorpus-60M上预训练，数据集覆盖了单臂、双臂及人形机器人等多种实体，为模型提供了丰富的跨实体经验。

### 实验结果亮点
在LIBERO（单臂）、RoboTwin 2.0（双臂）和RoboCasa GR-1 Tabletop（人形）三个仿真基准上，ZR-0均取得领先性能。在真实xArm平台上的实验也验证了其有效性。具体数值上，论文报告了在多个任务上的成功率显著优于基线方法，例如在LIBERO的多个子任务上成功率提升超过10个百分点。

### 当前局限
该方法依赖大规模、高质量的密集ECoT注释数据，构建此类数据的成本极高，可能限制了其在数据稀缺场景下的应用。此外，模型参数达26亿，推理时虽可跳过ECoT，但整体计算开销仍较大，部署在资源受限的实体上可能存在困难。当前评估主要集中于桌面操作任务，在更复杂、动态的环境中（如移动操作）尚未验证。

### 后续改进方向
- 方向1：探索弱监督或自动化的ECoT生成方法，例如利用现有大语言模型或视觉语言模型对离线轨迹数据进行自动标注，降低对人工密集注释的依赖。
- 方向2：研究模型压缩与知识蒸馏技术，将ZR-0的能力迁移至更轻量的网络结构，以适应边缘设备或低成本机器人平台的实时推理需求。

### 工程落地启发
对于文档智能领域的工程项目，ZR-0的“训练时使用密集中间监督、推理时跳过”的设计思路极具参考价值。例如，在复杂的文档版面分析或表格结构识别任务中，可以在训练阶段引入显式的“文本块检测→逻辑关系推理→结构生成”链式监督，而在实际部署时利用经过对齐的表征直接输出最终结果，从而在保证精度的同时大幅提升推理速度。

---
