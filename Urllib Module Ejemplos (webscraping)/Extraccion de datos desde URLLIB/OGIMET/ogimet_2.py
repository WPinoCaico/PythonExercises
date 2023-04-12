import urllib.request

page = urllib.request.urlopen("http://ogimet.com/display_metars2.php?lugar=SPJC&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=2018&mes=06&day=03&hora=00&anof=2018&mesf=06&dayf=04&horaf=00&minf=59&enviar=Ver")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

a = len(respuesta2)

x2=-1
lis =[]

for i in range(a):
	x = respuesta2.find("<pre>",i)
	if x2 == x:
		pass
	elif x == -1:
		break
	else:
		lis.append(x+5)
		x2 = x

x2=-1
lis2=[]

for i in range(a):
	x = respuesta2.find("</pre>",i)
	if x2 == x:
		pass
	elif x == -1:
		break
	else:
		lis2.append(x)
		x2 = x

#print (lis)
#print ()
#print (lis2)

for i in range(len(lis)):
	print ((respuesta2[lis[i]:lis2[i]]).replace("\n"," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," "))
	print()	
		