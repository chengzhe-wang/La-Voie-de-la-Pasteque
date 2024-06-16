'
fonctionne pas
'
init python:

    class Player:
        def __init__(self, hp, mp, atk, defense, mdef, level=1):
            self.hp = hp
            self.mp = mp
            self.max_hp = hp
            self.max_mp = mp
            self.atk = atk
            self.defense = defense
            self.mdef = mdef
            self.level = level
            self.weapon = None
            self.armor = {"head": None, "chest": None, "acc": None, "shield": None}

        def addHP(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        def addMP(self, amount):
            self.mp += amount
            if self.mp > self.max_mp:
                self.mp = self.max_mp

        def equip_weapon(self, weapon):
            if self.weapon != None:
                self.unequip_weapon()

            self.weapon = weapon
            self.atk += weapon.atk

        def unequip_weapon(self,):
            if self.weapon != None:
                self.atk -= self.weapon.atk
                self.weapon = None

        def equip_armor(self, armor, slot):
            if self.armor[slot] != None:
                self.unequip_armor(slot)

            self.armor[slot] = armor
            self.defense += armor.defense
            self.mdef += armor.mdef

        def unequip_armor(self,slot):
            if self.armor[slot] != None:
                self.defense -= self.armor[slot].defense
                self.mdef -= self.armor[slot].mdef
                self.armor[slot] = None
