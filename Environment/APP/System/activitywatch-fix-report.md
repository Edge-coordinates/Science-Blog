# ActivityWatch on Fedora 43 / KDE Plasma 6 Wayland — Fix Report

**Date:** 2026-04-30
**Environment:** Fedora 43, KDE Plasma 6, Wayland session, kwin 6.6.4
**Install location:** `/home/edge/.local/share/activitywatch/` (官方 bundle 直接解壓)

---

## TL;DR

ActivityWatch 在登入後並沒有「真正壞掉」——子模組 (`aw-server`, `aw-watcher-window`, `aw-watcher-afk`) 一直在背景記錄；但 **tray 管理器 `aw-qt` 在 Wayland session 下啟動時 crash**，所以工作列看不到圖示，也無法用 tray 選單控制服務。額外地，autostart 引用的 `Icon=activitywatch` 從未被安裝到 hicolor 主題，KDE 自動啟動面板裡的條目顯示空白圖示。

兩個問題都已修復，登出/登入後 tray 圖示會自動出現。

---

## 動了什麼

| Path | Change |
| --- | --- |
| `~/.local/share/icons/hicolor/512x512/apps/activitywatch.png` | create — 從 `media/logo/logo.png` (512×512) 複製 |
| `~/.local/share/icons/hicolor/128x128/apps/activitywatch.png` | create — 從 `media/logo/logo-128.png` 複製 |
| `~/.local/share/icons/hicolor/scalable/apps/activitywatch.svg` | create — 從 `media/logo/logo.svg` 複製 |
| `~/.local/share/icons/hicolor/icon-theme.cache` | regenerate — `gtk-update-icon-cache -f -t` |
| `~/.config/autostart/aw-qt.desktop` | modify — `Exec=` 前綴加 `env QT_QPA_PLATFORM=xcb`；`Icon=` 改為 freedesktop 名稱 `activitywatch` |

最終 autostart `.desktop` 內容：

```ini
[Desktop Entry]
Name=ActivityWatch
GenericName=Time-tracking application
Comment=Open source time-tracking application with a focus on extensibility and privacy.
Exec=env QT_QPA_PLATFORM=xcb /home/edge/.local/share/activitywatch/aw-qt
Hidden=false
StartupNotify=true
Terminal=false
Type=Application
X-GNOME-Autostart-enabled=true
Version=1.0
Icon=activitywatch
Categories=Utility;
```

---

## 診斷過程

### 1. 先排除「以為設過 systemctl」的記憶

- `~/.config/systemd/user/` 整個目錄不存在
- `systemctl --user list-unit-files | grep activitywatch` 空
- `/usr/lib/systemd/user/` 只有 `plasma-kactivitymanagerd.service`（KDE 自家 kactivitymanagerd，名字相像但跟 ActivityWatch 無關，可能是這個導致記憶混淆）

→ 結論：systemd user unit **從未被裝起來**，過去能跑是靠 XDG autostart。

### 2. autostart 機制本身正常

`~/.config/autostart/aw-qt.desktop` 存在，且 `Exec=` 已是絕對路徑。今天 10:10 的 log 顯示 aw-qt 確實有被登入時拉起來。所以 autostart 不是問題。

### 3. 子模組還在跑、但 aw-qt 自己不見了

```
ps -ef | grep aw-
edge  3524  2386  ...  aw-server/aw-server         (10:10 起)
edge  3603  2386  ...  aw-watcher-window/...       (10:10 起)
edge  3606  2386  ...  aw-watcher-afk/...          (10:10 起)
# 沒有 aw-qt
```

這三個的 PPID = 2386，而 PID 2386 是 `systemd --user`——表示它們本來的父進程 (aw-qt) 死了，被 systemd 收養。子進程沒掛是因為 aw-qt 以 `subprocess.Popen` 啟動它們，並沒有在自身退出時 kill 掉它們。

### 4. 在前景重跑 aw-qt 抓到真正的錯誤

```
$ /home/edge/.local/share/activitywatch/aw-qt
... [INFO] Creating trayicon... (aw_qt.trayicon:208)
/home/edge/.local/share/activitywatch/aw-qt: symbol lookup error:
  /home/edge/.local/share/activitywatch/libQt6WaylandClient.so.6:
  undefined symbol: wl_proxy_marshal_flags
```

**找到了。** 之前 log 永遠停在 `Creating trayicon...` 是因為 dynamic linker 在 trayicon 階段才 lazy-load Qt wayland plugin，符號解析失敗 → 進程被 kernel 直接幹掉，沒有機會寫任何錯誤到 log file。

### 5. 改用 XWayland 驗證假設

```
$ env QT_QPA_PLATFORM=xcb /home/edge/.local/share/activitywatch/aw-qt
... [INFO] Creating trayicon...
... [INFO] Initialized aw-qt and trayicon successfully
```

成功。tray 圖示出現。

---

## 根本原因

### 問題 A — aw-qt 在 Wayland 下 crash

ActivityWatch bundle 內附 `libQt6WaylandClient.so.6`，這個 .so 引用 `wl_proxy_marshal_flags` 這個 symbol（屬於 `libwayland-client`，在 wayland **1.20 之後**才加入）。

