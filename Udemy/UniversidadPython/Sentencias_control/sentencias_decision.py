# Titulo: Sentencias de decision
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Nos permiten controlar el flujo de un programa, dependiendo de una condicion.
# La estructura que se utiliza es la siguiente:
# if condicion:
#     # Bloque de instrucciones
# elif condicion:
#     # Bloque de instrucciones
# else:
#     # Bloque de instrucciones

separador = "-" * 50
# Ejemplo.
print(separador)
print("Sentencia if")

edad = 30
if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")

# Ejemplo
print(separador)
print("Sentencia if - else")
edad = 15
if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")
else:
    print(f"Tienes {edad} años, eres menor de edad")


# Ejemplo
print(separador)
print("Sentencia if - elif - else")
edad = 15
if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")
elif edad >= 12:
    print(f"Tienes {edad} años, eres un adolescente")
else:
    print(f"Tienes {edad} años, eres un niño")

print(separador)
