import re

def process_ini_file(input_file, output_file):
    # 正则表达式用于提取 UIName 行的内容
    ui_name_pattern = re.compile(r'\bUIName=\(：([^)]*)\)')
    money_amount_pattern = re.compile(r'^Money\.Amount=(-?\d+)')
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        ui_name_lines = []
        current_header = None
        money_amount = None
        
        for line in lines:
            line = line.strip()
            
            # 检查是否是以 ;# 开头的行
            if line.startswith(';#'):
                if current_header:
                    # 如果有之前的 header，先处理并写入
                    outfile.write(f'{current_header}\n')
                    if money_amount is not None:
                        amount_value = int(money_amount)
                        if amount_value <= 0:
                            outfile.write(f'消耗金钱：{abs(amount_value)}\n')  # 负值或0显示绝对值
                        else:
                            outfile.write(f'提供金钱：{amount_value}\n')
                    for ui_line in ui_name_lines:
                        outfile.write(f'{ui_line}\n')
                    outfile.write('\n')
                
                # 更新当前 header 和重置 ui_name_lines
                current_header = line
                ui_name_lines = []
                money_amount = None  # 重置金钱金额
                
            # 查找 Money.Amount 行并提取金额
            elif money_amount is None and line.startswith('Money.Amount='):
                match = money_amount_pattern.search(line)
                if match:
                    money_amount = match.group(1)
            
            # 查找 UIName 行并提取内容
            if 'UIName=(' in line:
                match = ui_name_pattern.search(line)
                if match:
                    ui_name_content = match.group(1)
                    ui_name_lines.extend(ui_name_content.split('\\n'))
        
        # 写入最后一组数据
        if current_header:
            outfile.write(f'{current_header}\n')
            if money_amount is not None:
                amount_value = int(money_amount)
                if amount_value <= 0:
                    outfile.write(f'消耗金钱：{abs(amount_value)}\n')  # 负值或0显示绝对值
                else:
                    outfile.write(f'提供金钱：{amount_value}\n')
            for ui_line in ui_name_lines:
                outfile.write(f'{ui_line}\n')

# 调用函数
process_ini_file('_developing.ini', '【魔杖系统说明书】.txt')
