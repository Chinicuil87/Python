import flet as ft


def main(page):
    """
    Función principal que configura una interfaz de usuario para saludar al usuario.

    Esta función permite al usuario ingresar su nombre en un campo de texto. Al hacer clic en el botón
    "Saludar!", se muestra un mensaje de saludo con el nombre ingresado. Si el campo de texto está vacío,
    se muestra un mensaje de error.

    Args:
        page (ft.Page): Objeto que representa la página principal de la aplicación.
    """

    def btn_click(e):
        """
        Función que se ejecuta cuando se hace clic en el botón "Saludar!".

        Verifica si el campo de texto está vacío. Si está vacío, muestra un mensaje de error.
        Si no está vacío, limpia la página y muestra un mensaje de saludo con el nombre ingresado.

        Args:
            e: Evento de clic (no se usa directamente, pero es requerido por Flet).
        """
        if not txt_name.value:  # Verificar si el campo de texto está vacío
            txt_name.error_text = "Ingresa tu nombre"  # Mostrar mensaje de error
            page.update()  # Actualizar la página para reflejar el mensaje de error
        else:
            name = txt_name.value  # Obtener el nombre ingresado
            page.clean()  # Limpiar la página
            page.add(ft.Text(f"Hola, {name}!"))  # Mostrar el mensaje de saludo

    # Campo de texto para que el usuario ingrese su nombre
    txt_name = ft.TextField(label="Tu nombre: ")

    # Añadir el campo de texto y el botón a la página
    page.add(txt_name, ft.ElevatedButton("Saludar!", on_click=btn_click))


# Iniciar la aplicación Flet
ft.app(target=main)
