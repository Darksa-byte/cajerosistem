def transferir(cuenta_origen, cuenta_destino, monto):
	if cuenta_origen.moneda != cuenta_destino.moneda:
		return False

	if cuenta_origen.retirar(monto):
		return cuenta_destino.depositar(monto)

	return False
