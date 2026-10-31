import numpy as np
from CoreFunctions.FixRFID import FixRFID

class NonCompanyRelatedCylinder:
 noncompanyrelatedcylinderCount = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/NonCompanyRelated/Cylinder/Cylinder_description.txt"
 noncompanyrelatedcylinderComment = """
this is the class related to all the cylinder tests that are not related to a WEC or a company.
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECNonCompanyRelatedCylinder")
    self.diameter = p1 # (m)
    self.draft = p2 # (m)
    NonCompanyRelatedCylinder.noncompanyrelatedcylinderCount += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and noncompanyrelatedcylinderCount = ",NonCompanyRelatedCylinder.noncompanyrelatedcylinderCount)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'noncompanyrelatedcylinderCount': NonCompanyRelatedCylinder.noncompanyrelatedcylinderCount, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/NonCompanyRelated/Cylinder/Cylinder_description.txt', 'noncompanyrelatedcylinderComment': '\nthis is the class related to all the cylinder tests that are not related to a WEC or a company.'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['diameter', '', '(m)', self.diameter], 'p2': ['draft', '', '(m)', self.draft]}
    return paramsDictionary