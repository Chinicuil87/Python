# Titulo: OperadoresSistemas de descuentos
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Descripcion: Sistema de descuentos.
# Una tienda de supermercado ofrece un desscuento especial a clientes
# que compren 10 o mas articulos, y ademas son miembros de la tienda.
# El sistema debe solicitar al lciente que indique el numero de artuculos que ha comprado y #
# preguntarle si es miembro de la tienda.

# Si el cliente es miembro y ha comprado 10 o mas articulos, se le aplicara un descuento VIP

separador = "*"*50

print(separador)
print("Sistema de descuentos".center(50))
print(separador)
numero_articulos = int(input("Ingrese el numero de articulos comprados: "))
es_miembro = input("Es miembro de la tienda? (si/no): ").strip().lower()
print(separador)

primera_condicion = numero_articulos >= 10
segunda_condicion = es_miembro == "si"

print("Condiciones:")
print(f"El cliente ha comprado {numero_articulos} articulos.")
print(f"El cliente es miembro de la tienda: {es_miembro}.")
print(separador)
print(
    f'El cliente tiene descuento VIP: {primera_condicion and segunda_condicion}.')
print(separador)
10
