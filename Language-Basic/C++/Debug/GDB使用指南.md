---
title: GDB使用指南
date: 2022/10/14
categories:
  - - Language-Basic
    - C++
    - Debug
tags:
  - Debug
abbrlink: a9afe229
---


## 调试

```cpp
编译命令： g++ 文件名 -o 编译生成文件名
调试命令： g++ 文件名 -o 编译生成文件名 -g
输入调试命令后打开调试：gdb 运行程序名
{（gdb中命令）
	l ；列出代码
	b ：设置断点（后跟行数）
	d ：清除断点 （后加断点编号）
	r ：运行
	p ：打印（后加变量）
	i ：查看信息（后可加多种东西，如：i b 可查看断点）
	c ：继续
	quit ：退出
}