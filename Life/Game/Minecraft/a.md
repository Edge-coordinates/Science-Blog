---
title: a
date: 2022/10/14
categories:
  - Minecraft
abbrlink: e8b7be43
tags:
---




/give @p netherite_sword{display:{Name:'{"text":" 弑神 ","color":"gold"}'},Unbreakable:1,Enchantments:[{id:smite,lvl:2147483647},{id:sharpness,lvl:2147483647},{id:bane_of_arthropods,lvl:2147483647},{id:knockback,lvl:3},{id:fire_aspect,lvl:2147483647},{id:looting,lvl:10},{id:sweeping,lvl:2147483647},{id:unbreaking,lvl:2147483647},{id:mending,lvl:2147483647}]}

/give @p bow{display:{Name:'{"text":" 逐日 ","color":"gold"}'}, Unbreakable:1,Enchantments:[{id:unbreaking,lvl:2147483647},{id:power,lvl:2147483647},{id:punch,lvl:5},{id:mending,lvl: 2147483647},{id:flame,lvl:1},{id:infinity,lvl:1}]}

/give @p crossbow{display:{Name:'{"text":" 千机 ","color":"gold"}'}, Unbreakable:1,Enchantments:[{id:multishot,lvl:1},{id:piercing,lvl:2147483647},{id:quick_charge,lvl:5},{id:unbreaking,lvl:2147483647},{id:mending,lvl:2147483647}]}


/give @p trident{display:{Name:'{"text":" 戟 ","color":"gold"}'},Unbreakable:1,Enchantments:[{id:unbreaking,lvl: 2147483647},{id:loyalty,lvl:10},{id:impaling,lvl:2147483647},{id:channeling,lvl:1},{id:mending,lvl: 2147483647}]}

/give @p trident{display:{Name:'{"text":" 戟2","color":"gold"}'},Unbreakable:1,Enchantments:[{id:unbreaking,lvl: 2147483647},{id:impaling,lvl:2147483647},{id:riptide,lvl:10},{id:mending,lvl: 2147483647}]}

1.16 版本，属于剑的附魔有：

Bane of Arthropods -- 节肢杀手（对蜘蛛，蠹虫，末影螨，蜜蜂造成额外伤害）

Curse of Vanishing -- 消失诅咒（物品会在玩家死亡时消失）

Fire Aspect -- 火焰附加（使被攻击的目标着火）

Knockback-- 击退（增加剑的击退的距离）（电脑不好不要附魔太高等级）

Looting -- 抢夺（增加掉落物的掉落数量和几率）（电脑不好不要附魔太高等级）

Mending -- 经验修补（经验球会被用于修复物品耐久度）

Sharpness -- 锋利（增加近战攻击伤害）

Smite -- 亡灵杀手（对亡灵生物造成额外伤害）

Sweeping Edge -- 横扫之刃（增加剑的横扫伤害）

Unbreaking -- 耐久（减缓物品的损耗）

（正常情况下节肢杀手、亡灵杀手和锋利三个属性互斥）

（有一些附魔，我抽不出时间去测试他们的等级上限是不是 2147483647，但是那些会造成致命错误的附魔等级，会明显造成附魔效果失败的附魔等级，我一定会在教程中特别说明。）

如果在指令生成的时候，想自定义武器名称，自定义武器名称的颜色，甚至加入不可破坏的属性，那么修改模板如下，对比前面的模板，大家应该能看出要做什么修改：

**/give** **玩家** **物品名称** **{display:{Name:'{"text":"** **自定义的名称** **","color":"** **自定义的颜色** **"}'},Unbreakable:1,Enchantments:[{id:"** **附魔属性英文名称** **",lvl:** **等级数字****}]}** **物品数量**

（此处用于自定义名称，自定义名称颜色的模板，适用于绝大多数的 / give 指令生成物品，所以后续将不再阐述。）

下面举一个指令生成下界合金剑的实例：

/give @p netherite_sword{display:{Name:'{"text":" 弑神 ","color":"gold"}'},Unbreakable:1,Enchantments:[{id:smite,lvl:2147483647},{id:sharpness,lvl:2147483647},{id:bane_of_arthropods,lvl:2147483647},{id:knockback,lvl:3},{id:fire_aspect,lvl:2147483647},{id:looting,lvl:10},{id:sweeping,lvl:2147483647},{id:unbreaking,lvl:2147483647},{id:mending,lvl:2147483647}]}

