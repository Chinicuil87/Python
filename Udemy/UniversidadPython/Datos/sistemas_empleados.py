# Titulo: Sistemas de empleados
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Solicitar informacion de empleados

# Nombre del empleado
# Edad del empleado
# Salario del empleado
# Jefe de departamento (SI/NO)

separador = "*"*50

# Variables
nombre = ""
edad = 0
salario = 0.0
jefe = False

print(separador)
print("Sistema de empleados".center(50))
print(separador)
nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
salario = float(input("Ingrese el salario del empleado: "))
# Convierte a mayusculas
jefe = input("Es jefe de departamento (SI/NO): ").upper()
jefe = jefe == "SI"  # Convierte a booleano
print(separador)
print("Datos del empleado".center(50))
print(separador)
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Salario: $", salario)
print("Jefe de departamento: ", jefe)
print(separador)
print("Fin del sistema de empleados".center(50))
