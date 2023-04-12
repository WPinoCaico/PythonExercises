import cv2

imagen = cv2.imread("tyler1.jpg")

#Invertimos la imagen ( R,G,B) --> (255-R,255-G,255-B)
imagen2 = ~imagen

#Funcion de conversion a formato "XYZ"
imagen3 = cv2.cvtColor(imagen,cv2.COLOR_BGR2XYZ)

cv2.imshow("Figura1",imagen)
cv2.imshow("Figura2",imagen2)
cv2.imshow("Figura3",imagen3)
cv2.waitKey(0)