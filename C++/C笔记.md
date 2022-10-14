---
title: C笔记
categories:
  - C++
abbrlink: 382f3c37
tags:
---


编程笔记

#include<stdlib.h>  对rand()的定义。
#include<time.h>    初始化rand()所用头文件。
srand(time(NULL));  初始化rand()所用代码。
sqrt  **的平方根
文件输入法：{
freopen("文件名.类型","r",stdin);  文件输入。
freopen("文件名.类型","w",stdout); 文件输出。}
float   较短浮点数定义法。
double  较长浮点数定义法。
浮点型数据输入、打印方法：{
输入：
float型：scanf("%f",&某某);
double型：scanf("%lf",&某某);
输出：
float型：printf("%f",某某);
double型：printf("%lf",某某);}
continue;  结束本次循环。
printf("%.某某f",某某);  表示精确到小数点后几位。
pow(一个数,次数);
freopen(“CON”,”r”,stdin);
freopen(“CON”,”w”,stdout);
CON-键盘。
sizeof：测量变量和数组的长度字节数。
switch(){
case常量:语句
case常量:语句
default:语句
}
deauflt--switch中都不是就执行。
#define L 10 定义一个符号代表常亮。
static 定义静态全局变量。
gets() 按行输入字符串。
puts() 输出字符串。
strcat() 连接两个字符串。
