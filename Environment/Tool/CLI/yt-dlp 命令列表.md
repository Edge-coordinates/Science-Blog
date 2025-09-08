---
title: yt-dlp 命令列表
date: 2025/4/26 17:44:47
categories:
  - - Environment
    - Tool
    - CLI
abbrlink: f29fca0e
---

`yt-dlp` 是一个强大的命令行工具，用于下载 YouTube 和其他视频网站的音视频资源。

下面是 `yt-dlp` 的常用命令参数列表和详解（已按用途分类）：

---

## 🌐 基本用法

```bash
yt-dlp [OPTIONS] URL
```

示例：
```bash
yt-dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

## 🎯 下载选项

| 参数 | 说明 |
|------|------|
| `-f` 或 `--format` | 指定视频/音频格式（详细见下方格式选择） |
| `-o` 或 `--output` | 自定义输出文件名和路径，例如 `-o "%(title)s.%(ext)s"` |
| `--download-sections` | 下载特定时间段，例如 `"*00:01:00-00:02:00"` |
| `--playlist-items` | 指定播放列表中的具体项，如 `--playlist-items 1,3,5-7` |
| `--no-playlist` | 禁止下载整个播放列表，只下载链接指定的视频 |
| `--yes-playlist` | 强制将链接作为播放列表处理 |
| `--no-part` | 不生成 `.part` 临时文件 |
| `--no-overwrites` | 如果文件已存在则跳过下载 |

---

## 🎵 音频提取

| 参数 | 说明 |
|------|------|
| `--extract-audio` 或 `-x` | 提取音频 |
| `--audio-format mp3` | 指定音频格式（如 mp3、aac、flac、m4a、opus） |
| `--audio-quality 0` | 音频质量（0 是最好） |
| `--postprocessor-args` | 传参给 FFmpeg，如 `--postprocessor-args "-af volume=1.5"` |

---

## 📺 格式选择（非常强大）

```bash
yt-dlp -F URL
```

显示可用的格式代码，然后可以用：

```bash
yt-dlp -f 137+140 URL
```

`137` 表示视频，`140` 表示音频，`+` 表示合并。

可选格式模板：

```bash
-f "bv*+ba/best"
```

意思是：选择最佳视频流 (bv) + 最佳音频流 (ba)，否则 fallback 为 best。

---

## 🌍 代理设置

| 参数 | 说明 |
|------|------|
| `--proxy` | 使用 HTTP/HTTPS/SOCKS 代理，例如 `--proxy socks5://127.0.0.1:1080` |
| `--geo-bypass` | 绕过地理限制（默认开启） |
| `--geo-bypass-country` | 模拟国家，如 `--geo-bypass-country US` |

---

## 🔐 账号与会员权限

| 参数 | 说明 |
|------|------|
| `-u` 或 `--username` | 登录用户名 |
| `-p` 或 `--password` | 密码 |
| `--cookies` | 通过浏览器导出的 cookies.txt 进行登录 |
| `--netrc` | 使用 `.netrc` 文件登录 |

---

## 💬 字幕下载

| 参数 | 说明 |
|------|------|
| `--write-subs` | 下载字幕 |
| `--write-auto-subs` | 下载自动生成的字幕 |
| `--sub-langs` | 指定语言，例如 `--sub-langs en,zh-Hans` |
| `--sub-format` | 指定字幕格式，如 `--sub-format "srt/vtt"` |

---

## 🔁 后处理

| 参数 | 说明 |
|------|------|
| `--merge-output-format` | 合并后输出格式，如 `mp4` 或 `mkv` |
| `--embed-subs` | 将字幕嵌入视频 |
| `--embed-thumbnail` | 嵌入缩略图 |
| `--embed-metadata` | 嵌入元数据 |
| `--remux-video mp4` | 使用 FFmpeg 重新封装为 MP4 格式 |

---

## 💾 文件名模板变量

| 变量 | 含义 |
|------|------|
| `%(title)s` | 视频标题 |
| `%(uploader)s` | 上传者 |
| `%(upload_date)s` | 上传日期 |
| `%(id)s` | 视频 ID |
| `%(ext)s` | 文件扩展名 |

示例：
```bash
-o "%(upload_date)s - %(title)s.%(ext)s"
```

---

## 🛠 实用选项

| 参数 | 说明 |
|------|------|
| `-N` 或 `--concurrent-fragments` | 并发下载片段数量，加快速度 |
| `--no-check-certificate` | 跳过 HTTPS 证书验证 |
| `--sleep-interval` | 每次下载之间休眠秒数（防止封锁） |
| `--limit-rate 1M` | 限速为 1MB/s |
| `--no-mtime` | 不保留文件原时间戳 |
| `--write-info-json` | 下载视频信息 json 文件 |
| `--skip-download` | 不下载视频，只提取信息/字幕等 |

---