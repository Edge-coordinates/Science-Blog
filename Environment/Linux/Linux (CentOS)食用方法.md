---
title: Linux (CentOS)食用方法
categories:
- Linux
tags:
---


<!-- TOC -->

- [教程](#教程)
- [配置 CentOS8 环境](#配置-centos8-环境)
  - [安装](#安装)
  - [问题](#问题)
      - [怎样配置yum源](#怎样配置yum源)
      - [怎样打开**root**权限](#怎样打开root权限)
      - [VmWare 15 设置Centos7 共享文件夹及问题记录](#vmware-15-设置centos7-共享文件夹及问题记录)
      - [中文打不开shell](#中文打不开shell)
      - [centos怎么设置快捷键启动终端](#centos怎么设置快捷键启动终端)
      - [安装中文输入法](#安装中文输入法)
- [配置编程环境](#配置编程环境)
  - [配置 VScode](#配置-vscode)
  - [配置 GDB](#配置-gdb)
  - [配置 vim](#配置-vim)

<!-- /TOC -->
# 教程

1. [菜鸟教程-Linux 教程](https://www.runoob.com/linux/linux-tutorial.html)
2. [Linux 系列教程-by YSOcean](https://www.cnblogs.com/ysocean/tag/Linux%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B/)

# 配置 CentOS8 环境

## 安装

1. **这里用的是 VM** 
[虚拟机上安装 centos8](https://www.cnblogs.com/wzb0228/p/12653104.html)
[虚拟机上安装 centos8.0(服务器)](https://www.cnblogs.com/fanzhenyong/p/11616192.html)

2. 购买云服务器 见菜鸟教程

## 问题
#### 怎样配置yum源

#### 怎样打开**root**权限 
1. 永久: 打开shell，输入
```
su root
密码
```
#### [VmWare 15 设置Centos7 共享文件夹及问题记录](https://www.cnblogs.com/skyheaving/p/12286513.html)

#### 中文打不开shell
需要在安装时选择中文，不然必须用英文。。。
[中文安装教程](https://blog.csdn.net/renfeigui0/article/details/102543039)  ~~好像没啥用?~~

#### [centos怎么设置快捷键启动终端](https://jingyan.baidu.com/article/14bd256e16e224fa6c26121e.html)

#### 安装中文输入法
[CentOS7中安装中文输入法](https://blog.csdn.net/qq_38880380/article/details/79013365)
**注意，安装后需退出重新登录才可生效**

# 配置编程环境
**注意：多数安装都要root权限**
[编程环境配置(VScode,Vim等)](https://www.cnblogs.com/Edge-coordinates/p/13960431.html)

## 配置 VScode
- [下载](https://code.visualstudio.com/Download).rpm文件
- 安装参见[Linux rpm文件安装指南](https://blog.csdn.net/neohuo/article/details/600339)
- 配置参见[编程环境配置(VScode,Vim等)](https://www.cnblogs.com/Edge-coordinates/p/13960431.html)

## 配置 GDB
1. 下载
```cpp
yum -y install gcc
yum -y install gdb
yum -y install g++
```

[在 CentOS 7 中使用 VS Code 编译调试 C++项目](https://www.cnblogs.com/lenmom/p/9193388.html)


## 配置 vim
- 下载vim
```
yum -y install vim
```
[Centos 下安装 VIM 编辑器](https://www.cnblogs.com/duanwandao/p/9947881.html)

- 配置vim 
1. [编程环境配置(VScode,Vim等)](https://www.cnblogs.com/Edge-coordinates/p/13960431.html)
2. [Vim的终极配置方案，完美的写代码界面! ——.vimrc](https://blog.csdn.net/amoscykl/article/details/80616688)

