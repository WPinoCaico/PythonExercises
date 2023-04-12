#CLASE
class vehiculo:
	#ATRIBUTOS
	color = ""
	modelo = ""
	espejos = 0
	llantas = 0
	velocidades = 0
	
	def caracteristicas(self):
		print ("COLOR:",self.color)
		print ("MODELO:",self.modelo)
		print ("ESPEJOS:",self.espejos)
		print ("LLANTAS:",self.llantas)
		print ("VELOCIDADES:",self.velocidades)
	

#AGREGANDO ATRIBUTOS
auto_1 = vehiculo()
auto_1.color = "Rojo"
auto_1.modelo = "Mercedes"
auto_1.espejos = 3
auto_1.llantas = 4
auto_1.velocidades = 5

auto_1.caracteristicas()

