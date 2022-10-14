---
title: 解决VScode的一些问题
date: 2022/10/14
categories:
  - Configure
tags:
  - VSCode
abbrlink: 6ed64ad2
---


<!-- TOC -->

- [GDB中文文件名，路径调试问题](#gdb中文文件名路径调试问题)
  - [配置配置文件](#配置配置文件)
    - [tasks.json](#tasksjson)
    - [launch.json](#launchjson)
  - [总结：](#总结)
- [VScode中启动的控制台闪退](#vscode中启动的控制台闪退)
  - [方案一](#方案一)
- [VSCode输出框中文乱码问题](#vscode输出框中文乱码问题)
  - [Markdown预览格式错误](#markdown预览格式错误)

<!-- /TOC -->

# GDB中文文件名，路径调试问题

TAGS GDB;C++;Chinese 

## 配置配置文件  
### tasks.json
``` json
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe build active file",
            "command": "C:\\MinGW\\bin\\g++.exe",
            "args": [
                "-g",
                "${file}",
                "-o",
                // "${fileDirname}\\${fileBasenameNoExtension}.exe" 生成一个与源文件文件名相同的.exe文件
                "${fileDirname}\\a.exe" //统一生成为a.exe
            ],
            "options": {
                "cwd": "C:\\MinGW\\bin"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Generated task by Debugger"
        },
    ],
    "version": "2.0.0"
}
```
### launch.json
``` json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++.exe - 生成和调试活动文件",
            "type": "cppdbg",
            "request": "launch",
            // "program": "C:\\Windows\\system32\\cmd.exe", 
            // "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "program": "${fileDirname}\\a.exe",//调用tasks.json中生成的文件
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "C:\\MinGW\\bin\\gdb.exe",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            //"preLaunchTask": "c/cpp task"
            "preLaunchTask": "C/C++: g++.exe build active file"
        }
    ]
}
```

> 参考文章链接：[真正解决VScode C\C++中文名无法运行问题](https://blog.csdn.net/qq_51380768/article/details/111479548) 
  
评论区【zhaoxf4】说“思路不错，不过要注意tasks.json下的"type"的值应当是"shell"，如果填成"cppbuild"，仍然会生成原来文件名的.exe文件”  
吾辈并未作更改，是可以编译中文文件名的，所以。。。

## 总结：
1. 找到问题所在：GDB可以编译但无法调试。
2. 尝试解决： 使GDB编译生成的文件为英文名
3. 测试方案可行性
运用到了JSON的相关知识，本身难度不大。


# VScode中启动的控制台闪退

TAGS C++;VScode

## 方案一
在 launch.json 加入如下代码
``` json
    {
        "name": "(Windows) Launch",
        "type": "cppvsdbg",
        "request": "launch",
        "program": "C:\\Windows\\system32\\cmd.exe",
        "args": [
            "/C",
            "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "&",
            "pause"
        ],
        "stopAtEntry": false,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": true
    }
```


# [VSCode输出框中文乱码问题](https://blog.csdn.net/a19990412/article/details/90270814)  

TAGS Chinese

总结：添加系统全局变量 PYTHONIOENCODING，值设置为 UTF8 然后再重启 VSCode 就好了。


## Markdown预览格式错误


