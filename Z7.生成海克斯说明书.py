import re

def process_ini_file(input_file, output_file):
    # 正则表达式用于提取 UIName 行的内容
    ui_name_pattern = re.compile(r'UIName=\(：(.*)')
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        current_header = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # 检查是否是以 ;@ 或 ;$ 开头的行
            if line.startswith(';@') or line.startswith(';$'):
                if current_header:
                    outfile.write('\n')  # 为上一个block和下一个block之间添加空行
                
                # 处理新的 header
                current_header = line[:2] + line[2:].strip()
                outfile.write(f'{current_header}\n')
                
                # 向下查找第一个 UIName= 行
                for next_line in lines[i+1:]:
                    next_line = next_line.strip()
                    if next_line.startswith('UIName='):
                        match = ui_name_pattern.search(next_line)
                        if match:
                            # 把 UIName 中的内容提取出来，并替换 \n 为换行符
                            ui_name_content = match.group(1).replace('\\n', '\n')
                            outfile.write(f'{ui_name_content}\n')
                            break
                else:
                    continue  # 如果没有找到 UIName= 行，则跳过当前 block

# 调用函数处理 _developing.ini 文件并生成结果
process_ini_file('_developing.ini', '【海克斯模式说明书】.txt')

