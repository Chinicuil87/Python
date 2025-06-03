# Titulo: Ticket ventas
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Compra de varios articulos.
# Permitir optener el ticket de venta total incluyendo impuestos
# El sistema solicitara el precio de cada producto y el usuario debe indicar su costo
# el sistema debe realizar la suma de cada producto, calcular el impuesto e imprimir el total de compra

separador = "*"*50

print(separador)
print("Bienvenido al sistema de ventas")
print(separador)

precio_leche = float(input("Ingrese el precio de la leche: "))
precio_huevos = float(input("Ingrese el precio de los huevos: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_queso = float(input("Ingrese el precio del queso: "))
descuento = float(input("Ingrese el descuento: "))

precio_total_antes = precio_leche + precio_huevos + precio_pan + precio_queso
descuento_total = precio_total_antes * (descuento / 100)
precio_total = precio_total_antes - descuento_total
impuesto = precio_total * 0.18
total_con_impuesto = precio_total + impuesto
print(separador)
print("Ticket de venta")
print(separador)
print("Precio de la leche: $", precio_leche)
print("Precio de los huevos: $", precio_huevos)
print("Precio del pan: $", precio_pan)
print("Precio del queso: $", precio_queso)
print("Precio total: $", precio_total_antes)
print("Descuento: $", descuento_total)
print("Subtotal: $", precio_total)
print("Impuesto: $", impuesto)
print("Total con impuesto: $", total_con_impuesto)
print(separador)
print("Gracias por su compra")
print(separador)
print("Fin del programa")
print(separador)
