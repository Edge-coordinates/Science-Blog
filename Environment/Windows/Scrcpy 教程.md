---
title: Scrcpy 教程
date: 2025/9/8 23:11:38
categories:
  - - Environment
    - Windows
abbrlink: 5dcdd3cb
---
# Scrcpy 教程

## 调用摄像机

scrcpy --video-source=camera --camera-id=0 --camera-size=4096x3072

查阅摄像头信息

scrcpy --video-source=camera --list-cameras

多设备

scrcpy -s 8943307a --video-source=camera --camera-id=0