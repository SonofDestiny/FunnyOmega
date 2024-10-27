

import os
import shutil

# 要复制的文件和文件夹列表
items_to_copy = [
    "Client", "INI", "MapsMO", "Resources", 
    "_不公平一块地说明.png", "【魔杖系统说明书】.txt", "【海克斯模式说明书】.txt", "_鸣谢.txt", "_优化说明.txt", "aimo.ini", "aimo_ex.ini", 
    "artmo.ini", "artmo_develop.ini", "art_expand.ini", "KeyboardMD.ini", "更新日志.txt",
    "expandmo50.mix", "expandmo51.mix", "expandmo52.mix", "game.fnt", "【PVP思路详解】by暗黑大魔王小豪猪.zip",
    "IHCore.dll", "IHCore.dll.inj", "Phobos.dll", "pipbrd.shp", "pips.shp", 
    "RA2MO.ini", "rulesmo.ini", "shroud.shp", "SIWinterIsComing#184.dll", "_避免弹窗说明.txt",
    "thememo.ini", "soundmo.ini", "stringtable10.csf", "uimd.ini", "version", "更新日志"
]

# 当前目录
current_dir = os.getcwd()

# 目标文件夹名
output_dir = os.path.join(current_dir, "_压缩包")

# 创建目标文件夹
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 复制文件和文件夹
for item in items_to_copy:
    source_path = os.path.join(current_dir, item)
    destination_path = os.path.join(output_dir, item)
    
    # 检查是文件还是文件夹
    if os.path.isdir(source_path):
        # 如果目标文件夹已存在，则删除它再复制
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        # 复制文件夹及其内部所有内容
        shutil.copytree(source_path, destination_path)
    elif os.path.isfile(source_path):
        # 复制文件，如果同名文件已存在则覆盖
        shutil.copy2(source_path, destination_path)
    else:
        print(f"未找到 {item}，跳过该项。")

print("文件复制并覆盖完成。")
