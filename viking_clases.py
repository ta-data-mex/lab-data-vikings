# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receive_damage(damage):
        self.health-=damage
    

# Viking

class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health > 0: 
            return "".join([self.name," has received ",str(damage)," points of damage"])
        else:
            return "".join([self.name," has died in act of combat"])

    def battleCry(self):
        return 'Odin Owns You All!
# Saxon


class Saxon(Soldier):
    def __init__(self,name,health):
        super().__init__(health,strength)
    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health > 0: 
            return "".join(["A Saxon has received ",str(damage)," points of damage"])
        else:
            return "A Saxon has died in combat"     
        
    
    

# War   
class War:    
    
    
pass
