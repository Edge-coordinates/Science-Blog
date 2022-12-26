---
title: Windows下常用命令总结
date: 2022/10/14

categories:
  - Environment
tags:
  - Windows
abbrlink: d67c5edc
---



## 
作为一名专业瞎搞人员，记录一下自己常用的命令是非常必要的，只有这样，才可以最大化的在朋友面前~~装逼~~bushi。

## 终端
```powershell
mkdir xxx #新建文件夹
cd . >a.json #新建文件
ren .\b.json a.json #重命名
new-item 文件名字.文件格式 -type file #新建文件
rename-Item .\a.json -NewName b.json #重命名
del xxx #删除
```

## 硬件相关
- nvcc -V"或“nvcc --version”即可查看CUDA
- nvidia-smi 提供监控GPU使用情况和更改GPU状态的功能，可以查看电脑目前支持的CUDA版本  
  相关内容参考[GPU之nvidia-smi命令详解](https://www.jianshu.com/p/ceb3c020e06b)
- 

## Python相关
