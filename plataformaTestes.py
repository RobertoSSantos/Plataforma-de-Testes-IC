from Controls.initialFormControls import *
from Models.allModels import *
from Service.dataService import *
import flet as ft
import time, random

baseUrl = "https://plataforma-testes-ic-default-rtdb.firebaseio.com/"
validation_count = 0

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

    backup_validation_types = ["Elemento de Vedacao", "Elemento de Apoio", "Elemento de Fixacao", "Elemento Elastico"]

    #Models
    initialFormModel = InitialFormModel()
    easyTestModel = EasyTestModel()

    #References
    agetextfield_ref = ft.Ref[ft.TextField]()
    coursetextfield_ref = ft.Ref[ft.TextField]()
    genderradiobuttons_ref = ft.Ref[ft.RadioGroup]()
    schoolingdropdown_ref = ft.Ref[ft.Dropdown]()
    elementsdropdown_ref = ft.Ref[ft.Dropdown]()
    vedvalidationbutton_ref = ft.Ref[ValidationButton]()
    apovalidationbutton_ref = ft.Ref[ValidationButton]()
    fixvalidationbutton_ref = ft.Ref[ValidationButton]()
    elastvalidationbutton_ref = ft.Ref[ValidationButton]()

    def increment_count():
        global validation_count
        validation_count += 1

    def verify_answer(val):
        if validation_count == 0:
            easyTestModel.firstAnswer = val
            easyTestModel.firstAnswerTime = countdown.get_current_time()
            print(easyTestModel.firstAnswer)
            print(easyTestModel.firstAnswerTime)
        elif validation_count == 1:
            easyTestModel.secondAnswer = val
            easyTestModel.secondAnswerTime = countdown.get_current_time()
            print(easyTestModel.secondAnswer)
            print(easyTestModel.secondAnswerTime)
        elif validation_count == 2:
            easyTestModel.thirdAnswer = val
            easyTestModel.thirdAnswerTime = countdown.get_current_time()
            print(easyTestModel.thirdAnswer)
            print(easyTestModel.thirdAnswerTime)
        elif validation_count == 3:
            easyTestModel.fourthAnswer = val
            easyTestModel.fourthAnswerTime = countdown.get_current_time()
            print(easyTestModel.fourthAnswer)
            print(easyTestModel.fourthAnswerTime)
        else:
            print("Error")
    
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

    def validation_builder(level):
        validationPage.level = level
        validation_types = backup_validation_types
        rand_type = random.choice(validation_types)
        print(rand_type)

        if len(validation_types) == 0:
            validation_types = backup_validation_types
        else:
            validation_types.remove(rand_type)
        
        validationPage.type = rand_type
        page.add(validationPage)
        increment_count()

    def validation_observer(level):
        print(validation_count)
        if validation_count >= 0 and validation_count < 4:
            validation_builder(level)
        else:
            print("Finalizando")


    def vedvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        if page_type == vedvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        verify_answer(val)
        validation_observer("Facil")
        #instanciar no objeto
    
    def apovalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        if page_type == apovalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        verify_answer(val)
        validation_observer("Facil")
        #instanciar no objeto
    
    def fixvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        if page_type == fixvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        verify_answer(val)
        validation_observer("Facil")
        #instanciar no objeto
    
    def elastvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        if page_type == elastvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        verify_answer(val)
        validation_observer("Facil")
        #instanciar no objeto

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

    def close_endSecondContext_dlg(e):
        dlg_dispersal.open = False
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
        appbar.actions.insert(0,countdown)
        page.add(ft.Column(controls=[trainPage, ft.FilledButton("Enviar",on_click=trainingNext)],alignment=ft.MainAxisAlignment.END))
        page.update()

    def trainingNext(e):
        easyTestModel.trainingTime = countdown.get_current_time()
        print(easyTestModel.trainingTime)
        page.dialog = dlg_dispersal
        dlg_dispersal.open = True
        page.update()

    def endSecondContext(e):
        close_endSecondContext_dlg(e)
        page.clean()
        appbar.title = ft.Text("Validacao - Facil", size=30)
        validation_observer("Facil")
        page.update()

    toggledarklight = ft.IconButton(on_click=changetheme,icon="dark_mode",selected_icon="light_mode",style=ft.ButtonStyle(color={"":ft.colors.BLACK, "selected":ft.colors.WHITE}))

    countdown = Countdown(900)

    appbar = ft.AppBar(title= ft.Text("Formulario Inicial", size=30),center_title=True,bgcolor='blue',leading=ft.Icon(name="home"),actions=[toggledarklight])
    
    dlg_endFistContext = ft.AlertDialog(modal=True,title=ft.Text("Confirmação"),content=ft.Text("Deseja iniciar o teste? ao aceitar nao sera possivel voltar ate que o teste seja concluido, e o cronometro sera iniciado."),actions=[ft.TextButton("Sim", on_click=endFistContext),ft.TextButton("Não", on_click=close_endFisrtContext_dlg)],actions_alignment=ft.MainAxisAlignment.END)

    dlg_dispersal = ft.AlertDialog(title=ft.Text("Responda essa questao"),content=ft.TextField(label="35 + 72 = ?"),actions=[ft.TextButton("Ok", on_click=endSecondContext)],actions_alignment=ft.MainAxisAlignment.CENTER)

    completeAll_sb = ft.SnackBar(content=ft.Text("Preencha todos os campos!",color=ft.colors.RED))

    initialForm = InitialForm(agetextfield_ref, coursetextfield_ref, genderradiobuttons_ref, schoolingdropdown_ref, elementsdropdown_ref,submitInitialForm)

    traininglist = [TrainingItem("Elementos de Apoio"),TrainingItem("Elementos Elasticos"),TrainingItem("Elementos de Fixacao"),TrainingItem("Elementos de Vedacao")]
    
    trainPage = TrainingPage(traininglist)

    validation_btn_1 = ValidationButton(vedvalidationbutton_ref,"Elemento de Vedacao","ved",vedvalidation)
    validation_btn_2 = ValidationButton(apovalidationbutton_ref,"Elemento de Apoio","apo",apovalidation)
    validation_btn_3 = ValidationButton(fixvalidationbutton_ref,"Elemento de Fixacao","fix",fixvalidation)
    validation_btn_4 = ValidationButton(elastvalidationbutton_ref,"Elemento Elastico","elast",elastvalidation)

    validationPage = ValidationPage(validation_btn_1,validation_btn_2,validation_btn_3,validation_btn_4)
    

    page.appbar = appbar
    page.add(initialForm)
    
ft.app(target=main)