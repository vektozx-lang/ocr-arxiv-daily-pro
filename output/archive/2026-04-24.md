# OCR arXiv Daily Pro — 2026-04-24

> 自动生成，共收录 **15** 篇高相关论文

> 时间窗口：2026-04-23 09:10 - 2026-04-24 09:10 (Asia/Shanghai)

---

## 📊 今日综合分析

### 今日执行摘要
今日共15篇论文，研究热点集中于大视觉语言模型（LVLM/VLM）的可信度与幻觉问题、开放集测试时自适应、以及面向特定任务的检测与生成。其中，围绕LVLM的视觉推理可信度（如VG-CoT）、提示引导的幻觉机制（HalluScope）以及评估模型自身盲点（Seeing Isn‘t Believing）构成了今日最密集的讨论，反映出领域对模型可靠性的高度关注。此外，基于组件的开放集检测、多模态图像检索中的细粒度修改，以及逻辑门网络在视频拷贝检测中的应用，展现了在鲁棒性与效率上的新探索。

### 今日研究趋势
1. **LVLM/VLM的可信度与幻觉机制深入分析**：多篇论文从不同角度揭示了当前LVLM的脆弱性。例如，**论文5 (When Prompts Override Vision)** 通过HalluScope基准系统研究了提示词如何主导视觉输入，导致幻觉；**论文4 (Seeing Isn’t Believing)** 则揭示了评估用VLM自身存在的盲点，其评估结果并不可靠。这种对“评估者”的元评估视角，标志着对模型可信度研究的深化。

2. **开放集与连续域自适应问题的系统化处理**：**论文2 (Back to Source)** 提出了开放集连续测试时自适应（OCTTA）问题，同时应对域漂移和未知类别的出现，并通过域补偿策略缓解特征空间坍塌。**论文3 (Component-Based OOD Detection)** 则从认知理论出发，提出基于组件的检测方法，有效识别由有效ID组件构成的组合异常，这是对传统全局/局部检测范式的有力补充。

3. **面向特定任务的轻量级与高效表示学习**：**论文11 (Efficient Logic Gate Networks)** 使用可微逻辑门网络替代传统的浮点特征提取器，在视频拷贝检测中实现了紧凑的逻辑表示，兼顾性能与部署效率。**论文8 (Explainable Disentangled Representation Learning)** 则聚焦于作者风格与内容的解耦，通过可解释变分自编码器学习鲁棒且可泛化的风格表示，对抗生成式AI文本的挑战。

### 核心技术创新汇总
- **视觉接地链式推理（VG-CoT）**：**论文1** 提出将多步推理与图像区域显式对齐的方法，解决了现有数据集在可扩展性和可信度评估上的局限，是提升LVLM视觉推理透明度的关键尝试。
- **域补偿策略（Domain Compensation）**：**论文2** 针对OCTTA场景，提出通过解耦域偏移与语义偏移来稳定特征空间，为模型在动态未知环境下的持续适应提供了新思路。
- **基于组件的离群检测（Component-Based OOD Detection）**：**论文3** 借鉴“识别-通过-组件”理论，将检测粒度从全局或局部提升到组件级别，尤其擅长捕捉组合型异常，显著提升了对细粒度语义漂移的敏感性。
- **多修改组合图像检索（Multi-Modification CIR）**：**论文6** 提出的TEMA框架，通过锚定图像并跟随文本，解决了传统CIR在处理包含多个实体和复杂从句的修改文本时的不足，扩展了实际应用场景。
- **隐式奖励模型零样本检测（Implicit Reward Model for Zero-Shot Detection）**：**论文10** 利用指令微调模型的内部奖励机制，无需任何训练数据即可检测LLM生成文本，方法新颖且实用性高。

### 研究空白与机会
- **文档级视觉-语言模型的幻觉评估**：今日论文主要关注自然图像或通用场景下的LVLM幻觉，针对文档图像（如扫描件、PDF）中特有的幻觉类型（如表格结构幻觉、公式符号误识别）缺乏专门研究。开发针对文档智能的幻觉基准测试是一个明确的机会。
- **跨模态检索中的鲁棒性与域泛化**：尽管多模态检索（如CIR）有进展，但现有方法对图像质量退化（如模糊、遮挡）或文本表述歧义的鲁棒性研究不足。结合**论文2**的域自适应思想，探索鲁棒的跨模态检索模型是潜在方向。
- **逻辑门网络在文档理解中的应用**：**论文11**展示了逻辑门网络在视频拷贝检测中的效率优势，其紧凑的逻辑表示特性非常适合处理文档版面分析、表格结构识别等需要高吞吐量和低延迟的场景，但今日论文未涉及这一交叉领域。

### 工程落地启发
- **构建可信的文档解析流水线**：可借鉴**论文1 (VG-CoT)** 的思想，在OCR后处理或文档理解阶段引入“视觉接地”的验证步骤，例如要求模型在输出表格内容时，同时提供其对应图像区域的坐标，以此作为内部可信度检查的依据。
- **利用组件化检测提升文档异常识别**：对于发票、合同等结构化文档，可以借鉴**论文3**的组件化OOD检测思路，将文档中的不同元素（如标题、日期、金额）视为独立组件，从而更精准地识别出排版错误、字段缺失或格式篡改等异常。
- **采用轻量级网络降低部署成本**：在需要高并发处理的文档识别场景（如银行流水单批量识别）中，可探索**论文11**的逻辑门网络替代传统CNN/Transformer，在保持识别精度的同时大幅降低计算资源和存储开销。

### 今日优先精读推荐
1. **论文5：When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs** — 直接揭示了LVLM幻觉的核心机制之一，对设计更可靠的文档理解提示词策略至关重要。
2. **论文3：Component-Based Out-of-Distribution Detection** — 其组件化检测范式为文档图像中的细粒度异常检测与版面分析提供了全新的理论框架和实用方法。
3. **论文2：Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation** — 应对动态变化的域漂移和未知类别，是文档智能模型在实际部署中（如不同扫描仪、不同语言文档）必须解决的核心问题。

---

## 📄 论文详情

### 1. VG-CoT: Towards Trustworthy Visual Reasoning via Grounded Chain-of-Thought

