import serial
import time
import os

arduino = serial.Serial('COM6', 9600)

time.sleep(2)

try:
	while 1:
		rawString = arduino.readline()
		print(rawString)
		time.sleep(1)
		ax = os.system("cls")

except:
	arduino.close()
	print "se ha cerrado adecuadamente"
	raw_input("ENTER PARA CERRAR EL CLI")