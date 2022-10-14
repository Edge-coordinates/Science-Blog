---
title: simpread-Archlinux（2020.11.1）系统安装及 kde 桌面环境配置
date: 2022/10/14
categories:
  - Linux
abbrlink: daa51e6a
tags:
---




> 原文地址 [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/282860950)

一、Archlinux（2020.11.1）系统安装
--------------------------

（硬件安装环境为：联想 think x250 笔记本）

**1. 官网下载 ArchLinux 镜像**  
163 镜像站（2020.11.1）：

**2.UltraISO 刻录，制作 U 盘启动盘**

打开 UltraISO，选择下载好的 archlinux 镜像，启动，选择写入硬盘映像，写入格式选择 raw，这一点非常重要，不然无法引导启动!)  

**3. 打开电脑选择从 u 盘启动（启动前 bios 设置 efi 模式）**  
开机按 F12，选择 u 盘引导启动。

**4. 验证 efi 启动模式**

终端窗口输入以下命令：

```
ls /sys/firmware/efi/efivars

```

# 如果有输出则支持 UEFI，反之不支持 UEFI，只能用 MBR 模式。

**5. 联网**  
笔记本：在终端中输入 iwctl 进入 iwd 提示符：

```
[root@archiso~] iwctl
[iwd#]device list                                 #查询机器的网卡设备，如wlan0之类。
[iwd#]station <devicename> scan                   #查询附近可用的wifi网络：
[iwd#]station <devicename> get-networks           #显示扫描的结果
[iwd#]station <devicename> connect <wifi-ssid>    #连接wifi网络
如果wifi加密，会提示你输入密码。

```

如果是用网线：dhcpcd

```
测试网络：ping www.baidu.com

```

**6. 同步系统时钟**

```
timedatectl set-ntp true
timedatectl status

```

**7. 更新系统源**

使用 reflector 来获取速度最快的 6 个镜像，并将地址保存至 / etc/pacman.d/mirrorlist

```
reflector -c China -a 6 --sort rate --save  /etc/pacman.d/mirrorlist
pacman -Syy         #执行刷新

```

**8. 查看磁盘分区情况**

用 lsblk 命令查看分区状态

建议共分四个区：根目录 /, 用户主目录：/home,efi 分区：/boot, 交换分区：swap

**9：磁盘分区**

用 parted 命令转换磁盘类型

```
Parted  /dev/sda            #执行parted命令变更磁盘类型
mktable                     #执行mktable命令
gpt                         #将模式转为gpt
quit

```

分区工具：cfdisk

```
 cfdisk /dev/sdax 
UEFI模式：
创建gpt分区表
在cfdisk中选择new 要new出4个分区 分区大小自己设置 然后选择type 分区类型 然后选择writer输入yes，最后选择quit退出。
结果如下：
磁盘分区     大小    类型type
/dev/sda1   1024M     EFI system 
/dev/sda2    50GB      Linux filesystem  （根目录）
/dev/sda3    4G        linuxswap
/dev/sda4    400GB      Linux filesystem （/home目录） 
以上大小可根据实际情况来定。 

```

**10. 分区格式化**  
#UEFI 模式格式分区：

```
mkfs.vfat  /dev/sda1          #EFI系统分区格式化
mkfs.ext4 /dev/sda2,4         #linux文件系统格式化 ext4
mkswap  /dev/sda3             #交换分区格式化
swapon /dev/sda3              #激活交换分区

```

**11. 挂载 把刚格式化的文件挂载到 linux 下**  
swap 分区不用挂载

```
mount /dev/sda2 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
mkdir /mnt/home
mount /dev/sda4 /mnt/home
fdisk -l                  #查看分区信息

```

**12. 安装系统**

```
pacstrap /mnt base linux linux-firmware   base-devel  vim  dhcpcd

```

**13：生成硬盘文件有关的信息**

```
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab    #查看硬盘信息是否正确

```

**14：切换到已经配置好的系统 系统已经配置到 / mnt 下了 也就是你挂载到的磁盘分区**

```
arch-chroot /mnt

```

**15. 设置时区**：

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc  

```

**16. 设置语言**  
打开 / etc/locale.gen

```
vim /etc/locale.gen

