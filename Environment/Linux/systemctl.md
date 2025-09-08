---
title: systemctl
date: 2025/4/26 17:44:47
categories:
  - - Environment
    - Linux
abbrlink: c53d77f
---

服务管理

设置开机自启， 并立即启动服务。  
systemctl enable --now hysteria-server.service

重启服务， 通常在修改配置文件后执行。  
systemctl restart hysteria-server.service

查询服务状态。  
systemctl status hysteria-server.service

systemctl stop hysteria-server.service

sudo systemctl status shadowsocks-libev