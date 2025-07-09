# Titulo: Cajero automático
# Descripcion: Simulación de un cajero automático que permite al usuario realizar operaciones bancarias básicas.
# Ejercicio del coblos de repericion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# Crear una aplicacion de cajero automatico.
# Funciones básicas:
# 1. Depositar
# 2. Retirar
# 3. Consultar saldo
# 4. Salir

# El saldo inical es de 1000.00
# Si relizas un retiro mayor al saldo, muestra un mensaje de error.

# Separador
separador = "*"*60

# Variables
saldo = 1000.00
activo = True

print(separador)
print("Bienvenido al Cajero Automático".center(60))
print(separador)

# Menú de opciones
menu = """1. Depositar
2. Retirar
3. Consultar saldo
4. Salir"""
# Bucle iterativo
while activo:
    print(separador)
    print(menu)
    print(separador)

    opcion = input("Ingrese una opción (1-4): ")
    print(separador)

    if opcion == "1":
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Monto inválido. El depósito debe ser mayor que cero.")
    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Error: Saldo insuficiente para realizar el retiro.")
        else:
            print("Monto inválido. El retiro debe ser mayor que cero.")
    elif opcion == "3":
        print(f"Saldo actual: ${saldo:.2f}")
    elif opcion == "4":
        print("Saliendo del cajero automático...")
        activo = False
    else:
        print("Opción no válida, por favor intente de nuevo.")

