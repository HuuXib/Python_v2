import random as rd

while True:
    oczka = rd.randint(1,6)
    next_throw = input("Czy chcesz rzucic ponownie kostką?(T/N): ")
    if(next_throw == "T"):
        print(f"Wypadło ci: {oczka} oczek")
    else:
        break