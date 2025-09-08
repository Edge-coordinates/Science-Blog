---
title: Pyinstaller打包python程序(单程序，多程序均可)教程
date: 2022/10/14
categories:
  - - Language
    - Python
tags: null
abbrlink: 4a00808d
---


# Pyinstaller打包python程序(单程序，多程序均可)教程
- [Pyinstaller打包python程序(单程序，多程序均可)教程](#pyinstaller打包python程序单程序多程序均可教程)
  - [前言](#前言)
  - [安装Pyinstaller](#安装pyinstaller)
  - [pyinstaller打包机制](#pyinstaller打包机制)
  - [打包方法](#打包方法)
    - [直接使用命令](#直接使用命令)
    - [使用spec](#使用spec)
    - [压缩](#压缩)
  - [问题](#问题)
  - [参考](#参考)
## 前言
这篇文章将介绍如何安装并使用pyinstaller打包python程序(单个程序和多个程序均会教)

## 安装Pyinstaller
使用命令`pip install pyinstaller`一键安装(记得把代理关掉如果有的话)

## pyinstaller打包机制
我也不是很了解，这里结合使用经验和网上的教程，如有错误/不妥指出，请指出，必将改正，谢谢。  
Python是解释型语言，我们写的python文件不可以脱离python解释器独立运行，所以打包时，必须要打包python解释器、使用到的第三方库和脚本。  
这里要注意，即使我们的项目只用了一两个库，但因为库之间的依赖关系，打包时需要全部打包。(一般情况默认就可以了)  
打包的简单原理，pyinstaller 此时会生成相应的 spec 文件，大体流程如下：
1. 在脚本目录生成 xxx.spec 文件 (取决于 -n 参数，没传，则与 xxx.py 同名为 xxx)；
2. 创建一个 build 目录；
3. 写入一些日志文件和中间流程文件到 build 目录；
4. 创建 dist 目录；
5. 生成可执行文件或文件夹到 dist 目录；

## 打包方法
### 直接使用命令
```shell
pyinstaller [主文件] -p [其他文件1] -p [其他文件2] 
--hidden-import [自建模块1] 
--hidden-import [自建模块2]
# 以上为一整条命令
```
比如我的命令即为`pyinstaller -F -w -i ship.ico set_up.py`，里面有些参数看不懂没关系，后面会讲解，我没有使用到`-p`,`--hidden-import`之类的参数，~~其实是我不知道它们要怎么用~~，但这种最普通的打包方式对于单个文件或多文件均适用。
在打包完之后，要将你的依赖文件(非依赖库)放到相对于可执行文件的相对位置，如果你在.py文件使用的是相对位置的话，建议将依赖文件直接复制到可执行文件所在的目录下。  

命令列表解析：

| 简写 | 完整版 | 注释 |  
| --- | --- | --- |  
| 无 | --clean |清理编译文件|
| -F | –onefile | 打包成一个exe文件|
| -D | –onedir |创建一个目录，包含exe文件，但会依赖很多文件（默认选项）。
| -c | –console, –nowindowed | 使用控制台，无界面(默认)
| -w | –windowed, –noconsole | 使用窗口，无控制台
| -p | 无 | 后面紧跟着你要指定的模块搜索路径，如果你的模块安装的路径没有被PyInstaller自动检索到的话，就需要自己指定了。
| 无 | --hidden-import | 打包指定模块，可以多次使用 |
| 无 | --add-data file | 打包指定文件，可以多次使用 |


几中命令形式总结：
```

文件夹-无命令行窗口：
pyinstaller -w -D --icon="./src/image/app.ico" run.py --clean

压缩有问题
pyinstaller -w -D --icon="./src/image/app.ico" --upx="D:/Program Files/upx-3.95-win64/upx.exe" run.py

单文件打包-无命令行窗口：
pyinstaller -w -F --icon=./src/image/app.ico run.py

调试：
pyinstaller  --icon=./src/image/app.ico run.py

单文件打包-有命令行窗口：
pyinstaller -F --icon=./src/image/app.ico run.py
```

### 使用spec
这部分我不会，看了一个大佬的博客，也没有搞懂[pyinstaller 打包 python 程序（多文件）](https://www.cnblogs.com/ronyjay/p/12713078.html)

### 压缩
[下载地址](https://upx.github.io)  
用法：
```shell
pyinstaller -F proxyWindow.spec --upx upx路径
pyinstaller -F proxyWindow.spec --upx=D:\Program Files\upx-3.95-win64
```

## 问题
- Q:`TypeError: expected str, bytes or os.PathLike object, not _io.BytesIO`之类  
A:详见[PyInstaller + pygame default font #2603](https://github.com/pygame/pygame/issues/2603),目前，我认为最好的解决方案是不适用默认字体，将字体设置为自己的字体:pygame的话是这么用的`font = pygame.font.Font(your_font_file, size)`，`your_font_file`放文件目录，最好没中文，注意是`pygame.font.Font`而不是`pygame.font.SysFont`。  
- Q：no modle named "PyQt5.sip"  
A： pyinstaller -F -I manage.ico yourpyfile.py --hidden-import PyQt5.sip

- Q: 此时如果直接尝试打包好像能打包成功，但是应用程序会闪退。原因是pyinstaller无法判断pyqt动态链接库的位置。  
A: 解决方法：在打包时指明pyqt动态链接库的位置。切换到要打包的.py文件所在的目录，在此路径打开命令行输入(到时候以你自己的路径来定)：
`pyinstaller --paths "D:\Program Files (x86)\Python35-32\Lib\site-packages\PyQt5\Qt\bin" test.py`

## 参考
> [pyinstaller 打包 exe 程序步骤和添加依赖文件方法](https://blog.csdn.net/weixin_42409884/article/details/109293327)
> [pyinstaller深入使用，打包指定模块，打包静态文件 ](https://www.cnblogs.com/jackadam/p/10342627.html)
> [Python（Pygame）字体设置](https://blog.csdn.net/zengxiantao1994/article/details/58590594)