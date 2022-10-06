---
title: Arch！
categories:
- Linux
tags:
---


# Arch Linux 安装和kde桌面配置教程
## Arch Linux 的安装

## 配置kde桌面

## 桌面环境美化(Sweet主题)

## 总结
### 安装过程中必要安装软件列表

## 问题

### Linux软件安装模板
其中[AUR – visual-studio-code-bin](https://aur.archlinux.org/packages/visual-studio-code-bin/)提供了安装脚本
```bash
mkdir -p ~/Software/AUR
cd ~/Software/AUR
git clone https://aur.archlinux.org/visual-studio-code-bin.git
cd visual-studio-code-bin
makepkg -si
```

Q:安装过程虽历经几番波折，但终究成功OK,其实也就输入命令麻烦了一点，没什么难度。在使用过程中出现了一些问题，程序菜单使用的是`Activate Application Launcher Widget`设置了快捷键`alt`+`F1`,无法使用，打不开。  
A:右击程序启动器图标，可以看到一个`配置程序启动器`的按钮，点击一下，在打开的窗口中选择键盘快捷键，配置一下即可，在键盘快捷键中可以设置为`alt`+`F1`,再使用网上提供的方案即可用`win`键打开程序启动器。但在更换全局主题后需按上述过程重新配置，配置过程会提示冲突，正常操作即可。

Q;重装了Xorg，KDE，plasma，之后开机是显示了登录界面，但进去后卡了一会儿就黑屏了。  
A:最后发现竟然只是Plasma包没有安装好而已。

Q:如何删除下载的主题。  
A:

Q:ERROR: Running makepkg as root is not allowed as it can cause permanent, catastrophic damage to your system.  
A:您可能在root用户下使用了该命令，可以在切换回普通用户后试试。  
>[在reddit上有相关讨论](https://www.reddit.com/r/archlinux/comments/2wjpww/error_running_makepkg_as_root_is_not_allowed_as/)，下文摘录了回答：  
>Yes, your first attempt to build the package as root has changed the permissions of the folder. Now, as a normal user, you cannot access the folder properly, because the permissions are bogus. Check and fix the permissions and the ownership of those folders, then use makepkg as a normal user.  
>Um, the problem is exactly as the errors say. You need to give yourself write permissions on that directory, and you should not run makepkg as root. 