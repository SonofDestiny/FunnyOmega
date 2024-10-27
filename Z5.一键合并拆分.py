import os

# 读取并合并[#include]中的所有文件，包括rulesmo_proto.ini本身
def merge_include_files():
    include_file = 'rulesmo_proto.ini'
    temp_file = 'rules_all_temp.ini'
    
    with open(include_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 查找[#include]部分并读取文件列表
    include_section = False
    file_list = [include_file]  # 首先将rulesmo_proto.ini本身作为第一个文件
    for line in lines:
        line = line.strip()
        if line.startswith("[#include]"):
            include_section = True
            continue
        if include_section and "=" in line:
            file_name = line.split('=')[-1].strip()
            if os.path.exists(file_name):
                file_list.append(file_name)
            else:
                print(f"Warning: file '{file_name}' not found.")
        elif include_section and "[" in line:
            break
    
    # 合并文件内容并加注释
    with open(temp_file, 'w', encoding='utf-8') as outfile:
        for file_name in file_list:
            with open(file_name, 'r', encoding='utf-8') as infile:
                # 添加注释标记文件来源
                outfile.write(f"; 来源文件: {file_name}\n")
                # 写入文件内容
                outfile.write(infile.read() + "\n")
    
    print(f"Files merged into {temp_file}")

# 对合并后的文件执行处理并生成rulesmo.ini
def process_merged_file():
    input_file = 'rules_all_temp.ini'
    output_file = 'rulesmo.ini'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks = {}
    current_block = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        
        if line.startswith('[') and line.endswith(']'):  # 识别块名
            current_block = line
            if current_block not in blocks:
                blocks[current_block] = {'entries': {}, 'plus_entries': []}
        elif '=' in line and current_block:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            line = f"{key}={value}"
            if key == '+':
                # 如果键是'+'，将此行添加到plus_entries中
                blocks[current_block]['plus_entries'].append(line)
            else:
                # 如果键已经存在，覆盖其值
                blocks[current_block]['entries'][key] = value

    # 生成最终的rulesmo.ini
    with open(output_file, 'w', encoding='utf-8') as f:
        for block, data in blocks.items():
            f.write(f"{block}\n")
            # 先写入普通条目
            for key, value in data['entries'].items():
                f.write(f"{key}={value}\n")
            # 然后写入'+'键条目
            for line in data['plus_entries']:
                f.write(f"{line}\n")
            f.write("\n")
    
    print(f"Processed {input_file} into {output_file}")

    # 删除rulesmo.ini中的[#include]块
    remove_include_block(output_file)

    # 清除rulesmo.ini中的注释并去除等号两侧的空格
    clean_output_file(output_file)

# 清除最终rulesmo.ini中的注释，并去除等号两侧的空格
def clean_output_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            # 清除注释部分
            line = line.split(';', 1)[0].strip()
            if line:
                # 去除等号两侧的空格和制表符
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    line = f"{key}={value}"
                f.write(line + '\n')

# 删除[#include]块
def remove_include_block(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_name, 'w', encoding='utf-8') as f:
        in_include_block = False
        for line in lines:
            line = line.strip()
            if line.startswith("[#include]"):
                in_include_block = True
            elif line.startswith('[') and line.endswith(']'):
                if in_include_block:
                    in_include_block = False
                f.write(line + '\n')
            elif not in_include_block:
                f.write(line + '\n')
    
    print(f"Removed [#include] block from {file_name}")

# 主函数：先合并，再处理
def main():
    merge_include_files()
    process_merged_file()

if __name__ == "__main__":
    main()
