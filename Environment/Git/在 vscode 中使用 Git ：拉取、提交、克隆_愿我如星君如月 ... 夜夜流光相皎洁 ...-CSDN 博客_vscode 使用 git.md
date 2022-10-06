---
title: 在 vscode 中使用 Git ：拉取、提交、克隆_愿我如星君如月 ... 夜夜流光相皎洁 ...-CSDN 博客_vscode 使用 git
categories:
- Git
tags:
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/jiangyu1013/article/details/84031418)

[前些天发现了一个巨牛的人工智能学习网站，通俗易懂，风趣幽默，忍不住分享一下给大家。点击跳转到教程。](https://www.captainai.net/jiangyu1013/)

**PS：转载此文后，网友在评论中提到还有其它方法，不过目前个人尚在研究中，有兴趣的朋友们也可自行一探究竟 ...**

-------------------------------------------------------------------------

1、将代码放到码云

*   到码云里新建一个仓库，完成后码云会有一个命令教程按上面的来就行了
*   码云中的使用教程：

```
Git 全局设置:
 
git config --global user.name "ASxx" 
git config --global user.email "123456789@qq.com"
 
创建 git 仓库:
 
mkdir wap // 项目在本地的路径
cd wap
git init 
touch README.md 
git add README.md 
git commit -m "first commit" 
git remote add origin https://git.oschina.net/name/package.git  // 远程仓库地址
git push -u origin master
 
 
 
已有项目：
 
cd existing_git_repo
git remote add origin https://git.oschina.net/name/package.git
git push -u origin master
```

**下面说下详细的本地操作步骤：**

*   **1、用 vs 打开你的项目文件夹**

**![](https://img-blog.csdnimg.cn/img_convert/25448f25c7d0bb5949b598f7b52995cb.png)**

*   **2、配置 git**

 打开 Git Bash 输入以下命令

　　如果还没输入全局配置就先把这个全局配置输入上去

```
Git 全局设置:
 
git config --global user.name "ASxx" 
git config --global user.email "123456789@qq.com"
```

　　然后开始做提交代码到码云的配置

```
cd d:/wamp/www/mall360/wap //首先指定到你的项目目录下
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://git.oschina.net/name/package.git   //用你仓库的url
git push -u origin master  //提交到你的仓库
```

```
git config --global user.name "ASxx"
git config --global user.email "123456789@qq.com"  
 
git config --global credential.helper store   
 
 
 
#然后打开Git Bash输入以下命令
 
cd d:/test   //指定存放的目录
git clone https://git.oschina.net/name/test.git   //你的仓库地址
```

*   **3、在 vscode 中提交代码到仓库**

　　回到 VSCode 打开 git 工作区 （就是 直接 VSCode 中 file -> open 项目所在文件夹），就会看到所有代码显示在这里

![](https://img-blog.csdnimg.cn/img_convert/80ed1e7c5614033270a8e7ab44ad7e21.png)

点击 + 号，把所有文件提交到暂存区。

然后打开菜单选择 -- 提交已暂存的 (Commit Staged)

![](https://img-blog.csdnimg.cn/img_convert/312ae245f8dda00e4dc15ec9ac55de22.png)

然后按提示随便在消息框里输入一个消息，再按 ctrl + enter 提交

![](https://img-blog.csdnimg.cn/img_convert/9be74378f2059a049bb103014fbd8247.png)

然后把所有暂存的代码 push 云端，

![](https://img-blog.csdnimg.cn/img_convert/66262f148c7b0263b7cc1f29c9d722a3.png)

点击后，会弹出让你输入账号密码，把你托管平台的账号密码输入上去就行了。

不出问题的话你整个项目就会提交到云端上了。

在 vs 中每次更新代码都会要输入账号密码，可以配置一下让 GIT 记住密码账号：

```
git config --global credential.helper store   //在Git Bash输入这个命令就可以了
```

*   **4、同步代码**

 **这里说下平时修改代码后提交到云端的使用，和本地代码和云端同步**

　　随便打开一个文件，添加一个注释

![](https://img-blog.csdnimg.cn/img_convert/773454026d544a71a0dd787c86db4003.png)

可以看到 git 图标有一个提示，打开 git 工作区可以看到就是修改的这个文件

![](https://img-blog.csdnimg.cn/img_convert/ab84d9c7b74d11013897101f1fc39d44.png)

然后点击右侧的 + 号，把他暂存起来。

再在消息框里输入消息，按 ctrl + enter 提交暂存

![](https://img-blog.csdnimg.cn/img_convert/3c9f944ed0886acf6e3ca79b86590611.png)

再点击 push 提交，代码就提交到云端了。

![](https://img-blog.csdnimg.cn/img_convert/682e026c56a20a5fe830206b5d35352c.png)

打开 码云就可以看到了。。

 ![](https://img-blog.csdnimg.cn/img_convert/bfdb4aefe42837bafa993d5649e7f65a.png)

*   pull 使用

　　比如当你在家里修改了代码提交到云端后，回到公司只需要用 vscode 打开项目点击菜单中的 pull 就可以同步过来了。

 ![](https://img-blog.csdnimg.cn/img_convert/4fe0900a4226f115f266b33c62d93195.png)

*   **5、克隆你的项目到本地**

 回到家后想修改代码，但是电脑没有文件怎么办呢？  往下看

　　首先你电脑还是的有 vscode 和  GIT，，然后用 git 把上面那些全局配置再执行一次，如下

```
git config --global user.name "ASxx"
git config --global user.email "123456789@qq.com"  
 
git config --global credential.helper store   
 
 
 
#然后打开Git Bash输入以下命令
 
cd d:/test   //指定存放的目录
git clone https://git.oschina.net/name/test.git   //你的仓库地址
```

![](https://img-blog.csdnimg.cn/img_convert/142de88f99a1d888bbfa996d5b4f82b3.png)

下载成功，然后就可以用 vscode 打开项目修改了。修改后提交的步骤还是和上面一样：暂存 - 提交暂存 - push 提交到云端就 ok 了。