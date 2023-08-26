class InitialFormModel:
    def __init__(self):
        self.age = ""
        self.gender = ""
        self.schooling = ""
        self.course = ""
        self.elements = ""

class EasyTestModel():
    pass

class MediumTestModel():
    pass

class HardTestModel():
    pass

class FinalFormModel():
    pass

class ResultsModel:
    def __init__(self, initialFormModel, easyTestModel, mediumTestModel, hardTestModel, finalFormModel):
        self.initialFormModel = initialFormModel
        self.easyTestModel = easyTestModel
        self.mediumTestModel = mediumTestModel
        self.hardTestModel = hardTestModel   