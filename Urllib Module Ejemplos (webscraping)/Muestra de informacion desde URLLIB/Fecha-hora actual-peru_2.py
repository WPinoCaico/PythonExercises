import urllib.request

page = urllib.request.urlopen("https://www.timeanddate.com/worldclock/fullscreen.html?n=131")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

print (type(respuesta2))

print ()

print (respuesta2)