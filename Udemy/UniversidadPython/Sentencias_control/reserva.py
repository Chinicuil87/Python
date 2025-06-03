# Titulo: Reserva Hotel
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.


# El programa de Sistema de Reserva de Hotel debe solictar la siguiente informacion.
# Nombre del cliente
# Dias de estadia
# Cuarto con vista al mar
# Tarifas
# Cuarto sin vista al mar = $ 150.50 por dia
# Cuarto con vista al mar = $190.50 por  dia
# Se debe calcular el costo total de la estadia  dependiendo que cuarto escogio.

# Separador
separador = "*"*60

# Constantes.
SIN_VISTA_MAR = 150.50
CON_VISTA_MAR = 190.50

print(separador)
print("Sistema de Reserva de Hotel".center(60))
print(separador)
# Solicitar informacion al cliente
nombre = input("Nombre completo: ")
dias = int(input("Cuantos dias reseva: "))
vista = input("Quiere un cuarto  con vista al mar(si/no): ")

vista = vista.strip().upper()
print(separador)
print("Datos de la reservacion: ")
print(separador)
print("Reserva del cuarto: ")
print(f'Nombre del cliente: {nombre}')
print(f"Dias de estancia: {dias}")
print(f'Cuento con vista al mar: {vista}')

if vista == "SI":
    costo = CON_VISTA_MAR*dias
    print(f"Costo  total de la habitacion: ${costo}")
    print(separador)
else:
    costo = SIN_VISTA_MAR*dias
    print(f"Costo  total de la habitacion: ${costo}")
    print(separador)
