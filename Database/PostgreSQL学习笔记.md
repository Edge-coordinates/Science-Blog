---
title: PostgreSQL学习笔记
date: 2022/10/14
categories:
  - - Database
tags: null
abbrlink: 95327e2f
---

- [几个工具](#几个工具)
  - [pg\_ctl](#pg_ctl)
  - [常用命令](#常用命令)
- [用户管理](#用户管理)
  - [✅ 一、创建新用户并设置密码](#-一创建新用户并设置密码)
  - [🛡️ 二、授予权限（常见权限）](#️-二授予权限常见权限)
    - [1. 授予创建数据库权限：](#1-授予创建数据库权限)
    - [2. 授予超级用户权限（谨慎使用）：](#2-授予超级用户权限谨慎使用)
    - [3. 授予连接数据库权限（对已有数据库）：](#3-授予连接数据库权限对已有数据库)
  - [📦 三、在某个数据库中授予表的读写权限](#-三在某个数据库中授予表的读写权限)
  - [🚀 四、使用 `psql` 登录 PostgreSQL 并执行以上语句](#-四使用-psql-登录-postgresql-并执行以上语句)
  - [📁 五、可选：修改已有用户密码](#-五可选修改已有用户密码)


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



## 用户管理
在 PostgreSQL (`psql`) 中设置一个**新用户和密码**的步骤如下：

---

### ✅ 一、创建新用户并设置密码

```sql
CREATE USER new_username WITH PASSWORD 'your_password';
```

####NOTE -  示例：
```sql
CREATE USER alice WITH PASSWORD 'secure1234';
```

---

### 🛡️ 二、授予权限（常见权限）

根据用途授予权限：

#### 1. 授予创建数据库权限：
```sql
ALTER USER alice CREATEDB;
```

#### 2. 授予超级用户权限（谨慎使用）：
```sql
ALTER USER alice WITH SUPERUSER;
```

#### 3. 授予连接数据库权限（对已有数据库）：
```sql
GRANT CONNECT ON DATABASE your_database TO alice;
```

---

### 📦 三、在某个数据库中授予表的读写权限

进入某个数据库后，再运行：

```sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO alice;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO alice;
```

如果用户需要对未来创建的表也有权限，还需要：

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO alice;
```

---

### 🚀 四、使用 `psql` 登录 PostgreSQL 并执行以上语句

```bash
psql -U postgres
```

登录后复制粘贴这些 SQL 命令即可。

---

### 📁 五、可选：修改已有用户密码

```sql
ALTER USER alice WITH PASSWORD 'new_secure_password';
```

---

如果你是在 **Linux 或 Mac** 中用 `psql`，你也可以使用一行命令执行：
```bash
psql -U postgres -c "CREATE USER alice WITH PASSWORD 'secure1234';"
```

---

需要我帮你写一个完整的初始化脚本吗？可以包括创建数据库、用户、权限一体的 `init.sql`。你只需告诉我用户名、密码和数据库名就行。
