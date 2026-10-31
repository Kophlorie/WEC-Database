from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixPeople import FixPeople
from CoreFunctions.FixOrganisation import FixOrganisation
from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixDate import FixDate
from CoreFunctions.FixPeople import FixPeople
from CoreFunctions.FixOrganisation import FixOrganisation

class FixProject:

	fprCount = 0
	countryLine = 10
	
	def __init__(self, idproject = "", 
				 comment = "", start = FixDate("",""), 
				 endexpected = FixDate("",""), 
	             endactual  = FixDate("",""), budgetexpected = 0, 
				 budgetactual = 0, people = [FixPeople("")], 
				 organisations = [FixOrganisation(0,"","",[""])], 
				 wecnamestested = [""]):
		
		self.comment = comment
		self.start = start
		self.endExpected = endexpected
		self.endActual = endactual
		self.budgetExpected = budgetexpected
		self.budgetActual = budgetActual
		self.people = people
		self.organisations = organisations
		self.wecNamesTested = wecnamestested
		
		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/Projects/"+self.IDproject.ID+".txt"
		self.IDproject = self.checkProject(self.listFilePath)
		
		FixProject.fprCount += 1
		print(self.classAttached, "'s object created and fprCount = ",FixProject.fprCount)
	
	
	def checkProject(self, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		self.listFilePath = filePath
		idproject = FixRFID("", "FixProject", ["",""], "","","")
		return idproject
	
	def writeProject(self, filePath):
		
		return
		
	def splitFancy(self, text):
		if ":" in text:
			text = text.split(":")
		else: 
			if "=" in text:
				text = text.split("=")
			else:
				print("\nError using splitFancy, the element to split is not in the list")
		return text