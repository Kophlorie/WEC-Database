import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company2WEC2 import Company2WEC2

class Company2WEC20(Company2WEC2):
 company2wec20Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC2/WEC20/WEC20_description.txt"
 company2wec20Comment = """
BaseClass
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany2WEC20",["",""],""), p1 = "", p2 = "", p3 = ""):
    Company2WEC2.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2, p3)
    Company2WEC20.company2wec20Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec20Count = ",Company2WEC20.company2wec20Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company2WEC2):\np0:\n"+
    "company2wec2Count = "+str(Company2WEC2.company2wec2Count)+
    "\nnomenclatureFilePath = \""+Company2WEC2.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company2WEC2.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company2WEC2.descriptionFilePath+"\n"+
    "company2wec2Comment = "+"\"\"\""+Company2WEC2.company2wec2Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company2WEC20):\n"+
    "company2wec20Count = "+str(Company2WEC20.company2wec20Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company2/WEC2/WEC20/WEC20_description.txt\n"+
    "company2wec20Comment = "+"""\"\"\"
BaseClass
\"\"\""""+
    "\nMother (Company2WEC2) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (--) --> {0}\np2 = "" (kg) --> {1}\np3 = "" (kk) --> {2}\n""".format(self.bughf, self.hun, self.should)+"\n"+
    "Child (Company2WEC20) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company2wec20Count': Company2WEC20.company2wec20Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC2/WEC20/WEC20_description.txt', 'company2wec20Comment': '\nBaseClass'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['bughf', '', '(--)', self.bughf], 'p2': ['hun', '', '(kg)', self.hun], 'p3': ['should', '', '(kk)', self.should]}
    return paramsMotherDictionary