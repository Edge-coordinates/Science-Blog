---
title: 使用 putty 连接阿里云服务器
date: 2022/10/14
categories:
  - - Net-excerpt
tags: null
reprint: true
abbrlink: 4f2c986b
---


---
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/weixin_41800884/article/details/103148850)

### 1. 下载 PuTTY

1.  进入官网 [点击我跳转](https://www.putty.org/)
2.  点击 here  
    ![](https://img-blog.csdnimg.cn/20191119190425684.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
3.  看自己电脑是多少位选择下载  
    ![](https://img-blog.csdnimg.cn/20191119190445786.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

### 2. 安装

1.  一直点击下一步就行  
    ![](https://img-blog.csdnimg.cn/20191119190530473.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
2.  这里可以选择也可以不选择，这会在创建桌面快捷文件  
    ![](https://img-blog.csdnimg.cn/20191119190542332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
3.  看图注意事项  
    ![](https://img-blog.csdnimg.cn/2019111919060855.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

*   这里也可以用密匙，先去阿里云的网络安全 -> 密钥对 -> 里面就可以创建，然后会提示下载一个密匙. pem，然后做如下操作：
*   在 Putty 目录中有一个 PuTTYgen.exe，点击 Load  
    ![](https://img-blog.csdnimg.cn/20191119193557573.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)![](https://img-blog.csdnimg.cn/20191119193811472.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)  
    ![](https://img-blog.csdnimg.cn/20191119195628731.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
*   使用时还是打开 Putty.exe  
    ![](https://img-blog.csdnimg.cn/20191119195807276.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

4.  最后在出现黑框时会出现这个，点击是就行（这图是我从网上下的，自己因为先点了，所以我第二次登录不会提示）  
    ![](https://img-blog.csdnimg.cn/20191119190626334.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20191119190902727.png)

### 3. 可能出现的错误

在连接时，出现 connection time out，这时因为在云服务器的安全规则没有设置 SSH22 的端口

#### - 错误如图：

![](https://img-blog.csdnimg.cn/20191119193131447.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

#### - 解决如图：

*   点击 安全组  
    ![](https://img-blog.csdnimg.cn/20191119193141219.png)
*   点击快速创建规则  
    ![](https://img-blog.csdnimg.cn/20191119193154432.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
*   开放 22 端口  
    ![](https://img-blog.csdnimg.cn/20191119193206552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)

### 4. 额外

*   偶尔切换到网页隔一段时间，再切回到 putty 会发现无法使用了，这是因为没有重复发包给服务器，导致服务器休眠，在 putty 可以修改，每隔一段时间发给服务器一个包，让服务器不休眠。先把刚刚的信息加载出来  
    ![](https://img-blog.csdnimg.cn/20191210172540419.png)  
    ![](https://img-blog.csdnimg.cn/20191210172549429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTgwMDg4NA==,size_16,color_FFFFFF,t_70)
*   然后再回去刚刚的界面点击保存，下次也不用设置