import serial
import time

arduino = serial.Serial("COM6", 9600)
#El tiempo es muy importante para que lleguen bien lo datos
time.sleep(2)


while 1:
	#Enviamos un dato al arduino (el arduino)
	dato = input("ESCRIBA 'ON' para encender, 'OFF' para apagar o 'EXIT' para cerrar el programa: ")
	if dato == "ON":
		v = "1"
		arduino.write(v.encode())
	elif dato == "OFF":
		v = "0"
		arduino.write(v.encode())
	elif dato == "EXIT":
		arduino.close()
		break
	else: 
		print ("escriba un dato entendible por el programa!")
		
		

