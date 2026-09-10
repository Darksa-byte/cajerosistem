def extraerdinero(cajero, cuenta, monto):
    if cajero.consultardd(monto) and cuenta.retirar(monto):
        cajero.extraerdinero(monto)
        return True

    return False