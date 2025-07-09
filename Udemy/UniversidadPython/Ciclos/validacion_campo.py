# Titulo: Validacion de un campo de texto
# Descripcion: Validar que un campo de texto no esté vacío.
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# Separador
separador = "*" * 60

# variables
nombre_usuario = None

print(separador)
print("Validación de Campo de Texto".center(60))
print(separador)

while not nombre_usuario:
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()

print(separador)
print(f"Nombre de usuario ingresado: {nombre_usuario}")
print(separador)
