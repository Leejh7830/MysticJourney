# character.py

class Character:
    def __init__(self):
        self.health = 100
        self.step = 0

    def update_health(self, amount):
        self.health += amount

    def update_step(self, step):
        self.step = step

    def get_status(self):
        return f"Health: {self.health}"
