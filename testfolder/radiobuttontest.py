import tkinter as tk
from tkinter import messagebox


def choice():
    messagebox.showinfo("Wybór", f"Wybrałeś opcję:  {wybór.get}")


root = tk.Tk()
root.title("Przykładowy radiobutton")

wybór = tk.StringVar(value="")



radio_1 = tk.Radiobutton(root, text="Opcja 1", variable=wybór, value="opcja_1",)
radio_1.pack(pady=5)


radio_2 = tk.Radiobutton(root, text="Opcja 2",variable=wybór, value="opcja_2",)
radio_2.pack(pady=5)

przycisk_ok = tk.Button(root, text="confirm",command=choice,)
przycisk_ok.pack(pady=5)

root.mainloop()
