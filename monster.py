import json
import os
import random

class Monster:
    def __init__(self, name, grade, image, hp, attack):
        self.name = name
        self.grade = grade
        self.image = image
        self.hp = hp
        self.attack = attack

def load_monsters_from_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON 파일이 존재하지 않습니다: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    monsters_data = data['monsters']
    grade_ranges = data['grade_ranges']
    monsters = []
    for monster_data in monsters_data:
        name = monster_data['name']
        grade = monster_data['grade']
        image = monster_data['image']
        hp = grade_ranges[str(grade)]['hp']
        attack = grade_ranges[str(grade)]['attack']
        monsters.append(Monster(name, grade, image, hp, attack))
    return monsters

def get_random_monster_by_grade(monsters, grade):
    eligible_monsters = [monster for monster in monsters if monster.grade == grade]
    return random.choice(eligible_monsters)
