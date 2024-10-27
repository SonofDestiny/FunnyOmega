# 忽略护甲、国家注册表，这两个的顺序matters



# import random
# 
# def shuffle_ini(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
# 
#     blocks = {}
#     current_block = None
#     ignore_blocks = ['[ArmorTypes]', '[DataPackTypes]', '[Countries]']  # 要忽略的块
# 
#     # 解析文件，将块和对应的键值对保存到字典中
#     for line in lines:
#         line = line.strip()
#         if line.startswith('[') and line.endswith(']'):  # 识别块名
#             current_block = line
#             blocks[current_block] = []
#         elif current_block and '=' in line:  # 识别键值对
#             blocks[current_block].append(line)
# 
#     # 将块及其键值对顺序打乱，忽略指定的块
#     shuffled_blocks = list(blocks.keys())
#     random.shuffle(shuffled_blocks)
# 
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for block in shuffled_blocks:
#             f.write(f"{block}\n")
#             if block in ignore_blocks:
#                 # 对于忽略的块，保持键值对顺序
#                 for entry in blocks[block]:
#                     f.write(f"{entry}\n")
#             else:
#                 # 对于其他块，打乱键值对顺序
#                 entries = blocks[block]
#                 random.shuffle(entries)
#                 for entry in entries:
#                     f.write(f"{entry}\n")
#             f.write("\n")
# 
#     print(f"{file_name} 中的块和键值对已随机打乱，忽略 {', '.join(ignore_blocks)} 块的顺序")
# 
# # 调用函数处理rulesmo.ini
# shuffle_ini('rulesmo.ini')
