import flet as ft

class Basetextfield(ft.UserControl):
    def __init__(self, label,width,reference):
        super().__init__()
        self.label = label
        self.width = width
        self.reference = reference
    
    def build(self):
        return ft.TextField(
            ref=self.reference,
            label=self.label,
            width=self.width
        )
    
class Radiobuttons(ft.UserControl):
    def __init__ (self,reference):
        super().__init__()
        self.reference = reference
    
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Como você se identifica?"),
                ft.RadioGroup(ref=self.reference,on_change=lambda e: print(e.control.value),content=ft.Column([
                ft.Radio(value="Homem cis", label="Homem cis"),
                ft.Radio(value="Homem trans", label="Homem trans"),
                ft.Radio(value="Mulher cis", label="Mulher cis"),
                ft.Radio(value="Mulher trans", label="Mulher trans"),
                ft.Radio(value="não-binário", label="não-binário")]))
            ]
        )

class Schoolingdropdown(ft.UserControl):
    def __init__(self, reference):
        super().__init__()
        self.reference = reference
    
    def build(self):
        return ft.Dropdown(
            ref=self.reference,
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
    def __init__(self, reference):
        super().__init__()
        self.reference = reference
    
    def build(self):
        return ft.Dropdown(
            ref=self.reference,
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

class InitialForm(ft.UserControl):
    def __init__(self, agetextfield_ref, coursetextfield_ref, genderradiobuttons_ref, schoolingdropdown_ref, elementsdropdown_ref,btn_onclick):
        super().__init__()
        self.agetextfield_ref = agetextfield_ref
        self.coursetextfield_ref = coursetextfield_ref
        self.genderradiobuttons_ref = genderradiobuttons_ref
        self.schoolingdropdown_ref = schoolingdropdown_ref
        self.elementsdropdown_ref = elementsdropdown_ref
        self.btn_onclick = btn_onclick
    
    def build(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=[
                Basetextfield("Informe sua idade", 200, self.agetextfield_ref),
                Radiobuttons(self.genderradiobuttons_ref),
                Schoolingdropdown(self.schoolingdropdown_ref),
                Basetextfield("Qual curso você realiza atualmente", 300, self.coursetextfield_ref),
                Elementsdropdown(self.elementsdropdown_ref),
                ft.FilledButton("Enviar",on_click=self.btn_onclick)
            ]
        )