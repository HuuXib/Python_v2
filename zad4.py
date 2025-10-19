import sympy
import numpy as np
import matplotlib.pyplot as plt

t = sympy.Symbol('t')


wynik = sympy.integrate(t**2,t)

wynik2 = sympy.integrate(t**2,(t,-1,1))

print(wynik,wynik2)
