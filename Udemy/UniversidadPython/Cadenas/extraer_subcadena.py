# Titulo: Extraer subcadena
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# medodo split()
# Permite separar una cadena en subcadenas.
# La funcion split() devuelve una lista de subcadenas.
# La funcion split() separa la cadena en subcadenas utilizando un separador.
# Por defecto, el separador es un espacio en blanco.

cadena = "Cesar Lopez Orihuela"
print("Cadena: ", cadena)  # Cesar Lopez Orihuela
print("Subcadena: ", cadena.split())  # ['Cesar', 'Lopez', 'Orihuela']
lista = cadena.split(" ")  # ['Cesar', 'Lopez', 'Orihuela']
print("Subcadena: ", lista)  # ['Cesar', 'Lopez', 'Orihuela']
print('Tipo de dato: ', type(lista))  # <class 'list'>

# Usa un elemnto separador diferente
cadena = "Cesar,Lopez,Orihuela"
print("Cadena: ", cadena)  # Cesar,Lopez,Orihuela
lista = cadena.split(",")  # ['Cesar', 'Lopez', 'Orihuela']
print("Subcadena: ", lista)  # ['Cesar', 'Lopez', 'Orihuela']
print('Tipo de dato: ', type(lista))  # <class 'list'>
