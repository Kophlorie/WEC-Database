import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.WeptosWeptosWEC import WeptosWeptosWEC

class WeptosWeptosWEC1(WeptosWeptosWEC):
 weptosweptoswec1Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Weptos/WeptosWEC/WeptosWEC1/WeptosWEC1_description.txt"
 weptosweptoswec1Comment = """
test
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildWeptosWeptosWEC1",["",""],""), p1 = "", p2 = ""):
    WeptosWeptosWEC.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1)
    self.angle = p2 # (degree)
    WeptosWeptosWEC1.weptosweptoswec1Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and weptosweptoswec1Count = ",WeptosWeptosWEC1.weptosweptoswec1Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (WeptosWeptosWEC):\np0:\n"+
    "weptosweptoswecCount = "+str(WeptosWeptosWEC.weptosweptoswecCount)+
    "\nnomenclatureFilePath = \""+WeptosWeptosWEC.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+WeptosWeptosWEC.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+WeptosWeptosWEC.descriptionFilePath+"\n"+
    "weptosweptoswecComment = "+"\"\"\""+WeptosWeptosWEC.weptosweptoswecComment+"\"\"\"")
    print("Attributes from the WEC child class (WeptosWeptosWEC1):\n"+
    "weptosweptoswec1Count = "+str(WeptosWeptosWEC1.weptosweptoswec1Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Weptos/WeptosWEC/WeptosWEC1/WeptosWEC1_description.txt\n"+
    "weptosweptoswec1Comment = "+"""\"\"\"
test
\"\"\""""+
    "\nMother (WeptosWeptosWEC) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (m) --> {0}\n""".format(self.arm_length)+"\n"+
    "Child (WeptosWeptosWEC1) parameters:\n"+
    """p2 = "" (degree) --> {0}\n""".format(self.angle)+"\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'weptosweptoswec1Count': WeptosWeptosWEC1.weptosweptoswec1Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Weptos/WeptosWEC/WeptosWEC1/WeptosWEC1_description.txt', 'weptosweptoswec1Comment': '\ntest'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {'p2': ['angle', '', '(degree)', self.angle]}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['arm_length', '', '(m)', self.arm_length]}
    return paramsMotherDictionary