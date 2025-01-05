---
title: 0102 动画杂谈
date: '2025/1/5 14:18:19'
categories:
  - - 踩坑指北
    - NetWork
abbrlink: bc98bbfc
---

# 代理导致GenP破解Adobe失效

Date: October 7, 2024 7:15 PM (GMT+8)
Published: Yes

当开启代理软件后，GenP设置的系统的路由拦截，比如host拦截会失效（会被代理软件代理从而绕过规则）

从而导致**POPUPS问题**，该问题在[**GenpWIKI**](https://www.reddit.com/r/GenP/wiki/redditgenpguides/)文章中搜索*UNLICENSED POPUPS / ACCEPT TERMS POPUP 可以找到描述。*

也就是弹出未授权许可之类的红色弹窗

为了解决该问题，需要在代理软件中配置规则，本人使用的是 clash-verge-rev，采用了自定义**Script配置**的方案，参考文档：

https://www.clashverge.dev/guide/script.html

如果您是新版本，请在全局拓展脚本处设置，本人代码如下：

```jsx
// Define main function (script entry)

const rulesPro = [
  "DOMAIN-SUFFIX,adobestats.io,REJECT",
  "DOMAIN-SUFFIX,adobe.io,REJECT"
]

function main(config, profileName) {
  config["rules"] = rulesPro.concat(config["rules"])
  return config;
}
```

您也可以针对各个配置文件单独设置**Merge配置**，参考文档：https://www.clashverge.dev/guide/merge.html ，请注意：

> `v1.7.x` 版本的 `Merge配置` 改名为 `扩展配置` ，且prepend/append功能移动至订阅右键菜单中的可视化编辑器中实现（例如：prepend-rules移动至订阅右键菜单的 `编辑规则` 中的 `prepend`）。扩展配置仅用于配置项覆写/合并

### 几个小问题/踩坑指北

- 吾辈一开始将rulesPro添加到旧的rules后面，然后发现它并不会生效，虽然可以在规则搜索中搜到，但是不会执行
- 上方那个Quote吾辈一开始没看到，在全局拓展配置中写Merge配置，完全无效
- 同时，直接在全局拓展配置中配置rules的话，似乎会让配置文件中的rules无效，而不是将配置文件中的rules合并进来。
- 如果您想要有针对性的屏蔽验证会用到的域名，可以参考https://github.com/ignaciocastro/a-dove-is-dumb 项目，一个Clash配置示例如下：https://cdn.jsdelivr.net/gh/ignaciocastro/a-dove-is-dumb@latest/clash.yaml