#Importamos la librerias
import cv2
import numpy as np

imagen = cv2.imread("tyler1.jpg")

#Creamos una variable donde guardamos un "numpy-array" de extension : (x,y) = (512,512), donde
#cada elemento del array (matriz) es una lista de 3 elementos cuyo valor sera : (0,0,0) (por eso es el "zeros")
fondo = np.zeros((512,512,3),np.uint8)
fondo[:] = [0,255,0]

extension_y=imagen.shape[0]
extension_x=imagen.shape[1]

fondo[90:90+extension_y,130:130+extension_x] = imagen

#Mostramos la variable "fondo" que mas que una matriz, es una representacion numerica de una imagen RGB
cv2.imshow("Azul total",fondo)

#Pausamos la imagen esperando por una tecla para cerrar
cv2.waitKey(0)