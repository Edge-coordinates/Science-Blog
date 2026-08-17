---
title: README
date: 2022/10/14
categories:
  - README
notAutofm: true
abbrlink: 77cd4175
---


# Note
笔记备份


```sh
corepack enable
task setup          # yarn install + lefthook
task fm             # 补缺 front matter
task fm:ct          # 只重写 categories / tags
task fm:check       # CI 同款：补完后工作区必须干净
```

autofm 配置在 `.autofm/config.json`。提交前 lefthook 会跑 `yarn fm`。

## 常用正则

```
匹配图片

!\[(.*?)\]\((.*?)\)
```

## 更新 Blog

push 到 `master` 后，GitHub Actions 会构建 Hexo 并部署到 Cloudflare Pages（`rezedge-blog` / `blog.rezedge.com`）。