import tkinter as tk
from PIL import Image, ImageTk
import random
import os
from character import Character
from monster import load_monsters_from_json
from events import BattleEvent, ItemFoundEvent

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MysticJourney")
        self.root.geometry("800x600")  # 창 크기를 800x600으로 설정

        self.intro_text = "MysticJourney에 오신 것을 환영합니다! 이 게임에서는 영웅이 되어 모험을 떠나게 됩니다. 각 이벤트에서 선택지를 통해 게임을 진행하세요."
        self.output_text = tk.StringVar()
        self.output_label = tk.Label(root, textvariable=self.output_text, wraplength=700, font=("Arial", 14))
        self.output_label.pack(pady=20)

        self.start_button = tk.Button(root, text="게임 시작", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=20)

        self.option_buttons = [tk.Button(root, font=("Arial", 12), width=20) for _ in range(2)]
        for button in self.option_buttons:
            button.pack_forget()

        self.hero = Character(name="영웅", health=100, attack_power=15, image_path=os.path.join("resources", "hero", "hero_base.png"))

        self.hero_health_label = tk.Label(root, text=f"{self.hero.name} HP: {self.hero.health}", font=("Arial", 12))
        self.hero_health_label.pack(side="left", padx=20, anchor="s")

        self.monster_health_label = tk.Label(root, font=("Arial", 12))
        self.monster_health_label.pack(side="right", padx=20, anchor="n")

        monsters_file_path = os.path.join(os.path.dirname(__file__), "resources", "monsters.json")
        self.monsters = load_monsters_from_json(monsters_file_path)

        self.hero_image_label = tk.Label(root)
        self.hero_image_label.pack(side="left", padx=20, anchor="s")

        self.monster_image_label = tk.Label(root)
        self.monster_image_label.pack(side="right", padx=20, anchor="n")

        self.event_templates = [
            lambda: BattleEvent(self.hero, self.monsters, grade=1),
            lambda: BattleEvent(self.hero, self.monsters, grade=2),
            lambda: BattleEvent(self.hero, self.monsters, grade=3),
            # lambda: ItemFoundEvent(items=[{"name": "힐링 포션"}, {"name": "롱소드"}]),
            # lambda: ItemFoundEvent(items=[{"name": "마나 포션"}, {"name": "방패"}])
        ]
        self.current_event_index = 0

        self.output_text.set(self.intro_text)

    def start_game(self):
        self.start_button.pack_forget()  # 시작 버튼 숨기기
        self.trigger_next_event()

    def trigger_next_event(self):
        for widget in self.root.pack_slaves():
            if isinstance(widget, tk.Button):
                widget.pack_forget()

        event = random.choice(self.event_templates)()
        if isinstance(event, ItemFoundEvent):
            event.trigger(self.root, self.output_text, self.hero_health_label, self.monster_health_label, self.trigger_next_event)
        elif isinstance(event, BattleEvent):
            event.trigger(self.root, self.output_text, self.hero_health_label, self.monster_health_label, self.update_images, self.trigger_next_event)

    def update_images(self, hero_photo, monster_photo):
        self.hero_image_label.config(image=hero_photo)
        self.hero_image_label.image = hero_photo

        self.monster_image_label.config(image=monster_photo)
        self.monster_image_label.image = monster_photo

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
