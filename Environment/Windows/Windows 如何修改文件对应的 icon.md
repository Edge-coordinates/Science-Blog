---
title: Windows 如何修改文件对应的 icon
date: 2026/02/11 23:57:21
categories:
  - - Environment
    - Windows
abbrlink: 2a18929
---
# Windows 如何修改文件对应的 icon

吾辈设置的PDF文件查看器是okular，然而其图标作为pdf文件的图标的话着实不敢恭维。

尝试了各种方法去修改Windows上文件默认的图标，都没有一个好的成效，FileTypesMan 或者 Default Programs Editor 根本不起作用，检查注册表之后对于他们为什么不工作我可能有一些见解，然而也不能确定。

## PDF 的例子

总之，以PDF为例子，展示最新的`Windows 11`要如何修改文件类型关联的icon吧。(OS Version: Windows 11 Pro for Workstations 25H2 26200.7623)

文件类型相关的注册表在`Computer\HKEY_CLASSES_ROOT\`，本文说的是pdf,位置就是`Computer\HKEY_CLASSES_ROOT\.pdf`。

然后吾辈的电脑上，该目录下有如下Value and key:

```yml
.pdf
    - (Default): pdf_auto_file
    - Content Type: application
    - OpenWithProgids
        - (Default): value not set
        - ChromeHTML: blank
        - MSEdgePDF: blank
    - PersistentHandler
    - ShellEx
```

为什么那些程序不工作呢？我怀疑`OpenWithProgids`key发力了，虽然不知道为什么ChromeHTML在前面但是识别到了MSEdgePDF，而后我觉得修改icon的程序大概是直接去查看了`Computer\HKEY_CLASSES_ROOT\MSEdgePDF`相关值，所以读取了错误的信息以及错误的icon?

实际上，我们应该处理`Computer\HKEY_CLASSES_ROOT\pdf_auto_file\`，吾辈觉得是因为`.pdf`的`(Default)`Value，的值是`pdf_auto_file`

总之，吾辈`Computer\HKEY_CLASSES_ROOT\pdf_auto_file`目录下有一个shell key，不用管他，然而如果你想要查看的话大概会发现你指定的默认程序的路径。

我们New一个key，叫做`DefaultIcon`，最终目录就是`Computer\HKEY_CLASSES_ROOT\pdf_auto_file\DefaultIcon`，然后修改`(Default)`value到你想要指定的ico，比如吾辈选择的就是`D:\config\icon\pdf\applicationpdf_103614.ico`

以上。

## 总结

吾辈查找能够方便的修改的程序，然而怎么都找不到，有在考虑要不要自己开发一个呢？