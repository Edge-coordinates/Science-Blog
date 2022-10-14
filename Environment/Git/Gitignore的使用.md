---
title: Gitignore的使用
categories:
  - Git
abbrlink: 1ae30c16
tags:
---



`.gitignore` 文件是一个文本文件，它告诉 Git 要忽略项目中的哪些文件或文件夹。

本地 `.gitignore` 文件通常被放置在项目的根目录中。你还可以创建一个全局 `.gitignore` 文件，该文件中的所有条目都会在你所有的 Git 仓库中被忽略。


要创建本地 `.gitignore` 文件，请创建一个文本文件，并将其命名为 `.gitignore`（请记住在开头包含 `.`）。 然后根据需要编辑该文件。在每一行列出你希望 Git 忽略的文件或文件夹。

该文件中的条目也可以遵循匹配模式。

*   `*` 用作通配符匹配
*   `/` 用于忽略相对于 `.gitignore` 文件的路径名
*   `#` 用于将注释添加到 `.gitignore` 文件

这是一个 `.gitignore` 文件的示例：

```
# Ignore Mac system files
.DS_store

# Ignore node_modules folder
node_modules

# Ignore all text files
*.txt

# Ignore files related to API keys
.env

# Ignore SASS config files
.sass-cache

# 忽略所有的__pycache__文件夹（包括子文件夹）
**/__pycache__

```
## 全局的.gitignore

```
git config --global core.excludesfile ~/.gitignore_global

```

这将创建文件 `~/.gitignore_global`。现在，你可以通过与编辑本地 `.gitignore` 文件相同的方式编辑该文件。你所有的 Git 仓库都将忽略全局 `.gitignore` 文件中列出的文件和文件夹。

### 如何忽略已检入的文件

要忽略单个文件，即停止跟踪文件但不从系统中删除它，请使用：

`git rm --cached filename`

要忽略 `.gitignore` 中的_每个文件_：

首先**提交**代码修改，然后运行：

`git rm -r --cached`

这将从索引（暂存区域）中删除所有更改的文件，然后运行：

`git add .`

提交：

`git commit -m ".gitignore is now working"`

要取消 `git rm --cached filename`，请运行 `git add filename`。

## 文章推荐
> Git 文档：[gitignore](https://git-scm.com/docs/gitignore)  
> 忽略文件：[GitHub](https://help.github.com/articles/ignoring-files/)  
> 有用的 `.gitignore` 模版：[GitHub](https://github.com/github/gitignore)  
> [Gitignore Explained: What is Gitignore and How to Add it to Your Repo](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/)
