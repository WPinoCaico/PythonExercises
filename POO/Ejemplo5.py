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

	def __init__(self,COLOR,MODELO,ESPEJOS,LLANTAS,VELOCIDADES):
		self.color = COLOR
		self.modelo = MODELO
		self.espejos = ESPEJOS
		self.llantas = LLANTAS
		self.velocidades = VELOCIDADES

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

if __name__ == "__main__": 

	auto_1 = vehiculo("Rojo","Mercedes",3,4,5)

	auto_1.caracteristicas()

	auto_1.encender()

	auto_1.acelerar(40)
	time.sleep(3)
	auto_1.frenar(50)