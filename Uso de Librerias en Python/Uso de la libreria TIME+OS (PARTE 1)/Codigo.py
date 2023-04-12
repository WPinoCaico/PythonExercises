#Importamos las respectivas librerias
import time
import os

#Ingresamos un dato
a = input("INGRESE SU NOMBRE: ")

#Imprimimos un mensaje haciendo uso de ese dato
print ("BUENOS DIAS %s !"%a)

#Esperamos 2 segundos:
time.sleep(2)

#Limpiamos la pantalla:
ax = os.system('cls')

#Mostramos un ultimo mensaje:
print ("HASTA LUEGO!...")

#Esperamos unos 2 ultimos segundos 
time.sleep(2)

#Limpiamos la pantalla una ultima vez
ax = os.system('cls')

#Para evitar el cierre automatico, usamos "input()" a modo de pausa
input("ENTER PARA CERRAR EL PROGRAMA...")