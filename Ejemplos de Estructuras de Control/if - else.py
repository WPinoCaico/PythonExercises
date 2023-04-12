#Script de python para comparar 2 numeros enteros sin contar con la opcion de igualdad

print ("Programa de comparacion de 2 numeros enteros")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))


if (a>b):
	print ("El numero %d es mayor que el numero %d"%(a,b))

else:
	print ("El numero %d es mayor que el numero %d"%(b,a))


#Hacemos una pausa esperando por un "enter" para cerrar el programa
input()