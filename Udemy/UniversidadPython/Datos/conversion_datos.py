# Titulo: Conversion de tipo de datos
# Ejercicio de la funcion print
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.

# Aplicacion de consola.

# Casting o conversion de tipo de datos
# La conversion de tipo de datos es el proceso de convertir un tipo de dato a otro.
# En Python, la conversion de tipo de datos se realiza mediante funciones de conversion.

# Convertir a entero -> int()
# Convertir a float -> float()
# Convertir a cadena -> str()
# Convertir a booleano -> bool()

# Caden a entero
# La funcion int() convierte una cadena a un entero.

numero = "10"

print("Numero: ", numero)  # 10
print("Tipo de dato: ", type(numero))  # <class 'str'>
numero_entero = int(numero)  # 10
print("Numero entero: ", numero_entero)  # 10
print("Tipo de dato: ", type(numero_entero))  # <class 'int'>

# Caden a float
# La funcion float() convierte una cadena a un float.

numero = "10.5"
print("Numero: ", numero)  # 10.5
print("Tipo de dato: ", type(numero))  # <class 'str'>
numero_float = float(numero)  # 10.5
print("Numero float: ", numero_float)  # 10.5
print("Tipo de dato: ", type(numero_float))  # <class 'float'>

# Convertir numero a cadena
# La funcion str() convierte un numero a una cadena.

numero = 10
print("Numero: ", numero)  # 10
print("Tipo de dato: ", type(numero))  # <class 'int'>
numero_cadena = str(numero)  # "10"
print("Numero cadena: ", numero_cadena)  # "10"
print("Tipo de dato: ", type(numero_cadena))  # <class 'str'>

# Convertir a booleano
# La funcion bool() convierte un numero a un booleano.
# Si el numero es 0, devuelve False. Si el numero es diferente de 0, devuelve True.

# Valor de 0
numero_entero = 0
print("Numero: ", numero_entero)  # 0
print("Tipo de dato: ", type(numero_entero))  # <class 'int'>
numero_booleano = bool(numero_entero)  # False
print("Numero booleano: ", numero_booleano)  # False

# Valor que no es 0
numero_entero = 10
print("Numero: ", numero_entero)  # 10
print("Tipo de dato: ", type(numero_entero))  # <class 'int'>
numero_booleano = bool(numero_entero)  # True
print("Numero booleano: ", numero_booleano)  # True

numero_cadena = "10"
numero_cadena1 = "20"
print("Numero: ", numero_cadena)  # "10"
print("Tipo de dato: ", type(numero_cadena))  # <class 'str'>
print("Numero: ", numero_cadena1)  # "20"
print("Tipo de dato: ", type(numero_cadena1))  # <class 'str'>
resultado = numero_cadena + numero_cadena1  # "1020"
print("Resultado: ", resultado)  # "1020"
print("Tipo de dato: ", type(resultado))  # <class 'str'>

# Convetir los numeros de cadena a enteros
numero_entero = int(numero_cadena)  # 10
numero_entero1 = int(numero_cadena1)  # 20
print("Numero: ", numero_entero)  # 10
print("Tipo de dato: ", type(numero_entero))  # <class 'int'>
print("Numero: ", numero_entero1)  # 20
print("Tipo de dato: ", type(numero_entero1))  # <class 'int'>
resultado = numero_entero + numero_entero1  # 30
print("Resultado: ", resultado)  # 30
print("Tipo de dato: ", type(resultado))  # <class 'int'>
