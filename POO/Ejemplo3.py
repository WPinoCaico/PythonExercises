import time

#CLASE
class vehiculo:
	#ATRIBUTOS ESTATICOS
	color = ""
	modelo = ""
	espejos = 0
	llantas = 0
	velocidades = 0
	#ATRIBUTOS DINAMICOS
	estado = 0
	velocidad_actual = 0

	def caracteristicas(self):
		print ("COLOR:",self.color)
		print ("MODELO:",self.modelo)
		print ("ESPEJOS:",self.espejos)
		print ("LLANTAS:",self.llantas)
		print ("VELOCIDADES:",self.velocidades,"\n")

	def encender(self):
		print ("ENCENDIENDO AUTO...")
		time.sleep(1)
		self.estado = 1
		print ("AUTO ENCENDIDO")
		
	def apagar(self):
		print ("APAGANDO AUTO...")
		time.sleep(1)
		self.estado = 0
		print ("AUTO APAGADO")
		
	def acelerar(self,velocidad):
		if self.estado == 1:
			if velocidad > self.velocidad_actual:
				for i in range (self.velocidad_actual,velocidad,2):
					print ("El auto esta acelerando a una velocidad de:", i,"Km/h")
					time.sleep(0.5)
				self.velocidad_actual = velocidad	
				print ("Velocidad actual es de",velocidad,"Km/h")
			else: print ("EL VEHICULO ESTA A UNA VELOCIDAD MAYOR!")   
		else: print ("ENCENDER EL VEHICULO PRIMERO!")	
	
	def frenar(self,velocidad):
		if self.estado == 1:
			if velocidad < self.velocidad_actual:
				for i in range (self.velocidad_actual,velocidad,-2):
					print ("El auto esta frenando a una velocidad de:", i,"Km/h")
					time.sleep(0.5)
				self.velocidad_actual = velocidad
				print ("Velocidad actual es de",velocidad,"Km/h")
			else: print ("EL VEHICULO ESTA A UNA VELOCIDAD MENOR!")
		else: "EL VEHICULO ESTA APAGADO."

#AGREGANDO ATRIBUTOS
auto_1 = vehiculo()
auto_1.color = "Rojo"
auto_1.modelo = "Mercedes"
auto_1.espejos = 3
auto_1.llantas = 4
auto_1.velocidades = 5

auto_1.caracteristicas()

auto_1.encender()

#auto_1.apagar()

auto_1.acelerar(40)
time.sleep(3)
auto_1.frenar(50)