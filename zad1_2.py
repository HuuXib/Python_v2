import numpy as np
import matplotlib.pyplot as plt


#zad1
x = np.linspace(0,np.pi*2, 100)
sin = np.sin(x)
plt.subplot(2,2, (1,2))
plt.plot(x,sin, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x) = sin(x)'])
# plt.show()


#zad2
cos = np.cos(x)
arctg = np.arctan(x)
plt.subplot(2,2,3)
plt.plot(x, cos, color='blue')
plt.legend(['f(x) = cos(x)'])
plt.subplot(2,2,4)
plt.plot(x , arctg, color='black')
plt.legend(['f(x) = arctg(x)'])
plt.grid()
plt.show()


