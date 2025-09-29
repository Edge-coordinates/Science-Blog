---
title: Multi-Repo下通过Link快捷进行本地开发
date: 2025/09/11 03:00:34
updated: 2025/09/11 03:06:43
categories:
  - - Language
    - Javascript
    - Environment
abbrlink: 42ee0a77
---
- [Multi-Repo下通过Link快捷进行本地开发](#multi-repo下通过link快捷进行本地开发)
  - [Multi-Repo 架构的核心理念](#multi-repo-架构的核心理念)
  - [创建合约仓库](#创建合约仓库)
    - [项目结构](#项目结构)
    - [package.json 核心配置](#packagejson-核心配置)
    - [工作流程](#工作流程)
  - [在微服务中消费合约包](#在微服务中消费合约包)
  - [解决本地开发问题](#解决本地开发问题)
    - [本地开发流程](#本地开发流程)
  - [开发完成后的收尾工作](#开发完成后的收尾工作)
  - [使用私有 NPM 仓库](#使用私有-npm-仓库)
  - [总结](#总结)

# Multi-Repo下通过Link快捷进行本地开发

在 Multi-Repo 架构下优雅实现 oRPC 微服务 —— 合约包与本地开发的双重策略

在团队规模扩大、技术栈多元化、强调自治的场景下，**Monorepo 往往并不是最佳选择**。独立仓库（Multi-Repo）架构更能满足服务自治和解耦的需求。但一个现实问题是：
如何在 Multi-Repo 的模式下，依然优雅地实现 **oRPC 微服务架构**，并兼顾本地开发的顺畅体验？

答案是：**通过私有 NPM 包管理合约 + 本地链接 (link) 开发**。

---

## Multi-Repo 架构的核心理念

与 Monorepo 强调“统一工作区”不同，Multi-Repo 在共用contract上面临复杂的问题，clone仓库到文件夹里面并不是一个合适的做法。

但是我们不可能每次都将修改的合约发布新版本然后再进行dev，我们需要类似Workspace的功能。

核心策略就是**本地开发链接** —— 使用 `pnpm link` 在本地跨仓库开发时模拟 Monorepo 的实时体验。

---


## 创建合约仓库

创建一个独立的仓库，专门维护 API 合约。假设命名为 `contracts-repo`，它只负责发布 `@my-app/contracts` 包。

### 项目结构

```
/contracts-repo
├── src/
│   ├── user.contract.ts
│   ├── product.contract.ts
│   └── index.ts
├── package.json
└── tsconfig.json
```

### package.json 核心配置

```json
{
  "name": "@my-app/contracts",
  "version": "1.0.0",
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "files": ["dist"],
  "scripts": {
    "build": "tsc",
    "release": "pnpm build && pnpm publish"
  },
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  },
  "devDependencies": {
    "typescript": "latest"
  }
}
```

### 工作流程

1. 修改合约时更新版本号（遵循 [语义化版本](https://semver.org/lang/zh-CN/)）。
2. 运行 `pnpm run release` 将合约包发布到私有 NPM 仓库。

---

## 在微服务中消费合约包

任何一个微服务仓库（例如 `user-service-repo`），只需像使用普通 npm 包一样依赖：

```json
{
  "name": "user-service",
  "dependencies": {
    "@my-app/contracts": "1.0.0"
  }
}
```

这样，服务就能共享一套合约定义，避免因接口变更而出现隐性错误。

---

## 解决本地开发问题

这是关键：如果开发者同时修改 `contracts` 与 `user-service`，难道要频繁发布 `1.0.1-alpha` 版本测试？
**完全没必要。**

答案是：使用 `pnpm link` 本地链接。

### 本地开发流程

1. 克隆两个仓库到本地：

   ```
   /development
   ├── contracts-repo/
   └── user-service-repo/
   ```

2. 在合约仓库中注册全局链接：

   ```bash
   cd contracts-repo
   pnpm link --global
   ```

3. 在微服务仓库中使用本地链接：

   ```bash
   cd user-service-repo
   pnpm link --global @my-app/contracts
   ```

完成！
现在，`user-service` 使用的就是本地 `contracts` 的实时版本。IDE 的类型提示和构建流程都会即时更新，几乎等同于 Monorepo 体验。

---


## 开发完成后的收尾工作

1. **解除本地链接**，恢复到使用发布版本：

   ```bash
   cd user-service-repo
   pnpm unlink --global @my-app/contracts
   pnpm install
   ```
2. 在 `contracts-repo` 中更新版本号并发布新版本。
3. 在 `user-service-repo` 中升级依赖版本。

这样既保证了开发体验，又保证了生产环境的可控性。

## 使用私有 NPM 仓库

1. **私有 NPM 包** —— 发布合约包，统一所有服务的 API 标准。

常见选择：

* **云端方案（推荐）**：GitHub Packages、GitLab Package Registry
* **自托管**：[Verdaccio](https://verdaccio.org/) —— 一个轻量级私有 npm 服务器

---

## 总结

Multi-Repo 下优雅实现 oRPC 微服务的核心是：

- **中心化合约** —— 独立仓库管理 API 合约，发布为私有包。
- **私有分发** —— 通过 GitHub Packages / Verdaccio 等托管合约。
- **版本化依赖** —— 服务通过 `package.json` 明确依赖合约版本。
- **本地化开发** —— 使用 `pnpm link` 在本地模拟 Monorepo 体验。