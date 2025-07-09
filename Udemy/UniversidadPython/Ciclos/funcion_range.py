# Titulo: Función range en Python
# Descripción: Este script muestra cómo utilizar la función range para generar secuencias de números
# Cilos de repeticion.
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# General mente se utiliza para iterar sobre un rango de números en un bucle for.

# Sintaxis:
# range(start, stop, step)
# start: Valor inicial (incluido, por defecto es 0)
# stop: Valor final (excluido, obligatorio)
# step: Incremento (por defecto es 1)

# Ejemplo de uso de range
for i in range(1, 11):
    print(i, end=' ')
print()  # Imprime los números del 1 al 10 en una sola línea

# Ejemplo con un paso específico
for i in range(1, 11, 2):
    print(i, end=' ')
print()  # Imprime los números del 1 al 10 con un paso de 2 (1, 3, 5, 7, 9)
