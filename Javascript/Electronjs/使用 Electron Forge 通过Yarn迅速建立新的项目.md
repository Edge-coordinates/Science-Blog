---
title: 使用 Electron Forge 通过Yarn迅速建立新的项目
date: 2024/11/2 23:22:27
categories:
  - [Javascript, Electronjs]
---
# electron-forge

> Electron Forge is a tool for packaging and publishing Electron applications. It unifies Electron's tooling ecosystem into a single extensible interface so that anyone can jump right into making Electron apps.

Forge 始于一个使用了 Webpack 作为打包器的 a ready-to-use template 模板项目。 该项目包含有一个 typescript 配置的示例，并预置了两个便于定制化的配置文件。 Forge 的一些核心模块来自于上层的 Electron 社区（比如electron-packager），因而 Electron 主要维护人员（比如说 Slack）提交的 Electron 更新也会使 Forge 的用户受益。

那么，让我们开始。

官网的文档写的很完善，直接看吧[electronforge.io](https://www.electronforge.io/)

## 总结

很简单，一共两部开始工作
```bash
yarn create electron-app my-app
```
其中的`my-app`就是即将新建的文件夹的名称，去一个自己喜欢的名字吧。

```bash
cd my-app
yarn start
```

ok，这就启动了一个程序界面，但是它会默认打开开发者面板，建议自行阅读my-app文件夹中`app.js`内容并根据需求选择注释掉相关内容。
