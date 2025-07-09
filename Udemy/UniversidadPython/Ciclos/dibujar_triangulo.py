# Titulo: Dibujar un triángulo con asteriscos
# Descripcion: Este script dibuja un triángulo utilizando asteriscos.
# Ejercicio del coblos de repericion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# se debe pedir el número de filas del triángulo

# Separador
separador = "*" * 60
# Título del programa
print(separador)
print("Dibujar un triángulo con asteriscos".center(60))
print(separador)
# Solicitar el número de filas del triángulo
numero_filas = int(input("Ingrese el número de filas del triángulo: "))
# Bucle for para dibujar el triángulo
for i in range(1, numero_filas + 1):
    # Imprimir espacios en blanco
    print(" " * (numero_filas - i), end="")
    # Imprimir asteriscos
    print("*" * (2 * i - 1))
    
# Fin del programa
print(separador)
