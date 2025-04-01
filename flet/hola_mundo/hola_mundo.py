import flet as ft


def main(ventana: ft.Page):
    """
    Función principal que configura la interfaz de usuario de una aplicación simple en Flet.

    Esta función crea un texto que dice "Hola mundo" en color verde y lo añade a la ventana principal.

    Args:
        ventana (ft.Page): Objeto que representa la ventana principal de la aplicación.
    """
    # Titulo de la aplicacion.
    ventana.title = "Primer programa Flet"
    # Crear un texto con el valor "Hola mundo" y color verde
    t = ft.Text(value="Hola mundo", color="green")

    # Añadir el texto a la lista de controles de la ventana
    ventana.controls.append(t)

    # Actualizar la ventana para reflejar los cambios
    ventana.update()


# Iniciar la aplicación Flet
ft.app(target=main)
