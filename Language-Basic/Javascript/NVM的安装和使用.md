---
title: NVM的安装和使用
date: 2022/10/14
categories:
  - Javascript
abbrlink: 5a6c750f
tags:
---



## 准备，下载与安装

**本文在[nvm.uihtm.com](https://nvm.uihtm.com/)的基础上略加修改**  
**注意：本篇主要讲述NVM的使用，博主本人，只在Windows下安装成功过NVM。**

请前往[nvm.uihtm.com](https://nvm.uihtm.com/)，下载安装NVM。


### 安装完确认

打开 CMD，输入命令 `nvm` ，安装成功则如下显示。可以看到里面列出了各种命令，本节最后会列出这些命令的中文示意。
![](https://nvm.uihtm.com/images/step5.png)

* * *

## NVM使用
### nvm 命令总结

*   `nvm arch`：显示 node 是运行在 32 位还是 64 位。
*   `nvm install <version> [arch]` ：安装 node， version 是特定版本也可以是最新稳定版本 latest。可选参数 arch 指定安装 32 位还是 64 位版本，默认是系统位数。可以添加 --insecure 绕过远程服务器的 SSL。
*   `nvm list [available]` ：显示已安装的列表。可选参数 available，显示可安装的所有版本。list 可简化为 ls。
*   `nvm on` ：开启 node.js 版本管理。
*   `nvm off` ：关闭 node.js 版本管理。
*   `nvm proxy [url]` ：设置下载代理。不加可选参数 url，显示当前代理。将 url 设置为 none 则移除代理。
*   `nvm node_mirror [url]` ：设置 node 镜像。默认是 https://nodejs.org/dist/。如果不写 url，则使用默认 url。设置后可至安装目录 settings.txt 文件查看，也可直接在该文件操作。
*   `nvm npm_mirror [url]` ：设置 npm 镜像。https://github.com/npm/cli/archive/。如果不写 url，则使用默认 url。设置后可至安装目录 settings.txt 文件查看，也可直接在该文件操作。
*   `nvm uninstall <version>` ：卸载指定版本 node。
*   `nvm use [version] [arch]` ：使用制定版本 node。可指定 32/64 位。
*   `nvm root [path]` ：设置存储不同版本 node 的目录。如果未设置，默认使用当前目录。
*   `nvm version` ：显示 nvm 版本。version 可简化为 v。

* * *

### 安装 node.js 版本

`nvm list available` 显示可下载版本的部分列表

![](https://nvm.uihtm.com/images/nvm-list-available.png)

`nvm install latest`安装最新版本 (安装时可以在上面看到 node.js 、 npm 相应的版本号 ，不建议安装最新版本)

![](https://nvm.uihtm.com/images/nvm-install-latest.png)

`nvm install` 版本号 安装指定的版本的 nodejs

![](https://nvm.uihtm.com/images/nvm-install-node.png)

* * *

### 查看已安装版本

`nvm list`或`nvm ls`查看目前已经安装的版本 （ 当前版本号前面没有 * ， 此时还没有使用任何一个版本，这时使用 node.js 时会报错 ）

![](https://nvm.uihtm.com/images/nvm-list1.png)![](https://nvm.uihtm.com/images/nvm-list2.png)

* * *

### 切换 node 版本

`nvm use`版本号 使用指定版本的 nodejs （ 这时会发现在启用的 node 版本前面有 * 标记，这时就可以使用 node.js ）

![](https://nvm.uihtm.com/images/nvm-use.png)

* * *

### nvm 常见问题

如果下载 node 过慢，请更换国内镜像源, 在 nvm 的安装路径下，找到 settings.txt，设置 node_mirro 与 npm_mirror 为国内镜像地址。下载就飞快了~~
```
root: D:\nvm  
path: D:\nodejs  
node_mirror: https://npm.taobao.org/mirrors/node/  
npm_mirror: https://npm.taobao.org/mirrors/npm/  
```