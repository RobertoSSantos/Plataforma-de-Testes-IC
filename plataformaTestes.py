from Controls.initialFormControls import *
from Models.allModels import *
from Service.dataService import *
import flet as ft
import time, random, json, requests

baseUrl = "https://plataforma-testes-ic-default-rtdb.firebaseio.com/"
validation_count = 0
backup_validation_types = ["Elemento de Vedacao", "Elemento de Apoio", "Elemento de Fixacao", "Elemento Elastico"]

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
    easyTestModel = EasyTestModel()
    mediumTestModel = MediumTestModel()
    hardTestModel = HardTestModel()
    finalFormModel = FinalFormModel()

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

    def reset_list():
        global backup_validation_types
        backup_validation_types = ["Elemento de Vedacao", "Elemento de Apoio", "Elemento de Fixacao", "Elemento Elastico"]

    def verify_answer(testmodel,val):
        if validation_count == 1 or validation_count == 6 or validation_count == 11:
            testmodel.firstAnswer = val
            testmodel.firstAnswerTime = countdown.get_current_time()
        elif validation_count == 2 or validation_count == 7 or validation_count == 12:
            testmodel.secondAnswer = val
            testmodel.secondAnswerTime = countdown.get_current_time()
        elif validation_count == 3 or validation_count == 8 or validation_count == 13:
            testmodel.thirdAnswer = val
            testmodel.thirdAnswerTime = countdown.get_current_time()
        elif validation_count == 4 or validation_count == 9 or validation_count == 14:
            testmodel.fourthAnswer = val
            testmodel.fourthAnswerTime = countdown.get_current_time()
        else:
            print("Todos os objetos instanciados")
    
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
        validation_types.remove(rand_type)
        validationPage.type = rand_type
        page.add(validationPage)
        increment_count()

    def validation_observer():
        print(validation_count)
        if validation_count >= 0 and validation_count <= 3:
            validation_builder("Facil")
        elif validation_count == 4:
            reset_list()
            increment_count()
            mediumTrainingContext()
        elif validation_count > 4 and validation_count <= 8:
            validation_builder("Medio")
        elif validation_count == 9:
            reset_list()
            increment_count()
            hardTrainingContext()
        elif validation_count > 9 and validation_count <= 13:
            validation_builder("Dificil")
        else:
            print("Todas as Validacoes Foram realizadas")
            finalFormContext()

    def vedvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        page_level = validationPage.get_level()
        if page_type == vedvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        if page_level == "Facil":
            verify_answer(easyTestModel,val)
        elif page_level == "Medio":
            verify_answer(mediumTestModel,val)
        elif page_level == "Dificil":
            verify_answer(hardTestModel,val)
        else:
            print("Error on validation")
        print(val)
        validation_observer()
        #instanciar no objeto
    
    def apovalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        page_level = validationPage.get_level()
        if page_type == apovalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        if page_level == "Facil":
            verify_answer(easyTestModel,val)
        elif page_level == "Medio":
            verify_answer(mediumTestModel,val)
        elif page_level == "Dificil":
            verify_answer(hardTestModel,val)
        else:
            print("Error on validation")
            print(val)
        validation_observer()
        #instanciar no objeto
    
    def fixvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        page_level = validationPage.get_level()
        if page_type == fixvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        if page_level == "Facil":
            verify_answer(easyTestModel,val)
        elif page_level == "Medio":
            verify_answer(mediumTestModel,val)
        elif page_level == "Dificil":
            verify_answer(hardTestModel,val)
        else:
            print("Error on validation")
            print(val)
        validation_observer()
        #instanciar no objeto
    
    def elastvalidation(e):
        val = "vazio"
        page_type = validationPage.get_type()
        page_level = validationPage.get_level()
        if page_type == elastvalidationbutton_ref.current.text:val = "Correto"
        else: val = "Errado"
        if page_level == "Facil":
            verify_answer(easyTestModel,val)
        elif page_level == "Medio":
            verify_answer(mediumTestModel,val)
        elif page_level == "Dificil":
            verify_answer(hardTestModel,val)
        else:
            print("Error on validation")
            print(val)
        validation_observer()
        #instanciar no objeto

    #Modified during tests and development, take out comments and set count to 0
    def submitInitialForm(e):
        cont = 0
        referenceslists = [agetextfield_ref,coursetextfield_ref,genderradiobuttons_ref,schoolingdropdown_ref,elementsdropdown_ref]
        
        for ref in referenceslists:
            if not ref.current.value:opensb(e)
            else:cont+=1

        if cont == len(referenceslists):
            page.dialog = dlg_easyTrainingContext
            dlg_easyTrainingContext.open = True
            page.update()

    # Envio do formulario final + envio dos dados para o banco
    def submitFinalForm(e):
        finalFormModel.teste = "teste"
        print("Teste Finalizado")
        resultsModel = ResultsModel(initialFormModel.__dict__, easyTestModel.__dict__, mediumTestModel.__dict__, hardTestModel.__dict__, finalFormModel.__dict__)

        jsonstr = json.dumps(resultsModel.__dict__)
        requisicao = requests.post('https://plataforma-testes-ic-default-rtdb.firebaseio.com//entrevistados/.json', data=jsonstr)
        print(requisicao)
        print(requisicao.text)


    def close_endFisrtContext_dlg(e):
        dlg_easyTrainingContext.open = False
        page.update()

    def close_easyDispersal_dlg(e):
        easy_dispersal_dialog.open = False
        page.update()

    def close_mediumDispersal_dlg(e):
        medium_dispersal_dialog.open = False
        page.update()

    def close_hardDispersal_dlg(e):
        hard_dispersal_dialog.open = False
        page.update()

    def easyTrainingContext(e):
        initialFormModel.age = agetextfield_ref.current.value
        initialFormModel.gender = genderradiobuttons_ref.current.value
        initialFormModel.course = coursetextfield_ref.current.value
        initialFormModel.schooling = schoolingdropdown_ref.current.value
        initialFormModel.elements = elementsdropdown_ref.current.value

        close_endFisrtContext_dlg(e)
        page.clean()
        appbar.title = ft.Text("Treinamento - Facil", size=30)
        appbar.actions.insert(0,countdown)
        page.add(ft.Column(controls=[trainPage, ft.FilledButton("Enviar",on_click=easytrainingNext)],alignment=ft.MainAxisAlignment.END))
        page.update()

    def mediumTrainingContext():
        page.clean()
        appbar.title = ft.Text("Treinamento - Medio", size=30)
        appbar.actions.insert(0,countdown)
        page.add(ft.Column(controls=[trainPage, ft.FilledButton("Enviar",on_click=mediumTrainingNext)],alignment=ft.MainAxisAlignment.END))
        page.update()

    def hardTrainingContext():
        page.clean()
        appbar.title = ft.Text("Treinamento - Dificil", size=30)
        appbar.actions.insert(0,countdown)
        page.add(ft.Column(controls=[trainPage, ft.FilledButton("Enviar",on_click=hardTrainingNext)],alignment=ft.MainAxisAlignment.END))
        page.update()

    def easytrainingNext(e):
        easyTestModel.trainingTime = countdown.get_current_time()
        print(easyTestModel.trainingTime)
        page.dialog = easy_dispersal_dialog
        easy_dispersal_dialog.open = True
        page.update()

    def mediumTrainingNext(e):
        mediumTestModel.trainingTime = countdown.get_current_time()
        print(mediumTestModel.trainingTime)
        page.dialog = medium_dispersal_dialog
        medium_dispersal_dialog.open = True
        page.update()

    def hardTrainingNext(e):
        hardTestModel.trainingTime = countdown.get_current_time()
        print(hardTestModel.trainingTime)
        page.dialog = hard_dispersal_dialog
        hard_dispersal_dialog.open = True
        page.update()

    def easyValidationContext(e):
        close_easyDispersal_dlg(e)
        page.clean()
        appbar.title = ft.Text("Validacao - Facil", size=30)
        validation_observer()
        page.update()

    def mediumValidationContext(e):
        close_mediumDispersal_dlg(e)
        page.clean()
        appbar.title = ft.Text("Validacao - Medio", size=30)
        validation_observer()
        page.update()

    def hardValidationContext(e):
        close_hardDispersal_dlg(e)
        page.clean()
        appbar.title = ft.Text("Validacao - Dificil", size=30)
        validation_observer()
        page.update()

    # Define o formulario Final
    def finalFormContext():
        page.clean()
        appbar.title = ft.Text("Formulario Final", size=30)
        page.add(finalForm)

    toggledarklight = ft.IconButton(on_click=changetheme,icon="dark_mode",selected_icon="light_mode",style=ft.ButtonStyle(color={"":ft.colors.BLACK, "selected":ft.colors.WHITE}))

    countdown = Countdown(1800)

    appbar = ft.AppBar(title= ft.Text("Formulario Inicial", size=30),center_title=True,bgcolor='blue',leading=ft.Icon(name="home"),actions=[toggledarklight])
    
    dlg_easyTrainingContext = ft.AlertDialog(modal=True,title=ft.Text("Confirmação"),content=ft.Text("Deseja iniciar o teste? ao aceitar nao sera possivel voltar ate que o teste seja concluido, e o cronometro sera iniciado."),actions=[ft.TextButton("Sim", on_click=easyTrainingContext),ft.TextButton("Não", on_click=close_endFisrtContext_dlg)],actions_alignment=ft.MainAxisAlignment.END)

    easy_dispersal_dialog = ft.AlertDialog(title=ft.Text("Responda essa questao"),content=ft.TextField(label="35 + 72 = ?"),actions=[ft.TextButton("Ok", on_click=easyValidationContext)],actions_alignment=ft.MainAxisAlignment.CENTER)

    medium_dispersal_dialog = ft.AlertDialog(title=ft.Text("Responda essa questao"),content=ft.TextField(label="54 + 84 = ?"),actions=[ft.TextButton("Ok", on_click=mediumValidationContext)],actions_alignment=ft.MainAxisAlignment.CENTER)

    hard_dispersal_dialog = ft.AlertDialog(title=ft.Text("Responda essa questao"),content=ft.TextField(label="984 + 84 = ?"),actions=[ft.TextButton("Ok",on_click=hardValidationContext)],actions_alignment=ft.MainAxisAlignment.CENTER)

    completeAll_sb = ft.SnackBar(content=ft.Text("Preencha todos os campos!",color=ft.colors.RED))

    initialForm = InitialForm(agetextfield_ref, coursetextfield_ref, genderradiobuttons_ref, schoolingdropdown_ref, elementsdropdown_ref,submitInitialForm)

    finalForm = ft.FilledButton("Finalizar Teste",on_click=submitFinalForm)

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