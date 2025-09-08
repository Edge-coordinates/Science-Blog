---
title: rust cargo
date: 2025/3/22 15:41:47
categories:
  - - Language
    - Rust
abbrlink: 6b9a7c58
---

在 Rust 中，类似于 `npm` 的工具是 **Cargo**，它是 Rust 的包管理器和构建工具。

## 命令详解

### 安装依赖
Rust 使用 `Cargo.toml` 文件来管理依赖项。`cargo build` 是类似于 `npm install` 的方法：  
它将会**这会下载并编译所有依赖项** 进而生成可执行文件

如果你从一个已有的项目中拉取代码（例如带有 `Cargo.toml` 文件），可以直接运行：
```bash
cargo build
```
或者：
```bash
cargo check
```
cargo check 不会编译并生成可执行文件，所以效率会高很多

### 更新依赖
如果需要更新依赖项到最新版本，可以运行：
```bash
cargo update
```

### 运行项目
类似于 `npm start`，你可以运行以下命令来构建并运行项目：
```bash
cargo run
```

### 总结
- `cargo build`：安装并编译依赖。
- `cargo run`：运行项目（会自动安装依赖）。
- `cargo update`：更新依赖到最新版本。