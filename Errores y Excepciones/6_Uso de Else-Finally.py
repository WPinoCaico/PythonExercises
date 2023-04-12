try :
	d = {'a':1}
	d['b']
	1+'a'
	a = 1/0
except NameError:
	print ("Error tipo NameError")

except KeyError:
	print ("Error tipo KeyError")

#Solo se ejecuta cuando no ha ocurrido ningun error
else:
	print ("No hubo ningun problema")

#Se ejecuta despues del try independiente de si hubo o no error
finally:
	print ("Terminamos en Try-except")