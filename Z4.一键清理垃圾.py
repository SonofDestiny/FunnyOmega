
import re

# 打开输入文件和输出文件
with open('rules_main_pre.ini', 'r', encoding='utf-8') as infile, open('rules_main.ini', 'w', encoding='utf-8') as outfile:
    for line in infile:
        # 移除每行中的注释部分（以分号开始的内容）
        line = re.sub(r';.*$', '', line).strip()
        
        # 跳过空行或只包含空格/制表符的行
        if line:
            outfile.write(line + '\n')

print("清理完成，输出结果保存在 'rules_main.ini'")
