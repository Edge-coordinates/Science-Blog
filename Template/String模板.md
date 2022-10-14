---
title: String模板
date: 2022/10/14
categories:
  - Template
abbrlink: b00469aa
tags:
---


写在开头：**学习** 用这是一些总结的方法不喜勿喷。。。

# string 系列 
- 转字符
```cpp
string Transfer_character(int n)
{ //将n转为字符
	string a;
	while (n)
	{
		a.append(1, (char)(n % 10 + 48));
		n /= 10;
	}
	return a;
}
```

**注意：转换过后是倒序！**  
>例： n = 14458 则 a = 85441

- 去零
```cpp
void Remove_0(string *a)
{ //去'0'
	while (a->at(a->length() - 1) == '0' && a->size() > 1)
	{
		a->erase(a->length() - 1, 1);
	}
}
```

- 转数字 （也是逆序）
```cpp
int trann(string str) //将str转为数字
{
	int pow[11] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000}; //用以更快的算幂次
	int k = str.length();
	int n = 0;
	for (int i = 0; i < k; ++i)
	{
		n += (str[i] - 48) * pow[i + 1];
	}
	return n;
}
```

>例： str = "77458" 则 n = 84577 可以和上文搭配着用。。。



