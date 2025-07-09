# Titulo: Contador de Vocales
# Ciclos de repeticion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025
"""
Ejercicio Contador de Vocales en Python
Escribe un programa que declare una variable llamada cadena con el valor de "Hola Mundo".
Posteriormente usando un ciclo for, debe contar la cantidad de vocales presentes en la cadena y finalmente imprimir la cantidad de vocales encontradas (solo el número con la cantidad de vocales encontradas es el que se debe imprimir).
Nota: La salida del programa debe ser idéntico al solicitado, no agregar espacios, textos o saltos de línea innecesarios, de lo contrario la prueba a ejecutar podría fallar.

Instrucciones de Ejecución:
1. Deben presionar el botón de "Ejecutar código" para ver su resultado,
2. Finalmente presionar el botón de "Ejecutar pruebas" para que quede resuelto el ejercicio.
3. Nota: Tu código podría estar correcto, pero recuerda que lo importante es el resultado de ejecutar la prueba, así que revisa nuevamente las instrucciones del ejercicio y respétalas por completo.
"""
# Separador
separador = "*" * 50

print(separador)
print("Contador de Vocales")
print(separador)
cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1
print(contador_vocales)
print(separador)
# Fin del programa
print("Fin del programa")
print(separador)
