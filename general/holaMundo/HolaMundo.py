"""
Aplicación Hola Mundo

Este es un programa simple en Python que muestra un mensaje de saludo en la consola.
El programa utiliza variables para almacenar el mensaje y lo imprime en un formato centrado,
rodeado por asteriscos para mejorar la presentación.

Uso:
    - Ejecuta el script para ver el mensaje "Hola Mundo!" y una descripción centrada en la consola.
"""

# Variables
saludo = "Hola Mundo!"  # Mensaje principal de saludo
mensaje = "Primer programa desde Python"  # Descripción del programa

# Imprimir en consola con formato
print("*" * 50)  # Línea decorativa de asteriscos
print(saludo.center(50, " "))  # Centrar el saludo en 50 caracteres
print(mensaje.center(50, " "))  # Centrar el mensaje en 50 caracteres
print("*" * 50)  # Línea decorativa de asteriscos
