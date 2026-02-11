---
title: Linux 链接 Github
date: 2026/02/11 23:57:21
categories:
  - - Environment
    - Git
abbrlink: "24036393"
---
# 配置 Linux Git 密钥

#### You:

linux 怎么 配置 git 密钥？

#### ChatGPT:

在 Linux 上配置 Git 的 SSH 密钥，这个流程本质上跟其他类 Unix 系统一样，像在给一把锁（GitHub/GitLab）配一把独属于你的魔法钥匙。下面把整个过程拆成几个清爽的步骤，你照着敲就行。

---

## 1. 先看看你是不是已经有钥匙了

在终端里敲：

```bash
ls ~/.ssh
```

如果你看到了 `id_rsa` / `id_ed25519` / `.pub` 这样的文件，说明你已经有密钥，可以直接用。

---

## 2. 没有？那就生成一把新的

一般推荐 **ed25519**，更快更安全。

```bash
ssh-keygen -t ed25519 -C "edgecoordinates@gmail.com"
```

执行后会出现：

```
Enter file in which to save the key (/home/xxx/.ssh/id_ed25519):
```

直接按 Enter 就好。

再来一个：

```
Enter passphrase (empty for no passphrase):
```

可填可不填（填的话更安全，不填更方便）。

---

## 3. 启动 SSH Agent（钥匙管理器）

保证系统正在帮你“记住”这把钥匙：

```bash
eval "$(ssh-agent -s)"
```

然后加入密钥：

```bash
ssh-add ~/.ssh/id_ed25519
```

---

## 4. 把公钥贴到 GitHub / GitLab

查看你的公钥内容：

```bash
cat ~/.ssh/id_ed25519.pub
```

接着复制整行，从 “ssh-ed25519 …” 开头，到邮箱结尾。

到 GitHub：

- Settings → SSH and GPG keys → New SSH key

到 GitLab：

- User Settings → SSH Keys → Add key

贴进去保存。

---

## 5. 测试是否连通

GitHub：

```bash
ssh -T git@github.com
```

成功会看到：

```
Hi <username>! You've successfully authenticated...
```

GitLab：

```bash
ssh -T git@gitlab.com
```

---

## 6. 以后 clone 用 SSH 链接

像这样：

```bash
git clone git@github.com:owner/repo.git
```

---

## 想进一步魔改？

比如多个密钥、多个平台、Host 匹配、跳板机，都可以通过编辑：

```bash
nano ~/.ssh/config
```

写：

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
```

这让 Git 用户生涯舒服得像是给项目添了自动门。

---

如果你说的是 **Git 账号的 credential（HTTPS）** 而非 SSH 密钥，也可以说，我把那套也给你带上。


#### You:

eval "$(ssh-agent -s)" 是什么意思？ssh-add ~/.ssh/id_ed25519

#### ChatGPT:

这两个命令其实是一套组合拳，用来让你的系统**启动 SSH Agent**并**把私钥交给它保管**。把它想象成：你启动一个“钥匙侍从”，再把你的“主密钥”交给它，这样之后 Git 操作时无需手动输入路径或密码。

我拆开讲一下，让整个过程透明得像空气。

---

# 1. `eval "$(ssh-agent -s)"` 是什么？

这个命令的作用是：**启动 ssh-agent，并把它输出的环境变量导入当前 shell。**

### ssh-agent 是啥？

它是一个“后台进程”，专门帮你：

- 存放你的 SSH 私钥（暂存在内存）
- 处理签名请求（比如 ssh 登录、git pull 等）
- 如果你给私钥设置了密码，它还能帮你记住密码，不用每次输入

### 那 `-s` 是干嘛的？

`ssh-agent -s` 让 ssh-agent 输出一段用 shell 语法写的环境变量，比如：

```
SSH_AUTH_SOCK=/tmp/ssh-XXXX/agent.1234; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

这些变量告诉你的系统：

- `SSH_AUTH_SOCK`：ssh-agent 的通信 socket 文件
- `SSH_AGENT_PID`：agent 的进程号

**但注意：这段输出只是文本，不会自动执行。**

### 所以要用 `eval`

`eval` 的作用是：**把 ssh-agent 的输出当作命令再执行一遍。**

像这样：

```
ssh-agent -s → 输出一堆 export 指令
eval → 执行这些 export 指令
当前 shell 就知道 ssh-agent 在哪里
```

于是整个系统都能通过这个 socket 找到 agent，让后续 SSH/Git 都能用你的密钥。

---

# 2. `ssh-add ~/.ssh/id_ed25519` 是什么？

这句话的意思是：

**把你的私钥 `id_ed25519` 加载到 ssh-agent，让它替你保管并使用。**

相当于：

- 你：把我的钥匙拿着。
- ssh-agent：好，以后需要签名（ssh 登录、git pull）的时候我来。

如果你给私钥设置了密码，执行 `ssh-add` 会出现：

```
Enter passphrase for /home/xxx/.ssh/id_ed25519:
```

输入一次就行，后面 session 内都不用再输入。

