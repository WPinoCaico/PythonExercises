#Importamos la librerias
import cv2
import numpy as np

#Creamos una variable donde guardamos un "numpy-array" de extension : (x,y) = (256,256), donde
#cada elemento del array (matriz) es una lista de 3 elementos cuyo valor sera : (0,0,0) (por eso es el "zeros")
fondo = np.zeros((256,256,3),np.uint8)
for x in range(0,256):
	for y in range(0,256):
		fondo[y,x] = (255,0,0)

#Mostramos la variable "fondo" que mas que una matriz, es una representacion numerica de una imagen RGB
cv2.imshow("Azul total",fondo)

#Pausamos la imagen esperando por una tecla para cerrar
cv2.waitKey(0)