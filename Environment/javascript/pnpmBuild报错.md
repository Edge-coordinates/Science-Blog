---
title: pnpmBuild报错
date: 2025/7/1 21:25:28
categories:
  - - Environment
    - javascript
abbrlink: 77ca20c5
---
你遇到的报错：

```
 ERR_PNPM_MISSING_HOISTED_LOCATIONS  msw@2.8.7(@types/node@22.15.29)(typescript@5.8.3) is not found in hoistedLocations inside node_modules/.modules.yaml
```

这是一种 **pnpm 特有的依赖结构错误**，我们来逐步解释：

---

## 🧠 一句话解释

你在构建 `msw@2.8.7` 包时，pnpm 试图根据 `.modules.yaml` 的记录来定位依赖（比如 `@types/node` 和 `typescript`），但它 **在 node\_modules 的 hoisted 记录中找不到这些依赖的位置**。

这通常是由以下几种情况引起：

---

## 📋 可能原因

### 1. 旧版 pnpm 安装生成的 `node_modules`

> 错误提示已经说明了：

> 💬 *“If you installed your node\_modules with pnpm older than v7.19.0...”*

pnpm 的 hoisting 机制在 7.19.0 之后有较大变化，如果你之前用了旧版本（比如 6.x 或 7.0.x）安装过依赖，生成的 `.modules.yaml` 是旧格式，会导致新版本无法解析。

---

### 2. 锁文件损坏或不一致（常见于多包 monorepo、pnpm workspaces）

如果你使用了 workspace（例如 monorepo 结构），某些包之间的依赖可能未被正确 hoist，`.modules.yaml` 中的信息和实际 `node_modules` 状态不一致，也会导致构建错误。

---

## 🛠️ 如何修复

### ✅ 方法一：最推荐（全清理重新安装）

```bash
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

确保用的是 **最新版本 pnpm**，你可以升级：

```bash
pnpm add -g pnpm@latest
```

> ✅ 这将清除所有可能过期或错误的模块缓存，强制重新生成 `.modules.yaml` 并重新 hoist 所有依赖。

---

### ✅ 方法二：只清除 hoisting metadata（如果你不想删除 node\_modules）

```bash
rm -rf node_modules/.modules.yaml
pnpm install
```

> 这会强制 pnpm 重新生成 hoisting 记录。

---

### ✅ 方法三：清理全局缓存（如果问题反复出现）

```bash
pnpm store prune
pnpm install
```

---

### 🧪 验证构建是否修复

之后重新运行你刚才的构建命令或启动项目：

```bash
pnpm run dev
# 或者
pnpm build
```

---

## 🧾 补充：为什么 `.modules.yaml` 会如此重要？

`pnpm` 使用了所谓的 **“内容寻址的 node\_modules”**，即：

* 不将所有依赖扁平化（不像 npm/yarn）
* 使用 `.modules.yaml` 来记录 hoisted 包的真实位置，供构建脚本和依赖查找引用

一旦这个文件失效或版本不兼容，就可能导致类似 `ERR_PNPM_MISSING_HOISTED_LOCATIONS` 的错误。

---

## ✅ 总结建议

| 操作           | 命令                                                   |
| ------------ | ---------------------------------------------------- |
| 清理一切重新安装（推荐） | `rm -rf node_modules pnpm-lock.yaml && pnpm install` |
| 仅删除 hoist 记录 | `rm -rf node_modules/.modules.yaml && pnpm install`  |
| 清缓存后重装       | `pnpm store prune && pnpm install`                   |
| 升级 pnpm      | `pnpm add -g pnpm@latest`                            |

如果你是在 **monorepo（多包项目）** 中遇到这个问题，我可以给出 workspace 专用的诊断建议。需要吗？


你**不应该忽略这个报错**，尤其是在 **Monorepo 架构下使用 pnpm 的场景中**。这个 `ERR_PNPM_MISSING_HOISTED_LOCATIONS` 报错不是一个普通的警告，而是一个 **构建失败的致命错误（error）**，意味着：

> ⚠️ **某些包将无法正确构建或运行，可能导致服务启动失败、测试失效、产物不完整**。

---

### 📌 为什么 Monorepo 更容易出现这个问题？

在 Monorepo 下：

* 各个 package（如 `package/admin`, `package/core` 等）共用一套 `node_modules`（通常放在 repo 根部）；
* pnpm 会根据各个子包的依赖关系进行 hoist，记录在 `.modules.yaml` 中；
* 一旦这个文件损坏、过时、或跨包引用不一致，就会发生依赖“找不到”的错误；
* 这在运行 `postinstall`、打包、测试等阶段**都可能失败**。

---

### ❌ 如果忽略，会发生什么？

* 你可能在 `pnpm build` 时构建失败（如你贴出的 `msw`, `esbuild`）
* 某些包（如 `msw`, `graphql-ws`）无法正确执行生命周期钩子（如 postinstall）
* 某些工具（如 Vite plugin、Storybook）引用这些模块时会发生“模块未找到”的运行时异常

---

### ✅ 正确解决方式（适用于 Monorepo）

你应当清理所有模块并**从根目录重新安装**：

```bash
# 在项目根目录执行
rm -rf node_modules pnpm-lock.yaml **/node_modules
pnpm install
```

或者，如果你不想删掉所有 `node_modules`，最小方案是：

```bash
rm -rf node_modules/.modules.yaml
pnpm install
```

---

### 🧪 附：确认是否为 Monorepo Workspace 项目

你的根目录应当有：

```
pnpm-workspace.yaml
```

并包含类似配置：

```yaml
packages:
  - "packages/*"
  - "apps/*"
