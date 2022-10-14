---
title: 调试 NOI Linux 中的调试
categories:
  - C++
tags:
  - Debug
abbrlink: 8c14664b
---


[TOC]
# 开始
## 搭建环境：
可直接在电脑上装NOI Linux 或 下载 虚拟机（虚拟机推荐VM虽然要钱但**有密钥**，网上一大堆自己搜去。。。）
 

## 终端的使用：
打开你的终端:Ctrl+Alt+T即可打开终端模拟器，来与shell 来一把紧张刺激的交互吧~

### 常用Linux 命令：（注意：Tab键可以自动补全，请多按，省时间！）
1. echo [msg]：直接输出一段信息.
2. cat：输出一个文件的内容 
3. touch：新建一个文件
4. cd：切换目录
5. g++：编译你的代码 例： g++ HellowWorld.cpp （这里注意g++后加空格）
6. 执行程序：./helloworld 执行当前目录下的helloworld 文件。（这里注意 ./ 后请不要加空格）

### 总结
Linux 的路径：从/ 开始的路径。
相对路径
当前目录：**.**
父目录：**..**

## 调试技巧：
### 常见错误
1. 段错误：爆栈、访问非法内存。
```cpp
解决： ulimit -s 2444444
                这里随便加一个大数 （注意：指令只对当前终端有效）
```
2. 浮点数例外：整型除以0 或模0。
```cpp
用
#define DEBUG fprintf(stderr,"Passrd [%s] in LINE %d\n", __FUNCTION__,__LINE__)；
进行调试

```