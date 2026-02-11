---
title: wsl 服务链接失败
date: 2026/02/11 23:57:21
categories:
  - - Environment
    - Windows
abbrlink: d93d03a8
---


在 wsl 启动 meilisearch，发现无法连接上，最后切换为net 模式，获取虚拟机IP之后，察觉是代理的问题，命令行如果进行代理的话，可能产生冲突。

需要关闭命令行代理