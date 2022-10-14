---
title: Interesting Problems
categories:
  - Life
abbrlink: a976e6e0
tags:
---


Q：编程实现输入两个整数a,b，当a≥b时，输出a的值，否则输出0。
你知道如何不使用 if，switch以及 3 目运算符，来解决这个问题么？
A: 先将a和b进行比较，t=(a>b),当a>b时为真则t为1,否则是假t为0,为真a大要是输出为a则t*a就行，反之0*a=0,满足了否输出了0的条件，合并起来就是 printf("%d",(a>b)*a);