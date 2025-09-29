---
title: PostgreSQL学习笔记
date: 2022/10/14
updated: 2025/09/11 17:43:48
categories:
  - - Database
tags: null
abbrlink: 95327e2f
---

- [几个工具](#几个工具)
  - [pg\_ctl](#pg_ctl)
  - [常用命令](#常用命令)
- [PSQL结构](#psql结构)
  - [Schema](#schema)
    - [在 Prisma 里的意义](#在-prisma-里的意义)
    - [为什么要指定 schema？](#为什么要指定-schema)
- [用户管理](#用户管理)
  - [创建新用户并设置密码](#创建新用户并设置密码)
    - [NOTE -  示例：](#note----示例)
  - [授予权限（常见权限）](#授予权限常见权限)
    - [1. 授予创建数据库权限：](#1-授予创建数据库权限)
    - [2. 授予超级用户权限（谨慎使用）：](#2-授予超级用户权限谨慎使用)
    - [3. 授予连接数据库权限（对已有数据库）：](#3-授予连接数据库权限对已有数据库)
  - [在某个数据库中授予表的读写权限](#在某个数据库中授予表的读写权限)
  - [使用 `psql` 登录 PostgreSQL 并执行以上语句](#使用-psql-登录-postgresql-并执行以上语句)
  - [修改已有用户密码](#修改已有用户密码)


## 几个工具
### pg_ctl
- `pg_ctl start` 启动PostgreSQL服务

### 常用命令

``` powershell
pg_ctl start
# 启动
psql -U postgres

```

DATABASE_URL
```
DATABASE_URL="postgresql://postgres@localhost:5432/rezics_oauth?schema=public"
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


## PSQL结构

### Schema
在 PostgreSQL 里，**数据库 (database)** 和 **模式 (schema)** 是两个不同层级的概念：

* **Database**：就像是一个「图书馆」。
* **Schema**：就像是图书馆里的「书架」。
* **Table**：则是书架上的「书」。

同一个数据库里可以有多个 schema，它们用来**组织和隔离表、视图、函数等对象**。例如：

```sql
-- 数据库 mydb 下有两个 schema
CREATE SCHEMA sales;
CREATE SCHEMA hr;

-- sales 下的表
CREATE TABLE sales.orders (...);

-- hr 下的表
CREATE TABLE hr.employees (...);
```

这样 `sales.orders` 和 `hr.employees` 就能在同一个数据库里共存，不会互相冲突。

---

#### 在 Prisma 里的意义

Prisma 连接 PostgreSQL 时，`DATABASE_URL` 里的 `schema=public` 表示**默认使用哪个 schema**。

* PostgreSQL 默认有一个 `public` schema，几乎所有人一开始的表都建在这里。
* 如果你想做更清晰的隔离，可以在数据库里建一个新的 schema，比如 `app`，然后在连接字符串里写：

  ```env
  DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=app"
  ```

  Prisma 就会在 `app` 这个 schema 下生成和管理表。

---

#### 为什么要指定 schema？

1. **多租户隔离**：一个数据库服务多个客户时，每个客户一个 schema。
2. **逻辑分组**：不同业务模块放到不同 schema，比如 `analytics`、`auth`。
3. **避免命名冲突**：两个团队都要建 `users` 表时，可以各自放在不同 schema 里。

---

换句话说：指定 database 决定了「用哪个图书馆」，指定 schema 决定了「用图书馆里的哪个书架」。



## 用户管理
在 PostgreSQL (`psql`) 中设置一个**新用户和密码**的步骤如下：

---

### 创建新用户并设置密码

```sql
CREATE USER new_username WITH PASSWORD 'your_password';
```

#### NOTE -  示例：
```sql
CREATE USER alice WITH PASSWORD 'secure1234';
```

---

### 授予权限（常见权限）

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

### 在某个数据库中授予表的读写权限

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

### 使用 `psql` 登录 PostgreSQL 并执行以上语句

```bash
psql -U postgres
```

登录后复制粘贴这些 SQL 命令即可。

---

### 修改已有用户密码

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
