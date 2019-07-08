# Soldier
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
  def __init__(self, health, strength, name):
    super().__init__(health, strength)
    self.name = name
  
  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      print(f"{self.name} received {damage} points of damage.")
    if self.health <= 0:
      print(f"{self.name} has died in act of combat.")
  
  def battle_cry(self):
    return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
  def __init__(self, health, strength):
    super().__init__(health, strength)
  
  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      print(f"A Saxon has received {damage} points of damage.")
    if self.health <= 0:
      print(f"A Saxon has died in combat.")


# War
class War:
  def __init__(self):
    self.vikingArmy = []
    self.saxonArmy = []

  def add_viking(self, vikingo):
    self.vikingArmy.append(vikingo)

  def add_saxon(self, sajon):
    self.saxonArmy.append(sajon)

  def viking_attack(self):
    import random
    if len(self.saxonArmy) > 0:
      saxon_random = random.randint(0,len(self.saxonArmy)-1)
      viking_random = random.randint(0, len(self.vikingArmy)-1)
      self.saxonArmy[saxon_random].receive_damage(self.vikingArmy[viking_random].strength)
      if self.saxonArmy[saxon_random].health <= 0:
        del self.saxonArmy[saxon_random]
    else:
      print("No one left for battle.")

  def saxon_attack(self):
    import random
    if len(self.vikingArmy) > 0:
      saxon_random = random.randint(0,len(self.saxonArmy)-1)
      viking_random = random.randint(0, len(self.vikingArmy)-1)
      self.vikingArmy[viking_random].receive_damage(self.saxonArmy[saxon_random].strength)
      if self.vikingArmy[viking_random].health <= 0:
        del self.vikingArmy[viking_random]
    else:
      print("No one left for battle.")

  def show_status(self):
    if len(self.saxonArmy) == 0:
      print("Vikings have won the war of the century!")
    if len(self.vikingArmy) == 0:
      print("Saxons have fought for their lives and survived another day...")
    if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
      print("Vikings and Saxons are still in the thick of battle.")
