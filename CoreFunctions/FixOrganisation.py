import sys
from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixDate import FixDate

class FixOrganisation:
	foCount = 0
	countryLine = 7 # because starting from 0 otherwise it would be 8 if starting from 1 
	# but there is an issue because the comments line may take more than its line...
		
	def __init__(self, optionidOrFile = 0, idorganisationOrFile = "", 
				 type = "", name_previousnames = [""]):
		
		self.comments = ""
		self.type = type
		self.name_PreviousNames = name_previousnames
		self.classAttached = self.__class__.__name__
		self.date = FixDate("","")
		self.name = ""
		
		if optionidOrFile == 0:
			# Default initialisation
			self.descriptionFilePath = ""
			self.listFilePath = "Database/Lists/Organisations/"+idorganisationOrFile+".txt"
			self.IDorganisation = FixRFID("", "FixOrganisation", ["",""], "","","")
		else:
			if optionidOrFile == 1:
			# Initialisation based on the list
				self.descriptionFilePath = ""
				self.listFilePath = "Database/Lists/Organisations/"+idorganisationOrFile+".txt"
				self.checkOk = self.readOrganisationList(self.listFilePath, idorganisationOrFile)
			else:
				# Initialisation based on the descrition file
				if optionidOrFile == 2:
					self.descriptionFilePath = idorganisationOrFile
					print(self.descriptionFilePath)
					self.listFilePath = "Database/Lists/Organisations/"
					self.checkOk = self.readOrganisationDescription(idorganisationOrFile)
					self.checkOk = self.checkOrganisation(1, self.listFilePath)
					print(self.checkOk)
					print(self.descriptionFilePath)
					if "0" in self.checkOk:
						self.writeOrganisationList(self.listFilePath)
		
		objectDictionary = {}
		objectDictionary['descriptionFilePath'] = self.descriptionFilePath
		objectDictionary['listFilePath'] = self.listFilePath
		objectDictionary['comments'] = self.comments
		objectDictionary['type'] = self.type
		objectDictionary['name'] = self.name
		objectDictionary['name_PreviousNames'] = self.name_PreviousNames
		objectDictionary['IDorganisation'] = self.IDorganisation.ID
		objectDictionary['Country_time'] = self.date.country
		
		self.objectDictionary = objectDictionary
		
		FixOrganisation.foCount += 1
		print(self.classAttached, "'s object created and foCount = ",FixOrganisation.foCount)
	
	def readOrganisationDescription(self, descriptionFilePath):
		checkedOk = "1"
		try:
			fh = open(descriptionFilePath,'r')
			text_readlines = fh.read().split("==")
			if len(text_readlines) != 3:
				print("\nError in FixOrganisation in readOrganisationDescription:\n"+
					  "The file \""+descriptionFilePath+"\" should be split in three section as follows:\n"+
					  "The number of sections is of: "+str(len(text_readlines))+" whereas it should be 3 such that:\n"+
					  "OrganisationObject\n==\nUser comments\n==\nParameters as follows:\n"+
					  "\nIDorganisation: user entering the organisation's ID structured as CompanyNameYearMonthDayHourMinute when the company has been entered in the database.\n"+
					  "!!!!!!!! Be carefull at the date: provide 2 digits expl: day 5th hour 2am -> 0502"+
					  "\nCountry_time: country in which the date of ID has ben entered or refered"+
					  "\nType: user entering the organisation's type (company, institute, non-profit organisation, etc.)"+
					  "\nName_PreviousNames: user entering the organisation's name with \", \" followed by the previous names the organisation might have before.\n"
					  )
				print("\ntext_readlines is:\n"+str(text_readlines))
				sys.exit()
		except IOError:
			print("\nError in FixOrganisation in readOrganisation:\nThe file \""+descriptionFilePath+"\" is not found.")
			checkedOk = "0"
		else:
			fh.close()
			self.comments = text_readlines[1]
			#s = "=="
			#print("text_readlines = "+s.join(text_readlines))
			params = text_readlines[2].split("\n") # self.splitFancy(
			s = "\n"
			#print("\nThe vec params is:"+s.join(params))
			while "" in params:
				params.remove("")
			if len(params) != 4:
				print("\nError in FixOrganisation in readOrganisationDescription:\n"+
					  "The file \""+descriptionFilePath+"\" should have the following parameters:\n"+
					  "The number of params is of: "+str(len(params))+" whereas it should be 4 such that:\n"+
					  "\nIDorganisation: user entering the organisation's ID structured as CompanyNameYearMonthDayHourMinute when the company has been entered in the database.\n"+
					  "!!!!!!!! Be carefull at the date: provide 2 digits expl: day 5th hour 2am -> 0502"+
					  "\nCountry_time: country in which the date of ID has ben entered or refered"+
					  "\nType: user entering the organisation's type (company, institute, non-profit organisation, etc.)"+
					  "\nName_PreviousNames: user entering the organisation's name with \", \" followed by the previous names the organisation might have before.\n"
					  )
				print("\nparams is:\n"+str(params))
				sys.exit()
			
			id = self.splitFancy(params[0])[1].strip()
			date = FixDate(id[-12:], self.splitFancy(params[1])[1].strip()) # date, country_time
			self.date = date
			#print(date)
			self.name = id[0:-12]
			#print("name = "+name)
			#print("date = "+id[-12:-1])
			id = FixRFID(self.name, self.classAttached, date, id, descriptionFilePath, self.listFilePath)
			self.IDorganisation = id
			self.listFilePath = self.listFilePath+id.ID+".txt"
			
			self.type = self.splitFancy(params[2])[1].strip()
			names = self.splitFancy(params[3])[1].strip()
			#print(names)
			if "," in names:
				names = names.split(",")
				j = -1
				for element in names:
					j += 1
					names[j] = element.strip()
				self.name_PreviousNames = names
			else:
				self.name_PreviousNames = [names.strip()]
			#print(self.name_PreviousNames)
			#print(param[2000000000]) # to block to test the function
		return checkedOk
		
	def readOrganisationList(self, listFilePath, id):
		checkedOk = "1"	
		try:
			fh = open(listFilePath, 'r')
			text_readlines = fh.readlines()
		except IOError:
			print("\nError in FixOrganisation in readOrganisationList:\nThe file \""+listFilePath+"\" is not found.")
			#print("I need to write here the function to create the considered file in the list..")
			checkedOk = "0"
		else:
			fh.close()			
			self.descriptionFilePath = self.splitFancy(text_readlines[1])[1].strip()
			s = "\n"
			self.comments = s.join(text_readlines[2:-5]).split("\"\"\"")[1].strip() 
			# Be carefull when doing the checking: the \n are taken away
			#print([self.comments])
			self.type = self.splitFancy(text_readlines[-5])[1].strip()
			self.name = self.splitFancy(text_readlines[-4])[1].strip()
			if self.name != id[0:-12]:
				print("\nError in FixOrganisation in readOrganisationList: self.name ("+self.name+")!= ("+id[0:-12]+") id[0:-12]...")
				sys.exit()
			names = self.splitFancy(text_readlines[-3])[1]
			if "," in names:
				names = names.split(",")
				j = -1
				for element in names:
					j += 1
					names[j] = element.strip()
				self.name_PreviousNames = names
			else:
				self.name_PreviousNames = [names.strip()]
			self.date = FixDate(id[-12:], self.splitFancy(text_readlines[-1])[1].strip()) # date, country_time
			 
			
		#print(name[20000]) # hilight an error to stop the program because function not finished

		self.IDorganisation = FixRFID(self.name, self.classAttached, self.date, id, self.descriptionFilePath, listFilePath)		
		return checkedOk 
		
	def checkOrganisation(self, option, filePath):
		# should not be filePath in the RFID constructor... !!
		# -> to be updated
		#self.listFilePath = filePath
		checkedOk = "0"
		descriptionFilePath = self.descriptionFilePath
		listFilePath = self.listFilePath
		comments = self.comments
		type = self.type
		name = self.name
		name_PreviousNames = self.name_PreviousNames
		IDorganisation = self.IDorganisation
		date = self.date
		Country_time = date.country
		
		if option == 1:
			checkedOk = self.readOrganisationList(filePath, IDorganisation.ID)
		else:
			checkedOk = readOrganisationDescription(filePath)
		if checkedOk == "1":	
			if descriptionFilePath == self.descriptionFilePath:
				checkedOk = "1"
				if listFilePath == self.listFilePath:
					checkedOk = "1"
					if comments == self.comments:
						checkedOk = "1"
						if type == self.type:
							checkedOk = "1"
							if name == self.name:
								checkedOk = "1"
								if name_PreviousNames == self.name_PreviousNames:
									checkedOk = "1"
									if IDorganisation == self.IDorganisation:
										checkedOk = "1"
										if Country_time == self.date.country:
											checkedOk = "1"
										else:
											checkedOk = "0 Country_time != self.date.country"
									else:
										checkedOk = "0 IDorganisation != self.IDorganisation"
								else:
									checkedOk = "0 name_PreviousNames != self.name_PreviousNames"
							else:
								checkedOk = "0 name != self.name"
						else:
							checkedOk = "0 type != self.type"
					else:
						checkedOk = "0 comments != self.comments"
				else:
					checkedOk = "0 listFilePath != self.listFilePath"
			else:
				checkedOk = "0 descriptionFilePath != self.descriptionFilePath"
		
		self.descriptionFilePath = descriptionFilePath
		self.listFilePath = listFilePath
		self.comments = comments
		self.type = type
		self.name = name
		self.name_PreviousNames = name_PreviousNames
		self.IDorganisation = IDorganisation
		self.date = date
		return checkedOk
	
	def writeOrganisationList(self, listFilePath):
		names = self.name_PreviousNames
		id = self.IDorganisation.ID
		name = id[0:-12]
		if len(names) != 1:
			text = ""
			for element in names:
				text += element+", "
			names = text[0:-2]
		else:
			names = names[0]
		
		fh = open(listFilePath,'w')
			
		fh.write("classAttached = "+self.classAttached+" in CoreFunctions")
		fh.write("\ndescriptionFilePath = "+self.descriptionFilePath)
		fh.write("\ncomments = \"\"\""+self.comments+"\"\"\"")
		fh.write("\ntype = "+self.type)
		fh.write("\nname = "+name)
		fh.write("\nname_PreviousNames = "+names)
		fh.write("\nIDorganisation: {0}".format(self.IDorganisation))
		fh.write("\nCountry_time = "+self.date.country+"\n")
		
		fh.close()
		return
		
	def createObjectMainRun(self):
		s = ""
		names = self.name_PreviousNames
		id = self.IDorganisation.ID
		name = id[0:-12]
		text = "["
		for element in names:
			text += "\""+element+"\", "
		names = text[0:-2]+"]"
		
		text = s.join(["\n		#"+name+"_description",
			   "\n		self."+name+" = FixOrganisation(1, \""+id+"\", \""+
			   self.type+"\", "+names+")\n"])
		#print(text)
		#print(name[2000]) # to stop the run and test the function
		return text
	
	def __str__(self):
		names = self.name_PreviousNames
		id = self.IDorganisation.ID
		name = id[0:-12]
		if len(names) != 1:
			text = "["
			for element in names:
				text += "\""+element+"\", "
			names = text[0:-2]+"]"
		else:
			name = "[\""+names[0]+"\"]"
		
		print("classAttached = "+self.classAttached+" in CoreFunctions")
		print("foCount = "+str(FixOrganisation.foCount))
		print("descriptionFilePath = "+self.descriptionFilePath)
		print("listFilePath = "+self.listFilePath)
		print("comments = "+self.comments)
		print("type = "+self.type)
		print("name = "+name)
		print("name_PreviousNames = "+str(names))
		print("IDorganisation:{0}".format(self.IDorganisation))
		return "Country_time = {0}".format(self.date.country)
	
	def splitFancy(self, text):
		if ":" in text:
			text = text.split(":")
		else: 
			if "=" in text:
				text = text.split("=")
			else:
				print("\nError using splitFancy, the element to split is not in the list")
		return text