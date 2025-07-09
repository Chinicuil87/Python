# Titulo: Break y Continue
# Descripcion: Este programa muestra el uso de las instrucciones break y continue en un bucle.
# Cilos de repeticion
# Curso: Universidad Python
# Plataforma: Udemy
# Programador: Cesar Lopez Orihuela.
# Aplicacion de consola.
# Fecha: 16-06-2025

print("Programa que muestra el uso de las instrucciones break y continue en un bucle.")

# break: Termina el bucle
for i in range(10):
    if i == 5:
        print("Se ha alcanzado el valor 5, se termina el bucle.")
        break
    print(f"Valor de i: {i}")

# continue: Salta a la siguiente iteracion del bucle
print("\nPrograma que muestra el uso de la instruccion continue en un bucle.")
for i in range(10):
    if i == 5:
        print("Se ha alcanzado el valor 5, se salta a la siguiente iteracion.")
        continue
    print(f"Valor de i: {i}")
    
print("\nFin del programa.")
# Fin del programa
