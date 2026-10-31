import sys

class CreationWEC:
	wCount = 0
	readingPath = "Database/"
	writtingPath = "DynamicFunctions/"
	s = ""
	fixedClassParams1 = "name, comments, descriptionpath, nomenclaturefilepath, functionfilespath, country_time"
	fixedClassParams = s.join(["    self.name = name\n    self.comments = comments\n    self.descriptionPath = descriptionpath\n",
					   "    self.nomenclatureFilePath = nomenclaturefilepath\n",
					   "    self.functionFilesPath = functionfilespath\n",
					   "    self.country_time = country_time\n"])
	fixedClassParamsNames = "name, comments, descriptionPath, nomenclatureFilePath, functionFilesPath, country_time"
	
	def __init__(self, readfilespath):
		self.nomenclatureFilePath = " "
		self.functionFilesPath = " "
		self.writtingFilePath = " "
		self.firstWrite = 0
		
		self.comments = [" "]
		self.pParams = [" "]
		self.paramsName = [" "]
		self.paramsUnit = [" "]
		
		self.companyName = " "
		self.className = readfilespath.split("/")[-1]
		
		self.descriptionFilePath = readfilespath+"/"+self.className+"_description.txt"
		self.text_readlines = self.readClass(self.className, self.descriptionFilePath)
		self.nb_params = self.readParametersClass(self.text_readlines)
		self.countParam = self.className.lower()+"Count"
		
		self.RFIDparamdef = "    self.IDwec = FixRFID(idwec, \"WEC"+self.className+"\")"
		self.checkOk = self.checkClass(self.writtingFilePath)		
		
		classParamsDictionary = {}
		classParamsDictionary[self.countParam] =  self.className+"."+self.countParam
		classParamsDictionary['nomenclatureFilePath'] = self.nomenclatureFilePath
		classParamsDictionary['functionFilesPath'] = self.functionFilesPath
		classParamsDictionary['descriptionFilePath'] = self.descriptionFilePath
		classParamsDictionary[self.className.lower()+"Comment"] = self.comments
		self.classParamsDictionary = classParamsDictionary # parameters of the WEC Class (Child again according to whom is calling) so not defined by the __init__
		
		text_sub_left = self.pParams
		text_sub_right_left = self.paramsName
		text_sub_right_right = self.paramsUnit
		fixedClassParamsNames = CreationWEC.fixedClassParamsNames.split(", ")
		paramsDictionaryMotherBase = {}
		paramsDictionary = {}
		i = -1
		for element in fixedClassParamsNames:
			i += 1
			paramsDictionaryMotherBase[element] = "info coming from the creation of objects"
		if text_sub_left != "None":
			j = -1
			for i in text_sub_left:
				j += 1
				paramsDictionaryMotherBase[text_sub_left[j]] = [text_sub_right_left[j],text_sub_right_right[j]]
				paramsDictionary[text_sub_left[j]] = [text_sub_right_left[j],text_sub_right_right[j]]
		self.paramsDictionary = paramsDictionary # here are the params of the WEC class (Child if called by CreationWECChild) such as p1, p2 (p3, p4 if called by the creationWECChild)
		self.paramsDictionaryMotherBase = paramsDictionaryMotherBase  # here are the params used for the object such as its name, comments, nomenclautre etc.
		
		CreationWEC.wCount += 1
		
	def readParametersClass(self, text_readlines):	
		if len(text_readlines) != 3:
			print("\nError in CreationWEC in readParametersClass:\nThe description file in:\n"+
			 self.descriptionFilePath+"\ndoes not suits the requiremenents; it should be provided as:\n"+
			 "WEC\n==\nWEC class comments\n==\nWEC class parameters written as follows:\np1: param1Name (paramsUnits)\np2: param2Name (param2Units)\netc.")
			sys.exit()
		
		self.comments = text_readlines[1].rstrip().rstrip("\n")		
		self.companyName = self.descriptionFilePath.split("/")[-3]
		self.className = self.companyName + self.className
		self.writtingFilePath = self.writtingPath+self.className+".py"
		nb_params=self.readParameters(self.text_readlines, 2)
		return nb_params
		
	def readClass(self, className, descriptionfilepath):
		try:
			fh = open(descriptionfilepath, "r")
			text_readlines = fh.read().split("==")
		except IOError:
			print("\nError in CreationWEC in readClass:\ncan\'t find file \""+descriptionfilepath+"\" and write data\nThe WEC class name is: "+self.className+
				  " you may check the description file(s) in the path:\n"+"/".join(descriptionfilepath.split("/")[0:-1]))
			sys.exit()
		else:
			fh.close()			
		return text_readlines
		
	def readParameters(self, text_readlines, indexParagraph):
		text = text_readlines[indexParagraph].split("\n")
		while "" in text:
			text.remove("")
		while " " in text:
			text.remove(" ")
		while "\t" in text:
			text.remove("\t")
		
		nb_params = len(text)
		
		# Check the parameters
		if nb_params<=0:
			print("\nError in CreationWEC in readParametersClass:\nThe description file in:\n"+
			 self.descriptionFilePath+
			 "\nPlease put \"None\" if there is no parameters to be implemented.")
			sys.exit()
			
		#print(text)
		text[0] = text[0].strip()
		if (nb_params > 1) | ("none" != text[0].lower()):
			#print(text)
			
			text_sub_left = [" "]*nb_params
			text_sub_right_left = [" "]*nb_params
			text_sub_right_right = [" "]*nb_params
			i = -1
			s = "_"
			ss="=="
			for element in text:
				i += 1
				if "(" not in element:
					print("\nError in CreationWEC in readParameters in:\n"+self.descriptionFilePath+
						  "\nThe parameters should be implemented as follows:"
						  "\np1: param name (param unit)\np2: param name (param unit)\netc.\n\nWhereas the parameter you have implemented looks like:\n"+
						  element+"\nand the text:\n"+text_readlines[2])
					sys.exit()
				temp = self.splitFancy(element) #element.split(":")
				text_sub_left[i] = temp[0].rstrip()
				text_sub_right = temp[1].split("(")
				text_sub_right_left[i] = text_sub_right[0].split(" ")
				while ("" in text_sub_right_left[i]):
					text_sub_right_left[i].remove("")
				text_sub_right_left[i]=s.join(text_sub_right_left[i])
				text_sub_right_right[i] = "("+text_sub_right[1].split(")")[0].rstrip().rstrip(".")+")"

				
			vec = self.arrangeOrderVect([text_sub_left, text_sub_right_left, text_sub_right_right],0)
		
			self.pParams = vec[0]
			self.paramsName = vec[1]
			self.paramsUnit = vec[2]
		else:
			self.pParams = "None"
			self.paramsName = "None"
			self.paramsUnit = "None"
			nb_params = 0
			
		return nb_params
		
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
						#print(text)
						comments = """\n%s""" % (text[j].split("\"\"\"")[1].lstrip("\n").rstrip("\n")) # rstrip vs lstrip... vs strip
						#print(comments)
						#print(self.comments)
						#print("comments == self.comments :", comments == self.comments)
						if (comments == self.comments):
							checkedOk = "1"
							while ((j<len(text)) & ("def __init__" not in text[j])):
								j +=1			
							pParams = text[j].split("self, "+CreationWEC.fixedClassParams1+", idwec,")
							# Check that there are parameters in the mother class...
							if (len(pParams) == 1):
								if (self.pParams == "None"):
									checkedOk = "1"
								else:
									checkedOk = "0 (len(pParams) != 1) & (self.pParams != \"None\")"
							else:
								pParams = pParams[1].split(")")[0].split(" ")
								i = -1
								for element in pParams:
									i += 1
									pParams[i]=element.split(",")[0]
								while ("" in pParams):
									pParams.remove("")								
								nb_params = len(pParams)
								#print(pParams)
								temp = self.arrangeOrderVect(pParams,1)
								#print(temp)
								#print("nb_params == self.nb_params :, nb_params = "+ str(nb_params)+" self.nb_params = "+str(self.nb_params))
								if (nb_params != self.nb_params) | (temp != self.pParams):
									checkedOk = "0 (nb_params != self.nb_params) | (pParams != self.pParams)"
								else:
									checkedOk = "1"
									text = text_readlines.split("def __init__")[1].split("):")
									text = text[1].split(self.RFIDparamdef)[1].split(self.className+"."+self.countParam)[0].split(".")
									i = -1
									#text = text.split(CreationWEC.fixedClassParams)[1]
									idx = text.index("\n    self")+1
									paramsName = [" "]*nb_params
									paramsUnit = [" "]*nb_params
									for j in range(nb_params+idx)[idx:]:
										i += 1
										temp = text[j].split("=")			
										paramsName[i] = temp[0].rstrip()
										paramsUnit[i] = "("+temp[1].split("(")[1].split(")")[0]+")"
									
									vec = self.arrangeOrderVect([pParams, paramsName, paramsUnit],0)
									paramsName = vec[1]
									paramUnit = vec[2]
									#print(text)
									if ((paramsName != self.paramsName) | (paramsUnit != self.paramsUnit)):
										checkedOk = "0 (paramsName != self.paramsName) | (paramsUnit != self.paramsUnit)"
									else:	
											checkedOk = "1"
						else:
							checkedOk = "0 (comments != self.comments)"
					else:
						checkedOk = "0 (descriptionFilePath == self.descriptionFilePath)"
				else:
					checkedOk = "0 (functionFilesPath == self.functionFilesPath)"
			else: 
				checkedOk = "0 (nomenclatureFilePath == self.nomenclatureFilePath)"
			
			# Comments
			#self.writtingFilePath - the path does not change	
			#self.className - same class name
			#self.countParam - same as above	
			#self.text_readlines - cannot be compared 
			# because I am using two fidderent files 
			# (description.txt and .py)
		except IOError:
			print("\nError in CreationWEC in checkClass:\ncan\'t find file \""+writtingFilePath+"\" and write data\n")
			checkedOk = "0"
			self.firstWrite = 1
		else:
			fh.close()
		
		return checkedOk
		
	def writeClass(self):
		s = ", "
		className = self.className
		comments = self.comments 
		countParam = self.countParam 
		writtingFilePath = self.writtingFilePath 
		text_readlines = self.text_readlines
		fixedClassParamsNames = CreationWEC.fixedClassParamsNames.split(s)
		paramsDictionary = {}
		i = -1
		for element in fixedClassParamsNames:
			i += 1
			paramsDictionary["\""+element+"\""] = "\'\"self."+element+"\'\""
		
		text_sub_left = self.pParams
		text_sub_right_left = self.paramsName
		text_sub_right_right = self.paramsUnit
		classParamsDictionary = self.classParamsDictionary
		
		text=" "
		for i in text_sub_left:
			text += i + s
		
		j = -1
		for i in text_sub_left:
			j += 1
			paramsDictionary[text_sub_left[j]] = [text_sub_right_left[j],"",text_sub_right_right[j],"self."+text_sub_right_left[j]]
		paramsDictionary = str(paramsDictionary).split(s)
		i = -1
		for element in paramsDictionary:
			i +=1
			if "'self." in element:
				paramsDictionary[i] = element.replace("'","")
		paramsDictionary = s.join(paramsDictionary).replace("'\"","'").replace("\"'","'").replace("'\\'","").replace("\\''","")
		
		classParamsDictionary[countParam] =  "\'\""+className+"."+countParam+"\'\""
		classParamsDictionary = str(classParamsDictionary).replace("'\\'\"","").replace("\\'\"'","")
	
		#print("paramsDictionary (mother) = "+str(paramsDictionary))
		#print("classParamsDictionary (mother) = "+str(classParamsDictionary))
		#print(vec[200000]) # to be able to check things before the program run and write everything
			
		# Start writting 
		fh = open(writtingFilePath, "w")
		fh.write("import numpy as np\n")
		fh.write("from CoreFunctions.FixRFID import FixRFID\n\n")
		fh.write("class "+className+":\n")
		fh.write(" "+countParam+" = 0\n")
		fh.write(" nomenclatureFilePath = \""+self.nomenclatureFilePath+"\"\n")
		fh.write(" functionFilesPath = \""+self.functionFilesPath+"\"\n")
		fh.write(" descriptionFilePath = \""+self.descriptionFilePath+"\"\n")
		fh.write(" "+className.lower()+"Comment = \"\"\""+comments+"\n\"\"\"")
		fh.write("\n def __init__(self, "+CreationWEC.fixedClassParams1+", idwec")
		if ((self.nb_params != 0) & (text_sub_left != "None")): 
			fh.write(","+text[0:-2])		
		fh.write("):\n")
		fh.write(CreationWEC.fixedClassParams)
		fh.write(self.RFIDparamdef+"\n")
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
		fh.write("\n\n def getWECMotherClassParams(self):\n    classParamsDictionary = "+ classParamsDictionary+
			  "\n    return classParamsDictionary"+
			  "\n\n def getWECMotherObjectParams(self):\n    paramsDictionary = "+ paramsDictionary+
			  "\n    return paramsDictionary")
		print("Writting content in the file \""+writtingFilePath+"\" successfully") #+" and in fact the w option + write(\"blabla\") rewrite the file completelly... I guess (I don't know for the below lines...)\n")
		fh.close()
		return
		
	def functionCreation(self, functionfilespath):
		print("Not available for the moment.")		
		return
	
	def __str__(self):
		s=", "
		print("nomenclatureFilePath = "+self.nomenclatureFilePath)
		print("functionFilesPath = "+self.functionFilesPath)
		print("descriptionFilePath = "+self.descriptionFilePath)
		print("writtingFilePath = "+self.writtingFilePath)
		print("firstWrite = "+str(self.firstWrite))
		print("comments = "+self.comments)
		print("nb_params = "+str(self.nb_params))
		print("pParams = ["+s.join(self.pParams)+"]")
		print("paramsName = ["+s.join(self.paramsName)+"]")
		print("paramsUnit = ["+s.join(self.paramsUnit)+"]")
		return "%s" %(str(self.checkOk))
		
	def splitFancy(self, text):
		if ":" in text:
			text = text.split(":")
		else: 
			if "=" in text:
				text = text.split("=")
			else:
				print("\nError using splitFancy, the element to split is not in the list")
		return text
		
	def arrangeOrderVect(self, vec, optionidx):
		#print(vec)
		nb_vecs = len(vec)
		
		#temp = []*nb_vecs
		#repere = [temp[:]]*nb_vecs
		#print(optionidx)
		if optionidx == 1:
			maximum = nb_vecs+1
			repere = [""]*nb_vecs
			previous_order = vec[:]
			for j in range(nb_vecs):
				idx = previous_order.index(min(previous_order))
				#print("j = ",str(j)," repere[j] = ",repere[j])
				repere[j] = vec[idx]
				previous_order[idx] = previous_order[idx][0:-1]+str(maximum)
		else: # Option 0 generally writen in the code
			previous_order = vec[0][:]
			nb_params = len(previous_order)
			#repere = []*nb_vecs
			
			if nb_vecs == 2:
				repere = [[" "]*nb_params, [" "]*nb_params]
				#print(repere)
			else:
				if nb_vecs == 3:
					repere = [[" "]*nb_params, [" "]*nb_params, [" "]*nb_params]
				else:
					if nb_vecs == 4:
						repere = [[" "]*nb_params, [" "]*nb_params, [" "]*nb_params, [" "]*nb_params]
					else:
						print("\nError the cases above 4 elements in vec within arrangeOrderVect in CreationWEC are not treated")
						sys.exit
			
			#print(repere)
			maximum = max(int(max(previous_order)[-1]),nb_params)+1
			#print(maximum)
			for i in range(nb_params):			
				idx = previous_order.index(min(previous_order))
				#print(idx)
				for j in range(nb_vecs):
					repere[j][i] = vec[j][idx] # repere[j].insert(i,vec[j][idx]) # 
					#print(vec)
					#print(repere)
				previous_order[idx] = previous_order[idx][0:-1]+str(maximum)
		#print(repere)
		return repere