import numpy as np
from CoreFunctions.FixRFID import FixRFID

class WeptosWeptosWEC:
 weptosweptoswecCount = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Weptos/WeptosWEC/WeptosWEC_description.txt"
 weptosweptoswecComment = """
weptos mother class
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECWeptosWeptosWEC")
    self.arm_length = p1 # (m)
    WeptosWeptosWEC.weptosweptoswecCount += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and weptosweptoswecCount = ",WeptosWeptosWEC.weptosweptoswecCount)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'weptosweptoswecCount': WeptosWeptosWEC.weptosweptoswecCount, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Weptos/WeptosWEC/WeptosWEC_description.txt', 'weptosweptoswecComment': '\nweptos mother class'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['arm_length', '', '(m)', self.arm_length]}
    return paramsDictionary