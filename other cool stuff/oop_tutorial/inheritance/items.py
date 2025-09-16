
class Item():

    def __init__(self,name, value):
        self.name = name
        self.value = value
    def show_value(self):
        print(f"This item is worth: {self.value} $")
            
    

class Armor(Item):
    def defense(self, protection):
        self.protection = protection
        print(f"{self.name} has {protection} defense")

class Weapon(Item):
    def typeofitem(self):
        print(f"{self.name} is a Weapon")
    def damage(self,dmg):
        self.dmg = dmg
        print(f"{self.name} zadaje {dmg} obrażeń")

class Staff(Weapon):
    def typeofdmg(self):
        print(f"This weapon deals magic damage ")
    def forwho(self, typeofcharacter="Mage"):
        print(f"This weapon can be used only by {typeofcharacter}")

class Attack():
    def __init__(self, weapon: Weapon, armor: Armor):
        self.weapon = weapon
        self.armor = armor

    def attack(self):
        real_dmg = self.weapon.dmg - self.armor.protection
        if real_dmg < 0:
            real_dmg = 0
        print(f"You attacked with {self.weapon.name} and dealt {real_dmg} damage")
        print(f"Enemy armor absorbed {self.armor.protection} damage")



