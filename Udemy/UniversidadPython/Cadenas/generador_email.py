# Titulo: Reto - Generador de Email
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Crea un programa para generar email a partir de los siguientes datos.
# Nombre: Cesar Lopez
# Empresa: eysen
# Dominio: .com.mx

# Resultado final
# email = cesar.lopez@eysen.com.mx

separador = "*"*50

# Variables
nombre = "Cesar Lopez"
empresa = "Eysen"
dominio = ".com.mx"

# Titulo
print(separador)
print("Generador de Email".center(50))
print(separador)

# Imprimimos varables
print("Datos de entrada")
print(separador)
print("Nombre: ", nombre)  # Cesar Lopez
print("Empresa: ", empresa)  # Eysen
print("Dominio: ", dominio)  # .com.mx
# Nomalizamos nombre
nombre = nombre.lower()  # Convertimos a minusculas
nombre = nombre.replace(" ", ".")  # Reemplazamos el espacio por un punto

# Nomalizamos empresa
empresa = empresa.lower()  # Convertimos a minusculas
empresa = empresa.replace(" ", "")  # Reemplazamos el espacio por nada

# Generamos el email
email = nombre + "@" + empresa + dominio  # Concatenamos el email

print(separador)
print("Resultado final")
print(separador)
print("Email: ", email)  #
print(separador)