```

#去掉以下三行的注释

```
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
zh_TW.UTF-8 UTF-8

```

#写入配置文件并使其生效

```
locale-gen

```

**17. 编辑 / etc/locale.conf**

```
echo "LANG=en_US.UTF-8" > /etc/locale.conf

```

**18：设置电脑主机名 #名字随便设置**

```
echo "主机名" > /etc/hostname

```

**19. 设置 hosts 文件**

```
vim/etc/hosts
#写入
127.0.0.1        localhost
::1              localhost
127.0.1.1        主机名.localdomain 主机名

```

**20. 设置 root 密码**

```
passwd

```

21.intel cpu 安装：

```
pacman -S intel-ucode

```

**22. 安装引导**

```
pacman -S grub efibootmgr
grub-install --target=x86_64-efi  --efi-directory=/boot/efi --bootloader-id=Archlinux 
grub-mkconfig -o /boot/grub/grub.cfg

```

**23. 安装网络工具**

```
pacman -S iwd  dialog  netctl
systemctl enable dhcpcd #台式机执行  

```

  
**24. 退出系统重启**

```
exit           # 退出系统
umount -R /mnt #取消挂载
reboot         #重启

```

二、kde 桌面环境配置
------------

**25. 安装 kde 环境部分**  
登入 root 用户 输入密码  
**26. 启动后设置 wifi 联网先**

```
systemctl start iwd.service # 启动服务
systemctl enable iwd.service # 开机自启动服务
systemctl enable systemd-resolved.service

```

**27. 创建用户**

```
useradd -m -g users -s /bin/bash 用户名
passwd 用户名
vim /etc/sudoers
#在root ALL=（ALL）ALL下面添加：
用户名 ALL=（ALL）ALL

```

保存退出：wq！强制保存退出  
**28. 切换用户**  
exit# 退出 root 用户  
使用普通用户登录 (如我创建的 nicemoe 用户登录)  

**29. 安装驱动**

```
sudo pacman -S alsa-utils pulseaudio-alsa #声卡驱动
查看显卡型号
lspci | grep VGA
#安装显卡驱动
sudo pacman -S xf86-video-intel mesa #intel核心显卡驱动
#nvidia独显驱动：
sudo pacman -S nvidia nvidia-utils  #nvidia独显驱动
#或者安装nvidia开源驱动：
sudo pacman -S xf86-video-nouveau mesa  #nvidia开源驱动

```

**30. 安装 x 窗口系统**

```
sudo pacman -S xorg

```

**31. 安装触摸板驱动（笔记本）**

```
sudo pacman -S xf86-input-synaptics #libinput

```

**31. 安装中文字体**

```
sudo pacman -S ttf-dejavu wqy-microhei wqy-zenhei

```

**32. 安装 kde 桌面**

```
sudo pacman -S plasma

```

**33. 安装 kde 应用**

```
sudo pacman -S kde-applications#kde所有应用
#或者：sudo pacman -S kdebase##kde基础包

```

**33. 识别 windows 分区**

```
pacman -S  ntfs-3g

```

**34. 安装 sddm 图像登录界面**

```
sudo pacman -S sddm sddm-kcm

```

**35. 安装网络工具**

```
sudo pacman -S networkmanager netctl 

```

**36. 启动服务**  

```
su #且换root用户
systemctl enable NetworkManager
systemctl enable sddm
systemctl enable dhcpcd
sddm --example-config > /etc/sddm.conf
reboot
设置中文
在设置界面里
Control Center -> Keyboard and Language -> Enable Numeric Keyboard
#添加中文，并将中文移到第一个
reboot重启


```

**37. 创建默认目录 (普通用户下)**

```
sudo pacman -S xdg-user-dirs
xdg-user-dirs-update --force  #或者 xdg-user-dirs-update
# 使用 LC_ALL=C xdg-user-dirs-update --force 命令可以强制创建英语目录。

```

**38. 安装蓝牙驱动并设置开机自启服务**

```
sudo pacman -S bluez bluez-utils
systemctl start bluetooth
#安装蓝牙音频
sudo pacman -S pulseaudio-bluetooth
sudo vim /etc/pulse/system.pa
#写入
load-module module-bluetooth-policy
load-module module-bluetooth-discover
reboot#重启

```

结束。