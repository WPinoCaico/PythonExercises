import cv2	#Importamos la libreria

#llamamos una imagen (se recomienda que este en el mismo lugar donde esta el script)
imagen = cv2.imread("tyler1.jpg")

#Funcion para cambiar las extensiones de la imagen (1er argumento: nombre de la imagen; 2do argumento: extension
#horizontal y vertical de la imagen (x,y))
imagen2 = cv2.resize(imagen,(512,680))

#Funcion para mostrar la imagen, el 1er argumento es la etiqueta, el 2do es el nombre de la imagen
cv2.imshow("Imagen",imagen)
cv2.imshow("Imagen2",imagen2)

#Funcion para que la imagen mostrada permanesca en pausa y no se cierre (se cerrara con el presionar
#de una tecla).
cv2.waitKey(0)

