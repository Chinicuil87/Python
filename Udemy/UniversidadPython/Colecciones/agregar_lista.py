# Titulo: agregar elementos a una lista
# Descripcion: Agregar elementos a una lista en Python
# Tema: Colecciones
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

print("Programa que muestra el uso de las listas para agregar elementos.")
lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")
# Agregar un elemento al final de la lista
lista.append(6)
print(f"Lista despues de agregar un elemento al final: {lista}")
# Agregar varios elementos al final de la lista

# Modificar un elemento de la lista
lista[0] = 10
print(f"Lista despues de modificar el primer elemento: {lista}")

# Agregar un elemento en una posicion especifica
lista.insert(2, 7)  # Agrega el elemento 7 en la posicion 2
print(f"Lista despues de agregar un elemento en la posicion 2: {lista}")

