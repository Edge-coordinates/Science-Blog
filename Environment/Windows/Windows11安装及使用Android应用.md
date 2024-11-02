---
title: Windows11安装及使用Android应用
date: 2022/10/14
categories:
  - [Environment, Windows]
tags:
  - Windows
abbrlink: 1e7cf617
---


Windows11终于安装Android应用啦！！！！
如遇问题可以在回复区回复，电脑崩溃或者出现奇怪问题均自行负责。
必须是WIN11才可以其他均不能使用，且必须为WIN11最新正式版本。

Windows11安装Android应用
第一步（安装必要程序）
1. 右键开始---运行---control.exe---程序和功能---开启或关闭 Windows 功能---勾选 Hyper-V以及Windows 虚拟机监控平台，成功后，必须重启系统。
2. 安装Window Subsystem for Android应用，直接在Microsoft Store中安装 Amazon Appstore，会自带 Window Subsystem for Android。  
3. 打开Window Subsystem for Android(直接在开始菜单打开，可能是中文名适用于**Android<sup>TM</sup>的Windows子系统设置**)应用开发人员模式


第二步（安装Android应用，必须通过ADB安装）
1. 解压ADB(platform-tools-latest-windows.zip),在解压后的目录右键选择"在Windows终端中打开”
2. 输入”.\adb connect 127.0.0.1:58526“
3. 输入”.\adb install xxx“,安装下载的app。<注意：xxx为文件路径>
4. 在开始菜单可以看到新安装的安卓应用。

## 问题
### **cannot connect to 127.0.0.1:58526: 由于目标计算机积极拒绝，无法连接。 (10061)**
省流
重启系统试试

啰里啰嗦
使用离线方式安装完WSA，启动，开发者模式显示支持本地127.0.0.1:58526调试。  
使用adb connect 127.0.0.1:58526 显示`cannot connect to 127.0.0.1:58526: 由于目标计算机积极拒绝，无法连接。 (10061)  `原因不明，其实是该端口并未 真正 启用，可使用`netstat -anep tcp | findstr "58526"`验证，若未找到记录则实锤🔨。  
我的经验：重启电脑后，再次启动WSA（点开最上方文件管理，曲线启动一个应用），此时刷新出`同一专用网络上的设备可以访问子系统，可以在127.0.0.1:58526上连接ADB。`此时，执行`netstat -anep tcp | findstr "58526"`, 存在记录：`TCP 0.0.0.0:58526 0.0.0.0:0 LISTENING`之后再执行adb连接命令，安装应用即可。  
**介于**我也在**适用于Android<sup>TM</sup>的Windows子系统设置** 的开发人员模式设置中把一些和Wifi有关的设置启用了，如，所以如果上面的方法不能解决问题，请大家尝试更改**适用于Android<sup>TM</sup>的Windows子系统设置**的开发人员模式设置。  
设置更改后也许会有缓冲期，建议等个30s再确定是否是方法存在问题。

### 印象笔记链接扫译笔要链接蓝牙Windows蓝牙已开启但无用。
未解决，如有大佬有解决方案，可以在回复区回复，谢谢。