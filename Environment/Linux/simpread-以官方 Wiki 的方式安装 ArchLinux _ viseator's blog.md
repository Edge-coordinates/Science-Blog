---
title: simpread-以官方 Wiki 的方式安装 ArchLinux _ viseator's blog
date: 2022/10/14
categories:
  - Linux
abbrlink: dbc3380d
tags:
---


> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.viseator.com](https://www.viseator.com/2017/05/17/arch_install/)

> 写在前面 这可能是你能找到的最适合你的中文 ArchLinux 安装教程。

[](#写在前面 "写在前面")写在前面
--------------------

> **这可能是你能找到的最适合你的中文`ArchLinux`安装教程。**

前几天硬盘挂了，万幸的是家目录放在了另一块硬盘上所以存活了下来。不得不再重装一遍`Arch`，算上帮朋友装的，这已经是我第四次安装`Arch`了。也想借此机会记录这个过程写一篇完全按照官方 Wiki 指导再加上 Wiki 上没有重点写出来但是安装过程中会遇到的一些问题的一篇不太一样的安装教程。

很多人提起起`Arch`的第一反应就是安装困难，这种困难有很多原因，也就是接下来我们将会面对的问题。

*   没有图形界面的引导：`Arch`只给我们提供了一个最小的环境，所有的安装操作都需要在命令行中完成，这对于不习惯命令行操作的人来说是最难以跨越的一个坎。许多发行版之所以可以流行开来就是因为他们提供了友好的、流程化的安装过程，这帮很多人解决了学习`Linux`的第一步：安装一个`Linux`。
*   预备知识的不足与缺乏查找并解决问题的能力：一些对于安装系统比较重要的知识例如系统引导、配置文件的编辑、简单的命令行操作等没有接触过，所以操作时往往摸不着头脑，一旦自己的操作结果与教程不符便不知道如何去解决遇到的问题。
*   缺乏合适的教程：安装 Arch 最好的也是最完备的教程就是官方的 [Installation guide](https://wiki.archlinux.org/index.php/installation_guide) 与 [Wiki](https://wiki.archlinux.org/)，虽然部分内容有中文版，但是中文的翻译有些时候会落后于英文版，不推荐完全依赖于中文 Wiki。并且官方 Wiki 的写作方式更偏向于文档，没有我们所习惯的按步骤编排的安装过程，给不熟悉这种写作方式的同学造成了阅读与使用上的困难。国内的可以找到的教程往往都是时间比较久远，或是没有提及或是忽略了一些新手容易犯错误的地方。

> **本篇教程致力于与现有的 Wiki 保持一致，并且适当地加入一些适合初学者学习的链接，希望可以让阅读了这篇教程的同学可以提高自己利用现有及以后可能出现的新的 Wiki 内容的能力。**

`ArchLinux`或者是`Linux`的优点就不在这里多说了，我相信打开这篇教程的同学一定可以从这样的过程中得到很多。

### [](#注意事项 "注意事项")注意事项

请一定**仔细阅读教程中的每一个指示**，绝大部分安装失败都是由于没有仔细看教程，遗漏、错输指令导致的。安装的方式根据引导方式的不同会有所不同，所以请按教程中的指示进行，切忌一味地输命令而不管说明。

对于**硬盘分区相关**的操作，请更加小心检查命令，数据无价。

下面就正式开始我们的教程。

[](#安装教程 "安装教程")安装教程
--------------------

### [](#前期准备 "前期准备")前期准备

#### [](#安装介质 "安装介质")安装介质

在安装之前我们先要准备一个安装介质，在这里只推荐 U 盘作为安装介质。

1.  到 [https://www.archlinux.org/download/](https://www.archlinux.org/download/) 页面下方的中国镜像源中下载`archlinux-**-x86_64.iso`这个`iso`文件。
    
2.  *   如果是`Linux`系统下制作安装介质，推荐使用`dd`命令，教程：
        
        > [http://www.runoob.com/linux/linux-comm-dd.html](http://www.runoob.com/linux/linux-comm-dd.html)
        
    *   如果是`windows`系统下制作安装介质，推荐使用`usbwriter`这款轻量级的工具，下载链接：
        
        > [https://sourceforge.net/projects/usbwriter/](https://sourceforge.net/projects/usbwriter/)
        

#### [](#磁盘准备 "磁盘准备")磁盘准备

我们需要有一块空闲的磁盘区域来进行安装，这里的空闲指的是**没有被分区**的空间。下面来介绍如何准备这块空间。

*   在`windows`下空出一块分区来安装：利用`windows`自带的磁盘管理工具就可以：
    
    1.  右击`windows`图标，在弹出菜单中选择磁盘管理（其他版本的`windows`请自行找到打开磁盘管理的方式）：
        
        ![](https://www.viseator.com/images/arch01.jpeg)
        
    2.  右击想要删除的分区，选择删除卷（注意这步之后这个分区的所有数据将会丢失）：
        
        ![](https://www.viseator.com/images/arch02.jpeg)
        
*   在`linux`下分出一块区域安装：使用`fdisk`进行，教程请见链接中的删除分区：
    
    > [http://www.liusuping.com/ubuntu-linux/linux-fdisk-disk.html](http://www.liusuping.com/ubuntu-linux/linux-fdisk-disk.html)
    
*   空闲的磁盘（新磁盘）：不需要进行任何操作。
    

### [](#U盘安装 "U盘安装")U 盘安装

下面的过程实际上都在刚刚准备好的 U 盘启动介质上的`Linux`系统下进行，所以**启动时都应该选择 U 盘**。

#### [](#设置启动顺序 "设置启动顺序")设置启动顺序

这一步在不同品牌的电脑上都不一样，所以需要大家自行搜索**自己电脑品牌 + 启动顺序**这个关键词来进行设置。

例如我的电脑搜索神舟 启动顺序可以得到如下的结果：

> [https://zhidao.baidu.com/question/170954184.html](https://zhidao.baidu.com/question/170954184.html)

一般来说现在的主板都可以不用进入 BIOS 而快速地切换启动顺序，只要找到相应的快捷键就可以了。

#### [](#进入U盘下的Linux系统 "进入U盘下的Linux系统")进入 U 盘下的 Linux 系统

1.  按上一步设置好启动顺序，启动之后会看到如下界面（UEFI 启动方式的界面可能不同）：
    
    ![](https://www.viseator.com/images/arch03.jpeg)
    
    如果直接进入`windows`，请检查启动顺序是否设置成功，U 盘是否在制作启动介质时成功写入。
    
    如果没有看到这个界面，请检查 U 盘是否制作成功，如果多次遇到问题可以考虑换一个 U 盘。
    
    选择第一个选项。
    
2.  这时`Arch`开始加载，你将会看到屏幕显示如下内容：
    
    ![](https://www.viseator.com/images/arch04.jpeg)
    
    加载完成后你将会进入一个有命令提示符的界面：
    
    ![](https://www.viseator.com/images/arch05.jpeg)
    
    如果出现`FAIL`或是其他错误信息导致无法启动请自行搜索错误信息来获得解决方法。
    
    这就是`Linux`的终端界面了，接下来我们将通过在这个界面执行一系列命令来将`Arch`安装到我们的磁盘上。
    

下面进行的过程是按照官方 [Installation guide](https://wiki.archlinux.org/index.php/installation_guide) 为依据进行的，出现的任何问题都可以到链接中的相应部分查找原文找到解决方式。

#### [](#检查引导方式 "检查引导方式")检查引导方式

目前的引导方式主要分为 EFI 引导 + GPT 分区表与 BIOS(LEGACY) 引导 + MBR 分区表两种，几乎比较新的机器都采用了 EFI/GPT 引导的方式。关于这部分的内容如果有兴趣可以通过这个链接进行了解：

> [http://www.chinaz.com/server/2016/1017/595444.shtml](http://www.chinaz.com/server/2016/1017/595444.shtml)

如果你不知道自己的引导方式，请在命令提示符下执行以下命令：

```
ls /sys/firmware/efi/efivars
```

这里的`ls`是命令，空格后面的一串为路径，作为`ls`命令的参数。`ls`命令的作用是显示路径目录下的所有的文件（夹）。

如果你对命令行下的常用操作（TAB 补全、取消命令等）不熟悉，请先学习了解下面部分实用的快捷键或命令：

> **Tab 键 命令行自动补全。键入命令或文件名的前几个字符，然后按 [Tab] 键，它会自动补全命令或显示匹配你键入字符的所有命令**
> 
> ↑(Ctrl+p) 显示上一条命令
> 
> ↓(Ctrl+n) 显示下一条命令
> 
> Ctrl-C: 终止当前正在执行的命令

输入命令并回车执行后，如果提示

```
ls: cannot access '/sys/firmware/efi/efivars': No such file or directory
```

表明你是以`BIOS`方式引导，否则为以`EFI`方式引导。现在只需要记住这个信息，之后这两种引导类型的安装方式会略有不同（下文中涉及到不同的地方请仔细区别）。

**更新：**  
  
部分同学反馈这种方式并不能100% 确认你就是`BIOS`方式引导的，更加保险的方法是执行`fdisk -l`查看分区表，如果**你的硬盘（而不是你的 U 盘）**的`Disklabel type`属性为`gpt`并且有一个`Type`为`EFI System`的小分区（一般为 256M 左右，如下图），那么你应该是`EFI`引导的。  
  
![](https://www.viseator.com/images/arch26.png)

#### [](#联网 "联网")联网

`arch`并不能离线安装，因为我们需要联网来下载需要的组件，所以我们首先要连接网络。

*   如果你是有线网并且路由器支持 DHCP 的话插上网线后先执行以下命令获取 IP 地址：
    
    ```
    dhcpcd
    ```
    
*   然后执行以下命令来判断网络连接是否正常：
    
    ```
    ping www.baidu.com
    ```
    
    如果可以看到类似下面的内容就说明连上了网络：
    
    ![](https://www.viseator.com/images/arch05.jpg)
    
    > 再次提示用快捷键 Ctrl-C 可以终止当前正在执行的命令
    
*   如果你是无线网，请执行以下命令：
    
    ```
    iwctl
    ```
    
    会进入一个以 [iwd] 开头的命令行环境中，接着执行：
    
    ```
    device list
    ```
    
    会列出当前可用的所有网卡设备，如图所示：
    
    ![](https://www.viseator.com/images/arch27.png)
    
    记住`Name`一列你所使用的无线网卡的名称，比如我的就叫`wlan0`，下面的命令要用到，**下面命令中请替换成自己的网卡名称**
    
    接着执行下列命令进行无线网络的扫描：（**`wlan0`替换成你自己的网卡名称 **）
    
    ```
    station wlan0 scan
    ```
    
    接着执行下列命令列出扫描到的网络：（**`wlan0`替换成你自己的网卡名称 **）
    
    ```
    station wlan0 get-networks
    ```
    
    可以看到当前扫描到的无线网络都展示出来了：
    
    ![](https://www.viseator.com/images/arch28.png)
    
    最后输入下列命令连接指定网络：（**`wlan0`替换成你自己的网卡名称，`CatAndPomelo`替换成你想连的网络名称 **）：
    
    ```
    station wlan0 connect CatAndPomelo
    ```
    
    这时如果网络有密码的话会提示输入密码，输入后回车确认就行：
    
    ![](https://www.viseator.com/images/arch29.png)
    
    注意这里就算密码输入错误也不会有提示的，所以请保证密码正确，如果你是中文无线网名称 / 密码的话建议先改一下，把密码取消会更方便些。
    
    顺利的话，此时你已经连接上网络了，执行下面命令退出`iwd`：
    
    ```
    quit
    ```
    
    连接以后同样可以通过上面的`ping`命令来进行测试。
    
    `iwd`是一个实用的命令行下联网工具，利用它可以方便地联网，如果它没能起作用，需要进入以下页面查找解决方式：
    
    > [https://wiki.archlinux.org/index.php/Wireless_network_configuration](https://wiki.archlinux.org/index.php/Wireless_network_configuration)
    

**注意**：由于部分无线网卡驱动的支持并不完善，所以在这里可能会遇到问题，并且各机型的解决方法都不同，如果不幸遇到无线连不上的问题，可以插有线联网先把系统装好再去慢慢解决。解决问题可以参照：[https://wiki.archlinux.org/index.php/Network_configuration](https://wiki.archlinux.org/index.php/Network_configuration)

#### [](#更新系统时间 "更新系统时间")更新系统时间

执行如下命令：

```
timedatectl set-ntp true
```

> 正常情况下这样的命令并没有输出，所谓没有消息就是最好的消息

#### [](#分区与格式化 "分区与格式化")分区与格式化

**特别注意：涉及到分区与格式化的操作要格外注意，命令在回车之前请再三确认知道自己在做什么，并且没有输错命令，否则将会来带来数据的丢失！如果有需要在操作之前请备份重要的数据。**

但是我们也并不要过于惧怕分区与格式化过程，正确操作的情况下不会对你其他数据产生任何影响。

##### [](#查看目前的分区情况 "查看目前的分区情况")查看目前的分区情况

执行命令：

```
fdisk -l
```

以我的电脑为例：

![](https://www.viseator.com/images/arch06.jpg)

可以看到我的一块 238.5g 的硬盘 (`/dev/sda`就代表这块硬盘)，下面列出了`/dev/sda*`这三个分区，`/dev/sda3`是我存活下来的家目录，可以看到它的类型为`Linux`分区。注意看`Start`与`End`的数值，这个数值代表扇区号，可以理解成硬盘被划分成了一个个小单元，可以直观地看出来在`/dev/sda2`的`End`与`/dev/sda3`的`Start`之间空出了一大块未分配的空间，接下来我们将分配这块区域。

*   如果你是 BIOS/MBR 方式引导，**跳过下面创建一个引导分区**的步骤。
*   如果你是 EFI/GPT 方式引导，并且同时安装了其他系统，那么你应该可以在分区列表中发现一个较小的并且类型为 EFI 的分区（**注意查看硬盘的大小，这个`EFI`分区有可能是你 U 盘中的，需要排除**），这是你的引导分区，请记下它的路径（/dev/sdxY) 备用，**跳过下面创建一个引导分区**的步骤。
*   如果你是 EFI/GPT 方式引导，但是没有这个较小的并且类型为 EFI 的引导分区（这种情况一般只会出现在新的硬盘），那么你需要**先创建一个引导分区**。

##### [](#创建一个引导分区（仅上面所列的第三种情况需要进行这步） "创建一个引导分区（仅上面所列的第三种情况需要进行这步）")创建一个引导分区（**仅上面所列的第三种情况需要进行这步**）

执行命令：

```
fdisk /dev/sdx （请将sdx替换成你要操作的磁盘如sdb sdc等）
```

下面你就进入了`fdisk`的操作环境， 输入`m`并回车可以查看各命令的作用。

1.  **如果你是一块全新的硬盘**：输入`g`来创建一个全新的 gpt 分区表，**否则直接进行第 2 步**。
    
2.  输入`n`创建一个新的分区，首先会让你选择起始扇区，一般直接回车使用默认数值即可，然后可以输入结束扇区或是分区大小，这里我们输入`+512M`来创建一个 512M 的引导分区。
    
3.  这时我们可以输入`p`来查看新创建的分区。
    
4.  输入`t`并选择新创建的分区序号来更改分区的类型，输入`l`可以查看所有支持的类型，输入`ef`更改分区的类型为`EFI`。
    
5.  输入`w`来将之前所有的操作写入磁盘生效，在这之前可以输入`p`来确认自己的分区表没有错误。
    
6.  输入以下命令来格式化刚刚创建的引导分区：
    
    ```
    mkfs.fat -F32 /dev/sdxY （请将sdxY替换为刚创建的分区）
    ```
    
    现在引导分区就创建好了。
    

##### [](#创建根分区 "创建根分区")创建根分区

输入命令：

```
fdisk /dev/sdx （请将sdx替换成你要操作的磁盘如sdb sdc等）
```

1.  **如果你是一块全新的硬盘**（**否则直接进行第 2 步**）：
    
    1.  **如果你是`BIOS/MBR`引导方式**：输入`o`来创建一个全新的`MBR`分区表。
    2.  **如果你在上一步新建了分区表并创建了引导分区**：直接进行步骤 2。
    3.  **如果你在另一块硬盘中已经有引导分区**：输入`g`来创建一个全新的`gpt`分区表。
2.  输入`n`创建一个新的分区，首先会让你选择起始扇区，一般直接回车使用默认数值即可，然后可以输入结束扇区或是分区大小，如果我们想要使创建的分区完全占满空闲的空间，可以直接回车使用默认结束扇区。
    
3.  这时我们可以输入`p`来查看新创建的分区。
    
4.  输入`w`来将之前所有的操作写入磁盘生效，在这之前可以输入`p`来确认自己的分区表没有错误。
    
5.  输入以下命令来格式化刚刚创建的根分区：
    
    ```
    mkfs.ext4 /dev/sdxY （请将的sdxY替换为刚创建的分区）
    ```
    
    这是我的分区过程供参考：
    

![](https://www.viseator.com/images/arch07.jpg)

![](https://www.viseator.com/images/arch08.jpg)

**如果你在分区这步遇到了问题**，先看看自己的操作是否与上面的指引一致，如果仍然无法解决可参考 [https://www.cnblogs.com/freerqy/p/8502838.html](https://www.cnblogs.com/freerqy/p/8502838.html) 这篇文章的 “建立硬盘分区” 一节尝试使用`cfdisk`进行分区。

#### [](#挂载分区 "挂载分区")挂载分区

执行以下命令将根分区挂载到`/mnt`：

```
mount /dev/sdxY /mnt （请将sdxY替换为之前创建的根分区）
```

**如果你是 EFI/GPT 引导方式**，执行以下命令创建 / boot 文件夹并将引导分区挂载到上面。**BIOS/MBR 引导方式无需进行这步。**

```
mkdir /mnt/boot
mount /dev/sdxY /mnt/boot （请将sdxY替换为之前创建或是已经存在的引导分区）
```

#### [](#选择镜像源 "选择镜像源")选择镜像源

因为从这步开始，需要进行一些编辑配置文件的操作，所以需要掌握一些命令行下非常著名的一款编辑器`Vim`的基本操作，在这里推荐学习下面这个链接中的存活部分，可以完成编辑、复制粘贴与保存工作即可。

> [http://coolshell.cn/articles/5426.html](http://coolshell.cn/articles/5426.html)

镜像源是我们下载的软件包的来源，我们需要根据自己的地区选择不同的源来加快下载的速度。

执行以下命令，用`Vim`来编辑`/etc/pacman.d/mirrorlist`这个文件

```
vim /etc/pacman.d/mirrorlist
```

> 提示：输入路径时可以用`Tab`键补全

![](https://www.viseator.com/images/arch09.jpg)

找到标有`China`的镜像源，`normal`模式下按下`dd`可以剪切光标下的行，按`gg`回到文件首，按`P`（注意是大写的）将行粘贴到文件最前面的位置（优先级最高）。

当然也可以直接手工输入。

这里推荐使用清华、浙大源：

```
Server = http://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = http://mirrors.zju.edu.cn/archlinux/$repo/os/$arch
```

最后记得用`:wq`命令保存文件并退出。

#### [](#安装基本包 "安装基本包")安装基本包

下面就要安装最基本的`ArchLinux`包到磁盘上了。这是一个联网下载并安装的过程。

执行以下命令：

```
pacstrap /mnt base base-devel linux linux-firmware dhcpcd
```

根据下载速度的不同在这里需要等待一段时间，当命令提示符重新出现的时候就可以进行下一步操作了。

#### [](#配置Fstab "配置Fstab")配置 Fstab

生成自动挂载分区的`fstab`文件，执行以下命令：

```
genfstab -L /mnt >> /mnt/etc/fstab
```

由于这步比较重要，所以我们需要输出生成的文件来检查是否正确，执行以下命令：

```
cat /mnt/etc/fstab
```

![](https://www.viseator.com/images/arch10.jpg)

如图，可以看到`/dev/sda4`被挂载到了根分区。

`/dev/sda3`是我之前存活下来的家目录被挂载到了`/home`目录（你们没有这条）。

**如果是`EFI/GPT`引导的还应该有引导分区被挂载到`/boot`目录**。

#### [](#Chroot "Chroot")Chroot

`Chroot`意为`Change root`，相当于把操纵权交给我们新安装（或已经存在）的`Linux`系统，**执行了这步以后，我们的操作都相当于在磁盘上新装的系统中进行**。

执行如下命令：

```
arch-chroot /mnt
```

这里顺便说一下，如果以后我们的系统出现了问题，只要插入 U 盘并启动， 将我们的系统根分区挂载到了`/mnt`下（如果有`efi`分区也要挂载到`/mnt/boot`下），再通过这条命令就可以进入我们的系统进行修复操作。

#### [](#设置时区 "设置时区")设置时区

依次执行如下命令设置我们的时区为上海并生成相关文件：

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

![](https://www.viseator.com/images/arch11.jpg)

#### [](#提前安装必须软件包 "提前安装必须软件包")提前安装必须软件包

因为我们现在已经`Chroot`到了新的系统中，只有一些最基本的包（组件），这时候我们就需要自己安装新的包了，下面就要介绍一下`ArchLinux`下非常强大的包管理工具`pacman`，大部分情况下，一行命令就可以搞定包与依赖的问题。

安装包的命令格式为`pacman -S 包名`，`pacman`会自动检查这个包所需要的其他包（即为依赖）并一起装上。下面我们就通过`pacman`来安装一些包，这些包在之后会用上，在这里先提前装好。

执行如下命令（注意大小写，大小写错误会导致包无法找到）：

```
pacman -S vim dialog wpa_supplicant ntfs-3g networkmanager netctl
```

一路确认之后包就被成功装上了。

![](https://www.viseator.com/images/arch12.jpg)

图中只安装了`Vim`和它的依赖。

#### [](#设置Locale "设置Locale")设置 Locale

设置我们使用的语言选项，执行如下命令来编辑`/etc/locale.gen`文件：

```
vim /etc/locale.gen
```

在文件中找到`zh_CN.UTF-8 UTF-8` `zh_HK.UTF-8 UTF-8` `zh_TW.UTF-8 UTF-8` `en_US.UTF-8 UTF-8`这四行，去掉行首的 #号，保存并退出。如图：

![](https://www.viseator.com/images/arch13.jpg)

![](https://www.viseator.com/images/arch14.jpg)

然后执行：

```
locale-gen
```

![](https://www.viseator.com/images/arch15.jpg)

打开（不存在时会创建）`/etc/locale.conf`文件：

```
vim /etc/locale.conf
```

在文件的第一行加入以下内容：

```
LANG=en_US.UTF-8
```

保存并退出。

#### [](#设置主机名 "设置主机名")设置主机名

打开（不存在时会创建）`/etc/hostname`文件：

```
vim /etc/hostname
```

在文件的第一行输入你自己设定的一个`myhostname`

保存并退出。

编辑`/etc/hosts`文件：

```
vim /etc/hosts
```

在文件末添加如下内容（将`myhostname`替换成你自己设定的主机名）

```
127.0.0.1	localhost
::1		localhost
127.0.1.1	myhostname.localdomain	myhostname
```

![](https://www.viseator.com/images/arch16.png)

这里我设置的是`viseator`。

保存并退出。

#### [](#设置Root密码 "设置Root密码")设置 Root 密码

`Root`是`Linux`中具有最高权限帐户，有些敏感的操作必须通过`Root`用户进行，比如使用`pacman`，我们之前进行所有的操作也都是以`Root`用户进行的，也正是因为`Root`的权限过高，如果使用不当会造成安全问题，所以我们之后会新建一个普通用户来进行日常的操作。在这里我们需要为`Root`帐户设置一个密码：

执行如下命令：

```
passwd
```

按提示设置并确认就可以了。

![](https://www.viseator.com/images/arch17.jpg)

或许有的人已经发现官方 Wiki 和一些其他教程资料中的命令是以`#`或`$`开头的，这两个符号就对应着命令行中的命令提示符，`#`代表以`Root`用户执行命令，`$`代表以普通用户执行命令，平时使用教程中的命令时应该注意这一点。

#### [](#安装Intel-ucode（非IntelCPU可以跳过此步骤） "安装Intel-ucode（非IntelCPU可以跳过此步骤）")安装`Intel-ucode`（非`Intel`CPU 可以跳过此步骤）

直接`pacman`安装：

```
pacman -S intel-ucode
```

#### [](#安装Bootloader "安装Bootloader")安装`Bootloader`

经常听说很多人因为引导问题导致系统安装失败，多数是因为教程没有统一或是过时的教程引起的，这里只要按照步骤来其实是不难的。

这里我们安装最流行的`Grub2`。**（如果曾经装过`Linux`，记得删掉原来的`Grub`，否则不可能成功启动）**

*   首先安装`os-prober`和`ntfs-3g`这两个包，它可以配合`Grub`检测已经存在的系统，自动设置启动选项。
    
    ```
    pacman -S os-prober ntfs-3g
    ```
    

##### [](#如果为BIOS-MBR引导方式： "如果为BIOS/MBR引导方式：")**如果为 BIOS/MBR 引导方式：**

*   安装`grub`包：
    
    ```
    pacman -S grub
    ```
    
*   部署`grub`：
    
    ```
    grub-install --target=i386-pc /dev/sdx （将sdx换成你安装的硬盘）
    ```
    
    注意这里的`sdx`应该为硬盘（例如`/dev/sda`），**而不是**形如`/dev/sda1`这样的分区。
    
*   生成配置文件：
    
    ```
    grub-mkconfig -o /boot/grub/grub.cfg
    ```
    
    ![](https://www.viseator.com/images/arch18.jpg)
    

**如果你没有看到如图所示的提示信息，请仔细检查是否正确完成上面的过程。常见问题如下：**

1.  如果报`warning failed to connect to lvmetad，falling back to device scanning.`错误。参照 [wiki](https://wiki.archlinux.org/index.php/Install_from_existing_Linux) 中搜索关键词`use_lvmetad`所在位置，简单的方法是编辑`/etc/lvm/lvm.conf`这个文件，找到`use_lvmetad = 1`将`1`修改为`0`，保存，重新配置 grub。
    
2.  有部分同学反馈后面安装`grub`包的时候报如下错误：
    
    ![](https://www.viseator.com/images/arch25.png)
    
    是因为实际是`UEFI`引导的系统没有正确挂载`boot`分区。首先检查你是不是按照`BIOS`方式安装的系统，二是检查是否正确挂载`/mnt/boot`。正确配置好`boot`分区之后可以从 “挂载分区” 这步开始重做。
    

##### [](#如果为EFI-GPT引导方式： "如果为EFI/GPT引导方式：")**如果为 EFI/GPT 引导方式：**

*   安装`grub`与`efibootmgr`两个包：
    
    ```
    pacman -S grub efibootmgr
    ```
    
*   部署`grub`：
    
    ```
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
    ```
    
*   生成配置文件：
    
    ```
    grub-mkconfig -o /boot/grub/grub.cfg
    ```
    
*   * 提示信息应与上面的图类似，如果你发现错误，请仔细检查是否正确完成上面的过程。**
    

如果报`warning failed to connect to lvmetad，falling back to device scanning.`错误。参照[这篇文章](https://www.pckr.co.uk/arch-grub-mkconfig-lvmetad-failures-inside-chroot-install/)，简单的方法是编辑`/etc/lvm/lvm.conf`这个文件，找到`use_lvmetad = 1`将`1`修改为`0`，保存，重新配置 grub。

如果报`grub-probe: error: cannot find a GRUB drive for /dev/sdb1, check your device.map`类似错误，并且`sdb1`这个地方是你的 u 盘，这是 u 盘`uefi`分区造成的错误，对我们的正常安装没有影响，可以不用理会这条错误。

##### [](#安装后检查 "安装后检查")安装后检查

**如果你是多系统，请注意上面一节中对`os-prober`这个包的安装。**

**强烈建议使用如下命令检查是否成功生成各系统的入口，如果没有正常生成会出现开机没有系统入口的情况：**

```
vim /boot/grub/grub.cfg
```

检查接近末尾的`menuentry`部分是否有`windows`或其他系统名入口。下图例子中是`Arch Linux`入口与检测到的`windows10`入口（安装在`/dev/sda1`），具体情况可能有不同：

![](https://www.viseator.com/images/arch22.jpg)

**如果你没有看到`Arch Linux`系统入口或者该文件不存在**，请先检查`/boot`目录是否正确部署`linux`内核：

```
cd /boot
ls
```

查看是否有`initramfs-linux-fallback.img initramfs-linux.img intel-ucode.img vmlinuz-linux`这几个文件，如果都没有，说明`linux`内核没有被正确部署，很有可能是`/boot`目录没有被正确挂载导致的，确认`/boot`目录无误后，可以重新部署`linux`内核：

```
pacman -S linux
```

再重新生成配置文件，就可以找到系统入口。

**如果你已经安装`os-prober`包并生成配置文件后还是没有生成其他系统的入口**：

**你目前处的 U 盘安装环境下有可能无法检测到其他系统的入口，请在下一步中重启登陆之后重新运行**：

```
grub-mkconfig -o /boot/grub/grub.cfg
```

如果还没有生成其他系统的入口，请参照：

> [https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Combining_the_use_of_UUIDs_and_basic_scripting](https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Combining_the_use_of_UUIDs_and_basic_scripting)

编辑配置文件手动添加引导的分区入口。

##### [](#重启 "重启")重启

接下来，你需要进行重启来启动已经安装好的系统，执行如下命令：

```
exit
```

** 如果挂载了`/mnt/boot`，先`umount /mnt/boot`，再`umount /mnt`，否则直接`umount /mnt`：**

```
umount /mnt/boot
umount /mnt
reboot
```

注意这个时候你可能会卡在有两行提示的地方无法正常关机，长按电源键强制关机即可，没有影响。

关机后拔出 U 盘，启动顺序会自动以硬盘启动，如果一切顺利，那么你将会看到下面的界面：

![](https://www.viseator.com/images/arch19.jpg)

启动时有可能会有输出信息显示在这里，直接回车就可以了。

输入`root`，再输入之前设置的密码，显示出命令提示符，恭喜你，你已经成功安装`ArchLinux`！

[](#安装后配置 "安装后配置")安装后配置
-----------------------

虽然系统安装好了，但是还没有进行基本配置和安装图形界面，所以接下来我们要进行一些必须的配置和图形界面的安装。

请见下一篇文章：[ArchLinux 安装后的必须配置与图形界面安装教程](http://www.viseator.com/2017/05/19/arch_setup/)

[](#特别感谢 "特别感谢")特别感谢
--------------------

评论区中`Senrey_Song`、`YKun`、`imzhwk`、`haonan mao`、`Lichen Zhang`、`回风`、`Nee`、`Wafer`、`LIU SHIKE`、`Charles`、`MegatonZed`、`beer!code!`、`禾七`、`Unira`、`arc`、`ZhiChao Li`、`多听音乐多喝水`、`AirLongdian`、`若尘`对于本教程内容的宝贵建议与指正。

`leccesg`、`Sophie Spivey`、`竹林里有冰`、`王心语`通过邮件提供的宝贵建议。

[](#最后 "最后")最后
--------------

如果觉得这篇教程对你有帮助，可以移步我的知乎回答下点个赞，让更多的人可以看到这篇教程，你的支持是我最大的动力：

> Arch Linux 怎么安装？ - viseator 的回答 - 知乎  
> [https://www.zhihu.com/question/21427410/answer/171867330](https://www.zhihu.com/question/21427410/answer/171867330)

**同时，如果你是想要从事计算机方向的新人，非常推荐看看我的分享：**：

[从开始到微信 / 支付宝 / Airbnb / 抖音 Offer——我的大学客户端开发学习之路（一）开始——步入大学生活](https://www.viseator.com/2020/05/24/university_1/)

[从开始到微信 / 支付宝 / Airbnb / 抖音 Offer——我的大学客户端开发学习之路（二）过程——技术学习与个人成长](https://www.viseator.com/2020/07/25/university_2/)

也欢迎关注我的微信公众号 VirMe：  
![](https://www.viseator.com/images/wechat_channel.jpg)

如果安装过程中遇到问题，可以直接在下方评论区 / 公众号留言或邮件 [viseator@gmail.com](mailto:viseator@gmail.com)（尽量附上错误信息），我会尽力回复解决。