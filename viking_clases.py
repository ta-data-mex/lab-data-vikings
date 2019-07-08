# Soldier


class Soldier:
   def __init__(self, health, strength):
       self.health = health
       self.strength = strength
   def attack(self):
       return self.strength

   def receive_damage(self, strength):
       self.health -= strength

# Viking


class Viking(Soldier):
   def __init__(self, name, health, strength):
       self.name = name
       super().__init__(health, strength)


   def receive_damage(self, strength):
       self.health -= strength
       if self.health > 0:
           return f"{self.name} has received {strength} points of damage"
       else:
           return f"{self.name} has died in act of combat"


   def battle_cry (self):
       return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
   def __init__(self, health, strength):
       super().__init__(health, strength)

   def receive_damage(self, strength):
       self.health -= strength
       if self.health > 0:
           return f"A Saxon has received {strength} points of damage"

       else:
           return f"A Saxon has died in combat"



# War

import random
from random import randint

class War:
   def __init__(self):
       self.saxon_army=[]
       self.viking_army=[]

   def add_viking(self, viking):
       self.viking_army.append(viking)

   def add_saxon(self, saxon):
       self.saxon_army.append(saxon)

   def viking_attack(self):
       s = random.choice(self.saxon_army)
       v = random.choice(self.viking_army)
       dano = s.receive_damage(v.strength)
       if s.health <= 0:
           self.saxon_army.remove(s)
       return dano

   def saxon_attack(self):
       s = random.choice(self.saxon_army)
       v = random.choice(self.viking_army)
       dano = v.receive_damage(s.strength)
       if v.health <= 0:
           self.viking_army.remove(v)
       return dano

   def show_status(self):
       if len(self.saxon_army)== 0:
           return "Vikings have won the war of the century!"
       elif len(self.viking_army)== 0:
           return "Saxons have fought for their lives and survive another day..."
       else:
           return "Vikings and Saxons are still in the thick of battle."
