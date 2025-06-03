# Titulo: Operadores asignacion
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Los operadores de asignacion nos permiten asignar valores a variables.
# Los operadores de asignacion son:
# =, +=, -=, *=, /=, //=, %=, **=
# =: Asignacion simple
# +=: Asignacion de suma
# -=: Asignacion de resta
# *=: Asignacion de multiplicacion
# /=: Asignacion de division
# //=: Asignacion de division entera
# %=: Asignacion de modulo
# **=: Asignacion de potencia

# Sintaxis:
# variable = valor

numero = 10  # Asignacion simple
print("Numero: ", numero)  # 10
texto = "Hola Mundo"  # Asignacion simple
print("Texto: ", texto)  # Hola Mundo

# Asignacion de multiples
# sintaxis:
# variable1, variable2, variable3 = valor1, valor2, valor3
numero1, numero2, numero3 = 10, 20, 30  # Asignacion de multiples
print("Numero1: ", numero1)  # 10
print("Numero2: ", numero2)  # 20
print("Numero3: ", numero3)  # 30

# Asignacion en cadena
# sintaxis:
# variable = valor1, valor2, valor3

a = b = c = 10  # Asignacion en cadena
print("A: ", a)  # 10
print("B: ", b)  # 10
print("C: ", c)  # 10

# Ejercico: Intercambio de variables, sin variable temporal
# sintaxis:
# variable1, variable2 = variable2, variable1

a = 10
b = 20
print("Antes del intercambio: ")
print("A: ", a)  # 10
print("B: ", b)  # 20
a, b = b, a  # Intercambio de variables
print("Despues del intercambio: ")
print("A: ", a)  # 20
print("B: ", b)  # 10

# Recibir multiples valores de enrada de un usuario

nombre, edad, ciudad = input(
    "Introduce tu nombre, edad y ciudad (separados por coma) :").split(",")
print("Nombre: ", nombre)  # Nombre
print("Edad: ", edad)  # Edad
print("Ciudad: ", ciudad)  # Ciudad
