---
title: 随即图片API的使用(同一页面请求多张图浏览器缓存导致图片相同的解决方案)
categories:
- Life
tags:
---


博客可以写很多，有更多的地方会用到图片，因为一般人都会懒得自己设置每一张图片的样式，所以随机图片api就诞生了。

图片api很常见，一搜就可以搜到很多，文末会放置一些Edge在使用的api，和高质量的api推荐，但当很多人意气风发的将图片api给的接口地址替换掉原来的图片地址后，会发现如果你在同一个页面请求了多张图片，会导致图片实际显示的是同一张。。。  
对于一个没有充足的网络相关的知识储备的人来说，判断问题的所在的和搞出解决方案是需要花费大量的时间的。  
**所以这篇文章就诞生啦！**

## 同一个页面请求了多张图片，图片相同的解决方案

问题就出现在, 发起请求时, 由于链接地址是同一个, 实际上即使同一个页面中有多个(相同)图片链接, 也仅仅发起一次请求, 所以也就返回一张图片了!

所以只要修改链接不同即可!


- 首先，选取一个API  

Edge将选两个不同的api作为讲解的素材，它们分别是：
```python
https://tuapi.eees.cc/api.php  # 随机图片API 随心而换 想刷就刷
https://acg.toubiec.cn/random.php # 晓晴博客
https://img.paulzzh.tech/touhou/random # 二次元随机图片
```

- 生成随机数并按照正确的形式传入
```JavaScript
// JavaScript代码
let coverx = "https://acg.toubiec.cn/random.php"
coverx += ("?" + Math.ceil(Math.random()*10000))
```
可以看到，如过api没有特殊的要求，那么只要最终生成形如`https://acg.toubiec.cn/random.php?一个数字`的链接就可已返回一个图片。  
对于形如`https://img.paulzzh.tech/touhou/random`,同样在末尾加上`?数字`就可以了。  
那么，当API本身的链接已经包含`?`，我们应当怎么办呢？这里，大家可以自行查阅url中的?是干嘛用的，但那些内容已经超出了本文的范围。  
就比如本文的选用的第一个api,如果你打开`https://tuapi.eees.cc/api.php`,会看到它让你使用形如`https://tuapi.eees.cc/api.php?category={dongman,fengjing}&type=302`来获取图片，那么，我们只需要在URL的末尾加上`&一个数字`就可以了！即生成一个形如`https://tuapi.eees.cc/api.php?category={dongman,fengjing}&type=302&一个数字`的URL就可以了。


## 附录

### 如何使用随机图片API

使用: 只要请求图片时, 将路径改为API提供的路径即可.  
对于Markdown来说:  
`![image_infp](API_URL)`  
对于HTML来说是修改src属性:  
`<img src="API_URL" />`  