---
title: WSL 损坏
date: 2025/11/05 16:58:48
categories:
  - - Environment
    - Windows
abbrlink: 293c0a47
---

进入功能，取消勾选所有，重启，再勾上 （不行）

Uninstall then reinstall WSL on Windows 10 (clean way)

https://gist.github.com/4wk-/889b26043f519259ab60386ca13ba91b

# Uninstall then reinstall WSL on Windows 10 (clean way)
## Background
I've been using `wsl` (version 2) with [`genie` mod](https://gist.github.com/djfdyuruiry/6720faa3f9fc59bfdf6284ee1f41f950) for years without issue, but one day, Windows 10 [finally catch up](https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/) on `wsl` Windows **11** features and gives us a way to use `systemD` natively. 

I wanted to use the new "right way" to enable `systemD` on **Windows Subsystem for Linux** (without `genie`), and I also had a (probably related) infinite [Windows RemoteApp error](https://user-images.githubusercontent.com/1439550/210227714-d15c1eac-9138-48c1-a03f-157fd90fec6c.png) poping in.

## Fixing it

### A - Uninstall wsl and related stuff
1) **In powershell (as admin)**
```powershell
# list all installed distros
wsl -l -v

# destroy distros
wsl --unregister Ubuntu
wsl --unregister Debian # and so on
```

&nbsp;

2) **In Settings > Apps > Apps & Features**
- search for `Ubuntu` (then `Debian`, etc), and if something is found, click on **uninstall**
- search for `Linux`, and if something is found, click on **uninstall** on all results

&nbsp;

3) **In Start Menu > Turn Windows Features on or off**
- Untick `Virtual Machine Platform` checkbox
- Untick `Windows Subsystem for Linux` checkbox

&nbsp;

4) **Reboot**
- I might have reboot between step **2)** and **3)** as well.

----

### B - Re-install and configure wsl to use `systemD`
The process of installing wsl have become [super straightforward](https://learn.microsoft.com/en-us/windows/wsl/install).

1) **Installing wsl - In powershell (as admin)**
```powershell
# install wsl
wsl --install
```
Then **reboot** and **wait for the Ubundu installation to complete** and ask for username (it might takes some time).

&nbsp;

3) **Optional: Changing distribution - In powershell (as admin)**
```powershell
# list available distributions
wsl --list --online

# install favorite distro
wsl --install -d Debian

# set Debian as default
wsl --set-default Debian
```
**NB:** `wsl --set-default-version 2` is not needed anymore.

&nbsp;

3) **Enabling systemD support - Inside wsl**
- Launch your distribution
- Edit `/etc/wsl.conf` (or create the file if it doesn't exist)
```ini
[boot]
systemd=true

# Optional: remove windows from PATH (autocompletion)
[interop]
appendWindowsPath = false
```

&nbsp;

4) **Clean rebooting - In powershell (as admin)**
```powershell
# clean shutdown
wsl --shutdown
```

**Great success!** :tada: You have now enabled `systemD` in `wsl` natively. You can test it with `sudo systemctl status time-sync.target` (inside your Linux distribution).

----

**NB:** System wide configuration file `.wslconfig` will not be deleted/reseted, you would have to do it manually.

Let me know if I missed anything, I'll be glad to update this gist.