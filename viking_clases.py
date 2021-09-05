# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health= self.health-damage
    
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.health= self.health-damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health= self.health-damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.viking_army=[]
        self.saxon_army=[]

    def add_viking(self, Viking):
        return self.viking_army.append(Viking)

    def add_saxon(self, Saxon):
        return self.saxon_army.append(Saxon)

    def viking_attack(self):
        Saxon.receive_damage(Viking.strength)
        if Saxon.health<0:
            self.saxon_army.pop()
        return Saxon.receive_damage(Viking.strength)

    def saxon_attack(self):
        Viking.receive_damage(Saxon.strength)
        if Viking.name.health<0:
            self.viking_army.remove(Viking.name)
        return Saxon.receive_damage(Viking.strength)

    def show_status(self):
        if len(self.viking_army)==0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxon_army)==0:
            return f"Vikings have won the war of the century!"
        elif len(self.viking_army)>=1 and len(self.saxon_army)>=1:
            return f"Vikings and Saxons are still in the thick of battle."
