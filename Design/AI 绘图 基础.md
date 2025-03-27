---
title: AI 绘图 基础
date: '2025/3/22 15:23:3'
categories:
  - - Design
abbrlink: acd19762
---
- [基础关键词](#基础关键词)
  - [**1. CFG Scale（Classifier-Free Guidance Scale）**](#1-cfg-scaleclassifier-free-guidance-scale)
  - [**2. Sampling Method（采样方法）**](#2-sampling-method采样方法)
  - [**3. Noise Strength（降噪强度）**](#3-noise-strength降噪强度)
  - [**4. Clip Guidance（CLIP 指导）**](#4-clip-guidanceclip-指导)
  - [**如何调整？**](#如何调整)
- [LyCORIS 和 lora 模型是一种嘛？](#lycoris-和-lora-模型是一种嘛)
  - [**1. LoRA（Low-Rank Adaptation）**](#1-loralow-rank-adaptation)
    - [✅ **特点**](#-特点)
    - [🔧 **工作原理**](#-工作原理)
    - [⚡ **适用场景**](#-适用场景)
  - [**2. LyCORIS（Lora beYond Conventional methods, Rethinking Image Super-resolution）**](#2-lycorislora-beyond-conventional-methods-rethinking-image-super-resolution)
    - [✅ **特点**](#-特点-1)
    - [🔧 **LyCORIS 的主要变种**](#-lycoris-的主要变种)
  - [**3. LoRA vs LyCORIS 总结**](#3-lora-vs-lycoris-总结)
  - [**4. 什么时候用 LoRA？什么时候用 LyCORIS？**](#4-什么时候用-lora什么时候用-lycoris)



## 基础关键词
在 **Stable Diffusion** 及其衍生模型（如 Automatic1111 的 WebUI）中，**Guidance** 主要指的是 **CFG Scale（Classifier-Free Guidance Scale）**，它控制 AI 对 Prompt（提示词）的遵循程度。以下是一些可能的设置项及其影响：

### **1. CFG Scale（Classifier-Free Guidance Scale）**
- **作用**：调整模型对 Prompt 的依赖程度。较低的值会让生成结果更自由、更具创造性，而较高的值则会让 AI 更严格地遵循 Prompt 的描述。
- **推荐设置**：
  - **低值（1-5）**：较自由，可能偏离 Prompt，但更具创意。
  - **中值（7-10）**（**推荐**）：平衡细节与自然度，符合 Prompt 但不过度强化。
  - **高值（12-20+）**：严格遵循 Prompt，但可能导致画面失真或过度强化细节（如光影、锐度等）。

### **2. Sampling Method（采样方法）**
- 与 Guidance 相关的采样器（如 Euler, DPM++ 2M Karras, etc.）会影响 AI 生成图像时的优化方式，较精确的采样方法通常可以减少 **CFG Scale** 过高带来的瑕疵。

### **3. Noise Strength（降噪强度）**
- 在 **img2img** 或 **ControlNet** 里，如果 **CFG Scale** 过高，但 **Noise Strength**（降噪强度）不足，可能导致 Prompt 影响力不足，无法达到预期效果。

### **4. Clip Guidance（CLIP 指导）**
- 某些 Stable Diffusion 版本（如 DeepFloyd IF）可能包含 CLIP Guidance，它用来优化 Prompt 相关性，增强文本到图像的一致性。

### **如何调整？**
- **如果模型生成的图像偏离 Prompt**，可适当 **提高 CFG Scale**（如从 7 调到 10）。
- **如果画面过度锐利、光影失真**，尝试 **降低 CFG Scale**（如从 14 降到 10）。
- **如果画面过度依赖 AI 自发性**（Prompt 影响力弱），可调整 **采样器**（如使用 DPM++ 2M Karras 代替 Euler）。

你是想调整 **CFG Scale** 来优化绘图效果，还是有其他 Stable Diffusion 相关的设定想了解？


## LyCORIS 和 lora 模型是一种嘛？

**LyCORIS** 和 **LoRA** 模型在 **Stable Diffusion** 生态系统中有很多相似之处，但它们并不是完全相同的东西。它们都是用于 **降低训练成本** 并 **优化模型微调** 的技术，主要区别在于 **架构、训练方法和适用场景**。

---

### **1. LoRA（Low-Rank Adaptation）**
#### ✅ **特点**
- **基于线性变换**，通过 **低秩分解**（Low-Rank Decomposition）对 **预训练模型** 进行高效微调。
- **减少显存占用**，可以在 **消费级显卡**（如 8GB-12GB VRAM）上训练 **高质量的个性化模型**。
- 适用于 **人物风格、角色设定、服饰、姿势、艺术风格等**。

#### 🔧 **工作原理**
- 通过 **冻结原始模型的权重**，只在 **LoRA 层** 进行微调，避免大规模调整整个模型，提高训练效率。
- LoRA 层会对 **特定特征** 进行学习，例如 **特定角色的面部特征、服装、艺术风格**，然后在生成时应用这些特征。

#### ⚡ **适用场景**
- **角色定制**（如二次元角色、游戏角色）
- **艺术风格微调**（如特定画家的风格）
- **服装、道具、背景调整**
- **多种LoRA组合使用**（可以叠加多个 LoRA 模型，如同时使用“角色 LoRA”+“服饰 LoRA”）

---

### **2. LyCORIS（Lora beYond Conventional methods, Rethinking Image Super-resolution）**
#### ✅ **特点**
- **LyCORIS 是 LoRA 的扩展**，提供 **更灵活的架构**，能够适应 **更复杂的训练目标**。
- 提供比标准 **LoRA 更强的泛化能力**，可以在 **更深层次** 调整 Stable Diffusion 模型。
- 主要用于 **风格化、复杂结构（如机械、背景、特定艺术风格）**，或者需要更 **动态控制** 的任务。

#### 🔧 **LyCORIS 的主要变种**
LyCORIS 目前有多种不同的扩展版本，每种都有其特定的用途：
1. **LoCon（LoRA with Convolution）**
   - 结合 **卷积层（Convolutional Layers）**，对复杂结构（如背景、机械、纹理）更有效。
   - **适用于背景风格、机械设计、抽象艺术。**
   
2. **LoHa（Low-Rank Adaptation with Hadamard Product）**
   - 采用 **Hadamard 乘法（哈达玛积）**，增强对 **人物细节和艺术风格的学习能力**。
   - **适用于细节丰富的角色或复杂的服饰设计**。

3. **DyLoRA（Dynamic LoRA）**
   - **动态调整 LoRA 训练权重**，提高 LoRA 对多样化风格的适应性。

---

### **3. LoRA vs LyCORIS 总结**
| **特性**      | **LoRA** | **LyCORIS（LoCon / LoHa）** |
|-------------|--------|------------------|
| **显存占用** | 低    | 略高（但比全量模型微调低） |
| **训练速度** | 快    | 略慢（训练更复杂） |
| **适用范围** | 角色、风格、服饰等 | 复杂风格、背景、机械、细节等 |
| **模型复杂度** | 简单 | 复杂，可调整更多参数 |
| **稳定性** | 高 | 可能需要调试，适应性强 |

---

### **4. 什么时候用 LoRA？什么时候用 LyCORIS？**
- **如果你的目标是角色、服饰、画风调整** → **LoRA** 足够。
- **如果你的目标是复杂的场景、背景、机械、抽象艺术** → **LyCORIS（LoCon / LoHa）** 更适合。
- **如果你想要更高自由度的调整，并愿意尝试不同的参数** → LyCORIS 提供更多控制能力。

你目前是想训练自己的 **LoRA / LyCORIS**，还是在选择使用哪种模型？


