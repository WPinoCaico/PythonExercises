import urllib.request

page = urllib.request.urlopen("https://www.timeanddate.com/worldclock/fullscreen.html?n=131")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

x = respuesta2.find("<div id=i_time>")
x += 15

hora = respuesta2[x:x+8]

print ()

print (hora)