from peso import Peso


class Cliente:
	def __init__(self, dni, nombre, cuenta_pesos=None, cuenta_dolares=None):
		self.__dni = dni
		self.__nombre = nombre
		self.__cuentas = {}
		for cuenta in (cuenta_pesos, cuenta_dolares):
			if cuenta is not None:
				self.__cuentas[type(cuenta.moneda)] = cuenta

	@property
	def dni(self):
		return self.__dni

	@property
	def nombre(self):
		return self.__nombre

	@property
	def cuenta(self):
		return self.__cuentas.get(Peso)

	@property
	def cuentas(self):
		return self.__cuentas.copy()

	def obtener_cuenta(self, moneda):
		return self.__cuentas.get(type(moneda))

	def mostrar_datos(self):
		print("Cliente:", self.__nombre)
		print("DNI:", self.__dni)
		for cuenta in self.__cuentas.values():
			print("Numero de cuenta:", cuenta.numero, "-", cuenta.moneda)
