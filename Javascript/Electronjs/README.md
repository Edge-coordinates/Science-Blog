---
title: README
date: 2024/11/2 23:22:27
categories:
  - [Javascript, Electronjs]
---
# Electron 学习笔记

## 启用Nodejs环境

```js
const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration:true,
      contextIsolation:false,
    },
  });
  ```