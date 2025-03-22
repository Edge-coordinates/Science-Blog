---
title: express-错误处理
date: 2024/11/2 23:22:27
categories:
  - - Language-Basic
    - Javascript
    - Nodejs
abbrlink: 8fbf0568
---
在 Express.js 中，错误处理是通过特定的中间件来实现的。当在请求处理过程中发生错误时，Express.js会自动调用错误处理中间件来处理该错误。

对于常规的中间件函数，如果其执行过程中出现了异常，则应该将该异常传递给下一个中间件或者交由全局错误处理中间件处理。为此，可以使用next()函数将异常对象作为参数传递给下一个中间件，例如：

```javascript
app.get('/', function(req, res, next) {
  try {
    // some code that may throw an exception
  } catch(err) {
    // 将异常传递给下一个中间件来处理
    next(err);
  }
});
```
如果没有捕获到异常，那么最终会交给全局错误处理中间件来处理。全局错误处理中间件需要有四个参数，形式如下：

```javascript
app.use(function(err, req, res, next) {
  // 处理错误
});
```
其中err是错误对象，req和res分别是请求和响应对象，next是下一个中间件函数。在错误处理中间件中，可以根据需要对错误进行处理，例如记录日志、发送错误信息等。

除了常规的中间件函数外，也可以创建专门处理错误的中间件函数。这些中间件函数通常用于处理特定类型的错误，例如404错误、500错误等。

以下是一个示例，展示了如何创建一个处理404错误的中间件函数：

```javascript
app.use(function(req, res, next) {
  res.status(404).send('Sorry, we cannot find that!');
});
```
在上面的例子中，我们使用res.status(404)来设置HTTP响应状态码为404，并使用res.send()方法来发送响应内容。这样，当客户端请求一个不存在的路由时，就会收到一个包含错误信息的404响应。