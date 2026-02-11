---
title: WSL apt-get卡死
date: 2026/02/11 23:57:21
categories:
  - - Environment
    - Linux
abbrlink: 6d996757
---
- [解决apt卡住问题](#解决apt卡住问题)
      - [You:](#you)
      - [ChatGPT:](#chatgpt)
  - [修复方案](#修复方案)


# 解决apt卡住问题

#### You:
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  ibverbs-providers libibverbs1 libnet1 libnl-3-200 libnl-route-3-200 libpcap0.8t64
The following NEW packages will be installed:
  ibverbs-providers libibverbs1 libnet1 libnl-3-200 libnl-route-3-200 libpcap0.8t64 ngrep
0 upgraded, 7 newly installed, 0 to remove and 39 not upgraded.
Need to get 922 kB of archives.
After this operation, 2911 kB of additional disk space will be used.
Do you want to continue? [Y/n]
0% [Connecting to archive.ubuntu.com]

卡住的解决方案

#### ChatGPT:
当 `apt` 卡在 **0% \[Connecting to archive.ubuntu.com]** 的时候，本质就是：\
**网络不通 / DNS 不通 / 源地址太慢 / IPv6 问题**。

给你一个从简单到彻底的排查 & 解决方式合集，不啰嗦：

—

先试两个最常见的解决：

1）强制使用 IPv4（很多 VPS 或 WSL 出问题在这里）

```
sudo apt-get -o Acquire::ForceIPv4=true update
```

然后再安装：

```
sudo apt-get -o Acquire::ForceIPv4=true install ngrep
```

2）更换国内/更快的镜像源（例如阿里云）
编辑：

```
sudo nano /etc/apt/sources.list
```

替换为：

```
deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
```

更新：

```
sudo apt update
```

—

如果还不行 → DNS 问题

修改 `/etc/resolv.conf`：

```
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "nameserver 1.1.1.1" >> /etc/resolv.conf'
```

再执行：

```
sudo apt update
```

—

如果依旧卡 → 直接验证网络连通性

```
ping archive.ubuntu.com
curl http://archive.ubuntu.com/
```

没有反应 → 换域名或加代理\
例如 Cloudflare 镜像（速度很好）：

```
deb http://ubuntu.cloudflare-dns.com/ jammy main
```

—

WSL 特别注意：

如果你是在 WSL 内卡住，大概率是 Windows DNS 泄漏问题

## 修复方案

执行快速修复：

```
echo "[network]" | sudo tee -a /etc/wsl.conf
echo "generateResolvConf = false" | sudo tee -a /etc/wsl.conf
sudo rm /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

然后

```
wsl --shutdown
```

重新打开 WSL → `sudo apt update`

—

总结
最推荐你直接试三步：

```
sudo apt-get -o Acquire::ForceIPv4=true update
sudo apt-get -o Acquire::ForceIPv4=true upgrade
sudo apt-get -o Acquire::ForceIPv4=true install ngrep
```

如果还卡，请告诉我：
• 你是否在 VPS？（地区？）\
• 是否在使用 WSL？\
• `ping archive.ubuntu.com` 是否通？

我能根据具体环境给你最精准、最快速的配置。科学地折腾比瞎撞墙有趣多了。
