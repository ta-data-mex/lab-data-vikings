#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:51:50 2019

@author: Luis Gallo / Rodolfo Pardo
"""
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength
   
    def receive_damage(self, damage):
        self.damage = damage
        
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name
    
    def attack(self): 
        return self.strength
    
    def receive_damage(self, damage): 
        self.damage = damage
        gabriel.health -= self.damage
        if self.health > 0:
            print(f'{self.name} has receive {self.damage} points of damage')
        else:
            print(f'{self.name} has died in act of combat')
    def battle_cry(self):
        return print("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self): 
        return self.strength
    
    def receive_damage(self, damage):
        self.damage = damage
        sax.health -= self.damage
        if self.health > 0:
            print(f"A Saxon has received {self.damage} points of damage")
        else:
            print("A saxon has died in combat")



#while gabriel.health > 0 and sax.health > 0:
    #sax.receive_damage(gabriel.attack())

# War


class War:
    def __init__(self, vikingArmy =[], saxonArmy = []):
        pass
    
    def add_viking(gabriel):
        vikingArmy.append(gabriel.strength)
    
    
    def add_saxon(sax):
        saxonArmy.append(sax.strength)
    def viking_attack():
        sax.receive_damage(gabriel.attack())
    def saxon_attack():
        gabriel.receive_damage(sax.attack())
    def show_status():
        if saxonArmy == 0:
            print("Vikings have won the war of the century!")
        elif VikingArmy == 0:
            print("Saxons have fought for their lives and survive another day...")
        elif saxonArmy == 1 and VikingArmy == 1: 
            print("Vikings and Saxons are still in the thick of battle.")
    
    

soldado = Soldier(100, 60)
gabriel = Viking("Gabriel", 100, 10)
sax = Saxon(100, 60)


    
