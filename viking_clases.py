# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self,health, strength):
        super().__init__(health,strength)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return  f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
import random

class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self,viking):
        self.viking_army.append(viking)

    def add_saxon(self,saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        result = random.choice(self.saxon_army).receive_damage(random.choice(self.viking_army).strength)
        self.saxon_army = [saxon for saxon in self.saxon_army if saxon.health > 0]
        return result

    def saxon_attack(self):
        result = random.choice(self.viking_army).receive_damage(random.choice(self.saxon_army).strength)
        self.viking_army = [viking for viking in self.viking_army if viking.health > 0]
        return result

    def show_status(self):
        if not self.saxon_army:
            return "Vikings have won the war of the century!"
        elif not self.viking_army:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."




