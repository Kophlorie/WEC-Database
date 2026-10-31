import sys
from CoreFunctions.CreationFoldersPath import CreationFoldersPath
from CoreFunctions.CreationWEC import CreationWEC
from CoreFunctions.CreationWECChild import CreationWECChild

from CoreFunctions.CreationFoldersPath import CreationFoldersPath 
from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixPeople import FixPeople
from CoreFunctions.FixOrganisation import FixOrganisation
from CoreFunctions.FixProject import FixProject
from CoreFunctions.FixDate import FixDate
from CoreFunctions.FixCalibration import FixCalibration
from CoreFunctions.FixTestingEnvironment import FixTestingEnvironment
from CoreFunctions.FixTestWECPostProcess import FixTestWECPostProcess

class CreationMainCreation:

	cmcCount = 0
	mainCreationPath = "DynamicFunctions/MainCreation.py"
	
	def __init__(self, previous_folderspath, new_folderspath):
		
		self.firstWrite = 0
		
		self.databaseDictionary = {}
		self.organisationDictionary = {}
		self.wecMotherDictionary = {}
		self.wecChildrenDictionary = {}
		
		self.creationFoldersPath = CreationFoldersPath()
		#print(str(self.creationFoldersPath.updated))
		self.creationFoldersPath.checkFoldersPath(previous_folderspath, new_folderspath)
		#print(str(self.creationFoldersPath.updated))
		#print(self)
		
		if 1:
			self.writeBaseMainCreationText()
			self.firstWrite = 1
		
		
		self.text_readlines = self.readMainCreation(CreationMainCreation.mainCreationPath)
	
		
		self.updateClassesAndObjects(self.creationFoldersPath.new_FoldersPath.folders,self.creationFoldersPath.new_FoldersPath.folders_Type, self.creationFoldersPath.new_FoldersPath.folders_TypePath)
		
		CreationMainCreation.cmcCount += 1			
		return
		
	def readMainCreation(self, mainCreationPath):
		try:
			fh = open(CreationMainCreation.mainCreationPath,"r")
		except IOError:
			print("\nError in CreationMainCreation in readMainCreation:\ncan\'t find file\""+CreationMainCreation.mainCreationPath+"\"...")
			self.writeBaseMainCreationText()
			self.firstWrite = 1
			fh = open(CreationMainCreation.mainCreationPath,"r")
			
		text_readlines = fh.readlines()
		fh.close()
		
		if text_readlines == []:
			print(text_readlines)
			text_readlines = self.writeBaseMainCreationText()
		
		return text_readlines
	
	def updateMainCreationModules(self, creationWEC, text_readlines):
		s = "."
		text ="from "+s.join(creationWEC.writtingFilePath.split("/")[0:-1])+"."+creationWEC.className+" import "+creationWEC.className+"\n"
		if text not in text_readlines:
			text_readlines.insert(2,text)
			s = ""
			fh = open(CreationMainCreation.mainCreationPath,"w")
			fh.write(s.join(text_readlines))
			fh.close()
		return text_readlines
		
	def updateClassesAndObjects(self, folders, folders_type, folders_typepath):	
		""" The are
		first an initialisation
		second an initialisation loop that implements the first WEC mother 
		and the first company
		third the "big" loop starts implement all wec children and
		associated objects + if the object is not from a WEC Child then it is created in elseObject
		the objects are saved in the children classes saved in the mother 
		classes saved in the organisations
		"""
		# Initialisation
		
		text_readlines = self.text_readlines
		s = ""
		print_str = s.join(text_readlines).split("#Object definition")[1]
		objectText = print_str.split("#Rest of the function")[0]
		print_str = print_str.split("def __str__(self):")[1].split("return")[0].split("#")
		print_str = print_str[1:]
		objectText = objectText.split("#")
		#objectTextEnd = objectText[0]
		#print(objectText)
		#print(print_str)
		for objecti in range(1,len(objectText)):
			objectText[objecti] = "\n		#"+objectText[objecti].strip("\n\t\t")+"\n"
			print_str[objecti-1] = "\n		#"+print_str[objecti-1].strip("\n\t\t")+"\n"
		objectText = objectText[1:]
		objectText_base = objectText[:]
		#print(objectText)
		s = "/"
		i = -1
		objecti = -1
		
		#databaseDictionary = {}
		organisationDictionary = {}
		#organisationDictionaryALL = {}
		wecMotherDictionary = {}
		wecMotherDictionaryALL = {}
		wecChildrenDictionary = {}
		wecChildrenDictionaryALL = {}
		wecChildrenObjectsDictionary = {}
		wecChildrenObjectsDictionaryALL = {}
		first_class = 1
		previousClassName = ""
		organisation = ""
		
		# First loop to catch the first WEC class particularly ;
		# It also implement the first organisation object
		while first_class != 0:
			i += 1
			element = folders_type[i].lower()
			print(folders[i])
			if (("wec" in element) & ("child" not in element)):
				if ("object" not in element):
					creationWEC = CreationWEC(folders[i])
					previousClassName = creationWEC.className
					print("WECClass:",creationWEC.className+",\nchecked: "+str(creationWEC.checkOk)+"\n")
					first_class = first_class - 1
					if "0" in creationWEC.checkOk:
						creationWEC.writeClass()
					#if (creationWEC.firstWrite == 1) | (self.firstWrite	== 1):
					text_readlines = self.updateMainCreationModules(creationWEC, text_readlines)
					#print(creationWEC)	
			else:
				# to catch the first object that is the company of the first WEC
				elementObjectPath = folders_typepath[i].split(" ") # split(" ") should not be needed! see message below
				if len(elementObjectPath) > 1:
					print("Error in CreationMainCreation at the beginning of updateClassesAndObjects:\n"+
						  "There might be an issue with the path:\n"+ folders_typepath[i]+
						  "\nBecause there should not be more than on object...")
					sys.exit()
				
				if ("object" in element.lower()):
					
					objecti += 1
					print("Else object: "+element)		
					#print("folders_typepath: "+elementObjectPath)
					
					if ("organisation" in element) | ("company" in element):	
						# First initialisation of the first organisation
						organisation = FixOrganisation(2, elementObjectPath[0], "", [""])
						text = organisation.createObjectMainRun()
						vec = self.updateMainCreationObjects(print_str, text, elementObjectPath[0], objectText, objecti)
						objectText = vec[0]
						print_str = vec[1]
						
		#print(previousClassName)
		if organisation == "":
			print("Error in CreationMainCreation in updateClassesAndObjects:\n"+
				  "The first organisation attached to: "+creationWEC.className+
				  "\nhas not been created.")
			sys.exit()
		
		# Loop for all the element after the above initialisation
		for element in folders_type[i+1:]:
			i += 1
			element = element.lower()
			print("folder = "+folders[i])
			#print("folder type = "+element)
			#print("folder type path of description file = "+folders_typepath[i])
			if (("wec" in element) & ("child" not in element)):
				if ("object" not in element):
					temp = creationWEC.descriptionFilePath.split(s)[0:-1]
					if  (len(temp) != len(folders[i].split(s))) & (s.join(temp) in folders[i]):
						print("\nError in CreationMainCreation in updateClassesAndObjects in:\n"+folders_typepath[i]+
							  "\nand the previous WEC class path was:\n"+s.join(creationWEC.descriptionFilePath.split(s)[0:-1])+
							  "\nthe WEC class should not be created within an already existing WEC class.\n"+
							  "The header of the file is: "+element+
							  "\nIt is likely that the word \"Child\" is missing in the header of the _description.txt file.")
						sys.exit()
					elif s.join(organisation.descriptionFilePath.split(s)[0:-1]) in folders[i]:
						
						# Update of the previous class children
						#print("first_class == "+str(first_class))
						if first_class == 1:
							first_class = 0
						else:
							wecMotherDictionary[previousClassName] = wecChildrenDictionary
							wecMotherDictionaryALL[previousClassName] = { 'WECChildren classes' : wecChildrenDictionary, 'WEC class params' : creationWEC.classParamsDictionary}
						#print(wecMotherDictionary)
						#print(previousClassName)
						
						# Now creating the new class 
						#print("first_class == "+str(first_class))
						creationWEC = CreationWEC(folders[i])
						newClassName = creationWEC.className
						print("WECClass:",creationWEC.className+",\nchecked: "+str(creationWEC.checkOk)+"\n")
						
						# Updating the previous name by the new class'
						previousClassName = newClassName
						#print(previousClassName)
						wecChildrenDictionary = {}
						
						if "0" in creationWEC.checkOk:
							creationWEC.writeClass()
						#if (creationWEC.firstWrite == 1) | (self.firstWrite	== 1):
						text_readlines = self.updateMainCreationModules(creationWEC, text_readlines)
						#print(creationWEC)	
					else:
						print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
							  "The WEC class attached to:\n"+
							  str(s.join(organisation.descriptionFilePath.split(s)[0:-1]))+
							  ",\ncannot be created\nin relation to the previous organisation object attached to :\n"+
							  s.join(organisation.descriptionFilePath.split(s)[0:-1])+
							  " does not seem to exist;\nThe current folders is: "+folders[i]+"\nYou may check that inside this (or above) folder,\n"+
							  "the proper description file exist with a title following this format:\n"+
							  "organisationname_description.txt"+
							  "\nIn the first line of the organisation should be written: OrganisationObject"+
							  "Otherwise it will not be detected by the program")
						sys.exit()
				else:
					print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
						  "The object: "+element+									  
						  "\nThere cannot be any object out from a WEC class,\n"+
						  "only from WECChild classes.")
					sys.exit()
					
			else: 
				if (("wec" in element) & ("child" in element.lower())) & ("object" not in element):
					
					if s.join(creationWEC.descriptionFilePath.split(s)[0:-1]) in folders[i]:
						
						creationWECChild = CreationWECChild(folders[i])
						print("WECChild:",creationWECChild.className+",\nchecked: "+str(creationWECChild.checkOk)+"\n")
						wecChildrenDictionary[creationWECChild.className] = {'classParams':creationWECChild.classParamsDictionary, 'motherParams': creationWECChild.paramsMotherDictionary, 'params': creationWECChild.paramsDictionary}
						wecChildrenDictionaryALL[creationWECChild.className] = {'classParams':creationWECChild.classParamsDictionary, 'motherParams': creationWECChild.paramsMotherDictionary, 'params': creationWECChild.paramsDictionary}
						wecChildrenObjectsDictionary = {}
						if "0" in creationWECChild.checkOk:
							creationWECChild.writeClass()
						#if (creationWEC.firstWrite == 1) | (self.firstWrite	== 1):
						text_readlines = self.updateMainCreationModules(creationWECChild, text_readlines)
						#print(creationWECChild)
					else:
						print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
							  "The WECChild class attached to:\n"+
							  str(s.join(creationWEC.descriptionFilePath.split(s)[0:-1]))+
							  ",\ncannot be created\nin relation to the previous WEC class attached to :\n"+
							  s.join(creationWEC.descriptionFilePath.split(s)[0:-1])+
							  " does not seem to exist;\nThe current folders is: "+folders[i]+"\nYou may check that inside this (or above) folder,\n"+
							  "the proper description file exist with a title following this format:\n"+
							  "wecclassname_description.txt"+
							  "\nIn the first line of the organisation should be written: WECClass"+
							  "Otherwise it will not be detected by the program")
						sys.exit()
				else:
					if ("object" in element.lower()):
						
						objectPath = folders_typepath[i].split(" ")
						objectElementVec = element.split(" ") #folders_type[i+1]
						j = -1
						for elementObjectPath in objectPath:
							j += 1
							objectElement = objectElementVec[j] # Related to the type only from folders_type[i+1]
							#print("folder type = "+objectElement)
							#print("folder type path of description file = "+elementObjectPath)
							
							if (objectElement.lower() != "description_absent") & ("object" not in objectElement.lower()):
								print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
									  "The object: "+str(objectElement)+									  
									  "\nThere is an issue in the split of \n"+str(objectElementVec)+
									  "\neach element should be written all attached\n"+
									  "so the pb is in one of the attached description files (see just object object type elements):\n")
								print(objectPath)
								sys.exit()
									  
							if (("wec" in objectElement.lower()) & ("child" in objectElement.lower())):
								if s.join(creationWECChild.descriptionFilePath.split(s)[0:-1]) in folders[i]:
										text = creationWECChild.createObjectMainRun(elementObjectPath)
										object_name = elementObjectPath.split(s)[-1].split(".")[0]
										print("WECChildObject:",object_name)
										wecChildrenObjectsDictionary[object_name] = creationWECChild.objectDictionary
										wecChildrenObjectsDictionaryALL[object_name] = creationWECChild.objectDictionary
										objecti += 1
										#print(element)							
										vec = self.updateMainCreationObjects(print_str, text, elementObjectPath, objectText, objecti)
										objectText = vec[0]
										print_str = vec[1]
								else:
									print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
										  "The object: "+objectElement+"attached to:\n"+
										  str(s.join(creationWECChild.descriptionFilePath.split("/")[0:-1]))+
										  ",\ncannot be created\nin relation to the previous WECChild class attached to :\n"+s.join(creationWECChild.descriptionFilePath.split("/")[0:-1])+
										  " does not seem to exist;\nThe current folders is: "+folders[i]+"\nYou may check that inside this (or above) folder,\n"+
										  "the proper description file exist with a title following this format:\n"+
										  "either for the object such as: wechildobjectname_description.txt\n"+
										  "or for the WEC mother or WEC child class such as: wecclassname_description.txt"+
										  "\nIn the first line of the organisation should be written: WECChild"+
										  "Otherwise it will not be detected by the program")
									sys.exit()
							else:
								
								vec = self.elseObjects(wecChildrenDictionary, wecChildrenDictionaryALL,
												  previousClassName, first_class,
												  wecMotherDictionary, wecMotherDictionaryALL,
												  organisationDictionary, #organisationDictionaryALL, 
												  objectText, print_str, text_readlines, objecti, 
												  i, folders, objectElement, elementObjectPath,
												  organisation,creationWEC)
								wecChildrenDictionary = vec[0]
								#wecChildrenDictionaryALL = vec[1]
								first_class = vec[3]
								wecMotherDictionary = vec[2+2]
								wecMotherDictionaryALL = vec[2+3]
								organisationDictionary = vec[2+4]
								objectText = vec[2+4+1] # 1 because you start from 0
								print_str = vec[2+4+2]
								objecti = vec[2+4+4]
								organisation = vec[-2]						
					elif ("description_absent" in element.lower()):	
						print("\nError in CreationMainCreation in updateClassesAndObjects:\n"+
							  "The object or class: "+objectElement+"attached to:\n"+
							  folders_typepath[i]+
							  "\nIn the first line of the organisation should be written\n"+
							  "WEC or WEChild or the fixed class from which the element belongs to."+
							  "\nIf it is an object and not a class, then the word \"object\" must appear,"+
							  "\notherwise it will not be detected by the program")
						sys.exit()
		if previousClassName not in wecMotherDictionary: #.has_key(key)
			wecMotherDictionary[previousClassName] = wecChildrenDictionary
			wecMotherDictionaryALL[previousClassName] = { 'WECChildren classes' : wecChildrenDictionary, 'WEC class params' : creationWEC.classParamsDictionary}
		organisationDictionary[organisation.name] = {'WECs':wecMotherDictionary, 'organisationInfo': organisation.objectDictionary}
		#print("organisationDictionary = \n"+str(organisationDictionary))
		wecMotherDictionary = {}	
		wecChildrenDictionary = {}
		
		#print(objectText)
		#print(objectText_base)
		#creationWECChild.test()
		#print("wecChildrenDictionary: "+str(wecChildrenDictionary))
		#print("wecMotherDictionary: "+str(wecMotherDictionary))
		
		#self.databaseDictionary = databaseDictionary
		self.organisationDictionary = organisationDictionary
		#self.organisationDictionaryALL = organisationDictionary
		self.wecMotherDictionary = wecMotherDictionary
		self.wecMotherDictionaryALL = wecMotherDictionaryALL
		self.wecChildrenDictionary = wecChildrenDictionary
		self.wecChildrenDictionaryALL = wecChildrenDictionaryALL
		self.wecChildrenObjectsDictionary = wecChildrenObjectsDictionary
		self.wecChildrenObjectsDictionaryALL = wecChildrenObjectsDictionaryALL
		if objectText != objectText_base:
			text_readlines = self.writeMainCreationObjects(print_str, objectText, text_readlines)
		self.text_readlines = text_readlines
		
		#text_readlines = self.writeMainCreationObjects(print_str, objectText, text_readlines)
		print("\nNumber of objects in the program: "+str(objecti+1)+" vs "+str(len(objectText))+"\n")
		return
		
	
	def elseObjects(self, wecChildrenDictionary, wecChildrenDictionaryALL,
				    previousClassName, first_class,
					wecMotherDictionary, wecMotherDictionaryALL,
					organisationDictionary, #organisationDictionaryALL, 
					objectText, print_str, text_readlines, objecti, 
					i, folders, folders_type_element, folders_typepath_elementObjectPath,
					organisation, creationWEC):
		'''elseObjects is used to handle every classes that are not a WEC class.
		This include organisation, FixTestWECPostProcess, etc...
		'''
		element = folders_type_element
		elementObjectPath = folders_typepath_elementObjectPath
		
		
		print("Else object: "+element)
		#print(organisation)
		#print(creationWEC)
		#print("folders_typepath: "+elementObjectPath)
		
		if ("organisation" in element) | ("company" in element):
			objecti += 1
			# The previous organisation get the directionary of wecs and reinitialise it
			s = "/"
			if s.join(organisation.descriptionFilePath.split(s)[0:-1]) in s.join(creationWEC.descriptionFilePath.split(s)[0:-1]):
				#PS: if you wouldn't have a mother there shouldn't be any children
				#so you just check over the mother class that the organisation path
				#is within the wec mother class.
				if wecChildrenDictionary == {}:
					wecChildrenDictionary['none']={
					'classParams': creationWEC.classParamsDictionary,
					'motherParams': creationWEC.paramsDictionaryMotherBase,
					'params': creationWEC.paramsDictionary}
				wecMotherDictionary[previousClassName] = wecChildrenDictionary
				wecMotherDictionaryALL[previousClassName] = { 'WECChildren classes' : wecChildrenDictionary, 'WEC class params' : creationWEC.classParamsDictionary}
			
			organisationDictionary[organisation.name] = {'WECs':wecMotherDictionary, 'organisationInfo': organisation.objectDictionary}
			#if 	organisation.name.lower() == "crestwing":
			#print(wecMotherDictionary)
			#print(wecMotherDictionaryALL)
			#print(organisationDictionary)
