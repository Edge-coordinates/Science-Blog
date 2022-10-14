---
title: 优雅的在Windows中调试C++程序
categories:
  - C++
tags:
  - Debug
abbrlink: fd01dc7a
---


## 开始：

## 一：搭建环境：

按 Windows + R 打开运行 ，输入 cmd 即可打开 cmd
进入 cmd 命令提示行，输入再回车即可使用调试：
PATH=Dev-Cpp 安装路径\Dev-Cpp\MinGW64\bin;%PATH%

当然，这是一次性的方法，不是很方便，可以直接在系统属性的环境变量中加入路径
详见： 1. [如何在 win10 中设置环境变量](https://baijiahao.baidu.com/s?id=1652502091402613426&wfr=spider&for=pc) 2.[怎么在 CMD 下直接运行 G++编译源代码](https://zhidao.baidu.com/question/488013928.html)
二：cmd 的使用（简单的)

```cpp
cmd（打开） exit（关闭）
cd{后加
	1.\文件夹名
	2. ..(后退一个文件夹)
	3.文件名（前进打开文件）
}
type 打印
dir 列出
del 删除
```

> 该文原地址：https://blog.csdn.net/qq_45718756/article/details/103102160
> **本人已换博客，原地址弃用。**
