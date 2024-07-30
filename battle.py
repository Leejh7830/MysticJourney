import tkinter as tk
from PIL import Image, ImageTk
import random
import os
from monster import load_monsters_from_json, get_random_monster_by_grade

class Character:
    def __init__(self, name, health, attack_power, image_path):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.image_path = image_path

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.take_damage(damage)
        return damage

    def take_damage(self, damage):
        self.health -= damage

class BattleEvent:
    def __init__(self, hero, monsters, grade):
        self.hero = hero
        self.monsters = monsters
        self.grade = grade

    def trigger(self, root, output_text, hero_health_label, monster_health_label):
        monster = get_random_monster_by_grade(self.monsters, self.grade)
        monster_image_path = os.path.join("resources", "monster", monster.image)
        monster_character = Character(name=monster.name, health=random.randint(*monster.hp),
                                      attack_power=random.randint(*monster.attack), image_path=monster_image_path)

        output_text.set(f"{monster_character.name}와(과) 전투가 시작됩니다!")

        # 주인공 이미지
        hero_image = Image.open(self.hero.image_path)
        hero_image = hero_image.resize((150, 150), Image.ANTIALIAS)
        hero_photo = ImageTk.PhotoImage(hero_image)
        hero_label = tk.Label(root, image=hero_photo)
        hero_label.image = hero_photo
        hero_label.pack(side="left", padx=20, anchor="s")

        # 몬스터 이미지
        monster_image = Image.open(monster_character.image_path)
        monster_image = monster_image.resize((150, 150), Image.ANTIALIAS)
        monster_photo = ImageTk.PhotoImage(monster_image)
        monster_label = tk.Label(root, image=monster_photo)
        monster_label.image = monster_photo
        monster_label.pack(side="right", padx=20, anchor="n")

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
            else:
                output_text.set(f"{monster_character.name}을(를) 물리쳤습니다!")
                monster_health_label.config(text=f"{monster_character.name} HP: 0")

        attack_button = tk.Button(root, text="공격", command=attack)
        attack_button.pack()

def main():
    root = tk.Tk()
    root.title("Battle Screen")
    root.geometry("600x400")

    resources_path = os.path.join(os.path.dirname(__file__), "resources")
    hero_image_path = os.path.join(resources_path, "hero", "hero_base.png")
    monsters_file_path = os.path.join(resources_path, "monsters.json")

    hero = Character(name="영웅", health=100, attack_power=15, image_path=hero_image_path)
    monsters = load_monsters_from_json(monsters_file_path)

    output_text = tk.StringVar()
    output_label = tk.Label(root, textvariable=output_text, wraplength=500, font=("Arial", 14))
    output_label.pack(pady=20)

    hero_health_label = tk.Label(root, text=f"{hero.name} HP: {hero.health}", font=("Arial", 12))
    hero_health_label.pack(side="left", padx=20, anchor="s")

    monster_health_label = tk.Label(root, font=("Arial", 12))
    monster_health_label.pack(side="right", padx=20, anchor="n")

    # 예시: 2등급 몬스터와의 전투
    battle_event = BattleEvent(hero, monsters, grade=2)
    battle_event.trigger(root, output_text, hero_health_label, monster_health_label)

    root.mainloop()

if __name__ == "__main__":
    main()
