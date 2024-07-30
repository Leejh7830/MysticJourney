import random

class Character:
    def __init__(self, name, health, attack_power, image_path=None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.image_path = image_path

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

    def __repr__(self):
        return f"Character(name={self.name}, health={self.health}, attack_power={self.attack_power})"
