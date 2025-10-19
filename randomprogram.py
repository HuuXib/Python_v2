import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
root = tk.Tk()

root.title("Plotter by HuXibb")

window_h = 500
window_w = int(500 * 0.6)
root.geometry(f"{window_h}x{window_w}")
label = tk.Label(text="Input coefficients")
label.pack(pady=5)

text = tk.Text(root, height=1, width=10)
text.pack(pady=5)
x = np.linspace(-10,10,100)
def retrieve_input():
    input = (text.get("1.0", "end-1c"))
    y = np.poly1d([])
    for i in range(len(input)):
        y[i] = input[i]
    plt.plot(x,y(x))
    plt.grid()
    plt.show()



def plot_cosinus():
    cos = np.cos
    plt.plot(x, cos(x))
    plt.grid()
    plt.ylim(-2,2)
    plt.axvline(x=2*np.pi, color='red', linestyle='--', label='Period')
    plt.axvline(x=0, color='red', linestyle='--')
    plt.show()
def plot_sinus():
    sin = np.sin
    plt.plot(x, sin(x))
    plt.grid()
    plt.xlim(0,np.pi*2)
    plt.ylim(-2,2)
    plt.show()
def plot_tangens():
    tg = np.tan
    plt.plot(x, tg(x))
    plt.grid()
    plt.show()

def plot_cotangens():
    tg = np.tan
    plt.plot(x, 1/tg(x))
    plt.grid()
    plt.show()
def plot_exponential():
    e = np.e
    plt.plot(x, e**(x))
    plt.grid()
    plt.show()
def plot_sa():
    sa = np.sin
    plt.plot(x, np.sin(x)/x)
    plt.grid()
    plt.show()

button = tk.Button(root, text="Plot",command=retrieve_input, width=30)
button.pack(pady=5)


label = tk.Label(text="Basic functions")
label.pack(pady=5)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)

grid_text = ["sin(x)", "cos(x)", "tg(x)","ctg(x)","e^x", "Sa(x)/Sinc(x)"]

com = [plot_sinus, plot_cosinus, plot_tangens, plot_cotangens, plot_exponential, plot_sa]
for i in range(3):
    for j in range(2):
        button_grid = tk.Button(grid_frame, text=grid_text[i*2+j],width=10, command=com[i*2+j])
        button_grid.grid(row = i, column=j, padx=5, pady=5)





root.mainloop()