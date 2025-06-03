# Titulo: Sistema de Autentificacion
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Crear un sistema para validar los valores de usuario y password proporcionados.
# De finir dos cconstantes con los valores de usario y password
# El sistema debe de compararlos los valores
# se deben de considerar 4 casos
# 1. Usuario y password validos
# Imprimir "Bienvenidos al sistema"
# 2. Solo usuario valido
# Se debe de imprimir "Error en password"
# 3. Solo password valido
# Se debe de imprimir " Error en usuario"
# 4. Ninguno de los valores proporciondos son validos.
# Imprimir "Erro en usuario y contraseña favor de validar"

# Constantes
USUSRIO = "Chicharo"
PASSWORD = "Cesar1234"

# separador
separador = "*"*60

# Titulo
print(separador)
print("Sistema de validacion".center(60))
print(separador)

# Solicitud de datos al usuario
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
print(separador)

# Validacion de los datos
if usuario == USUSRIO and contraseña == PASSWORD:
    print("Bienvenido al sistema.")
    print(separador)
elif usuario == USUSRIO and contraseña != PASSWORD:
    print("Error en la contraseña")
    print("Vuelve a intentar")
    print(separador)
elif usuario != USUSRIO and contraseña == PASSWORD:
    print("Error en el usuario")
    print("Vuelve a intentar")
    print(separador)
else:
    print("Error en usuario y contraseña")
    print("Vuelve a intentar")
    print(separador)
