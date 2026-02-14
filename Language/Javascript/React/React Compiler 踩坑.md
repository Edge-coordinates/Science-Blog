---
title: React Compiler 踩坑
date: 2026/02/13 10:48:29
categories:
  - - Language
    - Javascript
    - React
abbrlink: a0a5fdef
---
先说问题，再放简介

## 问题

### Few Hooks error

因为 `babel-plugin-react-compiler` 会优化 Hooks，但是只会优化以`use`开头的`useXXX`函数，理论上未使用use开头的函数是会跳过？

然而实际上这可能触发非常严重的问题，会导致完全无法调试的Few Hooks error。

推荐调试的时候先禁用插件，然后确定问题是不是由于`babel-plugin-react-compiler`导致的。

## 简介

> Generate by AI 

`babel-plugin-react-compiler` 本质上是 React Compiler 的 Babel 接入层：它把你的函数组件与自定义 Hook（以及部分相关函数）在“构建期”改写成带有自动缓存与细粒度失效的代码，让你在不大量手写 `useMemo` / `useCallback` / `React.memo` 的前提下，尽量把“更新时真正需要重算/重渲染的部分”压到最小，同时还会基于同一套核心逻辑去验证你是否违反了 React 的基本规则（纯渲染、Hooks 规则等）。这套方向在官方设计目标里写得很直白：希望应用默认就快、启动时间不要倒退、并且尽量“移除概念而不是引入概念”（减少对手动 memo 的依赖）。([GitHub][1])

从产物形态上看，这个 Babel 插件干的事并不神秘：它会在编译后的输出里插入一个“memo cache”数组，并以一个哨兵值 `Symbol.for("react.memo_cache_sentinel")` 来判断缓存是否已填充，然后复用上一次渲染计算出来的 JSX 或中间值。官方安装文档给了一个最小例子：编译后会出现 `import { c as _c } from "react/compiler-runtime";`，随后用 `_c(n)` 初始化缓存槽位并在命中时直接取回。([React][2]) 这也是你判断“插件是否真的在跑”的最硬证据之一（另一个是 DevTools 里出现 “Memo ✨” 标记）。([React][2])

再往里一层，React 团队公开的编译器架构描述解释了“为什么它能做到更细粒度”：Babel 插件先决定哪些函数要编译（取决于选项与局部指令），随后把 Babel AST lowering 成编译器自己的高层中间表示 HIR（保留高层语义、并以控制流图组织），再进入 SSA 形式、跑一系列校验（检测条件式 Hook、无条件 setState 等）、做基础优化（DCE、常量传播）、做保守类型推断，然后推断并构造所谓“reactive scopes”（把会一起创建/变更、以及相关指令聚成组），最后 codegen 回 Babel AST 替换原函数。([GitHub][1]) 这段描述里有两个对使用者非常关键的含义：第一，它强依赖“遵守 React 规则”来保证变换安全；第二，它明确把“完全零冗余重算”列为非目标，因为额外追踪与代码膨胀可能反噬启动性能。([GitHub][1]) 也因此你会看到它不支持类组件、也不会承诺支持 100% JS 语法角落（例如 `eval()` 等）。([GitHub][1])

落到 `babel-plugin-react-compiler` 的实操层面，有三件事决定你能否顺利落地。第一是插件顺序：官方明确要求它必须在 Babel 插件流水线里最先运行，因为它需要尽可能“原始”的源码信息做分析，后置变换会破坏这些信息。([React][2]) 第二是接入方式：React 官方文档直接给了 Babel 与 Vite 的推荐配置（Vite 既可以走 `@vitejs/plugin-react` 的 `babel.plugins`，也可以用 `vite-plugin-babel` 单独挂载）。([React][2]) 第三是版本目标：React 19 默认就能工作；如果你在 React 17/18 上用编译产物，则需要安装 `react-compiler-runtime` 并在配置里设置 `target: '17' | '18'`，否则运行期会缺少相应 runtime。([React][3])

