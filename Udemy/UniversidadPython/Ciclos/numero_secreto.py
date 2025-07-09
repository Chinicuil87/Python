# Titulo: Numero secreto
# Descripcion: Este programa solicita al usuario que adivine un número secreto entre 1 y 100.
# Ejercicio de cilos de repeticion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# El programa solicita al usuario que adivine un número secreto entre 1 y 100.
# Si el usuario adivina correctamente, se imprime un mensaje de éxito.
# Si el numero proporcionado es menor que el número secreto, se le indica al usuario que el número es mayor.
# Si el número proporcionado es mayor que el número secreto, se le indica al usuario que el número es menor.
# Debe de llevar un contador de numeros de intentos.
# Numero de intentos maximo 10

# importamos la libreria random
import random

# Definimos el numero secreto
numero_secreto = random.randint(1, 100)

# Inicializamos el contador de intentos
intentos = 1

# Definimos el numero maximo de intentos
max_intentos = 10

# Separador
separador = "*" * 60

print(separador)
print("Bienvenido al juego del número secreto")
print(separador)

# Bucle para solicitar al usuario que adivine el número secreto
while intentos <= max_intentos:
    # Incrementamos el contador de intentos
    intentos += 1

    print(f"Intento {intentos - 1} de {max_intentos}")

    # Solicitamos al usuario que ingrese un número
    numero_usuario = int(input("Adivina el número secreto (entre 1 y 100): "))
    print(separador)
    # Verificamos si el número ingresado es igual al número secreto
    if numero_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto: {numero_secreto}")
        print(f"Lo lograste en {intentos - 1} intentos.")
        break
    # Verificamos si el número ingresado es menor que el número secreto
    elif numero_usuario < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    # Verificamos si el número ingresado es mayor que el número secreto
    else:
        print("El número secreto es menor. Intenta de nuevo.")
    # Verificamos si se han alcanzado el número máximo de intentos
    if intentos > max_intentos:
        print(
            f"Lo siento, has alcanzado el número máximo de intentos ({max_intentos}).")
        print(f"El número secreto era: {numero_secreto}")
        break
# Mensaje final
print(separador)
print("Gracias por jugar al juego del número secreto.")
print(separador)
