import random


class Soldier:
    def __init__(self, health, strength):
      self.health = health
      self.strength = strength
    
    def attack(self):
      return self.strength
      
    def receive_damage(self, damage):
      self.health -= damage
    


class Viking(Soldier):
  def __init__(self, name, health, strength):
    super().__init__(health, strength)
    self.name = name
    

  def receive_damage(self, damage):
    self.health -= damage
    while self.health > 0:
      return f'{self.name} has received {damage} points of damage'
    return f'{self.name} has died in act of combat'

  def battle_cry(self):
    return "Odin Owns You All!"    


class Saxon(Soldier):
  def __init__(self, health, strength):
    super().__init__(health, strength)
    
  def receive_damage(self, damage):
    self.health -= damage
    while self.health > 0:
      return f'A Saxon has received {damage} points of damage'
    return 'A Saxon has died in combat'

class War:
  viking_army = []
  saxon_army = []

  def __init__(self):
    self.viking_army = []
    self.saxon_army = []

  def add_viking(self, viking):
    self.viking_army.append(viking)

  def add_saxon(self, saxon):
    self.saxon_army.append(saxon)

  def viking_attack(self):
    sax = random.choice(self.saxon_army)
    vik = random.choice(self.viking_army)
    res = sax.receive_damage(vik.strength)
    if sax.health <= 0:
      self.saxon_army.remove(sax)
    return res


  def saxon_attack(self):
    sax = random.choice(self.saxon_army)
    vik = random.choice(self.viking_army)
    res = vik.receive_damage(sax.strength)
    if vik.health <= 0:
      self.viking_army.remove(vik)
    return res
  
  def show_status(self):
    if len(self.viking_army) == 0:
      return "Saxons have fought for their lives and survive another day..."
    elif len(self.saxon_army) == 0:
      return 'Vikings have won the war of the century!'
    else:
      return "Vikings and Saxons are still in the thick of battle."
