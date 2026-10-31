import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company1WEC2 import Company1WEC2

class Company1WEC21(Company1WEC2):
 company1wec21Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company1/WEC2/WEC21/WEC21_description.txt"
 company1wec21Comment = """
The plate has been decided to be rectangle in any case.
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany1WEC21",["",""],""), p1 = "", p2 = "", p3 = "rectangle", p4 = "", p5 = ""):
    Company1WEC2.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2, p3)
    self.plate_width = p4 # (m)
    self.plate_length = p5 # (m)
    Company1WEC21.company1wec21Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company1wec21Count = ",Company1WEC21.company1wec21Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company1WEC2):\np0:\n"+
    "company1wec2Count = "+str(Company1WEC2.company1wec2Count)+
    "\nnomenclatureFilePath = \""+Company1WEC2.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company1WEC2.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company1WEC2.descriptionFilePath+"\n"+
    "company1wec2Comment = "+"\"\"\""+Company1WEC2.company1wec2Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company1WEC21):\n"+
    "company1wec21Count = "+str(Company1WEC21.company1wec21Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company1/WEC2/WEC21/WEC21_description.txt\n"+
    "company1wec21Comment = "+"""\"\"\"
The plate has been decided to be rectangle in any case.
\"\"\""""+
    "\nMother (Company1WEC2) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (--) --> {0}\np2 = "" (m) --> {1}\np3 = "rectangle" (--) --> {2}\n""".format(self.nb_of_plates, self.overall_length_of_the_wire, self.plate_shape)+"\n"+
    "Child (Company1WEC21) parameters:\n"+
    """p4 = "" (m) --> {0}\np5 = "" (m) --> {1}\n""".format(self.plate_width, self.plate_length)+"\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company1wec21Count': Company1WEC21.company1wec21Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company1/WEC2/WEC21/WEC21_description.txt', 'company1wec21Comment': '\nThe plate has been decided to be rectangle in any case.'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {'p4': ['plate_width', '', '(m)', self.plate_width], 'p5': ['plate_length', '', '(m)', self.plate_length]}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['nb_of_plates', '', '(--)', self.nb_of_plates], 'p2': ['overall_length_of_the_wire', '', '(m)', self.overall_length_of_the_wire], 'p3': ['plate_shape', 'rectangle', '(--)', self.plate_shape]}
    return paramsMotherDictionary