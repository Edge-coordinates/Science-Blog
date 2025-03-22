---
title: Python网络爬虫-requests库使用指南
date: 2022/10/14
categories:
  - - Language-Basic
    - Python
tags: null
abbrlink: f520aaed
---



## request的八个方法
requests 所有功能都能通过 "requests/api.py" 中的方法访问。它们分别是：

*   requests.request(method, url, **kwargs)
*   requests.get(url, params=None, **kwargs)
*   requests.options(url, **kwargs)
*   requests.head(url, **kwargs)
*   requests.post(url, data=None, json=None, **kwargs)
*   requests.put(url, data=None, **kwargs)
*   requests.patch(url, data=None, **kwargs)
*   requests.delete(url, **kwargs)

除了 requests.request() 外，其余 7 个方法与 http 协议中的请求方法一一对应。阅读源码后，不难发现，这 7 个方法其实都是在调用 requests.request() 方法，所以了解 requests.request() 方法提供了哪些参数就变得至关重要了。

### 对于requests.request(method, url, **kwargs)方法
- method : 请求方式，对应get/put/post等7种
- url : 拟获取页面的url链接
- **kwargs: 控制访问的参数，共15个

#### method : 请求方式
```python
r = requests.request('GET', url, **kwargs)
r = requests.request('HEAD', url, **kwargs)
r = requests.request('POST', url, **kwargs)
r = requests.request('PUT', url, **kwargs)
r = requests.request('PATCH', url, **kwargs)
r = requests.request('delete', url, **kwargs)
r = requests.request('OPTIONS', url, **kwargs)
```


#### **kwargs: 控制访问的参数，均为可选项 

```python
>>> kv = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.request('GET', 'http://python123.io/ws', params=kv)
>>> print(r.url)
http://python123.io/ws?key1=value1&key2=value2
```
|**kwargs参数列表|
| 参数              | 解释                                                                    |
|-----------------|-----------------------------------------------------------------------|
| method          | 各种方法，比如 get、options、head、post、put、patch、delete，当然也支持自定义扩展             |
| url             | 请求的 url                                                               |
| params          | 请求携带的 params                                                          |
| data            | 请求 body 中的 data                                                       |
| json            | 请求 body 中的 json 格式的 data                                              |
| headers         | 请求携带的 headers                                                         |
| cookies         | 请求携带的 cookies                                                         |
| files           | 上传文件时使用                                                               |
| auth            | 身份认证时使用                                                               |
| timeout         | 设置请求的超时时间，可以设置连接超时和读取超时                                               |
| allow_redirects | 是否允许重定向，默认 True，即允许重定向                                                |
| proxies         | 设置请求的代理，支持 http 代理以及 socks 代理（需要安装第三方库 "pip install requests[socks]"） |
| verify          | 用于 https 请求时的 ssl 证书验证，默认是开启的，如果不需要则设置为 False 即可                      |
| stream          | 是否立即下载响应内容，默认是 False，即立即下载响应内容                                        |
| cert            | 用于指定本地文件用作客户端证书                                                       |

那么发送请求时，我们可以根据自身需求去组合上述的参数。在调用 requests.request() 方法之后，会返回一个 requests.Response 对象供大家使用，关于 Response 的用法，请移步 [python 之 requests 模块 - Response](https://www.cnblogs.com/zhuosanxun/p/12641052.html) 查看。

**参考文档**

*   [https://github.com/psf/requests/blob/master/requests/api.py](https://github.com/psf/requests/blob/master/requests/api.py)