#Compila el código C++
g++ CalderonWilmarS6C1.cpp

#Redirige los datos provenientes del archivo .cpp al archivo dat.txt
./a.out >> dat.txt

#Ejecuta el scipt de Python que grafica los datos
python CalderonWilmarPlot.py
