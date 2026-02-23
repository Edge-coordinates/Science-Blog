---
title: 如何手动修改BIOS以升级微码
date: 2026/02/23 17:16:19
categories:
  - - Environment
    - System
abbrlink: 15e7d1d4
---
# 如何手动修改BIOS以升级微码

众所周知，机械革命不是一个好的电脑厂商。

所以虽然Intel 14900 系列一直有着问题，但是想要让他们去更新bios那是想都不要想的。

所以基本上得要自己想办法去更新微码。

二六年二月二十三日朋友告诉吾辈，微码是可以自己手动更新的，感恩。

## 需要用到的 Tool

### Flash Programming Tool (FPT)

对于Intel芯片组的主板，FPT 作为 CSME System Tools 包中的一部分，用来提取和刷入 BIOS。  
**注意**：刷入前可能需要先禁用 BIOS 的写保护功能（如果 BIOS 支持该功能）。

### MMTool

American Megatrends Inc. 公司 Aptio 工具套件的一部分，所以自然是没有直接下载方案的


#### 下载 


### UEFI-Editor

GitHub: https://github.com/BoringBoredom/UEFI-Editor

### 