---
title: WSL 常用命令
date: '2025/9/8 23:11:38'
categories:
  - Environment
  - Windows
abbrlink: 8add49dd
---
wsl -l -v 

## 注销发行版（会删掉这个发行版的根文件系统）
wsl --unregister EdgeDB.WSL.1 

## 进入 WSL 发行版
wsl -d EdgeDB.WSL.1 