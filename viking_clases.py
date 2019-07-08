import random
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
        super().__init__(health, strength)
        self.name = name
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battle_cry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0 :
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'



# War


class War:
    import random
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    def add_viking(self, viking):
        self.viking_army.append(viking)
    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)
    def viking_attack(self):
        num_viking = random.randint(0,len(self.viking_army)-1)
        num_saxon = random.randint(0,len(self.saxon_army)-1)
        a = self.saxon_army[num_saxon].receive_damage(self.viking_army[num_viking].strength)
        for x in self.saxon_army:
            if x.health <= 0:
                self.saxon_army.remove(x)
        return a
    def saxon_attack(self):
        num_viking = random.randint(0,len(self.viking_army)-1)
        num_saxon = random.randint(0,len(self.saxon_army)-1)
        a2 = self.viking_army[num_viking].receive_damage(self.saxon_army[num_saxon].strength)
        for x in self.viking_army:
            if x.health <= 0:
                self.viking_army.remove(x)
        return a2
    def show_status(self):
        if len(self.saxon_army) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.viking_army) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            #elif len(self.saxon_army) == 1 or len(self.viking_army) == 1:
            return 'Vikings and Saxons are still in the thick of battle.'
