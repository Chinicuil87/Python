import flet as ft

def main(page):
    """
    Función principal que configura una interfaz de usuario con un checkbox y un texto de salida.

    Esta función muestra un checkbox con la etiqueta "ToDo: Aprende Python". Cuando el estado del
    checkbox cambia (marcado o desmarcado), se actualiza un texto que indica si el usuario ha
    aprendido a usar checkboxes.

    Args:
        page (ft.Page): Objeto que representa la página principal de la aplicación.
    """

    def checkbox_changed(e):
        """
        Función que se ejecuta cuando el estado del checkbox cambia.

        Actualiza el texto de salida para reflejar si el checkbox está marcado o desmarcado.

        Args:
            e: Evento de cambio (no se usa directamente, pero es requerido por Flet).
        """
        output_text.value = (
            f"Has aprendido a usar checkboxes: {todo_check.value}."
        )  # Actualizar el texto de salida
        page.update()  # Actualizar la página para reflejar los cambios

    # Texto de salida que se actualiza según el estado del checkbox
    output_text = ft.Text()

    # Checkbox con la etiqueta "ToDo: Aprende Python"
    todo_check = ft.Checkbox(
        label="ToDo: Aprende Python", 
        value=False, 
        on_change=checkbox_changed  # Asignar la función de cambio
    )

    # Añadir el checkbox y el texto de salida a la página
    page.add(todo_check, output_text)

# Iniciar la aplicación Flet
ft.app(target=main)