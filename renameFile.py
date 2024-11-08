import os
import re

def rename_files_in_directory(directory):
    # 正则模式匹配两种情况：
    # 1. `simpread-` 后可能跟 `(n 条消息)`（可选）
    # 2. 如果包含 `CSDN_`，则 `_` 后面的内容也会被删除
    pattern = re.compile(r'simpread-(\(\d+ 条消息\))?')
    pattern2 = re.compile(r'_.*')
    for root, _, files in os.walk(directory):
        for filename in files:
            filenameExtension = os.path.splitext(filename)[-1]
            # 使用正则替换匹配内容
            new_filename = pattern.sub('reprint-', filename)

            if 'CSDN' in new_filename:
                new_filename = pattern2.sub('', new_filename) + filenameExtension
            
            if new_filename != filename:  # 只有在文件名发生变化时才重命名
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                
                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")

# 指定要遍历的文件夹路径
directory_path = "./"
rename_files_in_directory(directory_path)
