---
title: font-setup-report
date: 2026/08/17 13:15:15
categories:
  - - Environment
    - Linux
abbrlink: 3e07a109
---
# 字體配置變更報告

時間：2026-04-30
系統：Fedora 43 KDE Plasma 6.6.4 (Wayland)
備份目錄：`~/.font-config-backup/20260430-120735/`

---

## 目標

把系統全局默認字體換成 **CaskaydiaMono Nerd Font**（拉丁/代碼）+
**Sarasa Gothic TC**（繁中），解決原來 Noto Sans CJK 在 Bold 字重下繁中
"糊成一團"的問題；同時修復 Ghostty 沒加粗、沒上色的配置缺失。

範圍覆蓋：KDE 桌面、Konsole、Ghostty、GTK 應用、Flatpak 沙盒應用。
未動：VS Code / Cursor（用戶確認無問題，且兩者各有獨立字體設定）。

---

## 關鍵發現（執行前的診斷）

1. **CascadiaMono 完全不含 CJK 字形**（fc-scan 驗證：CJK Unified
   Ideographs 0/20992，Hiragana 0/96，Hangul 0/11184）。所以 Chinese
   渲染必須由 fallback 字體承擔。原以爲它支持中文是 fontconfig fallback
   到 Noto Sans CJK 在背後工作的錯覺。
2. 系統原本繁中 Bold 解析到 `NotoSansCJK-VF.ttc Bold` —— 是真實 Bold，
   不是合成。問題出在 Variable Font 在小字號 + 繁中 + Bold 三重壓力下
   hinting 退化。
3. Ghostty `~/.config/ghostty/config` 只有一行 `shell-integration = zsh`，
   完全沒設字體 / 主題 / bold 行爲。
4. Konsole 沒有自定義 profile，跑系統默認。
5. Plasma 6 + `kwriteconfig6` 可用。
6. 已裝 7 個 Flatpak 應用（DataGrip / Spotify / GoldenDict / PodmanDesktop
   / Typora / Inkscape / LocalSend），需要 fonts 目錄掛載授權才能看到
   新字體。

---

## 安裝的字體

### CaskaydiaMono Nerd Font（來源：`~/Downloads/CascadiaMono.zip`）
- 路徑：`~/.local/share/fonts/CaskaydiaMono/`
- 數量：36 個 ttf
- 變體：
  - **Nerd Font**（雙寬圖標，通用）
  - **Nerd Font Mono**（單寬圖標，終端嚴格對齊）
  - **Nerd Font Propo**（比例間距，UI 用）
  - 各含 12 個字重/斜體（ExtraLight / Light / SemiLight / Regular /
    SemiBold / Bold + 各自 Italic）

### Sarasa Gothic（來源：GitHub `be5invis/Sarasa-Gothic` v1.0.37）
- 路徑：`~/.local/share/fonts/SarasaGothic/`
- 數量：4 個 ttc（`Sarasa-{Regular,Bold,Italic,BoldItalic}.ttc`，總 322MB）
- 每個 ttc 內含全部區域（TC/SC/J/HC/CL）× 全部變體（Gothic/Mono/Term/
  Fixed/UI/Slab）
- 我們實際使用的是 TC 子集中的：
  - **Sarasa Gothic TC**（比例，UI 用）
  - **Sarasa Mono TC**（等寬 1.0× 配 Cascadia Mono）

---

## 配置變更

### 1. `~/.config/fontconfig/fonts.conf`（新建）
```
generic family aliases:
  monospace  → CaskaydiaMono Nerd Font Mono → Sarasa Mono TC → Noto fallback
  sans-serif → CaskaydiaMono Nerd Font Propo → Sarasa Gothic TC → Noto fallback
  serif      → Noto Serif → Noto Serif CJK TC

per-language strong bindings：
  zh-tw  monospace  → Sarasa Mono TC
  zh-tw  sans-serif → Sarasa Gothic TC
  zh-tw  serif      → Noto Serif CJK TC
  zh-hk  → Sarasa *-HC
  zh-cn  → Sarasa *-SC
  ja     → Sarasa *-J

global rules：
  embolden = false       (禁用合成加粗，避免雙重加粗導致糊)
  embeddedbitmap = false
  hinting = slight, antialias = true, lcdfilter = lcddefault
```

### 2. `~/.config/kdeglobals`（修改 6 個鍵）
| Key | Value |
| --- | --- |
| `[General] font` | CaskaydiaMono Nerd Font Propo, 10 (Regular) |
| `[General] fixed` | CaskaydiaMono Nerd Font Mono, 10 (Regular) |
| `[General] smallestReadableFont` | CaskaydiaMono Nerd Font Propo, 8 (Regular) |
| `[General] toolBarFont` | CaskaydiaMono Nerd Font Propo, 10 (Regular) |
| `[General] menuFont` | CaskaydiaMono Nerd Font Propo, 10 (Regular) |
| `[WM] activeFont` | CaskaydiaMono Nerd Font Propo, 10 (Bold) |

