# Titulo: Calculo de area y perimetro de un rectangulo
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Sistema que calcula el area y perimetro de un rectangulo.
# Se le pide al usuario que ingrese la base y la altura del rectangulo.

separador = "*" * 50
print(separador)
print("Calculo de area y perimetro de un rectangulo")
print(separador)

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")
print(separador)
print("Fin del programa")
print(separador)
10
