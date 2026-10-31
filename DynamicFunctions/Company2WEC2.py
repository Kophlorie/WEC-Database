import numpy as np
from CoreFunctions.FixRFID import FixRFID

class Company2WEC2:
 company2wec2Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC2/WEC2_description.txt"
 company2wec2Comment = """
Flap that is beautiful
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2, p3):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECCompany2WEC2")
    self.bughf = p1 # (--)
    self.hun = p2 # (kg)
    self.should = p3 # (kk)
    Company2WEC2.company2wec2Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec2Count = ",Company2WEC2.company2wec2Count)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'company2wec2Count': Company2WEC2.company2wec2Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC2/WEC2_description.txt', 'company2wec2Comment': '\nFlap that is beautiful'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['bughf', '', '(--)', self.bughf], 'p2': ['hun', '', '(kg)', self.hun], 'p3': ['should', '', '(kk)', self.should]}
    return paramsDictionary