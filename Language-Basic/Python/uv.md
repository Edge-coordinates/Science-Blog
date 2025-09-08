---
title: uv
date: '2025/7/1 21:25:28'
categories:
  - Language-Basic
  - Python
abbrlink: aaf74b45
---
你提到的那个用 Rust 编写的 Python 包和环境管理器，很可能是 **uv**。([Astral: Next-gen Python tooling][1])

---

### 🌟 什么是 uv？

**uv** 是由 Astral 公司开发的一款高性能 Python 包和项目管理工具，旨在成为 Python 生态中的 “Cargo”——即一个统一的、快速、可靠且易用的包管理器。([豌豆花下猫][2])

其主要特点包括：

* **极致性能**：得益于 Rust 的高效实现，uv 在依赖解析和安装方面比传统工具如 pip 快 8～10 倍，在有缓存的情况下甚至可达 80～115 倍。&#x20;
* **一站式管理**：uv 集成了包安装、依赖锁定、虚拟环境创建等功能，简化了项目的管理流程。
* **高度兼容**：uv 设计为 pip 和 pip-tools 的直接替代品，支持现有的 requirements.txt 和 pyproject.toml 文件，便于现有项目的迁移。
* **跨平台支持**：uv 支持 Linux、Windows 和 macOS 平台，适用于多种开发环境。([CSDN Blog][3], [hinnuryuu.cc][4], [豌豆花下猫][2])

---

### 🚀 如何安装 uv？

你可以通过以下方式安装 uv：

* **使用官方安装脚本**：

  * macOS 和 Linux：

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

  * Windows（PowerShell）：

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

* **使用 pip 安装**：

```bash
  pip install uv
```



安装完成后，可以通过 `uv --help` 命令查看 uv 的使用帮助。([豌豆花下猫][2])

---

### 🛠️ uv 的基本用法

以下是 uv 的一些常用命令：

* **初始化项目**：

```bash
  uv init my_project
```



该命令会创建一个新的项目目录，并生成 `pyproject.toml` 和 `uv.lock` 文件。([Cnblogs][5])

* **添加依赖**：

```bash
  uv add requests
```



这会将 `requests` 包添加到项目的依赖中，并更新锁定文件。

* **创建虚拟环境**：

```bash
  uv venv
```



该命令会在项目目录下创建一个 `.venv` 虚拟环境。([少数派 - 高品质数字消费指南][6])

* **运行项目**：

```bash
  uv run python main.py
```



这会在 uv 管理的环境中运行 `main.py` 脚本。

---

### 🔗 相关资源

