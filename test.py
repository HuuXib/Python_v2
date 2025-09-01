import tkinter as tk

def function():
    print("spierdalaj")

root = tk.Tk()
root.title("chuj wie co to")
root.geometry("300x200")

button = tk.Button(root, text="umyj dupe", command= function , width = 10)
button.pack(pady=5)
root.mainloop()