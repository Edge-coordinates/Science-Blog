---
title: Cursor如何安装离线插件
date: 2026/02/11 23:57:22
categories:
  - - Environment
    - IDE
    - VSCode
abbrlink: 377425ec
---
# Cursor or VSCode 如何安装离线插件

有时候网络受限比如公司内网封锁外部市场，有时候Cursor市场并不包含想要安装的软件o((>ω< ))o。  
不管原因是什么，只要能拿到 `.vsix` 文件，Cursor 就可以离线安装扩展。

Cursor 本质上基于 VS Code 内核，所以它的扩展机制完全兼容 VS Code 的 `.vsix` 包格式。这意味着：**只要是标准 VS Code 扩展，理论上都可以离线装进 Cursor。**

下面让吾辈从VSIX是什么开始讲起。


## 什么是 VSIX？

VS Code 扩展的本质是一个打包文件，后缀名叫 `.vsix`，可以理解为“插件的安装压缩包”。

它内部包含：

- extension manifest（package.json）
- 插件源码
- 依赖声明
- 图标与资源文件

只要拥有这个文件，就不需要在线访问扩展市场。

So now we need to find a way to get a .visx file.

## 获取 `.vsix` 文件的方法

### 从扩展市场下载

官方文档

> Some users prefer to download an extension once from the Marketplace and then install it to multiple VS Code instances from a local share. This is useful when there are connectivity concerns or if your development team wants to use a fixed set of extensions.
> 
> To download an extension, search for it in the Extensions view, right-click on an extension from the results, and select Download VSIX or Download Specific Version VSIX.

例如： [Nested Comments](https://marketplace.visualstudio.com/items?itemName=philsinatra.nested-comments)

> 事实上，Nested Comments就是吾辈写这一篇Blog的理由

- 使用可以访问网路的VSCode搜索Nested Comments。
- 右击搜索结果就可以看到Download VSIX
- 点击后就可以选一个位置保存`.vsix` 文件啦。


### 使用 Open VSX

很多开源扩展可以在 Open VSX 上找到： [https://open-vsx.org](https://open-vsx.org)

搜索插件 then 下载对应版本 `.vsix`

### 使用命令行工具下载

CLI的话可以使用 `vsce`，吾辈未进行测试。

```bash
npm install -g @vscode/vsce
vsce package
```


## 在 Cursor 中安装 VSIX

现在来到需要安装离线包的机器，打开 Cursor。

`Ctrl` + `Shift` +  `P` 打开指令输入行，然后搜索`Install from VSIX`，之后根据提示一步一步来就可以啦。

实际上，吾辈习惯于 `Ctrl` +  `P` 然后手动输入 `>` 进入指令输入模式

之后搜索的时候，输入`install v` 一般就会出来想要的指令啦。


## 可能的问题

- 插件版本是否兼容？Cursor 使用特定版本的 VS Code 内核。如果扩展声明了最低 VS Code 版本要求，可能会出现不兼容情况。  

> 实际上吾辈之前遇到过类似的问题，就是`prettier`在cursor里出现了错误，具体什么问题吾辈也记不得了，总之，降一个版本（prettier）之后就能正常工作啦。

- 有些插件会依赖其他扩展，根据报错提示一并下载对应的 `.vsix`。

- 依赖在线API的插件自然不能再离网条件下运行，emm，不过这种其实比较少见。

## 手动放入扩展目录

如果想更底层操作，可以手动放入扩展目录。

Windows 通常在：

```
%USERPROFILE%\.cursor\extensions
```

## 总结

离线安装 Cursor or VSCode 插件的核心逻辑如下

> 拿到 `.vsix`，然后 `Ctrl` + `Shift` + `P` search Install from VSIX。