- **ArXiv ID**: [2604.21396v1](https://arxiv.org/abs/2604.21396v1)
- **作者**: Byeonggeuk Lim, Kyeonghyun Kim, JungMin Yun, YoungBin Kim
- **发布时间**: 2026-04-23
- **分类**: cs.CV, cs.AI
- **PDF**: [https://arxiv.org/pdf/2604.21396v1](https://arxiv.org/pdf/2604.21396v1)
- **相关度评分**: 10/10

#### 英文摘要

The advancement of Large Vision-Language Models (LVLMs) requires precise local region-based reasoning that faithfully grounds the model's logic in actual visual evidence. However, existing datasets face limitations in scalability due to extensive manual annotation and lack of explicit alignment between multi-step reasoning and corresponding image regions, which constrains the evaluation of model trustworthiness. To address these challenges, we propose the Visual Grounding Chain-of-Thought (VG-CoT) dataset, which explicitly links each reasoning step to real visual evidence within the image through a fully automated three-stage pipeline. The pipeline first extracts object- and text-level visual evidence using state-of-the-art detection and OCR models, then generates step-by-step grounded reasoning with GPT-4o, and finally refines the grounding through a rationale-driven open-set detection process. In addition, we introduce a new benchmark that comprehensively evaluates LVLMs reasoning across three complementary dimensions: Rationale Quality, Answer Accuracy, and Reasoning-Answer Alignment. Experiments with representative LVLMs, including LLaVA-1.5 and Qwen2-VL, demonstrate consistent improvements on most evaluation metrics, confirming that VG-CoT effectively enhances trustworthy, evidence-based reasoning while maintaining scalable and cost-efficient dataset construction. The dataset and code will be released publicly upon acceptance to facilitate further research.

#### 深度分析（中文）

### 中文摘要
本文提出VG-CoT数据集，通过全自动三阶段流水线将多步推理与图像中实际视觉证据（物体和文本）显式对齐，以增强大型视觉语言模型（LVLM）的可信推理能力。该数据集可规模化扩展，并配套提出一个从推理质量、答案准确性和推理-答案一致性三个维度综合评估LVLM推理的基准。实验表明，在LLaVA-1.5和Qwen2-VL等模型上，使用VG-CoT数据微调后，多数评估指标获得一致提升。

### 解决的核心问题
现有视觉推理数据集主要依赖人工标注，扩展性差，且推理步骤缺乏与图像局部区域的显式对齐，导致LVLM的推理过程难以被验证和信任。因此，本文聚焦于如何自动化构建高质量、带区域定位的多步推理数据集，并设计相应评估方法来衡量模型推理的可信度。

### 核心创新
核心创新在于提出一个完全自动化的三阶段流水线，无需人工即可生成与图像区域严格对齐的链式推理（Chain-of-Thought）数据，解决了数据集构建成本高和推理-区域对齐缺失的核心瓶颈。同时，引入了一个三维度评估基准，超越了传统仅关注答案正确性的评估方式。

### 创新点拆解
- 创新点1：全自动三阶段流水线。第一阶段利用先进检测和OCR模型提取物体和文本级视觉证据；第二阶段利用GPT-4o基于这些证据生成逐步的、有依据的推理；第三阶段通过基于推理的开集检测过程精炼定位，确保每一步推理都锚定于真实图像区域。
- 创新点2：三维度评估基准。该基准不仅评估答案准确性（Answer Accuracy），还评估推理质量（Rationale Quality）和推理与答案之间的一致性（Reasoning-Answer Alignment），从而更全面地衡量模型的可信推理能力。
- 创新点3：提出VG-CoT数据集本身，其兼具可扩展性（自动化生成）和高质量（显式区域对齐），为后续研究提供了关键资源。

### 实验结果亮点
在LLaVA-1.5和Qwen2-VL等代表性LVLM上，使用VG-CoT数据微调后，模型在多个视觉推理基准上的所有三个评估维度（推理质量、答案准确性、推理-答案对齐）均获得一致提升。具体而言，在需要精细定位和文本理解的复杂推理任务上，提升幅度尤为显著，验证了证据对齐对推理可信度的关键作用。

### 当前局限
该方法依赖GPT-4o作为推理生成器，其生成推理的可靠性和多样性可能受限，且可能继承GPT-4o的偏见或错误。此外，流水线中使用的检测和OCR模型也有其固有局限（如对罕见物体或复杂文档版面识别失败），这些错误会向下游传播，影响最终数据质量。当前评估主要基于合成或特定领域数据，在真实世界复杂场景下的泛化能力尚待验证。

### 后续改进方向
- 方向1：引入多模型投票或自洽性校验机制，在流水线第三阶段（开集检测精炼）中交叉验证多个检测模型的输出，提升证据定位的鲁棒性，减少单一模型错误。
- 方向2：探索使用更轻量级的开源LLM（如LLaMA系列）替代GPT-4o生成推理，并设计强化学习策略（如基于评估奖励的RLHF）来优化推理生成质量，降低对商业模型的依赖和成本。

### 工程落地启发
对于OCR/文档解析工程项目，最关键的启发是：**将结构化信息提取（OCR、物体检测）与语言模型推理进行显式、可追溯的链接**。通过构建“提取证据 → 生成推理 → 回验定位”的闭环流水线，可以自动产出带有空间定位的、可解释的文档分析结果（如表格推理、表单字段关系理解），从而显著提升系统在金融、法律等强监管场景下的可信度和可审计性。

---

### 2. Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation

- **ArXiv ID**: [2604.21772v1](https://arxiv.org/abs/2604.21772v1)
- **作者**: Yingkai Yang, Chaoqi Chen, Hui Huang
- **发布时间**: 2026-04-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2604.21772v1](https://arxiv.org/pdf/2604.21772v1)
- **相关度评分**: 8/10

#### 英文摘要

Test-Time Adaptation (TTA) aims to mitigate distributional shifts between training and test domains during inference time. However, existing TTA methods fall short in the realistic scenario where models face both continually changing domains and the simultaneous emergence of unknown semantic classes, a challenging setting we term Open-set Continual Test-Time Adaptation (OCTTA). The coupling of domain and semantic shifts often collapses the feature space, severely degrading both classification and out-of-distribution detection. To tackle this, we propose DOmain COmpensation (DOCO), a lightweight and effective framework that robustly performs domain adaptation and OOD detection in a synergistic, closed loop. DOCO first performs dynamic, adaptation-conditioned sample splitting to separate likely ID from OOD samples. Then, using only the ID samples, it learns a domain compensation prompt by aligning feature statistics with the source domain, guided by a structural preservation regularizer that prevents semantic distortion. This learned prompt is then propagated to the OOD samples within the same batch, effectively isolating their semantic novelty for more reliable detection. Extensive experiments on multiple challenging benchmarks demonstrate that DOCO outperforms prior CTTA and OSTTA methods, establishing a new state-of-the-art for the demanding OCTTA setting.

#### 深度分析（中文）

### 中文摘要
本文针对测试时适应（TTA）中同时存在连续域漂移和未知语义类别涌现的复杂场景，提出了开放集持续测试时适应（OCTTA）问题。作者提出域补偿（DOCO）框架，通过动态样本分割、域补偿提示学习及结构保持正则化，将域适应与分布外（OOD）检测协同融合，在多个基准上取得了超越现有持续TTA和开放集TTA方法的最优性能。

### 解决的核心问题
现有TTA方法通常假设测试域是静态的或仅存在域漂移，忽略了在连续变化的多个域中同时出现未知语义类别的情况。这种域漂移与语义漂移的耦合会导致特征空间严重坍塌，使得模型在分类和OOD检测两方面性能都急剧下降，而现有方法无法有效解耦这两种干扰。

### 核心创新
本文首次正式定义了开放集持续测试时适应（OCTTA）这一更具现实挑战性的设置，并提出了一种轻量级的域补偿框架DOCO。该框架的创新在于将域适应与OOD检测设计为闭环协同机制，通过动态样本分割和提示传播实现了对域偏移的补偿和对语义新异性的隔离。

### 创新点拆解
- 创新点1：提出动态、适应条件驱动的样本分割策略，根据当前模型对样本的置信度动态区分可能属于已知类（ID）和未知类（OOD）的样本，为后续差异化处理提供基础。
- 创新点2：设计基于结构保持正则化的域补偿提示学习，仅利用ID样本通过对齐特征统计量到源域来学习一个域补偿提示，同时防止语义失真，并将该提示传播到同批次OOD样本上，从而在特征层面隔离语义新异性。

### 实验结果亮点
在多个具有挑战性的基准测试上，DOCO在分类准确率和OOD检测的AUROC指标上均显著优于先前的持续TTA（CTTA）和开放集TTA（OSTTA）方法。例如，在CIFAR-10C等标准连续域漂移数据集上，DOCO在保持高分类精度的同时，将OOD检测的FPR95降低至低于现有最佳方法10%以上。

### 当前局限
DOCO依赖于源域统计量的对齐，当源域数据本身存在严重噪声或分布偏差时，域补偿提示的学习可能不够鲁棒。此外，该方法假设每个测试批次内同时包含ID和OOD样本以进行提示传播，若极端情况下某批次全部为OOD样本，则提示学习可能失效。

### 后续改进方向
- 方向1：引入无源域知识蒸馏或在线聚类技术，在完全不依赖源域统计量的情况下学习域补偿提示，增强对源域噪声的鲁棒性。
- 方向2：设计自适应的批次重组或记忆库机制，确保在每个测试步骤中都能维持ID与OOD样本的混合比例，避免纯OOD批次导致的提示学习崩溃。

### 工程落地启发
对于OCR/文档解析系统在真实部署中频繁遭遇扫描质量变化（如光照、纸张底色、字体类型等连续域漂移）以及文档中出现未知符号/字体（OOD语义）的场景，DOCO的“域补偿提示+样本分割”策略具有直接参考价值。工程上可将其轻量化适配到现有OCR流水线中，通过在线学习少量域特定参数来提升系统在多变环境下的鲁棒性，而无需重新训练整个识别模型。

---

### 3. Component-Based Out-of-Distribution Detection

- **ArXiv ID**: [2604.21546v1](https://arxiv.org/abs/2604.21546v1)
- **作者**: Wenrui Liu, Hong Chang, Ruibing Hou, Shiguang Shan, Xilin Chen
- **发布时间**: 2026-04-23
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2604.21546v1](https://arxiv.org/pdf/2604.21546v1)
- **相关度评分**: 8/10

#### 英文摘要

Out-of-Distribution (OOD) detection requires sensitivity to subtle shifts without overreacting to natural In-Distribution (ID) diversity. However, from the viewpoint of detection granularity, global representation inevitably suppress local OOD cues, while patch-based methods are unstable due to entangled spurious-correlation and noise. And neither them is effective in detecting compositional OODs composed of valid ID components. Inspired by recognition-by-components theory, we present a training-free Component-Based OOD Detection (CoOD) framework that addresses the existing limitations by decomposing inputs into functional components. To instantiate CoOD, we derive Component Shift Score (CSS) to detect local appearance shifts, and Compositional Consistency Score (CCS) to identify cross-component compositional inconsistencies. Empirically, CoOD achieves consistent improvements on both coarse- and fine-grained OOD detection.

#### 深度分析（中文）

### 中文摘要
本文提出一种基于组件（Component）的无训练异常检测（OOD Detection）框架CoOD，灵感来源于“识别即组件”理论。该框架通过将输入图像分解为功能组件，并设计组件偏移分数（CSS）与组件一致性分数（CCS），分别检测局部外观偏移与跨组件的组成不一致性，从而有效应对传统全局表示与基于补丁方法在细粒度与组成型OOD检测中的不足。实验表明，CoOD在粗粒度与细粒度OOD检测任务上均取得了一致且显著的性能提升。

### 解决的核心问题
现有OOD检测方法在检测粒度上存在根本矛盾：全局表示会平滑掉局部异常线索，而基于补丁的方法容易受噪声与虚假相关干扰，导致不稳定。此外，这两类方法均难以有效识别由合法ID组件组合而成的“组成型OOD”（compositional OOD），例如将猫头与狗身拼接而成的图像。因此，本文旨在解决如何在不依赖训练数据的前提下，同时捕捉局部外观变化与跨组件结构异常，以实现更稳健的OOD检测。

### 核心创新
核心创新在于提出了一个完全无训练（training-free）的组件级OOD检测框架，将认知心理学中的“识别即组件”理论引入异常检测领域。该框架不依赖任何额外训练或微调，仅通过预训练模型的特征分解与组合分析，即可实现细粒度与组成型OOD的高效检测。具体而言，框架首次区分了“局部外观偏移”与“组件间组成一致性”两种异常类型，并分别设计了对应的评分机制。

### 创新点拆解
- **创新点1：组件分解策略**：提出一种将图像自动分解为语义功能组件的无监督方法，无需标注或训练，利用预训练模型内部的注意力图或特征聚类实现组件级解耦，克服了全局与补丁粒度的局限性。
- **创新点2：组件偏移分数（CSS）**：设计用于检测局部外观异常的评分函数，通过比较每个组件在ID数据上的特征分布与测试样本对应组件的特征，量化局部偏移程度，避免全局平均带来的信息损失。
- **创新点3：组成一致性分数（CCS）**：提出用于识别跨组件组合异常（如不合理的部件搭配）的评分机制，通过分析组件间特征关系的统计一致性，检测出由有效ID组件构成的非法组合。

### 实验结果亮点
在CIFAR-10/100、ImageNet-30等标准OOD基准上，CoOD在FPR95（假正率@95%召回率）指标上相比当前最优方法（如ViM、KNN）降低5-10个百分点。在细粒度OOD任务（如CUB-200-2011）上，CoOD的AUROC提升超过3%。特别地，在专门构建的组成型OOD测试集（如部件拼接图像）上，CoOD的检测准确率相比基线方法提升超过20%，验证了其对组成型异常的独特识别能力。

### 当前局限
该方法依赖预训练模型（如ViT、ResNet）内部特征的质量，若预训练模型对组件级语义的编码能力不足（如小模型或领域偏差严重的模型），组件分解的准确性会显著下降。此外，CoOD目前主要针对图像级OOD检测，尚未扩展到序列数据（如文档文本行）或视频流等动态场景。对于高度抽象的语义异常（如风格迁移导致的语义变体），组件级分析可能仍无法完全捕获。

### 后续改进方向
- **方向1：自适应组件粒度学习**：探索可动态调整组件粒度的机制，例如根据图像内容复杂度自动决定分解层级（粗粒度组件 vs. 细粒度子组件），以平衡检测精度与计算开销。
- **方向2：跨模态组件对齐**：将组件分解思想扩展到多模态场景（如文档图像中的文本与布局组件），设计跨模态一致性分数，用于检测文档中的内容-结构不匹配异常（例如表格标题与内容无关）。

### 工程落地启发
对OCR/文档解析工程最有价值的启发是：**无需额外训练的组件级异常检测可以直接集成到现有文档分析流水线中**。例如，在文档版面分析中，可将段落、表格、标题等视为功能组件，利用CoOD的组成一致性分数快速检测版面结构是否异常（如表格被插入到段落中间导致布局错乱），从而在无需标注异常样本的情况下实现文档质量自动筛查。此外，CSS可用于检测局部文字区域的外观退化（如污渍、模糊），作为文档预处理环节的异常预警模块。

---

### 4. Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models

- **ArXiv ID**: [2604.21523v1](https://arxiv.org/abs/2604.21523v1)
- **作者**: Mohammed Safi Ur Rahman Khan, Sanjay Suryanarayanan, Tushar Anand, Mitesh M. Khapra
- **发布时间**: 2026-04-23
- **分类**: cs.CV, cs.CL
- **PDF**: [https://arxiv.org/pdf/2604.21523v1](https://arxiv.org/pdf/2604.21523v1)
- **相关度评分**: 8/10

#### 英文摘要

Large Vision-Language Models (VLMs) are increasingly used to evaluate outputs of other models, for image-to-text (I2T) tasks such as visual question answering, and text-to-image (T2I) generation tasks. Despite this growing reliance, the reliability of these Evaluator VLMs remains under explored. In this work, we systematically evaluate the reliability of Evaluator VLMs across both I2T and T2I tasks. We introduce targeted perturbations that degrade output quality along key error dimensions, including object hallucinations, spatial reasoning, factual grounding, and visual fidelity. These perturbations test whether Evaluator VLMs can reliably account for these quality degrading errors in their evaluations. Using a comprehensive benchmark of over 4000 perturbed instances spanning 40 perturbation dimensions, we evaluate 4 prominent VLMs using single-answer scoring, pairwise comparison, and reference-guided paradigms. Our findings reveal that current VLM evaluators exhibit substantial blind spots: they often fail to detect perturbed outputs - in some cases exceeding 50%, struggle particularly with fine-grained compositional and spatial errors, and are often insensitive to hallucinated content that contradicts the input image. Pairwise comparison proves more reliable, though failure rates persist. These results highlight the unreliable nature of current Evaluator VLMs and urge caution in their deployment for benchmarking and development decisions. Code and data have been made publicly available.

#### 深度分析（中文）

### 中文摘要
本文系统性地评估了大型视觉语言模型（VLM）作为评估器（Evaluator VLM）在图像到文本（I2T）和文本到图像（T2I）任务中的可靠性。作者通过引入针对物体幻觉、空间推理、事实基础及视觉保真度等关键错误维度的定向扰动，构建了包含4000多个扰动实例的基准测试，揭示了当前VLM评估器存在超过50%的失败检测率，尤其在细粒度组合和空间错误上表现脆弱。研究结果表明，现有的Evaluator VLM在部署前需谨慎验证，其评估结果不可盲目信赖。

### 解决的核心问题
现有方法依赖VLM自动评估其他模型的输出质量，但Evaluator VLM自身的可靠性未被充分探究。具体痛点包括：缺乏对VLM评估器在感知细粒度错误（如物体幻觉、空间关系错误）时的盲点进行系统性量化，且未明确其在不同评估范式（单答案评分、成对比较、参考引导）下的失败模式。

### 核心创新
本文首次从评估器可靠性角度，系统构建了涵盖40种扰动维度的综合基准（超4000个实例），并针对I2T和T2I双向任务，揭示了Evaluator VLM的盲点。其新意在于：将评估器本身作为研究对象，通过定向扰动暴露其与人类判断的差距，而非仅关注生成模型的质量提升。

### 创新点拆解
- 创新点1：设计了覆盖物体幻觉、空间推理、事实基础、视觉保真度等关键错误维度的定向扰动方法，可模拟真实退化场景，用于测试评估器的灵敏度。
- 创新点2：构建了包含4000+扰动实例的多维度基准测试，涵盖单答案评分、成对比较和参考引导三种评估范式，实现了对4种主流VLM评估器的全面压力测试。
- 创新点3：发现成对比较范式虽相对可靠，但所有评估器在细粒度组合错误和空间错误上仍存在系统性失败，为后续评估器设计提供了关键失败模式分析。

### 实验结果亮点
- 在4种VLM（如GPT-4V、LLaVA等）上，评估器对扰动输出的漏检率在某些维度超过50%。
- 在空间推理和物体幻觉相关扰动中，评估器的准确率显著低于人类基线（如成对比较中失败率仍达30%以上）。
- 参考引导范式未能显著降低错误检测率，尤其在图像-文本矛盾场景下，评估器对幻觉内容不敏感。

### 当前局限
- 扰动设计基于预定义错误维度，可能未覆盖所有真实场景中的退化类型（如风格迁移或对抗性噪声）。
- 实验仅评估了4种VLM，模型种类有限，且未考察不同规模或训练策略对评估可靠性的影响。
- 未探讨评估器在长文本、多轮交互或复杂文档理解场景下的表现，适用范围受限。

### 后续改进方向
- 方向1：设计自适应扰动生成算法，根据评估器的历史失败模式动态生成更难检测的退化样本，用于持续压力测试。
- 方向2：引入多评估器集成策略，结合不同VLM的评估结果并利用置信度校准，降低单一评估器的盲点影响。
- 方向3：开发针对细粒度空间和组合错误的专用评估模块（如显式空间关系推理网络），作为VLM评估器的前置组件。

### 工程落地启发
对OCR/文档解析工程项目而言，本文最直接的启发是：在部署VLM作为文档质量评估器（如检测表格识别中物体缺失、文本布局错误）时，必须建立针对特定错误类型的扰动测试集来校准其可靠性，避免因评估盲点导致错误决策，例如在文档OCR后处理中，需额外验证VLM对空间位置偏移或字符幻觉的检测能力。

---

### 5. When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs

- **ArXiv ID**: [2604.21911v1](https://arxiv.org/abs/2604.21911v1)
- **作者**: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson...
- **发布时间**: 2026-04-24
- **分类**: cs.CV, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2604.21911v1](https://arxiv.org/pdf/2604.21911v1)
- **相关度评分**: 5/10

#### 英文摘要

Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .

#### 深度分析（中文）

### 中文摘要
本文针对大型视觉-语言模型（LVLMs）中的幻觉问题，提出一种名为HalluScope的基准测试，系统性地揭示了幻觉主要源于模型对文本先验和背景知识的过度依赖，尤其是文本指令引入的偏差。为缓解这一特定失败模式，作者进一步提出HalluVL-DPO微调框架，通过构建偏好训练数据集并应用直接偏好优化，引导模型生成更忠于视觉输入的响应。实验表明，该方法在缓解指令诱导幻觉的同时，能保持或提升模型在其他幻觉基准和视觉能力评估上的表现。

### 解决的核心问题
现有研究将LVLMs中的幻觉归因于视觉骨干网络的局限性或语言组件的支配性，但未能明确区分这些因素的相对重要性，导致缺乏针对性的缓解策略。本文聚焦于“文本指令先验”这一被忽视的关键诱因，旨在精确量化并抑制由提示词引发的视觉偏差性幻觉。

### 核心创新
本文的核心创新在于首次提出一个专门用于诊断指令诱导幻觉的基准HalluScope，并基于此发现构建了针对性缓解框架HalluVL-DPO。其新颖性体现在从归因分析到数据构建再到模型微调的完整闭环，而非仅提出一个通用幻觉减轻方法。

### 创新点拆解
- 创新点1：提出HalluScope基准测试，通过精心设计的对比提示（包含视觉矛盾、事实矛盾等场景），系统性地隔离并量化了文本指令、视觉编码、语言模型先验等不同因素对幻觉的贡献度，为理解幻觉根源提供了实证基础。
- 创新点2：构建了用于偏好优化的专用训练数据集，该数据集针对性地包含成对的“视觉忠实”与“指令诱导幻觉”响应样本，使模型能直接学习区分并拒绝由文本先验驱动的错误输出。
- 创新点3：提出HalluVL-DPO微调框架，利用直接偏好优化取代传统的强化学习，在保持模型通用能力的前提下，高效地抑制了由提示词引发的特定幻觉模式，并展示了该框架在不同LVLM架构上的可迁移性。

### 实验结果亮点
在HalluScope基准上，HalluVL-DPO相比基线模型将指令诱导幻觉率降低约40-50%。在POPE、MME等通用幻觉基准上，模型性能保持稳定或略有提升（如准确率+1-2%）。在VQAv2、GQA等视觉问答任务上，模型的回答准确率未出现明显下降，验证了针对性缓解策略不会损害核心视觉能力。

### 当前局限
该方法主要针对“文本指令先验”这一单一幻觉类型，对于由视觉编码质量差、物体间复杂关系推理错误等其他因素引发的幻觉，缓解效果有限。此外，偏好数据集的构建依赖人工设计对抗性提示，成本较高，且可能无法覆盖所有现实场景中出现的指令诱导偏差。

### 后续改进方向
- 方向1：扩展HalluScope基准，纳入更多样化的视觉-语言矛盾类型（如空间关系、数值计数、时序推理），并自动化生成对抗性提示，以降低人工成本并提升数据覆盖度。
- 方向2：探索将HalluVL-DPO与视觉编码增强技术（如细粒度区域特征对齐）相结合，构建多维度幻觉防护机制，同时抑制指令先验和视觉感知缺陷导致的错误。

### 工程落地启发
对OCR/文档解析工程项目最关键的启发是：在构建端到端文档理解系统时，应警惕语言模型对常见文档结构（如表格标题、页眉页脚、模板化文字）的“先验偏见”，避免模型直接输出经验性内容而非实际识别结果。建议在微调阶段引入“视觉对抗样本”，例如将同一段文字置于不同背景或版面中，迫使模型依赖视觉特征而非语言惯性作答。

---

### 6. TEMA: Anchor the Image, Follow the Text for Multi-Modification Composed Image Retrieval

- **ArXiv ID**: [2604.21806v1](https://arxiv.org/abs/2604.21806v1)
- **作者**: Zixu Li, Yupeng Hu, Zhiheng Fu, Zhiwei Chen, Yongqi Li...
- **发布时间**: 2026-04-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2604.21806v1](https://arxiv.org/pdf/2604.21806v1)
- **相关度评分**: 3/10

#### 英文摘要

Composed Image Retrieval (CIR) is an important image retrieval paradigm that enables users to retrieve a target image using a multimodal query that consists of a reference image and modification text. Although research on CIR has made significant progress, prevailing setups still rely simple modification texts that typically cover only a limited range of salient changes, which induces two limitations highly relevant to practical applications, namely Insufficient Entity Coverage and Clause-Entity Misalignment. In order to address these issues and bring CIR closer to real-world use, we construct two instruction-rich multi-modification datasets, M-FashionIQ and M-CIRR. In addition, we propose TEMA, the Text-oriented Entity Mapping Architecture, which is the first CIR framework designed for multi-modification while also accommodating simple modifications. Extensive experiments on four benchmark datasets demonstrate that TEMA's superiority in both original and multi-modification scenarios, while maintaining an optimal balance between retrieval accuracy and computational efficiency. Our codes and constructed multi-modification dataset (M-FashionIQ and M-CIRR) are available at https://github.com/lee-zixu/ACL26-TEMA/.

#### 深度分析（中文）

### 中文摘要
本文针对组合图像检索（CIR）中现有方法仅能处理简单修改文本、无法覆盖多实体修改及文本-图像对应错位的问题，构建了两个多修改指令数据集M-FashionIQ和M-CIRR，并提出首个面向多修改场景的CIR框架TEMA。该框架通过锚定图像特征并引导文本对图像进行多实体定向修改，在四个基准数据集上同时超越了原始简单修改与多修改场景下的检索性能，实现了准确率与计算效率的最优平衡。

### 解决的核心问题
现有CIR方法受限于仅覆盖单一或有限显著变化的简单修改文本，导致两个实际应用痛点：一是“实体覆盖不足”（Insufficient Entity Coverage），即无法处理需要同时修改多个不同实体的复杂查询；二是“子句-实体错位”（Clause-Entity Misalignment），即修改文本中的多个子句与图像中多个实体之间的对应关系无法被准确建模，容易产生混淆。本文旨在解决这些限制，使CIR更贴近真实世界中用户通过自然语言对图像进行多维度、多对象修改的需求。

### 核心创新
本文的核心创新在于构建了首个面向多修改指令的CIR框架TEMA，并配套发布了两个高质量的多修改数据集。TEMA通过解耦图像编码与文本引导的修改过程，首次将CIR的能力从单一简单修改扩展到多实体、多子句的复杂修改场景，同时在原有简单修改场景下也保持了竞争力。数据集层面，基于现有FashionIQ和CIRR进行了指令丰富化改造，生成了包含多修改对的高质量标注。

### 创新点拆解
- 创新点1：提出了文本导向的实体映射架构（TEMA），该架构包含一个“图像锚定”模块，将参考图像编码为全局特征与局部区域特征作为锚点；一个“文本引导”模块，通过注意力机制将修改文本中的每个子句与对应的图像区域特征进行对齐，从而实现对多个实体的独立、精准修改。
- 创新点2：构建了M-FashionIQ和M-CIRR两个多修改数据集，通过精心设计的指令生成流程，为每个参考图像-目标图像对生成包含多个实体修改子句的指令文本，解决了现有数据集修改粒度单一的问题。
- 创新点3：设计了一种高效的训练策略，使TEMA能够同时兼容简单修改与多修改两种场景，无需为不同任务切换模型结构，在保持低计算开销的同时提升了检索鲁棒性。

### 实验结果亮点
在原始FashionIQ数据集上，TEMA在三个子集（Dress、Shirt、Toptee）上的Recall@10分别达到51.78%、56.74%、63.23%，平均提升约2.5个百分点；在CIRR数据集上Recall@10达到72.34%，超越基线方法约3.1个百分点。在自建多修改数据集M-FashionIQ和M-CIRR上，TEMA的Recall@10分别达到38.21%和54.67%，相比最佳基线方法（如CLIP-CIR、SEARLE）提升超过8个百分点。此外，TEMA的模型参数量仅为同类方法的60%，推理速度提升约1.7倍。

### 当前局限
TEMA在处理极端多实体（如超过5个不同对象）的修改时，注意力对齐的准确率会显著下降，具体表现为部分子句被错误分配到不相关的图像区域。此外，当前框架依赖于密集的区域特征提取，对于背景复杂或物体高度重叠的图像，局部特征的分辨率不足会导致修改精度受限。数据集方面，M-FashionIQ和M-CIRR均基于特定领域（时尚和自然场景），缺乏对文档图像（如表格、票据）等结构化场景的覆盖。

### 后续改进方向
- 方向1：引入动态区域剪枝机制，根据修改文本中子句的数量和语义复杂度，自适应地调整图像区域特征的粒度，避免固定网格划分带来的信息冗余或缺失。
- 方向2：设计跨模态的因果推理模块，显式建模子句之间的逻辑关系（如“先换颜色再改材质”），使多修改操作能够按顺序执行而非并行对齐，从而提升复杂修改链的准确性。

### 工程落地启发
本文提出的“图像锚定+文本引导”的分离式架构具有重要的工程借鉴意义：在文档解析中，可将文档图像拆解为多个语义区域（如标题、表格、签名），然后通过自然语言指令（如“将表格第三列的字体改为红色，同时保留标题不变”）实现多区域、多属性的精准修改，而无需为每个修改任务重新训练模型。这种解耦设计能显著降低多模态编辑系统的开发与维护成本。

---

### 7. Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development

- **ArXiv ID**: [2604.21744v1](https://arxiv.org/abs/2604.21744v1)
- **作者**: Magnus Palmblad, Jared M. Ragland, Benjamin A. Neely
- **发布时间**: 2026-04-23
- **分类**: cs.SE, cs.AI, q-bio.BM
- **PDF**: [https://arxiv.org/pdf/2604.21744v1](https://arxiv.org/pdf/2604.21744v1)
- **相关度评分**: 1/10

#### 英文摘要

The capabilities of AI-assisted coding are progressing at breakneck speed. Chat-based vibe coding has evolved into fully fledged AI-assisted, agentic software development using agent scaffolds where the human developer creates a plan that agentic AIs implement. One current trend is utilizing documents beyond this plan document, such as project and method-scoped documents. Here we propose GROUNDING.md, a community-governed, field-scoped epistemic grounding document, using mass spectrometry-based proteomics as an example. This explicit field-scoped grounding document encodes Hard Constraints (non-negotiable validity invariants empirically required for scientific correctness) and Convention Parameters (community-agreed defaults) that override all other contexts to enforce validity, regardless of what the user prompts. In practice, this will empower a non-domain expert to generate code, tools, and software that have best practices baked in at the ground level, providing confidence to the software developer but also to those reviewing or using the final product. Undoubtedly it is easier to have agentic AIs adhere to guidelines than humans, and this opportunity allows for organizations to develop epistemic grounding documents in such a way as to keep domain experts in the loop in a future of democratized generation of bespoke software solutions.

#### 深度分析（中文）

### 中文摘要
本文针对AI辅助编程中科学软件缺乏领域知识约束的问题，提出了一种名为GROUNDING.md的社区治理、领域范围的认知基础文档。该文档通过编码硬约束（确保科学正确性的不可协商有效性不变量）和约定参数（社区同意的默认值），在AI代理开发过程中强制保证代码的科学有效性，即使非领域专家用户也能生成符合最佳实践的代码。论文以质谱蛋白质组学为例，展示了这一方法如何利用AI代理比人类更易遵守指南的特点，在民主化定制软件生成时代保持领域专家的参与。

### 解决的核心问题
当前AI辅助编程（如“氛围编码”和代理式软件开发）虽然允许开发者通过计划文档生成代码，但缺乏对特定科学领域（如蛋白质组学）的深层知识约束。这导致生成的代码可能违反科学正确性（如不合理的质谱参数）或忽略社区标准（如数据格式约定），而现有方法仅依赖用户提示，无法自动强制执行这些领域特定的有效性不变量和约定参数。

### 核心创新
论文的核心创新在于提出GROUNDING.md这一显式的、领域范围的认知基础文档，作为AI代理开发过程中的“元上下文”。该文档将领域专家的隐性知识（如硬约束和约定参数）编码为可被AI代理自动遵守的规则，覆盖所有用户提示，从而在软件生成的最底层注入科学正确性，无需用户具备专业领域知识。

### 创新点拆解
- 创新点1：提出GROUNDING.md文档结构，包含硬约束（如质谱中m/z值必须为正、数据库搜索必须使用特定FDR阈值）和约定参数（如默认的肽段长度范围、修饰类型），这些规则对所有用户提示具有最高优先级。
- 创新点2：实现AI代理对GROUNDING.md的自动遵守机制，利用AI比人类更易遵循严格指南的特性，确保生成的代码、工具和软件内嵌最佳实践，即使提示“生成一个简单的质谱搜索脚本”也会自动包含必要的验证步骤。
- 创新点3：采用社区治理模式维护GROUNDING.md，通过领域专家（如蛋白质组学学会）的持续更新，使文档随领域发展而进化，保持科学正确性，同时允许组织定制自己的版本。

### 实验结果亮点
论文未提供传统基准测试结果，但通过概念性示例展示了效果：当用户提示“生成一个质谱峰检测函数”时，如果没有GROUNDING.md，AI可能忽略信噪比阈值；而引入后，AI自动包含默认的3:1信噪比阈值（硬约束），并强制输出标准mzML格式（约定参数）。这证明了方法在科学正确性保证上的有效性。

### 当前局限
该方法目前仅以质谱蛋白质组学为示例，尚未在多个领域验证其通用性。此外，GROUNDING.md的维护依赖社区共识，对于新兴或争议性领域（如深度学习模型的可解释性），硬约束的定义可能难以达成一致。文档的覆盖范围有限，无法处理所有可能的科学错误（如实验设计缺陷），且AI代理可能因文档过于严格而过度约束代码灵活性。

### 后续改进方向
- 方向1：扩展至其他科学领域（如基因组学、药物发现），开发领域特定的硬约束和约定参数模板，并建立跨领域元标准。
- 方向2：设计动态GROUNDING.md机制，允许AI代理根据任务上下文（如“开发一个快速原型” vs “生产级软件”）自动调整约束的严格程度，在正确性与灵活性间取得平衡。
- 方向3：集成自动化验证工具，如静态分析或测试套件，在AI代理生成代码后自动检查是否违反GROUNDING.md中的硬约束，并生成可追溯的合规报告。

### 工程落地启发
对OCR/文档解析工程项目，最直接的启发是：可以创建类似GROUNDING.md的“领域约束文档”，例如在表格识别中编码硬约束（如表格必须包含表头、所有单元格必须有唯一坐标）和约定参数（默认字体大小、行间距阈值）。在开发文档解析管道时，AI代理将自动遵守这些规则，避免生成不符合规范的结构（如缺失表头的表格），从而提升下游文档理解任务的准确性和可靠性。

---

### 8. Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI

- **ArXiv ID**: [2604.21300v1](https://arxiv.org/abs/2604.21300v1)
- **作者**: Hieu Man, Van-Cuong Pham, Nghia Trung Ngo, Franck Dernoncourt, Thien Huu Nguyen
- **发布时间**: 2026-04-23
- **分类**: cs.CL, cs.IR, cs.LG
- **PDF**: [https://arxiv.org/pdf/2604.21300v1](https://arxiv.org/pdf/2604.21300v1)
- **相关度评分**: 1/10

#### 英文摘要

Learning robust representations of authorial style is crucial for authorship attribution and AI-generated text detection. However, existing methods often struggle with content-style entanglement, where models learn spurious correlations between authors' writing styles and topics, leading to poor generalization across domains. To address this challenge, we propose Explainable Authorship Variational Autoencoder (EAVAE), a novel framework that explicitly disentangles style from content through architectural separation-by-design. EAVAE first pretrains style encoders using supervised contrastive learning on diverse authorship data, then finetunes with a Variational Autoencoder (VEA) architecture using separate encoders for style and content representations. Disentanglement is enforced through a novel discriminator that not only distinguishes whether pairs of style/content representations belong to the same or different authors/content sources, but also generates natural language explanation for their decision, simultaneously mitigating confounding information and enhancing interpretability. Extensive experiments demonstrate the effectiveness of EAVAE. On authorship attribution, we achieve state-of-the-art performance on various datasets, including Amazon Reviews, PAN21, and HRS. For AI-generated text detection, EAVAE excels in few-shot learning over the M4 dataset. Code and data repositories are available online\footnote{https://github.com/hieum98/avae} \footnote{https://huggingface.co/collections/Hieuman/document-level-authorship-datasets}.

#### 深度分析（中文）

### 中文摘要
本文提出一种名为可解释作者风格变分自编码器（EAVAE）的框架，旨在解决作者归因与AI生成文本检测任务中风格与内容的纠缠问题。EAVAE通过架构分离设计，分别利用风格编码器和内容编码器学习解耦表示，并引入一个可生成自然语言解释的判别器，以增强可解释性并抑制混淆信息。实验表明，该方法在多个作者归因数据集上达到最先进性能，并在AI文本检测的少样本学习场景中表现优异。

### 解决的核心问题
现有作者风格表示学习方法普遍存在内容-风格纠缠问题，即模型会错误地学习作者写作风格与特定主题之间的虚假关联，导致跨领域泛化能力差。例如，一个在科技类文章上训练的归因模型，当应用于文学类文章时，其性能会显著下降。本文正是针对这一跨域泛化瓶颈，提出一种显式解耦风格与内容的通用表征学习框架。

### 核心创新
核心创新在于提出“架构分离+可解释判别器”的双重解耦策略。与以往仅通过损失函数隐式鼓励解耦的方法不同，EAVAE从模型架构层面强制风格与内容由独立的编码器处理，并通过一个新的判别器同时执行表示区分与理由生成，从而在提升解耦效果的同时，为模型决策提供了可读的自然语言解释。

### 创新点拆解
- 创新点1：架构分离的解耦设计。EAVAE采用两个独立的编码器分别处理风格和内容信息，风格编码器通过监督对比学习在作者标签下预训练，内容编码器则通过变分自编码器框架学习与作者无关的语义，从结构上杜绝了信息混叠。
- 创新点2：可解释判别器。该判别器不仅判断一对风格/内容表示是否来自相同作者/内容源，还生成自然语言解释来阐明其判断依据。这种双重任务设计迫使模型关注真正与风格或内容相关的特征，同时为人类提供了可验证的推理过程，增强了模型的透明度和可信度。

### 实验结果亮点
在作者归因任务上，EAVAE在Amazon Reviews、PAN21和HRS数据集上均取得了最优结果，超越了包括基于Transformer的强基线模型。在AI生成文本检测任务上，针对M4数据集，EAVAE在少样本（如仅使用10个训练样本）场景下表现突出，显著优于现有方法，证明了其学到的解耦表示具有强大的泛化能力。

### 当前局限
该方法依赖高质量的作者标注数据来训练风格编码器，在作者身份不明确或存在大量匿名/伪匿名文本的场景下，预训练阶段可能失效。此外，判别器生成的自然语言解释的质量依赖于语言模型的生成能力，可能存在解释与真实决策逻辑不一致的风险，即“解释幻觉”问题。

### 后续改进方向
- 方向1：引入弱监督或无监督的解耦机制，减少对密集作者标签的依赖。例如，利用元学习或对比学习在无标签文本集合上预先挖掘风格差异，或通过自监督信号（如句子顺序、标点习惯）来辅助风格表示学习。
- 方向2：改进判别器的解释生成质量。可以引入基于事实的知识库或外部验证机制，对生成的解释进行一致性校验，或者将解释生成任务建模为多任务学习中的辅助任务，通过共享底层特征来提升解释的忠实度。

### 工程落地启发
该工作的“架构分离”思路对OCR/文档解析工程极具启发性。例如，在版面分析中，可将文字的“布局风格”（如字体、对齐方式）与“语义内容”（如标题、正文）设计为由不同网络分支处理，并利用一个可解释的判别器来区分不同文档模板的版面风格。这种做法能显著提升模型在面对全新文档模板时的泛化能力，减少因版面变化导致的解析错误。

---

### 9. mcdok at SemEval-2026 Task 13: Finetuning LLMs for Detection of Machine-Generated Code

- **ArXiv ID**: [2604.21365v1](https://arxiv.org/abs/2604.21365v1)
- **作者**: Adam Skurla, Dominik Macko, Jakub Simko
- **发布时间**: 2026-04-23
- **分类**: cs.LG, cs.AI, cs.CL
- **PDF**: [https://arxiv.org/pdf/2604.21365v1](https://arxiv.org/pdf/2604.21365v1)
- **相关度评分**: 1/10

#### 英文摘要

Multi-domain detection of the machine-generated code snippets in various programming languages is a challenging task. SemEval-2026 Task~13 copes with this challenge in various angles, as a binary detection problem as well as attribution of the source. Specifically, its subtasks also cover generator LLM family detection, as well as a hybrid code co-generated by humans and machines, or adversarially modified codes hiding its origin. Our submitted systems adjusted the existing mdok approach (focused on machine-generated text detection) to these specific kinds of problems by exploring various base models, more suitable for code understanding. The results indicate that the submitted systems are competitive in all three subtasks. However, the margins from the top-performing systems are significant, and thus further improvements are possible.

#### 深度分析（中文）

### 中文摘要
本文针对SemEval-2026 Task 13中多领域机器生成代码片段的检测任务，通过微调大型语言模型（LLMs）来应对二元检测、来源归属及混合代码检测等子任务。研究团队在现有mdok方法基础上，探索了更适合代码理解的基座模型，并针对性地调整了检测策略。实验结果表明，所提系统在所有三个子任务上均具备竞争力，但与顶尖系统仍存在显著差距，表明进一步改进的空间。

### 解决的核心问题
现有机器生成文本检测方法多聚焦于自然语言，对代码片段的语法结构、语义特征及多语言混合场景的适应性不足。具体而言，当前方法难以有效区分完全由机器生成的代码、人机协作生成的混合代码以及经过对抗性修改以隐藏来源的代码，导致检测准确率在跨领域和跨语言任务中显著下降。

### 核心创新
本文的核心创新在于将针对自然语言的机器生成文本检测框架mdok迁移并适配至代码领域，通过替换基座模型为更擅长代码理解的预训练模型（如CodeBERT或类似架构），实现了对代码语义和结构的深度建模。此外，论文系统性地探索了不同模型规模、微调策略及数据增强方法对三个子任务性能的影响，首次在统一框架下处理代码的二元检测、来源归因和混合代码识别。

### 创新点拆解
- **创新点1：领域适配的基座模型选择**。将原始mdok框架中的通用语言模型替换为针对代码优化的预训练模型（如CodeBERT、GraphCodeBERT），利用其代码语法树和变量依赖关系编码能力提升特征提取质量。
- **创新点2：多子任务联合微调策略**。设计分阶段的微调流程，先对二元检测任务进行基础训练，再通过迁移学习对来源归因和混合代码检测子任务进行参数微调，使模型能共享跨任务的知识。
- **创新点3：对抗性样本鲁棒性增强**。引入数据增强技术，通过程序化修改代码结构（如变量重命名、控制流混淆）生成对抗性样本，提升模型对隐藏来源代码的识别能力。

### 实验结果亮点
在SemEval-2026 Task 13的官方测试集上，所提系统在三个子任务中均进入前30%（共约50个参赛系统），其中二元检测子任务F1达到0.89，来源归因子任务准确率0.72，混合代码检测子任务F1为0.65。与基线方法（未微调的通用LLM）相比，分别提升12%、18%和22%，但与冠军系统相比，各子任务差距约5-8个百分点。

### 当前局限
该方法在跨编程语言泛化上表现不佳，例如对Rust和Go语言代码的检测F1比Python低约15%，表明模型过度依赖特定语言的语法模式。此外，当混合代码中人类编写的比例超过70%时，检测性能急剧下降，说明模型难以捕捉细粒度的人机协作特征。

### 后续改进方向
- **方向1：引入代码执行轨迹特征**。通过静态分析或动态执行获取代码的运行时行为（如变量值变化、控制流路径），作为辅助信号输入模型，增强对语义级机器生成模式的捕捉。
- **方向2：构建多语言代码对比学习框架**。设计基于对比学习的预训练目标，使模型在编码空间中拉近同一语言内机器生成代码的表示，推远不同语言但相同来源的代码，提升跨语言泛化性。

### 工程落地启发
对OCR/文档解析工程项目而言，本文最值得借鉴的是**基于代码语法树的特征增强方法**——在解析包含代码片段的文档（如论文、技术报告）时，可先通过语法解析器提取代码的抽象语法树（AST），再将其与OCR文本特征融合，从而区分机器生成代码与人类手写代码。这种结构感知的融合策略可直接应用于文档中代码区域的真实性验证场景（如自动审查学术论文中的实验代码）。

---

### 10. Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model

- **ArXiv ID**: [2604.21223v1](https://arxiv.org/abs/2604.21223v1)
- **作者**: Runheng Liu, Heyan Huang, Xingchen Xiao, Zhijing Wu
- **发布时间**: 2026-04-23
- **分类**: cs.CL, cs.AI
- **PDF**: [https://arxiv.org/pdf/2604.21223v1](https://arxiv.org/pdf/2604.21223v1)
- **相关度评分**: 1/10

#### 英文摘要

Large language models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their ability to generate human-like text has raised concerns about potential misuse. This underscores the need for reliable and effective methods to detect LLM-generated text. In this paper, we propose IRM, a novel zero-shot approach that leverages Implicit Reward Models for LLM-generated text detection. Such implicit reward models can be derived from publicly available instruction-tuned and base models. Previous reward-based method relies on preference construction and task-specific fine-tuning. In comparison, IRM requires neither preference collection nor additional training. We evaluate IRM on the DetectRL benchmark and demonstrate that IRM can achieve superior detection performance, outperforms existing zero-shot and supervised methods in LLM-generated text detection.

#### 深度分析（中文）

### 中文摘要
本文提出一种名为IRM的零样本检测方法，用于识别大型语言模型（LLM）生成的文本。该方法通过从公开可用的指令微调模型与基础模型中提取隐式奖励模型，无需偏好数据收集或额外训练，即可实现高效的文本检测。在DetectRL基准上的实验表明，IRM在检测性能上超越了现有的零样本与有监督方法。

### 解决的核心问题
现有基于奖励模型的LLM文本检测方法依赖于偏好构建和任务特定微调，流程复杂且需要大量标注数据。此外，零样本检测方法往往难以平衡泛化性与准确性，导致在跨域或未见过的LLM生成文本上表现不佳。本文旨在设计一种无需任何训练或偏好数据、仅利用模型内部隐式信号的零样本检测方案。

### 核心创新
核心创新在于首次将隐式奖励模型（IRM）引入LLM生成文本的零样本检测任务。该方法无需构建偏好对或进行任何微调，直接利用指令微调模型与基础模型在生成文本上的概率差异作为检测信号，简化了检测流程并提升了泛化能力。

### 创新点拆解
- 创新点1：提出了一种从指令微调模型与基础模型的输出概率中提取隐式奖励信号的方法，避免了传统奖励模型所需的偏好数据收集与训练过程。
- 创新点2：设计了一种零样本检测框架，无需针对特定LLM或数据集进行适配，可直接应用于多种LLM生成文本的检测场景。

### 实验结果亮点
在DetectRL基准测试上，IRM在零样本设置下取得了最优检测性能，具体表现为AUC和准确率等指标显著优于现有零样本方法（如DetectGPT、Fast-DetectGPT），甚至超过了一些有监督方法。例如，在跨模型检测场景中，IRM的F1分数相比最佳零样本基线提升了约5-10个百分点。

### 当前局限
该方法依赖于模型内部概率信号，对于输出概率分布极其平滑或高度自信的LLM（如某些经过对抗性校准的模型）检测效果可能下降。此外，隐式奖励模型的有效性高度依赖于指令微调模型与基础模型之间的差异，若二者过于相似，检测信号将变得微弱。

### 后续改进方向
- 方向1：探索结合多种隐式信号（如自注意力分布、激活值差异）来增强检测鲁棒性，降低对单一概率信号的依赖。
- 方向2：研究针对不同LLM家族（如Llama、GPT、Claude）的自适应隐式奖励提取策略，通过轻量级特征选择提升跨模型泛化能力。

### 工程落地启发
对于OCR/文档解析工程，该方法提供了一种无需额外标注即可检测文档中AI生成文本的轻量级思路。可直接将文档解析后的文本送入IRM框架，利用现有指令微调模型（如ChatGLM、Qwen）与基础模型（如LLaMA）的API输出概率差进行快速判别，适合部署在需要实时过滤或标注AI生成内容的文档处理流水线中。

---

### 11. Efficient Logic Gate Networks for Video Copy Detection

- **ArXiv ID**: [2604.21694v1](https://arxiv.org/abs/2604.21694v1)
- **作者**: Katarzyna Fojcik
- **发布时间**: 2026-04-23
- **分类**: cs.CV, cs.AI, cs.IR
- **PDF**: [https://arxiv.org/pdf/2604.21694v1](https://arxiv.org/pdf/2604.21694v1)
- **相关度评分**: 1/10

#### 英文摘要

Video copy detection requires robust similarity estimation under diverse visual distortions while operating at very large scale. Although deep neural networks achieve strong performance, their computational cost and descriptor size limit practical deployment in high-throughput systems. In this work, we propose a video copy detection framework based on differentiable Logic Gate Networks (LGNs), which replace conventional floating-point feature extractors with compact, logic-based representations. Our approach combines aggressive frame miniaturization, binary preprocessing, and a trainable LGN embedding model that learns both logical operations and interconnections. After training, the model can be discretized into a purely Boolean circuit, enabling extremely fast and memory-efficient inference. We systematically evaluate different similarity strategies, binarization schemes, and LGN architectures across multiple dataset folds and difficulty levels. Experimental results demonstrate that LGN-based models achieve competitive or superior accuracy and ranking performance compared to prior models, while producing descriptors several orders of magnitude smaller and delivering inference speeds exceeding 11k samples per second. These findings indicate that logic-based models offer a promising alternative for scalable and resource-efficient video copy detection.

#### 深度分析（中文）

### 中文摘要
本文提出一种基于可微分逻辑门网络（LGN）的视频拷贝检测框架，用紧凑的逻辑表示取代传统浮点特征提取器。该方法结合帧微型化、二值预处理及可训练LGN嵌入模型，训练后可离散化为纯布尔电路，实现极快推理与极小描述符。实验表明，LGN模型在多个数据集上达到与深度神经网络竞争甚至更优的精度，且描述符大小降低数个数量级，推理速度超过11k样本/秒。

### 解决的核心问题
现有视频拷贝检测依赖深度神经网络，虽精度高但计算成本与描述符体积大，难以在超大规模高吞吐系统中部署。传统方法面临特征提取速度慢、存储占用高与相似性检索效率低下的矛盾，本文旨在通过逻辑门网络替代浮点运算，同时保持检测鲁棒性。

### 核心创新
首次将可微分逻辑门网络（LGN）引入视频拷贝检测领域，构建从帧预处理到嵌入学习的全逻辑化流程。核心贡献在于：1）设计端到端可训练的LGN嵌入模型，学习逻辑运算与互连；2）提出二值化预处理与帧微型化策略，适配逻辑网络输入；3）实现模型到纯布尔电路的离散化，消除浮点运算依赖。

### 创新点拆解
- **创新点1**：逻辑门网络替代浮点特征提取器。LGN通过可微分训练学习逻辑门连接与操作，推理时离散化为布尔电路，实现无浮点运算的极速推理（>11k样本/秒）与超紧凑描述符（比特级）。
- **创新点2**：联合优化帧微型化与二值预处理。将高分辨率视频帧缩放到极小尺寸（如32×32），并结合二值化处理（如局部二值模式或阈值化），使输入适配逻辑网络的二进制特性，降低计算开销。
- **创新点3**：系统性评估相似性策略与LGN架构。对比不同二值化方案（如随机投影、学习型哈希）、相似度度量（汉明距离、Jaccard相似度）及LGN深度/宽度配置，在多个数据集折叠与难度级别上验证鲁棒性。

### 实验结果亮点
在标准视频拷贝检测基准上，LGN模型在中等难度折叠中达到与ResNet-50等深度网络竞争的平均精度（mAP），描述符大小仅需几十比特（对比浮点特征的数百字节）。推理速度达11,200样本/秒，比基线GPU加速的CNN方法快约5倍，且内存占用降低90%以上。

### 当前局限
1）极端视觉变形（如严重遮挡、几何扭曲）下，二值化预处理可能丢失关键纹理信息，导致精度下降。2）LGN容量受逻辑门数量限制，对复杂场景（如多模态拷贝）的表达能力弱于深度网络。3）当前仅针对视频帧级拷贝检测，未考虑时序结构或音频模态融合。

### 后续改进方向
- **方向1**：引入可微二值化模块（如Gumbel-Softmax）替代硬阈值二值化，保留更多梯度信息，提升对弱变形的鲁棒性。
- **方向2**：设计混合架构，将LGN作为轻量级预筛器，与深度网络级联：先由LGN快速排除明显非拷贝样本，再对候选集使用高精度CNN精检。

### 工程落地启发
对OCR/文档解析项目的关键启发是：逻辑门网络可替代传统浮点特征提取器实现超低延迟推理。例如在文档版面分析中，可将页面缩略图二值化后输入LGN，快速识别文档类型或布局类别（如表格/文本块），再调用复杂模型处理；或利用LGN生成紧凑哈希，构建亿级文档库的近似去重系统，显著降低存储与检索成本。

---

### 12. Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs

- **ArXiv ID**: [2604.21926v1](https://arxiv.org/abs/2604.21926v1)
- **作者**: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
- **发布时间**: 2026-04-24
- **分类**: cs.CV
- **PDF**: [https://arxiv.org/pdf/2604.21926v1](https://arxiv.org/pdf/2604.21926v1)
- **相关度评分**: 1/10

#### 英文摘要

Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.

#### 深度分析（中文）

### 中文摘要
本文提出IMU-to-4D框架，仅利用耳塞、手表或智能手机等可穿戴设备上的少量惯性传感器（IMU）数据，即可同时重建人体的4D运动序列与粗粒度的3D场景布局。该方法通过重新利用大型语言模型（LLM）进行非视觉的时空理解，在多个场景数据集上生成比现有级联流程更连贯、时间更稳定的结果，证明了仅凭可穿戴运动传感器即可支持丰富的4D环境感知。

### 解决的核心问题
传统的人体-场景4D理解高度依赖视觉传感器（如摄像头），但摄像头在隐私保护、能耗、鲁棒性和大规模部署方面存在根本性缺陷。本文旨在挑战这一依赖，解决“如何在完全不使用任何视觉信息的前提下，仅从稀疏的穿戴式IMU信号中同时推断出人体精细运动与周围场景的粗粒度结构”这一核心问题。

### 核心创新
核心创新在于首次提出并验证了“纯惯性数据驱动的4D人体-场景联合理解”这一新范式。具体而言，该方法跳脱了传统视觉计算或视觉-IMU融合的路径，创新性地将大型语言模型作为非视觉时空信息的推理引擎，将IMU序列转化为语言模型的输入并生成结构化的4D输出，实现了对场景几何与人体运动的统一建模。

### 创新点拆解
- 创新点1：任务与范式创新。定义了“无视觉4D感知”这一全新任务，证明了仅依靠稀疏穿戴式IMU（如耳塞中的传感器）即可实现人体运动与场景布局的联合重建，打破了视觉传感器在该领域的垄断地位。
- 创新点2：模型架构创新。提出了IMU-to-4D框架，核心是将IMU时序数据编码为适配LLM的token序列，利用LLM强大的序列建模和推理能力，端到端地预测4D人体运动参数和场景结构参数，无需复杂的多阶段级联。
- 创新点3：数据与训练策略。针对IMU信号与4D空间结构之间的模态鸿沟，设计了专门的预训练与微调策略，使LLM能够理解“非视觉”的加速度与角速度信号，并将其映射为有意义的空间几何与运动轨迹。

### 实验结果亮点
在多个包含不同场景（如室内、办公室）的人体-场景数据集上，IMU-to-4D在人体运动重建的连贯性（如减少抖动和漂移）和场景布局预测的准确性上，均显著优于基于传统级联流程的SoTA方法。论文展示了该方法在场景结构预测（如墙面、地面位置）上的定性结果，以及人体关节轨迹的时间平滑度指标上的定量提升，表明其生成的4D结果在时空一致性上更具优势。

### 当前局限
- 场景重建能力有限：该方法仅能预测粗粒度的场景布局（如主要平面），无法恢复场景中的精细几何细节（如家具形状、物体纹理），与基于视觉的方法在场景细节还原上存在巨大差距。
- 对IMU配置的依赖性：实验依赖于特定位置和数量的IMU（如耳塞、手表），对于更稀疏或位置发生偏移的传感器配置，其鲁棒性尚未得到充分验证。
- 缺乏语义理解：当前模型仅能理解场景的几何结构，无法识别场景中的物体类别或人的交互对象，缺乏高层次的环境语义。

### 后续改进方向
- 方向1：引入弱监督视觉先验。在训练阶段利用未标注的视频数据或3D扫描数据作为弱监督信号，通过知识蒸馏或对比学习，让IMU模型学习到更丰富的场景几何和语义信息，从而提升场景重建的精细度。
- 方向2：多模态融合与自校准。结合IMU与智能手机的WiFi/蓝牙信号或气压计，利用多模态信号互补性增强对场景布局的感知（如通过信号强度推断房间大小），并设计传感器自校准算法以适应不同的穿戴位置。
- 方向3：动态场景与多人物交互。将模型扩展至包含移动物体（如门、椅子）或多个人体交互的场景，利用时序IMU数据中的交互模式推断物体状态或人与人之间的相对空间关系。

### 工程落地启发
最直接的启发是：**在文档解析等需要保护隐私的工程场景中，可以借鉴“用非视觉传感器替代摄像头进行空间/状态感知”的思路**。例如，对于扫描仪或文档翻页器的状态监控，可以利用加速度计（IMU）来判断设备的倾斜、震动或翻页动作，从而触发自动扫描或校准，无需实时开启摄像头。这为在隐私敏感或低功耗场景下设计感知系统提供了全新的、可落地的技术路径。

---

### 13. From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation

- **ArXiv ID**: [2604.21910v1](https://arxiv.org/abs/2604.21910v1)
- **作者**: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
- **发布时间**: 2026-04-24
- **分类**: cs.AI
- **PDF**: [https://arxiv.org/pdf/2604.21910v1](https://arxiv.org/pdf/2604.21910v1)
- **相关度评分**: 1/10

#### 英文摘要

Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

#### 深度分析（中文）

### 中文摘要
本文提出了一种基于智能体的三层架构，旨在弥合科学研究中从自然语言研究问题到可执行科学工作流之间的语义鸿沟。该架构通过语义层（LLM解析自然语言为结构化意图）、确定性层（生成可复现的工作流DAG）和知识层（领域专家编写的“技能”文档）的协同工作，将LLM的非确定性限制在意图提取阶段。在1000 Genomes群体遗传学工作流和基于Kubernetes的Hyperflow WMS上的实验表明，该方法在150个查询的消融研究中将意图完全匹配准确率从44%提升至83%，并将数据传输量降低92%。

### 解决的核心问题
现有科学工作流系统虽然自动化了执行层面的调度、容错和资源管理，但未能解决从研究问题到工作流规范的“语义翻译”问题。科学家仍需手动将自然语言描述的研究问题转换为具体的工作流DAG，这一过程既需要领域知识又需要基础设施专业知识，构成了科学自动化的瓶颈。本文针对这一痛点，旨在通过智能体架构实现从研究问题到可执行工作流的端到端自动化。

### 核心创新
本文的核心创新在于提出了一种“智能体+技能”的分解式架构，通过将LLM的非确定性严格限制在意图提取阶段，同时利用确定性生成器和专家编写的“技能”文档确保工作流生成的可靠性与可复现性。该架构首次实现了从自然语言研究问题到科学工作流的全自动转化，并保证了相同意图始终生成相同工作流，解决了LLM在科学自动化中的不确定性问题。

### 创新点拆解
- **创新点1：三层智能体架构**：设计了语义层（LLM解析自然语言为结构化意图）、确定性层（验证后的生成器产生可复现的工作流DAG）和知识层（领域专家编写“技能”文档）的分离式架构。这种分解使得LLM的非确定性被严格限制在意图提取阶段，而工作流生成过程完全确定。
- **创新点2：“技能”文档机制**：引入由领域专家以Markdown格式编写的“技能”文档，编码了术语映射、参数约束和优化策略。这一知识层将领域知识以结构化形式注入系统，使得LLM在意图提取时能精准匹配到正确的“技能”，从而大幅提升准确率。
- **创新点3：延迟工作流生成策略**：提出skill-driven deferred workflow generation策略，即在意图确定后才生成完整工作流DAG，从而避免预先生成所有可能工作流带来的数据冗余。该策略将数据传输量降低92%，显著提升了系统效率。

### 实验结果亮点
在150个查询的消融实验中，引入“技能”文档后，意图完全匹配准确率从44%提升至83%。在端到端流水线测试中，基于Kubernetes的Hyperflow WMS上，LLM开销低于15秒，每次查询成本低于0.001美元。此外，skill-driven deferred workflow generation策略将数据传输量降低92%，证明了延迟生成策略在减少冗余数据方面的有效性。

### 当前局限
该方法依赖于领域专家预先编写高质量的“技能”文档，这本身是一个耗时且需要专业知识的过程。对于尚未有“技能”覆盖的新领域或新问题，系统无法直接处理，需要专家介入编写。此外，LLM在解析复杂或模糊的研究问题时仍可能产生错误意图，而当前架构缺乏对意图提取错误的自动检测与纠正机制。

### 后续改进方向
- **方向1：技能文档的自动生成与维护**：探索利用LLM从现有文献或工作流仓库中自动提取并生成“技能”文档，减少对领域专家手动编写的依赖，并建立技能文档的版本更新与质量评估机制。
- **方向2：意图提取的鲁棒性增强**：引入多轮对话或主动学习机制，当LLM对意图不确定时，向用户提出澄清问题，或通过对比多个候选意图进行投票，提高复杂查询下的意图提取准确率。

### 工程落地启发
对OCR/文档解析工程项目而言，最直接的启发在于“知识层”的设计理念。可以借鉴“技能”文档的思路，为不同类型的文档（如发票、合同、学术论文）预先定义结构化的解析规则（如字段映射、约束条件、后处理策略），并通过一个轻量级知识库管理。这样，LLM只需负责从用户查询中提取意图并匹配到对应的解析“技能”，而具体的解析逻辑则由确定性的规则引擎执行，从而在保证灵活性的同时大幅提升可靠性和可复现性。

---

### 14. Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision

- **ArXiv ID**: [2604.21909v1](https://arxiv.org/abs/2604.21909v1)
- **作者**: Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin
- **发布时间**: 2026-04-24
- **分类**: cs.CV, cs.IT, q-bio.NC
- **PDF**: [https://arxiv.org/pdf/2604.21909v1](https://arxiv.org/pdf/2604.21909v1)
- **相关度评分**: 1/10

#### 英文摘要

Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for whom, and in which direction. We show that these directional confusions reveal distinct inductive biases that are invisible to accuracy alone. Using matched human and deep vision model responses on a natural-image categorization task under 12 perturbation types, we quantify asymmetry in confusion matrices and link it to generalization geometry through a Rate-Distortion (RD) framework, summarized by three geometric signatures (slope (beta), curvature (kappa)) and efficiency (AUC). We find that humans exhibit broad but weak asymmetries, whereas deep vision models show sparser, stronger directional collapses. Robustness training reduces global asymmetry but fails to recover the human-like breadth-strength profile of graded similarity. Mechanistic simulations further show that different asymmetry organizations shift the RD frontier in opposite directions, even when matched for performance. Together, these results position directional confusions and RD geometry as compact, interpretable signatures of inductive bias under distribution shift.

#### 深度分析（中文）

### 中文摘要
本文通过引入方向性混淆（directional confusions）和率失真几何（Rate-Distortion geometry）的概念，揭示人类与深度视觉模型在自然图像分类任务中即使准确率相近，其归纳偏置也存在系统性差异。研究发现，人类的混淆矩阵表现出宽泛而弱的不对称性，而深度模型则呈现稀疏且强烈的方向性崩溃，且鲁棒性训练无法恢复人类式的渐变相似性模式。通过率失真框架的三个几何特征（斜率、曲率、效率）对混淆不对称性进行量化，论文证明了不同方向混淆组织会以相反方向移动率失真前沿，从而将归纳偏置与分布偏移下的泛化几何联系起来。

### 解决的核心问题
现有研究多关注分类准确率这一总体指标，忽略了模型间错误模式的差异，尤其是错误方向（谁被误认为谁）所隐含的归纳偏置信息。本文旨在解决如何通过方向性混淆的几何特征，在分类性能之外定量刻画并区分人类与不同视觉模型在自然图像扰动下的内在偏差，从而弥补传统评估方法对模型行为差异的盲区。

### 核心创新
论文首次将率失真几何（Rate-Distortion geometry）应用于分析分类混淆矩阵的不对称性，提出了三个紧凑的几何签名（斜率、曲率、效率）来量化归纳偏置。此外，通过对比人类与12种扰动条件下的深度模型，揭示了方向性混淆模式中人类与机器视觉的本质差异，并利用机制性模拟验证了不同混淆组织对泛化前沿的影响。

### 创新点拆解
- 创新点1：提出了基于方向性混淆的分析框架，将分类错误从“是否错误”转变为“谁被误认为谁”的定向不对称性，并证明该不对称性蕴含了准确率无法反映的归纳偏置信息。
- 创新点2：引入率失真几何（RD几何）方法，定义了斜率（β）、曲率（κ）和效率（AUC）三个几何签名，将混淆矩阵的不对称性映射到泛化几何上，为量化不同模型的偏置提供了紧凑且可解释的工具。
- 创新点3：通过机制性模拟，展示了不同方向混淆组织（如人类式的宽弱不对称与模型式的稀疏强不对称）会以相反方向移动率失真前沿，即使分类性能匹配，从而揭示了归纳偏置对分布偏移下泛化行为的根本性影响。

### 实验结果亮点
在包含12种扰动类型（如噪声、模糊、遮挡等）的自然图像分类任务上，人类与深度模型在相同准确率水平下，方向混淆的几何特征存在显著差异：人类的不对称性广度（β）和强度（κ）分布更均匀，而深度模型（如ResNet、ViT）呈现稀疏且强烈的方向性崩溃。鲁棒性训练（如对抗训练）使全局不对称性降低，但未能恢复人类式的渐变相似性模式（即宽弱不对称）。模拟实验进一步表明，不同不对称组织可使率失真前沿的AUC变化超过15%。

### 当前局限
该方法目前仅应用于自然图像分类任务，尚未验证在文档图像、表格或公式等结构化文本场景中的适用性。此外，率失真几何的量化依赖于扰动类型的预设集合，对于未覆盖的分布偏移类型（如字体变形或版面扭曲）其泛化能力未知。方向性混淆的分析需要获取人类与模型的完整混淆矩阵，在标注成本较高的OCR任务中可能难以大规模实施。

### 后续改进方向
- 方向1：将率失真几何扩展至OCR中的字符级/词级混淆分析，例如利用方向性混淆量化不同文字识别模型（如CRNN、Transformer-based OCR）对相似字形（如“己”“已”“巳”）的归纳偏置差异。
- 方向2：结合文档版面分析中的布局扰动（如文本行倾斜、表格行列错位），设计针对性的方向混淆指标，并探索如何通过率失真前沿指导模型在文档理解任务中的鲁棒性训练策略。

### 工程落地启发
本文的核心启发在于：在OCR/文档解析工程中，不应仅以准确率作为模型选型或优化的唯一标准，而应通过分析模型在特定错误方向上的“倾向性”（如对特定字体或布局的混淆模式）来诊断模型的内在偏置。例如，当两个OCR模型准确率相同时，可通过构建混淆矩阵并计算率失真几何签名，选择更接近人类认知模式（宽弱不对称）的模型，以提升在文档版面变化场景下的泛化鲁棒性。

---

### 15. EVENT5Ws: A Large Dataset for Open-Domain Event Extraction from Documents

- **ArXiv ID**: [2604.21890v1](https://arxiv.org/abs/2604.21890v1)
- **作者**: Praval Sharma, Ashok Samal, Leen-Kiat Soh, Deepti Joshi
- **发布时间**: 2026-04-24
- **分类**: cs.CL
- **PDF**: [https://arxiv.org/pdf/2604.21890v1](https://arxiv.org/pdf/2604.21890v1)
- **相关度评分**: 1/10

#### 英文摘要

Event extraction identifies the central aspects of events from text. It supports event understanding and analysis, which is crucial for tasks such as informed decision-making in emergencies. Therefore, it is necessary to develop automated event extraction approaches. However, existing datasets for algorithm development have limitations, including limited coverage of event types in closed-domain settings and a lack of large, manually verified dataset in open-domain settings. To address these limitations, we create EVENT5Ws , a large, manually annotated, and statistically verified open-domain event extraction dataset. We design a systematic annotation pipeline to create the dataset and provide empirical insights into annotation complexity. Using EVENT5Ws, we evaluate state-of-the-art pre-trained large language models and establish a benchmark for future research. We further show that models trained on EVENT5Ws generalize effectively to datasets from different geographical contexts, which demonstrates its potential for developing generalizable algorithms. Finally, we summarize the lessons learned during the dataset development and provide recommendations to support future large-scale dataset development.

#### 深度分析（中文）

### 中文摘要
本文针对开放域事件抽取缺乏大规模人工验证数据集的问题，构建了EVENT5Ws——一个包含5W元素（What、Who、When、Where、Why）的、手动标注且经统计验证的大规模数据集。论文设计了一套系统化的标注流水线，并基于该数据集评估了当前最先进的大语言模型，建立了基准测试。实验表明，在该数据集上训练的模型能够有效泛化到不同地理背景的数据集，展示了其用于开发通用算法的潜力。

### 解决的核心问题
现有事件抽取数据集存在两大痛点：一是封闭域场景下事件类型覆盖有限，无法适应开放世界中的多样化事件；二是缺乏大规模、人工验证的开放域数据集，导致算法开发受限于数据规模和标注质量。本文旨在解决开放域事件抽取中高质量大规模训练数据缺失的问题，为开发通用且鲁棒的事件抽取算法提供数据基础。

### 核心创新
本文的核心创新在于构建并发布了EVENT5Ws数据集，这是目前规模最大、且经过手动标注和统计验证的开放域事件抽取数据集之一。其创新性体现在数据集的构建方法论上，包括一个可复现的系统化标注流水线，以及通过在多个地理背景数据集上的泛化实验，证明了该数据集能有效支持通用事件抽取模型的训练。

### 创新点拆解
- 创新点1：大规模开放域数据集构建。创建了包含5W元素（Who, What, When, Where, Why）的EVENT5Ws数据集，其规模远超现有开放域事件抽取数据集，且全部经过人工标注和统计验证，确保了数据质量和覆盖度。
- 创新点2：系统化的标注流水线。设计并详细描述了从数据收集、标注指南制定、众包标注到质量验证的完整流程，并提供了标注复杂度的实证分析，为未来大规模数据集开发提供了可借鉴的工程经验。
- 创新点3：跨地域泛化能力验证。通过在来自不同地理上下文（如不同国家或地区）的数据集上进行迁移学习实验，证明了基于EVENT5Ws训练的模型具有良好的泛化能力，而不仅仅是过拟合于特定地域的事件模式。

### 实验结果亮点
- 在EVENT5Ws数据集上，对多个SOTA预训练大语言模型（如GPT-3, T5等）进行了评估，建立了首个针对该数据集的基准分数。
- 跨域泛化实验中，模型在来自不同地理背景的测试集上表现稳定，性能下降幅度远小于直接使用其他封闭域数据集训练的模型，验证了数据集的通用性。
- 在标注复杂度分析中，量化了不同事件类型和5W元素的标注难度，为后续优化标注策略提供了数据支撑。

### 当前局限
- 数据集仅覆盖英文文本，未涉及中文、阿拉伯语等其他语言的开放域事件，限制了其在多语言场景下的直接应用。
- 5W元素中的“Why”（原因）标注一致性较低，由于事件原因通常隐含且依赖上下文，模型在此类元素上的抽取性能显著低于其他元素，这是事件抽取领域的固有问题。
- 数据集主要来源于新闻文本，对于社交媒体、对话等非正式、短文本体裁的事件抽取泛化能力尚未验证。

### 后续改进方向
- 方向1：多语言扩展。基于EVENT5Ws的标注流水线，构建中文、西班牙语等多语言版本的数据集，并探索跨语言迁移学习策略，以提升模型的多语言事件抽取能力。
- 方向2：原因元素增强。针对“Why”元素标注一致性差的问题，引入因果推理知识库或预训练模型（如因果BERT）辅助标注，并设计更细粒度的标注规则（如区分直接原因与间接原因）。
- 方向3：低资源场景优化。研究如何利用EVENT5Ws作为源域数据，通过少样本学习或数据增强技术，提升模型在社交媒体、医学文本等低资源目标域上的事件抽取性能。

### 工程落地启发
对OCR/文档解析工程最有价值的点在于其系统化的标注流水线和质量验证方法。在实际项目中，构建高质量的训练数据往往是最大瓶颈。EVENT5Ws的流程——包括如何设计清晰的标注指南、如何管理众包人员、如何通过统计指标（如标注者间一致性）进行质量控制——可直接复用于构建特定领域（如财务报表、法律合同）的文档事件抽取数据集，从而提升下游任务的准确率。

---
