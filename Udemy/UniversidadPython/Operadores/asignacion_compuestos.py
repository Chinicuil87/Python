# Titulo: Operadores asignacion compuestos
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Descripcion: Operadores de asignacion compuestos.
# Se utilizan para realizar operaciones y asignar el resultado a la misma variable.

# Ejemplo: a += 5 es equivalente a a = a + 5
# En este caso, se suma 5 a la variable a y se asigna el resultado a la misma variable a.

contador = 0
contador += 1  # contador = contador + 1
print(contador)  # 1
contador += 5  # contador = contador + 5
print(contador)  # 6

a, b = 5, 10

print(f'Valores iniciales: a = {a}, b = {b}')

a += b  # a = a + b
print(f'Valores despues de a += b: a = {a}, b = {b}')

a -= b  # a = a - b
print(f'Valores despues de a -= b: a = {a}, b = {b}')


a *= b  # a = a * b
print(f'Valores despues de a *= b: a = {a}, b = {b}')
