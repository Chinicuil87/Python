# Titulo: Tienda en linea.
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Crear un istema que ofrescas descuentos, dependiendo el monto de la compra o si es miembro de la tienda.
# Se debe revisar las siguientes condiciones.
# Compra mayor a $1000 y es miembro, 10 % de descuento
# Si es miembtro de la tienda, 5%  de descuento
# Si no es miembro y no compro mas de $ 1000 0

separador = "*"*60

MONTO_MINIMO = 1000

print(separador)
print("Sistema de descuento".center(60))
print(separador)
monto_compra = float(input("Monto total de tu compra: "))
miembro_tienda = input("Eres miembro de la tienda(si/no): ")
print(separador)

if monto_compra >= MONTO_MINIMO and miembro_tienda.strip().lower() == "si":
    print("Felicidades, has optenido un descuentio del 10%")
    print(f'Monto total de tu compra: ${monto_compra}')
    descuento = monto_compra*.1
    print(f'Monto de descuento: ${descuento}')
    print(f'Total a pagar: ${monto_compra-descuento}')
    print(separador)

elif miembro_tienda.strip().lower() == "si":
    print("Felicidades, has optenido un descuentio del 5%")
    print(f'Monto total de tu compra: ${monto_compra}')
    descuento = monto_compra*.05
    print(f'Monto de descuento: ${descuento}')
    print(f'Total a pagar: ${monto_compra-descuento}')
    print(separador)

else:
    print("Lo sentimos no obtuviste ningun descuento")
    print("Te invitamos a ser miembro de la tienda")
    print(f'Monto total de tu compra: ${monto_compra}')
    print(f'Total a pagar: ${monto_compra}')
    print(separador)
