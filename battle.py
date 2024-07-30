import tkinter as tk
from PIL import Image, ImageTk
import random
import os

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
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    def trigger(self, root, output_text, hero_health_label, monster_health_label):
        output_text.set(f"{self.monster.name}와(과) 전투가 시작됩니다!")

        def attack():
            hero_damage = self.hero.attack(self.monster)
            if self.monster.health > 0:
                monster_damage = self.monster.attack(self.hero)
                output_text.set(f"{self.hero.name}이(가) {self.monster.name}에게 {hero_damage}의 피해를 입혔습니다!\n"
                                f"{self.mon스터.name}이(가) {self.hero.name}에게 {monster_damage}의 피해를 입혔습니다!")
                hero_health_label.config(text=f"{self.hero.name} HP: {self.hero.health}")
                monster_health_label.config(text=f"{self.mon스터.name} HP: {self.monster.health}")
                if self.hero.health <= 0:
                    output_text.set(f"{self.hero.name}이(가) 쓰러졌습니다...")
            else:
                output_text.set(f"{self.mon스터.name}을(를) 물리쳤습니다!")
                monster_health_label.config(text=f"{self.mon스터.name} HP: 0")

        attack_button = tk.Button(root, text="공격", command=attack)
        attack_button.pack()

def main():
    root = tk.Tk()
    root.title("Battle Screen")
    root.geometry("600x400")

    resources_path = os.path.join(os.path.dirname(__file__), "resources")
    hero_image_path = os.path.join(resources_path, "hero_base.png")
    monster_image_path = os.path.join(resources_path, "monster.png")

    hero = Character(name="영웅", health=100, attack_power=15, image_path=hero_image_path)
    monster = Character(name="몬스터", health=80, attack_power=10, image_path=monster_image_path)

    output_text = tk.StringVar()
    output_label = tk.Label(root, textvariable=output_text, wraplength=500, font=("Arial", 14))
    output_label.pack(pady=20)

    # 주인공 이미지
    hero_image = Image.open(hero.image_path)
    hero_image = hero_image.resize((150, 150), Image.ANTIALIAS)
    hero_photo = ImageTk.PhotoImage(hero_image)
    hero_label = tk.Label(root, image=hero_photo)
    hero_label.image = hero_photo
    hero_label.pack(side="left", padx=20, anchor="s")

    # 몬스터 이미지
    monster_image = Image.open(monster.image_path)
    monster_image = monster_image.resize((150, 150), Image.ANTIALIAS)
    monster_photo = ImageTk.PhotoImage(monster_image)
    monster_label = tk.Label(root, image=monster_photo)
    monster_label.image = monster_photo
    monster_label.pack(side="right", padx=20, anchor="n")

    hero_health_label = tk.Label(root, text=f"{hero.name} HP: {hero.health}", font=("Arial", 12))
    hero_health_label.pack(side="left", padx=20, anchor="s")

    monster_health_label = tk.Label(root, text=f"{monster.name} HP: {monster.health}", font=("Arial", 12))
    monster_health_label.pack(side="right", padx=20, anchor="n")

    battle_event = BattleEvent(hero, monster)
    battle_event.trigger(root, output_text, hero_health_label, monster_health_label)

    root.mainloop()

if __name__ == "__main__":
    main()
