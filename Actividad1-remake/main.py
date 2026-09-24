from cajero import Cajero
from cliente import Cliente
from cuenta import Cuenta
from extraccion import extraerdinero
from dolar import Dolar
from peso import Peso
from transferencia import transferir
from versaldo import versaldo

sistema = True

cuenta_juan_pesos = Cuenta(100, 50000, Peso())
cuenta_juan_dolares = Cuenta(100, 1500, Dolar())
cuenta_ana_pesos = Cuenta(101, 30000, Peso())
cuenta_ana_dolares = Cuenta(101, 2300, Dolar())
cliente_juan = Cliente(30123456, "Juan", cuenta_juan_pesos, cuenta_juan_dolares)
cliente_ana = Cliente(30987654, "Ana", cuenta_ana_pesos, cuenta_ana_dolares)
clientes = [cliente_juan, cliente_ana]
cajero1 = Cajero(1, 1000000)


def elegir_cliente(moneda):
    print("\nClientes disponibles:")
    for cliente in clientes:
        cuenta = cliente.obtener_cuenta(moneda)
        print(cuenta.numero, "-", cliente.nombre)

    numero = input("Ingrese el numero de cuenta: ")
    for cliente in clientes:
        cuenta = cliente.obtener_cuenta(moneda)
        if str(cuenta.numero) == numero:
            return cuenta

    return None


def elegir_moneda():
    opcion = input("Ingrese la moneda (1: pesos, 2: dolares): ")
    if opcion == "1":
        return Peso()
    if opcion == "2":
        return Dolar()
    return None


def mostrar_menu():
    print("\n=== MENU DEL CAJERO ===")
    print("1. Consultar saldo")
    print("2. Extraer dinero")
    print("3. Depositar dinero")
    print("4. Transferir dinero")
    print("0. Salir")


while sistema:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        moneda = elegir_moneda()
        cuenta = elegir_cliente(moneda) if moneda is not None else None
        if cuenta is not None:
            print("Saldo:", versaldo(cuenta), moneda)
        else:
            print("No se encontro la cuenta.")

    elif opcion == "2":
        moneda = elegir_moneda()
        cuenta = elegir_cliente(moneda) if moneda is not None else None
        if cuenta is None:
            print("No se encontro la cuenta.")
            continue

        monto = int(input("Ingrese el monto a extraer: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif not cajero1.consultardd(monto):
            print("No hay suficiente saldo en el cajero.")
        elif extraerdinero(cajero1, cuenta, monto):
            print("Retiro exitoso.")
        else:
            print("No hay suficiente saldo en la cuenta.")

    elif opcion == "3":
        moneda = elegir_moneda()
        cuenta = elegir_cliente(moneda) if moneda is not None else None
        if cuenta is None:
            print("No se encontro la cuenta.")
            continue

        monto = int(input("Ingrese el monto a depositar: "))
        if cuenta.depositar(monto):
            print("Deposito exitoso.")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == "4":
        moneda = elegir_moneda()
        if moneda is None:
            print("Moneda invalida.")
            continue

        print("Cuenta de origen")
        origen = elegir_cliente(moneda)
        print("Cuenta de destino")
        destino = elegir_cliente(moneda)

        if origen is None or destino is None:
            print("No se encontro una de las cuentas.")
            continue

        monto = int(input("Ingrese el monto a transferir: "))
        if transferir(origen, destino, monto):
            print("Transferencia exitosa.")
        else:
            print("No se pudo realizar la transferencia.")

    elif opcion == "0":
        print("Gracias por usar el cajero.")
        sistema = False

    else:
        print("Opción inválida. Intentá otra vez.")