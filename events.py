import tkinter as tk
from tkinter import messagebox
import random
import os
from PIL import Image, ImageTk
from character import Character
from monster import get_random_monster_by_grade

class BattleEvent:
    def __init__(self, hero, monsters, grade):
        self.hero = hero
        self.monsters = monsters
        self.grade = grade

    def trigger(self, root, output_text, hero_health_label, monster_health_label, update_images, next_event_callback):
        monster = get_random_monster_by_grade(self.monsters, self.grade)
        monster_image_path = os.path.join("resources", "monster", monster.image)
        monster_character = Character(name=monster.name, health=random.randint(*monster.hp),
                                      attack_power=random.randint(*monster.attack), image_path=monster_image_path)

        output_text.set(f"{monster_character.name}와(과) 전투가 시작됩니다!")

        hero_image = Image.open(self.hero.image_path)
        hero_image = hero_image.resize((150, 150), Image.LANCZOS)
        hero_photo = ImageTk.PhotoImage(hero_image)

        monster_image = Image.open(monster_character.image_path)
        monster_image = monster_image.resize((150, 150), Image.LANCZOS)
        monster_photo = ImageTk.PhotoImage(monster_image)

        update_images(hero_photo, monster_photo)

        hero_health_label.config(text=f"{self.hero.name} HP: {self.hero.health}")
        monster_health_label.config(text=f"{monster_character.name} HP: {monster_character.health}")

        def attack():
            hero_damage = self.hero.attack(monster_character)
            if monster_character.health > 0:
                monster_damage = monster_character.attack(self.hero)
                output_text.set(f"{self.hero.name}이(가) {monster_character.name}에게 {hero_damage}의 피해를 입혔습니다!\n"
                                f"{monster_character.name}이(가) {self.hero.name}에게 {monster_damage}의 피해를 입혔습니다!")
                hero_health_label.config(text=f"{self.hero.name} HP: {self.hero.health}")
                monster_health_label.config(text=f"{monster_character.name} HP: {monster_character.health}")
                if self.hero.health <= 0:
                    output_text.set(f"{self.hero.name}이(가) 쓰러졌습니다...")
                    for button in root.pack_slaves():
                        if isinstance(button, tk.Button):
                            button.pack_forget()
            else:
                output_text.set(f"{monster_character.name}을(를) 물리쳤습니다!")
                monster_health_label.config(text=f"{monster_character.name} HP: 0")
                for button in root.pack_slaves():
                    if isinstance(button, tk.Button):
                        button.pack_forget()
                next_button = tk.Button(root, text="다음", command=next_event_callback)
                next_button.pack(pady=10)

        attack_button = tk.Button(root, text="공격", command=attack)
        attack_button.pack(pady=10)

class ItemFoundEvent:
    def __init__(self, items):
        self.items = items

    def trigger(self, root, output_text, hero_health_label, monster_health_label, next_event_callback):
        item = random.choice(self.items)
        output_text.set(f"{item['name']}을(를) 발견했습니다!")
        messagebox.showinfo("아이템 발견", f"{item['name']}을(를) 발견했습니다!")

        next_button = tk.Button(root, text="다음", command=next_event_callback)
        next_button.pack(pady=10)

def get_random_monster_by_grade(monsters, grade):
    eligible_monsters = [monster for monster in monsters if monster.grade == grade]
    if not eligible_monsters:
        raise ValueError(f"No monsters found for grade {grade}")
    return random.choice(eligible_monsters)
