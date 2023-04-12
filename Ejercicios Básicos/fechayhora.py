#El uso de date time se puede usar para fechas y horas
import datetime

#el now nos dará el tiempo actual basada en el sistema
tiempoactual = datetime.datetime.now()
print(tiempoactual)

#si se quiere pedir solo los datos exactos (día, mes,año, hora, minutos y segundos), se puede usar el comando strftime

print(tiempoactual.strftime('%d/%m/%y %H:%M:%S'))