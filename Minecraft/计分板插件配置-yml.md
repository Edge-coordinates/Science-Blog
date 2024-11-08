---
title: 计分板插件配置-yml
date: '2024/11/9 1:58:22'
categories:
  - Minecraft
abbrlink: 2dc74e5b
---
```yaml
#不需要权限则设置为null
permission: null
# 计分板优先级
priority: 1
# 显示的世界
worlds:
  - "example_1"
  - "example_2"
scoreboard:
  # 请注意，内容的line-#必须是按照数字顺序来的，比如123456
  # 计分板标题
  title:
    #刷新时间多少tick
    interval: 20
    #刷新的不同内容，如果只有一条则为不刷新
    lines:
      - '&3&lTR - 1.16.5'
      - '&b&lT&3&lR - 1.16.5'
      - '&b&lTR &3&l- 1.16.5'
      - '&b&lTR - &3&l1.16.5'
      - '&b&lTR - 1.&3&l16.5'
      - '&b&lTR - 1.16.&3&l5'
      - '&b&lTR - 1.16.5'
  #内容（行），line-必须严格按照顺序，比如123456
  line-1:
    interval: 100
    lines:
      - '    &e%player_name%'
  line-2:
    interval: 6
    lines:
      - '    &d&o%statistic_hours_played%小时'
  line-3:
    interval: 1000
    lines:
      - '&6余额：  &a%vault_eco_balance_fixed%'
  line-4:
    interval: 1000
    lines:
      - '&6QQ群：'
  line-5:
    interval: 1000
    lines:
      - ' &b999999999'
```