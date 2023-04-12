#Variables a usar

a = "Carlos"	#--> string
b = 25			#--> int
c = 22.14		#--> float
d = 5 + 3j		#--> complex
e = [1,2,3]		#--> list

#Metodo 1: Convirtiendo todas las variables a String.

print ("Mi nombre es "+a+". Tengo "+str(b)+" años de edad. "+"La temperatura actual es: "+str(c)+", el numero complejo es: "+str(d)+" y la lista es: "+str(e))

#Metodo 2: Los complejos, listas, tuplas no poseen equivalente en este metodo, solo quedaria convertirlos a otro tipo de variables como string.

print ("Mi nombre es %s. Tengo %d años de edad. La temperatura actual es: %f, el numero complejo es %s y la lista es %s "%(a,b,c,str(d),str(e)))

#Metodo 3: Metodo más usado y mas generico.

print ("Mi nombre es {}. Tengo {} años de edad. La temperatura actual es: {}, el numero complejo es {} y la lista es {} ".format(a,b,c,d,e))

input()
