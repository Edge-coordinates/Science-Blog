---
title: Space Error
date: 2025/09/09 04:37:20
updated: 2025/09/09 04:37:21
categories:
  - - Environment
    - IDE
    - VSCode
---


遇到缩进红色报错的问题

我个人的解决方案是设置`.editorconfig`

```.editorconfig
root = true

[*]
indent_style = space
indent_size = 2
```

这样之后全局运行了一下`dprint fmt`, 对于我来说编辑器右下角的space就顺利换过来了，也就不会导致缩进error红。

如果有个别文件没有换过来，可以考虑打开后切换文件，或者关闭重开来更新缓存。

实在不行就手动设置一下右下角

编辑器右下角的Space并不是全局设置，而是指代当前文件的属性，类似于编码`UTF-8`，所以可以放心配置