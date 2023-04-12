#Área de un circulo, a traves de instroducir su radio
#el áea de un circulo es igual a pi por el radio al cuadrado
#de la librería se puede sacar los datos de pi
from math import pi

r = float(input('Radio del circulo: '))

area= pi * r ** 2

print('El área del circulo es {}'.format(area))