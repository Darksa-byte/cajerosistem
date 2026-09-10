def transferir(cuenta_origen, cuenta_destino, monto):
	if cuenta_origen.retirar(monto):
		cuenta_destino.depositar(monto)
		return True

	return False
