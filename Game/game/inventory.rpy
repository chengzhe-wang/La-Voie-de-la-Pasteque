'
fonctionne pas
'
init python:

    class InventoryItem:
        def __init__(self, img, value):
            self.img = img
            self.value = value


    class Consumable(InventoryItem):
        def __init__(self, img, value, hp_gain, mp,gain):
            InventoryItem.__init__(self, img, value)
            self.hp_gain = hp_gain
            self.mp_gain = mp_gain


        def use(self, target):
            inventory.remove(self)
            target.addHP(self.hp_gain)
            target.addMp(self.mp_gain)
            global selected_item
            selected_item = None

    class Equipable(InventoryItem):
        def __init__(self, img, value):
            InventoryItem.__init__(self, img, value)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equipped = False
            self.equipped_to = None


    class Weapon(Equipable):
        def __init__(self, img, vale, atk, wpn_type):
            Equipable.__init__(self, img, value)
            self.atk = atk
            self.wpn_type = wpn_type

        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_weapon(self)

        def unequip():
            self.equipped_to.unequip_weapon()
            Equipable.unequip(self)


    class Armor(Equipable):
        def __init__(self, img, value, defense, mdef, slot):
            Equipable.__init__(self, img, value)
            self.defense = defense
            self.mdef = mdef
            self.slot = slot

        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_armor(self, self.slot)

        def unequip():
            self.equipable_to.unequip_armor(self.slot)
            Equipable.unequip(self)

    class KeyItem(InventoryItem):
        def __init__(self, img):
            InventoryItem.__init__(self, img, 0)
