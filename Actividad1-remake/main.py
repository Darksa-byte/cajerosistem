from cajero import Cajero
from cliente import Cliente
from cuenta import Cuenta
from extraccion import extraerdinero
from transferencia import transferir
from versaldo import versaldo

sistema = True

cuenta_juan = Cuenta(101, 50000)
cuenta_ana = Cuenta(102, 30000)
cliente_juan = Cliente(30123456, "Juan", cuenta_juan)
cliente_ana = Cliente(30987654, "Ana", cuenta_ana)
clientes = [cliente_juan, cliente_ana]
cajero1 = Cajero(1, 1000000)


def elegir_cliente():
    print("\nClientes disponibles:")
    for cliente in clientes:
        print(cliente.cuenta.numero, "-", cliente.nombre)

    numero = input("Ingrese el numero de cuenta: ")
    for cliente in clientes:
        if str(cliente.cuenta.numero) == numero:
            return cliente

    return None


def mostrar_menu():
    print("\n=== MENU DEL CAJERO ===")
    print("1. Consultar saldo")
    print("2. Extraer dinero")
    print("3. Depositar dinero")
    print("4. Transferir dinero")
    #print("5. Ver dinero del cajero")
    print("0. Salir")


while sistema:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        cliente = elegir_cliente()
        if cliente is not None:
            print("Saldo de", cliente.nombre, ": $", versaldo(cliente.cuenta))
        else:
            print("No se encontro la cuenta.")

    elif opcion == "2":
        cliente = elegir_cliente()
        if cliente is None:
            print("No se encontro la cuenta.")
            continue

        monto = int(input("Ingrese el monto a extraer: "))
        if extraerdinero(cajero1, cliente.cuenta, monto):
            print("Retiro exitoso.")
        else:
            print("No se pudo realizar el retiro. Revise el saldo y el cajero.")

    elif opcion == "3":
        cliente = elegir_cliente()
        if cliente is None:
            print("No se encontro la cuenta.")
            continue

        monto = int(input("Ingrese el monto a depositar: "))
        if cliente.cuenta.depositar(monto):
            print("Deposito exitoso.")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == "4":
        print("Cuenta de origen")
        origen = elegir_cliente()
        print("Cuenta de destino")
        destino = elegir_cliente()

        if origen is None or destino is None:
            print("No se encontro una de las cuentas.")
            continue

        monto = int(input("Ingrese el monto a transferir: "))
        if transferir(origen.cuenta, destino.cuenta, monto):
            print("Transferencia exitosa.")
        else:
            print("No se pudo realizar la transferencia.")

    #elif opcion == "5":
        #print("Dinero disponible en el cajero: $", cajero1.dinerodisponible)

    elif opcion == "0":
        print("Gracias por usar el cajero.")
        sistema = False

    else:
        print("Opción inválida. Intentá otra vez.")