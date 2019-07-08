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
  def __init__(self, name, health, strength):
    super().__init__(health, strength)
    self.name = name
  
  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f"{self.name} has received {damage} points of damage"
    if self.health <= 0:
      return f"{self.name} has died in act of combat"
  
  def battle_cry(self):
    return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
  def __init__(self, health, strength):
    super().__init__(health, strength)
  
  def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f"A Saxon has received {damage} points of damage"
    if self.health <= 0:
      return f"A Saxon has died in combat"


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
    import random
    if len(self.saxon_army) > 0:
      saxon_random = random.randint(0,len(self.saxon_army)-1)
      viking_random = random.randint(0, len(self.viking_army)-1)
      self.saxon_army[saxon_random].receive_damage(self.viking_army[viking_random].strength)
      if self.saxon_army[saxon_random].health <= 0:
        del self.saxon_army[saxon_random]
    else:
      print("No one left for battle.")

  def saxon_attack(self):
    import random
    if len(self.viking_army) > 0:
      saxon_random = random.randint(0,len(self.saxon_army)-1)
      viking_random = random.randint(0, len(self.viking_army)-1)
      self.viking_army[viking_random].receive_damage(self.saxon_army[saxon_random].strength)
      if self.viking_army[viking_random].health <= 0:
        del self.viking_army[viking_random]
    else:
      print("No one left for battle.")

  def show_status(self):
    if len(self.saxon_army) == 0:
      return "Vikings have won the war of the century!"
    if len(self.viking_army) == 0:
      return "Saxons have fought for their lives and survive another day..."
    if len(self.saxon_army) >= 1 and len(self.viking_army) >= 1:
      return "Vikings and Saxons are still in the thick of battle."
