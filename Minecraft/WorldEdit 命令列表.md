---
title: WorldEdit 教程&命令列表
date: 2022/10/14
categories:
  - Minecraft
abbrlink: 4ed2dd42
tags:
---

# 命令列表

| 命令               | 参数                                              | 支持性（1、单人 2、bukkit） | 描述                                                         |
| ------------------ | ------------------------------------------------- | --------------------------- | ------------------------------------------------------------ |
| //limit            | &lt;限制值&gt;                                    | 1/2                         | 设置最大操作方块数量，只对你生效。这是为了防止操作失误引起的灾难性事故，它不会将配置参数覆盖。 |
| 历史               |                                                   |                             |                                                              |
| //undo             | [步骤值]                                          | 1/2                         | 撤销上一次操作                                               |
| //redo             | [步骤值]                                          | 1/2                         | 还原操作，仅还原上一次操作，不能重复上一次命令               |
| /clearhistory      |                                                   | 1/2                         | 清理所有历史记录                                             |
| 选择               |                                                   |                             |                                                              |
| //wand             |                                                   | 1/2                         | 给你一个设置选区工具（默认为木斧）。单击左键设置点 1；右键设置点 2。 |
| /toggleeditwand    |                                                   | 1/2                         | 设置编辑选区工具的模式，可以让工具恢复正常。                 |
| //sel              | &lt;cuboid                                        | poly&gt;                    | 1/2                                                          |
| //pos1             |                                                   | 1/2                         | 将玩家脚下的方块设置为点 1                                   |
| //pos2             |                                                   | 1/2                         | 将玩家脚下的方块设置为点 2                                   |
| //hpos1            |                                                   | 1/2                         | 将玩家指向的方块设置为点 1                                   |
| //hpos2            |                                                   | 1/2                         | 将玩家指向的方块设置为点 2                                   |
| //chunk            |                                                   | 1/2                         | 将选区修改为你附近的 16*16*Max 大小的区域（PS：MAX 指 Z 轴最大化） |
| //expand           | &lt;amount&gt;                                    | 1/2                         | 根据玩家朝向扩大选区                                         |
| //expand           | &lt;amount&gt; &lt;direction&gt;                  | 1/2                         | 根据参数设定方向扩大（north, east, south, west, up, down）   |
| //expand           | &lt;amount&gt; &lt;reverse-amount&gt; [direction] | 1/2                         | 将选区朝两个方向同时扩大                                     |
| //expand           | vert                                              | 1/2                         | 扩大选区（包含地壳）                                         |
| //contract         | &lt;amount&gt;                                    | 1/2                         | 根据玩家朝向缩小选区                                         |
| //contract         | &lt;amount&gt; [direction]                        | 1/2                         | 根据参数设定方向缩小选区（north, east, south, west）         |
| //contract         | &lt;amount&gt; &lt;reverse-amount&gt; [direction] | 1/2                         | 将选区朝两个方向同时缩小                                     |
| //outset           | [-hv] &lt;amount&gt;                              | 1/2                         | 按照参数整体放大选区                                         |
| //inset            | [-hv] &lt;amount&gt;                              | 1/2                         | 按照参数整体缩小选区                                         |
| //shift            | &lt;amount&gt; [direction]                        | 1/2                         | 移动选区，但不移动选区内的方块                               |
| //size             |                                                   | 1/2                         | 获得选区内的方块数量                                         |
| //count            | &lt;block&gt;                                     | 1/2                         | 获取选区内某一种方块的数量                                   |
| //distr            | [-c]                                              | 1/2                         | 获取选区内方块的分布情况                                     |
| 选区操作           |                                                   |                             |                                                              |
| //set              | &lt;block&gt;                                     | 1/2                         | 修改区域内所有方块                                           |
| //replace          | &lt;to-block&gt;                                  | 1/2                         | 替换选区内所有方块（不包含空气）                             |
| //replace          | &lt;from-block&gt; &lt;to-block&gt;               | 1/2                         | 将选区内的某一种方块替换为另外一种方块                       |
| //overlay          | &lt;block&gt;                                     | 1/2                         | 在选区内的方块上放置方块                                     |
| //walls            | &lt;block&gt;                                     | 1/2                         | 填充选区边界（仅包含 Z 轴）                                  |
| //outline          | &lt;block&gt;                                     | 1/2                         | 填充选区边界（常规的建筑体，内部空心）                       |
| //smooth           | [iterations]                                      | 1/2                         | 向下压缩选区                                                 |
| //regen            |                                                   | 1                           | 重置选区                                                     |
| //move             | [count] [direction] [leave-id]                    | 1/2                         | 移动选区                                                     |
| //stack            | [count] [direction]                               | 1/2                         | 叠加选择                                                     |
| 剪切板             |                                                   |                             |                                                              |
| //copy             |                                                   | 1/2                         | 复制选区                                                     |
| //cut              |                                                   | 1/2                         | 剪切选区                                                     |
| //paste            | [-ao]                                             | 1/2                         | 粘贴选区                                                     |
| //rotate           | &lt;angle-in-degrees&gt;                          | 1/2                         | 旋转剪切板内容                                               |
| //flip             | [dir]                                             | 1/2                         | 翻转剪切板内容                                               |
| //load             | &lt;filename&gt;                                  | 1/2                         | 读取一个剪切板文件内容                                       |
| //save             | &lt;filename&gt;                                  | 1/2                         | 将剪切板内容保存为文件（可以尝试选择一座建筑保存为单独的文件，然后使用时读取） |
| /clearclipboard    |                                                   | 1/2                         | 清楚剪切板                                                   |
| 快速创建           |                                                   |                             |                                                              |
| //hcyl             | &lt;block&gt; &lt;radius&gt; [height]             | 1/2                         | 创建一个垂直空心圆柱                                         |
| //cyl              | &lt;block&gt; &lt;radius&gt; [height]             | 1/2                         | 创建一个垂直圆柱                                             |
| //sphere           | &lt;block&gt; &lt;radius&gt; [raised?]            | 1/2                         | 创建一个球体                                                 |
| //hsphere          | &lt;block&gt; &lt;radius&gt; [raised?]            | 1/2                         | 创建一个空心球体                                             |
| /forestgen         | [size] [type] [density]                           | 1/2                         | 创建一片森林                                                 |
| /pumpkins          | [size]                                            | 1/2                         | 创建一片南瓜森林                                             |
| 公共               |                                                   |                             |                                                              |
| /toggleplace       |                                                   | 1/2                         | 设置两点（不太明白，求补充……）Toggle between using pos #1 or your current position. |
| //fill             | &lt;block&gt; &lt;radius&gt; [depth]              | 1/2                         | Fill a hole.                                                 |
| //fillr            | &lt;block&gt; &lt;radius&gt;                      | 1/2                         | Fill a hole fully recursively.                               |
| //drain            | &lt;radius&gt;                                    | 1/2                         | 删除周围的水和岩浆                                           |
| /fixwater          | &lt;radius&gt;                                    | 1/2                         | 修正玩家附近水池内的水流为水源                               |
| /fixlava           | &lt;radius&gt;                                    | 1/2                         | 修正玩家附近岩浆池内的流动岩浆为岩浆源                       |
| /removeabove       | [size] [height]                                   | 1/2                         | 删除玩家头顶的方块                                           |
| /removebelow       | [size] [height]                                   | 1/2                         | 删除玩家脚下的方块                                           |
| /replacenear       | &lt;size&gt; &lt;from-id&gt; &lt;to-id&gt;        | 1/2                         | 替换玩家周围的某种方块                                       |
| /removenear        | [block] [size]                                    | 1/2                         | 删除玩家周围的方块                                           |
| /snow              | [radius]                                          | 1/2                         | 在玩家周围创建积雪                                           |
| /thaw              | [radius]                                          | 1/2                         | 删除玩家周围的积雪                                           |
| /ex                | [size]                                            | 1/2                         | 扑灭玩家周围的火灾                                           |
| /butcher           | [radius]                                          | 1/2                         | 杀死玩家周围的怪物                                           |
| /remove            | &lt;type&gt; &lt;radius&gt;                       | 1                           | 删除玩家周围一切实体                                         |
| 块工具             |                                                   |                             |                                                              |
| /chunkinfo         |                                                   | 1/2                         | 获取玩家所处块的文件名                                       |
| /listchunks        |                                                   | 1/2                         | 显示所有块列表                                               |
| /delchunks         |                                                   | 1/2                         | 使用一个 shell 脚本删除块                                    |
| 超级工具           |                                                   |                             |                                                              |
| //                 |                                                   | 1/2                         | 设置超级工具                                                 |
| /sp single         |                                                   | 1/2                         | 切换到单块超级工具                                           |
| /sp area           | &lt;range&gt;                                     | 1/2                         | 切换到大面积超级工具                                         |
| /sp recur          | &lt;Range&gt;                                     | 1/2                         | 切换到超级递归工具                                           |
| 工具               |                                                   |                             |                                                              |
| /none              |                                                   | 1/2                         | 切换无工具                                                   |
| /info              |                                                   | 1/2                         | 显示工具信息                                                 |
| /tree              | [type]                                            | 1/2                         | 工具右键创建树或其他，[tree, regular, big, bigtree, redwood, sequoia, tallredwood, tallsequoia, birch, white, whitebark, pine, randredwood, randomredwood, anyredwood, rand, random] |
| /repl              | &lt;block&gt;                                     | 1/2                         | 工具右键替换为某个方块                                       |
| /cycler            |                                                   | 1/2                         | Block data cycler tool.                                      |
| 刷子               |                                                   |                             |                                                              |
| /brush sphere      | [-h] &lt;type&gt; &lt;radius&gt;                  | 1/2                         | 设定刷子形状为球体                                           |
| /brush cylinder    | [-h] &lt;type&gt; &lt;radius&gt; [height]         | 1/2                         | 设定刷子形状为圆柱                                           |
| /brush clipboard   |                                                   | 1/2                         | 设定刷子形状为剪贴板内容                                     |
| /brush smooth      | &lt;radius&gt; [iterations]                       | 1/2                         | 设定刷子形状为光滑的平面                                     |
| /size              | &lt;size&gt;                                      | 1/2                         | 设置笔刷大小                                                 |
| /mat               | &lt;mat&gt;                                       | 1/2                         | 改变当前刷子使用的材料                                       |
| /mask              |                                                   | 1/2                         | 清除遮罩                                                     |
| /mask              | &lt;mask&gt;                                      | 1/2                         | 设置一个遮罩                                                 |
| 传送               |                                                   |                             |                                                              |
| /unstuck           |                                                   | 1/2                         | 去一个空旷的地方                                             |
| /ascend            |                                                   | 1/2                         | 向上传送一层                                                 |
| /descend           |                                                   | 1/2                         | 向下传送一层                                                 |
| /ceil              | [clearance]                                       | 1/2                         | 传送到顶部                                                   |
| /thru              |                                                   | 1/2                         | 穿过障碍物                                                   |
| /jumpto            |                                                   | 1/2                         | 传送到指向的方块上                                           |
| /up                | [distance]                                        | 1/2                         | 向上传送                                                     |
| 花絮               |                                                   |                             |                                                              |
| //restore          | [snapshot]                                        | 1/2                         | 还原到指定的快照                                             |
| /snap use          | &lt;snapshot&gt;                                  | 1/2                         | 使用特定的快照                                               |
| /snap list         | [num]                                             | 1/2                         | 显示快照列表                                                 |
| /snap before       | &lt;date&gt;                                      | 1/2                         | 回到上一个快照                                               |
| /snap after        | &lt;date&gt;                                      | 1/2                         | 进入下一个快照                                               |
| 脚本               |                                                   |                             |                                                              |
| /cs                | &lt;script&gt; [args...]                          | 1/2                         | 执行一个脚本                                                 |
| /.s                | [args...]                                         | 1/2                         | 重新执行最后一个脚本                                         |
| /&lt;script&gt;.js | [args...]                                         | 1/2                         | 执行一个 JS 脚本                                             |
| 通用命令           |                                                   |                             |                                                              |
| /search            | &lt;item&gt;                                      | 1/2                         | 搜索物品名称                                                 |
| /worldedit reload  |                                                   | 1/2                         | 重置 WorldEdit 配置                                          |
| /worldedit version |                                                   | 1/2                         | 显示 WorldEdit 版本                                          |
| /worldedit tz      |                                                   | 1/2                         | 设置时区（暂时）                                             |