---
title: 挂载onedrive
categories:
- Linux
tags:
---


# 

## 前言
本文会先介绍前置的知识，之后会以挂载onedrive下的`ICSpic`文件夹到`/www/wwwroot/www.ics.ink/public/assets/files`文件夹下以实现[轮回社](https://www.ics.ink/)(基于Flarum论坛)的图片上传功能。

## 前置知识


df -h 查看挂载情况。

挂载命令：rclone mount DriveName:Folder LocalFolder

卸载命令：fusermount -qzu LocalFolder


/www/wwwroot/www.ics.ink/public/assets/files

rclone mount ICS:ICSFILE /www/wwwroot/www.ics.ink/public/assets/files --copy-links --allow-other --allow-non-empty --umask 000 --vfs-cache-mode writes or full

