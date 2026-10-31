import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.Company2WEC4 import Company2WEC4

class Company2WEC41(Company2WEC4):
 company2wec41Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC4/WEC41/WEC41_description.txt"
 company2wec41Comment = """
we are implementing something a new param, since the above class has no parameters,
we cannot fix anything but we can add a new parameter (so the first of the class, well child class)...
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildCompany2WEC41",["",""],""), p1 = ""):
    Company2WEC4.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec)
    self.test = p1 # (--)
    Company2WEC41.company2wec41Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec41Count = ",Company2WEC41.company2wec41Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (Company2WEC4):\np0:\n"+
    "company2wec4Count = "+str(Company2WEC4.company2wec4Count)+
    "\nnomenclatureFilePath = \""+Company2WEC4.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+Company2WEC4.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+Company2WEC4.descriptionFilePath+"\n"+
    "company2wec4Comment = "+"\"\"\""+Company2WEC4.company2wec4Comment+"\"\"\"")
    print("Attributes from the WEC child class (Company2WEC41):\n"+
    "company2wec41Count = "+str(Company2WEC41.company2wec41Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Company2/WEC4/WEC41/WEC41_description.txt\n"+
    "company2wec41Comment = "+"""\"\"\"
we are implementing something a new param, since the above class has no parameters,
we cannot fix anything but we can add a new parameter (so the first of the class, well child class)...
\"\"\""""+
    "\nMother (Company2WEC4) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """None"""+"\n\n"+
    "Child (Company2WEC41) parameters:\n"+
    """p1 = "" (--) --> {0}\n""".format(self.test)+"\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'company2wec41Count': Company2WEC41.company2wec41Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC4/WEC41/WEC41_description.txt', 'company2wec41Comment': '\nwe are implementing something a new param, since the above class has no parameters,\nwe cannot fix anything but we can add a new parameter (so the first of the class, well child class)...'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {'p1': ['test', '""', '(--)', self.test]}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time}
    return paramsMotherDictionary