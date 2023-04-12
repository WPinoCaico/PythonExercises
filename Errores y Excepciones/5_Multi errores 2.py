try :
	d = {'a':1}
	d['b']
	1+'a'
except NameError:
	print ("Error tipo NameError")

except KeyError:
	print ("Error tipo KeyError")