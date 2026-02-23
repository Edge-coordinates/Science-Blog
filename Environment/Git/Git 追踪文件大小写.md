---
title: Git 追踪文件大小写
date: 2026/02/14 19:39:24
categories:
  - - Environment
    - Git
abbrlink: 7491252b
---
# Git 追踪目录大小写问题小记

有，而且这是一个**典型 Windows + Git + 大小写重命名**的工程问题。你这个 monorepo 规模下，确实值得用“工程级解法”一次性清干净。

我给你按**安全程度从低风险到高风险**分层讲清楚。

---

# ✅ 方案一（推荐）：强制 Git 重新识别当前大小写状态

这个是最干净、最可控的方法。

---

## 第一步：关闭 ignorecase

Windows 默认：

```bash
git config core.ignorecase
# 大概率是 true
```

改为：

```bash
git config core.ignorecase false
```

这一步非常关键。

---

## 第二步：强制 Git 重新扫描 index

让 Git 重新对比磁盘文件和 index：

```bash
git rm -r --cached .
git add .
```

然后：

```bash
git status
```

如果大小写有差异，你会看到 rename 或 delete/add。

最后：

```bash
git commit -m "chore: normalize file casing"
```

---

### 为什么这招有效？

因为：

* `--cached` 只清 index，不删物理文件
* 再 `git add .` 会根据当前磁盘真实大小写重新建 index
* Git 被强制重新建立大小写映射

这是最安全方案。

---

# ✅ 方案二：强制大小写重命名（更精确）

如果你只想修一个目录，比如：

```plaintext
component/navigation
```

想统一成：

```plaintext
component/Navigation
```

做法：

```bash
git mv component/navigation component/__tmp__
git mv component/__tmp__ component/Navigation
git commit -m "fix: normalize Navigation directory casing"
```

---

# ✅ 方案三：暴力重建 index（偏工程化）

如果你怀疑整个仓库 casing 混乱，可以：

```bash
rm -f .git/index
git reset
```

或者：

```bash
git read-tree --reset -u HEAD
```

这个会完全重建 index。

⚠️ 只建议在工作区 clean 时使用。

---

# 🚨 千万不要做的事

不要：

```bash
删除文件 → 手动重建
```

不要：

```bash
直接 rename 文件夹大小写（Windows 会忽略）
```

因为 NTFS 默认大小写不敏感，直接改大小写 Git 不一定感知。

---

# 🧠 为什么会发生？

你的项目：

```plaintext
Library.Book/package/app/src/component
```

如果你：

* 曾在 Linux/WSL 操作
* 或从 Mac clone
* 或 IDE 自动修正大小写
* 或做过 `git mv` 但 ignorecase=true

都会导致：

Git index 认为：

```plaintext
Navigation
```

但磁盘是：

```plaintext
navigation
```

TypeScript 再结合 path alias 就会触发 TS1149。

---

# 🛡 工程级预防方案（强烈建议）

### 1️⃣ tsconfig 打开

```json
"forceConsistentCasingInFileNames": true
```

---

### 2️⃣ 团队 Git 强制大小写敏感

在仓库级别执行：

```bash
git config core.ignorecase false
```

甚至可以写进：

```bash
.git/config
```

---

### 3️⃣ ESLint 规则

```js
import/no-unresolved
```

并开启 caseSensitive 选项。

---

# 🎯 给你最稳的一套操作顺序

如果我是你，现在这样做：

```bash
git config core.ignorecase false
git rm -r --cached .
git add .
git commit -m "chore: rebuild git index to normalize casing"
```

然后：

* 重启 TS server
* 重启 IDE
* 再跑一遍 typecheck

基本 99% 解决。

---

# 💬 说一句实话

你这个 monorepo 规模（Library.Book）已经到了：

> “路径规范必须制度化”的阶段。

否则以后 CI 上 Linux 一跑，直接炸。

---

如果你愿意，我可以给你：

* 一套跨平台命名规范
* 一套 React + TS + Bun monorepo 的 casing 规范模板
* 一套 pre-commit 自动检测大小写冲突脚本

这类问题属于工程成熟度问题，而不是单纯 bug。

你现在踩到的是正常进阶门槛。



## 为什么 Git 默认不追踪大小写变更？

* Git 默认大小写敏感，但会根据文件系统类型决定是否追踪大小写变化。
* **Linux**：默认大小写敏感（EXT4）。
* **macOS/Windows**：默认大小写不敏感（HFS+ / NTFS）。

## 如何让 Git 追踪大小写变化？

* 执行以下命令强制 Git 不忽略大小写：

  ```bash
  git config core.ignorecase false
  ```

## 如何解决已有的大小写更改未被识别？

* 使用中间临时名来实现大小写变更：

  1. 重命名为临时名：

     ```bash
     git mv foo temp_name
     ```
  2. 重命名为目标名：

     ```bash
     git mv temp_name Foo
     ```
  3. 提交更改：

     ```bash
     git commit -m "fix: rename foo → Foo (大小写更正)"
     ```

## 总结

* **跨系统协作时：**
  * 确保所有开发者统一 Git 设置：`git config core.ignorecase false`
  * 规范文件命名，避免随意更改大小写（例如，统一小写或使用下划线）。、
  
* **检查当前设置：**
  * 使用 `git config core.ignorecase` 查看当前的配置，确保其为 `false`。