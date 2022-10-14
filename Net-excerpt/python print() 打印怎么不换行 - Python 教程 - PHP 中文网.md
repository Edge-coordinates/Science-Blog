---
title: python print() 打印怎么不换行 - Python 教程 - PHP 中文网
date: 2022/10/14
categories:
  - Net-excerpt
reprint: true
abbrlink: bcbf16ce
tags:
---


---
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.php.cn](https://www.php.cn/python-tutorials-423471.html)

> Python2 和 Python3 就有明显的不同，python2 中，输出默认是换行的，为了抑制换行，可以在打印最后加一个逗号；python3 中，print 变成一个函数，这种语法便行不通了。

__原创__2019-12-28 11:37:50__0__19795

python print() 打印怎么不换行? 在 python 不同的版本中存在着差异，Python2 和 Python3 就有明显的不同。下面给大家介绍一下两者有什么不同之处。

![](https://img.php.cn/upload/article/000/000/037/5d0b19f22d9ee649.jpg)

**在 Python2.x 中**

python2.x 中输出默认是换行的，为了抑制换行，可以在打印最后加一个逗号

> 推荐手册：[Python 基础入门教程](https://www.php.cn/course/32.html)  

![](https://img.php.cn/upload/image/968/999/762/1560215808607564.png)

相关推荐：《[Python 视频教程](http://www.php.cn/course/list/30.html)》

**在 Python3.x 中**

到了 python3 中，print 变成一个函数，这种语法便行不通了。

> 推荐手册：[Python 3 教程](https://www.php.cn/course/50.html)

我们可以使用 print(x, end="")

end="" 可使输出不换行。

双引号之间的内容就是结束的内容， 可以是空格，也可以是其他字符，默认为换行

![](https://img.php.cn/upload/image/681/869/157/1560215830412404.png)

> 相关文章推荐：  
> 1.[python 编写时怎么换行](https://www.php.cn/python-tutorials-419100.html)  
> 2.[python print 怎么换行](https://www.php.cn/python-tutorials-421297.html)相关视频推荐：  
> 1.[2019python 自学视频](https://www.php.cn/course/1078.html)  
> 2.[Python Web 入门视频教程](https://www.php.cn/course/796.html)  
> 3. [python 入门视频教程](https://www.py.cn/course/list/97/type/2.html)

以上就是 python print() 打印怎么不换行的详细内容，更多请关注 php 中文网其它相关文章！

[![](https://img.php.cn/upload/article/000/000/003/60d557b50f89a276.jpg)](https://www.php.cn/k.html)

声明：本文原创发布 php 中文网，转载请注明出处，感谢您的尊重！如有疑问，请联系 admin@php.cn 处理

相关文章

相关视频

* * *

专题推荐
----

*   [![](https://img.php.cn/upload/article/000/000/003/5d1ef1e9e866e635.jpg)](https://www.php.cn/map/dugu.html)[独孤九贱 - php 全栈开发教程](https://www.php.cn/map/dugu.html)
    
    全栈 100W+
    
    主讲：Peter-Zhu 轻松幽默、简短易学，非常适合 PHP 学习入门
    
*   [![](https://img.php.cn/upload/article/000/000/003/5d1ef236ca878949.jpg)](https://www.php.cn/map/yunv.html)[玉女心经 - web 前端开发教程](https://www.php.cn/map/yunv.html)
    
    入门 50W+
    
    主讲：灭绝师太 由浅入深、明快简洁，非常适合前端学习入门
    
*   [![](https://img.php.cn/upload/article/000/000/003/5d1ef2477c7d7587.jpg)](https://www.php.cn/toutiao-409221.html)[天龙八部 - 实战开发教程](https://www.php.cn/toutiao-409221.html)
    
    实战 80W+
    
    主讲：西门大官人 思路清晰、严谨规范，适合有一定 web 编程基础学习