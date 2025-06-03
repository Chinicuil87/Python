# Titulo: Salud Fitness
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Solicitar al usuario:
# Nombre del usuario
# Pasos caminados en el dia

# Definir constantes:
# META_PASOS = 10000
# CALORIAS_PASOS = 0.04 -> valor aproximado en kilocalorias

# Calcular las calorias quemadas segun los pasos dados.
# Verificar si se cumplio la meta de pasos diarios

# Separador
separador = "*"*60

# Constantes
META_PASOS = 10000
CALORIAS_PASOS = 0.04

# Titulo de la aplicacion
print(separador)
print("Salud Fitness".center(60))
print(separador)

# Solicitamos informacion al usuario
nombre = input("Cual es tu nombre: ")
pasos = int(input("Numero de pasos dados en el dia:"))

calorias_quemadas = pasos * CALORIAS_PASOS

if pasos >= META_PASOS:
    print(separador)
    print(f"Felicidades {nombre} meta cumplicada")
    print(f"Total de pasos en el dia: {pasos} ")
    print(f"Total de kilocalorias quemadas: {calorias_quemadas}")
    print(separador)

else:
    print(separador)
    print("No cumpliste en numero de pasos diario")
    print("Sigue esforzandote")
    print(f"Pasos en el dia: {pasos}")
    print(f"Total de calorias quemadas: {calorias_quemadas}")
    print(separador)
