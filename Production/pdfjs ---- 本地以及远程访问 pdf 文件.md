---
title: pdfjs ---- 本地以及远程访问 pdf 文件
date: 2022/10/14
categories:
  - - Production
tags: null
abbrlink: 46d13b71
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/qiumen/article/details/83000284)

_如何下载 pdfjs，可查看我的另外一篇博客文章_ 

[https://blog.csdn.net/qiumen/article/details/82698471](https://blog.csdn.net/qiumen/article/details/82698471)

**一、本地访问**
----------

1. 把 pdfjs 放到项目，可把 pdf.js 和 pdf.worker.js 放到另外专门的 js 文件夹（放置位置自己调，pdf.min.js 以及 pdf.worker.min.js 是去网上找自动压缩工具压缩的，你自己要不要压缩随你的便）

![](https://img-blog.csdn.net/20181010171908559?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2. 打开 viewer.js 文件，ctrl+f 搜索‘DEFAULT_URL’查看默认文件位置，也就是说，你直接在网上打开文件的时候就可以默认打开这个文件了，下载的 pdf 文件里面会默认带有这个文件

![](https://img-blog.csdn.net/20181010172322127?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20181010172537920?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

如果想要修改文件的话，改掉文件名，以及把文件放在 pdfweb 下面下，与刚才的 pdf 文件同级，具体自己修改文件路径

3. 如果想要浏览其它 pdf 文件的话，我们的访问方式也可以这样表示：

http://localhost:9528/static/pdfweb/viewer.html?file=a.pdf

注意 file 文件的路径，放在 pdfweb 下，否则可能读不到，如果不放到 pdfweb 下也行，但访问的路径要写对

本地访问比较简单，接下来是远程访问了，接下来我会把我所遇到的问题都尽可能写出来。

**二、远程访问**
----------

一般项目是 MVVM 的话，前后端分离，一般都是远程访问，即访问远程服务器

1、远程访问的话，远程文件名也可以放在 file 后面： http://localhost:9528/static/pdfweb/viewer.html?file=******.pdf

但远程访问的话，file 后面肯定会跟 http 地址，浏览器会因识别不了两条 http 而报出奇奇怪怪的原因，因此 file 后面的文件需要编码，用 js 自带函数 encodeURIComponent 编码，把编码后的远程 pdf 文件的地址放在 file 后面，这样 file 后面的文件就是编码后的地址了

![](https://img-blog.csdn.net/20181010174033697?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2、这样远程访问肯定会有问题的，pdf.js 是不支持跨域文件加载的，直接加载是不会成功的。会报  “file origin does not match viewer” 错误。这里涉及到前后端的设置

首先先来说前端的设置，打开 viewer.js 文件

注释掉这个

![](https://img-blog.csdn.net/20181010174458608?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

后端的设置，后端会拒绝访问这个，因此需要远程服务器处理这个 pdf 的 servlet 上面设置可任何服务器访问，也可以在过滤器上设置，也可以在服务器上设置，比如 ngnix 的反向代理机制来解决前端跨域访问的问题，这个在网上也有很多资料，下面讲下在 servlet 上处理以及在 ngnix 上处理两种方法：

1）servlet 上处理，为了分片处理

![](https://img-blog.csdn.net/20181010180655777?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

2）ngnix 反向代理这个如何处理，在 nginx 配置中加入了这样一句：add_header 'Access-Control-Allow-Origin' '*';

   如图所示：

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)

关于 ngnix 反向代理可以参照网上这个链接：[https://www.cnblogs.com/soukingang/p/5445252.html](https://www.cnblogs.com/soukingang/p/5445252.html)

以上的方法对于访问远程服务器上的 pdf 文件或者 pdf 文件流都可以访问

3. 还有一个很重要的问题，关于 J2EE 跨域资源共享还需要在你的 xml 上面配置这样一段信息以及加上两个 jar 包，这个很重要，jar 包的获取很容易的，直接去这里下载就行：[https://mvnrepository.com/repos/central](https://mvnrepository.com/repos/central)

1）cors-filter-1.7.1.jar  
2）java-property-utils-1.9.1.jar  
web 项目中的 web.xml 文件  
添加过滤器：  
 

```
 <filter>
   <filter-name>CorsFilter</filter-name>
   <filter-class>com.thetransactioncompany.cors.CORSFilter</filter-class>
</filter>
<filter-mapping>
      <filter-name>CorsFilter</filter-name>
      <url-pattern>/*</url-pattern>
</filter-mapping>
```

4. 另外说一声，就是是返回字节流，其加载方式也可以这样操作的，然后把 servlet 链接放到 file 后面即可, 注意要用 js 自带函数 encodeURIComponent 编码

urlhttp://localhost:9528/static/pdfweb/viewer.html?file=******

5. 如果想要隐藏下载功能的话，可以在 viewer.html 设置这一小段代码，如果源代码看不懂，注释掉可能会引发奇奇怪怪的问题，所以还是加段代码把：style="visibility:hidden"

![](https://img-blog.csdn.net/2018101109413676?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20181011094406670?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

**三、优化 pdfjs 加载速度（cdn、压缩成 min.js、min.css、分片加载）**
------------------------------------------------

1、采用 cdn 加载，不懂的可以网上查询 cdn 加载的意思以及用处

在 pdfjs 官方存放代码里，里面有关于 cdn 加载的路径，以及提供 pdfjs 提供的地址

[https://cdnjs.com/libraries/pdf.js](https://cdnjs.com/libraries/pdf.js) 

如果你没有在插件改过代码的话，你可以直接引用官方提供的 cdn 地址，比如

![](https://img-blog.csdn.net/20181011094828884?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

注意版本号写对 1.9.426，别踩坑，不然显示不出资料，版本号怎么知道是哪个呢，如果你的 pdf 预览报错，就会显示版本号，因为我在代码没有看到版本号，所以我就通过页面报错找到版本号

如果代码改过就不要引用 cdn 了，直接压缩，比如我上图的 viewer.min.js ，在线压缩工具进行压缩就行了，这样发生产版本的远程加载就会快，注意路径要写对

![](https://img-blog.csdn.net/20181011095147404?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20181011095221460?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

分片加载：

但是如果 pdf 文件比较大， 往往会加载比较慢。影响用户体验。假设一个 pdf 文件大小为：100M，如何快速的在浏览器打开

前置条件   
第一：web 服务器必须要能支持，分片下载。nginx 1.09 版本已上默认的就支持了   
第二：浏览器支持，经过简单测试，谷歌和火狐都支持，谷歌支持的最好.

如何设置分片大小

```
PDFJS.getDocument({url:url,rangeChunkSize:65536*16}).then(function(pdfDoc_) {
        pdfDoc = pdfDoc_;
        document.getElementById('page_count').textContent = pdfDoc.numPages;
 
        // Initial/first page rendering
        renderPage(pageNum);
 
   })
```

*   rangeChunkSize ： 就是分块大小，默认：65536（64k）。默认太小了，这个文档 100m, 需要有 1000 多个请求，才能下载完毕。所以我调成成了 512k，减少请求数。如果你的 pdf 文件就是一两页，那么你设置分页没有多大效果，可以说不用设置。另外不同版本，可能设置分页的位置不一样，我现在的版本的话，就设置这个就行了
*   ![](https://img-blog.csdn.net/2018101109584313?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpdW1lbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

可参照此链接：[https://blog.csdn.net/niedewang/article/details/79883828](https://blog.csdn.net/niedewang/article/details/79883828)

===============================================================

以上总结的就是遇到的坑，有些步骤我给了，但我没有解释为什么要这样子做，有些你们要自己查原因为什么要这样子处理，如果我全部写了篇幅会很长，如果有疑问可以发表感言，很少写博客，描述文字不严谨，见谅、、告退、、、、