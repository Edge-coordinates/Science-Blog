---
title: NVIDIA APP 登陆后跳转到国区问题
date: 2024/11/17 0:8:15
categories:
  - - Environment
abbrlink: 595023aa
---
# NVIDIA APP 登陆后跳转到国区问题

中所周知,NVIDIA更新了其GeForce Experience，改成了更统一并且功能更强大的`NVIDIA APP`，但是，哪怕我开着代理的情况下，只要点击登录，就会跳到国区，并且没法改区，非常让人不爽啊，查了一下代理的记录，似乎和nvidia相关域名没有被代理有关，于是，因为上次代理adoble相关域名的经验，吾辈做出了如下尝试：

在全局扩展脚本中做如下配置：
```bash
  "DOMAIN-KEYWORD,nvidia,🚀 节点选择",
```
完整文档：
```js
// Define main function (script entry)

const rulesPro = [
  "DOMAIN-SUFFIX,adobestats.io,REJECT",
  "DOMAIN-SUFFIX,adobe.io,REJECT",
  "DOMAIN-SUFFIX,registeridm.com,REJECT",
  "DOMAIN-SUFFIX,internetdownloadmanager.com,REJECT",
  "DOMAIN-KEYWORD,nvidia,🚀 节点选择",
]

function main(config, profileName) {
  config["rules"] = rulesPro.concat(config["rules"])
  return config;
}

```

不过呢，单单是做这样的配置是没用的，似乎是缓存的原因？点击登录还是会跳转到.cn 
设置存储目录：
```bash
C:\Users\%USERNAME%\AppData\Local\NVIDIA Corporation

经过软件删除测试，软件删除后该目录会留有
GfnRuntimeSdk
FrameViewSDK
文件夹
```
本人是直接使用 IObit Uninstaller 对软件进行了删除和重装（不会破坏驱动）
在上一次记录中，直接这样操作可行，不过本次记录中，这样做失败了（依然.cn）。
```bash
删除重装，tun全局代理，登录就是海外登录了
```

区别是没有启用tun模式，明天我们删配置，然后用tun试一下好吧。  
（不过干啊，tun和我们学校网络不兼容QAQ）

## 别的问题
### NVIDIA自定义用户名

https://profile.nvgs.nvidia.com/profile  

进入这个网址，选择繁体中文就可以更新

账户网页：https://www.nvidia.com/zh-tw/account/