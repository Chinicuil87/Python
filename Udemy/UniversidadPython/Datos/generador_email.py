# Titulo: Generador de email
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Se solicita creae una nueva version del sistema genrador de email

# Se debe solicitar al usuario los siguientes datos:
# Nombre
# Apellidos
# nombre de la empresa
# Extencion dominios

# Resultado: juan.carlos.gomez.lara@eysen.com

separador = "*"*50
print(separador)
print("Generador de email".center(50))
print(separador)

# Obtener datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
empresa = input("Ingrese el nombre de la empresa: ")
extencion = input("Ingrese la extencion del dominio: ")
print(separador)

# lipieza de datos

nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ", "")
extencion = extencion.strip().lower()

# Formar el email
email = nombre + "." + apellido + "@" + empresa + "." + extencion

# Mostrar el email
print("Su email es: ", email)
print(separador)
print("Gracias por usar el generador de email".center(50))
print(separador)
print("Fin del programa".center(50))
print(separador)
