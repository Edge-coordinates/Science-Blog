---
title: simpread-面试官：CSS 如何实现固定宽高比？ - 腾讯云开发者社区 - 腾讯云
date: 2022/10/14

categories:
  - Design
abbrlink: 5cc18268
tags:
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [cloud.tencent.com](https://cloud.tencent.com/developer/article/1609830)

> 对于这个问题，你可能还没有过相关需求，或者还没有在面试的时候被问到过，但是歪马相信你终将有需要。

~ 欢迎点击上方蓝字「歪码行空」快速关注~

* * *

对于这个问题，你可能还没有过相关需求，或者还没有在面试的时候被问到过，但是歪马相信你终将有需要。

这个问题说起来也是老生常谈，歪马今天再次提起也是希望有朝一日当你被问到的时候，能够答得漂亮。

如果有一天你被问到：“你能说一下如何实现一个固定宽高比的元素吗？”

听到这个的时候你一定不要盲目的说出答案。因为这么问的话，题目并不明确。所以你可以帮面试官补充题设或提问来确认要求。你可以做如下回答：

*   如果元素的尺寸已知的话，没什么好说的，计算好宽高写上去就行了。
*   如果元素尺寸未知，最简单的方法是用 JavaScript 实现，如果用 CSS 的话可以分为以下几种：
    *   如果是可替换元素`<img>`或`<video>`，该怎么实现?
    *   如果是普通的元素，又应该怎么实现？

今天歪马就和大家一起看看上面几种情况。

首先，元素尺寸已知，这个 pass 掉。不用说，说了我怕你们打我。

我们重点讨论**元素尺寸未知**的情况。

所以本文主要分为可替换元素和普通元素如何实现固定宽高比。

**一、可替换元素实现固定宽高比**
------------------

可替换元素 (如`<img>`、`<video>`) 和其他元素不同，它们本身有像素宽度和高度的概念。所以如果想实现这一类元素固定宽高比，就比较简单。

我们可以**指定其宽度或者高度值，另一边自动计算就可以了**。

如下，我们固定图片元素的宽度，高度自适应：

```
<div class="img-wrapper">
  <img src="https://p3.ssl.qhimg.com/t01f7d210920c0c73bd.jpg" alt="">
</div>
```

```
.img-wrapper {
  width: 50vw;
  margin: 100px auto;
  padding: 10px;
  border: 5px solid lightsalmon;
  font-size: 0;
}

img {
  width: 100%;
  height: auto;
}
```

效果如下图所示，可以看出当可视区域不断变大的过程中，图片会跟着变大，并且保留了原比例。

![](https://ask.qcloudimg.com/http-save/yehe-7156129/wfu4grrpsv.gif)

图片元素固定宽高比

> 你可能没注意到，我们给`img`元素设定了`height: auto;`，这是为了避免开发者或者内容管理系统在 HTML 源码中给图片添加了`height`属性，通过这个方式可以覆盖掉，避免出现 bug。

此外，对于`video`元素也类似，大家可以试下，效果如下。

![](https://ask.qcloudimg.com/http-save/yehe-7156129/iqt6pau8r2.gif)

video 元素固定宽高比

**二、普通元素实现固定宽高比**
-----------------

虽然我们上面实现了可替换元素的固定宽高比，但是这个比例主要是因为可替换元素本身有尺寸，而且这个比例还会受到原有尺寸比例的限制。显然，这并不灵活，那我们该如何针对普通元素实现固定宽高比呢。

首先我们来看看最经典的`padding-bottom/padding-top`的 hack 方式。

### **2.1 `padding-bottom`实现普通元素固定宽高比**

在之前的陪读章节[**《精通 CSS》第 3 章 可见格式化模型**](https://mp.weixin.qq.com/s?__biz=MzI4OTI0NDc2NQ==&mid=2247483722&idx=1&sn=88d8d76ed9e9279d39c57311a62f9137&chksm=ec335278db44db6e6b2e83b7be1d16989b02f412481af159e2b2584a88b7dc98ed81c21ebdca&token=666946662&lang=zh_CN&scene=21#wechat_redirect)中，我们提到**垂直方向上的内外边距使用百分比做单位时，是基于包含块的宽度来计算的**。

> 下面均以`padding-bottom`为例

通过借助`padding-bottom`我们就可以实现一个宽高比例固定的元素，以`div`为例。

HTML:

```
<div class="wrapper">
  <div class="intrinsic-aspect-ratio-container"></div>
</div>
```

CSS:

```
.wrapper {
  width: 40vw;
}
.intrinsic-aspect-ratio-container {
  width: 100%;
  height: 0;
  padding: 0;
  padding-bottom: 75%;
  margin: 50px;
  background-color: lightsalmon;
}
```

效果如下：

![](https://ask.qcloudimg.com/http-save/yehe-7156129/1sxz3efp7u.gif)

固定宽高比的 div

如上代码，我们将`div`元素的高度设为了`0`，通过`padding-bottom`来撑开盒子的高度，实现了`4/3`的固定宽高比。

这样是实现了固定宽高比，但其`只是一个徒有其表的空盒子，里面没有内容。如果想在里面放入内容，我们还需要将`div` 内部的内容使用绝对定位来充满固定尺寸的[容器](https://cloud.tencent.com/product/tke?from=10680)元素。

如下：

```
.intrinsic-aspect-ratio {
  position: relative;
  width: 100%;
  height: 0;
  padding: 0;
  padding-bottom: 75%;
  margin: 50px;
  background-color: lightsalmon;
}
.content {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
```

通过这种方式我们就可以实现一个可以填充内容的固定尺寸的容器了。

此外，尺寸比例，我们也可以通过`calc()`来计算，这样比较灵活。我们可以快速的写出任意比例，如`padding-bottom: calc(33 / 17 * 100%);`。

不知道，你有没有发现，上面的这种方式只能高度随着宽度动，并不能实现宽度随着高度动。

那有没有办法实现宽度随着高度动呢？**答案是没有，至少现在没有。但将来就会有了**。接下来我们一起看看更简单便捷的另一种方式。

### **2.2 `aspect-ratio`属性指定元素宽高比**

由于固定宽高比的需求存在已久，通过`padding-bottom`来 hack 的方式也很不直观，并且需要元素的嵌套。

W3C 的 CSS 工作组为了避免这一问题，已经在致力于实现这样一个属性`aspect-ratio`。该方案已经提出，但是还没有浏览器实现，现在还处于设计节点，暂时还没有已发布的工作组草案，只有**编辑草案 [1]**。

但是这并不妨碍我们来提前了解一下这个新技术。

下面让我们一起来看看是如何的便利吧。

`aspect-ratio`的语法格式如下：`aspect-ratio: <width-ratio>/<height-ratio>`。

如下，我们可以将`width`或`height`设为`auto`，然后指定`aspect-ratio`。另一个值就会按照比例自动变化。

```
/* 高度随动 */
.box1 {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
}

/* 宽度随动 */
.box2 {
  height: 100%;
  width: auto;
  aspect-ratio: 16/9;
}
```

这一技术可以很灵活的实现元素的固定宽高比，并且指定宽高之一均可。只是现在还没有浏览器实现，让我们共同期待吧。

**三、总结**
--------

本文总结了如何实现元素的固定宽高比。如果你再在面试的过程中被问到这个问题。你就可以像这样回答了。

*   如果元素的尺寸已知的话，没什么好说的，计算好宽高写上去就行了。
*   如果元素尺寸未知，最简单的方法是用 JavaScript 实现，如果用 CSS 的话又要分为以下几种：
    *   如果是可替换元素`<img>`或`<video>`，可以将`width`/`height`其一设定尺寸，另一个设为`auto`，则可替换元素会根据其固有尺寸进行变化。
    *   如果是普通的元素，我们可以通过`padding-top`/`padding-bottom`的方式来模拟固定宽高比，不过这种方式不灵活，只能够高度随着宽度变。CSS 工作组现在正在引入一种新的方案`aspect-ratio`，可以很方便地指定宽高比，不过暂时还没有浏览器实现。相信不久之后就会有浏览器逐渐实现了。

如果最后你的答案是这样的，那么你不仅完善了老师的题设，给出了各种情况的解决方案，最后还点出了标准中正在制定的新方案。这样回答不仅展示了你对于问题考虑的严谨，还可以看出你时刻关注着标准的制定，这都是大大的加分项哟。这样，我只能说，这次面试你稳了。

**参考链接**
--------

*   **Aspect Ratio Boxes[2]**
*   **Designing An Aspect Ratio Unit For CSS[3]**
*   **CSS Box Sizing Module Level 4[4]**

### **参考资料**

[1] 编辑草案: _https://drafts.csswg.org/css-sizing-4/#ratios_

[2]Aspect Ratio Boxes: _https://css-tricks.com/aspect-ratio-boxes/_

[3]Designing An Aspect Ratio Unit For CSS: _https://www.smashingmagazine.com/2019/03/aspect-ratio-unit-css/_

[4]CSS Box Sizing Module Level 4: _https://drafts.csswg.org/css-sizing-4/%23ratios_