---
title: Git Push Summary 指南
date: 2025/4/2 21:32:53
categories:
  - - Environment
    - Git
abbrlink: 8df49a51
---
# Git Git Push Summary 指南

#### You:
git 提交 summary and deiscription 生成指南

#### ChatGPT:
Git 提交信息（commit message）分为两部分：

1. **Summary（摘要）：** 一行简洁描述，通常不超过 50 个字符。
2. **Description（描述）：** 更详细的说明（可选），解释变更的背景、动机和影响，建议每行不超过 72 字符。

---

## ✅ 标准格式示例

```
feat(login): 支援使用者透過 Google 登入

新增 Google OAuth 流程，包括前端按鈕與後端驗證邏輯。
目前僅支援網頁版，行動版尚未整合。
```

---

## ✍️ Summary（摘要）撰寫指南

- 使用祈使句（imperative mood），如：Add、Fix、Update
- 首字母小寫（英文）或正常中文語法
- 不加句號
- 包含類型與範圍（可選，但推薦）

### 常用類型（以 conventional commits 為基準）：

| 類型         | 說明           |
| ---------- | ------------ |
| `feat`     | 新功能          |
| `fix`      | 錯誤修復         |
| `refactor` | 重構（非功能變更）    |
| `docs`     | 文件變更         |
| `style`    | 格式（不影響邏輯）    |
| `test`     | 測試新增或修改      |
| `chore`    | 建構系統、套件更新等雜項 |

#### 範例：

- `feat: 新增文章列表分頁功能`
- `fix(api): 修正錯誤處理邏輯`
- `docs: 補充 README 使用方式`

---

## 📝 Description（描述）撰寫指南

可選，用來補充 Summary 無法涵蓋的資訊，例如：

- 變更的動機與背景
- 實作方式（概述即可）
- 對使用者或其他功能的影響
- 若有破壞性改動，應標註 `BREAKING CHANGE`

#### 範例：

```
fix(user): 修正無法儲存使用者偏好的問題

原本未正確處理 localStorage 的同步流程，導致設定未儲存。
已調整為每次點擊儲存按鈕時即同步狀態。
```

---

## 💡 建議工具與習慣

- 使用 `git commit -m "summary" -m "description"` 撰寫
- 搭配 `commitizen` 或 `git cz` 工具，可強制格式一致
- 可結合 Git Hook（如 Husky）進行檢查

---

需要我幫你根據修改內容生成 summary & description 嗎？你可以貼出 diff 或簡述內容。


#### You:
对于前端项目呢？比如添加新的组件，文档

#### ChatGPT:
对于前端项目，Git 提交规范同样适用，尤其推荐使用 [Conventional Commits](https://www.conventionalcommits.org/)，可以方便集成 changelog 自动生成、版本控制（如 Semantic Release）等工具。

下面是专为前端项目整理的建议 👇

---

## 🧩 前端常用提交类型（类型 + 范围）

| 类型         | 用途                    | 示例（含 scope）                  |
| ---------- | --------------------- | ---------------------------- |
| `feat`     | 新功能（组件、交互、逻辑等）        | `feat(button): 新增基础按钮组件`     |
| `fix`      | 修复 bug                | `fix(form): 修复表单验证逻辑错误`      |
| `refactor` | 重构，不影响功能              | `refactor(modal): 抽离重复的动画逻辑` |
| `style`    | UI 风格变动、CSS、代码格式      | `style(global): 微调主题色与字体大小`  |
| `docs`     | 文档变更（README、注释、组件说明等） | `docs(tooltip): 补充使用方式说明`    |
| `test`     | 添加或修改测试               | `test(header): 增加响应式测试用例`    |
| `chore`    | 构建配置、依赖更新等杂项          | `chore: 升级 vite 到 v5.0`      |
| `perf`     | 性能优化                  | `perf(list): 虚拟渲染长列表`        |
| `build`    | 构建相关变更                | `build: 调整 Webpack 插件配置`     |
| `ci`       | CI 相关                 | `ci: 新增 GitHub Actions 流程`   |

---

## 🧾 示例 1：新增组件

```
feat(card): 新增通用卡片组件

卡片组件支援標題、副標題、操作區與自定內容插槽。
樣式符合設計系統 V2 規範，支援深色模式。
```

---

## 🧾 示例 2：补充组件文档

```
docs(card): 補充卡片元件的 README 範例與屬性說明

包含 props、slots、事件與樣式自定義方式。
```

---

## 🧾 示例 3：调整样式 / 主题

```
style(theme): 微調主要按鈕顏色與 hover 效果
```

---

## ✅ Tips

- Scope（例如 `card`, `form`, `modal`）可以是元件名稱、模組名稱，有助於定位
- 文档变更写成 `docs(组件名)` 可读性佳，配合组件库（如 VuePress、Storybook）很实用
- 若你有自动部署或打包流程，使用标准提交格式非常重要（配合 semantic-release）

---

你有哪类改动我可以帮你写一条实际的提交信息？可以贴代码或简述一下～
