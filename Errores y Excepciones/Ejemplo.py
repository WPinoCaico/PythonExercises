import ast

print ("Programa para ordenar los numeros de una lista\n")

a = 0

while (a == 0):
	try :
		b = ast.literal_eval(input("Ingrese los valores en una lista: "))
		c = sorted(b)
		a = 1
	except SyntaxError:
		print ("No se olvide de colocar bien los corchetes!, ingrese de nuevo...\n")
	except IndexError:
		print ("Ingrese la informacion dentro de los corchetes!, ingrese de nuevo...\n")
	except ValueError:
		print ("Variable inexistente!, ingrese de nuevo...\n")
	except TypeError:
		print ("Ingrese solo valores numericos en la lista!, ingrese de nuevo...\n")


print ("Los valores ordenados son: {} ".format(c))