---

# 两者关系像这样：

1. `eval "$(ssh-agent -s)"`\
   → 启动钥匙管理器

2. `ssh-add ~/.ssh/id_ed25519`\
   → 把你的 SSH 私钥放进管理器随时使用

没有 `ssh-agent`，`ssh-add` 是没地方放钥匙的。\
没有 `ssh-add`，ssh-agent 就像空钱包，啥也干不了。

---

# 再比喻一层（最形象）

- ssh-agent：你的私人司机
- eval "$(ssh-agent -s)"：告诉你司机的电话号码和位置，并雇佣他
- ssh-add id\_ed25519：把车钥匙交给司机
- git pull：给司机发指令，让他开车带你走

---

# Bonus：不开 ssh-agent 可以吗？

可以，只是你每次 git 操作都会需要输入密钥密码（如果你的私钥有密码）。

---

如果你愿意，我还能给你画一个更底层的“SSH 认证数据流图”，把这两个步骤在系统内部到底做了什么完整解释得清清楚楚。


#### You:

这个是永久性的嘛？无论重启或是怎样？

#### ChatGPT:

这两个命令 **默认不是永久性的**。\
你可以把它当成“本次登录有效”的魔法。

它们的寿命如下：

---

# 1. `eval "$(ssh-agent -s)"` —— 会在你当前 Session 有效

ssh-agent 是一个 **用户进程**，不是系统服务。

所以：

- 你开一个新的终端窗口：**需要重新执行**
- 你注销：**失效**
- 你重启：**失效**

它不会长期跑在后台。\
属于“本次登录周期的钥匙管理器”。

---

# 2. `ssh-add ~/.ssh/id_ed25519` —— 只在当前 agent 有效

密钥加进 agent 后：

- 当前 session 内有效
- 你关闭 agent → 密钥消失
- 你重启电脑 → agent 关闭 → 密钥也没加载

但注意：**你的私钥文件永远在磁盘上，不会丢。**\
只是 agent 不会自动加载它。

---

# 所以默认情况下：

**重启 / 注销 / 开新终端 → 都需要重新 `ssh-add`**

如果你的私钥没有密码，那你完全可以不依赖 ssh-agent，直接用它也能正常工作，但一般仍建议加载 agent，因为它保证更好的安全习惯。

---

# 要想让它“永久有效”有三种方式

下面给你最干净的三个办法：

---

## ✅ 方案 1：让桌面环境自动管理（最常见）

如果你用的是：

- Ubuntu / GNOME / KDE
- Manjaro GNOME/KDE
- PopOS
- Elementary OS

它们自带**钥匙环系统（Keyring / gnome-keyring / kdewallet）**。

只需要：

### Step 1：把 SSH 密钥加入系统 keyring

```bash
ssh-add ~/.ssh/id_ed25519
```

### Step 2：登录时输入你的系统密码

图形界面会自动加载密钥，不需要手动执行 `eval` 或 `ssh-add`。

这对 99% 桌面 Linux 用户是最佳方式。

---

## ✅ 方案 2：把 ssh-agent 写进 shell 配置（常用）

比如 ZSH：

`~/.zshrc` 写入：

```bash
# Start ssh-agent if not running
if ! pgrep -u "$USER" ssh-agent >/dev/null 2>&1; then
    eval "$(ssh-agent -s)"
fi

ssh-add ~/.ssh/id_ed25519 2>/dev/null
```

Bash 在 `~/.bashrc` 加同样的。

启动新终端就自动加载。

---

## ✅ 方案 3：systemd user 服务（高级永久）

为 ssh-agent 创建用户级 systemd 服务：

```bash
systemctl --user enable ssh-agent
systemctl --user start ssh-agent
```

然后在 `~/.bashrc` 写：

```bash
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
```

这种方式最干净优雅，但需要点 systemd 技巧。

---

# 总结

默认情况：

- `ssh-agent` 不是永久
- `ssh-add` 也不是永久
- 重启 / 注销后，需要重新加载

想永久 → 用 Keyring / 或 .bashrc 自动加载。

---

如果你告诉我你的 Linux 发行版（Ubuntu? Arch? Debian? Manjaro? PopOS? WSL?）\
我可以给你定制一个“最适合你的永久方案”。


#### You:

如果不添加的话，git 就没法使用嘛？

#### ChatGPT:

不添加 `ssh-add`，Git **绝大多数情况下仍然能正常用**。\
真正决定 Git 能不能用的不是 `ssh-add`，而是 **你用的克隆地址类型**。

关键逻辑是这样：

# 1. 分两类：HTTPS vs SSH

Git 有两种访问方式：

---

## **① 你用 HTTPS：根本不需要 ssh-add**

例如：

```
https://github.com/xxx/yyy.git
```

这种方式完全不涉及 SSH 密钥，Git 会问你：

- GitHub Token（以前是账号密码后来改 token）
- 或者你在系统里配置了 credential helper，它会记住你的 token

所以不需要 SSH agent、ssh-add，全程都能用。

---

