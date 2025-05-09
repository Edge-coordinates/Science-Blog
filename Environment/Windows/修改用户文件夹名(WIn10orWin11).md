---
title: 修改用户文件夹名(WIn10orWin11)
date: 2022/10/14
categories:
  - [Environment, Windows]
tags:
  - Windows
abbrlink: b2a62941
---


- [需求](#需求)
- [做法](#做法)
- [注意配置有环境变量的同学，记得再去看看配置的环境变量是否正确](#注意配置有环境变量的同学记得再去看看配置的环境变量是否正确)

教程网上一搜一大堆，这里不细述，贴出一个: [Win10更改c盘下的用户文件夹名Bysea1216](https://blog.csdn.net/sea1216/article/details/79278202)以下内容有部分引用自此文章。

## 需求
**c:\user\中文 后来 许多软件因为 不支持 路径中有中文，必须改为c:\user\zhongwen**  
**用在线账户登录，会取邮箱前五个字母，别扭想更换**  

## 做法
下面说下怎么更改 c盘下的用户文件夹名。
1. 首先 要进入管理员账户（Administrator）
   - 桌面上 “此电脑”右击，点击管理，在左边的 “计算机管理”中找到“本地用户组”，点击“本地用户组”-“用户”，在右侧可以看到Administrator用户与当前用户，选中Administrator用户，右键-属性， 将“账户已禁用”前面的√去掉。点击确定。 注销电脑当前用户，就可以看到Administrator管理账号出现了，**可以选Administrator登Windows10**。  
   
    - 切换回原来账户后,请参照步骤一将Administrator禁用。
     
    - Win10怎么以管理员身份运行CMD命令提示符(选修,可不用)  
    我们可以在Windows10系统的开始菜单上，单击鼠标右键，这时候出现的菜单中，我们选择命令提示符（管理员）点击打开这样即可。在命令提示符中输入如下命令后回车：`net user administrator /active:yes`
    完成必要的工作后，请及时注销该账户登录，并且在回到普通账户后再次关闭Administrator账户。具体方法如下：     
      - 再次以管理员身份运行命令提示符  
      - 输入以下命令后回车：`net user administrator /active:no`
                            
2. 重命名 用户文件夹
用管理员账户登录进去后，进入C:下用户文件夹，找到你想要修改的用户文件夹，右击重命名，更改为你想要的名字

3. 修改注册表
Windows键+R打开运行，输入regedit，点击确定打开Windows注册表管理器
依次展开HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Profilelist，在Profilelist下的文件夹对应系统中用户，而文件夹中ProfileImagePath值是指向每个用户文件夹的地址，一个个点击查看，找到 之前用户名用户 的对应所在的ProfileImagePath值。

4. 修改ProfileImagePath的值，将地址改为修改成 后来你改为的文件夹名。与C盘用户 里面你改的文件夹名一致。再次注销，登录进原用户，进入此电脑便可发现 用户文件夹名已经更改。
   
## 注意配置有环境变量的同学，记得再去看看配置的环境变量是否正确

在更改环境变量后，仍会有一些问题，如`C++`文档的图标丢失，建议重装相关软件，如重装`VSCode`。
`IDM`也会出现下载的文件保存路径不对的问题，亦可重装解决。
下载一个注册表修复工具修复一下注册表(可以不做)

**对于以上问题，如有疑问或更好的解决方法(如不重装软件就可解决)，均可在评论区提出~**
谢谢大家。

