# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return strength
    
    def receive_damage(self, the_damage):
        health - the_damage
        
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        
    def receive_damage(self, the_damage):
        health - the_damage
        if health - the_damage > 0:
            return print(name, " has received ", the_damage, " points of damage")
        if health - the_damage <= 0:
            return print (name, " has died in act of combat")
        
    def battle_cry(self):
        print('Odin Owns You All!')
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receive_damage(self, the_damage):
        health - the_damage
        if health - the_damage > 0:
            return print('A Saxon has received ',the_damage, ' points of damage')
        if health - the_damage <= 0:
            return print('A Saxon has died in combat')
    

# War


class War:
    def __init__(self):
        viking_army = []
        saxon_army = []
        
    def add_viking(Viking):
        viking_army.append(viking)
        
    def add_saxon(Saxon):
        saxon_army.append(Saxon)
        
    def viking_attack(self):
         Saxon.receive_damage(Viking.strength)
            if Saxon.health <= 0:
                saxon_army.remove(Saxon)
        
        
        
        
        
        
        