* 官方网站：[https://astral.sh/uv](https://astral.sh/uv)
* GitHub 仓库：[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
* 官方文档：[https://docs.astral.sh/uv](https://docs.astral.sh/uv)([Cnblogs][5], [CSDN Blog][7])

---

如果你还记得其他细节，比如工具的名称或特定功能，也可以提供更多信息，我会尽力帮你找到它。

[1]: https://astral.sh/blog/uv?utm_source=chatgpt.com "uv: Python packaging in Rust - Astral"
[2]: https://pythoncat.top/posts/2024-03-05-uv?utm_source=chatgpt.com "用Rust 开发的Python 包管理工具uv，可替换pip - 豌豆花下猫"
[3]: https://blog.csdn.net/qq_35082030/article/details/146549871?utm_source=chatgpt.com "Python 包管理器UV 全面介绍原创 - CSDN博客"
[4]: https://hinnuryuu.cc/index.php/archives/53/?utm_source=chatgpt.com "UV：Python生态的下一代包管理革命 - YetAnotherSpace"
[5]: https://www.cnblogs.com/wang_yb/p/18635441?utm_source=chatgpt.com "Python包管理不再头疼：uv工具快速上手- wang_yb - 博客园"
[6]: https://sspai.com/post/75978?utm_source=chatgpt.com "10.2 细数Python 虚拟环境的管理方案 - 少数派"
[7]: https://blog.csdn.net/lovechris00/article/details/145428126?utm_source=chatgpt.com "UV - Rust 编写的Python 包管理器 - CSDN博客"


## 常用命令

当然可以，以下是 **uv** 工具的所有常用命令及其简单注释，涵盖依赖管理、虚拟环境管理、与 `requirements.txt` 的互操作等内容。

---

## 🧰 uv 常用命令速查表（含注释）

### 📦 依赖管理

| 命令                           | 用途       | 说明                                                      |
| ---------------------------- | -------- | ------------------------------------------------------- |
| `uv add <package>`           | 添加依赖     | 会自动解析版本并写入 `uv.lock` 和 `pyproject.toml`。                |
| `uv remove <package>`        | 移除依赖     | 会从 `pyproject.toml` 中移除并更新锁文件。                          |
| `uv pip install <args>`      | pip 兼容层  | 用于兼容 pip 命令的安装行为（可用于安装 `.whl`、`.tar.gz` 包等）。            |
| `uv pip uninstall <package>` | 卸载包      | 与 pip 行为一致，适用于某些特殊场景。                                   |
| `uv sync`                    | 安装依赖     | 根据 `uv.lock` 安装依赖。类似 `pip install -r requirements.txt`。 |
| `uv update`                  | 更新依赖     | 自动更新依赖版本，重新解析 `pyproject.toml`。                         |
| `uv lock`                    | 生成/更新锁文件 | 明确锁定当前环境下的包版本，生成 `uv.lock`。                             |
| `uv pip freeze`              | 导出依赖     | 生成 `requirements.txt` 格式输出。可重定向保存。                      |

---

### 🧪 虚拟环境管理

| 命令                        | 用途                 | 说明                                       |
| ------------------------- | ------------------ | ---------------------------------------- |
| `uv venv`                 | 创建虚拟环境             | 在项目目录下创建 `.venv` 虚拟环境。                   |
| `uv venv --python <path>` | 指定 Python 版本创建虚拟环境 | 用于选择系统中其他版本 Python。                      |
| `uv run <command>`        | 运行命令               | 在虚拟环境中运行任意命令，例如 `uv run python main.py`。 |
| `uv python`               | 启动解释器              | 直接启动项目的虚拟环境下的 Python。                    |

---

### 🔄 与 requirements.txt 的互操作

| 命令                                   | 用途                      | 说明                 |
| ------------------------------------ | ----------------------- | ------------------ |
| `uv pip install -r requirements.txt` | 从 `requirements.txt` 安装 | 兼容 pip 的行为。        |
| `uv pip freeze > requirements.txt`   | 导出到 `requirements.txt`  | 导出当前环境为传统格式，兼容旧项目。 |

---

### 🧱 项目初始化

| 命令              | 用途        | 说明                                   |
| --------------- | --------- | ------------------------------------ |
| `uv init [dir]` | 初始化 uv 项目 | 自动创建 `pyproject.toml` 和空的 `uv.lock`。 |
| `uv --version`  | 查看版本      | 显示 uv 当前安装版本。                        |
| `uv help`       | 帮助        | 查看所有命令的简要说明。                         |

---

### ✅ 示例流程（推荐使用流程）

```bash
# 初始化项目
uv init .

# 添加依赖
uv add requests numpy

# 创建虚拟环境
uv venv

# 运行脚本
uv run python app.py

# 锁定依赖
uv lock

# 同步依赖（安装）
uv sync

# 导出依赖列表
uv pip freeze > requirements.txt

# 从 requirements.txt 安装
uv pip install -r requirements.txt
```

---


## 虚拟环境管理
`uv` 本身支持虚拟环境的自动管理，但它与传统工具（如 `venv`, `virtualenv`, `conda`）的使用方式略有不同，下面是它在“保存虚拟环境配置”和“启用特定虚拟环境”方面的行为说明：

---

## ✅ uv 的虚拟环境行为说明

### 📍 默认行为：自动管理 `.venv`

* 执行 `uv venv` 时，**uv 会在项目目录创建 `.venv/` 文件夹**，这就作为项目的虚拟环境目录。
* **`uv run` / `uv python` / `uv pip`** 都默认在此 `.venv` 中运行，无需激活。
* 它不需要你手动 `source .venv/bin/activate`。

---

### ❌ 不支持的功能（当前版本）：

| 功能                     | 是否支持     | 说明                                                                              |
| ---------------------- | -------- | ------------------------------------------------------------------------------- |
| 保存多个虚拟环境配置             | ❌        | 不像 `poetry` 或 `conda` 可以管理多个 envs 并选择启用。                                        |
| 指定启用已有的 venv           | ⚠️ 有条件支持 | 可通过 `uv venv --python <path>` 创建不同环境，但不支持自由切换多个现存 venv。                         |
| 自动识别 `.venv` 之外的虚拟环境路径 | ❌        | 目前 `uv` 只管理它自己创建的 `.venv`，不支持读取 `.python-version` 或 `PYENV_VERSION` 等 pyenv 设置。 |

---

## 🛠️ 可行方案 / 替代思路

1. **手动切换不同虚拟环境目录：**

   * 如果你手动使用不同 `.venv-*` 文件夹，可以在 shell 中设置：

     ```bash
     VIRTUAL_ENV=".venv-py310" uv run python app.py
     ```

     但 uv 本身不提供这种切换机制。

2. **使用 `.python-version` 搭配 pyenv（间接解决 python 版本）**

   * uv 支持 `--python` 参数，你可以这样：

     ```bash
     uv venv --python ~/.pyenv/versions/3.11.7/bin/python
     ```

     但这仍不等于保存多个虚拟环境配置。

---

## uv 的哲学

* **单一项目目录绑定一个 `.venv`，一套依赖锁定（uv.lock）**
* 它是“Rust 风格”的简洁工具链，**不鼓励管理多个虚拟环境状态**，更倾向于：

  * 每个项目一个 env
  * 所有状态明确写入 `pyproject.toml` 和 `uv.lock`

---

如果你有使用多个 Python 项目切换虚拟环境的需求，也许可以搭配：

* `direnv`（自动切换 `.venv`）
* `pyenv + pyenv-virtualenv`（管理不同 Python 版本 + 虚拟环境）
* `rye`（另一种 Rust 写的工具，更注重多环境）
