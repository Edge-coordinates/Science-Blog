---
title: Git Rebase
date: 2025/10/08 18:57:34
updated: 2025/10/08 18:57:35
categories:
  - - Environment
    - Git
abbrlink: 11c6bb07
---

[一、直观理解](#直观理解)
[二、`rebase` 做了什么](#rebase-做了什么)
[三、为什么要这样做](#为什么要这样做)
[四、要小心的地方](#要小心的地方)
- [直观理解](#直观理解)
- [`rebase` 做了什么](#rebase-做了什么)
- [为什么要这样做](#为什么要这样做)
- [要小心的地方](#要小心的地方)
  - [视觉图上](#视觉图上)
  - [技术层面](#技术层面)
  - [额外的Tips](#额外的tips)
- [和merge的区别](#和merge的区别)
  - [初始状态（准备阶段）](#初始状态准备阶段)
  - [使用 `merge`](#使用-merge)
  - [使用 `rebase`](#使用-rebase)
- [合并回 dev](#合并回-dev)


好问题。`rebase` 是 Git 里一个**非常强大但也容易被误解**的命令。
简单说，它的作用是：

> 把你的提交“挪到”另一个分支的最新节点上去，就像时间旅行一样，把你的工作“重演”一遍。

---

### 直观理解

假设你有这样的历史：

```
A---B---C (dev)
         \
          D---E (feature)
```

这里：

* `A-B-C` 是 `dev` 分支的提交。
* 你从 `C` 开了一个 `feature` 分支，做了 `D`、`E` 两次提交。
* 但后来 `dev` 上别人又提交了 `F`、`G`。

现在变成：

```
A---B---C---F---G (dev)
         \
          D---E (feature)
```

如果你现在要把 `feature` 合并回 `dev`，会出现分叉历史，看起来乱糟糟。

---

### `rebase` 做了什么

执行：

```
git checkout feature
git rebase dev
```

Git 会把 `feature` 的提交 D、E **拿下来、暂存起来**，
然后**接在最新的 dev（G）之后**重新“播放”一遍。
于是历史就变成：

```
A---B---C---F---G---D'---E' (feature)
```

这里的 `D' E'` 是“重演版”的 D、E，内容一样但哈希不同。
现在看起来历史像是一条干净的直线。

---

### 为什么要这样做

优点是：

1. **历史更干净**：没有多余的“Merge commit”。
2. **方便 review**：每个提交按时间顺序排列。
3. **避免冲突积压**：提前在自己的分支里解决冲突，而不是到合并时才一锅端。

---

### 要小心的地方

* rebase **会改写提交历史**，因此不要对**公共分支**（别人也在用的分支）执行。
  否则别人拉代码时会出现冲突地狱。
* 自己的 feature 分支上用没问题（只影响你一个人）。

把你的 feature 分支的提交 “搬到” dev 的最新节点之后，改变的是 feature 分支的历史，是安全的。

`rebase` **不会删除分支**，而是“重塑”这个分支的历史。


#### 视觉图上

想象你原本的 `feature` 分支是一条从 `C` 出发的小支线：

```
A---B---C (dev)
         \
          D---E (feature)
```

当你执行：

```bash
git checkout feature
git rebase dev
```

Git 会做：

1. 把 D、E 拿下来暂存；
2. 把 feature 分支“移到” dev 的最新节点；
3. 再把 D、E 重新播放一遍（生成 D′、E′）。

于是结果变成：

```
A---B---C---F---G (dev)
                 \
                  D'---E' (feature)
```

`feature` 分支还在，只是它**现在指向 D′、E′**（新的提交），
而旧的 D、E 变成“悬空提交”，暂时没人引用（Git 会在几天后自动清理掉）。

---

#### 技术层面

* **不会删除分支名**：`feature` 仍存在，你依然可以 `git checkout feature`。
* **会改变提交哈希**：D、E 的哈希变成新的 D′、E′。
* **旧历史仍在**：Git 暂时保留被改写的提交（在 `.git/refs/original` 中）。

* 如果你立刻后悔，可以用：

  ```bash
  git reflog
  git reset --hard <旧哈希>
  ```

  来恢复。

而真正会“销毁分支”的操作是：

```bash
git branch -d feature
```

#### 额外的Tips

如果你在多人协作的远程仓库中使用：

* 本地 rebase 后推送时，必须加 `--force` 或 `--force-with-lease`：

  ```bash
  git push origin feature --force-with-lease
  ```

  否则远程因为哈希不同会拒绝。

### 和merge的区别

#### 初始状态（准备阶段）

假设我们有：

```
A---B---C---F---G (dev)
         \
          D---E (feature)
```

* `dev` 分支走到了 G。
* 你从 `C` 分出来开发 `feature`，做了两个提交 D、E。

---

#### 使用 `merge`


```bash
git checkout dev
git merge feature
```

结果：

```
A---B---C---F---G---M (dev)
         \         /
          D-------E (feature)
```

#### 使用 `rebase`

```bash
git checkout feature
git rebase dev
```

结果：

```
A---B---C---F---G---D'---E' (feature)
```

所以，rebase是用于处理个人分支，merge是用于将个人分支合并到公共分支

### 合并回 dev

正如上面所示，这时候就可以用merge合并回dev，不过因为feature的历史干净，所以合并之后的历史也会比较漂亮