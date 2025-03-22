---
title: express-req and res
date: 2024/11/2 23:22:27
categories:
  - - Language-Basic
    - Javascript
    - Nodejs
abbrlink: d130de5a
---
以下是一些常用的req对象的属性：

```
req.params - 该属性包含路由参数对象，例如：/users/:id这个路由中:id部分就是一个参数，可以通过req.params.id来访问。
req.query - 该属性包含查询参数对象, 例如：/search?name=xxx这个URL中的"name=xxx"就是一个查询参数，可以通过req.query.name来访问。
req.body - 该属性包含POST请求的请求体。需要在中间件中使用body-parser等库来解析请求数据。
req.headers - 该属性包含HTTP请求头对象。
req.cookies - 该属性包含HTTP cookie值对象。
req.originalUrl - 该属性包含完整的请求URL，包括查询参数和路由参数。
```
除了以上列出的属性，req对象还有许多其他有用的属性和方法，例如：req.path、req.protocol、req.ip、req.get()等。开发者可以根据需要使用这些属性和方法来处理HTTP请求。

以下是一些常用的res对象的方法：
```
res.send() - 该方法将HTTP响应发送给客户端，并自动设置Content-Type头。
res.json() - 该方法将一个JSON对象作为响应发送给客户端，并将Content-Type头设置为application/json。
res.status() - 该方法用于设置HTTP响应状态码。
res.setHeader() - 该方法用于设置HTTP响应头。
res.cookie() - 该方法用于设置HTTP cookie值。
res.redirect() - 该方法用于重定向HTTP请求到另一个URL。
res.render() - 该方法用于呈现视图模板并将其作为HTTP响应发送给客户端。
```
除了以上列出的方法，res对象还有许多其他有用的方法和属性，例如：res.type()、res.attachment()、res.end()等。开发者可以根据需要使用这些方法和属性来处理HTTP响应。

### 获取url查询字符串中的参数
在Express.js中，可以使用req.query对象来获取URL查询字符串中的参数。req.query是一个包含键值对的对象，每个键都是查询参数名，每个值都是查询参数的值。

例如，在以下的请求URL中：
```
http://localhost:3000/search?q=nodejs&page=2
```

我们可以通过下面的代码来获取q和page这两个查询参数的值：
```javascript
app.get('/search', function(req, res) {
  const searchQuery = req.query.q; // 获取查询参数 q 的值
  const page = req.query.page; // 获取查询参数 page 的值
  // ...
});
```
在上面的例子中，我们在GET请求处理程序中使用了req.query对象来获取查询参数的值，并将其分别保存到searchQuery和page变量中