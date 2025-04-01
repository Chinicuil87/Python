# Input
"""
Sirve para recibir un mensaje del usuario y guardarlo en una variable.
input("mensaje")
"""

# Imprimir el mensaje capturado por el input
print(input("Cual es tu nombre? "))
print(input("Cual es tu edad? "))

# Concadenar input
print("Hola " + input("Cual es tu nombre? ") +
      " tienes " + input("Cual es tu edad? ") + " años")

# Practica 1

"""
Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

¿Qué estás estudiando?

El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print). 
"""
print(input('¿Qué estás estudiando? '))

# Practica 2

""" 
Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

¿En qué país vives?

El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).
"""

print(input('¿En qué país vives? '))

# Practica 3

"""
Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:

Escribe tu nombre:
Escribe tu apellido:
El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.  
"""
print(input('Escribe tu nombre: ')+' '+input('Escribe tu apellido: '))
