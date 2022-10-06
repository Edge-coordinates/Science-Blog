---
title: 更新 linux gcc 版本到 gcc 4.4.2_奋斗中拥有 - CSDN 博客
categories:
- Net-excerpt
tags:
reprint: true
---


---
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/force_eagle/article/details/5203578)

**更新 linux gcc 版本到 gcc 4.4.2**

首先需要准备需要材料：gcc4.4.2 版需要安装 gmp4.2.0 + 和 mpfr2.3.0+，到 GMP 的网站（[http://gmplib.org/](http://gmplib.org/)）上下载 gmp-4.3.1.tar.gz 和 mprf 的网站（[http://www.mpfr.org/](http://www.mpfr.org/)）上下载 mpfr-2.4.2.tar.gz

1. **安装 gmp**  
# wget [ftp://ftp.gmplib.org/pub/gmp-5.0.0/gmp-5.0.0.tar.bz2](ftp://ftp.gmplib.org/pub/gmp-5.0.0/gmp-5.0.0.tar.bz2)  
# tar -zxvf gmp-4.3.2.tar.gz  
# cd gmp-4.3.2  
# ./configure  
# make  
# make check  
这一步用来查看有没有文件不匹配或缺失, 然后安装：  
# make install

2. **安装 mpfr**  
# wget [http://www.mpfr.org/mpfr-current/mpfr-2.4.2.tar.gz](http://www.mpfr.org/mpfr-current/mpfr-2.4.2.tar.gz)  
# tar -zxvf mpfr-2.4.2.tar.gz  
# cd mpfr-2.4.2  
配置：  
# ./configure --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib  
# make  
# make check  
接下来安装：  
# make install  
打包成 tar.gz, 需要 xz(LZMA) 支持; [http://tukaani.org/xz/](http://tukaani.org/xz/) 提供下载  
# make dist

准备工作完成，以下是 gcc 的安装与更新.

3. **编译安装 gcc**

从 GCC 官网（[http://gcc.gnu.org/](http://gcc.gnu.org/)）下载资源 gcc 源代码, 当前 gcc 版本为 gcc-4.4.2.

# wget [ftp://ftp.dti.ad.jp/pub/lang/gcc/releases/gcc-4.4.2/gcc-4.4.2.tar.gz](ftp://ftp.dti.ad.jp/pub/lang/gcc/releases/gcc-4.4.2/gcc-4.4.2.tar.gz)  
# tar xzvf gcc-4.4.2.tar.gz

建立目标目录, 目标目录是用来存放编译结果的地方  
# mkdir gcc-build  
# cd gcc-build

配置 gcc, 这里只选择了 c,c++.

# ../gcc-4.4.2/configure  --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-libgcj-multifile --enable-languages=c,c++,objc,obj-c++ --with-cpu=generic --disable-dssi --enable-plugin --prefix=/usr/local/gcc-4.4.2 --with-gmp=/usr/local --with-mpfr=/usr/local

编译  
# make

安装, 需要管理员的权限, 如为普通用户使用 su 命令切换到 root 用户.  
# make install

至此，GCC 就安装 完成了.

4. **环境设置**

将 gcc 的头文件和库文件指向新的版本  
cd $HOME  
ls -a  
sudo vi .bashrc

向其中添加以下语句。

GCCHOME=/usr/local/gcc-4.4.2  
PATH=$GCCHOME/bin:$PATH  
LD_LIBRARY_PATH=$GCCHOME/lib  
export GCCHOME PATH LD_LIBRARY_PATH

5. **测试  
**重新引导，查看 gcc 版本  
# source $HOME/.bashrc  
# # which  gcc  
/usr/local/gcc-4.4.2/bin/gcc  
会显示 gcc 新的路径为 /usr/local/gcc-4.4.2

# gcc -v  
Using built-in specs.  
Target: i686-pc-linux-gnu  
Configured with: ../gcc-4.4.2/configure --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-libgcj-multifile --enable-languages=c,c++,objc,obj-c++ --with-cpu=generic --disable-dssi --enable-plugin --prefix=/usr/local/gcc-4.4.2 --with-gmp=/usr/local --with-mpfr=/usr/local  
Thread model: posix  
gcc version 4.4.2 (GCC)

显示 gcc 的版本为 4.4.2