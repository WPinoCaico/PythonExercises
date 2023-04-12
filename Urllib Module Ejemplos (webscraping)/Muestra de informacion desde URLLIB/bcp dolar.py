import urllib.request

resultado = urllib.request.urlopen("http://www.bcrp.gob.pe/")

#variable tipo bytes
respuesta = resultado.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)