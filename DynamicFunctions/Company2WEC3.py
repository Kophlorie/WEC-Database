import numpy as np
from CoreFunctions.FixRFID import FixRFID

class Company2WEC3:
 company2wec3Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC3/WEC3_description.txt"
 company2wec3Comment = """
Flap that is beautiful
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECCompany2WEC3")
    Company2WEC3.company2wec3Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec3Count = ",Company2WEC3.company2wec3Count)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'company2wec3Count': Company2WEC3.company2wec3Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC3/WEC3_description.txt', 'company2wec3Comment': '\nFlap that is beautiful'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'N': ['N', '', 'N', self.N], 'o': ['o', '', 'o', self.o], 'n': ['n', '', 'n', self.n], 'e': ['e', '', 'e', self.e]}
    return paramsDictionary