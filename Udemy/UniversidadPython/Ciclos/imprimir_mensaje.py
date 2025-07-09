# Titulo: Imprimir mensaje repetidamente
# Descripcion: Este script imprime un mensaje varias veces utilizando un bucle for.
# Cliclos de repeticion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

# Separador
separador = "*" * 60

# Título del programa
print(separador)
print("Imprimir Mensaje Repetidamente".center(60))
print(separador)
# Mensaje a imprimir
mensaje = input("Ingrese el mensaje a repetir: ")
numero_repeticiones = int(input("Ingrese el número de repeticiones: "))

# Bucle for para imprimir el mensaje varias veces
for i in range(numero_repeticiones):
    print(f"{i + 1}. {mensaje}")
print(separador)
# Mensaje final
print("Fin del programa".center(60))
