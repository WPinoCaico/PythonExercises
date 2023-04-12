import serial
import time

arduino = serial.Serial("COM5", 9600)
#El tiempo es muy importante para que lleguen bien lo datos
time.sleep(2)


while 1:
	#Enviamos un dato al arduino (el arduino)
	dato = raw_input("ESCRIBA UN NUMERO ENTRE 0 y 9, 'E' PARA SALIR:\n")
	if dato=="E":
		arduino.close()
		break
	elif 0<=int(dato)<=25:
		arduino.write(dato)
	else: 
		print ("\nEscriba un dato del rango!\n")

		
		

