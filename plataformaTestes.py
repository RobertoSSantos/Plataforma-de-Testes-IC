from Controls.initialFormControls import *
from Models.allModels import *
from Service.dataService import *
import flet as ft
import time

baseUrl = "https://plataforma-testes-ic-default-rtdb.firebaseio.com/"

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

    #Models
    initialFormModel = InitialFormModel()

    #References
    agetextfield_ref = ft.Ref[ft.TextField]()
    coursetextfield_ref = ft.Ref[ft.TextField]()
    genderradiobuttons_ref = ft.Ref[ft.RadioGroup]()
    schoolingdropdown_ref = ft.Ref[ft.Dropdown]()
    elementsdropdown_ref = ft.Ref[ft.Dropdown]()

    #Toggle Dark/Light Mode
    def changetheme(e):
        page.splash.visible = True
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()
        time.sleep(0.5)
        toggledarklight.selected = not toggledarklight.selected
        page.splash.visible = False
        page.update()

    def opensb(e):
        page.snack_bar = completeAll_sb
        page.snack_bar.open = True
        page.update()

    #Modified during tests and development, take out comments and set count to 0
    def submitInitialForm(e):
        cont = 5
        referenceslists = [agetextfield_ref,coursetextfield_ref,genderradiobuttons_ref,schoolingdropdown_ref,elementsdropdown_ref]
        '''
        for ref in referenceslists:
            if not ref.current.value:opensb(e)
            else:cont+=1
        '''
        if cont == len(referenceslists):
            page.dialog = dlg_endFistContext
            dlg_endFistContext.open = True
            page.update()

    def close_endFisrtContext_dlg(e):
        dlg_endFistContext.open = False
        page.update()

    def endFistContext(e):
        initialFormModel.age = agetextfield_ref.current.value
        initialFormModel.gender = genderradiobuttons_ref.current.value
        initialFormModel.course = coursetextfield_ref.current.value
        initialFormModel.schooling = schoolingdropdown_ref.current.value
        initialFormModel.elements = elementsdropdown_ref.current.value

        close_endFisrtContext_dlg(e)
        page.clean()
        appbar.title = ft.Text("Treinamento - Facil", size=30)
        page.add(trainPage)
        page.update()

    toggledarklight = ft.IconButton(on_click=changetheme,icon="dark_mode",selected_icon="light_mode",style=ft.ButtonStyle(color={"":ft.colors.BLACK, "selected":ft.colors.WHITE}))

    placeholderCountdown = ft.Text("00:00")

    appbar = ft.AppBar(title= ft.Text("Formulario Inicial", size=30),center_title=True,bgcolor='blue',leading=ft.Icon(name="home"),actions=[placeholderCountdown,toggledarklight])
    
    dlg_endFistContext = ft.AlertDialog(modal=True,title=ft.Text("Confirmação"),content=ft.Text("Deseja iniciar o teste? ao aceitar nao sera possivel voltar ate que o teste seja concluido, e o cronometro sera iniciado."),actions=[ft.TextButton("Sim", on_click=endFistContext),ft.TextButton("Não", on_click=close_endFisrtContext_dlg)],actions_alignment=ft.MainAxisAlignment.END)

    completeAll_sb = ft.SnackBar(content=ft.Text("Preencha todos os campos!",color=ft.colors.RED))

    initialForm = InitialForm(agetextfield_ref, coursetextfield_ref, genderradiobuttons_ref, schoolingdropdown_ref, elementsdropdown_ref,submitInitialForm)

    traininglist = [TrainingItem("Elementos de Apoio"),TrainingItem("Elementos Elasticos"),TrainingItem("Elementos de Fixacao"),TrainingItem("Elementos de Vedacao")]
    
    trainPage = TrainingPage(traininglist)

    page.appbar = appbar
    page.add(initialForm)
    
ft.app(target=main)