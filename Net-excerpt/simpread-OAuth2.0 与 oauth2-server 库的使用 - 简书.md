---
title: simpread-OAuth2
date: 2022/10/14
categories:
  - Net-excerpt
tags: null
reprint: true
abbrlink: ff099914
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.jianshu.com](https://www.jianshu.com/p/83b0f6d82d6c)

[OAuth2.0](https://en.wikipedia.org/wiki/OAuth) 是关于授权的开放网络标准，它允许用户已第三方应用获取该用户在某一网站的私密资源，而无需提供用户名与密码，目前已在全世界得到广泛应用。

[league/oauth2-server](https://github.com/thephpleague/oauth2-server) 是一个轻量级并且功能强大的符合 OAuth2.0 协议的 PHP 库，使用它可以构建出标准的 OAuth2.0 授权服务器。

本文通过对 PHP 库：league/oauth2-server 进行实践的同时，理解 OAuth2.0 的工作流程与设计思路。

术语
--

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
4.  **JWT**：[Json Web Token](https://tools.ietf.org/html/rfc7519) 是一种用于安全传输的数据传输格式。

运行流程
----

![](http://upload-images.jianshu.io/upload_images/3364371-d32505bf7e60f960.png) flowchart.png

安装
--

推荐使用 [Composer](https://getcomposer.org/) 进行安装：

```
composer require league/oauth2-server
```

根据[授权模式](#%E6%8E%88%E6%9D%83%E6%A8%A1%E5%BC%8F)的不同，oauth2-server 提供了不同的 Interface 与 Triat 帮助实现。

_本文发布时，版本号为 7.3.1。_

**生成公钥与私钥**

公钥与私钥用于签名和验证传输的 [JWT](https://tools.ietf.org/html/rfc7519)，授权服务器使用私钥签名 JWT，资源服务器拥有公钥验证 JWT。

_oauth2-server 使用 JWT 传输访问令牌 (access token)，方便资源服务器获取其中内容，所以需要使用非对称加密。_

生成私钥，在终端中运行：

```
openssl genrsa -out private.key 2048
```

使用私钥提取私钥：

```
openssl rsa -in private.key -pubout -out public.key
```

私钥必须保密于授权服务器中，并将公钥分发给资源服务器。

**生成加密密钥**

加密密钥用于加密授权码 (auth code) 与刷新令牌 (refesh token)，AuthorizationServer(授权服务器启动类) 接受两种加密密钥，`string` 或 `defuse/php-encryption` 库的对象。

_加密授权码 (auth code) 与刷新令牌 (refesh token) 只有授权权服务器使用，所以使用对称加密。_

生成字符串密钥，在终端中输入：

```
php -r 'echo base64_encode(random_bytes(32)), PHP_EOL;'
```

生成对象，在项目根目录的终端中输入：

```
vendor/bin/generate-defuse-key
```

将获得的内容，传入 AuthorizationServer：

```
use \Defuse\Crypto\Key;
$server = new AuthorizationServer(
    $clientRepository,
    $accessTokenRepository,
    $scopeRepository,
    $privateKeyPath,
    Key::loadFromAsciiSafeString($encryptionKey) //传入加密密钥
);
```

**PHP 版本支持**

*   PHP 7.0
*   PHP 7.1
*   PHP 7.2

授权模式
----

OAuth2.0 定义了四种授权模式，以应对不同情况时的授权。

1.  授权码模式
2.  隐式授权模式
3.  密码模式
4.  客户端模式

客户端类型
-----

*   保密的：
    *   客户端可以安全的存储自己与用户的凭据（例如：有所属的服务器端）
*   公开的：
    *   客户端无法安全的存储自己与用户的凭据（例如：运行在浏览器的单页应用）

选用哪种授权模式？
---------

如果客户端是保密的，应使用[授权码模式](#%E6%8E%88%E6%9D%83%E7%A0%81%E6%A8%A1%E5%BC%8F)。

如果客户端是公开的，应使用[隐式授权模式](#%E9%9A%90%E5%BC%8F%E6%8E%88%E6%9D%83%E6%A8%A1%E5%BC%8F)。

如果用户对于此客户端高度信任（例如：第一方应用程序或操作系统程序），应使用[密码模式](#%E5%AF%86%E7%A0%81%E6%A8%A1%E5%BC%8F)。

如果客户端是以自己的名义，不与用户产生关系，应使用[客户端模式](#%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%A8%A1%E5%BC%8F)。

预先注册
----

客户端需要预先在授权服务器进行注册，用以获取 `client_id` 与 `client_secret`，也可以在注册是预先设定好 `redirect_uri`，以便于之后可以使用默认的 `redirect_uri`。

授权码模式
-----

授权码模式是 OAuth2.0 种功能最完整，流程最严密的一种模式，如果你使用过 Google 或 QQ 登录过第三方应用程序，应该会对这个流程的第一部分很熟悉。

#### 流程

**第一部分（用户可见）**

用户访问客户端，客户端将用户导向授权服务器时，将以下参数通过 `GET query` 传入：

*   `response_type`：授权类型，必选项，值固定为：`code`
*   `client_id`：客户端 ID，必选项
*   `redirect_uri`：重定向 URI，可选项，不填写时默认预先注册的重定向 URI
*   `scope`：权限范围，可选项，以空格分隔
*   `state`：[CSRF](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0) 令牌，可选项，但强烈建议使用，应将该值存储与用户会话中，以便在返回时验证

用户选择是否给予客户端授权

假设用户给予授权，授权服务器将用户导向客户端事先指定的 `redirect_uri`，并将以下参数通过 `GET query` 传入：

*   `code`：授权码 (Authorization code)
*   `state`：请求中发送的 `state`，原样返回。客户端将此值与用户会话中的值进行对比，以确保授权码响应的是此客户端而非其他客户端程序

**第二部分（用户不可见）**

客户端已得到授权，通过 `POST` 请求向授权服务器获取访问令牌 (access token)：

*   `grant_type`：授权模式，值固定为：`authorization_code`
*   `client_id`：客户端 ID
*   `client_secret`：客户端 secret
*   `redirect_uri`：使用与第一部分请求相同的 URI
*   `code`：第一部分所获的的授权码，要注意 URL 解码

授权服务器核对授权码与重定向 URI，确认无误后，向客户端响应下列内容：

*   `token_type`：令牌类型，值固定为：`Bearer`
    
*   `expires_in`：访问令牌的存活时间
    
*   `access_token`：访问令牌
    
*   `refresh_token`：刷新令牌，访问令牌过期后，使用刷新令牌重新获取
    

#### 使用 oauth2-server 实现

##### 初始化

OAuth2.0 只是协议，在实现上需要联系到用户与数据库存储，oauth2-server 的新版本并没有指定某种数据库，但它提供了 [Interfaces](#Interfaces) 与 [Traits](#Traits) 帮助我们实现，这让我们可以方便的使用任何形式的数据存储方式，这种方便的代价就是需要我们自行创建 [Repositories](#Repositories) 与 [Entities](#Entities)。

##### 初始化 server

```
// 初始化存储库
$clientRepository = new ClientRepository(); // Interface: ClientRepositoryInterface
$scopeRepository = new ScopeRepository(); // Interface: ScopeRepositoryInterface
$accessTokenRepository = new AccessTokenRepository(); // Interface: AccessTokenRepositoryInterface
$authCodeRepository = new AuthCodeRepository(); // Interface: AuthCodeRepositoryInterface
$refreshTokenRepository = new RefreshTokenRepository(); // Interface: RefreshTokenRepositoryInterface
$userRepository = new UserRepository(); //Interface: UserRepositoryInterface

// 私钥与加密密钥
$privateKey = 'file://path/to/private.key';
//$privateKey = new CryptKey('file://path/to/private.key', 'passphrase'); // 如果私钥文件有密码
$encryptionKey = 'lxZFUEsBCJ2Yb14IF2ygAHI5N4+ZAUXXaSeeJm6+twsUmIen'; // 加密密钥字符串
// $encryptionKey = Key::loadFromAsciiSafeString($encryptionKey); //如果通过 generate-defuse-key 脚本生成的字符串，可使用此方法传入

// 初始化 server
$server = new \League\OAuth2\Server\AuthorizationServer(
    $clientRepository,
    $accessTokenRepository,
    $scopeRepository,
    $privateKey,
    $encryptionKey
);
```

##### 初始化授权码类型

```
// 授权码授权类型初始化
$grant = new \League\OAuth2\Server\Grant\AuthCodeGrant(
    $authCodeRepository,
    $refreshTokenRepository,
    new \DateInterval('PT10M') // 设置授权码过期时间为10分钟
);
$grant->setRefreshTokenTTL(new \DateInterval('P1M')); // 设置刷新令牌过期时间1个月

// 将授权码授权类型添加进 server
$server->enableGrantType(
    $grant,
    new \DateInterval('PT1H') // 设置访问令牌过期时间1小时
);
```

_[DateInterval](http://php.net/manual/zh/class.dateinterval.php)_

##### 使用

_注意：这里的示例演示的是 Slim Framework 的用法，Slim 不是这个库的必要条件，只需要请求与响应符合 [PSR-7](https://www.php-fig.org/psr/psr-7/) 规范即可。_

用户向客户端提出 OAuth 登录请求，客户端将用户重定向授权服务器的地址（例如：[https://example.com/authorize?response_type=code&client_id=](https://example.com/authorize?response_type=code&client_id=){client_id}&redirect_uri={redirect_uri}&scope{scope}&state={state})：

```
$app->get('/authorize', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {
   
    try {
        // 验证 HTTP 请求，并返回 authRequest 对象
        $authRequest = $server->validateAuthorizationRequest($request);
        // 此时应将 authRequest 对象序列化后存在当前会话(session)中
        $_SESSION['authRequest'] = serialize($authRequest);
        // 然后将用户重定向至登录入口或在当前地址直接响应登录页面
        return $response->getBody()->write(file_get_contents("login.html"));
        
    } catch (OAuthServerException $exception) {
        // 可以捕获 OAuthServerException，将其转为 HTTP 响应
        return $exception->generateHttpResponse($response);
        
    } catch (\Exception $exception) {
        // 其他异常
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
        
    }
});
```

此时展示给用户的是这样的页面：

![](http://upload-images.jianshu.io/upload_images/3364371-7242d85781cdfe64.png) qq-oauth.png

用户提交登录后，设置好用户实体 (userEntity)：

```
$app->post('/login', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {
    try {
        // 在会话(session)中取出 authRequest 对象
        $authRequest = unserialize($_SESSION['authRequest']);
        // 设置用户实体(userEntity)
        $authRequest->setUser(new UserEntity(1));
        // 设置权限范围
        $authRequest->setScopes(['basic'])
        // true = 批准，false = 拒绝
        $authRequest->setAuthorizationApproved(true);
        // 完成后重定向至客户端请求重定向地址
        return $server->completeAuthorizationRequest($authRequest, $response);
    } catch (OAuthServerException $exception) {
        // 可以捕获 OAuthServerException，将其转为 HTTP 响应
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        // 其他异常
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

客户端通过授权码请求访问令牌：

```
$app->post('/access_token', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {

    try {
        // 这里只需要这一行就可以，具体的判断在 Repositories 中
        return $server->respondToAccessTokenRequest($request, $response);
    } catch (\League\OAuth2\Server\Exception\OAuthServerException $exception) {
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

隐式授权模式
------

隐式授权相当于是授权码模式的简化版本：

#### 流程 (用户可见)

用户访问客户端，客户端将用户导向授权服务器时，将以下参数通过 `GET query` 传入：

*   `response_type`：授权类型，必选项，值固定为：`token`
*   `client_id`：客户端 ID，必选项
*   `redirect_uri`：重定向 URI，可选项，不填写时默认预先注册的重定向 URI
*   `scope`：权限范围，可选项，以空格分隔
*   `state`：[CSRF](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0) 令牌，可选项，但强烈建议使用，应将该值存储与用户会话中，以便在返回时验证

用户选择是否给予客户端授权

假设用户给予授权，授权服务器将用户导向客户端事先指定的 `redirect_uri`，并将以下参数通过 `GET query` 传入：

*   `token_type`：令牌类型，值固定为：`Bearer`
*   `expires_in`：访问令牌的存活时间
*   `access_token`：访问令牌
*   `state`：请求中发送的 `state`，原样返回。客户端将此值与用户会话中的值进行对比，以确保授权码响应的是此应用程序而非其他应用程序

整个流程与授权码模式的第一部分类似，只是授权服务器直接响应了访问令牌，跳过了授权码的步骤。它适用于没有服务器，完全运行在前端的应用程序。

_此模式下没有刷新令牌 (refresh token) 的返回。_

#### 使用 oauth2-server 实现

**[初始化 server](#%E5%88%9D%E5%A7%8B%E5%8C%96)**

##### 初始化授权码类型

```
// 将隐式授权类型添加进 server
$server->enableGrantType(
    new ImplicitGrant(new \DateInterval('PT1H')),
    new \DateInterval('PT1H') // 设置访问令牌过期时间1小时
);
```

_[DateInterval](http://php.net/manual/zh/class.dateinterval.php)_

##### 使用

_注意：这里的示例演示的是 Slim Framework 的用法，Slim 不是这个库的必要条件，只需要请求与响应符合 [PSR-7](https://www.php-fig.org/psr/psr-7/) 规范即可。_

```
$app->post('/login', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {
    try {
        // 在会话(session)中取出 authRequest 对象
        $authRequest = unserialize($_SESSION['authRequest']);
        // 设置用户实体(userEntity)
        $authRequest->setUser(new UserEntity(1));
        // 设置权限范围
        $authRequest->setScopes(['basic'])
        // true = 批准，false = 拒绝
        $authRequest->setAuthorizationApproved(true);
        // 完成后重定向至客户端请求重定向地址
        return $server->completeAuthorizationRequest($authRequest, $response);
    } catch (OAuthServerException $exception) {
        // 可以捕获 OAuthServerException，将其转为 HTTP 响应
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        // 其他异常
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

此时展示给用户的是这样的页面：

![](http://upload-images.jianshu.io/upload_images/3364371-7242d85781cdfe64.png) qq-oauth.png

用户提交登录后，设置好用户实体 (userEntity)：

```
$app->post('/login', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {
   
    try {
          // 在会话(session)中取出 authRequest 对象
        $authRequest = unserialize($_SESSION['authRequest']);
                // 设置用户实体(userEntity)
            $authRequest->setUser(new UserEntity(1));
                // 设置权限范围
                $authRequest->setScopes(['basic'])
                // true = 批准，false = 拒绝
            $authRequest->setAuthorizationApproved(true);
                // 完成后重定向至客户端请求重定向地址
            return $server->completeAuthorizationRequest($authRequest, $response);
    } catch (OAuthServerException $exception) {
        // 可以捕获 OAuthServerException，将其转为 HTTP 响应
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        // 其他异常
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

密码模式
----

密码模式是由用户提供给客户端账号密码来获取访问令牌，这属于危险行为，所以此模式只适用于高度信任的客户端（例如第一方应用程序）。客户端不应存储用户的账号密码。

_OAuth2 协议规定此模式不需要传 `client_id` & `client_secret`，但 oauth-server 库需要_

#### 流程

客户端要求用户提供授权凭据，通常是账号密码

然后，客户端发送 `POST` 请求至授权服务器，携带以下参数：

*   `grant_type`：授权类型，必选项，值固定为：`password`
*   `client_id`：客户端 ID，必选项
*   `client_secret`：客户端 secret
*   `scope`：权限范围，可选项，以空格分隔
*   `username`：用户账号
*   `password`：用户密码

授权服务器响应以下内容：

*   `token_type`：令牌类型，值固定为：`Bearer`
*   `expires_in`：访问令牌的存活时间
*   `access_token`：访问令牌
*   `refresh_token`：刷新令牌，访问令牌过期后，使用刷新令牌重新获取

#### 使用 oauth2-server 实现

**[初始化 server](#%E5%88%9D%E5%A7%8B%E5%8C%96)**

##### 初始化授权码类型

```
$grant = new \League\OAuth2\Server\Grant\PasswordGrant(
     $userRepository,
     $refreshTokenRepository
);

$grant->setRefreshTokenTTL(new \DateInterval('P1M')); // 设置刷新令牌过期时间1个月

// 将密码授权类型添加进 server
$server->enableGrantType(
    $grant,
    new \DateInterval('PT1H') // 设置访问令牌过期时间1小时
);
```

_[DateInterval](http://php.net/manual/zh/class.dateinterval.php)_

##### 使用

_注意：这里的示例演示的是 Slim Framework 的用法，Slim 不是这个库的必要条件，只需要请求与响应符合 [PSR-7](https://www.php-fig.org/psr/psr-7/) 规范即可。_

```
$app->post('/access_token', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {

    try {
        // 这里只需要这一行就可以，具体的判断在 Repositories 中
        return $server->respondToAccessTokenRequest($request, $response);
    } catch (\League\OAuth2\Server\Exception\OAuthServerException $exception) {
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

客户端模式
-----

客户端模式是指以客户端的名义，而不是用户的名义，向授权服务器获取认证。在这个模式下，用户与授权服务器不产生关系，用户只能感知到的客户端，所产生的资源也都由客户端处理。

#### 流程

客户端发送 `POST` 请求至授权服务器，携带以下参数：

*   `grant_type`：授权类型，必选项，值固定为：`client_credentials`
*   `client_id`：客户端 ID，必选项
*   `client_secret`：客户端 secret
*   `scope`：权限范围，可选项，以空格分隔

授权服务器响应以下内容：

*   `token_type`：令牌类型，值固定为：`Bearer`
*   `expires_in`：访问令牌的存活时间
*   `access_token`：访问令牌

_此模式下无需刷新令牌 (refresh token) 的返回。_

#### 使用 oauth2-server 实现

**[初始化 server](#%E5%88%9D%E5%A7%8B%E5%8C%96)**

##### 初始化授权码类型

```
// 将客户端授权类型添加进 server
$server->enableGrantType(
    new \League\OAuth2\Server\Grant\ClientCredentialsGrant(),
    new \DateInterval('PT1H') // 设置访问令牌过期时间1小时
);
```

_[DateInterval](http://php.net/manual/zh/class.dateinterval.php)_

##### 使用

_注意：这里的示例演示的是 Slim Framework 的用法，Slim 不是这个库的必要条件，只需要请求与响应符合 [PSR-7](https://www.php-fig.org/psr/psr-7/) 规范即可。_

```
$app->post('/access_token', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {

    try {
        // 这里只需要这一行就可以，具体的判断在 Repositories 中
        return $server->respondToAccessTokenRequest($request, $response);
    } catch (\League\OAuth2\Server\Exception\OAuthServerException $exception) {
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

刷新访问令牌 (access token)
---------------------

访问令牌有一个较短的存活时间，在过期后，客户端通过刷新令牌来获得新的访问令牌与刷新令牌。当用户长时间不活跃，刷新令牌也过期后，就需要重新获取授权。

#### 流程

客户端发送 `POST` 请求至授权服务器，携带以下参数：

*   `grant_type`：授权类型，必选项，值固定为：`refresh_token`
*   `client_id`：客户端 ID，必选项
*   `client_secret`：客户端 secret
*   `scope`：权限范围，可选项，以空格分隔
*   `refresh_token`：刷新令牌

授权服务器响应以下内容：

*   `token_type`：令牌类型，值固定为：`Bearer`
*   `expires_in`：访问令牌的存活时间
*   `access_token`：访问令牌
*   `refresh_token`：刷新令牌，访问令牌过期后，使用刷新令牌重新获取

#### 使用 oauth2-server 实现

**[初始化 server](#%E5%88%9D%E5%A7%8B%E5%8C%96)**

##### 初始化授权码类型

```
$grant = new \League\OAuth2\Server\Grant\RefreshTokenGrant($refreshTokenRepository);
$grant->setRefreshTokenTTL(new \DateInterval('P1M')); // 新的刷新令牌过期时间1个月

// 将刷新访问令牌添加进 server
$server->enableGrantType(
    $grant,
    new \DateInterval('PT1H') // 新的访问令牌过期时间1小时
);
```

_[DateInterval](http://php.net/manual/zh/class.dateinterval.php)_

##### 使用

```
$app->post('/access_token', function (ServerRequestInterface $request, ResponseInterface $response) use ($server) {

    try {
        // 这里只需要这一行就可以，具体的判断在 Repositories 中
        return $server->respondToAccessTokenRequest($request, $response);
    } catch (\League\OAuth2\Server\Exception\OAuthServerException $exception) {
        return $exception->generateHttpResponse($response);
    } catch (\Exception $exception) {
        $body = new Stream(fopen('php://temp', 'r+'));
        $body->write($exception->getMessage());
        return $response->withStatus(500)->withBody($body);
    }
});
```

资源服务器验证访问令牌
-----------

oauth2-server 为资源服务器提供了一个中间件用于验证访问令牌。

客户端需要在 `HTTP Header` 中使用 `Authorization` 传入访问令牌，如果通过，中间件将会在 `request` 中加入对应数据：

*   `oauth_access_token_id`：访问令牌 id
*   `oauth_client_id`: 客户端 id
*   `oauth_user_id`：用户 id
*   `oauth_scopes`：权限范围

授权不通过，则抛出 `OAuthServerException::accessDenied` 异常。

```
// 初始化
$accessTokenRepository = new AccessTokenRepository(); // Interface: AccessTokenRepositoryInterface

// 授权服务器分发的公钥
$publicKeyPath = 'file://path/to/public.key';
        
// 创建 ResourceServer
$server = new \League\OAuth2\Server\ResourceServer(
    $accessTokenRepository,
    $publicKeyPath
);

// 中间件
new \League\OAuth2\Server\Middleware\ResourceServerMiddleware($server);
```

如果所用路由不支持中间件，可自行实现，符合 [PSR-7](https://www.php-fig.org/psr/psr-7/) 规范即可 ：

```
try {
    $request = $server->validateAuthenticatedRequest($request);
} catch (OAuthServerException $exception) {
    return $exception->generateHttpResponse($response);
} catch (\Exception $exception) {
    return (new OAuthServerException($exception->getMessage(), 0, 'unknown_error', 500))->generateHttpResponse($response);
}
```

oauth2-server 实现
----------------

oauth2-server 的实现需要我们手动创建 [Repositories](#Repositories) 与 [Entities](#Entities)，下面展示一个项目目录示例：

```
- Entities
    - AccessTokenEntity.php
    - AuthCodeEntity.php
    - ClientEntity.php
    - RefreshTokenEntity.php
    - ScopeEntity.php
    - UserEntity.php
- Repositories
    - AccessTokenRepository.php
    - AuthCodeRepository.php
    - ClientRepository.php
    - RefreshTokenRepository.php
    - ScopeRepository.php
    - UserRepository.php
```

### Repositories

Repositories 里主要是处理关于授权码、访问令牌等数据的存储逻辑，oauth2-server 提供了 [Interfaces](#Interfaces) 来定义所需要实现的方法。

```
class AccessTokenRepository implements AccessTokenRepositoryInterface
{
    /**
     * @return AccessTokenEntityInterface
     */
    public function getNewToken(ClientEntityInterface $clientEntity, array $scopes, $userIdentifier = null)
    {
        // 创建新访问令牌时调用方法
        // 需要返回 AccessTokenEntityInterface 对象
        // 需要在返回前，向 AccessTokenEntity 传入参数中对应属性
        // 示例代码：
        $accessToken = new AccessTokenEntity();
        $accessToken->setClient($clientEntity);
        foreach ($scopes as $scope) {
            $accessToken->addScope($scope);
        }
        $accessToken->setUserIdentifier($userIdentifier);

        return $accessToken;
    }

    public function persistNewAccessToken(AccessTokenEntityInterface $accessTokenEntity)
    {
        // 创建新访问令牌时调用此方法
        // 可以用于持久化存储访问令牌，持久化数据库自行选择
        // 可以使用参数中的 AccessTokenEntityInterface 对象，获得有价值的信息：
        // $accessTokenEntity->getIdentifier(); // 获得令牌唯一标识符
        // $accessTokenEntity->getExpiryDateTime(); // 获得令牌过期时间
        // $accessTokenEntity->getUserIdentifier(); // 获得用户标识符
        // $accessTokenEntity->getScopes(); // 获得权限范围
        // $accessTokenEntity->getClient()->getIdentifier(); // 获得客户端标识符
    }

    public function revokeAccessToken($tokenId)
    {
        // 使用刷新令牌创建新的访问令牌时调用此方法
        // 参数为原访问令牌的唯一标识符
        // 可将其在持久化存储中过期
    }

    public function isAccessTokenRevoked($tokenId)
    {
        // 资源服务器验证访问令牌时将调用此方法
        // 用于验证访问令牌是否已被删除
        // return true 已删除，false 未删除
        return false;
    }
}
```

```
class AuthCodeRepository implements AuthCodeRepositoryInterface
{
    /**
     * @return AuthCodeEntityInterface
     */
    public function getNewAuthCode()
    {
        // 创建新授权码时调用方法
        // 需要返回 AuthCodeEntityInterface 对象
        return new AuthCodeEntity();
    }

    public function persistNewAuthCode(AuthCodeEntityInterface $authCodeEntity)
    {
        // 创建新授权码时调用此方法
        // 可以用于持久化存储授权码，持久化数据库自行选择
        // 可以使用参数中的 AuthCodeEntityInterface 对象，获得有价值的信息：
        // $authCodeEntity->getIdentifier(); // 获得授权码唯一标识符
        // $authCodeEntity->getExpiryDateTime(); // 获得授权码过期时间
        // $authCodeEntity->getUserIdentifier(); // 获得用户标识符
        // $authCodeEntity->getScopes(); // 获得权限范围
        // $authCodeEntity->getClient()->getIdentifier(); // 获得客户端标识符
    }

    public function revokeAuthCode($codeId)
    {
        // 当使用授权码获取访问令牌时调用此方法
        // 可以在此时将授权码从持久化数据库中删除
        // 参数为授权码唯一标识符
    }

    public function isAuthCodeRevoked($codeId)
    {
        // 当使用授权码获取访问令牌时调用此方法
        // 用于验证授权码是否已被删除
        // return true 已删除，false 未删除
        return false;
    }
}
```

```
class ClientRepository implements ClientRepositoryInterface
{
    /**
     * @return ClientEntityInterface
     */
    public function getClientEntity($clientIdentifier, $grantType = null, $clientSecret = null, $mustValidateSecret = true)
    {
        // 获取客户端对象时调用方法，用于验证客户端
        // 需要返回 ClientEntityInterface 对象
        // $clientIdentifier 客户端唯一标识符
        // $grantType 代表授权类型，根据类型不同，验证方式也不同
        // $clientSecret 代表客户端密钥，是客户端事先在授权服务器中注册时得到的
        // $mustValidateSecret 代表是否需要验证客户端密钥
        $client = new ClientEntity();
        $client->setIdentifier($clientIdentifier);

        return $client;
    }
}
```

```
class RefreshTokenRepository implements RefreshTokenRepositoryInterface
{
    /**
     * @return RefreshTokenEntityInterface
     */
    public function getNewRefreshToken()
    {
        // 创建新授权码时调用方法
        // 需要返回 RefreshTokenEntityInterface 对象
        return new RefreshTokenEntity();
    }

    public function persistNewRefreshToken(RefreshTokenEntityInterface $refreshTokenEntity)
    {
        // 创建新刷新令牌时调用此方法
        // 用于持久化存储授刷新令牌
        // 可以使用参数中的 RefreshTokenEntityInterface 对象，获得有价值的信息：
        // $refreshTokenEntity->getIdentifier(); // 获得刷新令牌唯一标识符
        // $refreshTokenEntity->getExpiryDateTime(); // 获得刷新令牌过期时间
        // $refreshTokenEntity->getAccessToken()->getIdentifier(); // 获得访问令牌标识符
    }

    public function revokeRefreshToken($tokenId)
    {
        // 当使用刷新令牌获取访问令牌时调用此方法
        // 原刷新令牌将删除，创建新的刷新令牌
        // 参数为原刷新令牌唯一标识
        // 可在此删除原刷新令牌
    }

    public function isRefreshTokenRevoked($tokenId)
    {
        // 当使用刷新令牌获取访问令牌时调用此方法
        // 用于验证刷新令牌是否已被删除
        // return true 已删除，false 未删除
        return false;
    }
}
```

```
class ScopeRepository implements ScopeRepositoryInterface
{
    /**
     * @return ScopeEntityInterface
     */
    public function getScopeEntityByIdentifier($identifier)
    {
        // 验证权限是否在权限范围中会调用此方法
        // 参数为单个权限标识符
        // ......
        // 验证成功则返回 ScopeEntityInterface 对象
        $scope = new ScopeEntity();
        $scope->setIdentifier($identifier);

        return $scope;
    }

    public function finalizeScopes(
        array $scopes,
        $grantType,
        ClientEntityInterface $clientEntity,
        $userIdentifier = null
    ) {
        // 在创建授权码与访问令牌前会调用此方法
        // 用于验证权限范围、授权类型、客户端、用户是否匹配
        // 可整合进项目自身的权限控制中
        // 必须返回 ScopeEntityInterface 对象可用的 scope 数组
        // 示例：
        // $scope = new ScopeEntity();
        // $scope->setIdentifier('example');
        // $scopes[] = $scope;

        return $scopes;
    }
}
```

```
class UserRepository implements UserRepositoryInterface
{
    /**
     * @return UserEntityInterface
     */
    public function getUserEntityByUserCredentials(
        $username,
        $password,
        $grantType,
        ClientEntityInterface $clientEntity
    ) {
        // 验证用户时调用此方法
        // 用于验证用户信息是否符合
        // 可以验证是否为用户可使用的授权类型($grantType)与客户端($clientEntity)
        // 验证成功返回 UserEntityInterface 对象
        $user = new UserEntity();
        $user->setIdentifier(1);

        return $user;
    }
}
```

### Entities

Entities 里是 oauth2-server 处理授权与认证逻辑的类，它为我们提供了 [Interfaces](#Interfaces) 来定义需要实现的方法，同时提供了 [Traits](#Traits) 帮助我们实现，可以选择使用，有需要时也可以重写。

```
class AccessTokenEntity implements AccessTokenEntityInterface
{
    use AccessTokenTrait, TokenEntityTrait, EntityTrait;
}
```

```
class AuthCodeEntity implements AuthCodeEntityInterface
{
    use EntityTrait, TokenEntityTrait, AuthCodeTrait;
}
```

```
class ClientEntity implements ClientEntityInterface
{
    use EntityTrait, ClientTrait;
}
```

```
class RefreshTokenEntity implements RefreshTokenEntityInterface
{
    use RefreshTokenTrait, EntityTrait;
}
```

```
class ScopeEntity implements ScopeEntityInterface
{
    use EntityTrait;
    
    // 没有 Trait 实现这个方法，需要自行实现
    // oauth2-server 项目的测试代码的实现例子
    public function jsonSerialize()
    {
        return $this->getIdentifier();
    }
}
```

```
class UserEntity implements UserEntityInterface
{
    use EntityTrait;
}
```

### Interfaces

**Repositories**

*   League\OAuth2\Server\Repositories\AccessTokenRepositoryInterface.php
    
*   League\OAuth2\Server\Repositories\AuthCodeRepositoryInterface.php
    
*   League\OAuth2\Server\Repositories\ClientRepositoryInterface.php
    
*   League\OAuth2\Server\Repositories\RefreshTokenRepositoryInterface.php
    
*   League\OAuth2\Server\Repositories\ScopeRepositoryInterface.php
    
*   League\OAuth2\Server\Repositories\UserRepositoryInterface.php
    

**Entities**

*   League\OAuth2\Server\Entities\AccessTokenEntityInterface.php
*   League\OAuth2\Server\Entities\AuthCodeEntityInterface.php
*   League\OAuth2\Server\Entities\ClientEntityInterface.php
*   League\OAuth2\Server\Entities\RefreshTokenEntityInterface.php
*   League\OAuth2\Server\Entities\ScopeEntityInterface.php
*   League\OAuth2\Server\Entities\TokenInterface.php
*   League\OAuth2\Server\Entities\UserEntityInterface.php

### Traits

*   League\OAuth2\Server\Entities\Traits\AccessTokenTrait.php
*   League\OAuth2\Server\Entities\Traits\AuthCodeTrait.php
*   League\OAuth2\Server\Entities\Traits\ClientTrait.php
*   League\OAuth2\Server\Entities\Traits\EntityTrait.php
*   League\OAuth2\Server\Entities\Traits\RefreshTokenTrait.php
*   League\OAuth2\Server\Entities\Traits\ScopeTrait.php
*   League\OAuth2\Server\Entities\Traits\TokenEntityTrait.php

事件
--

oauth2-server 预设了一些事件，目前官方文档中只有两个，余下的可以在 RequestEvent.php 文件中查看。

##### client.authentication.failed

```
$server->getEmitter()->addListener(
    'client.authentication.failed',
    function (\League\OAuth2\Server\RequestEvent $event) {
        // do something
    }
);
```

客户端身份验证未通过时触发此事件。你可以在客户端尝试 `n` 次失败后禁止它一段时间内的再次尝试。

##### user.authentication.failed

```
$server->getEmitter()->addListener(
    'user.authentication.failed',
    function (\League\OAuth2\Server\RequestEvent $event) {
        // do something
    }
);
```

用户身份验证未通过时触发此事件。你可以通过这里提醒用户重置密码，或尝试 `n` 次后禁止用户再次尝试。

参考文章
----

《oauth2-server 官方文档》([https://oauth2.thephpleague.com/](https://oauth2.thephpleague.com/))

《理解 OAuth 2.0》- 阮一峰（[http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)）