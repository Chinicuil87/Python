# Titulo: Mayor de dos numeros
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# sepador

separador = "*"*60

# Titulo
print(separador)
print("El mayor de dos numeros".center(60))
print(separador)
# Solicitud de la informacion
primer_numero = int(input("Ingresa el primer numero: "))
segundo_numero = int(input("Ingresa el segundo numero: "))


if primer_numero > segundo_numero:
    print(f"El primer numero es mayor: {primer_numero}")

else:
    print(f'El segundoi numero es mayor: {segundo_numero}')
