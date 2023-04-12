#NOTA: en este caso no hay forma de cerrar por ESC, poner Ctrl+C para terminar 
#el bucle

import serial
import time
import os

#Habilitamos el puerto serial, "COM6" es el puerto USB y "9600" es 
#el baudio (velocidad de transmision)

arduino = serial.Serial('COM6', 9600)

#Esperamos obligatoriamente 2 segundos para darle tiempo a 
#que responda el puerto serie

time.sleep(2)

#Ciclo while para leer continuamente

while 1:
	#recibimos la informacion haciendo uso de la funcion "arduino.readline()"
	
	rawString = arduino.readline()
	
	#"imprime en el CLI de python lo recibido
	
	print(rawString)
	
	#esperamos 1 segundo antes de volver a solicitar dato serial
	
	time.sleep(1)
	
	#limpiamos la pantalla

	ax = os.system("cls")

#cerramos adecuadamente el puerto serial

arduino.close()
