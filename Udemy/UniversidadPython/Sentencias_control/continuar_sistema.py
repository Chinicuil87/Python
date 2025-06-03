# Titulo: Continuar en sistema.
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Preguntar al usuario si desea continuar dentro del sistema.


separador = "*"*60

print(separador)
print("Sistema Bancario".center(60))

salir = input("Desea salir en el sistema(si/no): ")
salir = salir.strip().lower() == "si"

if not salir:
    print("Continuamos dentro del sistema")
    print(separador)

else:
    print("Saliendo del sistema")
    print(separador)
