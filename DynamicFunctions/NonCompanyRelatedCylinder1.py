import numpy as np
from CoreFunctions.FixRFID import FixRFID
from DynamicFunctions.NonCompanyRelatedCylinder import NonCompanyRelatedCylinder

class NonCompanyRelatedCylinder1(NonCompanyRelatedCylinder):
 noncompanyrelatedcylinder1Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/NonCompanyRelated/Cylinder/Cylinder1/Cylinder1_description.txt"
 noncompanyrelatedcylinder1Comment = """
Be carefull we are only mentioning here about the submerged draft!
"""
 def __init__(self, name = "", comments = "", descriptionpath = "", nomenclaturefilepath = "", functionfilespath = "", country_time = "", idwec = FixRFID("","WECChildNonCompanyRelatedCylinder1",["",""],""), p1 = "", p2 = ""):
    NonCompanyRelatedCylinder.__init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2)
    NonCompanyRelatedCylinder1.noncompanyrelatedcylinder1Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and noncompanyrelatedcylinder1Count = ",NonCompanyRelatedCylinder1.noncompanyrelatedcylinder1Count)
 def __str__(self):
    print("\n\nPrinting the object ("+self.name+"):\n\nAttributes from the WEC mother class (NonCompanyRelatedCylinder):\np0:\n"+
    "noncompanyrelatedcylinderCount = "+str(NonCompanyRelatedCylinder.noncompanyrelatedcylinderCount)+
    "\nnomenclatureFilePath = \""+NonCompanyRelatedCylinder.nomenclatureFilePath+"\"\n"+
    "functionFilesPath = \""+NonCompanyRelatedCylinder.functionFilesPath+"\"\n"+
    "descriptionFilePath = "+NonCompanyRelatedCylinder.descriptionFilePath+"\n"+
    "noncompanyrelatedcylinderComment = "+"\"\"\""+NonCompanyRelatedCylinder.noncompanyrelatedcylinderComment+"\"\"\"")
    print("Attributes from the WEC child class (NonCompanyRelatedCylinder1):\n"+
    "noncompanyrelatedcylinder1Count = "+str(NonCompanyRelatedCylinder1.noncompanyrelatedcylinder1Count)+
    "\nnomenclatureFilePath = \" \"\n"+
    "functionFilesPath = \" \"\n"+
    "descriptionFilePath = Database/NonCompanyRelated/Cylinder/Cylinder1/Cylinder1_description.txt\n"+
    "noncompanyrelatedcylinder1Comment = "+"""\"\"\"
Be carefull we are only mentioning here about the submerged draft!
\"\"\""""+
    "\nMother (NonCompanyRelatedCylinder) parameters including the fixed ones:\n"+
    "name = "+self.name+"\ncomments = "+self.comments+"\ndescriptionpath = "+self.descriptionPath+"\nnomenclaturefilepath = "+self.nomenclatureFilePath+"\nfunctionfilespath = "+self.functionFilesPath+"\ncountry_time = "+self.country_time+"\nidwec = "+str(self.IDwec)+"\n"+
    """p1 = "" (m) --> {0}\np2 = "" (m) --> {1}\n""".format(self.diameter, self.draft)+"\n"+
    "Child (NonCompanyRelatedCylinder1) parameters:\n"+
    """None"""+"\n\n")
    return "That's all for the WEC ({0})".format(self.name)

 def getWECChildClassParams(self):
    classParamsDictionary = {'noncompanyrelatedcylinder1Count': NonCompanyRelatedCylinder1.noncompanyrelatedcylinder1Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/NonCompanyRelated/Cylinder/Cylinder1/Cylinder1_description.txt', 'noncompanyrelatedcylinder1Comment': '\nBe carefull we are only mentioning here about the submerged draft!'}
    return classParamsDictionary

 def getWECChildObjectParams(self):
    paramsChildDictionary = {}
    return paramsChildDictionary

 def getWECMotherObjectParams(self):
    paramsMotherDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['diameter', '', '(m)', self.diameter], 'p2': ['draft', '', '(m)', self.draft]}
    return paramsMotherDictionary