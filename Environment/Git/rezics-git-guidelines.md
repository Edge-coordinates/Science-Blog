---
title: rezics-git-guidelines
date: 2025/10/08 18:55:04
updated: 2025/10/08 18:55:29
categories:
  - - Environment
    - Git
abbrlink: a91f3b75
---

## Git 使用规范

### 一、分支策略

仓库采用简化版 **Git Flow** 模型：

```
main
└── dev
    ├── feature/xxx
    ├── fix/yyy
    └── chore/zzz
```

#### 各分支职责：

* **`main`**：稳定版本分支，对应线上部署环境。

  * 每次发布前从 `dev` 合并并打 tag。
  * 禁止直接提交代码。

* **`dev`**：开发整合分支，用于联调与测试。

  * 所有新功能分支应从 `dev` 拉出，完成后再合并回 `dev`。

* **`feature/*`、`fix/*`、`chore/*`**：

  * 分别对应功能开发、Bug 修复、维护性改动（依赖更新、脚本调整等）。
  * 开发完成后通过 Pull Request 合并到 `dev`。

---

### 二、分支操作流程

1. **创建分支**

   ```bash
   git checkout dev
   git pull
   git checkout -b feature/user-login
   ```

2. **开发与提交**

   * 小步提交，逻辑原子化。
   * commit message 采用规范格式（见下文）。

3. **保持分支更新**

   ```bash
   git fetch origin
   git rebase origin/dev
   ```

   > 💡 *注释：`rebase` 会将当前分支的提交“重放”到最新的 dev 之后，从而保持线性历史，避免多余的 merge 记录。它会改写提交哈希，因此仅应在个人分支使用。*

4. **合并回 dev**

   * 提交 PR 或在测试通过后手动合并：

     ```bash
     git checkout dev
     git merge --no-ff feature/user-login
     git push origin dev
     ```

5. **发布到 main**

   ```bash
   git checkout main
   git merge --no-ff dev
   git tag -a v1.2.0 -m "Release 1.2.0"
   git push origin main --tags
   ```

---

### 三、提交信息规范

采用 **Conventional Commits** 标准：

```
<type>: <description>
```

**常见 type：**

* `feat`：新增功能
* `fix`：修复缺陷
* `refactor`：重构（非功能性修改）
* `chore`：构建流程、工具、依赖调整
* `docs`：文档变更
* `style`：代码格式修改（无逻辑改动）

**示例：**

```
feat: 新增用户登录接口
fix: 修复 token 过期导致无法刷新问题
refactor: 重构 userService 提高性能
chore: 更新依赖与脚本
docs: 更新 README
```

> 推荐结合 [commitlint](https://github.com/conventional-changelog/commitlint) 与 [husky](https://github.com/typicode/husky) 自动校验提交信息。

---

### 四、发布与修复流程

* **发布**：`dev` → `main` → 打 tag → 自动部署。
* **热修复（hotfix）**：
  从 `main` 拉出 `hotfix/x.y.z` 分支 → 修复后合并回 `main` 与 `dev`。

---

### 五、单人项目简化规则

若项目仅由个人维护，可采用：

* `dev` 作为开发主分支
* `main` 仅在版本发布前同步一次
* 临时改动可直接在 `dev` 提交，无需频繁建分支