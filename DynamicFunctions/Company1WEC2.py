import numpy as np
from CoreFunctions.FixRFID import FixRFID

class Company1WEC2:
 company1wec2Count = 0
 nomenclatureFilePath = " "
 functionFilesPath = " "
 descriptionFilePath = "Database/Company1/WEC2/WEC2_description.txt"
 company1wec2Comment = """
The WEC is made of a wire and some plates moving back and forth
"""
 def __init__(self, name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time, idwec, p1, p2, p3):
    self.name = name
    self.comments = comments
    self.descriptionPath = descriptionpath
    self.nomenclatureFilePath = nomenclaturefilepath
    self.functionFilesPath = functionfilespath
    self.country_time = country_time
    self.IDwec = FixRFID(idwec, "WECCompany1WEC2")
    self.nb_of_plates = p1 # (--)
    self.overall_length_of_the_wire = p2 # (m)
    self.plate_shape = p3 # (--)
    Company1WEC2.company1wec2Count += 1
    self.classAttached = self.__class__.__name__
    self.listFilePath = "Database/Lists/WECs/"+self.IDwec.ID+".txt"
    print(self.classAttached, "'s object created and company1wec2Count = ",Company1WEC2.company1wec2Count)

 def getWECMotherClassParams(self):
    classParamsDictionary = {'company1wec2Count': Company1WEC2.company1wec2Count, 'nomenclatureFilePath': ' ', 'functionFilesPath': ' ', 'descriptionFilePath': 'Database/Company1/WEC2/WEC2_description.txt', 'company1wec2Comment': '\nThe WEC is made of a wire and some plates moving back and forth'}
    return classParamsDictionary

 def getWECMotherObjectParams(self):
    paramsDictionary = {'name': self.name, 'comments': self.comments, 'descriptionPath': self.descriptionPath, 'nomenclatureFilePath': self.nomenclatureFilePath, 'functionFilesPath': self.functionFilesPath, 'country_time': self.country_time, 'p1': ['nb_of_plates', '', '(--)', self.nb_of_plates], 'p2': ['overall_length_of_the_wire', '', '(m)', self.overall_length_of_the_wire], 'p3': ['plate_shape', '', '(--)', self.plate_shape]}
    return paramsDictionary