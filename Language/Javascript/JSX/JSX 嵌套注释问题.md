---
title: JSX 嵌套注释问题
date: 2026/02/11 23:57:22
categories:
  - - Language
    - Javascript
    - JSX
abbrlink: 480c8559
---
开发中需要面对嵌套注释问题由来已久，向来不知道应该怎么处理这样的问题，现在发现两个解决方案

## “原生”嵌套注释

```
<div>
    {/* This is the outer comment */}
    {
    // {/* The inner comment and surrounding JSX are effectively commented out here */}
    // <SomeComponent prop1="value" />
    // {/* Another inner comment */}
    }
</div>
```

## Nested Comments

[Market Link](https://marketplace.visualstudio.com/items?itemName=philsinatra.nested-comments)

[GitHub Link](https://github.com/philsinatra/NestedCommentsVSCode)

对了，这个插件cursor版本不支持，所以可以阅读[Cursor如何安装离线插件](../../../Environment/IDE/VSCode/Cursor如何安装离线插件.md)



