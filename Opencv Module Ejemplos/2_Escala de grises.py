import cv2

#Llamamos la imagen
imagen = cv2.imread("tyler1.jpg")

#Funcion de conversion a escala de grises
imagen2 = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#Mostramos solo la version en escala de grises
cv2.imshow('imagen',imagen2)

#Pausamos
cv2.waitKey()
