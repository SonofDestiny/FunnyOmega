# 定义替换字典
replacements = {
    "PowerBases": "Power.Bases",
    "PowerMults": "Power.Mults",
    "AType": "After.Type",
    "EType": "Effect.Type",
    "EDataPack": "Effect.DataPack",
    "ESelf": "Effect.Self",
    "EDelay": "Effect.Delay",
    "EOwner": "Effect.Owner",
    "EModes": "Effect.Modes",
    "EWarheads": "Effect.Warheads",
    "EWeapons": "Effect.Weapons",
    "ECounts": "Effect.Counts",
    "BuffInitTypes": "BuffInit.Types",
    "BuffAddTypes": "BuffAdd.Types",
    "BuffAddCheck": "BuffAdd.Check",
    "BuffAddSets": "BuffAdd.Sets",
    "AttachEffectAttachTypes": "AttachEffect.AttachTypes",
    "AttachEffectAnimation": "AttachEffect.Animation",
    "AttachEffectDuration": "AttachEffect.Duration",
}

# 读取文件并进行替换
input_file = '____developing.ini'
output_file = '_developing.ini'  # 输出文件名

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.readlines()

# 替换内容
for i in range(len(content)):
    for old, new in replacements.items():
        content[i] = content[i].replace(old, new)

# 写入修改后的内容到新文件
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(content)

print("替换完成，结果已保存到", output_file)
