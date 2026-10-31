import numpy as np
from CoreFunctions.FixRFID import FixRFID

class FixTestingEnvironment:
	
	fteCount = 0
	countryLine = 1 # to be updated
		
	def __init__(self, optionidOrFile = 0, idtestingenvironmentOrFile = "", locationaddress = "", bathymetrypath = ""):
	
		self.locationAddress = locationaddress
		self.bathymetryPath = bathymetrypath
		self.bathymetry = bathymetryCreation(bathymetrypath) # will not be written in the listFile
		
		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/Projects/"+idtestingenvironment+".txt"
		self.IDtestingenvironment = self.checkTestingEnvironment(self, self.listFilePath) 
		
		FixTestingEnvironment.fteCount += 1
		print(self.classAttached, "'s object created and fteCount = ",FixTestingEnvironment.fteCount)
	
		
	def bathymetryCreation(self, bathymetrypath):
		# function to be coded...
		bathmat = np.matrix([[0],[0]])	
		return bathmat
		
	def checkTestingEnvironment(self, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		self.listFilePath = filePath
		idtestingenvironment = FixRFID("","FixTestingEnvironment",["",""],"","","")
		return idtestingenvironment
	
	def writeTestingEnvironment(self, filePath):
	
		return