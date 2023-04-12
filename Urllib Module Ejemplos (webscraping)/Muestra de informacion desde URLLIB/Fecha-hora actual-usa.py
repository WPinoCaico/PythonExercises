import urllib.request

resultado = urllib.request.urlopen("http://just-the-time.appspot.com/")

#variable tipo bytes
respuesta = resultado.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)