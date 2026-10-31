import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.WeptosWeptosWEC import WeptosWeptosWEC

class WeptosWeptosWEC0(WeptosWeptosWEC):
 weptosweptoswec0Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Weptos/WeptosWEC/WeptosWEC0/WeptosWEC0_description.txt"
 weptosweptoswec0Comment = """
blunt used of the WEC mother
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildWeptosWeptosWEC0",["",""],""), p1 = ""):
    WeptosWeptosWEC.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1)
    WeptosWeptosWEC0.weptosweptoswec0Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and weptosweptoswec0Count = ",WeptosWeptosWEC0.weptosweptoswec0Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (WeptosWeptosWEC):\np0:\n"+
    "weptosweptoswecCount = "+str(WeptosWeptosWEC.weptosweptoswecCount)+
    "\nnomenclatureFilePath = \""+WeptosWeptosWEC.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+WeptosWeptosWEC.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+WeptosWeptosWEC.descriptionFilePath+"\n"+
    "weptosweptoswecComment = "+"\"\"\""+WeptosWeptosWEC.weptosweptoswecComment+"\"\"\"")
    print("Attributes from the WEC child class (WeptosWeptosWEC0):\n"+
    "weptosweptoswec0Count = "+str(WeptosWeptosWEC0.weptosweptoswec0Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/Weptos/WeptosWEC/WeptosWEC0/WeptosWEC0_description.txt\n"+
    "weptosweptoswec0Comment = "+"""\"\"\"
blunt used of the WEC mother
\"\"\""""+
    "\nMother (WeptosWeptosWEC) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (m) --> {0}\n""".format(self.arm_length)+"\n"+
    "Child (WeptosWeptosWEC0) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'weptosweptoswec0Count': WeptosWeptosWEC0.weptosweptoswec0Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Weptos/WeptosWEC/WeptosWEC0/WeptosWEC0_description.txt', 'weptosweptoswec0Comment': '\nblunt used of the WEC mother'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['arm_length', '', '(m)', self.arm_length]}
    return paramsMotherDictionary