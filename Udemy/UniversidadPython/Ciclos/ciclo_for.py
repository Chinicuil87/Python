# Titulo: Ciclo for
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# el ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de texto) o un objeto iterable.
# Se utiliza para ejecutar un bloque de codigo un numero determinado de veces.
# Sintaxis:
# for variable in secuencia:
#     bloque de codigo

# Ejemplo de uso del ciclo for
cadena = "Hola, Python!"
for caracter in cadena:
    print("El caracter es:", caracter)

# Ejemplo de uso del ciclo for con una lista
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print("El numero es:", numero)

# Ejemplo de uso del ciclo for con un rango
for i in range(5):
    print("El valor de i es:", i)

# Ejemplo de uso del ciclo for con un diccionario
diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(f"La clave es: {clave} y el valor es: {valor}")
