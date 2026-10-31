import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.NonCompanyRelatedCylinder import NonCompanyRelatedCylinder

class NonCompanyRelatedCylinder0(NonCompanyRelatedCylinder):
 noncompanyrelatedcylinder0Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/NonCompanyRelated/Cylinder/Cylinder0/Cylinder0_description.txt"
 noncompanyrelatedcylinder0Comment = """
Base class
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildNonCompanyRelatedCylinder0",["",""],""), p1 = "", p2 = ""):
    NonCompanyRelatedCylinder.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2)
    NonCompanyRelatedCylinder0.noncompanyrelatedcylinder0Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and noncompanyrelatedcylinder0Count = ",NonCompanyRelatedCylinder0.noncompanyrelatedcylinder0Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (NonCompanyRelatedCylinder):\np0:\n"+
    "noncompanyrelatedcylinderCount = "+str(NonCompanyRelatedCylinder.noncompanyrelatedcylinderCount)+
    "\nnomenclatureFilePath = \""+NonCompanyRelatedCylinder.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+NonCompanyRelatedCylinder.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+NonCompanyRelatedCylinder.descriptionFilePath+"\n"+
    "noncompanyrelatedcylinderComment = "+"\"\"\""+NonCompanyRelatedCylinder.noncompanyrelatedcylinderComment+"\"\"\"")
    print("Attributes from the WEC child class (NonCompanyRelatedCylinder0):\n"+
    "noncompanyrelatedcylinder0Count = "+str(NonCompanyRelatedCylinder0.noncompanyrelatedcylinder0Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/NonCompanyRelated/Cylinder/Cylinder0/Cylinder0_description.txt\n"+
    "noncompanyrelatedcylinder0Comment = "+"""\"\"\"
Base class
\"\"\""""+
    "\nMother (NonCompanyRelatedCylinder) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (m) --> {0}\np2 = "" (m) --> {1}\n""".format(self.diameter, self.draft)+"\n"+
    "Child (NonCompanyRelatedCylinder0) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'noncompanyrelatedcylinder0Count': NonCompanyRelatedCylinder0.noncompanyrelatedcylinder0Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/NonCompanyRelated/Cylinder/Cylinder0/Cylinder0_description.txt', 'noncompanyrelatedcylinder0Comment': '\nBase class'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['diameter', '', '(m)', self.diameter], 'p2': ['draft', '', '(m)', self.draft]}
    return paramsMotherDictionary