# Titulo: Casa de los espejos
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Para poder ingresar a la casa de los espejos debe de cumplir algusno requisitos.
# Debes tener mas de 10 años
# No debes tenerle miedo a la obscuridad

separador = "*"*60

print(separador)
print("Casa de los espejos".center(60))
print(separador)


edad = int(input("Cual es tu edad: "))
miedo_obcuridad = input("Te da miedo la oscuridad(si/no): ")
acceso = edad >= 10 and miedo_obcuridad.strip().lower() == "no"

print(acceso)

if acceso:
    print("Puedes acceder a la casa")

else:
    print("No puede acceder a la casa")
