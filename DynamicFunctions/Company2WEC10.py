import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company2WEC1 import Company2WEC1

class Company2WEC10(Company2WEC1):
 company2wec10Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC1/WEC10/WEC10_description.txt"
 company2wec10Comment = """
BaseClass
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany2WEC10",["",""],""), p1 = "", p2 = ""):
    Company2WEC1.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2)
    Company2WEC10.company2wec10Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec10Count = ",Company2WEC10.company2wec10Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company2WEC1):\np0:\n"+
    "company2wec1Count = "+str(Company2WEC1.company2wec1Count)+
    "\nnomenclatureFilePath = \""+Company2WEC1.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company2WEC1.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company2WEC1.descriptionFilePath+"\n"+
    "company2wec1Comment = "+"\"\"\""+Company2WEC1.company2wec1Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company2WEC10):\n"+
    "company2wec10Count = "+str(Company2WEC10.company2wec10Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company2/WEC1/WEC10/WEC10_description.txt\n"+
    "company2wec10Comment = "+"""\"\"\"
BaseClass
\"\"\""""+
    "\nMother (Company2WEC1) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (--) --> {0}\np2 = "" (m) --> {1}\n""".format(self.angle, self.length_of_the_axles)+"\n"+
    "Child (Company2WEC10) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company2wec10Count': Company2WEC10.company2wec10Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC1/WEC10/WEC10_description.txt', 'company2wec10Comment': '\nBaseClass'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['angle', '', '(--)', self.angle], 'p2': ['length_of_the_axles', '', '(m)', self.length_of_the_axles]}
    return paramsMotherDictionary