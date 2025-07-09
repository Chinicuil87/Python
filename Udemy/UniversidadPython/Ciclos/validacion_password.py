# Titulo: Validacion de contraseña
# Descripcion: Este programa solicita al usuario que ingrese una contraseña y verifica si cumple con ciertos criterios:
# Ejercicio de cilos de repetecion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# El programa solicita al usuario que ingrese una contraseña y verifica si cumple con ciertos criterios:
# - Debe tener al menos 8 caracteres.
# En caso de no cumplir con los criterios, se solicita al usuario que ingrese una nueva contraseña hasta que se cumplan todos los requisitos.
# Si la contraseña es válida, se imprime un mensaje de éxito.

# separador
separador = "*"*60


activo = True

print(separador)
print("Bienvenido al validador de contraseñas")
print(separador)

while activo:

    password = input(
        "Ingrese una contraseña (debe tener al menos 8 caracteres): ")
    
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Intente nuevamente.")
        password = input("Ingrese una nueva contraseña: ")
    else:
        print(f"Contraseña '{password}' es válida.")
        activo = False

else:
    print("Proceso finalizado.")
print(separador)
