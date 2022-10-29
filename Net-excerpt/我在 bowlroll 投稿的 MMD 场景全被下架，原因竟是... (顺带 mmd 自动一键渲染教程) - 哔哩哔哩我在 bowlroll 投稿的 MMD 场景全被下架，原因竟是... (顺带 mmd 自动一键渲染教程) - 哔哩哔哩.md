---
title: 我在 bowlroll 投稿的 MMD 场景全被下架，原因竟是... (顺带 mmd 自动一键渲染教程) - 哔哩哔哩我在 bowlroll 投稿的 MMD
  场景全被下架，原因竟是... (顺带 mmd 自动一键渲染教程) - 哔哩哔哩
date: 2022/10/14
categories:
  - Net-excerpt
reprint: true
abbrlink: 3494a12e
tags:
---


---
> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.bilibili.com](https://www.bilibili.com/read/cv11852457)

> 明天是我要配布新模型的日子，却在码这段字的今天发生了大无语事件，专门开一个专栏来记录这件事好了，顺便做一个 MMD 自动渲染教学，教学完全保姆式，尽量写的好玩些，大概会很尬 233（明明是个低技术力的玩意 x）......

明天是我要配布新模型的日子，却在码这段字的今天发生了大无语事件，

专门开一个专栏来记录这件事好了，顺便做一个 MMD 自动渲染教学，

教学完全保姆式，尽量写的好玩些，大概会很尬 233

（明明是个低技术力的玩意 x）

我是一个 mmder，会在 bowlroll 投稿一些 3D 的模型与场景，

但对新手来说会发生一件哭笑不得的事情，开开心心跑到 b 碗（bowlroll）

从 b 碗里下载宣传图十分绚丽好看的场景，兴奋的导入 mmd 中一看！！

场景效果异常简陋！！

什么特效都没有！！

和宣传图完全不符...

原来 3D 场景需要复杂的渲染和配置材质，才能变得像 “卖家秀” 中一样好看

对新手 mmder 来说，很难直接渲染出好看的场景，而就算对老手 mmder 来说，

导入一个场景的材质，打光，都十分麻烦，地板要贴上地板的材质，

墙壁要贴上墙壁的材质，是不是感觉十分繁琐与重复？

大部分 mmder 每一次制作 mmd 时都要重复这些相同的过程，

感觉十分繁琐

于是我喜爱研究各种 mmd 中便利的技巧，如配置好一次材质渲染后，

下一次直接导入配置文件，即可马上恢复上一次配置好的材质，

该怎么做到这一点呢？先从普通的渲染讲起吧！

最基础的开始~

准备好模型文件和特效 fx，将模型 pmx 与特效 fx 文件放在同一个文件夹中

或者特效 fx 文件放在 PMX 所在文件夹中的子文件夹里，相对路径能找到的地方

总之要放在一起，如果没有把模型和特效放在一起，文件夹名称一变，就读取不了啦！

（相对路径是什么自己百度！！记得常用./ 和../）从右上角分配特效中打开 mme 特效面板，

右键模型选择展开，就能看见下面所有的材质，此时一个一个添加不同材质吧

![](https://i0.hdslb.com/bfs/article/8d37cdd19ea155e07cdfc39b731934710563f71f.png@942w_936h_progressive.webp)添加一堆材质…… 好麻烦!!!

！终于把材质添加好了！！那么怎么将这个配置保存成预设呢？

首先点击模型. pmx，让模型这一栏选中变蓝（重要，别忘了选中模型呀！！）

然后左上角文件 - 按模型单位保存模型，就可以单个模型保存出一个 emd 文件

![](https://i0.hdslb.com/bfs/article/8272fe139c706eaf8db5622d8dd6751178458a94.png@942w_521h_progressive.webp)如果没有按模型单位保存的话... 会变成以 pmm 全体模型的工程为单位保存吧...

就决定保存在和模型相同的目录~ 因为好找.

![](https://i0.hdslb.com/bfs/article/9cfd3db100a5cb55656cb290d196106a30224df2.png@942w_707h_progressive.webp)还真是完全的保姆式教学...

既然学会保存了，是不是也学会读取了呢？很简单，

只要从这里打开刚刚保存的文件就可以

![](https://i0.hdslb.com/bfs/article/8668e5e031fbe1cfdfd9d04f97a116cd2586dc15.png@803w_1040h_progressive.webp)

之前配置好的预设 fx 就被轻松读取了~

![](https://i0.hdslb.com/bfs/article/e53914d976a1a649417468a53c6077d09deffdbd.png@942w_594h_progressive.webp)

但这种方法还是要从右上角的 mme 材质面板中打开 emd 配置文件读取，

好像还是很麻烦耶~ 追求研究 mmd 到便利极致的我怎么能停下脚步呢——

能不能一载入模型或场景，就让它自动读取 fx？

能！方法很简单，只要你修改命名，把刚刚保存的 emd 配置文件的

文件名更改为和 pmx 相同的名称，并当前文件夹名称是纯英文，

一载入 pmx，fx 就自动读取好了！

![](https://i0.hdslb.com/bfs/article/82e342f458c1ddb25ee5e1ff1825192c800cb3f6.png@390w_312h_progressive.webp)命名要相同哦！其实还有 White[XXX.fx].pmx 的方式，但只能加一个 fx，不太好用

恭喜你，你已经学会怎么给一个 pmx 添加自动渲染了。

有人可能会问 Ray 怎么办，又要加 Main 栏，又要加 MaterialMap 栏，

那只要分别保存俩个栏的 emd，到时候在 ray 里分别读取即可~

![](https://i0.hdslb.com/bfs/article/5742ddf6f2d2fc543c470bf1c3d89cf18d592ab7.jpg@942w_516h_progressive.webp)

流程如图，都是差不多的，以后记得保存 emd，不要再重复加材质咯

但别急！但你还没学会怎么制作一个自动渲染的 pmm 格式 mmd 工程文件，

接下来，教你怎么打开一个 mmd 的工程，里面就是配置好的场景渲染效果吧！

可能有人会疑惑，mmd 怎么可能做相对路径工程？

没错，mmd 还真的支持相对路径，但是需要一个判定相对路径的契机，那就是

名称被命名为 “UserFile” 的文件夹，那么如何利用这个特性呢？

首先当然是准备好文件和文件夹

1. 创建文件夹（场景名称命名随意）

2. 在场景文件夹中创建文件夹 命名为 UserFile

3. 在 UserFile 文件夹中放入人物，场景，滤镜 x 文件

但以我个人的习惯，还是喜欢再创建文件夹进行分类：

创建 Model 文件夹，里面放入人物模型文件夹，与场景模型文件夹

Model 中人物和场景都像上面一样配置成一载入，fx 渲染就生效的那种.

Accessory 文件夹中里面放入 mme 特效文件夹，如 XX 滤镜，ScreenTex，SvSSAO 等

![](https://i0.hdslb.com/bfs/article/7df69ae75a4fd6f60bf1d90e4e4f051c16e67a14.png@587w_186h_progressive.webp)

但是特效是有限制的，那就是不能动 mme 面板，只能是直接载入就生效的 x 文件特效.

如果你要动 mme 面板中的内容，如调节部分材质钩子与 fx，那现在这里就不行（下面会解决）

4. 打开新建工程的 mmd，读取场景，人物，特效 x 文件，

配置好画面效果（注意模型与附件描画顺序）保存 pmm

重点来了

把 pmm 保存到命名为 UserFile 的文件之中

现在这个文件夹应该这样的：

![](https://i0.hdslb.com/bfs/article/aa9fa6e2c21d6cb7dabc90a8f55eef5490f8e32e.png@942w_351h_progressive.webp)一般我命名为 Stage.pmm

恭喜你，你完成了基础的 pmm 工程相对路径封包，

但是别高兴的太早，你发现更改一下场景命名，mme 就会出错，

因为你会发现 Stage.pmm 旁边，有一个和 pmm 相同名称的 Stage.emm 文件，

还记得上面是按模型文件保存 XX 的吗？其实这个 emm 文件就是工程版本的 emd，

但现在为了做一键渲染的工程，这个 emm 文件是不需要的，只要删除这个 emm 文件，

直接运行 pmm 文件，里面就是配置好的内容啦！

其实在右上角 mme 插件中选择不自动保存配置文件的话，

就不会跟着一起保存出这个 emm 文件了，但为了以防翻车，

还是，每次保存后手动删除 emm 文件比较好，别问为什么...

![](https://i0.hdslb.com/bfs/article/36f4aec4d155f1e74e6856c7983883c2e4ce0797.png@528w_468h_progressive.webp)小知识：加了很多 fx 后关闭自动更新，不监视 fx 文件的 mmd 能大幅提高帧率

现在你可以再在 pmm 工程中添加一些小彩蛋，

给人物摆个姿势或小动画，给场景 k 帧加一些动态，k 个好看的镜头保存，

之后发给别人，打开 pmm 文件，就是有一个漂亮渲染，fx 全配置好的工程啦！

当然带控制器的 x 特效也可以，比如 ikBokeh 景深，用控制器设置成

自动聚焦模式，就能很方便的读取带景深和渲染的场景了

如此例，发给别人后，别人一打开 pmm 工程，就是这个画面，

是不是谜之很震撼，有种 Sketchfab 的感觉

![](https://i0.hdslb.com/bfs/article/325dc6eeba04faa1aaa38953e08335b8a2c4cfe0.png@942w_497h_progressive.webp)原理都一样

如此一来，pmm 就会自动读取 pmx 和 x 文件，pmx 会因为有 emd 自动读取 fx 渲染，

而 x 文件滤镜 mme 也因为会自动挂载相同名称的 fx 而生效

但是这有一个致命的缺点——无法改动 mme 面板中的内容，

因为你会把 emm 文件删掉，做到每次读取都重新配置 mme 路径，

因此不能调整 mme 面板中的任何 fx 和钩子...

也就是说，不能用 Ray！！NOOO——

这确实是困扰我很久的一个问题，mmd 竟然能以这样奇葩的方式支持了相对路径，

但 mme 插件保存出来的 emm 配置文件，竟是不支持任何相对路径的...

为了让自动渲染能用上需要调节控制面板的 mme，我开始想各种办法，

于是得到了俩个方法，方法 1 和方法 2，这俩个方法也可以同时使用，

但最佳最便利的方法其实是方法 2，想看的建议直接跳到方法 2.

方法 1 有很大缺点，但想看也可以先看看，

因为方法 1 不能根据材质设置不同 fx.

方法 1：通过修改 fx 文件，让某些模型默认挂载不同的 fx

当你载入一些 x 格式的 mme 特效后，mme 面板就会多出该特效的调节栏，

第一排会有谜之灰色代码，那就是用于设定初始挂载什么 fx

比如这个 SvSSAO，我想修改 NormalMapRT 栏中默认挂载 fx 的状态

![](https://i0.hdslb.com/bfs/article/51a304dc4ad1b3376ea0eed39d867ff7f69916d1.png@864w_612h_progressive.webp)代码痴一脸懵逼

通过搜索关键词 DefaultEffect，发现在 SvSSAO.fx 的 407 行开始，

可以设定 x 和 pmx 的默认状态

=xxx.fx 为此栏默认挂载该 fx

=hide 为隐藏，默认不勾显示钩子

=none 为不隐藏但不添加任何 fx

![](https://i0.hdslb.com/bfs/article/29ddbb610afb19a2238ffc0688473854feb25889.png@942w_584h_progressive.webp)

在这里，我只要把可能对 SvSSAO 效果会造成干扰的物件进行屏蔽隐藏即可，

所以我设置了一堆的 = hide，这样一读取这些名称的模型，

SvSSAO 就能自动屏蔽这些不需要的模型了

Ray 也是用此设定 DefaultEffect

给天空球默认添加一个 none 环境光，和给材质添加一个 material_2.0 材质球的

![](https://i0.hdslb.com/bfs/article/92e394a2ffea0971a73cbeb58f5908f34189ad29.png@942w_558h_progressive.webp)在 104 行可进行修改

原来环境光的 DefaultEffect 藏在.\ray-mmd-1.5.2\Shadertextures.fxsub 中，

默认用相对路径指定了这个 skylighting_none.fx 并把其他物体设置为无环境光

学学怎么写相对路径后，可以在这里添加特定名称的 pmx 设定

让 ray 自动挂载想要的天空球环境光

当然除了环境光外，下面还有其他的比如 MaterialMap 材质栏，

SSAOMap 缝隙阴影栏，PSSM 阴影显示栏等多处的 DefaultEffect 设定

![](https://i0.hdslb.com/bfs/article/c54dfe86616b42a7eca28048954c7e632ef06af6.png@942w_761h_progressive.webp)

如果你让 ray 载入模型后自动挂载一个卡通材质 fx，也是可以在这修改与添加啦！

但因为方法 1 只能对每个模型单独进行设定，不能根据材质分别设定 fx，

所以还是不能用于给 ray 加材质，而且很麻烦！我绕了很大的弯路呀 qwq

赶快抛弃这个繁杂的方法 1，看看方法 2 吧.

方法 2 就是——编写一个读取当前目录并修正 mme 路径的小程序~

也就是对 emm 文件中的路径信息动刀，这是我的想法：

准备好一个等待修改 mme 目录的配置目录用 emm 文件

把小程序放在和 pmm 相同的目录中，首先让小程序检测当前在什么目录，

把当前的目录信息添加到配置用的 emm 文件中，保存为和 pmm 命名相同的 emm 文件

这样一来，即可完成修正 mme 路径了 xd

（P.S. 不建议 emd 自动加 fx 那招和这个一起用，虽然也没啥太大问题...

但你配置好 emm 之后，后续才添加 emd 会有问题（？））

这是小程序 bat 中的内容

![](https://i0.hdslb.com/bfs/article/af0642329424ddbd93cdf62ea170461f062ded02.png@942w_912h_progressive.webp)

把以下这些代码保存到 txt 文本（GB2312 编码），把 txt 格式尾名改为 bat，

就是能运行这些指令的 bat 批处理小程序了：

@echo off

color f0

title MME FIX

echo Detecting drive letter and path for current location:

echo 正在检测当前位置的盘符和路径：

echo Start repairing Mme path:

echo 即将开始修复 mme 路径:

echo ...Loading files...

echo ... 读取文件中...

set "currentpath=%~dp0"

if "%currentpath:~-1%" equ "\" set "currentpath=%currentpath:~,-1%"

cd /d "%currentpath%"

set "txtfile1=%currentpath%\MME.emm"

set "txtfile2=%currentpath%\Stage.emm"

set "oldword=--Waiting for edit path--"

set "newword=%currentpath%"

echo ...Repair path...

echo ... 修正路径中...

(echo;txt1=WSH.Arguments^(0^):txt2=WSH.Arguments^(1^):ow=WSH.Arguments^(2^):nw=WSH.Arguments^(3^)

echo;enc="GB2312"

echo;Set stream=CreateObject^("ADODB.Stream"^)

echo;stream.Type=2:stream.Mode=3

echo;stream.Charset=enc

echo;stream.Open^(^)

echo;stream.LoadFromFile txt1

echo;stream.Position=0

echo;text=stream.ReadText^(^)

echo;text=replace^(text, ow, nw^)

echo;stream.Position=0

echo;stream.WriteText text

echo;stream.SaveToFile txt2, 2)>"%tmp%\v.v"

if not exist "%txtfile1%" (echo;"%txtfile1%" not found&goto end)

for /f "delims=" %%a in ("%txtfile2%") do md "%%~dpa" 2>nul

cscript -nologo -e:vbscript "%tmp%\v.v" "%txtfile1%" "%txtfile2%" "%oldword%" "%newword%"

:end

for /l %%i in (1,1,2000) do echo %%i >nul

echo MME Repair complete.

echo 修复 mme 路径已成功.

pause

exit

另外一边，当然是要准备好替换目录信息的 emm 文件，

复制出正常保存出来的 emm 文件更名为 MME.emm，用文本打开，

把盘符到 \ UserFile 为止的内容都全部替换为上面 bat 设定好的文本内容：

“--Waiting for edit path--”

![](https://i0.hdslb.com/bfs/article/0b5344e5371498de5169a4f116040ff5929d5b28.png@942w_569h_progressive.webp)别替换错内容了哦！！注意 \ 的位置和空格

以后只要一运行 bat 程序，就能从 MME.emm 文件中配置出正确路径的 Stage.emm 了

![](https://i0.hdslb.com/bfs/article/97e7786f378a45653fe79f0c663758f825c8f625.png@473w_395h_progressive.webp)但是打包一键渲染后发给别人时要记得删除哦，虽然不删也没啥事 x

于是我用这个原理，制作了不少一键渲染 ray 渲的场景

打包时记得写好完整的借物表，以及注意不能二配的素材哦

但是。。。

翻车了，b 碗把我的 ray 自动渲染场景都下架了...

... 原因就在那个小程序

![](https://i0.hdslb.com/bfs/article/15ac6d1cee2ab41cc0392e1c40fc09b9e600b77d.png@942w_528h_progressive.webp)

因为我考虑到如果有人把场景解压在了 C 盘，系统盘，系统有关目录中，

bat 小程序会因为防火墙，没有管理员权限修改保存 emm 文件而失效...

为了防止这件事情的发生，我也想了对策，

既然都做保姆擦屁股了！那就要擦到底 X

我想了一个方法，把 bat 封包成一个运行时自动需求管理员权限的 exe 文件，

当有人使用 bat 版本因为没权限而失效时，可以用能获取管理员权限的 exe 版本解决，

这样一来，就不怕修正 mme 路径失效了！

但正因我给 bat 程序加壳封包，导致了一部分杀毒软件的误报，

我的投稿中收到了这样的评论：

![](https://i0.hdslb.com/bfs/article/0b4323071aef0378175d79680790c457b64bf91c.png@942w_725h_progressive.webp)

我是否加了恶意病毒，是否是恶意软件分销商，

也请阅读这篇专栏的人自行判断。

![](http://i0.hdslb.com/bfs/article/2945529f9b15ae181e7e6849bebb636f0c2a20a0.png@942w_956h_progressive.webp)

我投稿了一年的自动渲染，四个自动渲染场景都被举报不放过，我天美的谢谢你

打包一次一个自动渲染的场景，又要建模，又要做材质，又要配置特效，又要封包，

制作和配布都来之不易，其中费劲了我心血研究怎么让他人使用更加便利，

却因此搬起石头砸了自己的脚

![](https://i0.hdslb.com/bfs/article/22fb0d734078618944b51408b00478c62f9de5c4.png@942w_338h_progressive.webp)

昨晚我在紧急联系了 bowlroll 官方推特，

b 碗经理果然解释是因为接到了举报，并且误 Northon 确实报毒，

我表达了我的愤怒，争取到了把投稿文件恢复到未公开的状态

但现在还没有回复不清楚能否重新公开我的场景

我费尽心思搞自动渲染的目的大概是气死我自己吧

---------     ---------

现在码这段字已经是第二天，收到了 b 碗回复：

如果去除了病毒，可以重新公开，b 碗官方也会重新对文件进行检测，

虽然是喜事，但看来官方依然认为这是一个病毒，让我感觉很难过

我之后还是会坚持自己的清白

总之终于码完了我所知的 mmd 自动渲染全部方法，你学废了吗？

这么受苦受累的保姆怎么能只有我一个人当呢，带上大家一起受苦受累才好玩啊

顺便贴一下我的 b 碗账号，之后会重新公开这些场景

https://bowlroll.net/user/182602