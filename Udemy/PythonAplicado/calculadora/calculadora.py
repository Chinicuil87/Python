from tkinter import *

# variables y constantes

ICONO = "./img/icono.ico"
expresion = ""
estado_visor = False

# Se crea ventana principal
ventana_calculadora = Tk()

# Modificacion de la ventana.

# icono de la ventana
ventana_calculadora.iconbitmap(ICONO)

# Titulo de la ventana
ventana_calculadora.title("CALCULADORA")

# Tamaño de la ventana
# ventana_calculadora.geometry("800x600")

# Color de la ventana
ventana_calculadora.configure(bg="dark slate gray")

# Crear filas y columnas

# Filas
for i in range(5):
    ventana_calculadora.grid_rowconfigure(i, weight=1)
# Columnas
for i in range(4):
    ventana_calculadora.grid_columnconfigure(i, weight=1)

# Visor
visor_calculadora = StringVar()
visor = Entry(ventana_calculadora,
              textvariable=visor_calculadora,
              font=("Helvetica", 24),
              bd=10,
              insertwidth=4,
              width=14,
              borderwidth=4,
              justify="right"
              )

visor.grid(row=0,
           column=0,
           columnspan=4)

# Botones
list_botones = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
                ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
                ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
                ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3)]

# Posicion de los botones
for (t, f,  c) in list_botones:
    if texto == "C":
        pass
    else:
        def comando(x=texto): return pulsar_tecla(x)

    Button(ventana_calculadora,
           text=t,
           padx=20,
           pady=20,
           font=("Helvetica", 20),
           command=comando
           ).grid(row=f,
                  column=c,
                  sticky="nsew")

# Boton de igual
Button(ventana_calculadora,
       text="=",
       padx=20,
       pady=20,
       font=("Helvetica", 40),
       command=comando
       ).grid(row=5,
              column=0,
              columnspan=4,
              sticky="nsew")


# Se inicia bucle principal de la aplicacion
ventana_calculadora.mainloop()
