import os
import shutil
import subprocess
import time

def copy_files(source_dir, target_dir):
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    message = f"正在从 {source_dir} 复制文件到 {target_dir}\n"
    
    # 定义不希望复制的文件扩展名
    excluded_extensions = ['.py', '.zip', '.exe', '.mix']
    
    # 复制文件和目录
    try:
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(target_dir, item)

            # 跳过指定的文件夹
            if item in ["_压缩包", "新建文件夹"]:
                message += f"跳过文件夹: {s}\n"
                continue
            
            # 如果是文件且后缀名在排除列表中，则跳过
            if os.path.isfile(s) and any(s.endswith(ext) for ext in excluded_extensions):
                message += f"跳过文件: {s}\n"
                continue

            # 如果是目录则递归复制整个目录，否则复制文件
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)

        message += "文件复制成功完成。"
    except Exception as e:
        message += f"复制过程中发生错误：{e}"

    return message

def show_result_in_new_console(message):
    # 准备新控制台中要执行的Python代码
    code = f"""
import time
print('''{message}''')
time.sleep(1)
"""
    
    # 使用subprocess启动新的Python解释器来运行上面的代码
    subprocess.Popen(['python', '-c', code], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__": 
    source_dir = r"C:\_心灵终结备份\_大杂烩\新开坑\新环境"
    target_dir = r"C:\Fortest"
    
    # 直接复制文件
    result = copy_files(source_dir, target_dir)
    
    # 显示结果
    show_result_in_new_console(result)
