import tkinter as tk
from character import Character
from monster import load_monsters_from_json
from item import load_items_from_json
from events import BattleEvent, ItemFoundEvent

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MysticJourney")
        self.root.geometry("600x400")  # 창 크기를 600x400으로 설정

        self.intro_text = "MysticJourney에 오신 것을 환영합니다! 이 게임에서는 영웅이 되어 모험을 떠나게 됩니다. 각 이벤트에서 선택지를 통해 게임을 진행하세요."
        self.output_text = tk.StringVar()
        self.output_label = tk.Label(root, textvariable=self.output_text, wraplength=500, font=("Arial", 14))
        self.output_label.pack(pady=20)

        self.start_button = tk.Button(root, text="게임 시작", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=20)

        self.option_buttons = [tk.Button(root, font=("Arial", 12), width=20) for _ in range(2)]
        for button in self.option_buttons:
            button.pack_forget()

        self.hero = Character(name="영웅", health=100, attack_power=15)

        try:
            self.monsters = load_monsters_from_json('monsters.json')
            self.hero.monsters = self.monsters  # hero 객체에 monsters 할당
            self.items = load_items_from_json('items.json')
        except FileNotFoundError as e:
            print(e)
            self.root.destroy()
            return

        self.events = [
            ItemFoundEvent(items=self.items),
            BattleEvent(grade=2),  # 2등급 몬스터와의 전투
            ItemFoundEvent(items=self.items)
        ]
        self.current_event_index = 0

        self.output_text.set(self.intro_text)

    def start_game(self):
        self.start_button.pack_forget()  # 시작 버튼 숨기기
        self.trigger_next_event()

    def trigger_next_event(self):
        if self.current_event_index < len(self.events):
            event = self.events[self.current_event_index]
            event.trigger(self.hero, self.root, self.output_text, self.option_buttons, self.trigger_next_event)
            self.current_event_index += 1
        else:
            self.output_text.set(f"{self.hero.name}이(가) 모험을 완료했습니다! 남은 체력: {self.hero.health}")
            for button in self.option_buttons:
                button.pack_forget()

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
