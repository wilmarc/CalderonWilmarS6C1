import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt("dat.txt",delimiter=" ")
x=dat[:,0]
y=dat[:,1]

plt.figure()
plt.scatter(x,y,c="g",s=3)
plt.title("Solución a la Ecuación Diferencial")
plt.show()