### 3. Konsole
- `~/.config/konsolerc` 加 `[Desktop Entry] DefaultProfile=Cascadia.profile`
- `~/.local/share/konsole/Cascadia.profile`（新建）：
  - Font = CaskaydiaMono Nerd Font Mono, 11pt
  - BoldIntense = true
  - UseFontLineCharacters = true
  - HistorySize = 10000

### 4. Ghostty `~/.config/ghostty/config`（從 1 行擴展爲完整配置）
```
shell-integration = zsh

font-family             = CaskaydiaMono Nerd Font Mono
font-family-bold        = CaskaydiaMono Nerd Font Mono
font-family-italic      = CaskaydiaMono Nerd Font Mono
font-family-bold-italic = CaskaydiaMono Nerd Font Mono
font-size               = 11

font-synthetic-style = no-bold,no-italic,no-bold-italic
bold-is-bright       = false
theme                = catppuccin-mocha
```
這裏 `bold-is-bright = false` 是關鍵 —— 之前"沒加粗"是因爲 Ghostty
默認把 bold 屬性當成"變亮顏色"，我們強制它走真實 Bold 字體文件。

### 5. GTK 應用（gsettings org.gnome.desktop.interface）
| Key | Before | After |
| --- | --- | --- |
| font-name | `Noto Sans 10` | `CaskaydiaMono Nerd Font Propo 10` |
| monospace-font-name | `Noto Sans Mono 10` | `CaskaydiaMono Nerd Font Mono 10` |
| document-font-name | `Noto Sans 10` | `CaskaydiaMono Nerd Font Propo 10` |

### 6. Flatpak（7 個應用全部加 read-only 掛載）
```
flatpak override --user --filesystem=~/.local/share/fonts:ro <app>
```
應用：`com.jetbrains.DataGrip` / `com.spotify.Client` /
`io.github.xiaoyifang.goldendict_ng` / `io.podman_desktop.PodmanDesktop` /
`io.typora.Typora` / `org.inkscape.Inkscape` / `org.localsend.localsend_app`

---

## 驗證結果（fc-match）

```
默認 monospace            → CaskaydiaMono Nerd Font Mono Regular ✓
繁中 monospace            → Sarasa Mono TC Regular              ✓
繁中 monospace Bold       → Sarasa Mono TC Bold (real)          ✓
默認 sans-serif           → CaskaydiaMono Nerd Font Propo Regular ✓
繁中 sans-serif           → Sarasa Gothic TC Regular            ✓
繁中 sans-serif Bold      → Sarasa Gothic TC Bold (Sarasa-Bold.ttc) ✓
繁中 serif                → Noto Serif CJK TC Regular           ✓
```

**繁中 Bold 從原來的 NotoSansCJK-VF（VF hinting 退化）切到了
Sarasa-Bold.ttc（手工逐像素 hinting）—— 這是本次修復的核心。**

---

## 備份與還原

### 備份內容（`~/.font-config-backup/20260430-120735/`）
| 文件 | 用途 |
| --- | --- |
| `manifest.json` | 描述變更全貌 |
| `kdeglobals.bak` | 原 kdeglobals 完整副本 |
| `konsolerc.bak` | 原 konsolerc 完整副本 |
| `ghostty-config.bak` | 原 ghostty config（只有 shell-integration = zsh） |
| `.fontsconf-was-absent` | 標記文件：原本沒有 fonts.conf（還原時要刪除新建的） |
| `gsettings.json` | 三個 GTK font-name 鍵的原始值 |
| `flatpak-overrides-global.txt` | 全局 flatpak 配置原樣 |
| `flatpak-per-app/<app>.txt` | 每個應用的原始 override（7 個） |
| `restore.ts` | Bun TypeScript 還原腳本 |

### 還原命令
```bash
# 完整還原（默認）
bun ~/.font-config-backup/20260430-120735/restore.ts

# 還原配置但保留字體文件（之後想自己選用）
bun ~/.font-config-backup/20260430-120735/restore.ts --keep-fonts

# 預演（不實際修改任何東西）
bun ~/.font-config-backup/20260430-120735/restore.ts --dry-run
```
restore.ts 已用 `--dry-run` 驗證可正常運行。

---

## 後續事項

1. **重啓會話讓 Plasma shell 拾取新字體**：
   ```bash
   kquitapp6 plasmashell && kstart plasmashell &
   ```
   或者直接登出再登錄。已開的 Konsole / Ghostty / Firefox / Typora
   窗口需要關了重開。

2. **Ghostty 主題**改：編輯 `~/.config/ghostty/config` 最後一行，
   `ghostty +list-themes` 看可選項。

3. **DataGrip**（JetBrains Flatpak）字體要在 IDE 內 Settings → Editor →
   Font 裏手動選 `CaskaydiaMono Nerd Font Mono`。權限掛載已做完。

4. **可選清理**：`~/Downloads/Sarasa-TTC-1.0.37.7z`（143MB）已用完
   可刪。

5. **如果繁中加粗仍然偏糊**：可以再加一條 fontconfig 規則把繁中 Bold
   重映射到 Medium 字重（Sarasa 有 Medium/SemiBold 字重可選）。在
   實際使用幾天後再評估。
