try :
	1+'a'
	d = {'a':1}
	d['b']
except (KeyError,TypeError) as dato:
	print (dato)
	print ("Se ha evitado el cierre de programa!")