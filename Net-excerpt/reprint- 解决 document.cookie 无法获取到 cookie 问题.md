---
title: reprint- 解决 document
date: 2022/10/14
categories:
  - Net-excerpt
tags: null
reprint: true
abbrlink: e8c7e2e7
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/weixin_40686603/article/details/116188863)

一、前言
----

在进行前后端联调的时候，由于想实现一个登出操作，前端自动删除浏览器存储的 cookie，想通过 document.cookie 来获取进而进行删除操作，但是发现浏览器有 cookie；但是无法获取到情况遂记录

二、场景复现
------

1.  首先登录后，浏览器中是有记录 cookie 的，如图  
    ![](https://img-blog.csdnimg.cn/20210427084217576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDY4NjYwMw==,size_16,color_FFFFFF,t_70)
2.  然后我代码层执行`documen.cookie`发现获取不到，浏览器控制台也同样  
    ![](https://img-blog.csdnimg.cn/20210427084637984.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDY4NjYwMw==,size_16,color_FFFFFF,t_70)
3.  后面去研究了一下 application 中存放的 cookies 的属性内容，发现有个属性 HttpOnly 是选中状态，这个状态是由于后端设置 cookie 的时候设置了该属性为 true 导致

```
//后端代码
public static void addCookie(HttpServletResponse response, String name, String value, String domain, int maxAge) {
    try {
        Cookie cookie = new Cookie(name, URLEncoder.encode(value, "utf-8"));
        cookie.setPath("/");
        cookie.setDomain(domain);
        cookie.setMaxAge(maxAge);
        cookie.setHttpOnly(true);   //后端设置httpOnly属性为true
        response.addCookie(cookie);
    } catch (Exception var6) {
        throw new RuntimeException(var6.getMessage());
    }
}
```

![](https://img-blog.csdnimg.cn/20210427084849886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDY4NjYwMw==,size_16,color_FFFFFF,t_70)

4.  后面我将 HttpOnly 设置 false 状态后，`documen.cookie`就能够获取到  
    ![](https://img-blog.csdnimg.cn/20210427085313313.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDY4NjYwMw==,size_16,color_FFFFFF,t_70)
5.  百度查了一下 HttoOnly 属性的作用，觉得这个博主解释很到位【[HttpOnly 解答](https://www.jianshu.com/p/ba6500990694)】

> HttpOnly 是 2016 年微软为 IE6 而新增了这一属性  
> HttpOnly 是包含在 http 返回头 Set-Cookie 里面的一个附加的 flag，所以它是后端服务器对 cookie 设置的一个附加的属性，在生成 cookie 时使用 HttpOnly 标志有助于减轻客户端脚本访问受保护 cookie 的风险（如果浏览器支持则会显示，若不支持则选择传统方式）

6.  也就是说 HttpOnly 的存在主要是为了防止用户通过前端来盗用 cookie 而产生的风险，例如 XSS 攻击就是对 cookie 进行盗窃，使用这一属性就可以防止客户端（前端）不可访问