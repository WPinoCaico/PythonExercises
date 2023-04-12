import serial
import time
import os

arduino = serial.Serial('COM6', 9600)

time.sleep(2)

try:
	while 1:
		rawString = arduino.readline()

		rawString = (str(rawString))[2:-5]

		print(rawString)
	
		time.sleep(1)
	
		ax = os.system("cls")

except:

	arduino.close()
	print ("se ha cerrado adecuadamente")
	input("ENTER PARA CERRAR EL CLI")