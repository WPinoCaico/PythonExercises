#Importamos la librerias
import cv2
import numpy as np

#Fondo completamente oscuro
fondo = np.zeros((256,256,3),np.uint8)

for i in range(0,256):
	fondo[0:i,0:i] = [255,255,255]
	cv2.imshow("Fondo dinamico",fondo)
	cv2.waitKey(20)

for i in range(0,256):
	fondo[0:i,0:i] = [0,0,0]
	cv2.imshow("Fondo dinamico",fondo)
	cv2.waitKey(20)

#Pausamos la imagen esperando por una tecla para cerrar
cv2.waitKey(0)