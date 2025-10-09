---
title: whisper
date: 2025/10/08 18:54:50
updated: 2025/10/08 18:54:51
categories:
  - - Environment
    - Tool
    - CLI
abbrlink: 76e12b8d
---

ffmpeg -i input_video.mp4 output_audio.mp3 

then 

whisper output_audio.mp3

## How to install whisper

pip install --upgrade pip setuptools wheel
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install openai-whisper

