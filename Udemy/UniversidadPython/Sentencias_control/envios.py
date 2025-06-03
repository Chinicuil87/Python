# Titulo: Sistema de envios.
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Sistema de nevio de paquetes.
# Se multiopliucara de acuerdo al peso del paquete y el destino.
# Nacional con un costo de 10 por cada kilogramo
# Internacional con un costo de 20 por cada kilogramo
# El usuario debe poder escoger que tipo de nevio rquiere y proporcionar el peso del paquete en kilogramos.

# Separador
separador = "*"*60

# Constantes
NACIONAL = 10
INTERNACIONAL = 20

# Titulo
print(separador)
print("sistema de envio".center(60))
print(separador)

# Obtener datos
destino = input("Tipo de envio (N: Nacionar I: Internacional): ")
destino = destino.strip().lower()
peso = float(input("Peso del paquete: "))

if destino == "n":
    tipo = "Nacional"
    costo = NACIONAL * peso
else:
    tipo = "Internacional"
    costo = INTERNACIONAL * peso

print(separador)
print(f"Envio: {tipo}")
print(f"Peso del paquete: {peso} KG")
print(f"Costo del envio: ${costo}")
print(separador)
