import flet as ft
import time

class Basetextfield(ft.UserControl):
    def __init__(self, label,width):
        super().__init__()
        self.label = label
        self.width = width
    
    def build(self):
        return ft.TextField(
            label=self.label,
            width=self.width
        )
    
class Radiobuttons(ft.UserControl):
    def __init__ (self):
        super().__init__()
    
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Como você se identifica?"),
                ft.RadioGroup(content=ft.Column([
                ft.Radio(value="Homem cis", label="Homem cis"),
                ft.Radio(value="Homem trans", label="Homem trans"),
                ft.Radio(value="Mulher cis", label="Mulher cis"),
                ft.Radio(value="Mulher trans", label="Mulher trans"),
                ft.Radio(value="não-binário", label="não-binário")]))
            ]
        )

class Schoolingdropdown(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return ft.Dropdown(
            label="Escolaridade",
            hint_text="Selecione seu nivel de escolaridade",
            width=400,
            options=[
                ft.dropdown.Option("Ensino Fundamental"),
                ft.dropdown.Option("Ensino Médio"),
                ft.dropdown.Option("Ensino Superior"),
                ft.dropdown.Option("Pós-graduação"),
                ft.dropdown.Option("Mestrado"),
                ft.dropdown.Option("Doutorado"),
                ft.dropdown.Option("Pós-doutorado")
            ],
        )

class Elementsdropdown(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return ft.Dropdown(
            label="Elementos de maquina",
            hint_text="Qual seu nivel de conhecimento sobre elementos de maquina",
            width=400,
            options=[
                ft.dropdown.Option("Nenhum"),
                ft.dropdown.Option("Tenho pouco conhecimento"),
                ft.dropdown.Option("Estou aprendendo atualmente"),
                ft.dropdown.Option("Tenho um bom entendimento"),
            ],
        )

def main (page: ft.Page):
    page.title = "Menu - Plataforma de Testes"
    page.theme_mode = "light"
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
        pass


    placeholderCountdown = ft.Text("00:00")
    formtitle = ft.Text(value="Teste de Identidade",style=ft.TextThemeStyle.DISPLAY_SMALL)
    agetextfield = Basetextfield("Informe sua idade", 200)
    genderradiobuttons = Radiobuttons()
    schoolingdropdown = Schoolingdropdown()
    coursetextfield = Basetextfield("Qual curso você realiza atualmente", 300)
    elementsdropdown = Elementsdropdown()
    submitbutton = ft.FilledButton("Enviar")

    page.add(
        ft.AppBar(
            title= ft.Text("Plataforma de testes", size=30),
            center_title=True,
            bgcolor='blue',
            leading=ft.Icon(name="home"),
            actions=[
                placeholderCountdown,
                toggledarklight
            ]
        ),
        ft.Column(
            controls=[
                formtitle,
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