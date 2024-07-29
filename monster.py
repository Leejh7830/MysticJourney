import random
import json
import os

class Monster:
    def __init__(self, name, grade, grade_ranges):
        self.name = name
        self.grade = grade
        self.health = random.randint(*grade_ranges[str(grade)]['hp'])
        self.attack_power = random.randint(*grade_ranges[str(grade)]['attack'])

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")

def load_monsters_from_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON 파일이 존재하지 않습니다: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    grade_ranges = data['grade_ranges']
    monsters_data = data['monsters']
    monsters = []
    for monster_data in monsters_data:
        name = monster_data['name']
        grade = monster_data['grade']
        monsters.append(Monster(name, grade, grade_ranges))
    return monsters
