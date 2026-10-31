from CoreFunctions.FixRFID import FixRFID

class FixPeople:
	fpeCount = 0
	countryLine = 6
	
	def __init__(self, idpeople = "",
			     firstname = "", familyname = "",
			     workingaddress = "", email = "", tel = ""):

		
		self.firstName = firstname
		self.familyName = familyname
		self.workingAddress = workingaddress
		self.email = email
		self.telephone = telephone
		
		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/People/"+idpeople.ID+".txt"
		self.IDpeople = self.checkPeople(self.listFilePath, idpeople)
		
		FixPeople.fpeCount += 1
		
	def __init__(self, idpeople = ""):

		
		self.firstName = ""
		self.familyName = ""
		self.workingAddress = ""
		self.email = ""
		self.telephone = ""
		
		self.classAttached = self.__class__.__name__
		self.listFilePath = "Database/Lists/People/"+idpeople+".txt"
		self.IDpeople = self.checkPeople(self.listFilePath) 
		
		FixPeople.fpeCount += 1
		
	def checkPeople(self, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		self.listFilePath = filePath
		idpeople = FixRFID("", "FixPeople",["",""],"","","")
		return idpeople
		
	def writePeople(self, filePath):
	
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