```

这意味着所有 `packages/xxx` 会共用一套依赖结构，**必须由根目录统一执行 `pnpm install`**。不要在子包目录（如 `packages/admin/`）单独跑 `pnpm install`。

---

### ✅ 建议补充配置：强制依赖一致性

在 `package.json` 中添加：

```json
"pnpm": {
  "strictPeerDependencies": true
}
```

这样能在 install 时提前提示不匹配的 peer 依赖，防止运行时报错。

---

### ✅ 总结

| 问题                                   | 是否可以忽略          |
| ------------------------------------ | --------------- |
| `ERR_PNPM_MISSING_HOISTED_LOCATIONS` | ❌ 不可以，必须修复      |
| `WARN deprecated subdependencies`    | ✅ 可暂时忽略，等待上游修复  |
| `WARN peer dependency mismatch`      | ⚠️ 推荐修复，避免运行时错误 |

---

需要我检查你 workspace 的结构和依赖是否正确设置吗？你可以贴出 `pnpm-workspace.yaml` 和各子包的 `package.json`，我可以帮你诊断 hoist 问题根源。


你遇到的错误：

```
Remove-Item: A parameter cannot be found that matches parameter name 'rf'.
```

是因为你在 **PowerShell 中执行了 `rm -rf` 命令**，但：

* PowerShell 默认识别 `rm` 为 `Remove-Item`（这是 PowerShell 的内部命令），
* 而 `Remove-Item` 并不支持 `-rf` 参数，
* 所以它报错说 “找不到参数 `-rf`”。

---

## ✅ 解决方案：**明确使用 coreutils 的 `rm.exe`**

### 🟢 方法一：使用 coreutils 的 `rm.exe`（最推荐）

确保你已经用 Scoop 安装了 coreutils：

```powershell
scoop install coreutils
```

然后用完整命令调用 coreutils 提供的 `rm.exe`，如下：

```powershell
rm.exe -rf node_modules pnpm-lock.yaml
```

✅ 这就是 GNU `rm`，支持 `-rf` 参数，行为与你在 Linux/macOS 上一样。

---

## 🛠️ 可选：设置 PowerShell 别名，让 `rm` 等于 `rm.exe`

如果你不想每次都打 `rm.exe`，可以手动添加别名：

### 临时设置（当前终端有效）：

```powershell
Set-Alias rm rm.exe
```

之后就可以直接：

```powershell
rm -rf node_modules
```

### 永久设置（添加到 PowerShell 启动脚本）：

```powershell
notepad $PROFILE
```

在文件中加入：

```powershell
Set-Alias rm rm.exe
```

保存后，重启 PowerShell 即可生效。

---

## 🧪 测试推荐

你可以运行以下命令验证：

```powershell
where rm
```

如果输出中包含 coreutils 的路径，例如：

```
C:\Users\you\scoop\apps\coreutils\current\bin\rm.exe
```

说明已成功安装并可用。

---

## ✅ 总结

| 场景                 | 正确做法                          |
| ------------------ | ----------------------------- |
| PowerShell 默认 `rm` | 是 `Remove-Item`，**不能**加 `-rf` |
| 安装 coreutils 后     | 使用 `rm.exe -rf`               |
| 想用 `rm -rf`        | 添加别名 `Set-Alias rm rm.exe`    |
| 跨平台清理              | 使用 `npx rimraf` 或脚本封装         |

---

如你愿意，我可以为你写一个 **Windows + macOS/Linux 通用的项目清理脚本**，只需双击即可清除 `node_modules` 和锁文件。需要吗？
