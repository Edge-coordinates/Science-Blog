---
title: Caddy使用
date: 2022/10/14
categories:
  - Linux
abbrlink: 77c82341
tags:
---

配置文件路径一般在： `/etc/caddy/Caddyfile`
当配置文件更新之后：`systemctl reload caddy`


## 常用命令总结：
```powershell
systemctl reload caddy # 重载Caddy服务
```

## 一些配置示例

### 纯静态网站
```
booka.wasteland.ink {
    root * /www/wwwroot/booka.wasteland.ink/src/public
    file_server
    encode gzip
}
```

### Wordpress
```
about.ics.ink {
	root * /www/wwwroot/about.ics.ink
	php_fastcgi unix//var/php-fpm/phpfpm74.socks {
		try_files {path} {path}/index.php =404
	}
	file_server
	encode gzip
	rewrite @notfile /index.php
	@notfile {
		not {
			file

		}
	}
	rewrite /wp-admin/ /{path}
}
```

### 重定向域名
有的时候，可能同时需要绑定xxx.xyz和www.xxx.xyz，那么如下
```
rereadchina.com {
	redir https://www.rereadchina.com
}
```

### 代理某个端口
```
alist.ics.ink {
	reverse_proxy 127.0.0.1:5244
}
```