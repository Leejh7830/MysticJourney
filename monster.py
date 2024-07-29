import random
import json
import os

class Monster:
    grade_ranges = {
        1: {'hp': (10, 20), 'attack': (1, 2)},
        2: {'hp': (20, 40), 'attack': (2, 4)},
        3: {'hp': (40, 60), 'attack': (4, 6)},
        4: {'hp': (60, 80), 'attack': (6, 8)},
        5: {'hp': (80, 100), 'attack': (8, 10)},
        6: {'hp': (150, 200), 'attack': (15, 20)},
        7: {'hp': (200, 250), 'attack': (20, 25)},
        8: {'hp': (250, 300), 'attack': (25, 30)},
        9: {'hp': (300, 350), 'attack': (30, 35)},
        10: {'hp': (350, 400), 'attack': (35, 40)},
    }

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.health = random.randint(*self.grade_ranges[grade]['hp'])
        self.attack_power = random.randint(*self.grade_ranges[grade]['attack'])

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
    monsters = []
    for monster_data in data:
        name = monster_data['name']
        grade = monster_data['grade']
        monsters.append(Monster(name, grade))
    return monsters
