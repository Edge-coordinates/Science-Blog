---
title: 教程-Scoop 超好用的Windows包管理器
categories:
- Configure
tags:
---


- [前言](#前言)
- [环境要求](#环境要求)
- [安装 Scoop](#安装-scoop)
- [基础使用](#基础使用)
  - [下载特定版本的软件](#下载特定版本的软件)
  - [迁移到新电脑](#迁移到新电脑)
  - [更换源](#更换源)
- [进阶使用](#进阶使用)
  - [添加 bucket](#添加-bucket)
    - [第三方 bucket](#第三方-bucket)
  - [清理安装包缓存](#清理安装包缓存)
  - [删除旧版本软件](#删除旧版本软件)
  - [在同一程序的不同版本之间切换](#在同一程序的不同版本之间切换)
  - [全局安装](#全局安装)
  - [别名](#别名)
  - [代理设置](#代理设置)
  - [开启多线程下载](#开启多线程下载)
  - [利用 aria2 进行断点续传](#利用-aria2-进行断点续传)
- [一些使用实例](#一些使用实例)
  - [安装和切换JDK、Python的版本](#安装和切换jdkpython的版本)
- [常用命令总结](#常用命令总结)
- [尾巴](#尾巴)
- [遗留的问题](#遗留的问题)
  - [网络问题](#网络问题)
    - [fatal: unable to access 'https://github.com/lukesampson/scoop-extras/': OpenSSL SSL_read: Connection was reset, errno 10054](#fatal-unable-to-access-httpsgithubcomlukesampsonscoop-extras-openssl-ssl_read-connection-was-reset-errno-10054)
    - [手动配置http代理后aria2多线程下载不可使用](#手动配置http代理后aria2多线程下载不可使用)
  - [安装软件失败](#安装软件失败)
    - [网络问题导致app安装失败](#网络问题导致app安装失败)
    - [其它问题导致安装失败](#其它问题导致安装失败)
    - [Scoop安装软件失败的原因分类](#scoop安装软件失败的原因分类)

## 前言

[Scoop](https://github.com/lukesampson/scoop) 是一个 Win­dows 包管理工具，类似于 De­bian 的 `apt`、ma­cOS 的 `homebrew`。它由开源社区驱动，体验可能是是目前所有 Win­dows 包管理工具中最好的。对开发者来说，包管理器能非常方便的部署开发环境，比如 Python 、Node.js 。而对于像博主这样的普通的计算机使用者来说，可以方便的安装一些常用软件，尤其是开源软件，免去了手动去官网下载的繁琐步骤，而且后续对软件进行升级只需要输入一行命令，非常便捷。

## 环境要求

*   Windows 7 SP1 + / Windows Server 2008+  
*   [PowerShell 5](https://p3terx.com/go/aHR0cHM6Ly9ha2EubXMvd21mNWRvd25sb2Fk)（或更高版本，包括 [PowerShell Core](https://p3terx.com/go/aHR0cHM6Ly9kb2NzLm1pY3Jvc29mdC5jb20vZW4tdXMvcG93ZXJzaGVsbC9zY3JpcHRpbmcvaW5zdGFsbC9pbnN0YWxsaW5nLXBvd2Vyc2hlbGwtY29yZS1vbi13aW5kb3dzP3ZpZXc9cG93ZXJzaGVsbC02)）和 [.NET Framework 4.5](https://p3terx.com/go/aHR0cHM6Ly93d3cubWljcm9zb2Z0LmNvbS9uZXQvZG93bmxvYWQ)（或更高版本）Win10(11)默认满足此条件  
*   Windows 用户名为英文（Windows 用户环境变量中路径值不支持中文字符）  
*   **正常、快速**的访问 GitHub 并下载资源  

## 安装 Scoop

Scoop 默认使用普通用户权限，其本体和安装的软件默认会放在 `%USERPROFILE%\scoop`(即 `C:\Users\用户名\scoop`)，使用管理员权限进行全局安装 (`-g`) 的软件在 `C:\ProgramData\scoop`。如果有自定安装路径的需求，那么要提前设置好环境变量，否则后续再改不是一件容易的事情。

*   打开 PowerShell
*   设置用户安装路径

```
$env:SCOOP='C:\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')

```

*   设置全局安装路径（需要管理员权限）

```
$env:SCOOP_GLOBAL='C:\Scoop_Global'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')

```

*   设置允许 PowerShell 执行本地脚本

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

*   安装 Scoop

```
iwr -useb get.scoop.sh | iex  
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```
<font color=red size=4>**其实,上面两种都不可行**</font>  
先配置Host文件，加上    
199.232.68.133 raw.githubusercontent.com  
然后执行另一条可用的网址的命令:
```
iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/lukesampson/scoop/master/bin/install.ps1')  
```

*   没安装过 Git 则需要安装。

```
scoop install git
```

## 基础使用

最基础的使用方法和其它包管理器类似，这里就不做赘述了，直接上命令列表：

*   `scoop search <app>` - 搜索软件
*   `scoop install <app>` - 安装软件
*   `scoop info <app>` - 查看软件详细信息
*   `scoop list` - 查看已安装软件
*   `scoop uninstall <app>` - 卸载软件，`-p`删除配置文件。
*   `scoop update` - 更新 scoop 本体和软件列表
*   `scoop update <app>` - 更新指定软件
*   `scoop update *` - 更新所有已安装的软件
*   `scoop checkup` - 检查 scoop 的问题并给出解决问题的建议
*   `scoop help` - 查看命令列表
*   `scoop help <command>` - 查看命令帮助说明

### 下载特定版本的软件
使用`scoop install [软件名]@版本号`来安装想要的版本。
```powershell
scoop install python@3.6.8 # 安装指定的版本 scoop
```
### 迁移到新电脑
将文件夹拷贝到新电脑,将文件夹添加到环境变量然后`scoop reset *`

### 更换源
因为某些原因，Scoop在国内经常访问不了，可以选择更换源比如[这个](https://gitee.com/squallliu/scoop),但本人并未使用此方法，更建议配置代理。

进阶使用
----

### 添加 bucket

所有的包管理器都会有相应的软件仓库 ，而 bucket 就是 Scoop 中的软件仓库。细心的你可能会发现 `scoop` 翻译为中文是 “舀”，而 `bucket` 是 “水桶”，所以安装软件可以理解为从水桶里舀水，似乎很形象的说。  
Scoop 默认软件仓库（main bucket）软件数量是有限的，但是可以进行额外的添加。通过 `scoop bucket known` 命令可以查看官方认可的 bucket：  
```
$ scoop bucket known
main
extras
versions
nightlies
nirsoft
php
nerd-fonts
nonportable
java
games
jetbrains
```

以上官方认可的 bucket 可以通过下面这个命令直接添加：

```
scoop bucket add <bucketname>
```
好像有人添加bucket出现问题？如有，请在评论区提出。



[extras](https://github.com/lukesampson/scoop-extras) 涵盖了大部分因为种种原因不能被收录进主仓库的常用软件，这个是强推荐添加的。

```
scoop bucket add extras
```

常用的写盘工具 Ru­fus 就在 `extras` 这个仓库中。

```
scoop install rufus

```

[nerd-fonts](https://github.com/matthewjberger/scoop-nerd-fonts) 包含了美化终端时会用到的 Pow­er­line 字体

```
scoop bucket add nerd-fonts

```

当添加 `nerd-fonts` 仓库后可以通过以下命令搜索到所有的字体：

```
scoop search "-NF"
```

安装字体需要使用管理员权限：

```
sudo scoop install FiraCode-NF
```

#### 第三方 bucket

添加第三方 bucket

```
scoop bucket add <bucketname> https://github.com/xxx/xxx
```

从第三方 bucket 中安装软件

```
scoop install <bucketname>/<app>
```

这里给出一个第三方软件源[Scoop Directory](https://github.com/rasa/scoop-directory),它记录了 Github 上各种 bucket。

### 清理安装包缓存

Scoop 会保留下载的安装包，对于卸载后又想再安装的情况，不需要重复下载。但长期累积会占用大量的磁盘空间，如果用不到就成了垃圾。这时可以使用 `scoop cache` 命令来清理。

*   `scoop cache show` - 显示安装包缓存
*   `scoop cache rm <app>` - 删除指定应用的安装包缓存
*   `scoop cache rm *` - 删除所有的安装包缓存

如果你不希望安装和更新软件时保留安装包缓存，可以加上 `-k` 或 `--no-cache` 选项来禁用缓存：

*   `scoop install -k <app>`
*   `scoop update -k *`

### 删除旧版本软件

当软件被更新后 Scoop 还会保留软件的旧版本，更新软件后可以通过 `scoop cleanup` 命令进行删除。

*   `scoop cleanup <app>` - 删除指定软件的旧版本
*   `scoop cleanup *` - 删除所有软件的旧版本

与安装软件一样，删除旧版本软件的同时也可以清理安装包缓存，同样是加上 `-k` 选项。

*   `scoop cleanup -k <app>` - 删除指定软件的旧版本并清除安装包缓存
*   `scoop cleanup -k *` - 删除所有软件的旧版本并清除安装包缓存

### 在同一程序的不同版本之间切换
使用命令：`scoop reset [app]@[version]`  
实例：
```bash
scoop reset idea-ultimate-eap@201.6668.13

scoop reset idea-ultimate-eap@201.6073.9

# 切换到最新版本
scoop reset idea-ultimate-eap
```
对应版本的程序需要已经安装于本地系统中；所以在你清除某个软件的旧版本时考虑一下自己是否还会再次使用到此旧版本。  
另外 idea-ultimate-eap 切换过程可能需要更长时间。

### 全局安装

全局安装就是给系统中的所有用户都安装，且环境变量是系统变量，对于需要设置系统变量的一些软件就需要全局安装，比如 Node.js、Python ，否则某些情况会出现无法找到命令的问题。

使用 `scoop install <app>` 命令加上 `-g` 或 `--global` 选项可对软件进行全局安装，全局安装需要管理员权限，所以需要提前以管理员权限运行的 Pow­er­Shell 。更简单的方式是先安装 `sudo`，然后用 `sudo` 命令来提权执行：

```
scoop install sudo
sudo scoop install -g <app>
```

> 达成在 Win­dows 上使用`sudo`的成就

使用 `scoop list` 命令查看已装软件时，全局安装的软件末尾会有 `*global*` 标志。

```
➜ scoop list
Installed apps:

  7zip 19.00
  adb 30.0.0
  aria2 1.35.0-1
  busybox 3466-g53c09d0e1
  CascadiaCode-NF 2.1.0 [nerd-fonts]
  colortool 1904.29002
  dark 3.11.2 *global*
  ffmpeg 4.2.3
  figlet 1.0-go
  FiraCode-NF 2.1.0 [nerd-fonts]
  git 2.26.2.windows.1 *global*
  innounp 0.49
  iperf3 3.1.3
  lessmsi 1.6.91 *global*
  lxrunoffline 3.4.1 [extras]
  nano 4.9-4
  neofetch 7.0.0
  nodejs-lts 12.17.0 *global*
  python 3.8.3 *global*
  rclone 1.52.0
  rufus 3.10 [extras]
  screentogif 2.24.2 [extras]
  sudo 0.2020.01.26

```

此外对于全局软件的更新和卸载等其它操作，都需要加上 `-g` 选项：

*   `sudo scoop update -g *` - 更新所有软件（且包含全局软件）
*   `sudo scoop uninstall -g <app>` - 卸载全局软件
*   `sudo scoop uninstall -gp <app>` - 卸载全局软件（并删除配置文件）
*   `sudo scoop cleanup -g *` - 删除所有全局软件的旧版本
*   `sudo scoop cleanup -gk *` - 删除所有全局软件的旧版本（并清除安装包包缓存）

### 别名
> ⚠️️ 注意：请在 Powershell 中运行下面的命令
```powershell
# 可用操作
scoop alias add|list|rm [<args>]

## 添加别名，格式：
scoop alias add <name> <command> <description>

# 示例：（注意：必须在 Powershell中运行）
scoop alias add st 'scoop status' '检查更新'
# 检查已添加的别名
scoop alias list -v

Name Command      Summary
---- -------      -------
st   scoop status 检查更新

# 测试已添加的别名 st
scoop st


# 另一个示例：
scoop alias add rm 'scoop uninstall $args[0]' '卸载某 app'
```

### 代理设置
>因为种种原因，有时Scoop会连不上Github，请检查您的代理服务器(比如重启代理软件)。

Scoop 默认使用的是系统代理，如果你想手动指定代理，可以输入下面的命令。需要注意的是只支持 http 协议。

```
scoop config proxy localhost:1080
```

**警告：有些代理软件器http协议使用端口与https协议使用端口并不相同，比如V2ray，配置的时候需要使用正确的端口，有的时候使用系统默认代理设置也是可以的，具体情况具体看待吧。**
![20220712084509](https://fastly.jsdelivr.net/gh/Edge-coordinates/PicBed/imgs_for_blogs/20220712084509.png)

> 设置完可以通过`scoop config proxy`查看。

如果你想取消代理，那么输入下面的命令，这将会恢复使用系统代理。

```
scoop config rm proxy
```
**注：**   
- 手动配置http代理后aria2多线程下载有概率不可使用，求修复方案。。。谢谢！

### 开启多线程下载

使用 Scoop 安装 Aria2 后，Scoop 会自动调用 Aria2 进行多线程加速下载。

```
scoop install aria2
```

使用 `scoop config` 命令可以对 Aria2 进行设置，比如 `scoop config aria2-enabled false` 可以禁止调用 Aria2 下载。以下是与 Aria2 有关的设置选项：

*   `aria2-enabled`: 开启 Aria2 下载，默认`true`
*   `aria2-retry-wait`: 重试等待秒数，默认`2`
*   `aria2-split`: 单任务最大连接数，默认`5`
*   `aria2-max-connection-per-server`: 单服务器最大连接数，默认`5` ，最大`16`
*   `aria2-min-split-size`: 最小文件分片大小，默认`5M`

更详细的见[这里](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-retry-wait)，博主在这里推荐以下优化设置，单任务最大连接数设置为 `32`，单服务器最大连接数设置为 `16`，最小文件分片大小设置为 `1M`

```bash
scoop config aria2-split 32
scoop config aria2-max-connection-per-server 16
scoop config aria2-min-split-size 1M
```

### 利用 aria2 进行断点续传

先看具体示例：

scoop 更新 vscode 时下载到 80% 的时候 失败了（安装时处理方法也一样）。我们需要在提示中找到如下内容：

```bash
'D:\Scoop\Applications\apps\aria2\current\aria2c.exe' --input-file='D:\Scoop\Applications\cache\vscode-portable.txt' 
--user-agent='Scoop/1.0 (+http://scoop.sh/) PowerShell/5.1 (Windows NT 10.0; Win64; x64; Desktop)' 
--allow-overwrite=true --auto-file-renaming=false --retry-wait=2 
--split=5 --max-connection-per-server=5 --min-split-size=5M 
--console-log-level=warn --enable-color=false --no-conf=true 
--follow-metalink=true --metalink-preferred-protocol=https 
--min-tls-version=TLSv1.2 --stop-with-process=15584 --continue
```

我们从上面的信息中提取出下面的命令；若要进行断点续传，只需再次执行下面的命令即可：
```bash
aria2c.exe --input-file='D:\Scoop\Applications\cache\vscode-portable.txt'
```
当提示下载完成后，我们需要再次运行 scoop 对应的 app 更新命令（或安装命令），即可完成 app 更新（或安装）：

```bash
scoop update vscode-portable
```

## 一些使用实例
### 安装和切换JDK、Python的版本
> 转载自[Scoop包管理器的相关技巧和知识](https://www.thisfaner.com/p/scoop/#%E5%AE%89%E8%A3%85%E5%92%8C%E5%88%87%E6%8D%A2jdkpython%E7%9A%84%E7%89%88%E6%9C%AC)，相关内容仅作介绍，一般来说版本管理还是交给专门软件比较好，python可以使用虚拟环境或Anaconda.

这里需要使用`scoop reset`它的作用是：重置一个应用程序来解决冲突。  
命令格式为：`scoop reset <java>[@<version>]`

安装和切换不同的 JDK 版本：
```powershell
PS C:> scoop bucket add java

PS C:> scoop install oraclejdk
Installing 'oraclejdk' (12.0.2-10) [64bit]

PS C:> scoop install zulu6
Installing 'zulu6' (6.18.1.5) [64bit]

PS C:> scoop install openjdk10
Installing 'openjdk10' (10.0.1) [64bit]

PS C:> java -version
openjdk version "10.0.1" 2018-04-17
OpenJDK Runtime Environment (build 10.0.1+10)
OpenJDK 64-Bit Server VM (build 10.0.1+10, mixed mode)

PS C:> scoop reset zulu6
Resetting zulu6 (6.18.1.5).
Linking ~\scoop\apps\zulu6\current => ~\scoop\apps\zulu6\6.18.1.5

PS C:> java -version
openjdk version "1.6.0-99"
OpenJDK Runtime Environment (Zulu 6.18.1.5-win64) (build 1.6.0-99-b99)
OpenJDK 64-Bit Server VM (Zulu 6.18.1.5-win64) (build 23.77-b99, mixed mode)

PS C:> scoop reset oraclejdk

PS C:> java -version
java version "12.0.2" 2019-07-16
Java(TM) SE Runtime Environment (build 12.0.2+10)
Java HotSpot(TM) 64-Bit Server VM (build 12.0.2+10, mixed mode, sharing)
```

安装和切换不同的 Python 版本：
```powershell
scoop bucket add versions # add the 'versions' bucket if you haven't already

scoop install python27 python
python --version # -> Python 3.6.2

# switch to python 2.7.x
scoop reset python27
python --version # -> Python 2.7.13

# switch back (to 3.x)
scoop reset python
python --version # -> Python 3.6.2
```



## 常用命令总结


emm想要记住上文那么多的知识有些困难，这里总结一下 Scoop 在日常使用中常用的命令：

```powershell
# 更新 scoop 及软件包列表
scoop update

## 安装软件 ##
# 非全局安装（并禁止安装包缓存）
scoop install -k <app>
# 全局安装（并禁止安装包缓存）
sudo scoop install -gk <app>

## 卸载软件 ##
# 卸载非全局软件（并删除配置文件）
scoop uninstall -p <app>
# 卸载全局软件（并删除配置文件）
sudo scoop uninstall -gp <app>

## 更新软件 ##
# 更新所有非全局软件（并禁止安装包缓存）
scoop update -k *
# 更新所有软件（并禁止安装包缓存）
sudo scoop update -gk *

## 垃圾清理 ##
# 删除所有旧版本非全局软件（并删除软件包缓存）
scoop cleanup -k *
# 删除所有旧版本软件（并删除软件包缓存）
sudo scoop cleanup -gk *
# 清除软件包缓存
scoop cache rm *

```

## 尾巴

文章仍有许多不足之处，希望大家可以指出，如有疑问，请大家在评论区中提出，也请看到的人积极回答，我将尽力解答并收集问题以完善文章。

## 遗留的问题
### 网络问题
#### fatal: unable to access 'https://github.com/lukesampson/scoop-extras/': OpenSSL SSL_read: Connection was reset, errno 10054
```powershell
fatal: unable to access 'https://github.com/lukesampson/scoop/': OpenSSL SSL_read: Connection was reset, errno 10054
Update failed.
fatal: unable to access 'https://github.com/lukesampson/scoop-extras/': OpenSSL SSL_read: Connection was reset, errno 10054
```
遇到这种情况请**检查代理**，参考[代理设置](#代理设置)

#### 手动配置http代理后aria2多线程下载不可使用
如题，求解决方案，如果有大佬知道可以分享在评论区，谢谢~


### 安装软件失败
#### 网络问题导致app安装失败
step1:**检查代理**,下载7zip,aria2失败需要开代理，可以直接将代理软件设为全局，也可以自己配置。  
step2:**手动下载安装文件**  
一个实例：
```
ERROR Download failed! (Error 1) An unknown error occurred
ERROR https://mediaarea.net/download/binary/mediainfo/19.09/MediaInfo_CLI_19.09_Windows_x64.zip
    referer=https://mediaarea.net/download/binary/mediainfo/19.09/
    dir=D:\Scoop\Applications\cache
    out=mediainfo#19.09#https_mediaarea.net_download_binary_mediainfo_19.09_MediaInfo_CLI_19.09_Windows_x64.zip

ERROR & 'D:\Scoop\Applications\apps\aria2\current\aria2c.exe' --input-file='D:\Scoop\Applications\cache\mediainfo.txt'
```
我们可以发现文件的下载路径和下载后的文件名称，这里 `out=` 后面的压缩包就是下载后 文件的名称，(也可以在 scoop 的 `cache` 目录下的 `mediainfo.txt` 文件中找到下载路径与文 件名称)

然后我们可以尝试在浏览器或其他下载程序中（可以 fq 的程序中）下载该程序，下载完成 后再更改文件名并将其放入 scoop 的 `cache` 目录，最后再次运行 `scoop install mediainfo` 即可安装。

#### 其它问题导致安装失败
![scoop安装软件失败](https://fastly.jsdelivr.net/gh/Edge-coordinates/PicBed/imgs_for_blogs/scoop安装软件失败.png)
下载其他软件失败看看你有没有装某些软件，如sudo(用于全局安装的，导致某些语法无法使用，详见前文说的全局安装),反正我吧sudo删掉就好了~

#### Scoop安装软件失败的原因分类
1. 未及时更新仓库
2. 连不上Github，因为众所周知的原因，解决方案的话可以参考代理设置中的重启/更换代理（参考：[代理设置](#代理设置)），还不可以的话可以尝试在浏览器中打开Github，然后再尝试。

### 更新失败
```powershell
Updating 'adb' (33.0.2 -> 33.0.3)
Downloading new version
无法从传输连接中读取数据: 远程主机强迫关闭了一个现有的连接。。
所在位置 C:\Scoop\apps\scoop\current\lib\install.ps1:111 字符: 9
+         throw $e
+         ~~~~~~~~
    + CategoryInfo          : OperationStopped: (:) [], IOException
    + FullyQualifiedErrorId : 无法从传输连接中读取数据: 远程主机强迫关闭了一个现有的连接。。
```
上面是报错的命令行提示，在使用Scoop升级的时候出现了这样的错误是让人悲伤的，这个错误经常在使用`scoop update *`到时候被引发，因为只要有一个维护者没有跟上最新版本就会导致报错(详见[[Feature Request] Offer a flag to skip installs/updates that failed to download](https://github.com/ScoopInstaller/Scoop/issues/5063))，所以可以跳过报错的应用，更新别的应用吧~

--------
>参考资料  
>[Scoop Documentation](https://github.com/lukesampson/scoop/wiki)  
>[再谈谈 Scoop 这个 Windows 下的软件包管理器](https://chawyehsu.com/blog/talk-about-scoop-the-package-manager-for-windows-again)  
>[「一行代码」搞定软件安装卸载，用 Scoop 管理你的 Windows 软件](https://sspai.com/post/52496)  
>[Scoop - 最好用的 Windows 包管理器](https://p3terx.com/archives/scoop-the-best-windows-package-manager.html)  
>[scoop的安装及基本使用](https://www.cnblogs.com/lioa/p/13565622.html)  
>[你需要掌握的Scoop技巧和知识](https://zhuanlan.zhihu.com/p/135278662)  
