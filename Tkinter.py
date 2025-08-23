import tkinter as tk

def przycisk1_klik():
    print(f"Przycisk 1 kliknięty! Wybrana liczba: {wybrana_liczba.get()}")

def przycisk2_klik():
    print(f"Przycisk 2 kliknięty! Wybrana liczba: {wybrana_liczba.get()}")


root = tk.Tk()
root.title("Prosty Interfejs")
root.geometry("300x150")

wybrana_liczba = tk.IntVar(value=1)

label_liczba = tk.Label(root, text = "Wybierz liczbę:")
label_liczba.pack(pady=5)

spinbox = tk.Spinbox(root, from_=1, to=100, textvariable=wybrana_liczba, width=10)
spinbox.pack(pady=5)
root.mainloop()