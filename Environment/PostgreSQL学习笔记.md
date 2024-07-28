---
title: PostgreSQL学习笔记
date: 2022/10/14
categories:
  - Environment
abbrlink: 95327e2f
tags:
---


## 几个工具
### pg_ctl
- `pg_ctl start` 启动PostgreSQL服务

### 常用命令

``` powershell
pg_ctl start
# 启动
psql -U postgres

```

结尾要打一个`;`不然会逐条运行,相当于一个队列



以下是一些常用的 PostgreSQL 命令：

1.  `psql`: 启动 PostgreSQL 客户端。
    
2.  `\q`: 退出 psql 客户端。
    
3.  `\c database_name`: 连接到指定的数据库。
    
4.  `\l`: 列出当前 PostgreSQL 实例中的所有数据库。
    
5.  `\dt`: 列出当前数据库中的所有表格。
    
6.  `\d table_name`: 显示指定表格的结构。
    
7.  `SELECT * FROM table_name`: 选择指定表格中的所有行和所有列。
    
8.  `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)`: 向指定表格中插入新行。
    
9.  `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition`: 更新符合条件的行。
    
10.  `DELETE FROM table_name WHERE condition`: 删除符合条件的行。
    
11.  `CREATE TABLE table_name (column1 data_type, column2 data_type, ...)`: 创建新表格。
    
12.  `ALTER TABLE table_name ADD COLUMN column_name data_type`: 在现有表格中添加新列。
    
13.  `DROP TABLE table_name`: 删除指定表格。
    
14.  `GRANT permissions ON table_name TO user`: 授予用户对指定表格的权限。
    
15.  `REVOKE permissions ON table_name FROM user`: 撤销用户对指定表格的权限。



**注意:**

`\d "OAuthTokens"`:似乎带有大写字母的表名称，也需要使用双引号。。。

卧槽卧槽。

