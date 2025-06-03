# Titulo: Sistema de calificaciones
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Crear un programa para convertir una califica

# Convierne una calificacion numerica a letra.
# Si es mayor o igual a 9 ->  A
# Mayor o igual a 8 -> B
# Mayor o igual a 7 -> C
# Mayor o igual a 6 -> D
# Mayor o igual a 0 -> F
# "Valor Desconocido"

# Separador
separador = "*"*60

# Titulo
print(separador)
print("Sistema de calificaciones".center(60))
print(separador)

calificacion = float(input("Coloca tu calificacion: "))
valor = ""

if calificacion >= 9 and calificacion <= 10:
    valor = "A"
elif calificacion >= 8 and calificacion < 9:
    valor = "B"
elif calificacion >= 7 and calificacion < 8:
    valor = "C"
elif calificacion >= 6 and calificacion < 7:
    valor = "D"
elif calificacion >= 0 and calificacion < 6:
    valor = "F"
else:
    valor = "Valor desconocido"

print(separador)
print(f"La calificacion de {calificacion} corresponde {valor}")
print(separador)
