import serial
import time

#Habilitamos el puerto serial, "COM5" es el puerto USB y "9600" es 
#el baudio (velocidad de transmision)

arduino = serial.Serial('COM5', 9600)

#Esperamos obligatoriamente 2 segundos para darle tiempo a 
#que responda el puerto serie

time.sleep(2)

#recibimos la informacion haciendo uso de la funcion "arduino.readline()"

rawString = arduino.readline()

#imprime en el CLI de python lo recibido convirtiendolo primero a String
# ya que en el caso de python 3, la informacion es recibida en
#formato bytes.


print (rawString.decode("utf-8"))

print (type(rawString.decode("utf-8")))

#Cerramos adecuadamente el puerto serial
arduino.close()

#Esperamos por un "enter" para cerrar el CLI
input("ENTER PARA CERRAR")