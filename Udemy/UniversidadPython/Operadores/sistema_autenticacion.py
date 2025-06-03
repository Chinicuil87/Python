# Titulo: Sistema de autenticacion.
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Programa para validar el usuario y password del usuario.
# Crear dos constantes para el usuario y password.
# Se debe solicitar al usuario que ingrese su usuario y password.
# Debe imprimi true o false si el usuario y password son correctos.

USUARIO = "cesar"
PASSWORD = "123456"

separador = "*" * 50
print(separador)
print("Bienvenido al sistema de autenticacion")
print(separador)
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su password: ")
print(separador)

acceso = usuario.strip() == USUARIO and password.strip() == PASSWORD
print("Acceso: ", acceso)
print(separador)
print("Fin del programa")
print(separador)
