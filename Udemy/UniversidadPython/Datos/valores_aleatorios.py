# Titulo: Valores aleatorios
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# randint() devuelve un numero entero aleatorio entre dos valores.

# Sintaxis:
# random.randint(inicio, fin)

# para usar la funcion randint(), se debe importar el modulo random.
import random
from random import randint

print("Valores aleatorios")

# Numero aleatorio entre 1 y 10
numero_aleatorio = 0
numero_aleatorio = random.randint(1, 10)  # 1 y 10
print("Numero aleatorio: ", numero_aleatorio)  # 1 y 10

# Numero aleatorio entre 1 y 100
numero_aleatorio = 0
numero_aleatorio = random.randint(1, 100)  # 1 y 100
print("Numero aleatorio: ", numero_aleatorio)  # 1 y 100

# Simular dado
dado = randint(1, 6)  # 1 y 6
print("Dado: ", dado)  # 1 y 6
