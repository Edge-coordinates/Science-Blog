---
title: C++ 之 system 函数
date: 2022/10/14
categories:
  - - Net-excerpt
tags: null
reprint: true
abbrlink: 724ebb21
---


---
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/liuweiyuxiang/article/details/51658706)

转载自：[http://www.xuebuyuan.com/2119209.html](http://www.xuebuyuan.com/2119209.html)

**1.windows 操作系统下 system () 函数详解（主要是在 C 语言中的应用）** 

函数名: system

功 能: 发出一个 DOS 命令

用 法: int system(char *command);

system 函数已经被收录在标准 c 库中，可以直接调用

```
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
　　printf("About to spawn command.com and run a DOS command\n");
　　system("dir");
　　return 0;
}
```

又如： system("pause") 可以实现冻结屏幕，便于观察程序的执行结果； system("CLS") 可以实现清屏操作。而调用 color 函数可以改变控制台的前景色和背景，具体参数在下面说明 。 system("color 0A"); 其中 color 后面的 0 是背景色代号，A 是前景色代号。 各颜色[代码](http://www.xuebuyuan.com/ "代码")如 下：

　0 = 黑色 1 = 蓝色 2 = 绿色 3 = 湖蓝色 4 = 红色 5 = 紫色 6 = 黄色 7 = 白色 8 = 灰色 9 = 淡蓝色 A = 淡绿色 B = 淡浅绿色 C = 淡红色 D = 淡紫色 E = 淡黄色 F = 亮白色 system("mkdir F:\hello\world") 可以在 F：盘下建立一个文件夹 hello，在 hello 下面建立一个文件夹 world。

例一：C 语言调用 DOS 命令实现定时关机：  

```
#include<stdio.h>
#include<string.h>
include<stdlib.h>
int print()
{
　　printf(" ╪╪╪╪╪╪╧╧╧╧╧╧╧╧╪╪╪╪╪╪\n");
　　printf("╔═══╧╧ C语言 关机程序 ╧╧═══╗\n");
　　printf("║※1.实现10分钟内的定时关闭计算机 ║\n");
　　printf("║※2.立即关闭计算机 ║\n");
　　printf("║※3.注销计算机 ║\n");
　　printf("║※0.退出系统 ║\n");
　　printf("╚═══════════════════╝\n");
　　return 0;
}
void main()
{
　　system("title C语言关机程序");//设置cmd窗口标题
　　system("mode con cols=48 lines=25");//窗口宽度高度
　　system("color 0B");
　　system("date /T");
　　system("TIME /T");
　　char cmd[20]="shutdown -s -t ";
　　char t[5]="0";
　　print();
　　int c;
　　scanf("%d",&c);
　　getchar();
　　switch(c)
　　{
　　<span style="white-space:pre">	</span>case 1:printf("您想在多少秒后自动关闭计算机？（0~600）\n");scanf("%s",t);system(strcat(cmd,t));break;
　　<span style="white-space:pre">	</span>case 2:system("shutdown -p");break;
　　<span style="white-space:pre">	</span>case 3:system("shutdown -l");break;
　　<span style="white-space:pre">	</span>case 0:break;
　　<span style="white-space:pre">	</span>default:printf("Error!\n");
　　}
　　system("pause");
　　exit(0);
}
```

例二： 用 C 语言删除文件，例如文件的位置是 d:\123.txt

```
//用system（）函数执行windows命令。
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
　　system("del d:\123.txt");
　　return 0;
}
```

【system 函数 是可以调用一些 DOS 命令】  

下面列出常用的 DOS 命令, 都可以用 system 函数调用:

ASSOC 显示或修改文件扩展名关联。

AT 计划在计算机上运行的命令和程序。

ATTRIB 显示或更改文件属性。

BREAK 设置或清除扩展式 CTRL+C 检查。

CACLS 显示或修改文件的访问控制列表 (ACLs)。

CALL 从另一个批处理程序调用这一个。

CD 显示当前目录的名称或将其更改。

CHCP 显示或设置活动代码页数。

CHDIR 显示当前目录的名称或将其更改。

CHKDSK 检查磁盘并显示状态报告。

CHKNTFS 显示或修改启动时间磁盘检查。

CLS 清除屏幕。

CMD 打开另一个 Windows 命令解释程序窗口。

COLOR 设置默认控制台前景和背景颜色。

COMP 比较两个或两套文件的内容。

COMPACT 显示或更改 NTFS 分区上文件的压缩。

CONVERT 将 FAT 卷转换成 NTFS。您不能转换当前驱动器。

COPY 将至少一个文件复制到另一个位置。

DATE 显示或设置日期。

DEL 删除至少一个文件。

DIR 显示一个目录中的文件和子目录。

DISKCOMP 比较两个软盘的内容。

DISKCOPY 将一个软盘的内容复制到另一个软盘。

DOSKEY 编辑命令行、调用 Windows 命令并创建宏。

ECHO 显示消息，或将命令回显打开或关上。

ENDLOCAL 结束批文件中环境更改的本地化。

ERASE 删除至少一个文件。

EXIT 退出 CMD.EXE 程序 (命令解释程序)。

FC 比较两个或两套文件，并显示不同处。

FIND 在文件中搜索文字字符串。

FINDSTR 在文件中搜索字符串。

FOR 为一套文件中的每个文件运行一个指定的命令

FORMAT 格式化磁盘，以便跟 Windows 使用。

FTYPE 显示或修改用于文件扩展名关联的文件类型。

GOTO 将 Windows 命令解释程序指向批处理程序中某个标明的行。

GRAFTABL 启用 Windows 来以图像模式显示扩展字符集。

HELP 提供 Windows 命令的帮助信息。

IF 执行批处理程序中的条件性处理。

LABEL 创建、更改或删除磁盘的卷标。

MD 创建目录。

MKDIR 创建目录。

MODE 配置系统设备。

MORE 一次显示一个结果屏幕。

MOVE 将文件从一个目录移到另一个目录。

PATH 显示或设置可执行文件的搜索路径。

PAUSE 暂停批文件的处理并显示消息。

POPD 还原 PUSHD 保存的当前目录的上一个值。

PRINT 打印文本文件。

PROMPT 更改 Windows 命令提示符。

PUSHD 保存当前目录，然后对其进行更改。

RD 删除目录。

RECOVER 从有问题的磁盘恢复可读信息。

REM 记录批文件或 CONFIG.SYS 中的注释。

REN 重命名文件。

RENAME 重命名文件。

REPLACE 替换文件。

RMDIR 删除目录。

SET 显示、设置或删除 Windows 环境变量。

SETLOCAL 开始批文件中环境更改的本地化。

SHIFT 更换批文件中可替换参数的位置。

SORT 对输入进行分类。

START 启动另一个窗口来运行指定的程序或命令。

SUBST 将路径跟一个驱动器号关联。

TIME 显示或设置系统时间。

TITLE 设置 CMD.EXE 会话的窗口标题。

TREE 以图形模式显示驱动器或路径的目录结构。

TYPE 显示文本文件的内容。

VER 显示 Windows 版本。

VERIFY 告诉 Windows 是否验证文件是否已正确写入磁盘。

VOL 显示磁盘卷标和序列号。

XCOPY 复制文件和目录树。

命令大小写均可。  
**2.Linux 下 system () 函数详解简介（执行 shell 命令）** 相关函数： fork，execve，waitpid，popen 表头文件  #include<stdlib.h> 定义函数  int system(const char * string); 函数说明 system() 会调用 fork() 产生子进程，由子进程来调用 / bin/sh-c string 来执行参数 string 字符串所代表的命令，此命令执行完后随即返回原调用的进程。在调用 system() 期间 SIGCHLD 信号会被暂时搁置，SIGINT 和 SIGQUIT 信号则会被忽略。 返回值 　　如果 fork() 失败 返回 - 1: 出现错误 　　如果 exec() 失败，表示不能执行 Shell, 返回值相当于 Shell 执行了 exit(127) 　　如果执行成功则返回子 Shell 的终止状态 　　如果 system()在调用 / bin/sh 时失败则返回 127，其他失败原因返回 - 1。若参数 string 为空指针 (NULL)，则返回非零值>。如果 system() 调用成功则最后会返回执行 shell 命令后的返回值，但是此返回值也有可能为 system()调用 / bin/sh 失败所返回的 127，因此最好能再检查 errno 来确认执行成功。 附加说明 　　在编写具有 SUID/SGID 权限的程序时请勿使用 system()，system() 会继承环境变量，通过环境变量可能会造成系统安全的问题。 例一：

```
#i nclude<stdlib.h>
main()
{
　　system(“ls -al /etc/passwd /etc/shadow”);
}
```

执行结果： 　　-rw-r--r-- 1 root root 705 Sep 3 13 :52 /etc/passwd 　　-r--------- 1 root root 572 Sep 2 15 :34 /etc/shado 例二：

```
char tmp[];
sprintf(tmp,"/bin/mount -t vfat %s /mnt/usb",dev);
system(tmp);
```

其中 dev 是 / dev/sda1。 **System 与 exec 的区别**  
1、system()和 exec()都可以执行进程外的命令，system 是在原进程上开辟了一个新的进程，但是 exec 是用新进程 (命令) 覆盖了原有的进程　　 2、system() 和 exec() 都有能产生返回值，system 的返回值并不影响原有进程，但是 exec 的返回值影响了原进程