import sympy
import numpy as np
import matplotlib.pyplot as plt

#zad5

s = 1/2
mi = 0

Normal_distribution = np.random.normal(mi,s,100000)
plt.hist(Normal_distribution, bins=50, color='blue', edgecolor = 'black')
plt.grid()

plt.title(f'Example of Normal distribution with σ = 1/2 and μ = 0')
plt.show()