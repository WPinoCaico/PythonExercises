import matplotlib.pyplot as plt
import time
import random
import serial

arduino = serial.Serial('COM5',9600)

time.sleep(2) 
 
#vectores de los ejes "X" y "Y" inicial
xdata = [0,1,2,3,4,5,6,7,8,9]
ydata = [0,0,0,0,0,0,0,0,0,0]
 
#definir los limites de la grafica
axes = plt.gca()
axes.set_xlim(0, 9)
axes.set_ylim(+20, +45)



#agregar los datos y extraer el dato
line, = axes.plot(xdata, ydata, 'y')

line.set_xdata(xdata)

while 1:
	
	rawString = arduino.readline()
	ydata = ydata[1:]
	ydata.append(int(rawString))
	line.set_ydata(ydata)
	plt.draw()
	plt.pause(1e-17)
	time.sleep(1)

arduino.close()