import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company2WEC3 import Company2WEC3

class Company2WEC31(Company2WEC3):
 company2wec31Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC3/WEC31/WEC31_description.txt"
 company2wec31Comment = """
we are implementing something a new param, since the above class has no parameters,
we cannot fix anything but we can add a new parameter (so the first of the class, well child class)...
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany2WEC31",["",""],""), p1 = ""):
    Company2WEC3.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec)
    self.test = p1 # (--)
    Company2WEC31.company2wec31Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec31Count = ",Company2WEC31.company2wec31Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company2WEC3):\np0:\n"+
    "company2wec3Count = "+str(Company2WEC3.company2wec3Count)+
    "\nnomenclatureFilePath = \""+Company2WEC3.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company2WEC3.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company2WEC3.descriptionFilePath+"\n"+
    "company2wec3Comment = "+"\"\"\""+Company2WEC3.company2wec3Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company2WEC31):\n"+
    "company2wec31Count = "+str(Company2WEC31.company2wec31Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company2/WEC3/WEC31/WEC31_description.txt\n"+
    "company2wec31Comment = "+"""\"\"\"
we are implementing something a new param, since the above class has no parameters,
we cannot fix anything but we can add a new parameter (so the first of the class, well child class)...
\"\"\""""+
    "\nMother (Company2WEC3) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """None"""+"\n\n"+
    "Child (Company2WEC31) parameters:\n"+
    """p1 = "" (--) --> {0}\n""".format(self.test)+"\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company2wec31Count': Company2WEC31.company2wec31Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC3/WEC31/WEC31_description.txt', 'company2wec31Comment': '\nwe are implementing something a new param, since the above class has no parameters,\nwe cannot fix anything but we can add a new parameter (so the first of the class, well child class)...'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {'p1': ['test', '""', '(--)', self.test]}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time}
    return paramsMotherDictionary