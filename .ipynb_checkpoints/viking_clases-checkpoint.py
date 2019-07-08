import random
# Soldier
class Soldier():
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
        self.name= name
    
    def receive_damage(self, damage):
        self.health-=damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")
    
    def battle_cry(self):
        return ("Odin Owns You All!")
        
        
# Saxon
class Saxon(Soldier):
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health-=damage
        if self.health >=1:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return("A Saxon has died in combat")
        

# War
class War:
    
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
            
    def add_viking(self, Viking):
        self.viking_army.append(Viking)
        
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
        
    def viking_attack(self):
        saxon = self.saxon_army[random.randint(0, len(self.saxon_army)-1)]
        viking = self.viking_army[random.randint(0, len(self.viking_army)-1)]
        danio = saxon.receive_damage(viking.strength)
        if(saxon.health<=0):
            self.saxon_army.remove(saxon)
        return danio
    
    def saxon_attack(self):
        saxon = self.saxon_army[random.randint(0, len(self.saxon_army)-1)]
        viking = self.viking_army[random.randint(0, len(self.viking_army)-1)]
        danio =viking.receive_damage(saxon.strength)
        if(viking.health<=0):
            self.viking_army.remove(viking)
        return (danio)
        
    def show_status(self):
        if len(self.viking_army)>=1 and len(self.saxon_army) >=1:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxon_army)==0 and len(self.viking_army)>=1:
            return "Vikings have won the war of the century!"
        else:
            return "Saxons have fought for their lives and survive another day..."
