class Soldier:
    
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receive_damage(self,damage):
        self.health = self.health - damage
    
    pass

# Viking

class Viking:
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
        super().__init__(self,health,strength)
        
    def receive_damage(self,damage):
        self.health = self.health - damage
        if self.health <=0:
            return f'{name} has died in act of combat'
        else:
            return f'{name} has received DAMAGE {damage} points of damage'
     
    def battle_cry(self):
        return f'Odin Owns You All!'
    
    pass

# Saxon


class Saxon:
    
    def __init__(self,health,strength):
        super().__init__(self,health,strength)
        
    def attack(self):
        return self.strength
    
    def receive_damage(self,damage):
        self.health = self.health - damage

        if self.health <= 0:
            return f'A Saxon has died in combat'
            
        else:
            return f'A Saxon has received {damage} points of damage' 
    pass

# War

'''
class War:
    
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
        super().__init__(self,health,strength)
    
    def war(self):
        viking_army=[]
        saxon_army=[]
    
    def add_viking(self,Viking):
        viking_army.append[Viking]
        
    def add_saxon(self,saxon):
        saxon_army.append[saxon]
        
    def viking_attack(self):
        receive_damage=strength
    
        
    def saxon_attack():
    def show_status():
    pass
'''