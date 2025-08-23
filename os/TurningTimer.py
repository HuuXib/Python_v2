import os 
import tkinter as tk
def Turnoff():
    Time = selected_variable.get()
    # Time = int(input("Po ilu minutach ma się wyłączyć komputer?: "))
    print(f"Komputer zostanie wyłączony po {Time} minutach")
    os.system(f"shutdown /s /t {Time*60}")
def CancelTurning():
    os.system("shutdown /a")

#PARAMETRY SAMEGO OKNA
root = tk.Tk()
root.title("PC Shut down")
root.geometry("300x200")

#Zmienna reprezentowana przez spinbox 
selected_variable = tk.IntVar(value=1)
label_liczba = tk.Label(root, text="Minuty do wyłączenia PC: ")
label_liczba.pack(pady=5)


#PARAMETRY SPINBOXA
spinbox = tk.Spinbox(root, from_=1, to=500,textvariable=selected_variable, width=10)
spinbox.pack(pady=5)

#PRZYCISK POTWIERDZAJĄCY ZAPLANOWANE WYŁĄCZENIE 
confirm_button = tk.Button(root, text="Potwierdź", command=Turnoff, width=15)
confirm_button.pack(pady=5)

#PRZYCISK ANULUJĄCCY ZAPLANOWANE WYŁĄCZENIE
cancel_button = tk.Button(root, text="Anuluj operację", command=CancelTurning, width=15)
cancel_button.pack(pady=5)

root.mainloop()