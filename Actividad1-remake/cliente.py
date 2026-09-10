class Cliente:
	def __init__(self, dni, nombre, cuenta):
		self.__dni = dni
		self.__nombre = nombre
		self.__cuenta = cuenta

	@property
	def dni(self):
		return self.__dni

	@property
	def nombre(self):
		return self.__nombre

	@property
	def cuenta(self):
		return self.__cuenta

	def mostrar_datos(self):
		print("Cliente:", self.__nombre)
		print("DNI:", self.__dni)
		print("Numero de cuenta:", self.__cuenta.numero)
