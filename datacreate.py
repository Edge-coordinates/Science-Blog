import os
import datetime


fapath = os.path.split(os.path.realpath(__file__))[0]

for folderName, subfolders, filenames in os.walk(fapath):
    for filename in filenames:
        # 获取前缀（文件名称）
        tname = os.path.splitext(filename)[0]
        if os.path.splitext(filename)[-1][1:] == "md" :

            rpath = os.path.relpath(folderName, fapath) # 获取相对路径
            filepath = rpath + "\\" + filename # 获取文件的相对路径
            # print(filepath) # 测试路径是否正确
            TFile = open(filepath, 'r', encoding='utf-8') # 打开文件(只读)
            conntent = TFile.readlines() # 按行读取
            TFile.close() # 关闭文件

            if(conntent[0] == "---\n"): # 处理过的
                conntent.insert(2,"date: " + datetime.date.today().strftime('%Y/%m/%d') + "\n")
                # print(conntent)
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()

            else:
                # conntent = fm_dev(rpath, tname) + ["\n\n"] + conntent
                # TFile = open(filepath, 'w', encoding='utf-8')
                # TFile.writelines(conntent)
                # TFile.close()
                continue