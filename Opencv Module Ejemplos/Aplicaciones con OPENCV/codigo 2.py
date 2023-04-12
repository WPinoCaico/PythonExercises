import cv2
import numpy as np
import os
import serial
import time

arduino = serial.Serial("COM5",9600)
time.sleep(2)


fondo = np.zeros((256,256,3),np.uint8)

img0 = cv2.imread("f0.png")
img1 = cv2.imread("f1.png")	

tx,ty = img0.shape[1],img0.shape[0]

z = 0

fondo[20:20+ty,55:55+tx]=img0

def tactil_sec(event,x,y,flags,param):
	global z
	if (event == cv2.EVENT_LBUTTONDOWN) and 88<x<168 and 88<y<168 and z==0:
		fondo[20:20+ty,55:55+tx]=img1
		z = 1
		arduino.write("1".encode())

	elif (event == cv2.EVENT_LBUTTONDOWN) and 88<x<168 and 88<y<168 and z==1:
		fondo[20:20+ty,55:55+tx]=img0	
		z = 0
		arduino.write("0".encode())



cv2.namedWindow('APLICACION')
cv2.setMouseCallback('APLICACION',tactil_sec)

while(1):
	cv2.imshow('APLICACION',fondo)
	if cv2.waitKey(20) == 27:
      		  break

arduino.close()
cv2.destroyAllWindows()

