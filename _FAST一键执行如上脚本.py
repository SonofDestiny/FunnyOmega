import subprocess

# 定义脚本文件名
scripts = [
    'Z0.检测非键值对的行.py',
    'Z1.一键还原自定义写法.py',
    'Z2.一键全注册.py',
    'Z3.一键合并继承.py',
    'Z4.一键清理垃圾.py',
    'Z5.一键合并拆分.py',
    'Z6.一键全部乱序.py',
    'Z7.生成海克斯说明书.py',
    'Z8.生成魔杖说明书.py',
    'Z9.一键应用到测试游戏目录.py'
]

# 依次执行每个脚本
for script in scripts:
    try:
        print(f"正在执行脚本: {script}")
        result = subprocess.run(['python', script], check=True)
        print(f"{script} 执行完毕。\n")
    except subprocess.CalledProcessError as e:
        print(f"执行脚本 {script} 时出错: {e}")
        break  # 如果某个脚本出错，停止执行后续脚本
    except FileNotFoundError as e:
        print(f"无法找到脚本文件 {script}: {e}")
        break  # 如果脚本文件不存在，停止执行

print("所有脚本执行完成。")
