import serial
import time

arduino = serial.Serial("COM5", 9600)
#El tiempo es muy importante para que lleguen bien lo datos
time.sleep(2)


while 1:
	#Enviamos un dato al arduino (el arduino)
	dato = input("ESCRIBA UN NUMERO ENTRE 0 y 255, 'E' PARA SALIR:\n")
	if dato=="E":
		arduino.close()
		break
	elif 0<=int(dato)<=255:
		arduino.write(dato.encode())
	else: 
		print ("\nEscriba un dato del rango!\n")

		
		

