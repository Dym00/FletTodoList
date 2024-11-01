import flet as ft

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window.width = 350
        self.page.window.height = 450
        self.page.window.resizable = False
        self.page.window.always_on_top = True
        self.page.title = 'ToDo - App'
        self.page.update()
        self.main_page()

    def main_page(self):
        input_task = ft.TextField(hint_text='Digite aqui uma tarefa', expand=True, color= ft.colors.BLACK)
 
        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
            ]
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs= [
                ft.Tab(text='Todos'),
                ft.Tab(text='Em andamento'),
                ft.Tab(text='Finalizados')
            ]
        )

        self.page.add(input_bar, tabs)

ft.app(target=ToDo)

