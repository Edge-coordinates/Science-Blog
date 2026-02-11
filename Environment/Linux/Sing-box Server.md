---
title: Sing-box Server
date: 2026/02/11 23:57:21
categories:
  - - Environment
    - Linux
abbrlink: a0dcc66c
---
https://sing-box.sagernet.org/installation/package-manager/#service-management 

## :material-book-multiple: Service Management

For Linux systems with [systemd][systemd], usually the installation already includes a sing-box service,
you can manage the service using the following command:

| Operation | Command                                       |
|-----------|-----------------------------------------------|
| Enable    | `sudo systemctl enable sing-box`              |
| Disable   | `sudo systemctl disable sing-box`             |
| Start     | `sudo systemctl start sing-box`               |
| Stop      | `sudo systemctl stop sing-box`                |
| Kill      | `sudo systemctl kill sing-box`                |
| Restart   | `sudo systemctl restart sing-box`             |
| Logs      | `sudo journalctl -u sing-box --output cat -e` |
| New Logs  | `sudo journalctl -u sing-box --output cat -f` |



sing-box generate inbound hysteria2  --listen :443 \
  --password $(openssl rand -hex 8) \
  --tls \
  --domain your.domain.com \
  --config /etc/sing-box/config.json \
  --print-client

version

```
root@Ubuntu:~# sing-box version
sing-box version 1.12.12

Environment: go1.25.3 linux/amd64
Tags: with_gvisor,with_quic,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_tailscale
Revision: xxxx
CGO: disabled
```

```
{
  "log": {
    "level": "info"
  },
  "dns": {
    "servers": [
      {
        "address": "https://1.1.1.1/dns-query",
        "strategy": "prefer_ipv4"
      }
    ]
  },
  "inbounds": [
    {
      "type": "hysteria2",
      "listen": "::",
      "listen_port": 10809,
      "up_mbps": 100,
      "down_mbps": 100,
      "users": [
        {
          "name": "your name",
          "password": "your pass"
        }
      ],
      "tls": {
        "enabled": true,
        "server_name": "example.com",
        "certificate_path": "/www/server/panel/vhost/cert/example.com/fullchain.pem",
        "key_path": "/www/server/panel/vhost/cert/example.com/privkey.pem"
      }
    }
  ],
  "outbounds": [
    {
      "type": "direct"
    }
  ]
}
```