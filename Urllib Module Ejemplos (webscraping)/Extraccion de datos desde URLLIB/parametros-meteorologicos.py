import urllib.request

#Para que la pagina reconozca que es una persona, es necesario ingresar a la pagina de
#manera manual una primera y unica vez
page = urllib.request.urlopen("https://deltavolt.pe/weather/clientraw.txt")

#variable tipo bytes
respuesta = page.read()

#variable tipo string
respuesta2 = respuesta.decode()

respuesta3 = respuesta2.split(" ")


print ("LA TEMPERATURA ACTUAL ES: {} ºC".format(respuesta3[5]))

print ("LA HUMEDAD ACTUAL ES: {} %".format(respuesta3[6]))

print ("LA PRESION ACTUAL ES: {} hPa".format(respuesta3[7]))

print ("LA RADIACION ACTUAL ES: {} W/m2".format(respuesta3[-41]))