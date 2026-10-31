import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company1WEC1 import Company1WEC1

class Company1WEC12(Company1WEC1):
 company1wec12Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company1/WEC1/WEC12/WEC12_description.txt"
 company1wec12Comment = """
The plate has been decided to be circular in any case.
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany1WEC12",["",""],""), p1 = "", p2 = "", p3 = "circular", p4 = ""):
    Company1WEC1.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2, p3)
    self.plate_diameter = p4 # (m)
    Company1WEC12.company1wec12Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company1wec12Count = ",Company1WEC12.company1wec12Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company1WEC1):\np0:\n"+
    "company1wec1Count = "+str(Company1WEC1.company1wec1Count)+
    "\nnomenclatureFilePath = \""+Company1WEC1.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company1WEC1.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company1WEC1.descriptionFilePath+"\n"+
    "company1wec1Comment = "+"\"\"\""+Company1WEC1.company1wec1Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company1WEC12):\n"+
    "company1wec12Count = "+str(Company1WEC12.company1wec12Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company1/WEC1/WEC12/WEC12_description.txt\n"+
    "company1wec12Comment = "+"""\"\"\"
The plate has been decided to be circular in any case.
\"\"\""""+
    "\nMother (Company1WEC1) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (--) --> {0}\np2 = "" (m) --> {1}\np3 = "circular" (--) --> {2}\n""".format(self.nb_of_plates, self.overall_length_of_the_wire, self.plate_shape)+"\n"+
    "Child (Company1WEC12) parameters:\n"+
    """p4 = "" (m) --> {0}\n""".format(self.plate_diameter)+"\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company1wec12Count': Company1WEC12.company1wec12Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company1/WEC1/WEC12/WEC12_description.txt', 'company1wec12Comment': '\nThe plate has been decided to be circular in any case.'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {'p4': ['plate_diameter', '', '(m)', self.plate_diameter]}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['nb_of_plates', '', '(--)', self.nb_of_plates], 'p2': ['overall_length_of_the_wire', '', '(m)', self.overall_length_of_the_wire], 'p3': ['plate_shape', 'circular', '(--)', self.plate_shape]}
    return paramsMotherDictionary