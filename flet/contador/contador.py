import flet as ft


def main(pagina: ft.Page):
    """
    Función principal que configura la interfaz de usuario de la aplicación Contador.

    Args:
        pagina (ft.Page): Objeto que representa la página principal de la aplicación.
    """
    # Titulo de la aplicacion
    pagina.title = "Contador Flet"
    # Alineación vertical al centro
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campo de texto para mostrar el número actual
    txt_numero = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100
    )

    def disminuir_click(e):
        """
        Función que disminuye el valor del contador en 1 cuando se hace clic en el botón "-".

        Args:
            e: Evento de clic (no se usa directamente, pero es requerido por Flet).
        """
        txt_numero.value = str(int(txt_numero.value) -
                               1)  # Disminuir el valor en 1
        pagina.update()  # Actualizar la página para reflejar el cambio

    def aumentar_click(e):
        """
        Función que aumenta el valor del contador en 1 cuando se hace clic en el botón "+".

        Args:
            e: Evento de clic (no se usa directamente, pero es requerido por Flet).
        """
        txt_numero.value = str(int(txt_numero.value) +
                               1)  # Aumentar el valor en 1
        pagina.update()  # Actualizar la página para reflejar el cambio

    # Añadir una fila con botones y el campo de texto
    pagina.add(
        ft.Row(
            [
                # Botón para disminuir
                ft.IconButton(ft.icons.REMOVE, on_click=disminuir_click),
                txt_numero,  # Campo de texto con el número
                # Botón para aumentar
                ft.IconButton(ft.icons.ADD, on_click=aumentar_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear la fila al centro
        )
    )


# Iniciar la aplicación
ft.app(target=main)
