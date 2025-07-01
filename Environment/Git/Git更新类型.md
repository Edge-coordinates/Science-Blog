---
title: Git更新类型
date: 2025/7/1 21:25:28
categories:
  - Environment
  - Git
---
不是，**不仅仅只有 `feature`（或 `feat`）、`refactor`、`chore` 这三类**。
在语义化 Git 提交流程中（尤其是 [Conventional Commits](https://www.conventionalcommits.org/) 或用于自动化版本管理 like `semantic-release`），**常用的类型有 8\~10 种以上**。

---

## 📘 常见 Git Commit 类型大全（含含义和示例）

| 类型         | 说明                                        | 是否触发版本升级      |
| ---------- | ----------------------------------------- | ------------- |
| `feat`     | 新增功能（feature）                             | ✅ minor       |
| `fix`      | 修复 bug                                    | ✅ patch       |
| `refactor` | 代码重构，不新增功能、不修 bug                         | ❌ 否           |
| `chore`    | 日常杂项任务，如依赖更新、构建脚本、CI 配置等                  | ❌ 否           |
| `docs`     | 文档更新，如 README、注释、更正拼写                     | ❌ 否           |
| `style`    | 代码格式修改（不影响功能）如空格、缩进、分号                    | ❌ 否           |
| `test`     | 添加或修改测试相关代码                               | ❌ 否           |
| `perf`     | 性能优化，如缓存处理、提升响应速度                         | ✅ patch       |
| `build`    | 构建系统或依赖更新，如 webpack、rollup 的修改            | ❌ 否           |
| `ci`       | 持续集成配置更改，如 GitHub Actions、Travis、Husky 配置 | ❌ 否           |
| `revert`   | 回滚之前的提交                                   | ✅ patch/minor |

---

## 🔧 衍生 / 可选的类型（有团队自定义）

一些团队会扩展出自己的类型：

* `wip`: Work in Progress，开发中未完成的提交（建议避免合入主分支）
* `merge`: 专用于分支合并记录（Git 自动生成）
* `hotfix`: 临时生产环境修复（有些团队区分 `fix` 和 `hotfix`）
* `release`: 发布版本标记（可配合 changelog 工具）
* `temp`: 临时性测试或调试（建议 squash 掉）

---

## ✨ 示例对比

```bash
feat: add dark mode toggle for user settings
fix: correct markdown rendering for bold text
refactor: extract reply logic into separate Zustand-managed drawer
chore: upgrade eslint and add react-hooks plugin
docs: update contribution guide with new lint rules
style: fix indentation and remove unused imports
test: add unit tests for EasyEditor component
perf: improve comment loading with lazy render
```

---

## ✅ 推荐实践

1. **保持每个 commit 只做一件事，清晰分类型**
2. 使用 `type(scope): description` 形式更规范，例如：

   ```bash
   feat(reply): support threaded comment replies using Zustand
   ```

---

好的，下面是 `feature`、`refactor`、`chore` 三个最常见的 Git commit 类型总结，包括**语义含义、适用场景、是否影响版本号（如使用 semantic-release）**，并附上实际例子，方便你判断和使用。

---

## ✅ 1. `feat` / `feature`: **新增功能**

* **含义**：引入了用户可见的新功能或外部接口行为变更
* **用途**：

  * 添加新组件、页面、新按钮功能
  * 提供新 API、新配置项
* **语义化版本控制**：会触发 `minor` 版本号升级（`1.2.3` → `1.3.0`）

### 示例：

```bash
feat: add ReplyDrawer component for threaded comment replies
```

---

## ✅ 2. `refactor`: **重构代码（非行为变更）**

* **含义**：重写或优化已有代码结构，但**功能未变**
* **用途**：

  * 优化结构、改名、抽离组件、整理逻辑
  * 从 class 转 hook，或替换底层状态管理
* **语义化版本控制**：**不**影响版本号（除非影响外部功能）

### 示例：

```bash
refactor: restructure reply flow using Zustand and modular components
```

---

## ✅ 3. `chore`: **项目构建、配置类更新**

* **含义**：对开发工具、依赖、CI/CD 配置等的改动，**不影响业务代码**
* **用途**：

  * 更新依赖版本（`pnpm-lock.yaml`、`package.json`）
  * 修改 `.eslintrc`, `.gitignore`, `tsconfig.json` 等
  * 配置 GitHub Actions / Husky / Lint-Staged
* **语义化版本控制**：不触发任何版本变化

### 示例：

```bash
chore: update ESLint config and add eslint-plugin-react-hooks
```

---

## ✅ 小结对比表：

| 类型         | 是否改功能？ | 是否用户可见？ | 示例改动                | 影响版本？    |
| ---------- | ------ | ------- | ------------------- | -------- |
| `feat`     | ✅ 是    | ✅ 是     | 新增组件、新按钮、新路由        | ⬆️ Minor |
| `refactor` | ✅ 是    | ❌ 否     | 重构组件结构、优化代码、改状态管理逻辑 | ❌ 否      |
| `chore`    | ❌ 否    | ❌ 否     | 改配置、更新依赖、改CI脚本      | ❌ 否      |

---

如果你一个 commit 同时包含了三类变更，一般推荐：

1. 拆分为多个 commit；
2. 或使用主语义（如以 `refactor:` 为主），其他内容放在 description 里。

---

需要我帮你将当前项目变更拆分成三个 commit message 吗？