Bundle 內**同時**附了一份較舊的 `libwayland-client.so.0`，aw-qt 啟動時 `LD_LIBRARY_PATH` 把 bundle 目錄擺在最前，於是 Qt6WaylandClient 解析 `wl_proxy_marshal_flags` 時去 bundle 裡的舊 libwayland 找——找不到——symbol lookup error。

換句話說這是 **bundle 內部的版本不一致 bug**：打包者把新版 Qt wayland plugin 跟舊版 libwayland 放在一起。在 Wayland session（KDE Plasma 6、GNOME 都是）才會踩到，X11 session 不會，因為不會去 dlopen Qt wayland plugin。

**為什麼 Windows 沒這問題？** Windows 平台根本沒有 Qt wayland plugin，aw-qt 只走 Win32 native，不踩這條程式碼路徑。

**修法：** `QT_QPA_PLATFORM=xcb` 強制 Qt 走 XCB plugin（XWayland），跳過 wayland plugin 的載入。tray icon 走 StatusNotifierItem D-Bus protocol，KDE 對 XWayland 的 SNI 支援很好，視覺體驗跟 native Wayland 沒差。

### 問題 B — `.desktop` 圖示渲染不出來

KDE 自動啟動面板裡 ActivityWatch 條目的圖示空白。

之前 `Icon=` 雖然指了絕對路徑 `/home/edge/.local/share/activitywatch/media/logo/logo.png`，**但 KDE Plasma 6 自動啟動面板不接受絕對路徑**——它只查 freedesktop icon theme 的 name。Bundle 從未把 `activitywatch` 圖示安裝到 `~/.local/share/icons/hicolor/`，所以查不到 → 顯示空白。

**修法：** 把 bundle `media/logo/` 下的三種尺寸 (512×512 PNG, 128×128 PNG, scalable SVG) 安裝到對應的 hicolor 目錄，跑 `gtk-update-icon-cache`，並把 `Icon=` 改回 freedesktop name `activitywatch`。

---

## 解決辦法（最終做法）

```bash
# 1. 安裝 hicolor 圖示
mkdir -p ~/.local/share/icons/hicolor/{512x512,128x128,scalable}/apps
cp ~/.local/share/activitywatch/media/logo/logo.png      ~/.local/share/icons/hicolor/512x512/apps/activitywatch.png
cp ~/.local/share/activitywatch/media/logo/logo-128.png  ~/.local/share/icons/hicolor/128x128/apps/activitywatch.png
cp ~/.local/share/activitywatch/media/logo/logo.svg      ~/.local/share/icons/hicolor/scalable/apps/activitywatch.svg
gtk-update-icon-cache -f -t ~/.local/share/icons/hicolor/

# 2. 修 autostart .desktop
#    將 Exec= 改成 `env QT_QPA_PLATFORM=xcb /home/edge/.local/share/activitywatch/aw-qt`
#    將 Icon= 改成 `activitywatch`
$EDITOR ~/.config/autostart/aw-qt.desktop
```

---

## 驗證

登出/登入後：

- Plasma 工作列 system tray 出現 ActivityWatch 圖示
- 點開 tray 選單能看到 Modules 列表（aw-server / aw-watcher-window / aw-watcher-afk 都 running）
- KDE「系統設定 → 啟動與關機 → 自動啟動」面板裡 ActivityWatch 條目有正確圖示
- `http://localhost:5600` web UI 可訪問

---

## 後續建議

- **bundle 升級時可重新測試 native Wayland**：哪天上游打包修好 Qt wayland plugin 跟 libwayland 的版本錯位，可以拿掉 `QT_QPA_PLATFORM=xcb`。判斷方法：直接 `~/.local/share/activitywatch/aw-qt`（不帶 env），看是否有 `Initialized aw-qt and trayicon successfully`。
- **若想要 systemctl 化管理**（重啟、status、journald log），可改成 systemd user service：建 `~/.config/systemd/user/aw-qt.service`，`ExecStart=env QT_QPA_PLATFORM=xcb /home/edge/.local/share/activitywatch/aw-qt`，`PartOf=graphical-session.target`，`WantedBy=graphical-session.target`，並把 `~/.config/autostart/aw-qt.desktop` 設 `Hidden=true` 避免雙重啟動。本次採用 XDG autostart 簡單方案，未動 systemd。
- **目前的 orphan 子進程**：今天 10:10 起的 server/watcher 由 systemd 收養而非新 aw-qt，新的 aw-qt tray 選單裡的 Stop/Restart 控制不到那批。日常使用無影響（資料都進同一個 sqlite）。如果在意，重開機或手動 `pkill -f 'aw-(server|watcher)'` + 重啟 aw-qt 即可重新接管。

---

## 參考檔案

- Crash log（保留樣本）：`~/.cache/activitywatch/log/aw-qt/aw-qt_2026-04-30T11-37-26.log` 之後的前景輸出
- Bundle desktop template (上游原始)：`/home/edge/.local/share/activitywatch/aw-qt.desktop`
- 修改後的 autostart：`~/.config/autostart/aw-qt.desktop`
