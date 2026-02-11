---
title: 包管理-Link本地包
date: 2026/02/11 23:57:22
categories:
  - - Language
    - Javascript
    - Nodejs
abbrlink: 51a8dfc1
---
# Bun 环境下本地 Link 一个 TypeScript CLI 包的完整流程

在开发一个基于 TypeScript 的 CLI 工具时，最常见的需求之一，就是在发布到 npm 之前，先在本地项目中进行联调测试。本文以一个典型的 ESM CLI 包结构为例，系统说明如何在 Bun 环境下进行本地 link，以及不同包管理器之间的差异。

假设当前 CLI 包结构包含如下关键字段：

* `bin` 指向 `./dist/index.js`
* `main` / `module` / `types` 已配置
* 使用 `tsup` 构建
* `"type": "module"`
* `"preferGlobal": true`

这种结构已经是标准的 CLI 包结构，接下来只需要解决本地联调问题。

---

## 第一步：必须先构建

CLI 的 `bin` 指向的是 `./dist/index.js`，因此在 link 之前必须确保构建完成，否则即使成功 link，命令也不会存在。

在 CLI 包目录中执行：

```bash
bun run build
```

确认 `dist` 目录已经生成，并且包含 `index.js`。

---

## 第二步：使用 Bun 进行本地 Link

### 方式一：全局 link（模拟全局安装）

在 CLI 包目录执行：

```bash
bun link
```

这一步会将当前包注册到 Bun 的全局 link registry 中。

然后在需要使用该 CLI 的目标项目目录中执行：

```bash
bun link autofm
```

此时，目标项目的 `node_modules/autofm` 会被 symlink 到本地源码目录。

验证是否成功：

```bash
which autofm
# 或
autofm --help
```

如果 `bin` 配置正确，将会直接执行 `dist/index.js`。

需要注意的是，`"preferGlobal": true` 只是提示字段，不影响 Bun 的 link 行为。

---

### 方式二：仅测试全局 CLI

如果只是希望模拟“全局安装 CLI”效果，可以：

```bash
bun link
```

然后直接在终端执行：

```bash
autofm
```

Bun 会从全局 link registry 中找到该命令。

---

## npm 与 pnpm 的对应方式

如果使用 npm：

在 CLI 包目录：

```bash
npm link
```

在目标项目目录：

```bash
npm link autofm
```

如果使用 pnpm：

```bash
pnpm link --global
```

然后：

```bash
pnpm link autofm
```

---

## 更推荐的方式：file 协议（适合 monorepo）

对于多包工程或复杂 workspace 结构，直接使用 `file:` 协议通常更稳健。

在目标项目的 `package.json` 中：

```json
{
  "dependencies": {
    "autofm": "file:../auto-front-matter"
  }
}
```

然后执行：

```bash
bun install
```

这种方式同样会生成软链接，但不会污染全局 link registry，更适合多项目并行开发。

在大型工程或 monorepo 架构中，推荐优先使用 `file:` 或 workspace，而不是 `bun link`。

---

## 常见踩坑点：Shebang 丢失

如果 CLI 执行时报：

```
permission denied
```

或者系统无法识别命令，请检查 `dist/index.js` 文件顶部是否包含：

```js
#!/usr/bin/env node
```

并确认 `tsup` 构建时没有移除 shebang。

否则即使 `bin` 正确配置，CLI 也无法作为可执行文件运行。

---

## 总结

在 Bun 环境下本地联调 CLI 包的核心步骤：

1. 先构建
2. bun link 注册
3. 在目标项目 bun link 包名

在多项目或长期维护场景中，更推荐使用 `file:` 或 workspace 方式，以避免全局 link 带来的潜在污染。

一个标准、稳定的 CLI 工程，本地联调流程应该是确定性的。只要 `bin`、构建输出与 shebang 正确，link 过程本身不会成为问题。