命令方块执行一次这条指令，那么附近玩家将获得下面这把神器：

![](http://i0.hdslb.com/bfs/article/2f5f85beb35d17cff44beaa801a2d05f51d53143.png@942w_531h_progressive.webp)神剑![](http://i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png)

**弓**

1.16 版本，属于弓的附魔有：

Curse of Vanishing -- 消失诅咒（物品会在玩家死亡时消失）

Flame -- 火矢（让弓射出的箭着火）（有效的最高等级为 1 级）

Infinity -- 无限（只要有一根普通箭，就可以无消耗的射出普通箭）（有效的最高等级为 1 级）

Mending -- 经验修补（经验球会被用于修复物品耐久度）

Power -- 力量（增加弓射出的箭造成的伤害）

Punch -- 冲击（增加箭的击退距离）（电脑不好不要附魔太高等级）

Unbreaking -- 耐久（减缓物品的损耗）

（正常情况下无限和经验修补属性互斥）

下面举一个指令生成弓的实例：

/give @p bow{display:{Name:'{"text":" 逐日 ","color":"gold"}'}, Unbreakable:1,Enchantments:[{id:unbreaking,lvl:2147483647},{id:power,lvl:2147483647},{id:punch,lvl:5},{id:mending,lvl: 2147483647},{id:flame,lvl:1},{id:infinity,lvl:1}]}

![](http://i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png)

**弩**

1.16 版本，属于弩的附魔有：

Curse of Vanishing -- 消失诅咒（物品会在玩家死亡时消失）

Mending -- 经验修补（经验球会被用于修复物品耐久度）

Multishot -- 多重射击（消耗一支箭，射出三支箭）（耐久消耗是不附魔的三倍）

Piercing -- 穿透（使射出去的箭穿透多个实体，可以穿透盾牌的组队）

Quick Charge -- 快速装填（减少弩填装箭或烟花火箭的时间）（超过 5 级会使得弩箭无法装填）

Unbreaking -- 耐久（减缓物品的损耗）

下面举一个指令生成弩的实例：

/give @p crossbow{display:{Name:'{"text":" 千机 ","color":"gold"}'}, Unbreakable:1,Enchantments:[{id:multishot,lvl:1},{id:piercing,lvl:2147483647},{id:quick_charge,lvl:5},{id:unbreaking,lvl:2147483647},{id:mending,lvl:2147483647}]}

![](http://i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png)

**三叉戟**

1.16 版本，属于三叉戟的附魔有：

Channeling -- 引雷（雷暴天气时，掷出的三叉戟击中实体，会在被击中的实体处召唤闪电）（超过 1 级会使得三叉戟无法掷出）

Curse of Vanishing -- 消失诅咒（物品会在玩家死亡时消失）

Impaling -- 穿刺（对水生生物造成额外伤害）

Loyalty  -- 忠诚（掷出三叉戟后三叉戟会飞回来）（超过 3 级的附魔效果和 3 级一致，且太高等级会使得三叉戟无法掷出）

Mending -- 经验修补（经验球会被用于修复物品耐久度）

Riptide -- 激流（在水中或下雨时掷出三叉戟御戟飞行，其他时候无法掷出）（附魔太高等级容易摔死）

Unbreaking -- 耐久（减缓物品的损耗）

（正常情况下激流和引雷互斥）

下面举一个指令生成三叉戟的实例：

/give @p trident{display:{Name:'{"text":" 戟 ","color":"gold"}'},Unbreakable:1,Enchantments:[{id:unbreaking,lvl: 2147483647},{id:loyalty,lvl:10},{id:impaling,lvl:2147483647},{id:channeling,lvl:1},{id:mending,lvl: 2147483647}]}

![](http://i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png)

**特殊效果箭**

特殊效果箭属于武器类，但是这类物品的附魔指令与多属性药水附魔指令类似，因此放到药水篇进行说明。

![](http://i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png)

制作教程和排版挺费心神的，点个赞说两两句再走叭。

![](http://i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png)


引雷，用于苦力怕
/give @p trident{display:{Name:'{"text":" 戟 ","color":"gold"}'},Unbreakable:1,Enchantments:[{id:unbreaking,lvl: 2147483647},{id:loyalty,lvl:10},{id:channeling,lvl:2147483647}]}