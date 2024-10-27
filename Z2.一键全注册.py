# （把_developing里全部对象注册到rules_register）

import re
import os
from collections import defaultdict

# Initialize dictionaries to store registry data
registry = defaultdict(list)
armor_types = {}

# Rules dictionary, including suffixes and corresponding registry names
rules = {
    'S': 'SuperWeaponTypes',
    'W': 'WeaponTypes',
    'WH': 'Warheads',
    'P': 'Projectiles',
    'AN': 'Animations',
    'I': 'InfantryTypes',
    'B': 'BuildingTypes',
    'V': 'VehicleTypes',
    'AC': 'AircraftTypes',
    'TL': 'TunnelTypes',
    'DG': 'DigitalDisplayTypes',
    'SD': 'ShieldTypes',
    'AE': 'AttachEffectTypes',
    'DPK': 'DataPackTypes',
    'RST': 'ResistanceTypes',
}

# Read the content of the INI file, specifying utf-8 encoding
with open('_developing.ini', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Iterate through each line of the INI file
for line in lines:
    # Use regular expression to find item names (content between [])
    match = re.match(r'\[(\w+)\]', line)
    if match:
        item_name = match.group(1)
        # Determine which registry the item name belongs to based on rules
        for suffix, registry_name in rules.items():
            if item_name.endswith(suffix):
                registry[registry_name].append(item_name)
                break
    
    # Check for lines starting with "Armor="
    armor_match = re.match(r'Armor=(\w+);(\w+)', line)
    if armor_match:
        armor_types[armor_match.group(1)] = armor_match.group(2)

# Build the content to be written to the file
output_content = "[ArmorTypes]\n"
for key, value in armor_types.items():
    output_content += f'{key}={value}\n'
output_content += '\n'

for key, items in registry.items():
    output_content += f'[{key}]\n'
    for item in items:
        output_content += f'+={item}\n'
    output_content += '\n'

# Write the content to rules_register.ini file
output_filename = 'rules_register.ini'
try:
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(output_content)
    print(f"Content has been successfully written to {output_filename} file.")
except IOError as e:
    print(f"Failed to write to file: {e}")