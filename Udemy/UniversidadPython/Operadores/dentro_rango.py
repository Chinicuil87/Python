# Titulo: Valor dentro de un rango.
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.
# Solicitar al usuario que ingrese un numero entre 0 y 5 e indicarle si esta dentro del rango.
# Se deben definir dos constantes para el rango.
# Se debe de comrpobar si el numero esta dentro del rango.
# deb de imrpimir si el numero esta dentro del rango con true o false.

# Definicion de constantes.
MINIMO = 0
MAXIMO = 5
separador = "*" * 50
print(separador)
print("Bienvenido al sistema de validacion de rango")
print(separador)
# Solicitar al usuario que ingrese un numero entre 0 y 5.
numero = int(input("Ingrese un numero entre 0 y 5: "))
print(separador)
# Comprobar si el numero esta dentro del rango.
dentro_rango = numero >= MINIMO and numero <= MAXIMO
print("El numero esta dentro del rango: ", dentro_rango)
print(separador)
print("Fin del programa")
print(separador)
