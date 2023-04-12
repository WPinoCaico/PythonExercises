import serial
import time

arduino = serial.Serial("COM6", 9600)

#El tiempo es muy importante para que lleguen bien lo datos
time.sleep(2)

while (1):
	var = input("Ingrese 'e' para encender, 'a' para apagar y 'c' para cerrar: ")
	if var == 'e' or var == 'a':
		arduino.write(var.encode())
	elif (var == 'c'):	
		arduino.close()
		break
	else: 
		print ("Escriba un comando entendible!")