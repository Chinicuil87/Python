

# Programa que simula un menu iterativo para crear y eliminar cuentas.
# si el usuario elige.
# 1. Crear cuenta, muetra solo un mensaje de confirmacion.
# 2. Eliminar cuenta, muestra un mensaje de confirmacion.
# 3. Salir, finaliza el programa.


# separador
separador = "*"*60

# Variable
salir = False

# Menu iterativo
menu = """1. Crear cuenta 
2. Eliminar cuenta
3. Salir """

# Bucle iterativo
while not salir:

    print(separador)
    print("Bienvenido al menu de cuentas".center(60))
    print(separador)
    print(menu)
    print(separador)
    opcion = input("Ingrese una opcion (1-3): ")
    print(separador)

    if opcion == "1":
        print("Cuenta creada con exito.")
    elif opcion == "2":
        print("Cuenta eliminada con exito.")
    elif opcion == "3":
        print("Saliendo del programa...")
        salir = True
    else:
        print("Opcion no valida, por favor intente de nuevo.")
