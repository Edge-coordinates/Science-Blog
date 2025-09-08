---
title: iconLib
date: 2025/4/2 21:30:30
categories:
  - - Framework-Web
    - resource
abbrlink: a3ba6f2e
---
- [ICON Lib](#icon-lib)
  - [静态·未分类](#静态未分类)
    - [🥇 1. **Phosphor Icons**](#-1-phosphor-icons)
    - [🥈 2. **Material Symbols / Material Icons**](#-2-material-symbols--material-icons)
    - [🥉 3. **Iconoir**](#-3-iconoir)
    - [🧢 4. **Lucide**](#-4-lucide)
    - [🎯 5. **Tabler Icons**](#-5-tabler-icons)
    - [总结比较表：](#总结比较表)
  - [内置动画的图标库](#内置动画的图标库)
    - [**boxicons**](#boxicons)
    - [**Lordicon**](#lordicon)
    - [**Remix Icon + CSS 动画**](#remix-icon--css-动画)
    - [**Phosphor Icons**](#phosphor-icons)
    - [4. **IconScout Animated Icons**](#4-iconscout-animated-icons)
  - [设计图标库](#设计图标库)
  - [🧩 补充：如何给普通图标加动画？](#-补充如何给普通图标加动画)
  - [🎯 总结推荐：](#-总结推荐)
- [FontAwesome Pro 使用许可](#fontawesome-pro-使用许可)
      - [You:](#you)
      - [ChatGPT:](#chatgpt)
    - [✅ 你购买一份 Font Awesome Pro 许可后可以：](#-你购买一份-font-awesome-pro-许可后可以)
    - [🚫 不可以的情况：](#-不可以的情况)
    - [🧩 举个例子：](#-举个例子)
      - [例 1：](#例-1)
      - [例 2：](#例-2)
    - [📝 总结一句话：](#-总结一句话)


# ICON Lib

## 静态·未分类

如果你在找一个**可以完全免费商用**、并且**功能上能替代 Font Awesome Pro** 的图标库，下面这些都是优秀的选择：

---

### 🥇 1. **[Phosphor Icons](https://phosphoricons.com/)**

- **风格多样**（填充、线性、粗体、细线等统一设计风格）
- **开源协议**：MIT
- **免费商用**：✅
- **格式支持**：SVG、React/Vue/Svelte 等组件形式
- **优点**：
  - 多种风格统一化，适合现代 UI
  - 安装包干净，体积小
  - 很多图标与 Font Awesome 对应得上

---

### 🥈 2. **[Material Symbols / Material Icons](https://fonts.google.com/icons)**

- **Google 出品**，持续维护
- **开源协议**：Apache 2.0
- **免费商用**：✅
- **支持三种样式**：Outlined、Rounded、Sharp（也支持填充）
- **优点**：
  - 稳定可靠，现代感强
  - 很多系统 UI 都在用
  - 官方提供 Webfont、SVG、Iconfont、NPM 包

---

### 🥉 3. **[Iconoir](https://iconoir.com/)**

- **风格：极简、线性**
- **开源协议**：MIT
- **免费商用**：✅
- **图标数量**：超过 1500 个
- **适合场景**：极简设计、Web 和 App 都适用

---

### 🧢 4. **[Lucide](https://lucide.dev/)**

- **Fork 自 Feather Icons**，但更活跃
- **开源协议**：ISC
- **免费商用**：✅
- **风格**：现代、线性，开发者友好
- **优点**：
  - 提供各种前端框架组件（Vue、React、Svelte 等）
  - 项目结构清晰

---

### 🎯 5. **[Tabler Icons](https://tabler.io/icons)**

- **开源协议**：MIT
- **风格**：线性 + 现代
- **免费商用**：✅
- **图标数量**：超 4000
- **特点**：
  - 统一视觉风格
  - 支持自定义 stroke 宽度

---

### 总结比较表：

| 图标库            | 免费商用 | 协议         | 风格        | 图标数量  | 支持框架组件       |
| -------------- | ---- | ---------- | --------- | ----- | ------------ |
| Phosphor       | ✅    | MIT        | 多风格（填充等）  | 多     | ✅ React/Vue等 |
| Material Icons | ✅    | Apache 2.0 | Google 风格 | 超多    | ✅ 官方支持       |
| Iconoir        | ✅    | MIT        | 极简线性      | 1500+ | ✅            |
| Lucide         | ✅    | ISC        | 现代线性      | 1000+ | ✅            |
| Tabler         | ✅    | MIT        | 清爽线性      | 4000+ | ✅            |

---

如果是为了图标风格+数量多而考虑 Font Awesome Pro，上面这些组合起来基本都能覆盖需求，而且完全免费商用 💡


## 内置动画的图标库

Font Awesome Pro 的一个亮点确实是它内置了各种动画（比如 `fa-spin`、`fa-bounce`、`fa-flip` 等），如果你也希望图标库自带类似的动画功能，那下面这些图标库就特别适合你👇

### **[boxicons](https://boxicons.com/)**

之前用过~

### **[Lordicon](https://lordicon.com/)**

- **特色**：🧠 动画 SVG 图标，全部是动图！
- **动画风格**：滑入、跳动、点击响应、悬停、循环等超多种
- **交互方式**：通过 `hover`、`click`、`loop` 控制
- **免费商用**：✅ 有免费图标，商用许可清晰（需要注意部分为付费）
- **开发友好**：支持 Web Component、Lottie、JSON、React/Vue
- **缺点**：不是全部图标免费

✅ *非常适合酷炫交互或仪表盘界面*

---

### **[Remix Icon + CSS 动画](https://remixicon.com/)**

- **图标风格**：线性 + 现代，和 Font Awesome 接近
- **开源协议**：Apache 2.0，免费商用 ✅
- **内置动画**：Remix 本身没有内置动画，但搭配 CSS 动画框架（比如 Animate.css 或 Tailwind 动画类）非常顺滑
- **优点**：图标命名直观，可配合简单类名实现 `spin`、`pulse` 等效果

🧩 *推荐搭配使用：Tailwind CSS 的 `animate-spin`、`animate-bounce` 等类名*

---

### **[Phosphor Icons](https://phosphoricons.com/)**

- **图标丰富、风格多样**
- **官方提供**了一些动画示例（虽不是内建类名，但支持用 SVG 动画或组件动画）
- **适合前端框架使用**：React/Vue 可以直接加 transition/animate 属性
- **风格统一，可自定义权重**

✅ *搭配前端框架使用动画非常方便，尤其适合 React/Vue 项目*

---

### 4. **[IconScout Animated Icons](https://iconscout.com/lottie/animated-icons)**

- **形式**：Lottie JSON 动画图标（AE 制作）
- **可自定义颜色和大小**
- **支持平台多**：Web, React Native, Flutter
- **商业使用**：✅ 免费 + 付费混合模式（注意许可）

⚡ *适合需要动图又希望跨平台统一体验的开发者*

---

## 设计图标库

- https://www.flaticon.com/
- 


## 🧩 补充：如何给普通图标加动画？

如果你喜欢的图标库不带动画，可以用这些方式轻松补上：

- 使用 CSS 动画库，如：
  - [Animate.css](https://animate.style/)
  - Tailwind CSS 的 `animate-*` 类
  - 自定义 `@keyframes`
- 使用 [Lottie + LottieFiles](https://lottiefiles.com/)：配合 Lottie Web 播放器，给页面加可控动图

---

## 🎯 总结推荐：

| 图标库              | 动画支持     | 推荐场景              | 免费商用   |
| ---------------- | -------- | ----------------- | ------ |
| **Lordicon**     | ✅ 内建动画   | 高互动 UI、炫酷界面       | 部分免费   |
| **Phosphor**     | ✅ 易加动画   | 通用型项目             | ✅      |
| **Remix + CSS**  | ✅ 搭配动画类名 | 后台、网页             | ✅      |
| **Lottie Icons** | ✅ 复杂动效   | 移动端、Flutter、React | ✅/付费混合 |

---

如果你想要那种**类似 `fa-spin`, `fa-bounce`, `fa-beat` 的简单用法**，我可以帮你写一个“可复用的动画类系统”，你就可以把任何图标库套进去用啦～要不要我顺手整一个？



# FontAwesome Pro 使用许可

#### You:
fontawesome pro 在商业项目的使用到底是怎样的？我购买一份许可，可以将它下载使用在所有项目上嘛？

#### ChatGPT:
Font Awesome Pro 的商业许可使用规则比较清楚，但确实容易产生一些疑问。下面是他们官方许可（[Font Awesome Pro License](https://fontawesome.com/license/pro)）的核心内容，并结合你的问题来解释：

---

### ✅ 你购买一份 Font Awesome Pro 许可后可以：

1. **在你拥有或控制的多个项目中使用**：
   - 只要你是这个项目的**开发者、拥有者或是该产品的发布者**，就可以使用 Font Awesome Pro。
   - 可以是多个网站、应用、客户端项目等等，**不限数量**。

2. **在客户端打包分发**（如网页、桌面或移动应用）：
   - 你可以把图标字体、SVG 等文件随你的项目一起打包、分发给用户使用。

3. **在你的公司或组织内部共享**：
   - 一个许可可以覆盖多个开发者（取决于你购买的 seats 数量）。每个开发者都需要拥有合法 seat 才能使用 Font Awesome Pro。

---

### 🚫 不可以的情况：

1. **不能将 Font Awesome Pro 文件独立分发**或公开提供下载：
   - 比如你不能把图标库上传到 GitHub 或 CDN 上供其他人使用。
   - 你也不能作为「工具包的一部分」嵌入让别人提取和重用 Pro 图标资源。

2. **不能用于客户项目，除非客户也有许可**（视情况而定）：
   - 如果你为客户开发项目，而且你会持续维护并控制该项目，**可以使用你的 Pro 许可**。
   - 如果你开发完后把整个项目交给客户，客户继续维护且你不再参与，**客户也需要拥有自己的 Pro 许可**。

---

### 🧩 举个例子：

#### 例 1：

你是独立开发者，购买了一份 Font Awesome Pro 许可。

- ✅ 你可以用它做公司官网、博客系统、三个手机 App、一款桌面软件，没问题。
- ✅ 你可以在打包后让最终用户下载使用（只要他们不能提取图标重新使用就可以）。
- ❌ 如果你做了个 UI 框架，把图标整合进去放到 GitHub 开源——不行，除非用免费版或授权过的文件。

#### 例 2：

你是外包公司，客户 A 让你做一个后台管理系统。

- 如果你会持续维护这个项目，Pro 许可可以用在这个项目里；
- 如果你做完交给客户且你不再管这个项目，那么客户应该自己也买一份许可。

---

### 📝 总结一句话：

> 一份 Font Awesome Pro 许可可以让你在多个自己控制的项目中使用，但不能把图标资源单独分发，也不能用在你不再维护、控制的客户项目中。

---

如果你有特定的使用场景（比如做 SaaS 平台、插件、模板等），可以告诉我，我可以帮你分析是否符合许可。