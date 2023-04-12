#funcion para mostrar en pantalla los numeros del 1 al 100 haciendo uso de la funcion "while"

b = 1
a = 0

#Bucle "while" (Mientras), seguira haciendo el bucle hasta que la condicion sea falsa
while (a == 0):
	print (b)
	b = b+1
	if b > 100:
		a = 1

#Hacemos una pausa esperando por un "enter" para cerrar el programa
input()