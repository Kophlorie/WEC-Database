from CoreFunctions.FixDate import FixDate

class FixRFID:
	frfidCount = 0
	
	def __init__(self, name = "", classattached = "", 
				 date = FixDate("",""), id = "", 
				 descriptionfilepath = "", listfilepath = ""):
	
		self.ID = id
		self.classAttached = classattached
		self.date = date
		self.name = name
		self.descriptionFilePath = descriptionfilepath
		self.listFilePath = listfilepath
		
		self.initialisation = 2
		self.checkRFID(self.classAttached)
		
		FixRFID.frfidCount += 1
	
	def checkRFID(self,classAttached):
		
		filePath = self.listPath(classAttached)+self.ID+".txt"
		
		if self.initialisation == 1:
			try:
				fh = open(filePath,"r")
				text_readlines = fh.readlines()
			except IOError:
				if "wec" in classAttached.lower():
					self.writeWEC(filePath)
				else:	
					print("List "+classAttached+" not in RFID...")
			else:
				fh.close()
				self.date.country = text_readlines[countryLine(self.classAttached)]
		else:	
			try:
				fh = open(filePath,"r")
				text_readlines = fh.readlines()
			except IOError:
				if "wec" in classAttached.lower():
					self.writeWEC(filePath)
				else:
					print("List "+classAttached+" not in RFID...")
			else:
				fh.close()
				self.date.country = text_readlines[countryLine(self.classAttached)]
		
		return
		
		
	def checkWEC(self, filePath):
		
		return
	def writeWEC(self, filePath):
	
		return
		
		
		
	def countryLine(self,classAttached):

		if "wec" in classAttached.lower():
			return 1
		else:
		
			print("List "+classAttached+" not in RFID...")
			return 0
						
	def listPath(self,classAttached):
		if "wec" in classAttached.lower():
			return "Database/List/WECs/"
		else:
			print("List "+classAttached+" not in RFID..")
			return "0"
			
	def __str__(self):
		print(self.ID)
		return "{0}".format(self.ID)