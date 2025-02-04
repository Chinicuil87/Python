# importamos la libreria de flet (instalar antes de pip install flet)
import flet as ft

# Funcion principal que tiene como parametro un pagina de flet


def main(page: ft.Page):
    # Color de la ventana-
    page.bgcolor = ft.colors.BLUE_GREY_800
    # Alinear texto
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    # Titulo principal
    page.title = "Tablero de Notas"

    nota = ft.TextField(value="mi primera nota", multiline=True)

    page.add(nota)
    
    def create_note(text)


# Se instancia la aplicacion
ft.app(target=main)
