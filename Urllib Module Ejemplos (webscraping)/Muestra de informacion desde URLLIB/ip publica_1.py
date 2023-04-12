import urllib.request

page = urllib.request.urlopen("https://www.whatismyip.org")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)