import cv2	#Importamos la libreria
#llamamos una imagen (se recomienda que este en el mismo lugar donde esta el script)
imagen = cv2.imread("tyler1.jpg")
#convertimos a un formato de escala de grises
imagen2 = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
#Mostramos el resultado
cv2.imshow("Figura1",imagen2)
#Esperamos por una tecla
cv2.waitKey(0)
#Cerramos todas la GUI de OPENCV
cv2.destroyAllWindows()
#Guardamos la imagen (1er argumento: nombre con el que se guardara + extension, 2do argumento: nombre de la
#variable que contiene la imagen)
cv2.imwrite("resultado.png",imagen2)
#Mostramos en la ventana de comandos una confirmacion de que se guardo la imagen
print ("Se ha guardado la imagen!")
#esperamos por otra tecla
print ("presione una tecla para cerrar")
raw_input()
