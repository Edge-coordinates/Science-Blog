---
title: reprint-解决神舟 T8 Pro E64 无法开启安全启动的问题 - Moe Blog
date: 2026/02/23 17:16:19
categories:
  - - Environment
    - System
abbrlink: bf7f45c9
---
> 原文地址 [blog.1loli.link](https://blog.1loli.link/archives/105/)

### 问题描述

我在神舟 T8 Pro E64 (616QY) 笔记本上尝试开启安全启动 (Secure Boot) 时，BIOS 提示当前处于 "Setup Mode"，需要切换到"User Mode" 才能成功开启。  
![](https://blog.1loli.link/usr/uploads/2025/07/1378833192.png)  
经过大量尝试和查阅资料，发现此型号笔记本由广达代工，其 BIOS 隐藏了大量高级选项，包括关键的密钥管理 (Key Management) 设置页面，导致无法通过常规方法解决。

本文记录了解决此问题的完整过程。

### 教程

核心思路是通过修改 BIOS，将隐藏的 "Key Management" 菜单显示出来，然后手动注册安全启动所需的密钥文件。

#### 第一步：提取并修改 BIOS

1.  **提取 BIOS 文件**
    
    *   对于 Intel 芯片组的主板，可以使用官方 CSME System Tools 包中的 Flash Programming Tool (FPT) 来提取和刷入 BIOS。
    *   **注意**：刷入前可能需要先禁用 BIOS 的写保护功能（如果 BIOS 支持该功能）。
2.  **编辑 BIOS 文件**
    
    *   使用 [UEFI-Editor](https://github.com/BoringBoredom/UEFI-Editor) 工具打开提取出的 BIOS 文件。
    *   根据该工具的教程，在 BIOS 设置中找到安全启动 (Secure Boot) 相关的菜单。
    *   定位到被隐藏的 "Key Management" 项目（通常会被标记为 Suppressed），解除其隐藏状态。
    *   保存修改后的 BIOS 文件。
3.  **刷入修改后的 BIOS**
    
    *   使用 Flash Programming Tool (FPT) 将修改后的 BIOS 文件刷回主板。

#### 第二步：准备安全启动密钥文件

1.  **下载密钥文件**
    
    *   访问微软在 GitHub 上的官方仓库：[secureboot_objects](https://github.com/microsoft/secureboot_objects/releases)。
    *   下载最新版本的 `dbx`, `db`, `KEK`, `PK` 文件。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/1503472119.jpg)
2.  **准备存储介质**
    
    *   将下载的所有密钥文件解压，并存放至一个 FAT32 格式的 U 盘根目录。

#### 第三步：手动导入密钥并配置启动项

1.  **进入 BIOS 设置**
    
    *   重启电脑，进入 BIOS 设置界面。此时，你应该可以在安全启动菜单下看到之前被隐藏的 "Key Management" 选项。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/2465528013.png)
2.  **检查密钥状态**
    
    *   进入 "Key Management" 页面，检查 `PK`, `KEK`, `db`, `dbx` 的状态。在我的情况中，这些项目初始大小均为 0KB，且尝试恢复出厂默认密钥 (Restore Default PK) 会提示失败。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/3617543902.png)
3.  **手动导入密钥**
    
    *   依次选择 `PK`, `KEK`, `db`, `dbx` 选项，并从之前准备好的 U 盘中手动导入对应的文件。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/4247723101.png)
4.  **注册 Windows 启动文件**
    
    *   在 "Key Management" 页面中，找到并选择 "Enroll Efi Image" 选项。
    *   浏览到你的 Windows 启动分区 (ESP 分区)。
    *   选择 Windows 的启动文件，路径通常为 `/EFI/Microsoft/Boot/bootmgfw.efi`，并确认导入。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/288453274.jpg)
        
        #### 第四步：开启并验证安全启动
    
5.  **开启安全启动**
    
    *   完成上述所有操作后，返回上一级菜单，尝试开启安全启动 (Secure Boot)。此时应该可以被正常设置为 "Enabled"。  
        ![](https://blog.1loli.link/usr/uploads/2025/07/559349980.jpg)
6.  **保存并退出**
    
    *   按 `F10` 保存更改并重启电脑。
7.  **验证结果**
    
    *   进入 Windows 系统后，打开 "Windows 安全中心" 或运行 `msinfo32` (系统信息)，可以查看到安全启动状态是否已成功开启。

**注意**：如果在启动过程中遇到红色的提示框，显示 "Verification failed" 或类似的验证失败信息，这通常意味着启动文件验证不通过。你需要重新执行第三步的第 4 点，确保导入了正确的 `bootmgfw.efi` 文件。  
![](https://blog.1loli.link/usr/uploads/2025/07/59466183.png)