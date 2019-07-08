# Soldier
import random
class Soldier:
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
    self.name = name
    super().__init__(health, strength)
  
  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f'{self.name} has received {damage} points of damage'
    else:
      return f'{self.name} has died in act of combat'

  def battle_cry(self):
    return "Odin Owns You All!"
    
# Saxon
class Saxon(Soldier):
  def __init__(self, health, strength): 
    super().__init__(health, strength)

  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f'A Saxon has received {damage} points of damage'
    else:
      return 'A Saxon has died in combat'

# War
class War:
  def __init__(self):
    self.viking_army = []
    self.saxon_army = []

  def add_viking(self, vikingo):
    self.viking_army.append(vikingo)

  def add_saxon(self, sajon):
    self.saxon_army.append(sajon)

  def viking_attack(self):
    sajon = random.choice(self.saxon_army)
    vikingo = random.choice(self.viking_army)
    resultado = sajon.receive_damage(vikingo.strength)
    if sajon.health <= 0:
      self.saxon_army.remove(sajon)
    return resultado

  def saxon_attack(self):
    vikingo = random.choice(self.viking_army)
    sajon = random.choice(self.saxon_army)
    resultado = vikingo.receive_damage(sajon.strength)
    if vikingo.health <= 0:
      self.viking_army.remove(vikingo)
    return resultado

  def show_status(self):
    if len(self.saxon_army) == 0:
      return 'Vikings have won the war of the century!'
    if len(self.viking_army) == 0:
      return 'Saxons have fought for their lives and survive another day...'
    if len(self.viking_army) >= 1 and len(self.saxon_army) >= 1:
      return 'Vikings and Saxons are still in the thick of battle.'
