#Script de python para comparar 2 numeros enteros con la opcion de igualdad

print ("Programa de comparacion de 2 numeros enteros")

a = int(input("Ingrese el numero A: "))
b = int(input("Ingrese el numero B: "))

if (a>b):
	print ("El numero %d es mayor que el numero %d"%(a,b))

elif (a==b):
	print ('Los numeros "A" y "B" son iguales')

else:
	print ("El numero %d es mayor que el numero %d"%(b,a))


#Hacemos una pausa esperando por un "enter" para cerrar el programa
input()