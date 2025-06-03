# Titulo: Receta de cocina
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Crear un programa que solicite algunos valores para una receta de cocina.

# nombre de la receta
# ingredientes
# Tiempo de preparacion
# Dificultad

separador = "*"*50

# variables
nombre_receta = ""
ingredientes = ""
tiempo_preparacion = 0
dificultad = ""

print(separador)
print("Receta de cocina".center(50))
print(separador)
# Captura de datos
nombre_receta = input("Nombre de la receta: ")
ingredientes = input("Ingredientes: ")
tiempo_preparacion = int(input("Tiempo de preparacion (minutos): "))
dificultad = input("Dificultad: ")
print(separador)
print("Receta de cocina".center(50))
print(separador)
print("Nombre de la receta: ", nombre_receta)
print("Ingredientes: ", ingredientes)
print("Tiempo de preparacion: ", tiempo_preparacion, "minutos")
print("Dificultad: ", dificultad)
print(separador)

print("Gracias por usar el programa".center(50))
print(separador)
print("Fin del programa".center(50))
