# Titulo: Generador de ID
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Solicita crer un sistema de generacion de ID unico para cada persona.

# Valores solicitados:
# Nombre
# Apellido
# Año de nacimiento (YYYY)

# Proceso:
# Del valor de nombre, se usaran las 2 primeras letras y se convertiran a mayusculas.
# Del valor de apellido, se usaran las 2 primeras letras y se convertiran a mayusculas.
# Del valor de año de nacimiento, se usaran los 2 ultimos digitos y se convertiran a minusculas.
# El sistema debera generar un valor aleatorio de 4 digitos con ayuda de randint

# Final mente con los datos optenidos se generara un ID unico de la siguiente manera:

# nombre -> Cesar -> CE
# apellido -> Lopez -> LO
# año -> 1990 -> 90
# numero aleatorio -> randint -> 1234
# resultado -> CELO901234

from random import randint

separador = "*"*50

print(separador)
print("Generador de ID".center(50))
print(separador)
# Obtener datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
año = input("Ingrese su año de nacimiento (YYYY): ")
print(separador)

# Obtener los 2 primeros caracteres del nombre y convertirlos a mayusculas
nombre = nombre[0:2].upper()
# Obtener los 2 primeros caracteres del apellido y convertirlos a minusculas
apellido = apellido[0:2].upper()
# Obtener los 2 ultimos digitos del año y convertirlos a minusculas
año = año[-2:]
# Obtener un numero aleatorio de 4 digitos
numero_aleatorio = randint(1000, 9999)
# Generar el ID
id = nombre + apellido + año + str(numero_aleatorio)
# Mostrar el ID
print("Su ID es: ", id)
print(separador)
print("Gracias por usar el generador de ID".center(50))
print(separador)
print("Fin del programa".center(50))
print(separador)
