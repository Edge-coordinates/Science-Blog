---
title: WorldEdit  教程
categories:
  - Minecraft
reprint: true
abbrlink: 8568c97d
tags:
---
- [WorldEdit 使用教程](#worldedit-使用教程)
  - [命令](#命令)
    - [选择选区](#选择选区)
      - [选择长方体](#选择长方体)
      - [选择你的当前位置（//pos1、//pos2）](#选择你的当前位置pos1pos2)
      - [选择十字准星指向的位置（//hpos1、//hpos2）](#选择十字准星指向的位置hpos1hpos2)
      - [选择所在区块（//chunk）](#选择所在区块chunk)
      - [使用法杖选择（//wand）](#使用法杖选择wand)
    - [/toggleeditwand](#toggleeditwand)
    - [调整选区](#调整选区)
      - [缩小选区（//contract）](#缩小选区contract)
      - [移动选区位置（//shift）](#移动选区位置shift)
        - [在各轴同时扩张（//outset）](#在各轴同时扩张outset)
        - [在各轴同时收缩（//inset）](#在各轴同时收缩inset)
      - [扩展选区（//expand）](#扩展选区expand)
    - [选区信息](#选区信息)
      - [获得选区尺寸（//size）](#获得选区尺寸size)
      - [获取一种方块的数量（//count）](#获取一种方块的数量count)
      - [获取方块分布率（//distr）](#获取方块分布率distr)
    - [选择模式（//sel）](#选择模式sel)
      - [长方体选择模式（//sel cuboid）](#长方体选择模式sel-cuboid)
      - [长方体扩大选择模式（//sel extend）](#长方体扩大选择模式sel-extend)
      - [多边形选择模式（//sel poly）](#多边形选择模式sel-poly)
      - [椭球选择模式（//sel ellispoid）](#椭球选择模式sel-ellispoid)
      - [球体选择模式（//sel sphere）](#球体选择模式sel-sphere)
      - [圆柱体选择模式（//sel cyl）](#圆柱体选择模式sel-cyl)
      - [多面体选择模式（//sel convex）](#多面体选择模式sel-convex)
  - [选区操作命令](#选区操作命令)
    - [设置选区内所有方块（//set）](#设置选区内所有方块set)
    - [//line](#line)
    - [//curve](#curve)
    - [替换方块（//replace，或 //re、//rep）](#替换方块replace或-rerep)
    - [表面覆盖（//overlay）](#表面覆盖overlay)
    - [//center（或 //middle）](#center或-middle)
    - [自然化（//naturalize）](#自然化naturalize)
    - [在正方体四周建立墙壁（//walls）](#在正方体四周建立墙壁walls)
    - [//faces（或 //outline）](#faces或-outline)
    - [平滑化（//smooth）](#平滑化smooth)
    - [移动（//move）](#移动move)
    - [堆叠（//stack）](#堆叠stack)
    - [重新生成（//regen）](#重新生成regen)
    - [变形（//deform）](#变形deform)
    - [//hollow](#hollow)
    - [//forest](#forest)
    - [放置植物群（//flora）](#放置植物群flora)
  - [导入导出和剪贴板命令](#导入导出和剪贴板命令)
    - [导入与导出（/schematic、/schem、//schematic、//schem）](#导入与导出schematicschemschematicschem)
      - [显示可用的 schematic 文件列表（//schematic list）](#显示可用的-schematic-文件列表schematic-list)
      - [//schematic load 和 //schematic save](#schematic-load-和-schematic-save)
      - [//schematic delete](#schematic-delete)
      - [文件保存位置](#文件保存位置)
    - [复制与剪切（//copy、//cut）](#复制与剪切copycut)
    - [粘贴（//paste）](#粘贴paste)
    - [旋转（//rotate）](#旋转rotate)
    - [翻转（//flip）](#翻转flip)
    - [清空剪贴板（/clearclipboard）](#清空剪贴板clearclipboard)
  - [生成命令](#生成命令)
    - [圆柱体（//cyl）与空心圆柱（//hcyl）](#圆柱体cyl与空心圆柱hcyl)
    - [椭圆形圆柱体和椭圆形](#椭圆形圆柱体和椭圆形)
    - [球体和椭球体（//sphere）](#球体和椭球体sphere)
    - [金字塔（//pyramid 和 //hpyramid）](#金字塔pyramid-和-hpyramid)
    - [森林（/forest 和 //forest）](#森林forest-和-forest)
    - [南瓜丛（/pumpkins）](#南瓜丛pumpkins)
    - [任意表达式图像生成（//g、//gen、//generate）](#任意表达式图像生成ggengenerate)
  - [效用性命令](#效用性命令)
    - [填充凹洞（//fill）](#填充凹洞fill)
      - [递归填充（//fillr）](#递归填充fillr)
    - [抽空池塘（//drain）](#抽空池塘drain)
    - [修复池塘（/fixwater、/fixlava、//fixwater、//fixlava）](#修复池塘fixwaterfixlavafixwaterfixlava)
    - [修改附近方块](#修改附近方块)
      - [移除上方和下方的方块（/removeabove、/removebelow、//removeabove、//removebelow）](#移除上方和下方的方块removeaboveremovebelowremoveaboveremovebelow)
      - [移除附近方块（/removenear、//removenear）](#移除附近方块removenearremovenear)
      - [替换附近方块（/replacenear、//replacenear）](#替换附近方块replacenearreplacenear)
    - [模拟降雪（/snow、//snow）](#模拟降雪snowsnow)
    - [解冻区域（/thaw、//thaw）](#解冻区域thawthaw)
    - [模拟草地生长（/green、//green）](#模拟草地生长greengreen)
    - [扑灭火焰（/extinguish、/ext、/ex、//extinguish、//ext、//ex）](#扑灭火焰extinguishextexextinguishextex)
    - [移除生物（/butcher）](#移除生物butcher)
    - [/remove、/rem、/rement](#removeremrement)
    - [//calculate、//calc、//eval、//evaluate、//solve](#calculatecalcevalevaluatesolve)
    - [//help](#help)
  - [区块命令](#区块命令)
    - [区块信息（/chunkinfo）](#区块信息chunkinfo)
    - [列出区块（/listchunks）](#列出区块listchunks)
    - [删除区块（/delchunks）](#删除区块delchunks)
  - [快照命令](#快照命令)
  - [脚本命令](#脚本命令)
    - [/cs](#cs)
    - [/.s](#s)
  - [超级镐子命令（/superpickaxe、/pickaxe、/sp）](#超级镐子命令superpickaxepickaxesp)
    - [瞬间采集（/sp single）](#瞬间采集sp-single)
    - [瞬间破坏区域（/sp area、/sp recursive、/sp recur）](#瞬间破坏区域sp-areasp-recursivesp-recur)
  - [生物群系命令](#生物群系命令)
    - [/biomelist](#biomelist)
    - [/biomeinfo](#biomeinfo)
    - [//setbiome](#setbiome)
  - [工具（/tool）](#工具tool)
    - [树木生成工具（/tool tree）](#树木生成工具tool-tree)
    - [浮空树木清除工具（/tool deltree）](#浮空树木清除工具tool-deltree)
    - [方块替换工具（/tool repl）](#方块替换工具tool-repl)
    - [远程建筑工具（/tool lrbuild）](#远程建筑工具tool-lrbuild)
    - [远距离魔杖（/tool farwand）](#远距离魔杖tool-farwand)
    - [循环工具（/tool cycler）](#循环工具tool-cycler)
    - [查询工具（/tool info）](#查询工具tool-info)
    - [颜料桶填充（/tool floodfill 或 /tool flood）](#颜料桶填充tool-floodfill-或-tool-flood)
    - [解除工具绑定（/tool none 或 /tool unbind）](#解除工具绑定tool-none-或-tool-unbind)
  - [刷子命令（/brush、/br、//brush、//br）](#刷子命令brushbrbrushbr)
    - [森林刷子（/br forest）](#森林刷子br-forest)
    - [圆柱体刷子（/br cylinder、/br cyl、/br c）](#圆柱体刷子br-cylinderbr-cylbr-c)
    - [/br set](#br-set)
    - [/br apply](#br-apply)
    - [/br deform](#br-deform)
    - [/br lower](#br-lower)
    - [/br butcher 或 /br kill](#br-butcher-或-br-kill)
    - [/br paint](#br-paint)
    - [/br none 或 /br unbind](#br-none-或-br-unbind)
    - [剪贴板刷子（/br clipboard 或 /br copy）](#剪贴板刷子br-clipboard-或-br-copy)
    - [/br gravity 或 /br grav](#br-gravity-或-br-grav)
    - [/br ex 或 /br extinguish](#br-ex-或-br-extinguish)
    - [球体刷子（/br s 或 /br sphere）](#球体刷子br-s-或-br-sphere)
    - [/br raise](#br-raise)
    - [平滑刷子（/brush smooth）](#平滑刷子brush-smooth)
    - [刷子设定](#刷子设定)
      - [蒙版](#蒙版)
      - [尺寸](#尺寸)
  - [传送命令](#传送命令)
    - [解放自己（/unstuck 或 /!）](#解放自己unstuck-或-)
    - [上升（/ascend）与下降（/descend）](#上升ascend与下降descend)
    - [上升到屋顶（/ceil）](#上升到屋顶ceil)
    - [穿过墙壁（/thru）](#穿过墙壁thru)
    - [跳跃至视野内目标方块（/jumpto 或 /j）](#跳跃至视野内目标方块jumpto-或-j)
    - [上升任意距离（/up）](#上升任意距离up)

#  WorldEdit 使用教程

> 原文地址 [mineplugin.org](https://mineplugin.org/WorldEdit/%E5%91%BD%E4%BB%A4#.E8.A1.A8.E9.9D.A2.E8.A6.86.E7.9B.96.EF.BC.88.2F.2Foverlay.EF.BC.89)

命令
--

### 选择选区

WorldEdit 的一个最基本的部分是使用选区进行的操作。举个例子，如果你想把一个方形区域内的草方块换成泥土，你需要告诉 WorldEdit 这个方形区域的位置。

WorldEdit 提供了多种选择一个要进行修改的选区的命令，这个部分将会向你介绍选择选区和你可以对选区进行的操作。

#### 选择长方体

WorldEdit 允许你以选择长方体的两个角上的点的方式来选择长方体（想象一个 3D 的长方体）。

下方的图展示了如何用两点形成一个长方体。你选择的长方体必须与地图对齐（他们不能被以一个角度旋转）。

[![](https://mineplugin.org/images/0/05/WorldEdit_Cuboid.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Cuboid.png)

有许多方法可以用来选择这两个点，你可以混合使用这些方法。

#### 选择你的当前位置（//pos1、//pos2）

*   //pos1 [x,y,z]
*   //pos2 [x,y,z]

使用这些命令（空参数时）可以将你所站的方块上方一个方块的位置分别设定为第一个和第二个角。或添加参数指定坐标，选取指定坐标点。

一般使用法杖可以完成大部分操作，所以一般不会使用到这些命令。（有趣的是当你使用 ScriptBlock 插件时，可以使用此命令让脚本执行 we 的操作。）

#### 选择十字准星指向的位置（//hpos1、//hpos2）

*   //hpos1
*   //hpos2

这两个命令会将你十字准星所指的位置分别设置为第一个和第二个顶点。通过这个方式可以选择远处的点以及方便地选择非常大的长方体选区。

#### 选择所在区块（//chunk）

*   //chunk

这个命令会选择你所站区块的所有方块。区块是 16x16, 256 格高的范围。

#### 使用法杖选择（//wand）

*   //wand

最直观的选择选区的方式是使用法杖。使用 //wand 可以得到法杖（默认为木斧）。用法杖左键点击一个方块会把这个方块位置设定为你要选择的长方体的第一个角，右键点击会选择第二个角。

### /toggleeditwand

提醒用户这个法杖现在是一个工具，可以用 / none 解绑。

### 调整选区

#### 缩小选区（//contract）

*   //contract <数量> [反方向数量] [方向]

这个命令与 //expand 类似。

例子：向下收缩

使用 //contract 10 down 将选区会从上往下进行收缩。

[![](https://mineplugin.org/images/3/37/WorldEdit_Cuboid_contraction_down.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Cuboid_contraction_down.png)

#### 移动选区位置（//shift）

*   //shift <数量> [方向]

移动选区。这个命令的效果类似与向两个相反方向分别进行相同移动量的 //expand 与 //contract。如此会将选区移动一段距离。这个命令**不会**移动选区中的**内容**。（如果要达到该效果需要使用 [//move](#.2F.2Fmove) 命令，如需同时移动选区内容和位置，可以给 //move 添加 - s。）

##### 在各轴同时扩张（//outset）

这个命令会将选区向内缩小。

*   //outset <数量> [-hv]
*   -h 表示只水平方向上（horizonally）收缩。
*   -v 表示只竖直方向上（vertically）收缩。

##### 在各轴同时收缩（//inset）

这个命令会将选区向内缩小。

*   //inset <数量> [-hv]
*   -h 表示只水平方向上（horizonally）收缩。
*   -v 表示只竖直方向上（vertically）收缩。

#### 扩展选区（//expand）

*   //expand <数量> [反方向数量] [方向]
*   //expand vert

这些命令可以简单地以许多方式扩大选区:

*   给出一个方向（north、south、west、east、up、down）
*   看向一个方向（me、back）
*   扩大选区到基岩和天空

如果你想选择看向的一个方向，使用 me 或不输入方向参数来指定那个方向，也可以用 back 表示与看向的方向相反的方向。

你可以指定两个数字来使选区同时向两个方向扩大选区。使用 //expand vert 可以将选区竖直方向扩展到整个世界的限度。

例子：向上收缩

使用 //expand 10 up 将选区向上扩大

如图，选区向上扩大 [![](https://mineplugin.org/images/b/b2/WorldEdit_Cuboid_expansion_up.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Cuboid_expansion_up.png)

### 选区信息

WorldEdit 提供了一些可以得到选择的区域的信息的命令。

#### 获得选区尺寸（//size）

*   //size [-c]

显示选区内的方块数量。空气方块不会被计算。

v.5.5 以上，使用 - c 标签会对剪贴板进行计算

#### 获取一种方块的数量（//count）

*   //count <方块种类>

显示一种指定方块在选区内的数量。

v.5.5.1 以上，使用 - d 标签可以支持不同附加值的方块。注意使用 - d 标签是需要给出一个附加值。

例子：

```
//count 火把
数量：34
//count -d 火把[facing=west]
数量：3
```

#### 获取方块分布率（//distr）

*   //distr [-cd] [-p < 页面 >]
*   使用 - c 会对剪贴板内容进行计算（v.5.5 以上）。
*   使用 - d 会对不同状态的方块进行区分（v.5.5.1 以上）。

显示选区内的方块分布。

例子：

```
# Total Block Count: 6
16.667% 1 石头
33.333% 2 圆石
50.000% 3 空气
```

例子：//distr 与 //distr -d 的区别（为比较省略了部分结果输出）

```
//distr
...
34      (0.386%) 火把 #50
500     (5.682%) 石砖楼梯 #109
```

```
//distr -d
...
3       (0.034%) 火把 #50:1
4       (0.045%) 火把 #50:3
7       (0.080%) 火把 #50:2
7       (0.080%) 火把 #50:4
13      (0.148%) 火把 #50:5
46      (0.523%) 石砖楼梯 #109:2
48      (0.545%) 石砖楼梯 #109:3
62      (0.705%) 石砖楼梯 #109:0
64      (0.727%) 石砖楼梯 #109:1
68      (0.773%) 石砖楼梯 #109:6
69      (0.784%) 石砖楼梯 #109:5
71      (0.807%) 石砖楼梯 #109:7
72      (0.818%) 石砖楼梯 #109:4
```

### 选择模式（//sel）

除 cuboid 外，其他选区模式在左键选点后再次左键选点会重置选区。

#### 长方体选择模式（//sel cuboid）

*   //sel cuboid

左键点击选择第一个点，右键点击选择第二个点。选区为两个点形成的长方体。

#### 长方体扩大选择模式（//sel extend）

*   //sel extend

`v.4.8-SNAPSHOT以上`左键点击选择第一个点。之后的选择点使用右键选择。每次右键选择都会将长方体选区扩大以包含新的选择点。

#### 多边形选择模式（//sel poly）

*   //sel poly

左键点击选择第一个选择点。之后所有的选择点使用右键点击。每次右键点击选择都会增加一个新的点。顶部和底部将始终包含所选的最高点和最低点。

#### 椭球选择模式（//sel ellispoid）

*   //sel ellipsoid

左键点击选择中心，右键点击扩大选区。你可以通过分别多次点击以控制 x、y、z 半径。

#### 球体选择模式（//sel sphere）

*   //sel sphere

左键点击选择中心，右键点击扩大选区。选区总是为以第一个点为中心、到第二个点作为半径的一个球体。

#### 圆柱体选择模式（//sel cyl）

*   //sel cyl

左键点击选择中心点，右键点击扩大选区。第一次右键点击可以扩大圆柱体的底面，第二次右键点击可以提升圆柱体的高度。

#### 多面体选择模式（//sel convex）

*   //sel convex

`v6.0以上`左键点击选择第一个点，其余的点使用右键点击选择。选区是一个包含所有选定的点的凸面外壳。

选区操作命令
------

选择了选区之后，真正有趣的部分就要开始了。现在，你可以对你的选区进行各种功能各样的操作。

### 设置选区内所有方块（//set）

*   //set <方块样式>

**方块样式**可以是一个单一的方块的带有命名空间的 ID（其中原版命名空间`minecraft:`是可以省略的；方块的带有命名空间的 ID 的列表可以在 Minecraft wiki 上找到，或者，在游戏内按`F3+H`，这样在物品栏指向一个物品时，可以显示方块的带有命名空间的 ID），支持数字 ID（即使是在 Minecraft 1.13 以上的版本）。关于方块样式的用法，请参考本页面的[#方块样式](#.E6.96.B9.E5.9D.97.E6.A0.B7.E5.BC.8F)段落。

例子：设定选区为玻璃方块

//set glass

例子：删除选区内方块（将选区内的方块设为空气）

//set air 或 //set 0

注意：这些命令只有在选好了选区之后才能够进行！

如果你要_填充_一个区域，使用 //replace 或者 //fill 效果更好（接下来会提到）。

### //line

*   //line [-h] < 样式 > [粗细]
*   -h：仅生成外表

在长方体选区的两个顶点之间，或凸多面体选区顶点之间绘制线段。只能与长方体选区或凸多面体选区一起使用。

### //curve

*   //curve [-h] < 样式 > [粗细]

通过选择的点绘制曲线。只能用于凸多面体选区。

### 替换方块（//replace，或 //re、//rep）

*   //replace [要替换掉的方块] < 用于替换的方块 >

虽然设定方块很有用，但是有时你需要根据一些规则替换一些已有的方块。WorldEdit 可以将一种方块、多种方块或者所有的非空气方块替换成指定的方块。

让我们来看几个例子。

*   例：将所有非空气方块替换为草方块
    *   //replace grass

如果你想选择需要替换掉哪些方块，将它放在最后一个参数之前。

*   例：将所有原石方块替换为白色羊毛方块
    *   //replace stone white_wool

如果你想替换掉一系列方块，在它们之间加上逗号即可。

*   例：将泥土和草方块都替换为钻石矿
    *   //replace grass_block,dirt diamond_ore

自己试试吧！记住你也可以通过替换空气方块的方式填充一个区域（虽然有一个对应的命令，后面会提到）。

*   例：将空气方块替换为红石矿
    *   //replace air redstone_ore

你可以使用这个命令将空气方块替换为水或熔岩（旧称岩浆）来达到填充区域的效果，但是 //fill 命令更加适合。

本命令支持[#方块样式](#.E6.96.B9.E5.9D.97.E6.A0.B7.E5.BC.8F)。

### 表面覆盖（//overlay）

*   //overlay <方块样式>

//overlay 命令允许你在选区内的方块表面覆盖一层另一种方块。

只有选区内最上方的方块会被覆盖；如果你的选区内有一个洞穴，它不会被覆盖，除非它是露天的，或者你的选区范围没有延伸到洞穴之上。你可以使用这个命令来创建积雪（虽然 WorldEdit 有一个可以更好地完成这个操作的命令，会顾及到积雪不应该覆盖所有方块，比如火把上的问题），或者将栅栏覆盖到一个平坦过不平坦的表面。

例子：在选区上覆盖草方块

//overlay grass_block

`v.3.0以上`本命令支持方块图案。

### //center（或 //middle）

*   //center

设置中心方块。

### 自然化（//naturalize）

*   //naturalize

这个指令会使用石头、泥土与草方块 “自然化” 选区内容，以顶层草方块，下方 3 格泥土方块，泥土方块下方石头方块的构造对选区内方块进行替换。这个命令是一个需要使一个区域“看起来自然” 时可以使用的简单指令。

[![](https://mineplugin.org/images/1/1d/WorldEdit_Naturalize.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Naturalize.jpg "使地形看起来自然。")

### 在正方体四周建立墙壁（//walls）

*   //walls <方块样式>

//walls 命令只会在你的选区四周创建墙壁，即会忽略房顶与地板。

### //faces（或 //outline）

*   //faces <方块样式>

为选区建造墙壁、天花板和地板。

### 平滑化（//smooth）

*   //smooth [迭代次数] [蒙版]

如果你需要使一个粗糙的物体（如粗糙的山）更加平滑，这个指令可以做到。首先确认你选择了整个区域的选区，之后再使用命令。此外可以额外注明迭代次数，以达到连续多次进行算法计算来使结果成为更加平滑的表面。

### 移动（//move）

*   //move [-abes] [距离] [方向] [填充方块] [-m <mask>]
*   -s 表示将选区连同其内容移动到被移动的位置（默认情况下，选区的内容被移动后，选区仍留在原处）
*   -a 忽略空气方块
*   -e 同时复制实体
*   -b 同时复制生物群系

如果你建了一些东西，然后发现你需要把它向一边移动一点，这个命令十分好用，因为它可以移动整个选区的内容。

这个命令接受一个需要移动的距离，一个可选的方向，和一个填充移动后留下的空白的方块种类。

例子：将选区向上移动 2 格

`//move 2 up`

默认情况下，你不需要提供一个填充用方块，留下的区域将会是空气方块。如果你需要，可以指定另一种方块（方块样式）。

例子：将选择区域内容向朝向方向移动 2 方块，原位置留下石头

`//move 2 me stone`

例子：将选区内容向下移动 2 方块，复制空气方块

`//move 2 down`

例子：将选区内容向下移动 2 方块，同时移动选区，复制空气方块

`//move -s 2 down`

注意:

*   WorldEdit 的复制功能受 Minecraft 的特殊方块的限制（需要验证）。
*   特殊方块指 Minecraft 中带有标签的方块，如命令方块、装有东西的箱子等。
*   因为这个原因，某些操作无法还原，撤销操作也受相同的影响。

### 堆叠（//stack）

*   //stack [-abes] [次数] [方向] [-m <mask>]
*   -s 表示将选区移动到最后一个被堆叠的位置
*   -a 忽略空气方块
*   -e 同时复制实体
*   -b 同时复制生物群系

这个命令会向你所看的方向重复放置你的选区内容。你可以用这个命令延长桥梁、建造隧道或地铁，以及其他重复同一种结构的操作。

例子：将选区内容堆叠 50 次

`//stack 50`

例子：将选区内容向上堆叠 5 次

`//stack 5 up`

例子：将选取中的石头堆叠 5 次

`//stack 5 -m stone`

[![](https://mineplugin.org/images/4/49/WorldEdit_Bridge_stack.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Bridge_stack.jpg)

利用 WorldEdit 延长桥梁

//stack 命令允许你复制任何方块，无论 WorldEdit 的方块配置是怎样的。

[![](https://mineplugin.org/images/f/fd/WorldEdit_Tunnel_stack.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Tunnel_stack.jpg)

简单地延长一个隧道。注意将房顶与地板包括在选区内。

此命令也支持水平斜方向（东南、西南等）。

### 重新生成（//regen）

*   //regen

`v.4.2以上`这个命令会将你的选区重新生成为第一次生成地图时的状态。它会使用地图的种子，所以每次生成总会生成同样的地形。

注意：如果你的地图是通过外部地图生成器预生成的，或者该地区是在地形生成器修改之前生成的，这个指令不会如你所愿地运行。

### 变形（//deform）

*   //deform [-or] < 表达式…>
*   -r 使用游戏坐标原点
*   -o 使用选区中心原点
*   如果不使用标签，坐标会被正常化至 - 1..1

`v.4.8-SNAPSHOT以上`对选区内容进行一个由用户指定的形变：

*   旋转
*   把你心爱的教堂变成达利风格作品
*   其他任何你能想象的东西

标签:

变量:

*   x, y, z (输入 / 输出) - 坐标

例子：使地形变得颠簸

`//deform y+=0.2*sin(x*10)`

本命令使用表达式解析器。

### //hollow

*   //hollow [粗细] [样式]

清空此选区中包含的物体。厚度是以曼哈顿距离来测量的。

### //forest

*   //forest [类型] [密度]

生成森林。

### 放置植物群（//flora）

*   //flora [密度]

这个命令会将草丛与花以及仙人掌分散放置在选区内的草方块和沙子方块上。

导入导出和剪贴板命令
----------

WorldEdit 提供了一个非常强大的剪贴板功能，允许你复制一个区域，粘贴它，甚至将其保存为文件或从文件导入。剪贴板内容现在仅支持长方体并且复制时会使用你的选区范围。

### 导入与导出（/schematic、/schem、//schematic、//schem）

WorldEdit 可以使用_.schematic_文件来保存和加载副本。_.schematic_文件的好处是它与例如 MCEdit, NBTedit 和 Redatone Simulator 等程序兼容。这个格式也支持所有的 Minecraft 方块数据并有相关的支持文档让你可以在你自己的程序中使用它。

#### 显示可用的 schematic 文件列表（//schematic list）

*   //schematic list 或 ls 或 all [-dn] [-p < 页面 >]

`v.5.5以上`：

*   -d：按日期排序，旧的在前。
*   -n：按日期排序，新的在前。

#### //schematic load 和 //schematic save

*   从剪贴板加载 schematic：//schematic load <文件名> [< 格式 >]
*   存储 schematic 到剪贴板：//schematic save <文件名> [< 格式 >]

可以使用的格式有 mcedit 和 mce；如果没有给出 WorldEdit 会尝试确定格式。所有 build #1134-c76f119 (WorldEdit 5.3) 之前保存的. schematic 文件均为 mcedit 格式。文件名不需要包括. schematic 后缀。

你的副本的原点和你的相对位置都会被保存在文件中，这样你可以在之后加载它并以它原来的远点位置和你复制时的相对距离粘贴。关于 //copy 和 //paste 储存你的相对距离的方法，请参考下文。

#### //schematic delete

删除一个已保存的 schematic。

#### 文件保存位置

文件会被保存在你的 Minecraft 服务器的 **\plugins\WorldEdit\schematics** 文件夹下并从这里被加载。如果你使用的是 Single Player Commands，路径为 **\mods\spc\schematics**。WorldEdit 因为安全性原因将导入导出路径限制在这个文件夹。文件名会自动被添加_.schematic_扩展名。路径系统也是可以支持的，并且在需要的情况下可以创建新的子文件夹。目前不可以改变这个使用的文件夹位置。

两个命令都会检查 schematic 文件的路径来确认名字的有效性。路径只能含有字母和数字字符以及一些符号。检查使用的正则表达式为 ^[A-Za-z0-9_\ \./\\'\$@~!%\^\*\(\)\[\]\+\{\},\?]+$。如果路径长度大于系统支持的上限，Java 会报错并且用户会收到通知。

> 注意：每个用户没有自己的个人文件夹。

### 复制与剪切（//copy、//cut）

*   //copy [-be] [-m <mask>]
*   //cut [-be] [填充方块样式] [-m <mask>]
*   -b 同时复制生物群系
*   -e 同时复制实体

这个简单的命令可以复制你的选区内容到你的会话的剪贴板，**同时记录你与被复制物体的相对位置。**这句话的第二部分十分重要：举个例子，如果你之后要在你脚下粘贴一座桥，复制时你需要站在桥上的一个位置。这个方法允许你方便地对齐你的粘贴因为你可以提前计划；你需要一定的空间感来了解复制的过程，但是一旦学会你会觉得这个方法非常好用。

//cut 和 //copy 指令的效果十分相似，但是 //cut 会删除选区的内容。默认情况下它会留下空气方块，但你也可以指定一个其他方块（方块样式）。

### 粘贴（//paste）

*   //paste [-abenos] [-m <sourceMask>]
*   -a 忽略空气方块
*   -o 粘贴在原始位置
*   -s 在粘贴后，选区选中粘贴后的位置
*   -n 不粘贴，只选中粘贴后的位置
*   -e 同时粘贴实体
*   -b 同时粘贴生物群系

在你的剪贴板有东西了之后，你可以将它粘贴到地图上。参数都是选择性的：如果你想把它粘贴到它被复制时相同的位置，输入`//paste -o`，不然被粘贴的物体会被放置在与你相对的位置。**记住如果你在相对性粘贴，被粘贴的物体与你的相对位置和复制时的相同。**举例来说，如果你复制时站在你的城堡顶上，粘贴时城堡就会出现在你的下面。

[![](https://mineplugin.org/images/4/48/WorldEdit_paste.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_paste.png)

比如你需要复制一堵墙并且要把它放到别处。如果你现在几格之外，复制，然后尝试粘贴它，因为 Minecraft 储存位置的方法，有可能你会在一个方向上差一格（可能不会包括上下）。以下这个方法可以帮助你在正确的位置完成复制与粘贴：标出要复制的墙壁。在距离你的墙壁中心 3 格远的地方任何一个方块。对着那个方块，走得越近越好。复制。在粘贴之前在你需要被粘贴物体中心的位置 3 和距离的地方放下一个方块。对着方块走得越近越好。粘贴。注意你面向的方向不重要。如果你想你的墙朝另一个方向，旋转它，然后做同样的放置方块，走向方块并粘贴的操作。

### 旋转（//rotate）

*   //rotate <y 角度> [x 角度] [z 角度]

旋转剪贴板内容。

Non-destructively rotate the contents of the clipboard. Angles are provided in degrees and a positive angle will result in a clockwise rotation. Multiple rotations can be stacked. Interpolation is not performed so angles should be a multiple of 90 degrees.

有时你需要旋转你的副本。目前这个命令允许你沿 Y 轴（上下）旋转 90 度或 90 度的倍数。确切地说，这个命令其实可以以你复制时与物体相对的点作为中心来旋转你的副本。如果你想沿中心点旋转你的副本，复制时就需要站在它的中心点上。

[![](https://mineplugin.org/images/6/6d/WorldEdit_rotate.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_rotate.png)|

### 翻转（//flip）

*   //flip [方向]

按一个给出的方向翻转剪贴板。可用方向有 north、south、east、west、up 和 down；东南西北方向可以以朝向这些方向的模式选择，上下方向则不行。剪贴板会延一个与给出的方向垂直，位于剪贴板中间位置的平面翻转（非玩家位置）。一共有三个平面，一个水平的 (xz) 和两个竖直的(xy, yz)。水平平面 xz 以上下向量定义，xz 平面以东 / 西定义，yz 以南 / 北定义。

[![](https://mineplugin.org/images/b/b2/WorldEdit_flip2.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_flip2.png)|

### 清空剪贴板（/clearclipboard）

*   /clearclipboard

清空你的剪贴板会删除它的内容，释放少量的内存。

生成命令
----

有时你可能需要自动生成森林或者球体，因为手动做这些太乏味了。WorldEdit 有一系列可以完成这些操作的工具。这些指令不需要一个选区；他们使用你所站的位置的方块。

### 圆柱体（//cyl）与空心圆柱（//hcyl）

*   //cyl <方块样式> < 半径 > [高度] [-h]
*   //hcyl <方块样式> < 半径 > [高度]
*   -h 生成空心圆柱

WorldEdit 可以既可以生成空心圆柱，也可以生成实心的，同样也可以生成空心和实心的圆形。生成物体时使用的是一个快速的算法，并且这个算法会创建美观和对称的边缘。

圆柱体会在你的脚下被创建并会向上扩展。如果你需要一个圆形，创建一个高度 1 的圆柱即可。

例子：创建一个半径 5 高度 10 的实心玻璃圆柱体

`//cyl glass 5 10`

例子：创建一个半径为 5 的空心玻璃圆形

`//hcyl glass 5 1`

### 椭圆形圆柱体和椭圆形

*   //cyl <方块> < 东西半径 >_,_<南北半径> [高度] [-h]
*   //hcyl <方块> < 东西半径 >_,_<南北半径> [高度]

用指定两个半径，并用逗号隔开的方式，可以生成椭圆形圆柱体。

第一个半径是东西方向，第二个是南北方向。

### 球体和椭球体（//sphere）

*   //sphere [-hr] < 方块样式 > < 半径 >
*   //hsphere [-r] < 方块样式 > < 半径 >
*   -r 将球升高到你的脚下
*   -h 创建空心球体

实心和空心球体都可以创建。默认情况下，球体的中心会是你所站位置的上方一格。但是如果你设置了 - r 参数，球体会被升高，它的底部会在你的脚下。

例子：生成一个半径为 4 的玻璃球体

//sphere glass 4

例子：生成一个升高的半径为 4 的玻璃球体

//sphere glass 4 -r

### 金字塔（//pyramid 和 //hpyramid）

*   //pyramid <方块样式> < 大小 > [-h]
*   //hpyramid <方块样式> < 大小 >
*   -h 生成空心金字塔

按给出的方块样式和大小生成一个空心或者实心的金字塔。

例子：生成一个高度 5，边长 10 的空心玻璃金字塔

//hpyramid glass 5

### 森林（/forest 和 //forest）

*   /forestgen [范围] [种类] [密度]
*   //forest [种类] [密度]

使用这个命令可以生成森林。范围参数表示生成森林的正方形范围的宽度和高度。密度可以是从 0 至 100 的数字，允许使用小数。需要注意的是 100% 的密度（每个位置都有树）是不能达到的因为 Notch 的树木算法不能允许这样的生成，默认的 5% 已经可以生成一个很茂密的森林。最后，这个指令会按照给出的范围参数在你周围寻找可以生成的位置，并且搜索范围会向下扩展一两格以找到草方块或泥土方块（树木只会在这两个方块上生成），但是不会向上搜索。所以如果你想填满一片区域，最好站在一个稍高的平台上进行生成。查阅树木种类的部分来了解可以使用的树木种类。

//forest 指令用于在选区内生成森林。

> 注意：如果你使用的是单人模式版本，这些树木不能撤销。

例子：在 10x10 范围内生成森林

/forestgen 10

例子：在 10x10 范围生成 0.5% 密度的森林

/forestgen 10 tree 0.5

[![](https://mineplugin.org/images/d/d6/WorldEdit_Forestgen.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Forestgen.png)

### 南瓜丛（/pumpkins）

*   /pumpkins [范围]

WorldEdit 可以生成带有叶子的南瓜丛（Notch 的南瓜丛没有叶子）。范围参数是生成南瓜丛的方形区域的宽度和高度，从当前位置放射。目前不能调节南瓜丛的密度。

例子：在 5x5 范围生成南瓜丛

`/pumpkins 5`

### 任意表达式图像生成（//g、//gen、//generate）

*   //g[en[erate] [-chor] < 方块样式 > < 表达式…>
*   -r 使用游戏的原始坐标
*   -o 使用原点 (0,0,0) 位置设定为玩家位置或选区第一选择点的原始坐标，依设置而定
*   如果不使用标签，坐标会被正常化至 - 1..1
*   使用 - h 标签会生成空心形状。只有与不属于形状的方块相邻的方块会被放置。
*   -c 会将选区的空间作为原点

`v.5.0以上`生成任何可以用数学公式表达的形状：

*   环面
*   旋转过的圆柱体
*   锯齿状峡谷
*   任何你能想到并且用表达式表示的形状

变量：

*   x, y, z (输入) - 坐标
*   type, data (输入 / 输出) - 使用的材料，默认为输入的方块 / 图案

返回值：

*   true (>0) - 这个方块属于形状范围
*   false (<=0) - 这个方块不属于形状范围

表达式解析器的逻辑和比较的运算都会返回 0（假）或 1（真），所以可以给出一个只返回真值的方程。

例子：生成一个外半径 0.75，内半径 0.25 的环面

//g stone (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2

例子：粗糙的空心树

//g -h oak_log (0.5+sin(atan2(x,z)*8)*0.2)*(sqrt(x*x+z*z)/0.5)^(-2)-1.2 < y

例子：彩虹环面

//g white_wool data=(32+15/2/pi*atan2(x,y))%16; (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2

例子：彩虹蛋

//g white_wool data=(32+y*16+1)%16; y^2/9+x^2/6*(1/(1-0.4*y))+z^2/6*(1/(1-0.4*y))<0.08

例子：心形

//g red_wool (z/2)^2+x^2+(5*y/4-sqrt(abs(x)))^2<0.6

例子：正弦波

//g -h glass sin(x*5)/2<y

例子：环形余弦波

//g -h glass cos(sqrt(x^2+z^2)*5)/2<y

例子：圆形双曲面

//g stone -(z^2/12)+(y^2/4)-(x^2/12)>-0.03

这个命令使用表达式解析器。

效用性命令
-----

WorldEdit 提供了许多效用性工具，尤其是需要进行地形制作的时候会非常有用。

所有这些指令都会使用你的当前位置。你可以使用 [`/toggleplace`](#.2Ftoggleplace)命令把它切换成你的第一个选择点。

### 填充凹洞（//fill）

[![](https://mineplugin.org/images/b/b2/WorldEdit_filled.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_filled.png)

使用 //fill 填充的池塘

将空气替换成水方块（使用 / replace）的方法在这里不会好用，因为这个区域不能合适地被一个长方体包括在内。

*   //fill <_方块样式_> <_半径_> [_深度_]

你可以使用这个命令来填充地上的凹陷，瞬间完成水和岩浆池的制作，而不是手动放置大量的水源方块。只要站在需要填充的洞里并输入需要填充的范围半径，以及在需要的情况下一个深度即可（默认深度为 1）。这个指令的工作方式是在所有太阳会照到的位置放置方块，假设太阳在头顶位置：它只能填充不被盖住的凹陷的位置。所以使用这个指令不能填充洞穴因为洞穴会延伸至地下。

如果你很想知道，接下来有一个使用的算法的介绍。算法是这样的：

1.  A: 如果方块是空气方块
    1.  将方块设定为指定方块
    2.  将目标方块下方 深度 - 1 范围的所有方块填充为指定方块
    3.  对四周相邻的每个方块：
        1.  对每个给出范围内的方块重复 A

一般_//fill_会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。如果你使用法杖来选择，注意它可能会选择一个方块，这样指令不会有任何效果（见上方算法）

本命令支持[方块样式](#.E6.96.B9.E5.9D.97.E6.A0.B7.E5.BC.8F)。

#### 递归填充（//fillr）

*   //fillr <_方块样式_> <_半径_>

像之前提到的，填充命令不会填充不暴露在一个虚拟的太阳下的位置。如果你需要填充一个洞穴，或者是边上有更小的洞的洞，这就是一个问题。_//fillr_是不同的；它会填充所有和原始方块相接的方块，用这样的方式可以填充洞穴等。但无论如何，这个指令的范围不会延伸到你所站位置（或第一选择点）的高度以上，所以使用指令时还是要必须处于洞穴的顶部，一格向下的位置。

本指令支持[方块样式](#.E6.96.B9.E5.9D.97.E6.A0.B7.E5.BC.8F)。

### 抽空池塘（//drain）

*   //drain [-w] <_半径_>
*   -w：使含水方块不再含水

如果你曾经尝试过手动清除水或熔岩，你一定知道这么做有多么棘手。WorldEdit 可以为你清除一个池塘内的所有水或熔岩并且不会 “跳跃” 至不相连的另一个池塘。虽然你可以用 //replace 指令来完成同样的操作，但是池塘必须要被一个长方体完全包括才行。目前不支持 MOD 中加入的液体。

你必须要站在池塘的边缘与液体相同高度的位置或在液体内部进行操作。你不能站在比池塘高或者更远一格的位置。

算法很简单：

1.  对每个起始位置 1 格范围内的方块：
    1.  A: 如果是水方块或者岩浆方块：
        1.  移除方块。
        2.  对于每个相邻的方块，包括对角相邻与上下，如果这些方块不在半径范围之外，重复 A。

一般 //fill 会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

**注意：**有些方块，比如海带、海草，虽然看上去含水，但并无干燥状态。如果你尝试抽干含有这些方块的海洋或者河流，使用 //removenear 来移除这些方块。

### 修复池塘（/fixwater、/fixlava、//fixwater、//fixlava）

*   /fixwater <_半径_>
*   //fixwater <_半径_>
*   /fixlava <_半径_>
*   //fixlava <_半径_>

手动完成一个一格深平静的水池或熔岩池表面是很有挑战性的，对于更深的池塘几乎是不可能的，但这两个指令是专门来解决这个问题的。这两个指令会寻找附近的水或熔岩方块并把它们展开来填满整个区域并且将流动的水或熔岩替换成他们的静止型方块。你只需站在水或熔岩边上（不是一格上方）使用指令即可。注意如果你尝试在一个瀑布上方使用这个指令，水会被展开成一个巨大的液体伞形，因为这两个指令会同时扩大水或熔岩的范围！如果你在液体表面以下几格使用这些指令，只有你所在的高度的液体会被修复而不包括你上方的。

目前不支持 MOD 中加入的液体。

[![](https://mineplugin.org/images/b/ba/WorldEdit_fixed_water.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_fixed_water.jpg)

被使用 / fixwater 的池塘

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

### 修改附近方块

WorldEdit 也提供了许多可以修改周围方块的指令。

#### 移除上方和下方的方块（/removeabove、/removebelow、//removeabove、//removebelow）

*   /removeabove [_范围_] [_高度_]
*   /removebelow [_范围_] [_深度_]
*   //removeabove [_范围_] [_高度_]
*   //removebelow [_范围_] [_深度_]

这 4 个指令可以简单地移除你上方或下方的方块。比如一个使用的例子是清除玩家们为到达高处建造的方块塔。范围参数决定要移除的长方体的体积。长方体的长度和宽度为 (范围 - 1)*2+1。长方体的中心为你所站位置上方一格的位置。如果你不指定高度或深度，这两个命令的范围会扩展到地图上下边界。

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

#### 移除附近方块（/removenear、//removenear）

*   /removenear <_蒙版_> [_范围_]
*   //removenear <_蒙版_> [_范围_]

这个指令会清除附近指定种类的方块。范围参数决定了要移除的长方体的大小。长方体的长度和宽度为 (范围 - 1)*2+1。长方体的中心为你所站位置上方一格的位置。如果你不指定高度或深度，这两个命令的范围会扩展到地图上下边界。

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

#### 替换附近方块（/replacenear、//replacenear）

*   /replacenear <_范围_> [_需要替换方块_] <_替换使用方块_>
*   //replacenear <_范围_> [_需要替换方块_] <_替换使用方块_>

如果你需要替换附近的方块，这个指令是一个快捷方式。范围参数决定了要移除的长方体的大小。长方体的长度和宽度为 (范围 - 1)*2+1。长方体的中心为你所站位置上方一格的位置。

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

### 模拟降雪（/snow、//snow）

*   /snow [半径]
*   //snow [半径]

把一个区域用雪覆盖！这个指令的算法只会在需要被雪盖住的方块上生成降雪（比如火炬方块不会被盖住）。如果某个区域上方有物体（比如悬垂），降雪不会覆盖它。“降雪” 是完全竖直的。

[![](https://mineplugin.org/images/9/9c/WorldEdit_snow.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_snow.jpg)

被降雪的区域

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

**注意：**该命令不能增加雪的层数。

### 解冻区域（/thaw、//thaw）

*   /thaw [_半径_]
*   //thaw [_半径_]

如果你需要解冻一个区域（或许反转 [snow](#.2Fsnow) 的效果），这个指令有与降雪完全相反的效果。对所有被太阳直射的方块，如果是一个被雪覆盖的方块，雪会被移除，如果是冰，会被转换成水。

### 模拟草地生长（/green、//green）

*   /green [_半径_] [-f]
*   //green [_半径_] [-f]
*   -f 同时转换其他泥土

把一个区域用草地覆盖！这个指令的算法只会在需要被草地盖住的方块上生成草地（比如火炬方块不会被盖住）。如果某个区域上方有物体（比如悬垂），/green 不会覆盖它。/green 是完全竖直的。

一般这两个指令会使用你的所在位置（所站位置一格上方）来开始运作，你可以使用 [/toggleplace](#.2Ftoggleplace) 将它切换为你的第一选择点。

### 扑灭火焰（/extinguish、/ext、/ex、//extinguish、//ext、//ex）

说明：/extinguish、/ex、/ext、//ex、//ext、//extinguish 都是等价的。

*   /ex [_半径_]
*   //ex [_半径_]

这个指令相当于 `[/removenear](#.2Fremovenear) ##fire [_半径_]`的快捷方式，这个指令会移除在一定范围内的火焰方块（包括灵魂火焰）。默认这个指令会使用 40 作为半径。

虽然这个指令会移除火焰，但不会移除火源，比如熔岩池。

### 移除生物（/butcher）

*   /butcher [-pngabtfl] [_半径_]

这个指令会移除附近的怪物。如果你不指定一个半径，所有被加载的地图中活跃的怪物都会被移除。怪物_不会_掉落它们的掉落物。注意就算你杀死了所有怪物，它们也会很快重新生成。

标示:

*   -p 会同时移除宠物
*   -n 会同时移除 NPC
*   -g 会同时移除铁傀儡
*   -a 会同时移除动物
*   -b 会同时移除环境生物
*   -t 会同时移除使用自定义名称的生物
*   -f 包括所有之前的标示
*   -l 会在被移除的怪物位置生成闪电（WorldEdit 5 以上）

提示：有些生物同时属于多个种类，所以你可能需要同时使用多个标示来移除它们。

可以通过修改配置文件来设定一个这个指令使用的默认半径。

`v.6.0以上`你可以使用 `[//undo](#.2F.2Fundo)`来撤销生物的移除。

### /remove、/rem、/rement

*   /remove <要移除的实体> < 半径 >

移除一种类型的所有实体。

### //calculate、//calc、//eval、//evaluate、//solve

*   //calc <表达式>

计算一个数学表达式。

### //help

*   //help [-s] [-p < 页面 >] [命令...]
*   -s 显示给定命令的子命令
*   -p <页面> 显示指定的页码

区块命令
----

如果你需要操作区块，WorldEdit 也能帮到你。

### 区块信息（/chunkinfo）

*   /chunkinfo

如果你需要你所在的区块的信息，使用这个指令。

例子：/chunkinfo 输出示例

```
Chunk: 8, -17
```

8/1b/c.8-h.dat

### 列出区块（/listchunks）

*   /listchunks

你可以使 WorldEdit 列出你的选区覆盖的区块。不幸的是，这个指令只会在聊天框输出所以只有有限的用处。

### 删除区块（/delchunks）

*   /delchunks

WorldEdit 会生成一个可以删除选区覆盖的区块的脚本。WorldEdit **不会**实际删除区块。你需要手动运行脚本来真正的删除区块。在使用这个指令之前，你需要设置脚本保存格式。这个文件会被保存到服务器的根目录（或者说是你的有效路径），文件名为 **worldedit-delchunks.ext**。

![](https://mineplugin.org/images/thumb/5/57/Icon-info.png/50px-Icon-info.png)

注意：不要在服务器运行时使用生成的脚本。


重要提示：这里的提示中提到的 1.3 指的是 BETA 1.3, 在此版本中文件格式从按区块保存变为了按区域保存，并不指正式版 1.3 中的修改（如果有的话）。如果这个是真的，这些指令在 1.2.5 版本也不可使用，也不能用来删除不需要的区块。

快照命令
----

脚本命令
----

脚本命令包括 / cs 和 /.s。

### /cs

执行一个 CraftScript 脚本。

*   /cs <文件名称> [参数...]

### /.s

执行上一个 CraftScript。

*   /.s [参数...]

超级镐子命令（/superpickaxe、/pickaxe、/sp）
----------------------------------

WorldEdit 中的超级镐子功能能让所有的镐子拥有超能力！

超级镐子的功能会给予你的镐子快速破坏方块的能力。使用`//`指令可以切换你的超级镐子功能。默认情况下选择的模式是单方块模式。

如果你使用下面的命令来切换，超级镐子的功能就会被开启。注意：/superpickaxe、/pickaxe、/sp 是等价的，后两者是简称。为方便起见，本段统一使用 / sp。

![](https://mineplugin.org/images/thumb/5/57/Icon-info.png/50px-Icon-info.png)

注意：在服务器上，只有拥有 **worldedit.override.bedrock** 权限的玩家才可以用这些工具破坏基岩。

### 瞬间采集（/sp single）

*   /sp single

单个方块模式只会破坏一个方块。默认使用这个模式时被采集的方块会掉落，这个特性可以通过修改配置中的_super-pickaxe.drop-items_项目来改变。

### 瞬间破坏区域（/sp area、/sp recursive、/sp recur）

*   /sp area <_半径_>
*   /sp recur 或 recursive <_半径_>

这两个模式会破坏一整个区域，但是只会破坏与你击中的方块相同种类的方块。两个模式的区别是 recur 或 recursive 模式只会破坏与原始方块相接的方块，在半径范围内重复。而 area 模式只会破坏一个以击中的方块为中心长度和宽度为 (半径 * 2+1) 的长方体区域。

默认情况下，使用这些模式**不会**使被采集的方块掉落，但是这个特性可以通过修改配置中的_super-pickaxe.many-drop-items_项目来改变。

![](https://mineplugin.org/images/thumb/5/57/Icon-info.png/50px-Icon-info.png)

注意：在这些模式启用方块掉落会使过量的物品掉落造成严重的延迟。

生物群系命令
------

### /biomelist

*   /biomelist [-p < 页面>]

列举所有的生物群系。

### /biomeinfo

*   /biomeinfo [-pt]
*   -t 使用你正在看着的方块
*   -p 使用你当前所在的方块

获取目标方块的生物群系信息。默认情况下，使用选区内的所有方块。

### //setbiome

*   //setbiome [-p] < 目标 >
*   -p 使用你当前所处的坐标。

修改选区内的生物群系。默认情况下，使用选区内的所有方块。

工具（/tool）
---------

工具是可以 “绑定” 至一个物品来右键点击使用的效用性功能。手持需要绑定的物品并使用下面的一个指令就可以绑定一个工具。

### 树木生成工具（/tool tree）

*   /tool tree [_种类_]

启动树木生成工具。右键点击草地来生成一棵树。如果需要树木种类的列表，请查看_’树木种类_’部分。

[![](https://mineplugin.org/images/d/d6/WorldEdit_Forestgen.png)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_Forestgen.png)

一些大树的例子

### 浮空树木清除工具（/tool deltree）

*   /tool deltree

启动浮空树木清除工具。右键点击与浮空树木连接的树干或树叶来清除整个浮空树木。树木不能连接到地面。这个工具对浮空蘑菇也有效`v.4.7以上`。

### 方块替换工具（/tool repl）

*   /tool repl <_方块_>

使用这个工具可以用右键点击的方式将方块替换为需要的方块。使用 air 来使用这个工具来_清除_方块。

### 远程建筑工具（/tool lrbuild）

*   /tool lrbuild <_左键放置方块_> <_右键放置方块_>

使用这个工具可以在一段距离外放置和破坏方块。瞄准点击即可。方块放置的模式与右键点击目标方块的效果相通。如果其中一个方块被设定成空气，这个工具可以用来删除目标方块。`v.4.7以上`

### 远距离魔杖（/tool farwand）

*   /tool farwand

这个工具是上一个工具与选区选择魔杖的组合。它和选择魔杖的工作方式相同，但是有从远处选择方块的能力。`v.4.7以上`

### 循环工具（/tool cycler）

*   /tool cycler

被这个工具右键点击的方块会在它们所有的附加值状态中循环 (如果支持)。比如使用这个工具右键羊毛会使它在所有的颜色中循环。左键和右键可以分别用来“向前” 和“向后”循环。

### 查询工具（/tool info）

*   /tool info

使用这个工具右键点击方块时，玩家会收到关于这个方块的信息。显示的信息的格式是 “@(x, y, z) #id (名称) [附加值] (发光亮度等级 / 上方亮度等级)”。

### 颜料桶填充（/tool floodfill 或 /tool flood）

*   /tool floodfill <_图案_> <_范围_>
*   /tool flood <_图案_> <_范围_>

从右键点击的位置开始，填充工具会填充范围内所有相邻的方块（最大范围为超级镐子的最大范围）并将原始的方块种类设定为给出的图案。`v.4.7以上`

### 解除工具绑定（/tool none 或 /tool unbind）

*   /tool unbind
*   /tool none

刷子命令（/brush、/br、//brush、//br）
-----------------------------

WorldEdit 有一些刷子工具，可以让你从远处建筑和绘制。开启一个刷子的时候，它的功能会绑定到当前手持的物品上。你可以在不同的物品上绑定不同的工具。

/bursh、/br、//brush、//br 是等价的，本段统一使用 / br。

### 森林刷子（/br forest）

*   /br forest <形状> [半径] [密度] < 种类 >

### 圆柱体刷子（/br cylinder、/br cyl、/br c）

*   /br cylinder [-h] <_方块_> [_半径_] [_高度_]

### /br set

*   /br set <形状> [半径] < 样式 >

### /br apply

*   /br apply <形状> [半径] <forest|item|set>

### /br deform

*   /br deform [-or] < 形状 > [半径] < 表达式 >
*   -r 使用游戏的坐标原点
*   -o 使用放置的位置作为坐标原点

### /br lower

*   /br lower <形状> [半径]

### /br butcher 或 /br kill

*   /br butcher [-abfgnprt] [radius]
*   -p 同时杀死宠物
*   -n 同时杀死 NPC
*   -g 同时杀死傀儡
*   -a 同时杀死动物
*   -b 同时杀死环境实体
*   -t 同时杀死带有命名标签的生物
*   -f 同时杀死所有友好实体（相当于 - abgnpt）
*   -r 同时破坏盔甲架

### /br paint

*   /br paint <形状> [半径] [密度] <forest|item|set>

### /br none 或 /br unbind

*   /br unbind

解绑刷子。

### 剪贴板刷子（/br clipboard 或 /br copy）

*   /br clipboard [-abeo] [-m <sourceMask>]
*   -a 不从剪贴板粘贴空气
*   -o 从目标位置粘贴，而不是以它为中心
*   -e 如果可以，粘贴实体
*   -b 如果可以，粘贴生物群系
*   -m <sourceMask> 跳过剪贴板内符合蒙版的方块

选择你的剪贴板内容作为刷子。剪贴板的中心会被粘贴在你点击的方块位置。使用 - a 标示可以不粘贴空气。改变你的剪贴板内容不会改变你使用的剪贴板刷子，如果你需要更新你的刷子内容，你需要重新使用指令。

[![](https://mineplugin.org/images/1/1a/WorldEdit_clipboard_brush.jpg)](https://mineplugin.org/%E6%96%87%E4%BB%B6:WorldEdit_clipboard_brush.jpg)

使用剪贴板作为刷子内容

### /br gravity 或 /br grav

*   /br gravity [-h] [半径]
*   -h 影响从最大 Y 轴开始的方块，而不是目标 Y + 半径

重力刷子，刺激重力效果。

### /br ex 或 /br extinguish

*   /br ex [半径]

扑灭火焰。参见 [//ex](#.2F.2Fex)。

### 球体刷子（/br s 或 /br sphere）

*   /br s [-h] <_方块样式_> [_半径_]
*   -h 创建空心球体。

这里的 br 和 s 分别是 brush 和 sphere 的缩写。

### /br raise

*   /br raise <形状> [半径]

### 平滑刷子（/brush smooth）

*   /br smooth [_大小_] [_迭代次数_] [蒙版]

使用平滑刷子。这个刷子实际上使用两倍指定的大小作为平滑的范围。

### 刷子设定

#### 蒙版

*   /mask [_蒙版_]
*   /mask (关闭蒙版)

为你的刷子指令设定蒙版，使你可以限制被影响的方块种类。（更详细的资料请查看_’蒙版_’部分）

#### 尺寸

*   /size [_尺寸_]

设定刷子的尺寸（默认最大值为 6）。

传送命令
----

你可能会经常需要到达一些位置来更好地进行操作。下面的命令可以满足这些需求。

### 解放自己（/unstuck 或 /!）

*   /unstuck

这个指令可以在你被封在方块里时将你解救出来。它会将你移动到最高的空位，如果你没有被堵住的话这个命令就没有任何效果。（这是唯一与_/ascend_命令有区别的地方。）

### 上升（/ascend）与下降（/descend）

*   /ascend [_层数_]
*   /asc [_层数_]
*   /descend [_层数_]
*   /desc [_层数_]

这些指令可以使你穿过上方的顶或下方的地面。举个例子，如果你在一个房子里，使用 / ascend 会将你传送到房顶上。 你也可以指定一个上升或下降的层数。举个例子，如果你在一个摩天大楼的底层，使用 / ascend 2 会将你传送到第三层。

### 上升到屋顶（/ceil）

*   /ceil [-fg] [clearance]
*   -f 强制使用飞行以保持静止
*   -g 强制使用玻璃以保持静止

这个指令会把你带到你所在房间的屋顶位置。如果你没有使用了 clearance 参数，你会被传送到屋顶下方。如果你使用了 clearance 参数，你头顶的空间会更大一些。你传送时脚下会被放置一个支撑用的玻璃方块。你必须手动移除这个方块。

### 穿过墙壁（/thru）

*   /thru

这个指令会使你朝你看向的方向穿过一堵墙。看向墙并使用指令即可。注意不要朝下看因为它会尝试穿过地面。这个指令会合理地限制墙的厚度。

### 跳跃至视野内目标方块（/jumpto 或 /j）

*   /jumpto
*   /j

这个指令会将你传送至你所指向的方块上方。如果那个方块是一堵墙，你会被传送到顶部的边缘位置。

你可以将这个功能绑定到一个物品上来更方便地使用它。查看**配置**部分来了解详细信息。

### 上升任意距离（/up）

*   /up [-fg] <_距离_>
*   -f 强制使用飞行以保持静止
*   -g 强制使用玻璃以保持静止

这个指令会将你向上移动几个方块。你不能用这个指令来穿过墙壁，并且你脚下会被放置一个玻璃方块来支撑你。在你完成操作之后需要手动移除这个玻璃方块。

