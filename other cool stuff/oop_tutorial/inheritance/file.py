from items import Weapon, Staff, Armor,Attack

sword1 = Weapon("Steel Mace", 160)

sword1.show_value()
sword1.typeofitem()
sword1.damage(115)

# staff1 = Staff("WindForcer",80)
# staff1.show_value()
# staff1.typeofitem()
# staff1.damage(30,100)
# staff1.forwho()


steel_armor1 = Armor("Steel Armor", 550)
steel_armor1.defense(70)

fight = Attack(sword1, steel_armor1)
fight.attack()

