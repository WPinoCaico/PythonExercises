#funcion para mostrar en pantalla los numeros del 1 al 100 haciendo uso de la funcion 
#"while(1)" (bucle infinito).
#Y la funcion "break" para romper una secuencia (en este caso la funcion "while(1)").

b = 1

while (1):
	print (b)
	b = b+1
	if b > 100:
		break

#Hacemos una pausa esperando por un "enter" para cerrar el programa
input()