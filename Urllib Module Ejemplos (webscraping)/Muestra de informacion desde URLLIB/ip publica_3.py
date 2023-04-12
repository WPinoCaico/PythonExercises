import urllib.request

page = urllib.request.urlopen("http://icanhazip.com/")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)