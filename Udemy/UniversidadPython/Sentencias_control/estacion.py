# Titulo: Estacion del año
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Solicitar proporcionar el valor del mes(numerico entre 1 y 12), e indicar la estacion del año.
# Mes 1,2 o 12 -> Invierno
# Mes 3.4 o 5 -> Primavera
# Mes 6,7 o 8 -> Verano
# Mes 9,10 o 11-> Otoño
# Otro valor -> Estacion desconocida

# Separador
separador = "*"*60

# Titulo
print(separador)
print("Estacion del año".center(60))
print(separador)

# Obtener informacion del mes.
mes = int(input("Coloca el numero del mes a validar: "))
print(separador)

if mes == 1 or mes == 2 or mes == 12:
    print(f"El mes {mes} corresponde a Invierno.")

elif mes == 3 or mes == 4 or mes == 5:
    print(f"El mes {mes} corresponde a Primavera.")

elif mes == 6 or mes == 7 or mes == 8:
    print(f"El mes {mes} corresponde a Verano.")

elif mes == 9 or mes == 10 or mes == 11:
    print(f"El mes {mes} corresponde a Otoño.")

else:
    print(
        f'El mes proporcionado {mes} no corresponde a ninguna estacion del año.')

print(separador)
print("Fin del programa.".center(60))
