import flet as ft


def main(page):
    """
    Función principal que configura una interfaz de usuario para una lista de tareas.

    Esta función permite al usuario agregar tareas a una lista. Cada tarea se representa como un
    checkbox con una etiqueta. El usuario ingresa la tarea en un campo de texto y la agrega
    presionando un botón.

    Args:
        page (ft.Page): Objeto que representa la página principal de la aplicación.
    """

    def add_clicked(e):
        """
        Función que se ejecuta cuando se hace clic en el botón "Add".

        Agrega un nuevo checkbox a la página con la etiqueta del texto ingresado en el campo
        de texto. Luego, limpia el campo de texto y le devuelve el foco para una nueva entrada.

        Args:
            e: Evento de clic (no se usa directamente, pero es requerido por Flet).
        """
        page.add(ft.Checkbox(label=new_task.value)
                 )  # Agregar un nuevo checkbox con la tarea
        new_task.value = ""  # Limpiar el campo de texto
        new_task.focus()  # Devolver el foco al campo de texto
        new_task.update()  # Actualizar el campo de texto

    # Campo de texto para ingresar nuevas tareas
    new_task = ft.TextField(hint_text="Agregar tarea: ", width=300)

    # Fila que contiene el campo de texto y el botón "Add"
    page.add(
        ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))


# Iniciar la aplicación Flet
ft.app(target=main)
