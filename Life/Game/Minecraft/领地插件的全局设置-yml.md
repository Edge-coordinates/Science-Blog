---
title: 领地插件的全局设置-yml
date: 2024/11/9 1:58:22
categories:
  - - Life
    - Game
    - Minecraft
abbrlink: 1dc2e20e
---
```yaml
# 这是领地插件的全局设置。 汉化：羽神
# 译者注：作者在Chinese.yml中flag翻译为权限，但这里为了防止误导，会将flag翻译为“标志”，请注意和权限插件的权限区分开。
Global:
  # 是否启用UUID
  # 如果你不知道这是什么就不要动它
  UUIDConvertion: true
  # 如果你用的是盗版服务器，最好设置为true。这可以帮助你解决UUID的问题。
  OfflineMode: false
  # 在登录的时候，玩家拥有 residence.versioncheck 权限时会提示版本信息。
  versionCheck: true
  # 这会加载 <language>。yml 文件当作领地插件的语言信息。
  # 领地插件所有的语言信息都在这里。 (还没做完)
  Language: Chinese
  # 木斧头是默认的圈地工具。
  # 你可以修改成其他工具，物品ID在这里: http://www.minecraftwiki.net/wiki/Data_values
  SelectionToolId: WOODEN_HOE
  Selection:
    # 如果设置为 true，所有的选择都会无视Y轴，即从天空到基岩。
    IgnoreY: false
    # 如果设置为 true， 现有领地的选择都会从顶部选择到到底部。
    # 如果设置为 false， 现有领地的选择将会一样。
    IgnoreYInSubzone: false
    # 如果设置为 true， 玩家只需要付X*Z大小方块的价钱。
    # 这会让领地的价格缩小256倍，所以在启用此功能前请调整好价格。
    NoCostForYBlocks: false
  # 这个选项可以决定你可以用什么工具来查看领地信息，默认是线。
  # 只需要拿着这个道具，在领地内任意一个地方点一下即可查看领地信息
  InfoToolId: STRING
  Optimizations:
    # 这会稍微的改变用户组 CanTeleport 的行为，这包括了服务器的总体判定方式。
    # 如果这个选项设置为 false 并且 CanTeleport 设置为 false， 玩家不能选择传送到其他玩家的领地，只有领地主才可以传送。
    # 如果这个选项设置为 true 而 CanTeleport 设置为 false， 玩家不能传送到任何领地
    # 这只适用于 /res tp 指令
    CanTeleportIncludeOwner: false
    # 这是你主要世界的名字。 通常设置为 'world'。 大小写很重要。
    DefaultWorld: world
    DisabledWorlds:
      # 设置哪个世界不启用插件。
      List: []
      # 是否在这些世界禁用所有的监听器(即领地插件的权限等)。
      DisableListeners: true
      # 是否在这些世界禁用领地插件的指令
      DisableCommands: true
    # 设置间隔多少秒会检查一次标志内容
    # 保持 10 秒会有利于检查。
    ItemPickUpDelay: 10
    AutomaticResidenceCreation:
      # 如果设置为 true，/res auto 会检查新领地是否会与其他领地发生重叠。
      # 如果设置为 false，服务器可以获得一些优化，但会导致新领地覆盖了旧领地
      CheckCollision: true
      # 使用自动创建领地指令时，如果该领地名字已经被使用，则会在新领地名字中增加参数。
      IncrementFormat: _[number]
    GlobalChat:
      # 开启或关闭玩家在领地中是否可以修改领地聊天信息。
      Enabled: false
      # 修改添加的聊天标题。如果你启用了聊天管理，你需要添加 {residence} 变量，来显示聊天标题。
      SelfModify: true
      Format: '&c[&e%1&c]'
    # 如果设置为 true， 任何传送都会检查是否拥有 tp 标志，没有将会被取消传送。
    # 这可以保护玩家使用其他第三方传送方式进行传送，比如 esentials插件的/tpa。
    BlockAnyTeleportation: true
    # 请将这个选项尽可能设置得低，或你可以使用 residence.max.res.[number] 权限
    # 例如你给玩家的最大圈地数量是10，你需要将这个选项设置为 15，或是 30， 或者又是 35，此选项可以制造一些缓冲区，以防万一。
    MaxResCount: 30
    # 请将这个选项尽可能设置得低，或你可以使用 residence.max.rents.[number] 权限
    # 例如你给玩家的最大zujie数量是10，你需要将这个选项设置为 15，或是 30， 或者又是 35，此选项可以制造一些缓冲区，以防万一。
    MaxRentCount: 10
    # 请将这个选项尽可能设置得低，或你可以使用 residence.max.subzones.[number] 权限
    # 例如你给玩家的最大子领地数量是10，你需要将这个选项设置为 15，或是 30， 或者又是 35，此选项可以制造一些缓冲区，以防万一。
    MaxSubzoneCount: 5
    # 请将这个选项尽可能设置得低，或你可以使用 residence.max.subzonedepth。[number] 权限
    # 例如你给玩家的最大子领地高度是10，你需要将这个选项设置为 15，或是 30， 或者又是 35，此选项可以制造一些缓冲区，以防万一。
    MaxSubzoneDepthCount: 5
    # 如果设置为 true，领地插件的pvp标志会覆盖Overridepvp权限
    # 在领地内，Overridepvp 标志会尝试覆盖其他pvp保护插件的权限。
    OverridePvp: false
    KickLocation:
      # 如果设置为 true，当玩家被踢出领地的时候， 他会传送到下面的这个坐标
      Use: false
      World: world
      X: 0.5
      Y: 63.0
      Z: 0.5
      # 设置小于 0 - 抬头， 大于 0 - 低头。 角度范围为 -90到 90。
      Pitch: 0.0
      # 设置头的转向。 角度范围为 -180 到 180。
      Yaw: 0.0
    FlyLandLocation:
      # 因为 fly(飞行) 标志或其他方法让玩家着陆，玩家将会传送到哪个坐标。
      World: world
      X: 0.5
      Y: 63.0
      Z: 0.5
      # 设置小于 0 - 抬头， 大于 0 - 低头。 角度范围为 -90到 90。
      Pitch: 0.0
      # 设置头的转向。 角度范围为 -180 到 180。
      Yaw: 0.0
    ShortInfo:
      # 如果设置为 true，玩家使用 /res info 会检查是否有权限，只会在聊天框显示名字，将鼠标移动到上面，则可以显示标志列表
      Use: true
    Vote:
      # 玩家可以投票的范围，通常设置为 0 到 10 格。
      RangeFrom: 0
      RangeTo: 10
      # 如果设置为 true，玩家只能像使用商店那样来投票。
      OnlyLike: false
    ConsoleLogs:
      # 如果设置为 true，在引导菜单(GUI)改变的标志会显示到控制台。
      ShowFlagChanges: true
    Intervals:
      # 如果玩家有 heal/food 的标志，每隔多少秒会回复玩家的 生命值/饥饿度。
      # 设置大的数值可以优化服务器资源。
      Heal: 1
      Feed: 5
    # 如果没有pvp标志没有设置，下面这些药水效果将会被无视。
    NegativePotionEffects:
    - blindness
    - confusion
    - harm
    - hunger
    - poison
    - slow
    - slow_digging
    - weakness
    - wither
    NegativeLingeringPotions:
    - slowness
    - instant_damage
    - poison
    - slowness
    # 调整 wspeed1 和 wspeed2 标志的速度。 它可以设置为0 到 5.
    WalkSpeed:
      '1': 0.5
      '2': 2.0
  # 移动标志的检查间隔。
  # 减小该数值可以缓解服务器压力。
  # 增大这个选项会导致玩家移动到更远距离才能被传送回去。
  MoveCheckInterval: 500
  Tp:
    # 设置领地传送的等待时间
    # 设置为0则取消等待
    TeleportDelay: 3
    # 玩家传送到领地时，是否显示标题信息。
    TeleportTitleMessage: true
  #译者注：随机传送的设置
  RandomTeleportation:
    Worlds:
      world_nether:
        Enabled: true
        MaxCoord: 1000
        MinCoord: 500
        CenterX: 0
        CenterZ: 0
      world:
        Enabled: true
        MaxCoord: 1000
        MinCoord: 500
        CenterX: 0
        CenterZ: 0
      world_the_end:
        Enabled: true
        MaxCoord: 1000
        MinCoord: 500
        CenterX: 0
        CenterZ: 0
    # 玩家需要等待多久才能使用一次该指令。
    Cooldown: 5
    # 尝试多少次传送的落地点。
    # 请将这个选项保持尽可能低，因为玩家过几秒后还能再次使用此指令。
    MaxTries: 20
  # 领地经过多少秒保存一次。
  SaveInterval: 10
  # 新的保存机制会有更小的占用和更快的保存/读取时间。
  # 文件越大，影响越大。
  NewSaveMechanic: true
  Backup:
    AutoCleanUp:
      # 如果你开启自动删除备份，插件会自动选择超过时间的备份自动删除。
      Use: false
      Days: 30
    # 是否让你的备份文件使用ZIP格式压缩。
    # 这不会对备份文件产生影响
    UseZip: true
    #译者注：会进行备份的文件。
    IncludeFiles:
      Worlds: true
      forsale: true
      leases: true
      permlists: true
      rent: true
      flags: true
      groups: true
      config: true
  AutoCleanUp:
    # 玩家没有登录超过多少天，插件会自动清楚玩家的领地。
    # 玩家可以通过 residence.cleanbypass 权限来绕过自动删除领地。
    Use: false
    # 会删除多少天没有登录的玩家。
    Days: 60
    # 你是否想让这地区变回原来的样子？
    # 它会将领地变回先前的样子。
    Regenerate: false
    # 启用功能的世界
    Worlds:
    - world
  Lwc:
    # 删除领地时，同时删除所有该领地的LWC保护。
    OnDelete: true
    # 购买领地时，删除所有该领地LWC保护。
    OnBuy: true
    # 领地无反应时，删除所有该领地的LWC保护。
    OnUnrent: true
    # 被删除保护的物品。
    MaterialList:
    - CHEST
    - TRAPPED_CHEST
    - furnace
    - dispenser
  AntiGreef:
    TNT:
      # 如果设置为 true，在领地外会允许TNT在 62 (默认) 格高度下爆炸。
      # 这允许设置TNT的最大爆炸高度。
      ExplodeBelow: true
      level: 62
    Creeper:
      # 如果设置为 true 在领地歪会允许爬行者在 62 (默认) 格高度下爆炸。
      # 这会让游戏更加逼真。
      ExplodeBelow: true
      level: 62
    Flow:
      # 允许液体流动的最大高度。
      # 这不会影响到领地内。
      Level: 63
      # 如果设置为 true，岩浆不会在领地外的地方流动
      NoLavaFlow: false
      # 如果设置为 true，水不会在领地歪的地方流动。
      NoWaterFlow: false
      Worlds:
      - world
    Place:
      # 从哪一层开始组织岩浆和水的放置。
      # 这不会影响到领地内。
      Level: 63
      # 如果设置为 true，玩家不能在领地外放置岩浆。
      NoLavaPlace: false
      # 如果设置为 true，玩家不能在领地外放置水。
      NoWaterPlace: false
      Worlds:
      - world
    BlockFall:
      # 如果设置为 true，将会删除掉落在在不同的地区的方块
      Use: false
      # 从哪一层开始允许掉落
      # 这不会影响到领地内。
      Level: 62
      Worlds:
      - world
    ResCleaning:
      # 如果设置会 true，会在玩家离开后清除领地内方块，包括所有在blocks列表的方块，他们都会变成空气方块。
      # 阻止附近方块接近领地，并清除方块。(Effective way to prevent residence creating near greefing target and then remove it)
      # 注意! 如果在大型领地清理，会造成很大的服务器负担，所有服务器拥有大领地请不要使用这个，最大限制是1500万个区块。
      Use: false
      # 从哪一层高度开始替换。
      Level: 63
      # 被替换的方块。
      # 默认的方块是岩浆和水。
      Blocks:
      - WATER
      - LAVA
      Worlds:
      - world
    Flags:
      # 如果设置为 true，除领地主之外，标志将会被保护，改变后领地内玩家当前的标志不会被改变。
      # 比如你改变了pvp的标志，但是你不能马上击杀该领地内的玩家。
      Prevent: true
      list:
      - pvp
  # 如果你没有权限插件，这将是默认的权限组。
  DefaultGroup: default
  # 开启 / 关闭zulin系统。
  UseLeaseSystem: false
  # 设置zulin或chuzu的信息格式
  # 如何正确使用，更多信息请查看 http://www.tutorialspoint.com/java/java_date_time.htm
  DateFormat: E yyyy.MM.dd 'at' hh:mm:ss a zzz
  # 设置zulin或chuzu的信息格式
  # 如何正确使用，更多信息请查看 http://www.tutorialspoint.com/java/java_date_time.htm
  DateFormatShort: MM.dd hh:mm
  # 设置时区信息，这可以调整不同时区玩家在服务器内的时间
  # 其他的时区请看 http://www.mkyong.com/java/java-display-list-of-timezone-with-gmt/
  TimeZone: Asia/Shanghai
  # 开启 / 关闭删除领地返还金钱。
  ResMoneyBack: true
  # 设置zulin的检查间隔 (需要开启zulin系统)。
  LeaseCheckInterval: 10
  # 如果玩家有金钱，允许自动续zu，如果没有开启经济系统，这选项将没有用。
  LeaseAutoRenew: true
  # 是否将权限插件与此config权限同时使用。
  EnablePermissions: true
  # 使用 Permissions / PermissionsBukkit 插件，或者使用其他旧版的权限插件，请将它设置为 true
  LegacyPermissions: true
  # 开启 / 关闭领地插件的经济系统 (支持iConomy， MineConomy， Essentials， BOSEconomy，和 RealEconomy)。
  EnableEconomy: true
  # 设置为 None 会检查默认的经济系统，如 vault API 和其他支持经济的系统。
  # 自定义经济系统的话需要可以直接访问
  # 支持的插件: Vault， iConomy， MineConomy， Essentials， BOSEconomy， RealEconomy， CMIEconomy， None
  Type: None
  # 开启此选项，会在聊天框显示额外的信息，例如显示购买/zujie时的基础信息。
  ExtraEnterMessage: true
  Sell:
    # 如果设置为 true，可以允许出售子领地。建议设置为false。
    Subzone: false
  # 开启 / 关闭zulin系统。
  EnableRentSystem: true
  Rent:
    # 保护 领地/子领地在zulin期间不会被删除。
    PreventRemoval: true
    # 如果设置为true，可从领地银行里取钱续zu
    DeductFromBank: false
    # 如果设置为true，如果玩家的领地银行没有足够的钱续zu，则会从玩家的账户中扣钱。
    # 这会覆盖银行扣钱的行为
    DeductFromBankThenPlayer: false
    Inform:
      # 是否开启zulin时间提示
      OnEnding: true
      # 还有多少时间时提示zulin时间将要结束
      Before: 1440
      # 玩家登录多少秒后通知zulin时间结束
      Delay: 60
    DefaultValues:
      # chuzu的默认值
      AllowRenewing: true
      StayInMarket: true
      AllowAutoPay: true
      # 如果设置为 true， 当玩家没有开启自动续zu，则开启此值
      PlayerAutoPay: true
    Schematics:
      # 实验选项!!! 如果设置为 true，backup标志为true时会恢复备份的领地。
      # 为了安全，只有领地创始人可以修改此标志。备份权限可以设置备份标志节点。
      RestoreAfterRentEnds: true
      # 如果设置为 true，只有backup标志设置为true时才会备份
      # 如果设置为 false，领地会在每次zulin之前保存，并恢复到原来的样子。
      # 保持这个选项设置为 false，在一些zulin领地保存时会造成一些轻微的服务器负担。
      SaveOnFlagChange: true
  # 设置zu金到期的检查间隔 (需要zulin系统开启)。
  RentCheckInterval: 10
  # 是否开启聊天频道。
  ResidenceChatEnable: true
  Messages:
    # 设置领地 进入(enter)/离开(lease)/拒绝(deny)和其他更多信息显示在哪里。 可用选择: ActionBar， TitleBar， ChatBox
    # TitleBar 可以使用 %subtitle% 来显示子领地信息
    GeneralMessages: ChatBox
  ActionBar:
    ShowOnSelection: true
  # 领地聊天的颜色。
  ResidenceChatColor: DARK_PURPLE
  ResidenceChatPrefixLength: 16
  # 是否忽略通常的标志并且只有OP和拥有 'residence.admin' 权限的人去改变。
  AdminOnlyCommands: false
  # 设置为 true 拥有服务器OP管理员。
  AdminOPs: true
  # 设置为 true ，服务器管理员需要使用 /resadmin 指令来执行管理员权限，或者拥有 residence.admin 权限来执行。
  AdminFullAccess: false
  # 这是你多时间插件的名字，如果你没有多世界插件请无视它。
  # 只有多世界插件设置正确，领地插件才会正确加载其他世界。
  MultiWorldPlugin: Multiverse-Core
  # 设置为 true，可以让子领地继承主领地内容
  ResidenceFlagsInherit: true
  # 设置为 false，将会允许玩家布置zulin领地。
  PreventRentModify: true
  # 设置为 true，当删除子领地时进行保护，防止子领地与父领地的主人不是同一个的情况。
  PreventSubZoneRemoval: true
  # 设置为 false，领地在发现错误的时候仍然会尝试继续加载。
  StopOnSaveFault: true
  ResidenceNameRegex: '[^a-zA-Z0-9\-\_]'
  # 设置为 true，会将领地zulin和zujie到期的信息发送至控制台。
  ShowIntervalMessages: false
  # 设置为 true，新玩家放置箱子到地上时会引导玩家。
  ShowNoobMessage: true
  # 设置为 true，当玩家没有领地时，并且附近拥有他放置的箱子则会自动圈地。。
  # 只有当他在服务器没有任何领地时会这样做。
  NewPlayer:
    Use: false
    # 设置为 true，这个领地的创建将会是免费的
    # 设置为 false，如果他有钱，则会自动扣除他的钱。
    Free: true
    # 箱子放在身边的距离。如果设置为 5，领地将会圈 5+5+1 = 11 方块大小
    Range:
      X: 5
      Y: 5
      Z: 5
  # 实验功能 - 下面选项的ID是MOD物品可以使用 'container' 和 'use' 标志的物品。
  CustomContainers: []
  CustomBothClick: []
  CustomRightClick: []
  Visualizer:
    # 如果开启，玩家会在选择领地的时候看见粒子效果
    Use: true
    # 玩家显示粒子效果的范围
    # 保持这个选项小于 30，因为玩家只能看见16格内的效果。
    Range: 16
    # 显示效果持续多长 (5000 = 5秒) 。
    ShowFor: 5000
    # 多少秒更新一次玩家显示的粒子效果
    updateInterval: 20
    # 间隔多少的方块显示一粒子效果
    RowSpacing: 2
    # 粒子在共线时间隔的方块
    CollumnSpacing: 2
    # 设置需要跳过多少粒子
    # 这是创建移动粒子效果的选项并且会改进选择粒子的美观度。
    # 当数量越大，你可以缩进的时间间隔就越多
    SkipBy: 5
    # 一边显示的最大粒子数
    FrameCap: 500
    # 侧面显示的最大粒子数
    SidesCap: 2000
    # 特殊粒子名字。 possible: explode， largeexplode， hugeexplosion， fireworksSpark， splash， wake， crit， magicCrit
    #  smoke， largesmoke， spell， instantSpell， mobSpell， mobSpellAmbient， witchMagic， dripWater， dripLava， angryVillager， happyVillager， townaura
    #  note， portal， enchantmenttable， flame， lava， footstep， cloud， reddust， snowballpoof， snowshovel， slime， heart， barrier
    #  droplet， take， mobappearance

    # 如果你是spigot类服务器，还可以使用:
    # click2， click1， bow_fire， door_toggle， iron_door_toggle， trapdoor_toggle， iron_trapdoor_toggle， fence_gate_toggle， door_close， iron_door_close， trapdoor_close， iron_trapdoor_close， fence_gate_close， extinguish， record_play， ghast_shriek， ghast_shoot， blaze_shoot， zombie_chew_wooden_door， zombie_chew_iron_door， zombie_destroy_door， smoke， step_sound， potion_break， ender_signal， mobspawner_flames， brewing_stand_brew， chorus_flower_grow， chorus_flower_death， portal_travel， endereye_launch， firework_shoot， villager_plant_grow， dragon_breath， anvil_break， anvil_use， anvil_land， enderdragon_shoot， wither_break_block， wither_shoot， zombie_infect， zombie_converted_villager， bat_takeoff， end_gateway_spawn， enderdragon_growl， 
    Selected:
      Frame: happyVillager
      Sides: reddust
    Overlap:
      Frame: FLAME
      Sides: FLAME
    # 玩家进入领地是否显示粒子效果。 只会在主领地有效
    EnterAnimation: true
  # 玩家被推出领时是否显示粒子效果
  BounceAnimation: true
  GUI:
    # 打开标志引导菜单(GUI)
    Enabled: true
    # 当标志为true时显示的物品
    setTrue: GREEN_WOOL
    # 当权限显示为false时显示的物品
    setFalse: RED_WOOL
    # 当权限显示为remove时显示的物品
    setRemove: LIGHT_GRAY_WOOL
  # 默认 = false。 开启它，有 nomobs 标志的领地将会定期清理怪物。
  # 这对服务器造成的负担是非常严重的，所以在你需要的时候再打开它。
  AutoMobRemoval:
    Use: false
    # 多少秒进行一次检查。请进来保持数值够大。
    Interval: 3
  EnforceAreaInsideArea: false
  EnableSpout: false
  EnableLeaseMoneyAccount: true
  # 如果设置为 true，增加对 kCouldron 服务端的支持。 Action bar 信息和选择可视化等内容会被禁用。
  Couldroncompatibility: false
DynMap:
  # 是否开启对 DynMap 的支持
  Use: false
  # 显示隐藏的标志
  ShowFlags: true
  # 如果设置为true，会从dynmap中隐藏设置为true的标志。
  HideHidden: true
  Layer:
    # 开启 3D 区域
    3dRegions: true
    # 显示子领地的深度
    SubZoneDepth: 2
  Border:
    # 颜色代码。 从这网站选择颜色 http://www.w3schools.com/colors/colors_picker.asp
    Color: '#FF0000'
    # 透明度。 0.3 意味着只显示 30% 颜色
    Opacity: 0.3
    # 边框厚度
    Weight: 3
  Fill:
    Opacity: 0.3
    Color: '#FFFF00'
    ForRent: '#33cc33'
    Rented: '#99ff33'
    ForSale: '#0066ff'
  # 在列表上显示的区域
  VisibleRegions: []
  # 在游戏地图上隐藏的区域
  HiddenRegions: []
# 发展中选项
Raid:
  # 这是决定你服务器是否使用袭击功能
  # 当启用此功能的时候，袭击者仍然可以在该领地进行移动，即使 move 的标志为 false
  Enabled: false
  # 袭击开始前的时间
  # 这时间将会允许回到领地并做好保卫领地来与袭击者对抗
  PreTimer: 120
  # 这个时间是袭击的时间
  # 这个时间将允许袭击者偷走物品并杀害防卫者
  Timer: 120
  # 这是领地免受袭击的保护时间
  # 默认是 79200 秒，也就是22小时，如果重启会刷新时间
  Cooldown: 79200
  # 这是玩家免受袭击的保护时间
  # 这个情况适用于玩家有多个领地，防止玩家再次受到袭击
  # 默认是 79200 秒，也就是22小时，如果重启会刷新时间
  PlayerCooldown: 79200
  Allow:
    Attacker:
      # 允许袭击者打破方块，即使 destroy 标志设置为 false
      # 这只适用于袭击者袭击的时间
      blockBreak: true
      # 允许袭击者放置方块，即使 place 标志设置为 false
      # 这只适用于袭击者袭击的时间 
      blockPlace: true
    Defender:
      # 允许保卫者打破方块，即使 destroy 标志设置为 false
      # 这只适用于袭击者袭击的时间
      blockBreak: true
      # 允许保卫者放置方块，即使 place 标志设置为 false
      # 这只适用于袭击者袭击的时间
      blockPlace: true
      # 允许袭击者传送至领地，包括使用 /res tp 或其他第三方传送插件
      # 这只适用于袭击者袭击的时间
      # 请记住，如果袭击者没有此权限，他将无法在袭击的领地上进行传送
      Teleport: false
      # 在袭击者袭击时间和受保护的时间，允许袭击者使用容器，如箱子
      # 这只适用于袭击者袭击的时间和受保护的时间
      # 设置为 false 可以保证玩家在受保护的时候将物品移动到另外一个不被攻击的领地
      # 在袭击时间内，袭击者将会被允许打开任何的容器
      containerUsage: false
  # 当设置为 false 时，玩家处于同一队伍 (袭击者 或 保卫者) 会无法对队友进行伤害
  FriendlyFire: true
```