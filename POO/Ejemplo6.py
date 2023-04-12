from Ejemplo5 import vehiculo
import time

auto_1 = vehiculo("Rojo","Mercedes",3,4,5)

auto_1.caracteristicas()

auto_1.encender()

auto_1.acelerar(40)
time.sleep(3)
auto_1.frenar(50)