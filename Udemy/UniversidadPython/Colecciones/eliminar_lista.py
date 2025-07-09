# Titulo: Eliminar elementos de una lista
# Descripcion: Eliminar elementos de una lista en Python
# Tema: Colecciones
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

print("Programa que muestra el uso de las listas para eliminar elementos.")
lista = [1, 2, 3, 4, 5, 6]
print(f"Lista original: {lista}")

# remove
# Eliminar un elemento especifico de la lista
lista.remove(3)
print(f"Lista despues de eliminar el elemento 3: {lista}")

# pop
# Elimina un elemento por su indice
ultimo = lista.pop(0)
print(f"Lista despues de eliminar el ultimo elemento: {lista}")
print(f"Ultimo elemento eliminado: {ultimo}")

# del
del lista[0]
print(f"Lista despues de eliminar el primer elemento: {lista}")

# Obtener sublista
sublista = lista[1:3]
print(f"Sublista de la lista: {sublista}")


