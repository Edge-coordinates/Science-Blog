---
title: Git 追踪文件大小写
date: 2026/02/14 19:39:24
categories:
  - - Environment
    - Git
abbrlink: 7491252b
---
# Git 追踪目录大小写问题小记

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