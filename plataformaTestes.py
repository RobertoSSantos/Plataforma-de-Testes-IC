from Controls.initialFormControls import *
import flet as ft
import time

def main (page: ft.Page):
    page.title = "Menu - Plataforma de Testes"
    page.theme_mode = "light"
    page.window_width = 450
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll= ft.ScrollMode.AUTO
    page.splash = ft.ProgressBar(visible=False)
    page.window_always_on_top = True
    page.window_center()

    #Toggle Dark/Light Mode
    def changetheme(e):
        page.splash.visible = True
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()
        time.sleep(0.5)
        toggledarklight.selected = not toggledarklight.selected
        page.splash.visible = False
        page.update()

    def submit(e):
        page.clean()
        appbar.title = ft.Text("Plataforma de testes", size=30)
        page.add(appbar)

    toggledarklight = ft.IconButton(on_click=changetheme,icon="dark_mode",selected_icon="light_mode",style=ft.ButtonStyle(color={"":ft.colors.BLACK, "selected":ft.colors.WHITE}))

    placeholderCountdown = ft.Text("00:00")

    appbar = ft.AppBar(title= ft.Text("Formulario Inicial", size=30),center_title=True,bgcolor='blue',leading=ft.Icon(name="home"),actions=[placeholderCountdown,toggledarklight])

    agetextfield = Basetextfield("Informe sua idade", 200)
    genderradiobuttons = Radiobuttons()
    schoolingdropdown = Schoolingdropdown()
    coursetextfield = Basetextfield("Qual curso você realiza atualmente", 300)
    elementsdropdown = Elementsdropdown()
    submitbutton = ft.FilledButton("Enviar",on_click=submit)

    page.add(
        appbar,
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=[
                agetextfield,
                genderradiobuttons,
                schoolingdropdown,
                coursetextfield,
                elementsdropdown,
                submitbutton
            ]
        ),
    )
    
ft.app(target=main)