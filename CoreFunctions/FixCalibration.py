import numpy as np
from CoreFunctions.FixRFID import FixRFID

class FixCalibration:

	fcCount = 0
	countryLine = 1 # to be updated
	
	def __init__(self, idcalibration = FixRFID("","FixCalibration",["",""],"","",""), 
				 nomenclaturepath = ""):
				 
		self.nomenclaturePath = nomenclatureCreation(nomenclaturepath)
		self.nomenclature = np.matrix([[0],[0]])

		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/Calibrations/"+idcalibration.ID+".txt"
		self.IDcalibration = self.checkCalibration(self, self.IDcalibration, idcalibration)
		
		FixCalibration.fcCount += 1
		print(self.classAttached, "'s object created and fcCount = ",FixCalibration.fcCount)
		
	def __init__(self, idcalibration = "", nomenclaturepath = ""):
				 
		self.nomenclaturePath = nomenclatureCreation(nomenclaturepath)
		self.nomenclature = np.matrix([[0],[0]])

		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/Calibrations/"+idcalibration+".txt"
		self.IDcalibration = self.checkCalibration(self, self.listFilePath)
		
		FixCalibration.fcCount += 1
		
	def nomenclatureCreation(nomenclaturepath):
		
		nomenclature = np.matrix([[0],[0]])
		
		return nomenclature
		
	def checkCalibration(self, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		self.listFilePath = filePath
		idcalibration = FixRFID("", "FixCalibration",["",""],"","","")
		return idcalibration
	def writeCalibration(self, filePath):
	
		return