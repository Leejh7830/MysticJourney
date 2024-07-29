class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.inventory = []

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

    def show_inventory(self):
        print(f"{self.name}'s Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
