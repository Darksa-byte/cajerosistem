from moneda import Moneda


class Dolar(Moneda):
	def __init__(self):
		super().__init__("USD", "dolares")