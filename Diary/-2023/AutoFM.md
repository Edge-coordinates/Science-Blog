---
title: AutoFM
date: 2022/10/14
categories:
  - - Diary
    - "-2023"
tags: null
abbrlink: 2d05a2ab
---

- [AutoFM](#autofm)
  - [Explain](#explain)
- [Old Python Version](#old-python-version)
  - [功能](#功能)
  - [代码](#代码)

# AutoFM

将本地库链接到pnpm（global）

```powershell
pnpm build # 进入项目目录

pnpm link --global # 这个是用来链接库的

npm install -g . # 这个安装cli
```

命令列表
```
$ autofm --help
Usage:
  autofm --help // print help information
  autofm // current folder as root
  autofm --init (-i) // init model for the whole folder
  autofm --force (-f) // use force model to cover the old front matter
  autofm --ct (-c) // Re generate categories and tags
```

## Explain

init model：只会处理没有 Front-matter 的文章或者补全
CT Model： 重新生成 categories and tags

# Old Python Version

Hexo使用自动Front-matter生成器为每篇文章(包括新文章)添加 Front-matter

Hexo可以直接使用Git部署，所以可以在任何地方修改文章(只要你可以把它传到git上)，所以可以随心所欲的使用自己喜爱的编辑器，但手动为每篇文章添加Front-matter或批量修改老的Front-matter实在是太麻烦啦，于是就写了个自动化程序来干这件事情。

## 功能
- 自动根据目录填充分类和标签（最外层目录是分类，其他都是标签）
- 自动识别是否有Front-matter,只为没有Front-matter的文章添加
- 自定义标记，自定义标记之后的内容不做改动。

## 代码
```python
# 为内容添加Front-matter
import os

def fm_dev(rpath, tname, oldf = []): # 生成Front-matter
    rpath = rpath.split(os.path.sep)
    tit = "title: " + tname + "\n"
    tmpl = ["---\n", tit, "categories:\n", "tags:\n"]
    tmpl = tmpl + oldf + ["---\n"]

    if rpath[0] == '.': tmpl.insert(tmpl.index("categories:\n") + 1, "- Life\n") # 根目录下所有文件处于 Life 分类
    else: tmpl.insert(tmpl.index("categories:\n") + 1,"- " + rpath[0] + "\n")

    """路径中剩下的部分作为标签"""
    if len(rpath) > 1 :
        for i in range(1, len(rpath)):
            tmpl.insert(tmpl.index("tags:\n") + 1,"- " + rpath[i] + "\n")

    if rpath[0] == 'Net-excerpt': tmpl.insert(len(tmpl) - 1, "reprint: true\n") # 主题内自定义设置，转载文章标记

    return tmpl


fapath = os.path.split(os.path.realpath(__file__))[0]

for folderName, subfolders, filenames in os.walk(fapath):
    for filename in filenames:
        # 获取前缀（文件名称）
        tname = os.path.splitext(filename)[0]
        if os.path.splitext(filename)[-1][1:] == "md" :

            rpath = os.path.relpath(folderName, fapath) # 获取相对路径
            filepath = rpath + "\\" + filename # 获取文件的相对路径
            # print(filepath) # 测试路径是否正确
            TFile = open(filepath, 'r', encoding='utf-8') # 打开文件(只读)
            conntent = TFile.readlines() # 按行读取
            TFile.close() # 关闭文件

            if(conntent[0] == "---\n"): # 处理过的
                """找到Front-matter的位置"""
                for i in range(1, len(conntent)):
                    if(conntent[i] == "---\n"):
                        break
                
                """保留可能手动设置的信息"""
                oldf = []
                if "Flagold: true\n" in conntent : oldf = conntent[conntent.index("Flagold: true\n"): i]
                if "reprint: true\n" in oldf: oldf.remove("reprint: true\n")

                """生成Fornt-matter并写入文件"""
                conntent = fm_dev(rpath, tname, oldf) + conntent[i+1:]
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()

            else:
                conntent = fm_dev(rpath, tname) + ["\n\n"] + conntent
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()
```