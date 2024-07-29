import tkinter as tk

class Event:
    def trigger(self, character, root, output_text, option_buttons, next_event_callback):
        raise NotImplementedError("Subclasses should implement this!")

class BattleEvent(Event):
    def __init__(self, enemy):
        self.enemy = enemy

    def trigger(self, character, root, output_text, option_buttons, next_event_callback):
        self.character = character
        self.output_text = output_text
        self.option_buttons = option_buttons
        self.next_event_callback = next_event_callback
        self.output_text.set(f"야생의 {self.enemy.name}(이)가 나타났다! (등급: {self.enemy.grade})")

        self.update_options([("공격하기", self.attack), ("도망치기", self.run_away)])

    def attack(self):
        self.character.attack(self.enemy)
        if self.enemy.health > 0:
            self.enemy.attack(self.character)
            if self.character.health > 0:
                self.output_text.set(f"{self.enemy.name}(이)가 {self.character.name}을 공격했습니다!")
            else:
                self.output_text.set(f"{self.character.name}이(가) {self.enemy.name}에게 패배했습니다...")
                self.update_options([])
                self.next_event_callback()
        else:
            self.output_text.set(f"{self.character.name}이(가) {self.enemy.name}을 물리쳤습니다!")
            self.update_options([])
            self.next_event_callback()

    def run_away(self):
        self.output_text.set(f"{self.character.name}이(가) 도망쳤습니다!")
        self.update_options([])
        self.next_event_callback()

    def update_options(self, options):
        for button in self.option_buttons:
            button.pack_forget()
        for i, (text, command) in enumerate(options):
            button = self.option_buttons[i]
            button.config(text=text, command=command)
            button.pack()

class ItemFoundEvent(Event):
    def __init__(self, item):
        self.item = item

    def trigger(self, character, root, output_text, option_buttons, next_event_callback):
        self.character = character
        self.output_text = output_text
        self.option_buttons = option_buttons
        self.next_event_callback = next_event_callback
        self.output_text.set(f"{self.character.name}이(가) {self.item}을(를) 발견했습니다!")

        self.update_options([("줍기", self.pick_item), ("버리기", self.leave_item)])

    def pick_item(self):
        self.character.pick_item(self.item)
        self.output_text.set(f"{self.character.name}이(가) {self.item}을(를) 주웠습니다!")
        self.update_options([])
        self.next_event_callback()

    def leave_item(self):
        self.output_text.set(f"{self.character.name}이(가) {self.item}을(를) 버렸습니다.")
        self.update_options([])
        self.next_event_callback()

    def update_options(self, options):
        for button in self.option_buttons:
            button.pack_forget()
        for i, (text, command) in enumerate(options):
            button = self.option_buttons[i]
            button.config(text=text, command=command)
            button.pack()
