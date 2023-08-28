class InitialFormModel:
    def __init__(self):
        self.age = ""
        self.gender = ""
        self.schooling = ""
        self.course = ""
        self.elements = ""

class EasyTestModel():
    def __init__(self):
        self.trainingTime = ""
        self.firstAnswer = ""
        self.firstAnswerTime = ""
        self.secondAnswer = ""
        self.secondAnswerTime = ""
        self.thirdAnswer = ""
        self.thirdAnswerTime = ""
        self.fourthAnswer = ""
        self.fourthAnswerTime = ""

class MediumTestModel():
    def __init__(self):
        self.trainingTime = ""
        self.firstAnswer = ""
        self.firstAnswerTime = ""
        self.secondAnswer = ""
        self.secondAnswerTime = ""
        self.thirdAnswer = ""
        self.thirdAnswerTime = ""
        self.fourthAnswer = ""
        self.fourthAnswerTime = ""

class HardTestModel():
    def __init__(self):
        self.trainingTime = ""
        self.firstAnswer = ""
        self.firstAnswerTime = ""
        self.secondAnswer = ""
        self.secondAnswerTime = ""
        self.thirdAnswer = ""
        self.thirdAnswerTime = ""
        self.fourthAnswer = ""
        self.fourthAnswerTime = ""

class FinalFormModel():
    def __init__(self):
        self.teste = ""

class ResultsModel:
    def __init__(self, initialFormModel, easyTestModel, mediumTestModel, hardTestModel, finalFormModel):
        self.initialFormModel = initialFormModel
        self.easyTestModel = easyTestModel
        self.mediumTestModel = mediumTestModel
        self.hardTestModel = hardTestModel
        self.finalFormModel = finalFormModel   
