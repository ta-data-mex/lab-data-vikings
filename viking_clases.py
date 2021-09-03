# Soldier
import random
class Soldier():
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receive_damage(self,damage):
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
    
    def receive_damage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return str(self.name) + ' has received ' + str(damage) + ' points of damage'
        elif self.health <= 0:
            return str(self.name) + ' has died in act of combat'
        

    def battle_cry(self):
        return 'Odin Owns You All!'



class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    
    def receive_damage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        elif self.health <= 0:
            return 'A Saxon has died in combat'
    

# War


class War():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    
        
    def add_viking(self,vk):
        self.viking_army.append(vk)
        

    def add_saxon(self,sx):
        self.saxon_army.append(sx)

    def viking_attack(self):

        ran_sx = random.randint(0,len(self.saxon_army))
        ran_vk = random.randint(0,len(self.viking_army))
        strenght_vk = self.viking_army[ran_vk].attack()
        sx_soldier = self.saxon_army[ran_sx]
        damage = sx_soldier.receive_damage(strenght_vk)
        sx_soldier.receive_damage(strenght_vk)
        if sx_soldier.health <= 0:
            self.saxon_army[ran_sx].remove
        return damage

    def saxon_attack(self):
        ran_sx = random.randint(0,len(self.saxon_army))
        ran_vk = random.randint(0,len(self.viking_army))
        strenght_sx = self.saxon_army[ran_sx].attack()
        vk_soldier = self.viking_army[ran_vk]
        damage = vk_soldier.receive_damage(strenght_sx)
        if vk_soldier.health <= 0:
            self.viking_army[ran_vk].remove
        return damage

    def show_status(self):
        if len(self.viking_army) == 0:
            resp = 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxon_army) == 0:
            resp = 'Vikings have won the war of the century'
        elif len(self.saxon_army) > 1 or len(self.viking_army) > 1:
            resp = "Vikings and Saxons are still in the thick of battle."
        return resp

