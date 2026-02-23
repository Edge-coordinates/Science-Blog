---
title: Solidworks 2024 开启 RealView
date: 2026/02/23 17:16:19
categories:
  - - Environment
    - APP
    - Solidworks
abbrlink: c938871
---
将注册表定位到：
```
HKEY_CURRENT_USER\SOFTWARE\SolidWorks\AllowList\Current
```

在右侧窗口找到 Renderer 项，双击并复制其"Value"（例如：NVIDIA GeForce RTX 4080 Laptop GPU/PCIe/SSE2）

定位 Gl2Shaders：导航至：

```
HKEY_CURRENT_USER\SOFTWARE\SolidWorks\AllowList\Gl2Shaders
```

根据显卡品牌（NVIDIA 选 NV40，AMD 选 R420，Intel 选 Other），在对应文件夹下新建项（key），重命名为刚才复制的名称。

在新文件夹内新建 DWORD (32位) 值，命名为 Workarounds，数值建议填入 30408 或 31408 (十六进制)(Hexadecimal)