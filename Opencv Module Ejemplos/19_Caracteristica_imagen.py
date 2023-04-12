import cv2
import numpy as np
import os

img = np.zeros((128,128,3),np.uint8)

print ("Bienvenidos al programa para ver las caracteristicas de una imagen")
print ("Ingrese el nombre de la imagen con su extension (imagen.extension)")
a = input()
def click(event,x,y,flags,param):  	
	if event == cv2.EVENT_LBUTTONDOWN :	
		os.system('cls')
		imagen = cv2.imread(a)
		print ("Extension de la imagen:")
		print (imagen.shape)
		print ("Coordenadas X: ",x)
		print ("Coordenadas Y: ",y)		   	    
		print ("Color en formato BGR: ")
		z = imagen[y,x]
		print (z)
		img[:]=(z[0],z[1],z[2])
		cv2.imshow('color',img)

imagen = cv2.imread(a)
print ("Extension de la imagen:")
print (imagen.shape)
cv2.imshow('image',imagen)
cv2.namedWindow('image')
cv2.setMouseCallback('image',click)
while(1):	
	if cv2.waitKey(20) == 27:
		break
cv2.destroyAllWindows()