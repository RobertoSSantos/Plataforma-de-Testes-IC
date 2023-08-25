import flet as ft
import time

def main (page: ft.Page):

    #Base references

    #Toggle Dark/Light Mode
    def changetheme(e):
        page.splash.visible = True
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

        time.sleep(0.5)
        toggledarklight.selected = not toggledarklight.selected
        page.splash.visible = False
        page.update()

    #Toggle Dark/Light Mode Button
    toggledarklight = ft.IconButton(
        on_click=changetheme,
        icon="dark_mode",
        selected_icon="light_mode",
        style=ft.ButtonStyle(
            color={"":ft.colors.BLACK, "selected":ft.colors.WHITE}
        )

    )

    # Page definitions
    page.title = "Plataforma de Testes"
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll= ft.ScrollMode.AUTO
    page.splash = ft.ProgressBar(visible=False)
    page.window_center()
    page.window_always_on_top = True

    # Appbar
    page.appbar = ft.AppBar(
        title= ft.Text("Plataforma de Testes", size=30),
        bgcolor='blue',
        leading=ft.Icon(name="home"), 
        actions=[
            toggledarklight
        ]
    )
    page.update()

    

ft.app(target=main)