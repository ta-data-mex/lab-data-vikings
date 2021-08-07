# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self,damage):
        self.health -= damage


# Viking


class Viking(Soldier):

    def __init__(self,health,strength,name):
        self.name = name
        super().__init__(health,strength)

    def receive_damage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battle_cry(self):
        return "Odin Owns You All!"






# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receive_damage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in act of combat'




# War


class War(Viking,Saxon):

    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self,Viking):
        self.viking_army.append(Viking)


    def add_saxon(self,Saxon):
        self.saxon_army.append(Saxon)


    def viking_attack(self):
        saxon_target = random.choice(self.saxon_army)
        viking_target = random.choice((self.viking_army))

        result = saxon_target.receive_damge(viking_target.strength)

        if saxon_target.health <= 0:
            self.saxon_army.remove(saxon_target)

        return result

    def saxon_attack(self):
        saxon_target = random.choice(self.saxon_army)
        viking_target = random.choice(self.viking_army)

        result = viking_target.receive_damage(saxon_target.strength)

        if viking_target.health <= 0:
            self.saxon_army.remove(viking_target)

        return result


    def show_status(self):

        if self.saxon_army == []:
            return "Vikings have won the war of the century!"
        elif self.viking_army == []:
            return "Saxons have fought for their lives and survive another day..."

        else:
            return "Vikings and Saxons are still in the thick of battle."


