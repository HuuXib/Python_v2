

class sword:
    amount_of_items = 0 #This is a class variable
    def __init__(self, name , dmg, rarity):
        self.name = name
        self.dmg = dmg
        self.rarity = rarity
        sword.amount_of_items += 1

        
