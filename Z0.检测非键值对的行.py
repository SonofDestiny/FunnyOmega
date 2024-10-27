import os

def is_empty_or_comment(line):
    """检查是否为空行或注释行"""
    stripped = line.strip()
    return not stripped or stripped.startswith(';')

def is_block_header(line):
    """检查是否为块头行（即以[开头，并且[和]的数量相同）"""
    stripped = line.strip()
    return stripped.startswith('[') and stripped.count('[') == stripped.count(']') and stripped.count('[') > 0

def is_key_value_pair(line):
    """检查是否符合'键=值'格式"""
    # Remove comments from the line
    line = line.split(';', 1)[0].strip()
    return '=' in line and len(line.split('=', 1)) == 2

def process_ini_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        errors = []
        
        for line_num, line in enumerate(file, start=1):
            stripped_line = line.strip()
            
            # Ignore empty lines, comment lines, and block header lines
            if is_empty_or_comment(stripped_line) or is_block_header(stripped_line):
                continue
            
            # If not a key-value pair, record it
            if not is_key_value_pair(stripped_line):
                errors.append(f"File: {file_path}, Line {line_num}: {line.strip()}")
        
        return errors

def process_all_ini_files():
    output_file = '_DrytronLog.ini'
    ini_files = [f for f in os.listdir() if f.endswith('.ini') and f != output_file]  # Ignore _DrytronLog.ini
    all_errors = []
    
    for ini_file in ini_files:
        errors = process_ini_file(ini_file)
        if errors:
            all_errors.extend(errors)
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        if all_errors:
            out_file.write("\n".join(all_errors))
        else:
            out_file.write("没有不满足格式的行存在")

if __name__ == "__main__":
    process_all_ini_files()
