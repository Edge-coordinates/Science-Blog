---
title: 在 VM Linux中装载共享文件夹
date: 2022/10/14
categories:
  - Linux
abbrlink: 703be9e5
tags:
---


## 非永久挂载

启用共享文件夹后，除默认位置 `/mnt/hgfs` ~~**可能也没有哟~**~~ 外，您还可以将共享文件夹中的一个或多个目录 / 子目录装载到文件系统中的任意位置。

VMware Tools 会根据 Linux 客户机操作系统的内核版本，使用不同的组件来提供共享文件夹功能。在版本 4.0 之前的 Linux 内核中，VMware Tools 服务脚本会加载一个驱动程序来执行装载。Linux 内核 4.0 及更高版本使用 FUSE 文件系统组件。

您可以使用不同的装载命令将所有共享、某个共享或共享中的某个子目录装载到文件系统中的任意位置。这些命令也会因客户机 Linux 内核版本的不同而有所不同。

<table><caption>表 1. 装载命令语法 </caption><colgroup><col> <col> <col> </colgroup><thead><tr><th>4.0 之前的 Linux 内核</th><th>4.0 及更高版本的 Linux 内核</th><th>说明</th></tr></thead><tbody><tr><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__1 "><code>mount -t vmhgfs .host:/ /home/user1/shares</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__2 "><code>/usr/bin/vmhgfs-fuse .host:/ /home/user1/shares -o subtype=vmhgfs-fuse,allow_other</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__3 ">将所有共享装载到 /home/user1/shares</td></tr><tr><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__1 "><code>mount -t vmhgfs .host:/foo /tmp/foo</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__2 "><code>/usr/bin/vmhgfs-fuse .host:/foo /tmp/foo -o subtype=vmhgfs-fuse,allow_other</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__3 ">将名为 <code>foo</code> 的共享装载到 <code>/tmp/foo</code></td></tr><tr><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__1 "><code>mount -t vmhgfs .host:/foo/bar /var/lib/bar</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__2 "><code>/usr/bin/vmhgfs-fuse .host:/foo/bar /var/lib/bar -o subtype=vmhgfs-fuse,allow_other</code></td><td headers="GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758__ROW_49E8A75B20BB45AF9FDE0F0CF906E1C5__entry__3 ">将共享 <code>foo</code> 中的子目录 <code>bar</code> 装载到 /var/lib/bar</td></tr></tbody></table>

对于版本 4.0 之前的 Linux 内核，除了标准 `mount` 语法之外，您还可以使用 VMware 特定的选项。输入命令 `/sbin/mount.vmhgfs -h` 可列出这些选项。

对于 Linux 内核版本 4.0 或更高版本，输入命令 `/usr/bin/vmhgfs-fuse -h` 可列出可用的选项。

>注： 
>1. 如果共享文件夹被禁用或共享不存在，装载操作将失败。系统不会提示您重新运行 VMware Tools vmware-config-tools.pl 配置程序。  
>2. 如果等待挂在目录下有文件，在命令中加上  -o nonempty (比如加在末尾：/usr/bin/vmhgfs-fuse .host:/ /home/user1/shares -o subtype=vmhgfs-fuse,allow_other  -o nonempty) **如果将目录挂载到非空目录，该目录之前的文件将无法访问**  
>3.   若提示错误：`fusermount: option allow_other only allowed if 'user_allow_other' is set in /etc/fuse.conf` 则在/etc/fuse.conf中将user_allow_other前的注释符合#删除保存(需root权限)

## 永久挂载





## 删除挂载

卸载的话使用下面的命令：  
`sudo umount -f /mnt/shared`

>注意：
共享文件夹的名称千万不要和挂载点的名称相同。比如，上面的挂载点是/mnt/shared，如果共享文件夹的名字也是shared的话，在挂载的时候就会出现如下的错误信息(看http://www.virtualbox.org/ticket/2265)：
/sbin/mount.vboxsf: mounting failed with the error: Protocol error

 

提示错误 `/sbin/mount.vboxsf: mounting failed with the error: Invalid argument` 
或者重启虚拟机后没有挂载共享文件夹：  

1. 在/etc/fstab中添加一项
　　gongxiang /mnt/shared vboxsf rw,gid=100,uid=1000,auto 0 0  
2. 在vitualbox设置中共享文件夹里取消自动挂载、取消自动挂载、取消自动挂载，重要的事说三遍可以解决，  





>参考文章列表  
>[linux 客户机挂载vitualbox共享文件夹](https://www.cnblogs.com/zzyyxxjc/p/7110147.html)  
>[在 Linux 客户机中装载共享文件夹](https://docs.vmware.com/cn/VMware-Workstation-Player-for-Linux/16.0/com.vmware.player.linux.using.doc/GUID-AB5C80FE-9B8A-4899-8186-3DB8201B1758.html)  
>[优化对 Linux 共享文件的读写访问](https://docs.vmware.com/cn/VMware-Workstation-Pro/16.0/com.vmware.ws.using.doc/GUID-53B75A8F-7BE7-4E85-85F6-41307428EF08.html)  
>[Ubuntu使用sshfs挂载远程目录](https://bbs.huaweicloud.com/blogs/160748)