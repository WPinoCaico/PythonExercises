import urllib.request

page = urllib.request.urlopen("http://ogimet.com/display_metars2.php?lugar=SPJC&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=2018&mes=06&day=03&hora=00&anof=2018&mesf=06&dayf=04&horaf=00&minf=59&enviar=Ver")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)