---
title: JS的标点错误
date: 2022/10/14
categories:
  - - Pitfalls
    - FrontEnd
tags: null
abbrlink: 807da433
---

注意啊：
```js
console.log(`这是第一行
这是第二行`);

let a = 5,b = 1;
console.log(`a的值为${a}, b的值为${b}, a+b的值为${a+b}`)
// 对应的打印出来的结果为：a的值为5, b的值为1, a+b的值为6
```
中`号不是'（单引号）。
