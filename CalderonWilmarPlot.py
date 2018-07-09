import numpy as np
import matplotlib.pyplot as plt


#Importa los datos del archivo dat.txt
dat=np.genfromtxt("dat.txt",delimiter=" ")

#Defien a x como la primera columna y y como la segunda columna
x=dat[:,0]
y=dat[:,1]

#Genera la gráfica de los datos y los muestra en pantalla.
plt.figure()
plt.scatter(x,y,c="g",s=3)
plt.title("Solución a la Ecuación Diferencial")
plt.show()
