import cv2
import numpy as np
import os

fondo = np.zeros((256,256,3),np.uint8)

img0 = cv2.imread("play_off.png")
img1 = cv2.imread("play_on.png")	

tx,ty = img0.shape[1],img0.shape[0]

z = 0

fondo[88:88+ty,88:88+tx]=img0

def tactil_sec(event,x,y,flags,param):
	global z
	if (event == cv2.EVENT_LBUTTONDOWN) and 88<x<168 and 88<y<168 and z==0:
		fondo[88:88+ty,88:88+tx]=img1
		z = 1
		os.startfile("AHORA_Y_AQUI.mp4")

	elif (event == cv2.EVENT_LBUTTONDOWN) and 88<x<168 and 88<y<168 and z==1:
		fondo[88:88+ty,88:88+tx]=img0	
		z = 0
		os.system("TASKKILL /F /IM wmplayer.exe")



cv2.namedWindow('APLICACION')
cv2.setMouseCallback('APLICACION',tactil_sec)

while(1):
	cv2.imshow('APLICACION',fondo)
	if cv2.waitKey(20) == 27:
      		  break

cv2.destroyAllWindows()

