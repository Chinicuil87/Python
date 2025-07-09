# Titulo: Calculadora
# Descripcion: Simulación de una calculadora que permite al usuario realizar operaciones matemáticas básicas.
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# Crear un aplicacion que contenga las siguientes operaciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# 5. Salir

# Separador
separador = "*" * 60

# Variables
activo = True

print(separador)
print("Bienvenido a la Calculadora".center(60))
print(separador)
# Menú de opciones
menu = """1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir"""

# Bucle iterativo
while activo:
    print(separador)
    print(menu)
    print(separador)

    opcion = int(input("Ingrese una opción (1-5): "))
    print(separador)

    if 1 <= opcion <= 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado = num1 + num2
        print(f"Resultado de la suma: {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"Resultado de la resta: {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"Resultado de la multiplicación: {resultado}")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado de la división: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == 5:
        print("Saliendo de la calculadora. ¡Hasta luego!")
        activo = False
    else:
        print("Opción no válida, por favor intente de nuevo.")
        activo = True
