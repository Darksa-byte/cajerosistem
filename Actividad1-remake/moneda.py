class Moneda:
	def __init__(self, codigo, nombre):
		self.__codigo = codigo
		self.__nombre = nombre

	@property
	def codigo(self):
		return self.__codigo

	@property
	def nombre(self):
		return self.__nombre

	def __str__(self):
		return self.nombre

	def __eq__(self, otra):
		return type(self) is type(otra)

	def __hash__(self):
		return hash(type(self))