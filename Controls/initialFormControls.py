import flet as ft
import time, threading

class Countdown(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer,args=(),daemon=True)
        self.th.start()       

    def will_unmount(self):
        self.running = False
    
    def get_current_time(self):
        t = self.seconds
        m,s = divmod(t, 60)
        formated_time = "{:02d}:{:02d}".format(m, s)
        return formated_time
    
    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1
    
    def build(self):
        self.countdown = ft.Text()
        return self.countdown

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
    
class ValidationButton(ft.UserControl):
    def __init__(self,ref,text,type,on_click):
        super().__init__()
        self.ref = ref
        self.text = text
        self.type = type
        self.on_click = on_click
    
    def get_type(self):
        type = self.type
        return type
    
    def build(self):
        return ft.FilledButton(
            ref=self.ref,
            text=self.text,
            width=400,
            height=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=self.on_click
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
            label="nivel de conhecimento em elementos de máquina",
            hint_text="Qual seu nivel de conhecimento sobre elementos de maquina",
            width=430,
            options=[
                ft.dropdown.Option("Nenhum"),
                ft.dropdown.Option("Tenho pouco conhecimento"),
                ft.dropdown.Option("Estou aprendendo atualmente"),
                ft.dropdown.Option("Tenho um bom entendimento"),
            ],
        )

class ImgTraining(ft.UserControl):
    def __init__(self,src):
        super().__init__()
        self.src = src
    
    def build(self):
        return ft.Image(src=self.src, width=400, height=400,fit=ft.ImageFit.NONE,repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(10))

class ValidationImage(ft.UserControl):
    def __init__(self,src):
        super().__init__()
        self.src = src
    
    def build(self):
        return ft.Image(src=self.src, width=400, height=400,fit=ft.ImageFit.NONE,repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(10))

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
    
class TrainingItem(ft.UserControl):
    def __init__(self,title):
        super().__init__()
        self.title = title
        self.imglist = []

    def itembuilder(self):
        if self.title.lower() == "elementos de vedacao":
            img = ImgTraining("D:\ICpy\Plataforma de Testes IC\TrainingImages\Ved (2).jpg")
        elif self.title.lower() == "elementos de apoio":
            img = ImgTraining("D:\ICpy\Plataforma de Testes IC\TrainingImages\Apo (1).jpg")
        elif self.title.lower() == "elementos elasticos":
            img = ImgTraining("D:\ICpy\Plataforma de Testes IC\TrainingImages\Elast (2).jpg")
        elif self.title.lower() == "elementos de fixacao":
            img = ImgTraining("D:\ICpy\Plataforma de Testes IC\TrainingImages\Fix (3).jpg")
        else:
            print("Error")
        
        self.imglist = [img,img,img]
    
    def build(self):
        self.itembuilder()
        return ft.Column(
            controls=[
                ft.Text(value=self.title,text_align=ft.TextAlign.START,size=30),
                ft.Row(wrap=False,scroll="always",controls=self.imglist)
            ]
        )
    
class TrainingPage(ft.UserControl):
    def __init__(self,traininglist):
        super().__init__()
        self.traininglist = traininglist
    
    def build(self):
        return ft.Column(controls=self.traininglist)

class ValidationPage(ft.UserControl):
    def __init__(self,btn_1,btn_2,btn_3,btn_4):
        super().__init__()
        self.type = ""
        self.level = ""
        self.btn_1 = btn_1
        self.btn_2 = btn_2
        self.btn_3 = btn_3
        self.btn_4 = btn_4

    #images logic
    '''
    A partir do level setado, serao utilizados diferentes repositorios de imagens
    '''
    def get_level(self):
        level = self.level
        return level

    def get_type(self):
        type = self.type
        return type
    
    def build(self):
        return ft.Column(horizontal_alignment=ft.MainAxisAlignment.CENTER,controls=[
            ValidationImage("D:\ICpy\Plataforma de Testes IC\TrainingImages\Ved (2).jpg"),
            self.btn_1,
            self.btn_2,
            self.btn_3,
            self.btn_4    
        ])
'''
def main(page:ft.Page): page.add(ValidationPage())
ft.app(target=main)
'''