下面给你一个“工程里最常见、也最不容易踩坑”的 Babel 配置骨架，你只需要把它合并进现有配置即可（注意它要放在插件数组最前）：

```js
// babel.config.js
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      // 生产建议：遇到问题的组件跳过优化，不要直接炸构建
      panicThreshold: 'none',
      // React 19 默认即可；React 17/18 需要显式 target + 安装 react-compiler-runtime
      // target: '18',
    }],
    // ...other plugins
  ],
};
```

这里出现的 `panicThreshold` 来自官方配置参考，它决定“编译遇到错误时是失败构建还是跳过问题组件”；文档里把 `panicThreshold: 'none'` 标为推荐的生产配置（跳过出问题的组件，继续优化其他部分）。([React][3]) 同一份配置参考还给了调试与灰度手段：你可以用 `logger.logEvent(filename, event)` 捕获编译成功/失败等事件，用于定位到底哪些文件被编译、哪里被跳过。([React][3]) 如果你需要做 A/B 或渐进灰度，`gating` 允许你指定一个 feature-flag 模块与导出函数名，让编译产物在运行期根据开关选择是否走优化路径。([React][4])

另一个经常被忽略、但会直接影响“为什么我感觉没生效”的开关，是 `compilationMode`。默认是 `'infer'`：编译器靠启发式识别组件与 Hook（比如 PascalCase 组件名、`use` 前缀 Hook、并且确实创建 JSX 或调用 Hook），你不需要写任何额外标注；如果你想极其稳妥地逐步接入，可以改为 `'annotation'`，此时只有显式写了 `"use memo"` 指令的函数才会被编译；而 `"use no memo"` 则永远是强制跳过。([React][5]) 这套机制的价值在于：当你接入初期遇到少数库/组件不兼容或行为异常时，你可以先用 `"use no memo"` 把它们隔离出来，让整体构建与大部分页面继续享受优化，然后再用 lint/日志去逐个消化。官方安装页把这点写得非常明确：`"use no memo"` 是临时逃生舱。([React][2])

关于“手写 memo 还要不要存在”，官方立场其实很一致：目标是让绝大多数场景下你不需要再为了性能去写 `useMemo/useCallback/React.memo`，但它并不追求把所有重算都消到零，也不会为了极限最优引入高额追踪成本或显著膨胀代码体积。([GitHub][1]) 这意味着你的工程实践会变成“默认不写，只有在行为语义需要（比如你就是要一个稳定引用参与外部系统协议）或某些特殊性能剖析结论明确时再写”，而不是过去那种“先写一堆 memo 再说”。

最后说一下配套的“保证你不会盲用”的部分：官方推荐同时启用 ESLint 的相关规则，用来提示哪些组件/Hook 因为违反 Rules of React 而无法被优化。更重要的是，文档强调这是安全的：当 ESLint 报错时，编译器会跳过该组件/Hook 的优化，但不会影响其它代码的优化，你可以按自己的节奏逐步修。([React][2]) 接入完成后，最直接的验收方法就是打开 React DevTools，看看组件名旁边是否出现 “Memo ✨” 标记；或者直接在构建输出里搜 `react/compiler-runtime` 与 `react.memo_cache_sentinel`。([React][2])

如果你愿意把你当前的构建栈（Vite/Next/Rspack 等）、React 版本（17/18/19）、以及是否存在“必须保留稳定引用语义”的场景（例如订阅系统、第三方表单库、可视化库）贴出来，我可以按你的工程形态给一份更贴合的推荐配置（`compilationMode/target/panicThreshold/logger/gating` 该怎么组合、以及最小化风险的渐进接入路径）。

[1]: https://raw.githubusercontent.com/facebook/react/main/compiler/docs/DESIGN_GOALS.md "raw.githubusercontent.com"
[2]: https://react.dev/learn/react-compiler/installation "Installation – React"
[3]: https://react.dev/reference/react-compiler/configuration "Configuration – React"
[4]: https://react.dev/reference/react-compiler/gating "gating – React"
[5]: https://react.dev/reference/react-compiler/compilationMode "compilationMode – React"
