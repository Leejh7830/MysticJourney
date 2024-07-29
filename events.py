import random

class BattleEvent:
    def __init__(self, grade, monsters):
        self.grade = grade
        self.monsters = monsters

    def trigger(self, hero, root, output_text, option_buttons, next_event_callback):
        eligible_monsters = [monster for monster in self.monsters if monster.grade == self.grade]
        enemy = random.choice(eligible_monsters)

        output_text.set(f"{enemy.name}와(과) 전투가 시작됩니다!")

        def attack():
            enemy.attack(hero)
            if hero.health > 0:
                hero.attack(enemy)
                if enemy.health <= 0:
                    output_text.set(f"{enemy.name}을(를) 물리쳤습니다!")
                    for button in option_buttons:
                        button.pack_forget()
                    next_event_callback()
                else:
                    output_text.set(f"{enemy.name}의 체력: {enemy.health}")
            else:
                output_text.set("영웅이 쓰러졌습니다...")
                for button in option_buttons:
                    button.pack_forget()

        for i, button in enumerate(option_buttons):
            button.config(text="공격", command=attack)
            button.pack()

class ItemFoundEvent:
    def __init__(self, items):
        self.items = items

    def trigger(self, hero, root, output_text, option_buttons, next_event_callback):
        item = random.choice(self.items)
        output_text.set(f"{hero.name}이(가) {item.name}을(를) 발견했습니다! ({item.category})")

        def pick_item():
            output_text.set(f"{item.name}을(를) 주웠습니다!")
            for button in option_buttons:
                button.pack_forget()
            next_event_callback()

        def leave_item():
            output_text.set(f"{item.name}을(를) 버렸습니다!")
            for button in option_buttons:
                button.pack_forget()
            next_event_callback()

        option_buttons[0].config(text="줍기", command=pick_item)
        option_buttons[1].config(text="버리기", command=leave_item)
        option_buttons[0].pack()
        option_buttons[1].pack()