## **② 你用 SSH：只有特殊情况才需要 ssh-add**

SSH 连接：

```
git@github.com:xxx/yyy.git
```

这里才需要 SSH Key。

但注意——这个也分两种情况：

---

### **Case A：你的私钥 *没有密码***

如果你的密钥（`id_ed25519`）是**无密码私钥**：

你甚至不需要 ssh-agent，Git 可以直接从：

```
~/.ssh/id_ed25519
```

读取密钥文件。

你完全可以不执行：

```
ssh-add
eval "$(ssh-agent)"
```

照样能正常 git clone / pull / push。

---

### **Case B：你的私钥 *有密码***

如果你的 SSH 私钥设置了密码，那么：

- 不用 ssh-add 的情况下，**每次 Git 操作都会弹出密码提示**
- 用 ssh-add 之后只需要输入一次密码，后面不用重复

比如：

```
Enter passphrase for key '/home/you/.ssh/id_ed25519':
```

这就是没 `ssh-add` 的情况。

但 Git **仍然能用**。

---

# 2. 什么情况下 Git 真的会“不能用”？

只有这些情况：

- 你用 **SSH 地址**（git\@github...）
- 且 `.ssh/id_ed25519` 不存在
- 或你把密钥放到别的地方但没配置 `~/.ssh/config`
- 或你设置了奇怪的权限导致 SSH 拒绝加载密钥

否则，Git 都能用。

---

# 3. 所以总结一句话

### **ssh-add 不影响 Git 能不能用，它只是让你少输密码。**

真正影响 Git 能不能用的是：

- 你是否使用 SSH 地址
- 你是否把 SSH 密钥放在默认位置
- GitHub/GitLab 是否信任你的公钥

---

# 4. 最常见的实际情况

你通常只需要这样：

1. 在 GitHub 加入 `id_ed25519.pub`
2. 用 SSH 地址 clone
3. 你的本地 `~/.ssh/id_ed25519` 会自动使用
4. 不用 ssh-add（如果无密码）

绝大多数 Linux 用户从来没敲过 ssh-add，也一直在愉快地 push。

---

如果你告诉我：

- 你用的是 HTTPS 还是 SSH
- 私钥有没有设置密码
- 密钥文件放在哪里

我可以判断你是否需要 ssh-add，以及你现在的 Git 环境是否已经“足够好”。


#### You:

root@racknerd-16a6340:~# ssh -T git@github.com
The authenticity of host 'github.com (140.82.116.4)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi Edge-coordinates! You've successfully authenticated, but GitHub does not provide shell access.


解释

#### ChatGPT:

你看到的这一串输出，是一次非常典型、完全正常的 **SSH 首次连接 + 公钥验证成功** 的流程。\
像在一台新机器上第一次敲门，门卫确认你是谁——然后告诉你“你可以进仓库，但不能进办公室”。

下面把每一句拆开解释，让你理解得透亮。

---

# 1. 首次连接提示：主机真实性未知

```
The authenticity of host 'github.com (140.82.116.4)' can't be established.
```

意思是：\
你的服务器 **第一次连接** GitHub，还不知道 GitHub 的 SSH 公钥指纹，所以要你确认它是不是“真的 GitHub”。

这属于 SSH 的一个安全机制：**防止中间人攻击**。

---

# 2. 显示 GitHub 的指纹

```
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
```

这就是 GitHub 官方的 SSH 公钥指纹。\
你可以查 GitHub 官方文档，完全一致。

所以这是正常的。

---

# 3. 让你确认是否信任它

```
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

你输入了：

```
yes
```

于是 SSH 把 GitHub 的公钥加入你的 known\_hosts。

---

# 4. SSH 记录下来，下次不再问

```
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
```

写入了：

```
~/.ssh/known_hosts
```

之后再次 ssh GitHub 就不会问了。

---

# 5. 最关键的一句：认证成功

```
Hi Edge-coordinates! You've successfully authenticated, but GitHub does not provide shell access.
```

**这句话是“你的 SSH 密钥工作正常”的证明。**

解释：

- 它识别出了你 GitHub 账户 → `Edge-coordinates`
- 你成功用 SSH 私钥通过了认证
- 但 GitHub 的 SSH 服务只能做 Git 操作（clone/push/pull）
- 所以不会让你进入一个 shell

属于正常行为。

---

# 你得到的结论是：

### ✔ GitHub 公钥已加入 known\_hosts

### ✔ 你的 SSH 密钥配置正确

### ✔ GitHub 已正确识别你的账号

### ✔ 你现在可以用 SSH 地址进行 git clone / push / pull

完全正常，表示一切已经配置成功。

---

# 补充：为什么 GitHub 不提供 shell 访问？

GitHub 的 SSH 连接仅用于 Git 传输协议，不提供 shell。\
不管你是谁，结果都是：

```
... but GitHub does not provide shell access.
```

你不可能进入 GitHub 的服务器执行命令，这一点设计得非常合理。

---

如果你想测试 push 是否正常，我可以给你一条安全的测试命令（不会污染任何仓库）。