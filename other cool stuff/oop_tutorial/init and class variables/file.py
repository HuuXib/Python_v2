from sword import sword

sword1 = sword("Soul Reaper",105, "Legendary")
sword2 =sword("Heaveniser", 65, "Rare")

print(f"Swords added to game: {sword.amount_of_items} ")

sword1.attack()
sword2.attack()