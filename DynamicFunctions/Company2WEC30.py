import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company2WEC3 import Company2WEC3

class Company2WEC30(Company2WEC3):
 company2wec30Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC3/WEC30/WEC30_description.txt"
 company2wec30Comment = """
BaseClass
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany2WEC30",["",""],"")):
    Company2WEC3.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec)
    Company2WEC30.company2wec30Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec30Count = ",Company2WEC30.company2wec30Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company2WEC3):\np0:\n"+
    "company2wec3Count = "+str(Company2WEC3.company2wec3Count)+
    "\nnomenclatureFilePath = \""+Company2WEC3.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company2WEC3.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company2WEC3.descriptionFilePath+"\n"+
    "company2wec3Comment = "+"\"\"\""+Company2WEC3.company2wec3Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company2WEC30):\n"+
    "company2wec30Count = "+str(Company2WEC30.company2wec30Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company2/WEC3/WEC30/WEC30_description.txt\n"+
    "company2wec30Comment = "+"""\"\"\"
BaseClass
\"\"\""""+
    "\nMother (Company2WEC3) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """None"""+"\n\n"+
    "Child (Company2WEC30) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company2wec30Count': Company2WEC30.company2wec30Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC3/WEC30/WEC30_description.txt', 'company2wec30Comment': '\nBaseClass'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time}
    return paramsMotherDictionary