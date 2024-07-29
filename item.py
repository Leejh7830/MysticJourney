import json
import os
import random

class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category

def load_items_from_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON 파일이 존재하지 않습니다: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    equipment_data = data['equipment']
    potions_data = data['potions']
    items = []
    for item_data in equipment_data:
        name = item_data['name']
        items.append(Item(name, 'equipment'))
    for item_data in potions_data:
        name = item_data['name']
        items.append(Item(name, 'potion'))
    return items