#				sys.exit()
			
			wecMotherDictionary = {}
			wecChildrenDictionary = {}
			first_class = 1
			#print("organisationDictionary = \n"+str(organisationDictionary))
			
			# Defining the next organisation 
			organisation = FixOrganisation(2, elementObjectPath, "", [""])
			text = organisation.createObjectMainRun()	
			print(organisation.name)
			print(organisation.descriptionFilePath)
			
			# Later should get out from the if in a way or another...
			vec = self.updateMainCreationObjects(print_str, text, elementObjectPath, objectText, objecti)
			objectText = vec[0]
			print_str = vec[1]
		else:
			if ("testenvironment" in element):
				print("The rest of the function:\nelseObjects in CreationMainCreation\n"+
					  "including for TestEnvironmentsObjects\n"+
					  "must be implemented for all fixed classes objects\n"+
					  "(probably but people and RFID)")
			else:
				print("The rest of the function:\nelseObjects in CreationMainCreation\n"+
					  "must be implemented for all fixed classes objects\n"+
					  "(probably but people and RFID)")
		
		
		
		vec = [wecChildrenDictionary, wecChildrenDictionaryALL,
			   previousClassName, first_class,
			   wecMotherDictionary, wecMotherDictionaryALL,
			   organisationDictionary, #organisationDictionaryALL, 
			   objectText, print_str, text_readlines, objecti, 
			   i, folders, element, elementObjectPath,
			   organisation,creationWEC]
		return vec 
		
	def updateMainCreationObjects(self, print_str, text, objectPath, objectText, objecti):
		#print([print_str])
		object_name = text.split("		#")[1].split("_description")[0]+"_description"
		print_text = "\n		#"+object_name+"\n		print(self."+object_name.lower()+")\n"
		#print(print_text)
		#print(objectText)
		#print(len(objectText))
		#print(objecti)
		
		if (objecti < len(objectText)): # & (objectText != [])
		# PS: the < instead of <= is because of the indexing 
		# indeed it starts with 0 whereas length start with 1
		
			#print("if (objecti < len(objectText)):")
			if (object_name not in objectText[objecti]): # (objectPath not in objectText[objecti]) |
				"""
				print("# the code assumes that the object just does not exist in the code")			
				print("objecti = "+str(objecti))
				print("object_name = ")
				print([object_name])
				print("objectText[objecti] = ")
				print([objectText[objecti]])
				"""
				objectText.insert(objecti,text)
				print_str.insert(objecti, print_text)
			else:
				#print([text])
				#print([objectText[objecti]])
				
				if (text != objectText[objecti]):
					#print("if (text != objectText[objecti]):")
					#print("object "+str(objecti)+" updated")
					objectText[objecti] = text
					print_str[objecti] = print_text
		else:
			#print("the else of if (objecti < len(objectText)):")
			objectText.insert(objecti,text)
			print_str.insert(objecti, print_text)
		
		#print(objectText)
		#print(objectText[20000]) # To stop the function because of beug...
		return [objectText, print_str]
		
	def writeMainCreationObjects(self, print_str, objectText, text_readlines):
				
		ss = ""
		temp = ss.join(text_readlines).split("#Object definition")
		temp[1] = temp[1].split("#Rest of the function")
		#temp[1][0] = temp[1][0].split("#")#[1:]
		#objectTextEnd = objectText[0]
		#objectText = objectText[1:]
		
		s = ""#"\n		#"
		#objectText[0] = objectText[0]
		temp[1][0] = s.join(objectText)
		s = "\n		#Rest of the function"
		#print(temp[1])
		#temp = s.join(temp)
		temp = temp[1][0]+s
		s = "#Object definition"
		#print(temp)
		#print(print_str)
		
		text_readlines = s.join([ss.join(text_readlines).split("#Object definition")[0],temp+"""
		MainCreation.mcCount += 1"""+
								 "\n\n	def __str__(self):\n"+ss.join(print_str)+"\n		return \"Almost there!\""+	
								 "\n\n	def getAllOrganisations(self):\n		organisationDictionary = "+str(self.organisationDictionary)+
								 "\n		return organisationDictionary"+
								 "\n\n	def getOrganisationsWECs(self, organisation):\n		organisationDictionary = " + str(self.organisationDictionary) +
								 "\n		organisation_wecs = organisationDictionary[organisation]\n" +
								 "\n		return organisation_wecs" +
								 "\n\n	def getAllWECs(self):\n		wecMotherDictionaryALL = "+str(self.wecMotherDictionaryALL)+
								 "\n		return wecMotherDictionaryALL"+
								 "\n\n	def getAllWECChildren(self):\n		wecChildrenDictionary = "+str(self.wecChildrenDictionaryALL)+
								 "\n		return wecChildrenDictionary"+
								 "\n\n	def getAllWECChildrenObjects(self):\n		wecChildrenObjectsDictionary = "+str(self.wecChildrenObjectsDictionaryALL)+
								 "\n		return wecChildrenObjectsDictionary"
								 ])
		
		""" MOUAIS FUNCTION
		 "\n\n	def getAll(self):\n		databaseDictionary = "+str(self.databaseDictionary)+
								 "\n		return databaseDictionary"+
		 "\n\n	def getWECMothers(self):\n		wecMothers = "+str(wecMothers)+
								 "\n		return wecMothers"+
		"""
		#print(text_readlines)
		#print(str(len(text_readlines)))
		
		fh = open(CreationMainCreation.mainCreationPath,"w")
		fh.write(text_readlines)
		fh.close()
		
		return text_readlines
		
	def __str__(self):
		return "\nfolders:\n{0}\n\nfolders_type:\n{1}\n\n".format(self.creationFoldersPath.new_FoldersPath.folders,self.creationFoldersPath.new_FoldersPath.folders_Type)
		
	def writeBaseMainCreationText(self):
	
		plusplus ="""
from DynamicFunctions.NonCompanyRelatedCylinder0 import NonCompanyRelatedCylinder0
from DynamicFunctions.Company2WEC40 import Company2WEC40
from DynamicFunctions.Company2WEC30 import Company2WEC30
from DynamicFunctions.Company2WEC20 import Company2WEC20
from DynamicFunctions.Company2WEC10 import Company2WEC10
from DynamicFunctions.Company1WEC20 import Company1WEC20
from DynamicFunctions.Company1WEC10 import Company1WEC10
from DynamicFunctions.NonCompanyRelatedCylinder1 import NonCompanyRelatedCylinder1
from DynamicFunctions.NonCompanyRelatedCylinder import NonCompanyRelatedCylinder
from DynamicFunctions.Company2WEC42 import Company2WEC42
from DynamicFunctions.Company2WEC41 import Company2WEC41
from DynamicFunctions.Company2WEC4 import Company2WEC4
from DynamicFunctions.Company2WEC31 import Company2WEC31
from DynamicFunctions.Company2WEC3 import Company2WEC3
from DynamicFunctions.Company2WEC21 import Company2WEC21
from DynamicFunctions.Company2WEC2 import Company2WEC2
from DynamicFunctions.Company2WEC1 import Company2WEC1
from DynamicFunctions.Company1WEC22 import Company1WEC22
from DynamicFunctions.Company1WEC21 import Company1WEC21
from DynamicFunctions.Company1WEC2 import Company1WEC2
from DynamicFunctions.Company1WEC12 import Company1WEC12
from DynamicFunctions.Company1WEC11 import Company1WEC11
from DynamicFunctions.Company1WEC1 import Company1WEC1
"""

		plusplus = "\n"

		text = """import sys
import numpy as np
"""+plusplus+"""
from CoreFunctions.CreationFoldersPath import CreationFoldersPath 
from CoreFunctions.FixRFID import FixRFID
from CoreFunctions.FixPeople import FixPeople
from CoreFunctions.FixOrganisation import FixOrganisation
from CoreFunctions.FixProject import FixProject
from CoreFunctions.FixDate import FixDate
from CoreFunctions.FixCalibration import FixCalibration
from CoreFunctions.FixTestingEnvironment import FixTestingEnvironment
from CoreFunctions.FixTestWECPostProcess import FixTestWECPostProcess

class MainCreation:
	mcCount = 0
	def __init__(self):
			
		#company2wec2_1 = Company2WEC2(1,10,"rectagle",1,1))
		
		
		MainCreation.mcCount += 1
	
		
		#Object definition
		
		
		#Rest of the function
		MainCreation.mcCount += 1
	def __str__(self):
	
		
		return "Almost there!"
			
""" #def objectDefinition(self): #company2wec2_1 = Company2WEC2(1,10,"rectagle",1,1))  return
		fh = open(CreationMainCreation.mainCreationPath,"w")
		fh.write(text)
		fh.close()
		return text
		