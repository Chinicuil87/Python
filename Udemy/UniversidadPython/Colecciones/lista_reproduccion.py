# Titulo: Lista de reproducción de música
# Descripcion: Crear y manipular una lista de reproducción de música
# Tema: Colecciones
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# Crear un programa para administrar una lista de canciones.
# Debes soliccitar al usuario cuantas cacniones desea agregar a la lista y posterior mente ir solicitando cada cancion
# Final mente debe desplegar la lista de cacniones en orden alfabetico.

separador = "*"*50

print(separador)
print("Bienvenido a la lista de reproducción de música")
print(separador)
# Solicitar al usuario cuantas canciones desea agregar a la lista
cantidad_canciones = int(input("¿Cuántas canciones desea agregar a la lista? "))
# Crear una lista vacía para almacenar las canciones
lista_canciones = []
# Solicitar al usuario cada canción y agregarla a la lista
for i in range(cantidad_canciones):
    cancion = input(f"Ingrese el nombre de la canción {i + 1}: ")
    lista_canciones.append(cancion) 
# Ordenar la lista de canciones en orden alfabético
lista_canciones.sort()
# Mostrar la lista de canciones
print(separador)
print("Lista de canciones en orden alfabético:")
for cancion in lista_canciones:
    print(cancion)
print(separador)
# Fin del programa
print("Gracias por usar la lista de reproducción de música")
print(separador)
print("¡Hasta luego!")
