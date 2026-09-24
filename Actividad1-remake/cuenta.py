from peso import Peso


class Cuenta:
	def __init__(self, numero, saldo, moneda=None):
		self.__numero = numero
		self.__saldo = saldo
		self.__moneda = moneda if moneda is not None else Peso()

	@property
	def numero(self):
		return self.__numero

	@property
	def saldo(self):
		return self.__saldo

	@property
	def moneda(self):
		return self.__moneda

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
