import sympy
import numpy as np
import matplotlib.pyplot as plt


#zad 3
ax = np.poly1d([1,1,-1,0,-1])
bx = np.poly1d([1,0,-1,1])
cx = np.poly1d([1,-1,1,0,0,-1])

dx = np.polymul(ax,cx)
ex = np.polyder(dx)

fx = ex + bx - np.poly1d([-1,0,0,0])

x = np.linspace(-1,1,100)

plt.plot(x,fx(x))
plt.grid()
plt.show()