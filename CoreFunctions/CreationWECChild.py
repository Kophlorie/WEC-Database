import sys
import math
from CoreFunctions.CreationWEC import CreationWEC

defaultParamValue = "\"\""

class CreationWECChild(CreationWEC):
	wcCount = 0
	s = ""
	fixedClassParams1 = s.join(["name = \"\", comments = \"\", descriptionpath = \"\", ",
						"nomenclaturefilepath = \"\", functionfilespath = \"\", country_time = \"\""])
	fixedClassParams = "name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time"
	fixedClassParamsNames = "name, comments, descriptionPath, nomenclatureFilePath, functionFilesPath, country_time"
	
	def __init__(self, readfilespath):
		
		self.ptoPath = [" "]
		self.primeMoverPath = [" "]
		self.mooringPath = [" "]
		
		self.nb_paramsFixed = [" "]
		self.pParamsFixed = [" "]
		self.paramsFixedValue = [" "]
		
		self.commentsMother = [" "]
		self.pParamsMother = [" "]
		self.paramsNameMother = [" "]
		self.paramsUnitMother = [" "]
		self.paramsValueMother = [" "]
		
		CreationWEC.__init__(self, readfilespath)
		
		self.motherClassName = self.companyName+readfilespath.split("/")[-2]
		self.motherPath = self.writtingPath+self.motherClassName+".py"
		self.nb_paramsMother = self.readMother(self.motherPath)
		
		paramsMotherDictionary = {}
		fixedClassParamsNames = CreationWECChild.fixedClassParamsNames.split(", ")
		paramsNameMother = self.paramsNameMother
		mother_params_def1 = self.paramsValueMother
		
		for element in fixedClassParamsNames:
			paramsMotherDictionary[element] = ""
		
		if paramsNameMother != "None":
			i = -1
			for element in paramsNameMother:
				i += 1
				paramsMotherDictionary['p'+str(i+1)] = [element, self.paramsValueMother[i].split("= ")[1].strip("\""), self.paramsUnitMother[i]]
		self.paramsMotherDictionary = paramsMotherDictionary
		
		self.objectDictionary = {}
		
		CreationWECChild.wcCount += 1
		
	def readParametersClass(self, text_readlines):
		
		if len(text_readlines) != 4:
			print("\nError in CreationWEC in readParametersClass:\nThe description file in:\n"+
			 self.descriptionFilePath+"does not suits the requiremenents: it should be provided as:\n"+
			 "WECChild\n==\nWEC class comments\n==\nThe value of the WEC mother class parameter that are fixed are provided as such:\n"+
			 "p1: motherParam1Value\np2: motherParam2Value\netc.\n==\n"+
			 "WEC class parameters written as follows:\np1: param1Name (paramsUnits)\np2: param2Name (param2Units)\netc.")
			sys.exit()
		
		self.comments = text_readlines[1].rstrip().rstrip("\n")
		self.companyName = self.descriptionFilePath.split("/")[-4]
		self.className = self.companyName + self.className
		self.writtingFilePath = self.writtingPath+self.className+".py"
	
		text = text_readlines[2].split("\n")
		#print(text)
		while "" in text:
			text.remove("")
		while " " in text:
			text.remove(" ")
		while "\t" in text:
			text.remove("\t")
		#print(text)
		text[0] = text[0].strip()
		if ((len(text) == 1) & (("none" == text[0].lower()) | (text[0] == []))):
			self.nb_paramsFixed = 0
			self.pParamsFixed = "None"
			self.paramsFixedValue = "None"
		else:
			nb_params = len(text)
			text_sub_left = [" "]*nb_params
			text_sub_right = [" "]*nb_params
			i = -1
			s = "_"
			for element in text:
				i += 1
				temp = self.splitFancy(element) #element.split(":")
				text_sub_left[i] = temp[0].rstrip()
				text_sub_right[i] = temp[1].rstrip(".").split(" ")
				while ("" in text_sub_right[i]):
					text_sub_right[i].remove("")
				text_sub_right[i]=s.join(text_sub_right[i])
			
			self.nb_paramsFixed = nb_params
			
			vec = self.arrangeOrderVect([text_sub_left,text_sub_right],0)
			self.pParamsFixed = vec[0]
			self.paramsFixedValue = vec[1]
			
		"""
		print(self.nb_paramsFixed)
		print(self.pParamsFixed)
		print(self.paramsFixedValue)
		"""
		nb_params = self.readParameters(text_readlines, 3)
		
		return nb_params
		
	def readMother(self, motherPath):
		# Initialisation
		nb_paramsFixed = self.nb_paramsFixed
		pParamsFixed = self.pParamsFixed
		paramsFixedValue = self.paramsFixedValue
		motherClassName = self.motherClassName
		# Read the mother class and split over the constructor __init__
		fh=open(motherPath,"r") # not try: it is supposed to work / exist otherwise the child wouldn't be...
		mother_params_readlines=fh.read().split("def __init__(self, "+CreationWEC.fixedClassParams1+", idwec")
		# Split
		#print(mother_params_readlines)
		if (mother_params_readlines[1][1] == ","):
			mother_params_readlines[1] = mother_params_readlines[1][1:] #+",")
		mother_params=mother_params_readlines[1].split("):\n"+CreationWEC.fixedClassParams+
					  "    self.IDwec"+
					  " = FixRFID(idwec, \"WEC"+motherClassName+"\")\n")
		mother_params_def = mother_params[0].split(", ")	
		while ("" in mother_params_def):
					mother_params_def.remove("")
		#print(mother_params_def)
		nb_paramsMother = len(mother_params_def)
		
		mother_comments = mother_params_readlines[0].split("\"\"\"")[1]
		
		if nb_paramsMother != 0:
			if nb_paramsFixed > nb_paramsMother:
				print("There is an error, in CreationWECChild, in the number of fixed parameters from the child class to the mother's parameters in\n"+self.descriptionFilePath)
				sys.exit()

			mother_params = mother_params[1].split(motherClassName.lower()+"Count")[0].split(".")
			i = -1
			idx = mother_params.index("    self")+1
			paramsNameMother = [" "]*nb_paramsMother
			paramsUnitMother = [" "]*nb_paramsMother
			for j in range(nb_paramsMother+idx)[idx:]:
				i += 1
				temp = mother_params[j].split("=")			
				paramsNameMother[i] = temp[0].rstrip().lstrip()
				paramsUnitMother[i] = "("+temp[1].split("(")[1].split(")")[0]+")"
				mother_params_def[i] = mother_params_def[i].strip()

			mother_params_def1 = mother_params_def[:]
			i = -1
			if (nb_paramsFixed != 0) & (pParamsFixed != "None"):
				for element in pParamsFixed:
					i += 1
					idx = mother_params_def.index(element)
					mother_params_def1[idx] = mother_params_def[idx]+" = \""+paramsFixedValue[i]+"\""
				# Add px = [] is not a fixed value... see defaultParamValue
				i = -1
			
			for element in mother_params_def1:
				i += 1
				if ("=" not in element):
					mother_params_def1[i] = element+" = "+defaultParamValue
			
				
			vec = self.arrangeOrderVect([mother_params_def,paramsNameMother,paramsUnitMother,mother_params_def1],0)
			self.pParamsMother = vec[0]
			self.paramsNameMother = vec[1]
			self.paramsUnitMother = vec[2]
			self.paramsValueMother = vec[3]					
		else:
			self.pParamsMother = "None"
			self.paramsNameMother = "None"
			self.paramsUnitMother = "None"
			self.paramsValueMother = "None"	
		
		# Final check
		if self.pParams != "None":
			for element in self.pParams:
				if element in self.pParamsMother:
					print("\nError in CreationWECChild in readMother in:\n"+self.descriptionFilePath+
					"\nThe parameter: "+element+
						  " is in common with the mother parameters that are:")
					print(self.pParamsMother)
					print(self.paramsNameMother)
					print(self.paramsUnitMother)
					print("whereas the child contains:")
					print(self.pParams)
					print(self.paramsName)
					print(self.paramsUnit)
					print("It means that all child's (at the above description file path) parameters\nshould be incremented of at least 1 if not more\nsuch that the first child param should be: "+
						  "p"+str(int(self.pParamsMother[-1][-1])+1))
					sys.exit()
		
		self.commentsMother = mother_comments
		#print(mother_comments)
		"""
		print(self.mother_params_def)
		print(self.paramsNameMother)
		print(elf.paramsUnitMother)
		print(self.mother_params_def1)
		print(elf.nb_paramsMother)
		"""
		
		return nb_paramsMother
		
	def checkClass(self, writtingFilePath):
		try:
			fh = open(writtingFilePath, "r")
			text_readlines=fh.read()
			text = text_readlines.split(":")[1].split("=")
			
			j = 0
			while ((j<len(text)) & ("nomenclatureFilePath" not in text[j])):
				j +=1
			j +=1
			nomenclatureFilePath = text[j].split("\"")[1]
			if (nomenclatureFilePath == self.nomenclatureFilePath):
				checkedOk = "1"
				while ((j<len(text)) & ("functionFilesPath" not in text[j])):
					j +=1
				j +=1
				functionFilesPath = text[j].split("\"")[1]
				if (functionFilesPath == self.functionFilesPath):
					checkedOk = "1"
					while ((j<len(text)) & ("descriptionFilePath" not in text[j])):
						j +=1
					j +=1
					descriptionFilePath = text[j].split("\"")[1]
					if (descriptionFilePath == self.descriptionFilePath):
						checkedOk = "1"
						while ((j<len(text)) & ("Comment" not in text[j])):
							j +=1
						j +=1
						comments = """\n%s""" % (text[j].split("\"\"\"")[1].lstrip("\n").rstrip("\n")) # rstrip vs lstrip... vs strip
						#print(comments)
						#print("comments == self.comments :", comments == self.comments)
						if (comments == self.comments):
							checkedOk = "1"							
							text = text_readlines.split("def __init__(self, "+CreationWECChild.fixedClassParams1+", idwec = FixRFID(\"\",\"WECChild"+self.className+"\",[\"\",\"\"],\"\")")
							if (text[1][1] == ","):
								text[1] = text[1][1:] #+",")
							text = text[1].split("):") # (self.RFIDparamdef)
							nb_paramsMother = text[1].split(".__init__(self, "+CreationWECChild.fixedClassParams+", idwec")
							#print("nb_paramsMother = ")
							#print(nb_paramsMother)
							if ("," in nb_paramsMother[1]):
								if (self.pParamsMother != "None"):								
									checkedOk = "1"								
									nb_paramsMother[0] = nb_paramsMother[0][1:]
									nb_paramsMother = nb_paramsMother[1].split(")")[0].split(",") #+" = FixRFID(idwec"+self.className.lower()+"\"WEC"+self.className+"\")
									while ("" in nb_paramsMother):
										nb_paramsMother.remove("")
									nb_paramsMother = len(nb_paramsMother)							
									#print("nb_paramsMother = "+ str(nb_paramsMother))
									if (nb_paramsMother == 0):
										nb_paramsFixed = 0
										pParamsFixed = "None"
										paramsFixedValue = "None"
									else:
										#if (nb_paramsMother == self.nb_paramsMother):					
										pParams = text[0].split(" ")
										while ("" in pParams):
											pParams.remove("")
										
										pParamsFixed = [" "]*nb_paramsMother
										paramsFixedValue = [" "]*nb_paramsMother # [" = "+defaultParamValue]
										i = -1
										nb_paramsFixed = 0
										#print(range(nb_paramsMother))
										for j in range(nb_paramsMother):
											idx = pParams.index("=")
											#print(pParams[idx+1])
											if defaultParamValue not in pParams[idx+1]:
												i += 1
												pParamsFixed[i] =  pParams[idx-1]
												paramsFixedValue[i] =  pParams[idx+1].split(",")[0].split("\"")[1]
												del pParams[idx]
												nb_paramsFixed += 1
											else:
												del pParams[idx]
										#print(pParamsFixed)
										#print(i)
										if i != 0:
											pParamsFixed = pParamsFixed[0:i+1]
											paramsFixedValue = paramsFixedValue[0:i+1]
										else:
											pParamsFixed = [pParamsFixed[0]]
											paramsFixedValue = [paramsFixedValue[0]]
										nb_paramsFixed = i+1												
										if (nb_paramsFixed == 0):
											pParamsFixed = "None"
											paramsFixedValue = "None"
										else:
											vec = self.arrangeOrderVect([pParamsFixed,paramsFixedValue],0)
											pParamsFixed = vec[0]
											paramsFixedValue = vec[1]
										"""
										print("nb_paramsFixed = "+str(nb_paramsFixed))
										print(pParamsFixed)
										print(self.pParamsFixed)
										print(paramsFixedValue)	
										print(self.paramsFixedValue)	
										"""
									if (nb_paramsFixed != self.nb_paramsFixed) | (pParamsFixed != self.pParamsFixed) | (paramsFixedValue != self.paramsFixedValue):
										checkedOk = "0 (nb_paramsFixed != self.nb_paramsFixed) | (pParamsFixed != self.pParamsFixed) | (paramsFixedValue != self.paramsFixedValue)"
									else:
										checkedOk = "(\",\" in nb_paramsMother[0]) & (self.pParamsMother != \"None\")"
										checkedOk = self.checkParams(text, checkedOk)
									#else:
									#	checkedOk = 0
								else:
									checkedOk = "0 (\",\" in nb_paramsMother[0]) & (self.pParamsMother == \"None\")"
							else:
								if (self.pParamsMother != "None"):
									checkedOk = 0
								else:
									checkedOk = "(\",\" not in nb_paramsMother[0]) & (self.pParamsMother != \"None\")"
									checkedOk = self.checkParams(text, checkedOk)
						else:
							checkedOk = "0 (comments != self.comments)"
					else:
						checkedOk = "0 (descriptionFilePath != self.descriptionFilePath)"
				else:
					checkedOk = "0 (functionFilesPath != self.functionFilesPath)"
			else:
				checkedOk = "0 (nomenclatureFilePath != self.nomenclatureFilePath)"
			
			# Comments
			#self.writtingFilePath - the path does not change	
			#self.className - same class name
			#self.countParam - same as above	
			#self.text_readlines - cannot be compared 
			# because I am using two fidderent files 
			# (description.txt and .py)
		except IOError:
			print("\nError in CreationWECChild in checkClass:\ncan\'t find file \""+writtingFilePath+"\" and write data\n")
			checkedOk = "0"
			self.firstWrite = 1
		else:
			fh.close()
		
		return checkedOk
	
	def checkParams(self, text, checkedOk):
		#print(text)
		text = text[1].split(self.className+"."+self.countParam)
		text = text[0].split("\n")
		while ("" in text):
					text.remove("")
		#print(text)
		ending = len(text)
		#print(self.pParams)
		#print(len(text)> 2)
		if (len(text)> 2) & (self.pParams != "None"):
			#print(text)
			idx = 0
			element = text[idx]
			while ((idx < ending) & ("   self." not in element)):
				idx += 1
				element = text[idx]
			paramsName = [" "]*ending
			paramsUnit = [" "]*ending
			pParams = [" "]*ending
			i = -1								
			while ((idx < ending) & ("   self." in text[idx])):
				i += 1
				#print(text[idx])
				temp = text[idx].split("=")			
				paramsName[i] = temp[0].split("self.")[1].rstrip()
				pParams_temp = temp[1].split("#")[0].split(" ")
				while ("" in pParams_temp):
					pParams_temp.remove("")
				pParams[i] = pParams_temp[0]
				paramsUnit[i] = "("+temp[1].split("(")[1].split(")")[0]+")"
				idx += 1
			pParams = pParams[0:i+1]
			paramsName = paramsName[0:i+1]
			paramsUnit = paramsUnit[0:i+1]
			
			
			vec = self.arrangeOrderVect([pParams,paramsName,paramsUnit],0)
			pParams = vec[0]
			paramsName = vec[1]
			paramsUnit = vec[2]
			
			"""
			s=", "
			print("pParams =")
			print(pParams)
			print("paramsName = ["+s.join(paramsName)+"]")
			print("paramsUnit = ["+s.join(paramsUnit)+"]")
			"""
			nb_params = len(paramsUnit)
			#print("nb_params == self.nb_params :, nb_params = "+ str(nb_params)+" self.nb_params = "+str(self.nb_params))
			if ((nb_params != self.nb_params) | (paramsName != self.paramsName) | 
				(pParams != self.pParams) | (paramsUnit != self.paramsUnit)):
				checkedOk = "0 "+checkedOk+" & (nb_params != self.nb_params) | (paramsName != self.paramsName) | (pParams != self.pParams) | (paramsUnit != self.paramsUnit)"
			else:	
					checkedOk = "1"
		else:
			if (len(text)<= 2) & (self.pParams == "None"):
				checkedOk = "1"
			else:
				checkedOk = "0 "+checkedOk+" & (len(text)> 2) & (self.pParams != \"None\")"
				
		return checkedOk
	
	def writeClass(self):
	
		# First main initialisation
		
		className = self.className
		comments = self.comments 
		countParam = self.countParam 
		writtingFilePath = self.writtingFilePath 
		text_readlines = self.text_readlines
		
		fixedClassParamsNames = CreationWECChild.fixedClassParamsNames
		fixedClassParams = CreationWECChild.fixedClassParams
		fixedclassparams = "\""
		fixedClassParams = fixedClassParams.split(", ")
		fixedClassParamsNames = fixedClassParamsNames.split(", ")
		paramsMotherDictionary = {}
		i = -1
		for element in fixedClassParams:
			i += 1
			paramsMotherDictionary["\""+fixedClassParamsNames[i]+"\""] = "\'\"self."+fixedClassParamsNames[i]+"\'\"" #vec[i] = fixedClassParamsNames[i]
			fixedclassparams += element + " = \"+self." + fixedClassParamsNames[i] + "+\"\\n"
					
		text_sub_left = self.pParams
		text_sub_right_left = self.paramsName	
		text_sub_right_right = self.paramsUnit
		paramsChildDictionary = self.paramsDictionary
		classParamsDictionary = self.classParamsDictionary
		
		motherClassName = self.motherClassName
		mother_params_def = self.pParamsMother
		mother_params_def1 = self.paramsValueMother
		paramsUnitMother = self.paramsUnitMother
		paramsNameMother = self.paramsNameMother
		
		# Update of the mother and fixed param values including some of the child params
		text = ""
		
		if (mother_params_def != "None"):
			nb_paramsTotal = len(text_sub_left) + len(mother_params_def)
			mother_params = ", "
			mother_params1 = ", "
			mother_params2 = ""
			mother_params3 = ".format("
			i = -1
			for element in mother_params_def:
				i += 1
				paramsMotherDictionary['p'+str(i+1)] = [paramsNameMother[i], mother_params_def1[i].split("= \"")[1], paramsUnitMother[i],"self."+paramsNameMother[i]]
				mother_params += element + ", "
				mother_params1 += mother_params_def1[i] + ", "
				mother_params2 += mother_params_def1[i] +" "+paramsUnitMother[i]+" --> {"+str(i)+"}\\n"
				mother_params3 += "self."+paramsNameMother[i]+", "
			mother_params3 = mother_params3[0:-2]+")+\"\\n\""
			
			mother_params = mother_params[0:-2]
			if text_sub_left == "None":
				mother_params1 = mother_params1[0:-2]
				nb_paramsTotal = len(mother_params_def)
				text2 = "None"
				text3 = "+\"\\n\\n\""
			else:
				text2 = ""
				text3 = ".format("
				j = -1
				for i in text_sub_left:
					j += 1
					text += i + " = "+defaultParamValue+", "
					text2 += i + " = "+defaultParamValue+" "+text_sub_right_right[j]+" --> {"+str(j)+"}\\n"
					text3 += "self."+text_sub_right_left[j]+", "
					paramsChildDictionary[text_sub_left[j]] = [text_sub_right_left[j],"",text_sub_right_right[j],"self."+text_sub_right_left[j]]
				text3 = text3[0:-2]+")+\"\\n\""
		else:
			mother_params = ""
			mother_params2 = "None"
			mother_params3 = "+\"\\n\\n\""
			
			if text_sub_left == "None":
				mother_params1 = ""
				text2 = "None"
				text3 = "+\"\\n\\n\""
				nb_paramsTotal = 0
			else:
				mother_params1 = ", "
				nb_paramsTotal = len(text_sub_left)
				text2 = ""
				text3 = ".format("
				j = -1
				for i in text_sub_left:
					j += 1
					text += i + " = "+defaultParamValue+", "
					text2 += i + " = "+defaultParamValue+" "+text_sub_right_right[j]+" --> {"+str(j)+"}\\n"
					text3 += "self."+text_sub_right_left[j]+", "
					paramsChildDictionary[text_sub_left[j]] = [text_sub_right_left[j],"\"\"",text_sub_right_right[j],"self."+text_sub_right_left[j]]
				text3 = text3[0:-2]+")+\"\\n\""
		
		# Update of the dictionary for the child to get its parameters
		s = ", "
		paramsMotherDictionary = str(paramsMotherDictionary).split(s)
		i = -1
		for element in paramsMotherDictionary:
			i +=1
			if "'self." in element:
				paramsMotherDictionary[i] = element.replace("'","")
		paramsMotherDictionary = s.join(paramsMotherDictionary).replace("'\"","'").replace("\"'","'").replace("'\\'","").replace("\\''","")
		#print(paramsChildDictionary)
		paramsChildDictionary = str(paramsChildDictionary).split(s)
		i = -1
		for element in paramsChildDictionary:
			i +=1
			#print(element)
			if "self." in element:
				paramsChildDictionary[i] = element.replace("'","")
		paramsChildDictionary = s.join(paramsChildDictionary)
		
		classParamsDictionary[countParam] = "\'\""+className+"."+countParam+"\'\""
		classParamsDictionary = str(classParamsDictionary).replace("'\\'\"","").replace("\\'\"'","")#.replace("\"'","").replace("'\"","")
			 
		#print("paramsChildDictionary (child) = "+paramsChildDictionary+"\n")
		#print("classParamsDictionary (child) = "+classParamsDictionary+"\n")
		#print(vec[200000]) # to be able to check things before the program run and write everything
		# Start writting
		
		ss=" "
		
		fh = open(writtingFilePath, "w")
		fh.write("import numpy as np\n")
		fh.write("from CoreFunctions.FixRFID import FixRFID\n")
		fh.write("from "+CreationWECChild.writtingPath[0:-1]+"."+motherClassName+" import "+motherClassName+"\n\n") # fh.write(ss.join(mtext)+"\n\n")
		fh.write("class "+className+"("+motherClassName+"):\n")
		fh.write(" "+countParam+" = 0\n")
		fh.write(" nomenclatureFilePath = \""+self.nomenclatureFilePath+"\"\n")
		fh.write(" functionFilesPath = \""+self.functionFilesPath+"\"\n")
		fh.write(" descriptionFilePath = \""+self.descriptionFilePath+"\"\n")
		fh.write(" "+className.lower()+"Comment = \"\"\""+comments+"\n\"\"\"\n")
		fh.write(" def __init__(self, "+CreationWECChild.fixedClassParams1+", idwec = FixRFID(\"\",\"WECChild"+className+"\",[\"\",\"\"],\"\")"+mother_params1)
		if ((self.nb_params != 0) & (text_sub_left != "None")):
			fh.write(text[0:-2])
		fh.write("):\n")
		fh.write("    "+motherClassName+".__init__(self, "+CreationWECChild.fixedClassParams+", idwec"+mother_params+")\n")
		#fh.write(self.RFIDparamdef)
		if ((self.nb_params != 0) & (text_sub_left != "None")):
			i = 0
			for element in text_sub_right_left:
				fh.write("    self."+element
					  +" = "+text_sub_left[i]+" # "+ text_sub_right_right[i]+"\n")
				i += 1
		fh.write("    "+className+"."+countParam+" += 1\n"+
		  "    self.classAttached = self.__class__.__name__\n"+
		  "    self.listFilePath = \"Database/Lists/WECs/\"+self.IDwec.ID+\".txt\"\n"+
		  "    print(self.classAttached, \"'s object created and "+countParam+" = \","+className+"."+countParam+")") # write("This is my test file for exception handling!!")
		
		s = ""	
		
		text=s.join(["""\n def __str__(self):
    print("\\n\\nPrinting the object (\"+self.name+\"):\\n\\nAttributes from the WEC mother class (""",motherClassName+"):\\np0:\\n\"+\n"+
			  "    \""+motherClassName.lower()+"Count = \"+str("+motherClassName+"."+motherClassName.lower()+"Count)+\n"
			  "    \"\\nnomenclatureFilePath = \\\"\"+"+motherClassName+".nomenclatureFilePath+\"\\\"\\n\"+\n"+
			  "    \"functionFilesPath = \\\"\"+"+motherClassName+".functionFilesPath+\"\\\"\\n\"+\n"+
			  "    \"descriptionFilePath = \"+"+motherClassName+".descriptionFilePath+\"\\n\"+\n"+
			  "    \""+motherClassName.lower()+"Comment = \"+\"\\\"\\\"\\\"\"+"+motherClassName+"."+motherClassName.lower()+"Comment+\"\\\"\\\"\\\"\")\n",
			  "    print(\"Attributes from the WEC child class (",className+"):\\n\"+\n"+
			  "    \""+countParam+" = \"+str("+className+"."+countParam+")+\n"
			  "    \"\\nnomenclatureFilePath = \\\""+self.nomenclatureFilePath+"\\\"\\n\"+\n"+
			  "    \"functionFilesPath = \\\""+self.functionFilesPath+"\\\"\\n\"+\n"+
			  "    \"descriptionFilePath = "+self.descriptionFilePath+"\\n\"+\n"+
			  "    \""+className.lower()+"Comment = \"+\"\"\"\\\"\\\"\\\""+comments+"\n\\\"\\\"\\\"\"\"\"+\n"+
			  "    \"\\nMother ("+motherClassName+") parameters including the fixed ones:\\n\"+\n"+
			  "    "+fixedclassparams+"idwec = \"+str(self.IDwec)+\"\\n\"+\n"+
			  "    \"\"\""+mother_params2+"\"\"\""+mother_params3+"+"+
			  "\n    \"Child ("+className+") parameters:\\n\"+\n"+
			  "    \"\"\""+text2+"\"\"\""+text3+
			  ")"+"\n    return \"That's all for the WEC ({0})\".format(self.name)"+
			  "\n\n def getWECChildClassParams(self):\n    classParamsDictionary = "+ classParamsDictionary+
			  "\n    return classParamsDictionary"+
			  "\n\n def getWECChildObjectParams(self):\n    paramsChildDictionary = "+ paramsChildDictionary+
			  "\n    return paramsChildDictionary"+
			  "\n\n def getWECMotherObjectParams(self):\n    paramsMotherDictionary = "+ paramsMotherDictionary+
			  "\n    return paramsMotherDictionary"
			  ])
			  
		fh.write(text)
		
		print("Writting content in the file \""+writtingFilePath+"\" successfully") #+" and in fact the w option + write(\"blabla\") rewrite the file completelly... I guess (I don't know for the below lines...)\n")		
		fh.close()
		return
		
	def createObjectMainRun(self, objectPath):
	
		# Initialisation
		
		objectDictionary = self.objectDictionary
		paramsMotherDictionary = self.paramsMotherDictionary
		paramsDictionary = self.paramsDictionary		
		
		pParamsFixed = self.pParamsFixed
		paramsFixedValue = self.paramsFixedValue
		
		if pParamsFixed == "None":
			nb_paramsFixed = 0
		else:
			nb_paramsFixed = len(pParamsFixed)
		
		pParams = self.pParams
		mother_params_def = self.pParamsMother
		
		if (mother_params_def != "None"):
			nb_paramsTotal = len(pParams) + len(mother_params_def) # not counting for IDWEC and for country_time...
			if pParams == "None":
				nb_paramsTotal = len(mother_params_def)
		else:			
			if pParams == "None":
				nb_paramsTotal = 0
			else:
				nb_paramsTotal = len(pParams) # not counting for IDWEC and for country_time...
		text = ""
		
		# Reading 
		try:
			fh = open(objectPath,'r')
			object_readlines = fh.read().split("==")
		except IOError:
			print("\nError in CreationWECChild in createObjectMainRun:\nwe cannot open: "+objectPath+".")
		else:
			if len(object_readlines) != 3:
				print("Error in CreationWECChild in createObjectMainRun in:\n"+objectPath+
					  "\nThe file is not written properly:")
				print("It should be provided as:\n"+
					 "WECChildObject\n==\nWEC child object comments\n==\nIDWEC = WECNameYearMonthDayHourMinutes\nCountry_time = Country of ID date and hour\np1 = value\np2 = value\netc.\n\nSuch that:")
				print("Paremeters mother:")
				print(mother_params_def)
				print(self.paramsNameMother)
				print(self.paramsUnitMother)
				print("Paremeters fixed:")
				print(pParamsFixed)
				print(paramsFixedValue)
				print("Paremeters child:")
				print(pParams)
				print(self.paramsName)
				print(self.paramsUnit)
				sys.exit()
			
			fh.close()
			#print(object_readlines)
			object_name = objectPath.split("/")[-1].split(".")[0]
			comments = "\"\"\""+object_readlines[1].strip("\n")+"\"\"\""
			params = object_readlines[2].split("\n")
			while ("" in params):
				params.remove("")
			#print(params)
			nb_paramsMOtherTobeImplemented = 2 if len(params) > 1 and self.splitFancy(params[1])[0].strip().lower() == "country_time" else 1
			nb_params = len(params)- nb_paramsMOtherTobeImplemented 
			#print("nb_params = "+str(nb_params)+"\nnb_paramsTotal = "+str(nb_paramsTotal)+"\nnb_paramsFixed = ",str(nb_paramsFixed)+"\npParamsFixed is:\n"+str(pParamsFixed))
			
			if (params == []) | (nb_paramsTotal < 0) | nb_params<0 | (nb_params<nb_paramsTotal-nb_paramsFixed):
				print("Error in CreationWECChild in createObjectMainRun in:\n"+objectPath+
					  "\nThe file is not written properly:")
				print("It should be provided as:\n"+
					 "WECChildObject\n==\nWEC child object comments\n==\nIDWEC = WECNameYearMonthDayHourMinutes\nCountry_time = Country of ID date and hour\np1 = value\np2 = value\netc.\n\nSuch that:")
				print("Paremeters mother:")
				print(mother_params_def)
				print(self.paramsNameMother)
				print(self.paramsUnitMother)
				print("Paremeters fixed:")
				print(pParamsFixed)
				print(paramsFixedValue)
				print("Paremeters child:")
				print(pParams)
				print(self.paramsName)
				print(self.paramsUnit)
				print("\nparams looks like:\n\"\n"+"\n".join(params)+"\n\"")
				sys.exit()
			elif (params[0].lower().strip() == "none"):
				print("\nError in CreationWECChild in createObjectMainRun: in:\n"+objectPath+"\nthe identification is not even implemented, please implement it as:\n\"WECID= FullNameIndexYearMonthDayHourMinute\" below the 2nd \"==\" in order to proceed.")
				print("params looks like:\n"+"\n".join(params))
				sys.exit()
			else:
			
			
				idwec = "\""+self.splitFancy(params[0])[1].strip()+"\""
				country_time = "\""+self.splitFancy(params[1])[1].strip()+"\"" if nb_paramsMOtherTobeImplemented == 2 else "\"\""
			
			text_base = "\n		#"+object_name+"\n		self."+object_name.lower()+" = "+self.className+"(\"{0}\", {1}, \"{2}\", \"{3}\", \"{4}\", {5}, {6}".format(
							object_name,
							comments,
							objectPath,
							"",
							"",
							idwec, country_time)
			
			#print(str(nb_paramsTotal))
			
			if (nb_paramsTotal > 1):
				
				# Loop to check that the parameters are provided using "p" and the number
				# It also allows the preparation of the params in order to reange them properly
				i = 0
				j = -1
				pvec = [" "]*(nb_params) # considering of WEC ID and Country time and so below
				vvec = [" "]*(nb_params) # considering of WEC ID and Country time and so below  
				for element in params[nb_paramsMOtherTobeImplemented:]:
					j += 1
					temp = self.splitFancy(element)
					pvec[j] = temp[0].strip()
					vvec[j] = temp[1].strip()
					if pvec[j][0].lower() != "p":
						i += 1
				if nb_params > 0:
					idx = int(max(pvec)[1])
				else:
					idx = 0
				
				if ((params[1].strip().lower() == "none") & (nb_paramsFixed != nb_paramsTotal)) | (i != 0) | (idx > nb_paramsTotal):
					print("\nError in CreationWECChild in createObjectMainRun: in:\n"+objectPath+"\nThere is no param implemented or not enough parameters fixed="+str(nb_paramsFixed)+" for the total number of parameters="+str(nb_paramsTotal)+", such tat:")
					print("It should be provided as:\n"+
							 "WECChildObject\n==\nWEC child object comments\n==\nIDWEC = WECNameYearMonthDayHourMinutes\nCountry_time = Autralia\np1 = value\np2 = value\netc.\n\nSuch that:")
					print("Paremeters mother:")
					print(mother_params_def)
					print(self.paramsNameMother)
					print(self.paramsUnitMother)
					print("Paremeters fixed:")
					print(pParamsFixed)
					print(paramsFixedValue)
					print("Paremeters child:")
					print(pParams)
					print(self.paramsName)
					print(self.paramsUnit)
					print("\nparams looks like:\n\"\n"+"\n".join(params)+"\n\"")
					sys.exit()			
						
				#print(params[25200000]) # to check the above checking and stop the function instead of keeping running
				values = ["None"]*nb_paramsTotal
				pParamsObject = ["p"]*nb_paramsTotal
				
				if (nb_params > 0):
					
					# Check 
					
					if nb_paramsTotal < nb_params:
						print("\nError in CreationWECChild in createObjectMainRun: nb_paramsTotal="+str(nb_paramsTotal)+" < "+str(nb_params)+"=nb_params...")
						sys.exit()
						
					# Finilize the rearranging of the object parameters in the right order
					
					#print(pvec)
					#print(vvec)	
					vec =self.arrangeOrderVect([pvec,vvec],0)
					#print(vec)
					pvec = vec[0]
					vvec = vec[1]
					for i in range(nb_paramsMOtherTobeImplemented,len(params)): # considering of WEC ID and Country time
						params[i] = pvec[i-nb_paramsMOtherTobeImplemented]+" = "+vvec[i-nb_paramsMOtherTobeImplemented]
					
					# Update the values of the object at the right spot.
					
					for i in range(nb_paramsMOtherTobeImplemented,nb_params+nb_paramsMOtherTobeImplemented): # considering of WEC ID and Country time
						temp = self.splitFancy(params[i])
						nb_paramsObject = len(temp)
						paircheck = (nb_paramsObject/2) - math.floor(nb_paramsObject/2) - 1
						#print(temp)
						#print("nb_paramsObject = "+str(nb_paramsObject)+", paircheck ="+str(paircheck))
						if (nb_paramsObject >= 2) & ((paircheck == 0) | (paircheck == -1)):
							idx = int(temp[0].strip()[-1])-1
							values[idx] = temp[1].strip()
						else:
							print("\nError in CreationWECChild when reading the object of:\n"+objectPath+"\n the value of one of the object params is written:")
							print(temp)
							sys.exit()
					
					# Check for the fixed values
					
					text = ", "
					for i in range(0,nb_paramsTotal):
						pParamsObject[i] = pParamsObject[i]+str(i+1)
						if pParamsObject[i] in pParamsFixed:
							idx = pParamsFixed.index(pParamsObject[i])
							if (values[i] == "None"):
								values[i] = paramsFixedValue[idx]
							else:
								if (values[i] != paramsFixedValue[idx]):
									print("\nError in CreationWECChild in createObjectMainRun in:\n"+objectPath+"\nThe value assigned for "+pParams[idx]+" does not correspond to the fixed value:\n"+
										  "paramsFixedValue = "+paramsFixedValue[idx]+" whereas values = "+values[i])
									sys.exit()
						text = text+"\""+values[i]+"\", "
					# Check that we have filled in the parameters
					
					if ("None" in values) | ("" in values):
						print("\nError in CreationWECChild in createObjectMainRun in:\n"+objectPath+"\nThe object is not completely filled in...")
						print("It should be provided as:\n"+
							 "WECChildObject\n==\nWEC child object comments\n==\nIDWEC = WECNameYearMonthDayHourMinutes\nCountry_time = Country of ID date and hour\np1 = value\np2 = value\netc.\n\nSuch that:")
						print("Particularly here:")
						print("Paremeters mother:")
						print(mother_params_def)
						print(self.paramsNameMother)
						print(self.paramsUnitMother)
						print("Paremeters fixed:")
						print(pParamsFixed)
						print(paramsFixedValue)
						print("Paremeters child:")
						print(pParams)
						print(self.paramsName)
						print(self.paramsUnit)						
						print("\nAnd you have implemented: (the \"None\" value for missing information)")
						print(values)
						print("\nparams looks like:\n\"\n"+"\n".join(params)+"\n\"")
						sys.exit()
					else:
						text = text[0:-2]
						
					text = text_base+"{0})\n".format(text)
			else:
				if (nb_params > 0):
					print("\nError in CreationWECChild in createObjectMainRun: there are no parameters... but the script:\n"+objectPath+"\ntries to implement some...")
					print("You may have implemented a \"None\" or any other value/param below the ID and Country_time,\nplease delete it if this is the case")
					print("\nparams looks like:\n\"\n"+"\n".join(params)+"\n\"")
					sys.exit()
				else:
					text = text_base+")\n"
			#print(values)
			# create the line to write in the MainRun.py 
			# --> I am going to use the dictionary
			#paramsMotherDictionary
			#paramsDictionary
			vec = [object_name, comments, objectPath, "", "", idwec]
			i = -1
			for element in self.fixedClassParamsNames.split(", "):
				i += 1
				paramsMotherDictionary[element] = vec[i]
				objectDictionary[element] = paramsMotherDictionary[element]
			if mother_params_def != "None":
				i = -1
				for element in mother_params_def:
					i += 1
					vec = paramsMotherDictionary.get(element)
					vec = str(vec).lstrip("[").rstrip("]").replace("'","")+", "+values[i]
					vec = vec.split(", ")
					#vec = vec.insert(0,)
					#print(vec)
					objectDictionary[element] = vec
			if pParams != "None":
				for element in pParams:
					i +=1
					vec = paramsDictionary[element]
					vec = str(vec).lstrip("[").rstrip("]").replace("'","")+", "+values[i]
					vec = vec.split(", ")
					objectDictionary[element] = vec
			#print(objectDictionary)
			#print("The text is:\n\"\n"+text+"\n\"")
			
		"""
		if (mother_params_def != "None"):
			if pParams == "None":
		else:
			
			if pParams == "None":
			else:
		"""
		
		self.objectDictionary = objectDictionary
		return text
		
	def test(self):
	
		className = self.className
		comments = self.comments 
		countParam = self.countParam 
		writtingFilePath = self.writtingFilePath 
		text_readlines = self.text_readlines
		fixedClassParamsNames = CreationWECChild.fixedClassParamsNames
		fixedClassParams = CreationWECChild.fixedClassParams
		fixedclassparams = "\""
		fixedClassParams = fixedClassParams.split(", ")
		fixedClassParamsNames = fixedClassParamsNames.split(", ")
		i = -1
		for element in fixedClassParams:
			i += 1
			fixedclassparams += element + " = \"+self." + fixedClassParamsNames[i] + "+\"\\n"
			
		text_sub_left = self.pParams
		text_sub_right_left = self.paramsName	
		text_sub_right_right = self.paramsUnit
		text2=""
		text3 = ".format("
		j = -1
		for i in text_sub_left:
			j +=1
			text2 += i + " = "+defaultParamValue+" "+text_sub_right_right[j]+" --> {"+str(j)+"}\\n"
			text3 += "self."+text_sub_right_left[j]+", "
		text3 = text3[0:-2]+")+\"\\n\""
		
		motherClassName = self.motherClassName
		mother_params_def = self.pParamsMother
		mother_params_def1 = self.paramsValueMother
		paramsUnitMother = self.paramsUnitMother
		paramsNameMother = self.paramsNameMother
		
		if (mother_params_def != "None"):
			nb_paramsTotal = len(text_sub_left) + len(mother_params_def)
			mother_params2 = ""
			mother_params3 = ".format("
			i = -1
			for element in mother_params_def:
				i += 1
				mother_params2 += mother_params_def1[i] +" "+paramsUnitMother[i]+" --> {"+str(i)+"}\\n"
				mother_params3 += "self."+paramsNameMother[i]+", "
			mother_params3 = mother_params3[0:-2]+")+\"\\n\""
				
			if text_sub_left == "None":
				mother_params2 = mother_params2[0:-2]
				nb_paramsTotal = len(mother_params_def)
		else:
			
			mother_params2 = "None"
			mother_params3 = "None"
			
			if text_sub_left == "None":
				mother_params1 = ""
				nb_paramsTotal = 0
			else:
				mother_params1 = ", "
				nb_paramsTotal = len(text_sub_left)
		
		s = ""		
		
		text=s.join(["""\n def __str__(self):
    print("\\n\\nPrinting the object (\"+self.name+\"):\\n\\nAttributes from the WEC mother class (""",motherClassName+"):\\n\"+\n"+
			  "    \""+motherClassName.lower()+"Count = \"+str("+motherClassName+"."+motherClassName.lower()+"Count)+\n"
			  "    \"\\nnomenclatureFilePath = \\\"\"+"+motherClassName+".nomenclatureFilePath+\"\\\"\\n\"+\n"+
			  "    \"functionFilesPath = \\\"\"+"+motherClassName+".functionFilesPath+\"\\\"\\n\"+\n"+
			  "    \"descriptionFilePath = \"+"+motherClassName+".descriptionFilePath+\"\\n\"+\n"+
			  "    \""+motherClassName.lower()+"Comment = \"+\"\\\"\\\"\\\"\"+"+motherClassName+"."+motherClassName.lower()+"Comment+\"\\\"\\\"\\\"\")\n",
			  "    print(\"Attributes from the WEC child class (",className+"):\\n\"+\n"+
			  "    \""+countParam+" = \"+str("+className+"."+countParam+")+\n"
			  "    \"\\nnomenclatureFilePath = \\\""+self.nomenclatureFilePath+"\\\"\\n\"+\n"+
			  "    \"functionFilesPath = \\\""+self.functionFilesPath+"\\\"\\n\"+\n"+
			  "    \"descriptionFilePath = "+self.descriptionFilePath+"\\n\"+\n"+
			  "    \""+className.lower()+"Comment = \"+\"\"\"\\\"\\\"\\\""+comments+"\n\\\"\\\"\\\"\"\"\"+\n"+
			  "    \"\\nMother ("+motherClassName+") parameters including the fixed ones:\\n\"+\n"+
			  "    "+fixedclassparams+"idwec = \"+str(self.IDwec)+\"\\n\"+\n"+
			  "    \"\"\""+mother_params2+"\"\"\""+mother_params3+"+"+
			  "\n    \"Child ("+className+") parameters:\\n\"+\n"+
			  "    \"\"\""+text2+"\"\"\""+text3+
			  ")"])

		fh = open("Tests/TestWritting.py",'w')
		fh.write(text)
		fh.close()
		return text
		
	def __str__(self):
		s=", "
		print("pParamsFixed = ["+s.join(self.pParamsFixed)+"]")
		print("paramsFixedValue = ["+s.join(self.paramsFixedValue)+"]")
		print("nb_paramsFixed = ["+str(self.nb_paramsFixed)+"]")
		print("nomenclatureFilePath = "+self.nomenclatureFilePath)
		print("functionFilesPath = "+self.functionFilesPath)
		print("descriptionFilePath = "+self.descriptionFilePath)
		print("writtingFilePath = "+self.writtingFilePath)
		print("firstWrite = "+self.firstWrite)
		print("comments = "+self.comments)
		print("nb_params = "+str(self.nb_params))
		print("pParams = ["+s.join(self.pParams)+"]")
		print("paramsName = ["+s.join(self.paramsName)+"]")
		print("paramsUnit = ["+s.join(self.paramsUnit)+"]")
		return "%s" %(str(self.checkOk))
	