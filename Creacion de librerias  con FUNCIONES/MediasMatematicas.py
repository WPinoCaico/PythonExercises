def Aritmetica(x):
	u = 0
	for i in range(len(x)):
		u += x[i]
	return (u/len(x))

def Geometrica(y):
	w = 1
	for i in range(len(y)):
		w *= y[i]
	return pow(w,(1/len(y)))
 
def Armonica(z):
	v = 0
	for i in range(len(z)):
		v += 1/z[i]
	return (len(z)/v)
	
def Cuadratica(t):
	s = 0
	for i in range(len(t)):
		s += t[i]*t[i]
	return pow((s/len(t)),0.5)
	

