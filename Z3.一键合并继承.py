import re

# 定义文件路径
develop_file = '_developing.ini'
other_files = ['rules_changed.ini', 'rulesmo_proto.ini', 'rules_yr.ini', 'rules_battleunit.ini']
output_file = 'rules_main_pre.ini'

# 读取所有文件并存储块
def read_blocks_from_file(file_path):
    blocks = []
    current_block_name = None
    current_block = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 匹配块头
            block_match = re.match(r'\[([^\]]+)\](?::\[([^\]]+)\])?', line)
            if block_match:
                # 保存上一个块
                if current_block_name:
                    blocks.append((current_block_name, current_block))
                
                # 初始化新块
                current_block_name = block_match.group(1)
                current_block = [line]
            else:
                current_block.append(line)
        
        # 保存最后一个块
        if current_block_name:
            blocks.append((current_block_name, current_block))
    
    return blocks

# 合并继承逻辑
def merge_inheritance(n_block_name, n_block, all_blocks):
    header = n_block[0].strip()
    match = re.match(r'\[([^\]]+)\]:\[([^\]]+)\]', header)
    
    if match:
        n_name = match.group(1)
        m_name = match.group(2)
        
        # 将块头改为M类块头
        n_block[0] = f'[{n_name}]\n'
        
        # 初始化存储继承的键值对的字典
        inherited_keys = {}

        # 遍历所有块，找到名称为 m_name 的块并继承其键值对
        for block_name, block in all_blocks:
            if block_name == m_name:
                for line in block:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        inherited_keys[key.strip()] = value.strip()
        
        # 将继承的键值对合并进N类块
        n_keys = {line.split('=')[0].strip() for line in n_block if '=' in line}
        new_lines = []
        for key, value in inherited_keys.items():
            if key not in n_keys:
                new_lines.append(f'{key}={value}\n')
        
        # 找到继承者的最后一行属性并添加继承的属性
        for i in range(len(n_block) - 1, -1, -1):
            if '=' in n_block[i]:
                n_block = n_block[:i+1] + new_lines + n_block[i+1:]
                break
        else:
            n_block.extend(new_lines)
    
    return n_block

# 读取_developing.ini和所有其他文件的所有块
develop_blocks = read_blocks_from_file(develop_file)
all_blocks = develop_blocks.copy()  # 将 _developing.ini 本身作为继承源之一
for file in other_files:
    all_blocks.extend(read_blocks_from_file(file))  # 其他文件的块追加进来

# 处理_developing.ini里的N类块并进行继承合并
with open(output_file, 'w', encoding='utf-8') as output:
    for block_name, block_lines in develop_blocks:
        # 检查是否为N类块
        if re.match(r'\[([^\]]+)\]:\[([^\]]+)\]', block_lines[0]):
            # 进行继承合并，并将N类块头变为M类块头
            merged_block = merge_inheritance(block_name, block_lines, all_blocks)
            output.writelines(merged_block)
        else:
            # 写入未修改的M类块
            output.writelines(block_lines)
