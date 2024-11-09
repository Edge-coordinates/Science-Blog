---
title: CORS 问题
date: '2024/11/9 5:10:2'
categories:
  - Deploy
abbrlink: 3823c728
---

# CORS 问题
referrer 信息是什么？

防盗链怎么做？

CORS到底是被当前网站禁止还是被请求方禁止

> 整理自 Chatgpt  
> Date: November 9, 2024 5:00 AM (GMT+8)  
> Published: No

### 个人总结

吾辈一直看不到控制台输出，然后竟然没有发现是因为设置了控制台搜索（关键字），以后，这种情况一定要换浏览器，检查有没有过滤！！！！

这个错误表明在响应头中 `Access-Control-Allow-Origin` 被设置了多个值（`*` 和 `*`），而 CORS 规范要求该头部只能有一个值。通常，`Access-Control-Allow-Origin` 只能包含一个域或一个 `*`，不能同时设置多个。

### 新的修改方案
```bash 
# 第一行由 add_head 修改为 proxy_set_header
proxy_set_header Access-Control-Allow-Origin *;
add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
add_header Access-Control-Allow-Headers "Content-Type, Authorization";
if ($request_method = 'OPTIONS') {
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
    add_header Access-Control-Allow-Headers "Content-Type, Authorization";
    add_header Content-Length 0;
    add_header Content-Type text/plain;
    return 204;
}
```

要修复这个问题，以下是一些可能的解决方法：

### 1. **确保服务器端只返回一个有效的 `Access-Control-Allow-Origin` 值**

### 如果你允许所有源访问：

确保服务器配置只返回一个 `Access-Control-Allow-Origin: *` 头部，而不是多个头部。检查你的服务器配置，确保没有重复的 `add_header` 指令。

例如，如果你使用的是 Nginx，确保只设置一次 `Access-Control-Allow-Origin`：

```
location / {
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
    add_header Access-Control-Allow-Headers "Content-Type, Authorization";

    # 处理 OPTIONS 请求
    if ($request_method = 'OPTIONS') {
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Content-Type, Authorization";
        add_header Content-Length 0;
        add_header Content-Type text/plain;
        return 204;
    }
}

```
然而这样似乎只在**全局Nginx配置**中工作正常，直接在 1Panel 中的反向代理-源文做如此配置会触发如下报错：
```powershell
Access to fetch at 'https://' 
from origin 'https://' has been blocked by CORS policy: 
The 'Access-Control-Allow-Origin' header contains multiple values '*, *', but only one is allowed. 
Have the server send the header with a valid value, 
or, if an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.

```

这里贴出一般的报错：
```powershell
ccess to fetch at 'https://' 
from origin 'https://' 
has been blocked by CORS policy: 
Response to preflight request doesn't pass access control check: 
No 'Access-Control-Allow-Origin' header is present on the requested resource. 
If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```


### 2. **如果你只想允许特定的来源**

如果你想允许多个来源，但不是所有来源，可以在服务器端动态设置 `Access-Control-Allow-Origin` 头。假设你允许特定的域名，可以按以下方式进行设置：

### 例如，在 Node.js / Express 中动态设置：

```jsx
const express = require('express');
const app = express();

app.use((req, res, next) => {
    const allowedOrigins = ['<https://example.com>', '<https://anotherdomain.com>'];
    const origin = req.headers.origin;
    if (allowedOrigins.includes(origin)) {
        res.setHeader('Access-Control-Allow-Origin', origin); // 动态设置允许的来源
    }
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

app.get('/api', (req, res) => {
    res.json({ message: 'CORS fixed!' });
});

app.listen(3000, () => console.log('Server running on port 3000'));

```

这样就能确保只有允许的来源得到响应。

### 3. **避免在同一响应中设置多个 `Access-Control-Allow-Origin`**

在服务器配置中，避免设置多个 `Access-Control-Allow-Origin` 头。只设置一次，并且确保它不是重复的。

### 检查 Nginx、Apache 或 Express 配置

- **Nginx**：确保没有两个 `add_header Access-Control-Allow-Origin` 配置。只设置一个。
- **Express**：确保没有多次设置 `res.setHeader('Access-Control-Allow-Origin', ...)`。
- **Apache**：确保 `.htaccess` 或 Apache 配置中没有重复的 CORS 头部。

### 4. **调试和检查 CORS 配置**

确保在浏览器控制台中查看完整的 CORS 错误消息，以验证是否是由于多个 `Access-Control-Allow-Origin` 头部引起的问题。你可以使用浏览器的开发者工具检查响应头，确保只返回一个 `Access-Control-Allow-Origin`。

### 总结

1. 确保每次响应中只有一个 `Access-Control-Allow-Origin` 头部，且其值要么是 ``（允许所有域），要么是指定的特定域。
2. 如果允许多个来源，确保动态选择并返回合适的来源，而不是设置多个 ``。
3. 避免在服务器端有多个 CORS 配置，导致头部重复。

这些修改可以有效修复你遇到的 CORS 错误。

`(blocked: mixed-content)` 错误通常是由于在 HTTPS 页面上加载了 HTTP 资源（例如图片、脚本、样式表等），因为浏览器会阻止不安全的内容在安全页面上加载。要修复这个问题，可以使用以下方法：

### 1. **确保所有资源使用 HTTPS**

确保所有外部资源都通过 HTTPS 协议加载，而不是 HTTP。例如，将代码中的 `http://` 链接替换为 `https://`：

```html
<!-- 将 <http://example.com/script.js> 替换为 <https://example.com/script.js> -->
<script src="<https://example.com/script.js>"></script>

```

可以通过检查 HTML 文件、CSS 文件、JavaScript 文件中的所有链接，并将 HTTP 替换为 HTTPS。

### 2. **使用相对路径**

如果资源位于同一服务器上，可以使用相对路径，而不是绝对路径，这样可以避免协议问题：

```html
<!-- 从 <https://yourdomain.com/page> 加载资源会自动继承 https:// 协议 -->
<script src="/assets/script.js"></script>

```

### 3. **重定向 HTTP 到 HTTPS**

在服务器端配置强制 HTTPS，以确保即使请求了 HTTP 资源，服务器也会自动重定向到 HTTPS。

- **Nginx 配置**：

  在 Nginx 中设置 HTTP 到 HTTPS 的重定向：

  ```
  server {
      listen 80;
      server_name yourdomain.com;
  
      # 强制重定向到 HTTPS
      return 301 https://$host$request_uri;
  }
  
  ```

- **Apache 配置**：

  在 Apache 的 `.htaccess` 文件中添加以下内容：

  ```
  RewriteEngine On
  RewriteCond %{HTTPS} off
  RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
  
  ```

### 4. **检查和修复 JavaScript 中的 HTTP 链接**

如果在 JavaScript 中动态加载了 HTTP 资源，也会导致混合内容错误。检查所有 `fetch`、`XMLHttpRequest` 和其他动态加载的资源是否使用 HTTPS：

```jsx
// 确保动态请求也使用 HTTPS
fetch('<https://api.example.com/data>')
    .then(response => response.json())
    .then(data => console.log(data));

```

### 5. **使用 Content Security Policy (CSP)**

你可以使用 Content Security Policy (CSP) 来强制浏览器仅加载 HTTPS 资源，从而阻止混合内容加载：

在 HTML `<head>` 中添加以下元标签：

```html
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">

```

或在服务器响应头中添加 `Content-Security-Policy: upgrade-insecure-requests`，这将自动将页面中的 HTTP 请求升级为 HTTPS 请求。

通过这些方法，你可以有效地修复和避免混合内容错误。