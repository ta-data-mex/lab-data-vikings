# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receive_damage(self,damage):
        self.health = self.health - damage    

# Viking


class Viking(Soldier):
    def __init__(self, name,health, strength):
        self.name = name
        #Hereda atributo health y strength de Soldier
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()
        
    
    def receive_damage(self, damage):
        self.health = self.health - damage 
        if self.health<=0:
            mensaje1= self.name + "has died in act of combat"
            return mensaje1
        else:
            mensaje2= self.name ="has received DAMAGE points of damage"        
            
    def battle_cry(self):
        return "Odin Owns You All!"
    
# Saxon

class Saxon(Soldier):
    def __init__(self, health,strength):
        super().__init__(health,strength)
    
    def receive_damage(self, damage):
        self.health = self.health - damage 
        if self.health<=0:
            
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received DAMAGE points of damage" 
        

# War


class War:
    pass

