# Titulo: Metodos de cadenas
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Upper -> Convierte una cadena a mayusculas.
cadena = "Hola Mundo"
print(cadena.upper())  # HOLA MUNDO
# Lower -> Convierte una cadena a minusculas.
print(cadena.lower())  # hola mundo
# Capitalize -> Convierte la primera letra de una cadena a mayusculas.
print(cadena.capitalize())  # Hola mundo
# Title -> Convierte la primera letra de cada palabra a mayusculas.
print(cadena.title())  # Hola Mundo
# Swapcase -> Convierte las mayusculas a minusculas y las minusculas a mayusculas.
print(cadena.swapcase())  # hOLA mUNDO
# Strip -> Elimina los espacios en blanco al inicio y al final de una cadena.
cadena = "   Hola Mundo   "
print(cadena.strip())  # Hola Mundo
# Lstrip -> Elimina los espacios en blanco al inicio de una cadena.
print(cadena.lstrip())  # Hola Mundo
# Rstrip -> Elimina los espacios en blanco al final de una cadena.
print(cadena.rstrip())  # Hola Mundo
# Replace -> Reemplaza una cadena por otra.
print(cadena.replace("Hola", "Adios"))  # Adios Mundo
# Split -> Divide una cadena en una lista de cadenas.
print(cadena.split())  # ['Hola', 'Mundo']
# Join -> Une una lista de cadenas en una sola cadena.
print(" ".join(['Hola', 'Mundo']))  # Hola Mundo
# Find -> Busca una cadena en otra cadena y devuelve la posicion de la primera ocurrencia.
print(cadena.find("Mundo"))  # 8
# Index -> Busca una cadena en otra cadena y devuelve la posicion de la primera ocurrencia. Si no lo encuentra, lanza una excepcion.
print(cadena.index("Mundo"))  # 8
# Count -> Cuenta el numero de veces que aparece una cadena en otra cadena.
print(cadena.count("o"))  # 2
