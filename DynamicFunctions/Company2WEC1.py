import numpy as np
from CoreFunctions.FixRFID import FixRFID

class Company2WEC1:
 company2wec1Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company2/WEC1/WEC1_description.txt"
 company2wec1Comment = """
The WEC is made of two different axles connected at one point,
and with concern about the angle
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECCompany2WEC1")
    self.angle = p1 # (--)
    self.length_of_the_axles = p2 # (m)
    Company2WEC1.company2wec1Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company2wec1Count = ",Company2WEC1.company2wec1Count)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'company2wec1Count': Company2WEC1.company2wec1Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company2/WEC1/WEC1_description.txt', 'company2wec1Comment': '\nThe WEC is made of two different axles connected at one point,\nand with concern about the angle'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['angle', '', '(--)', self.angle], 'p2': ['length_of_the_axles', '', '(m)', self.length_of_the_axles]}
    return paramsDictionary