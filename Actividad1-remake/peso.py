from moneda import Moneda


class Peso(Moneda):
	def __init__(self):
		super().__init__("ARS", "pesos")