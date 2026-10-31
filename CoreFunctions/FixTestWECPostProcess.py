import numpy as np
import sys
from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixProject import FixProject
from CoreFunctions.FixCalibration import FixCalibration
from CoreFunctions.FixTestingEnvironment import FixTestingEnvironment

class FixTestWECPostProcess:

	ftwppCount = 0
	countryLine = 1 # to be updated
	
		
	def __init__(self, idtestwecpostprocess = "", testpath = ""):
	
		self.testPath = testpath
		self.wecsTested = []
		self.rawDataPath = ""
		self.rawDataTitles = []	
		
		self.project = initialisationProject(testPath)
		self.testEnvironment = initialisationTestEnvironment(testPath)
		self.calibration = initialisationCalibration(testPath)
		
		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/TestWECPostProcesses/"+idtestwecpostprocess+".txt"
		self.IDtestwecpostprocess = self.checkTestWECPostProcess(self, self.listFilePath) 
		
		FixTestWECPostProcess.ftwppCount += 1
		print(self.classAttached, "'s object created and ftwppCount = ",FixTestWECPostProcess.ftwppCount)
		
	def initialisationProject(self, testPath):
	
		idproject = ""#FixRFID("", "FixProject", ["",""], "","","")
		comment = ""
		start = FixDate(0,0,0,0,"")
		endexpected = FixDate(0,0,0,0,"")
		endactual  = FixDate(0,0,0,0,"")
		budgetexpected = 0
		budgetactual = 0
		people = [FixPeople("")]
		organisations = [FixOrganisation("","",[""])]
		wecnamestested = [""]
		
		project = FixProject(idproject, comment, start, endexpected, endactual, budgetexpected, budgetactual, people, organisations, wecnamestested)
		return project
		
	def initialisationTestEnvironment(self, testPath):
	
		idtestingenvironment = FixRFID("","FixTestingEnvironment",["",""],"","","")
		locationaddress = ""
		bathymetrypath = ""
		
		testEnvironment = FixTestingEnvironment(1, idtestingenvironment, locationaddress, bathymetrypath)
		return testEnvironment
		
	def initialisationCalibration(self, testPath):
	
		idcalibration = FixRFID("","FixCalibration",["",""],"","","")
		nomenclaturepath = ""
		
		calibration = FixCalibration(idcalibration,nomenclaturepath)
		return calibration
		
	def checkTestWECPostProcess(self, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		self.listFilePath = filePath
		idtestwecpostprocess = FixRFID("", "FixTestWECPostProcess",["",""],"","","")
		return idtestwecpostprocess	
	
	def writeTestWECPostProcess(self, filePath):
	
		return