# Clase para Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health -= damage
     
# Clase para Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        #Hereda atributo health/strength de soldier
        super().__init__(health,strength)
        print(name,health,strength)
        
    def attack(self):
        return super().attack()
    
    def receive_damage(self):
        super().receive_damage()
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + "has died in act of combat"
            
    def battle_cry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        #Hereda atributo health/strength de soldier
        super().__init__(health,strength)
        
    #No se necesita esta por que ya esta heredada la funcion de vikingo 
    #def attack(self):
    #    return super().attack()
        
    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health > 0: 
            return "".join(["A Saxon has received ",str(damage)," points of damage"])
        else:
            return "A Saxon has died in combat" 

# War


class War:
    pass
