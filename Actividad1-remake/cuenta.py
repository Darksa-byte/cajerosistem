class Cuenta:
	def __init__(self, numero, saldo):
		self.__numero = numero
		self.__saldo = saldo

	@property
	def numero(self):
		return self.__numero

	@property
	def saldo(self):
		return self.__saldo

	def depositar(self, monto):
		if monto <= 0:
			return False

		self.__saldo += monto
		return True

	def retirar(self, monto):
		if monto <= 0 or monto > self.__saldo:
			return False

		self.__saldo -= monto
		return True
