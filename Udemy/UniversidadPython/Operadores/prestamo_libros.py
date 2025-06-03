# Titulo: Prestamo de libros
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Sistema de prestamo de libros.

# Se le prestar aun libro al usuario si cumple cualquiera de las siguientes condiciones:
# 1. Tiene credencuiial de estudiante.
# 2. El usuario vive a no ma de 3 km de la biblioteca.

separador = "*" * 50

print(separador)
print("Bienvenido al sistema de prestamo de libros".center(50))
print(separador)
print("Por favor, ingrese sus datos para continuar")
print(separador)
nombre = input("Ingrese su nombre: ")
credencial = input("Ingrese su credencial de estudiante (si/no): ")
distancia = float(input("Ingrese la distancia a la biblioteca en km: "))
print(separador)
print("Datos ingresados:")
print(f"Nombre: {nombre}")
print(f"Credencial de estudiante: {credencial}")
print(f"Distancia a la biblioteca: {distancia} km")
print(separador)
# Verificar si el usuario cumple con las condiciones para el prestamo de libros
validar_credencial = credencial.lower() == "si"
validar_distancia = distancia <= 3
prestamo = validar_credencial or validar_distancia
print(separador)
print("Resultado de la verificacion:")
print(
    f'El usuario {nombre} \n Cumple con alguna de las condiciones: {prestamo}')
print(separador)
print("Gracias por usar el sistema de prestamo de libros")
print(separador)
print("Fin del programa")
print(separador)
