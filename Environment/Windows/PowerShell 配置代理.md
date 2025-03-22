---
title: PowerShell 配置代理
date: 2025/3/3 22:29:29
categories:
  - - Environment
    - Windows
---

检查代理配置：
```
Get-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
```

设置 HTTP 代理：

```
$env:HTTP_PROXY="http://127.0.0.1:7897"
```
 
设置HTTP HTTPS socks5 代理

powershell
```
$env:HTTPS_PROXY="http://127.0.0.1:7897"

$env:HTTP_PROXY="http://127.0.0.1:7897"

$env:all_proxy="socks5://127.0.0.1:7897"
```

cmd
```
set http_proxy=http://127.0.0.1:7897

set https_proxy=http://127.0.0.1:7897
```


## 注意

Anaconda 环境似乎会影响 Powershell代理，所以最好先禁用，或者配置代理

```
conda config --set auto_activate_base false
```