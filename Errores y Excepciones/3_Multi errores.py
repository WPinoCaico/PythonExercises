try :
	d = {'a':1}
	d['b']
	1+'a'
except (TypeError,KeyError):
	print ("se ha evitado el error! :)")