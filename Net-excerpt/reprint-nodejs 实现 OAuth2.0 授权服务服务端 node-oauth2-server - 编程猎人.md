---
title: reprint-nodejs 实现 OAuth2
date: 2022/10/14
categories:
  - - Net-excerpt
tags: null
reprint: true
abbrlink: 4009585d
---



> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.programminghunter.com](https://www.programminghunter.com/article/9119443063/)

> nodejs 实现 OAuth2.0 授权服务服务端 node-oauth2-server，编程猎人，网罗编程知识和经验分享，解决编程疑难杂症。

摘要：看了好多，头疼，自己写一个吧。

1、nodejs

2、node-oauth2-server (node 模块)

3、mysql（数据库）

1.  协议

　　　　OAuth 协议为用户资源的授权提供了一个安全的、开放而又简易的标准。

　　　　优点：OAuth 的授权不会使第三方触及到用户的帐号信息（如用户名与密码），即第三方无需使用用户的用户名与密码就可以申请获得该用户资源的授权。

　　　　流程：用户登录了第三方的系统后，会先跳去服务方获取一次性用户授权凭据，再跳回来把它交给第三方。 _第三方的服务器会把授权凭据以及服务方给它的的身份凭据一起交给服务方，这样，服务方一可以确定第三方得到了用户对此次服务的授权（根据用户授权凭据）二可以确定第三方的身份是可以信任的（根据身份凭据）。所以，最终的结果就是，第三方顺利地从服务方获取到了此次所请求的服务。_

了解 OAuth2.0 与 oauth2-server 的专用术语，对于理解后面内容很有帮助。

**OAuth2.0 定义了四个角色**

1.  **Client**：客户端，第三方应用程序。
2.  **Resource Owner**：资源所有者，授权 Client 访问其帐户的用户。
3.  **Authorization server**：授权服务器，服务商专用于处理用户授权认证的服务器。
4.  **Resource server**：资源服务器，服务商用于存放用户受保护资源的服务器，它可以与授权服务器是同一台服务器，也可以是不同的服务器。

**oauth2-server**

1.  **Access token**：用于访问受保护资源的令牌。
2.  **Authorization code**：发放给应用程序的中间令牌，客户端应用使用此令牌交换 access token。
3.  **Scope**：授予应用程序的权限范围。
4.  **JWT**：[Json Web Token](https://tools.ietf.org/html/rfc7519) 是一种用于安全传输的数据传输格式。　　

OAuth2.0 定义了四种授权模式，以应对不同情况时的授权。

1.  授权码模式（authorization code）
2.  隐式授权模式，简化模式（implicit）
3.  密码模式（resource owner password credentials）
4.  客户端模式（client credentials）

*   保密的：
    *   客户端可以安全的存储自己与用户的凭据（例如：有所属的服务器端）
*   公开的：
    *   客户端无法安全的存储自己与用户的凭据（例如：运行在浏览器的单页应用）

1.  如果客户端是保密的，应使用[授权码模式](https://www.cnblogs.com/mafei99/p/10308696.html#%E6%8E%88%E6%9D%83%E7%A0%81%E6%A8%A1%E5%BC%8F)。
2.  如果客户端是公开的，应使用[隐式授权模式](https://www.cnblogs.com/mafei99/p/10308696.html#%E9%9A%90%E5%BC%8F%E6%8E%88%E6%9D%83%E6%A8%A1%E5%BC%8F)。
3.  如果用户对于此客户端高度信任（例如：第一方应用程序或操作系统程序），应使用[密码模式](https://www.cnblogs.com/mafei99/p/10308696.html#%E5%AF%86%E7%A0%81%E6%A8%A1%E5%BC%8F)。
4.  如果客户端是以自己的名义，不与用户产生关系，应使用[客户端模式](https://www.cnblogs.com/mafei99/p/10308696.html#%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%A8%A1%E5%BC%8F)。

　　客户端需要预先在授权服务器进行注册，用以获取 `client_id` 与 `client_secret`，也可以在注册是预先设定好 `redirect_uri`，以便于之后可以使用默认的 `redirect_uri`。

　　授权码模式是 OAuth2.0 种功能最完整，流程最严密的一种模式，如果你使用过 Google 或 QQ 登录过第三方应用程序，应该会对这个流程的第一部分很熟悉。

1.  流程

![](https://www.programminghunter.com/images/403/af/af036ebcc43d7935b5c9ac9959c935fb.png)

1.  获取授权码。
    1.  /oauth2/authorize 为前端提交账户密码的路由，将以下参数通过 `GET query` 传入　
        1.  `response_type`：授权类型，必选项，值固定为：`code` 
        2.  `client_id`：客户端 ID，必选项　　
        3.  `redirect_uri`：重定向 URI，可选项，不填写时默认预先注册的重定向 URI　　
        4.  `scope`：权限范围，可选项，以空格分隔　　
        5.  `state`：[CSRF](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0) 令牌，可选项，但强烈建议使用，应将该值存储与用户会话中，以便在返回时验证　　
    2.  oAuth2Server 是你封装的获取授权码的模块。　　
    3.  authorizeHandler() 是获取授权码 code 的函数。
        1.  `code`：授权码 (Authorization code)　　
        2.  `state`：请求中发送的 `state`，原样返回。客户端将此值与用户会话中的值进行对比，以确保授权码响应的是此客户端而非其他客户端程序　　
    4.  redirectUriWithCode() 是服务端重定向至客户端的函数　　

```
// 路由文件
app.all('/oauth2/authorize', oAuth2Server.authorizeHandler(), oAuth2Server.redirectUriWithCode()); // 获取授权码
```

```
// 封装的oauth2文件
const oauthServer = require('oauth2-server');
import OAuthError from 'oauth2-server/lib/errors/oauth-error';
const Request = oauthServer.Request;
const Response = oauthServer.Respoconst oauth = new OauthServer({
```

```
model: oauthModel,
  allowEmptyState: true,
  authenticateHandler: {
    handle: function(req) {
      if (!req.user) {
        throw new OAuthError('需要登录', { code: 400 });
      }
      return req.user;
    },
  },
});


/**
 * 授权获取code
 * @param req
 * @param res
 * @param next
 * @returns {Promise<*>}
 */
export async function authorizeHandler(req, res, next) {
  log.info(`authorizeHandler: ${req.url}`);
  const request = new Request(req);
  const response = new Response(res);
  try {
    const code = await oauth.authorize(request, response);//
    log.info('finish authorization: ', code);
    res.locals.oauth = { code: code };
    next();
  } catch (err) {
    log.error(new OAuthError('authorizeHandler Error'), err);
    return res.status(500).json(err);
  }
}
/**
 * 带着code重定向到指定URL
 *
 * req.query.redirect_uri - 重定向URL
 * res.locals.oauth  - oauth信息
 */
async function redirectUriWithCode(req, res, next) {
  try {
    const { state, client_id: clientId } = req.query;
    const { code } = res.locals.oauth;
    if (!code || !code.authorizationCode) {
      throw new OAuthError('获取code失败', { code: 400 });
    } else if (!req.query.redirect_uri) {
      throw new OAuthError('redirect_uri不能为空', { code: 400 });
    } else {
      res.redirect(req.query.redirect_uri, { code: code.authorizationCode, state })); //url好像需要urlencode转码，这里不写了
    }
  } catch (e) {
    next(e);
  }
}
```

 2.3、客户端使用 code 向服务端获取 token

1.  _/oauth2/_tokenHandler __为前端提交账户密码的路由。通过 `POST` 请求向授权服务器获取访问令牌 (access token)__
    1.  `rant_type`：授权模式，值固定为：`authorization_code` 
    2.  `client_id`：客户端 ID　　
    3.  `client_secret`：客户端 secret　　
    4.  `redirect_uri`：使用与第一部分请求相同的 URI　　
    5.  `code`：第一部分所获的的授权码，要注意 URL 解码　　
2.  oAuth2Server 是你封装的获取授权码的模块。
3.  tokenHandler() 是获取授权码 token 的函数。
    1.  _`token_type`：令牌类型，值固定为：`Bearer`_ 
    2.  `expires_in`：访问令牌的存活时间
        
    3.  `access_token`：访问令牌
        
    4.  `refresh_token`：刷新令牌，访问令牌过期后，使用刷新令牌重新获取
        

```
// 路由文件
app.all('/oauth2/tokenHandler', oAuth2Server.tokenHandler()); // 获取token
```

```
/**
 * 授权获取token
 * @param req
 * @param res
 * @param next
 * @returns {Promise<*>}
 */
export function tokenHandler(type) {
  return async(req, res, next) => {
    const request = new Request(req);
    const response = new Response(res);
    try {
      const token = await oauth.token(request, response);
      res.locals.oauth = { token: token };
      res.header('Access-Control-Allow-Origin', '*');
      res.header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS');
      res.header('Access-Control-Allow-Headers', 'accept, content-type, x-parse-application-id, x-parse-rest-api-key, x-parse-session-token');
      next();
    } catch (err) {
      log.error(new Error('tokenHandler Error'), err);
      return res.status(500).json(err);
    }
  };
}
```