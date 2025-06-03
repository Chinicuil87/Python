# Titulo: Busqueda de subcadenas
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Find() busca una subcadena dentro de una cadena.
# Si la subcadena se encuentra, devuelve el indice de la primera ocurrencia.


cadena = "Hola Mundo"
subcadena = "Mundo"
print("Cadena: ", cadena)  # Hola Mundo
print("Subcadena: ", subcadena)  # Mundo
print("Posicion: ", cadena.find(subcadena))  # 5

# Si la subcadena no se encuentra, devuelve -1.
# La funcion find() es sensible a mayusculas y minusculas.
subcadena = "mundo"
print("Cadena: ", cadena)  # Hola Mundo
print("Subcadena: ", subcadena)  # mundo
print("Posicion: ", cadena.find(subcadena))  # -1
