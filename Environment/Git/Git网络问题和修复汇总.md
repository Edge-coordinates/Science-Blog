---
title: Git网络问题和修复汇总
categories:
- Git
tags:
---


# Git网络问题和修复汇总
## 问题列表
### Unable to access ‘https://github.com/user_name/repository_name/’: OpenSSL SSL_read: Connection was reset, errno 10054
### fatal: unable to access 'https://github.com/ICS-Community/ICS_club.git/': schannel: failed to receive handshake, SSL/TLS connection failed

这两种错误的解决方案好像差不多？先pull再push。

虽然网上看到很多说法，其实你之前配置没问题的话我相信一般是没有问题的，你照着他们说的去做也未必能解决问题。当时查资料倒是看到一个有趣的说法，有关于自己的网络连接，我觉得这种思考是很好的，都可以提供大家的参考。

## 问题总结&解决方案
1. 线上，线下版本不契合：在本地 commit 之前在 Github 直接修改(或其他人提交)了内容，导致本地修改记录和 Github 修改记录冲突，进而报错。比如在 New Repository 的时候点了初始化 readme.md，这次创建算是一次 commit，但你的本地没有这次记录，所以就会冲突，就不能提交，就必须在 pull 的时候处理新老版本的兼容问题。  
所以处理的方法就是做一下`git pull origin master --allow-unrelated-histories`，然后再 push 即可。
2. 网络链接问题：众所周知。。。您可以先Ping一下Github，如果Ping不通，在浏览器中打开Github网址，刷新一下，再在本操作。当然，您也可以更换代理（如果有的话）试试。  
3. 图形界面报错(VSCode或GitHub Desktop报错)： 可以换用命令行执行一下push或pull操作，如果在使用命令行后仍报错，尝试上面给出的解决方案。

## 总结
1. 执行`git pull origin master --allow-unrelated-histories`  
2. 在浏览器中打开Github并刷新或更换代理。  