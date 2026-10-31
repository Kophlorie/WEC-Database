import os

class CreationFoldersPath:
	cfpCount = 0
			
	def __init__(self):
		self.pathFoldersPath = "DynamicFunctions/FoldersPath.py"	
		self.updated = 0
		self.previous_FoldersPath = ""
		new_folderspath = ""
		
		self.new_FoldersPath = ""#self.readFoldersPath(new_folderspath)
		self.text = ""#self.createFoldersPath()
		try:
			fh = open("DynamicFunctions/FoldersPath.py",'r')
		except IOError: #FileNotFoundError:
			print("FoldersPath is being created.\n") # NO!
			self.updated = 1
			self.new_FoldersPath = self.readFoldersPath(new_folderspath)
			self.text = self.createFoldersPath()
			self.writeFoldersPath()
		else:
			fh.close()
	
	def checkFoldersPath(self, previous_folderspath, new_folderspath):
	
		self.previous_FoldersPath = previous_folderspath
		self.new_FoldersPath = self.readFoldersPath(new_folderspath)
		
		if ((self.updated != 1) & (previous_folderspath != new_folderspath)):
				print("FoldersPath is being updated.\n") # NO!
				self.updated = 1
				self.text = self.createFoldersPath()
				self.writeFoldersPath()
				
		return
	
	def readFoldersPath(self,new_folderspath):
		
		# This would give location of the current directory
		# Initialisation of path_dir
		base_path="Database/" # PS: it reads straight from the topest folder of the first launching function, here mainRun.py; not the folder where the class is.
		path1=os.listdir(base_path)
		path_dir=[" "]*len(path1)
		i = 0
		for element in path1:
			if (("." in element) | ("__pycache__" in element) | ("DraftsReports" in element)):
				element = element
			else:
				path_dir[i] = base_path+element
				i += 1	
		
		path_dir=path_dir[0:i]	
		# Initialisation of the main variables
		temp="End"
		nb_top_folders=len(path_dir)
		top_folders_end=[" "]*nb_top_folders
		top_folders_Type=[" "]*nb_top_folders
		top_folders_TypePath=[" "]*nb_top_folders
		
		il=0
		top_folders_Layer=[il]*nb_top_folders
		nb_top_folders=[" "]*nb_top_folders
		top_folders=path_dir[:]

		first_folders_Position=[" "]*len(top_folders)
		first_folders=top_folders[:]
		i=0
		for element in top_folders:
			first_folders_Position[i]=i
			i += 1
		second_folders=[]
		second_folders_Position=[]

		i = 0 
		
		# Loop
		while (" " in top_folders_end):
			idx=0
			il += 1
			# Here we are running over the first path_dir in order to implement the next one
			for element in first_folders:
				idx += 1
				i=first_folders_Position[idx-1]
				
				h=""
				""" Previous version for type implementation
				try:
					path1=element+"/"+element.split("/")[-1]+"_description.txt"
					folder_type = open(path1,'r')
					top_folders_Type[i] = h.join(folder_type.readline().lstrip().splitlines( ))
					folder_type.close()
				except IOError:
					top_folders_Type[i] = "Absent"
				""" #New version for type implementation
				temp_type = ""
				temp_TypePath = ""
				j = 0
				path1 = os.listdir(element)
				for temp in os.listdir(element):
					if "_description.txt" in temp:
						j += 1
						folder_type = open(element+"/"+temp,'r')
						temp_temp_type = h.join(folder_type.readline().lstrip().splitlines( ))
						if temp_temp_type == "":
							temp_temp_type = "description_Absent"
						#print([temp_temp_type])
						temp_TypePath = temp_TypePath+" "+element+"/"+temp
						temp_type = temp_type+" "+temp_temp_type
						folder_type.close()
				if j == 0:
					top_folders_Type[i] = "Absent"
					top_folders_TypePath[i] = "Absent"
				else:
					top_folders_Type[i] = temp_type.lstrip()
					top_folders_TypePath[i] = temp_TypePath.lstrip()
				
				top_folders_end[i]="End"
				new_path=element

				new_folders=os.listdir(new_path)
				j = 0
				path_dir=[" "]*len(new_folders)
				for element in new_folders:
					if (("." in element) | ("__pycache__" in element) | ("DraftsReports" in element)):
						element = element
					else:
						path_dir[j] = element
						j += 1
			 
				path_dir=path_dir[0:j]
			
				nb_top_folders[i] = len(path_dir)

				if (nb_top_folders[i] == 0):
					top_folders_end[i]="End"			 
				else:
					if (idx<len(first_folders)):
						for j in range(len(first_folders_Position))[idx:]:
							first_folders_Position[j]=first_folders_Position[j]+nb_top_folders[i]

					j = 0
					k = 0
					for element in path_dir:
						i += 1
						top_folders_end.insert(i+k," ")
						nb_top_folders.insert(i+k," ")
						second_folders.insert(i+k,first_folders[idx-1]+"/"+element)
						second_folders_Position.insert(i+k,i+k)
						top_folders.insert(i+k,new_path+"/"+path_dir[j])
						top_folders_Type.insert(i+k," ")
						top_folders_TypePath.insert(i+k," ")
						top_folders_Layer.insert(i+k,il)
						j += 1
			# Here we are saving the new path_dir into the previous one, 
			# we initialise all and the loop will run again and agin,
			# until the top_folders_end is full of "End"s
			first_folders=second_folders	 
			first_folders_Position=second_folders_Position
			second_folders=[]
			second_folders_Position=[]
			idx = 0
			
		# Check
		if len(top_folders) != len(top_folders_Layer) != len(nb_top_folders) !=len(top_folders_Type) != len(top_folders_TypePath):
			print("There is an error the length of top_folders, top_folders_Layer, nb_top_folders, top_folders_Type, and top_folders_TypePath in CreationMainCreation do not match!")
			sys.exit()
			
		# Savings
		if self.updated == 0:
			new_folderspath.folders = top_folders
			new_folderspath.folders_Layer = top_folders_Layer
			new_folderspath.folders_Position = nb_top_folders		
			new_folderspath.folders_Type = top_folders_Type
			new_folderspath.folders_TypePath = top_folders_TypePath
			self.folders = top_folders
			self.folders_Layer = top_folders_Layer
			self.folders_Position = nb_top_folders		
			self.folders_Type = top_folders_Type
			self.folders_TypePath = top_folders_TypePath
		else:
			new_folderspath = ""
			self.folders = top_folders
			self.folders_Layer = top_folders_Layer
			self.folders_Position = nb_top_folders		
			self.folders_Type = top_folders_Type
			self.folders_TypePath = top_folders_TypePath
			
		return	new_folderspath
		
	def createFoldersPath(self):
		folders_length=len(self.folders)
		text="""class FoldersPath:
	fpCount = 0	
	def __init__(self):"""
		text=text+"\n		self.folders = [\""+self.folders[0]
		if (folders_length > 1):
			for element in self.folders[1:]:
				text=text+"\", \""+element
		text=text+"\"]\n"
		text=text+"		self.folders_Layer = ["+str(self.folders_Layer[0])
		if (folders_length > 1):
			for element in self.folders_Layer[1:]:
				text=text+", "+str(element)
		text=text+"]\n"
		text=text+"		self.folders_Position = ["+str(self.folders_Position[0])
		if (folders_length > 1):
			for element in self.folders_Position[1:]:
				text=text+", "+str(element)
		text=text+"]\n"	
		text=text+"		self.folders_Type = [\""+self.folders_Type[0]
		if (folders_length > 1):
			for element in self.folders_Type[1:]:
				text=text+"\", \""+element
		text=text+"\"]\n"
		text=text+"		self.folders_TypePath = [\""+self.folders_TypePath[0]
		if (folders_length > 1):
			for element in self.folders_TypePath[1:]:
				text=text+"\", \""+element
		text=text+"\"]"
		text=text+"""
		FoldersPath.fpCount += 1
		return	
	def __eq__(self, other):
		valueBase = 1
		if (len(self.folders) == len(other.folders)):
			i = 0
			element1 = self.folders[i]
			element2 = self.folders[i]
			i = 1
			while ((i < len(self.folders)) & (element1 == element2)):
				element1 = self.folders[i]
				element2 = other.folders[i] 
				#print("i=",str(i),"element1",element1,"element2",element2)
				i += 1
			if ((i != len(self.folders)) | (element1 != element2)):
				valueCompared = 0
			else: 
				valueCompared = 1
				i = 0
				element1 = self.folders_Layer[i]
				element2 = other.folders_Layer[i]
				i = 1
				while ((i < len(self.folders)) & (element1 == element2)):
					element1 = self.folders_Layer[i]
					element2 = other.folders_Layer[i] 
					i += 1
				if ((i != len(self.folders)) | (element1 != element2)):
					valueCompared = 0
				else: 
					valueCompared = 1
					i = 0
					element1 = self.folders_Position[i]
					element2 = other.folders_Position[i]
					i = 1
					while ((i < len(self.folders)) & (element1 == element2)):
						element1 = self.folders_Position[i]
						element2 = other.folders_Position[i] 
						i += 1
					if ((i != len(self.folders)) | (element1 != element2)):
						valueCompared = 0
					else: 
						valueCompared = 1	
						i = 0
						element1 = self.folders_Type[i]
						element2 = other.folders_Type[i]
						i = 1
						while ((i < len(self.folders)) & (element1 == element2)):
							element1 = self.folders_Type[i]
							element2 = other.folders_Type[i] 
							i += 1
						if ((i != len(self.folders)) | (element1 != element2)):
							valueCompared = 0
						else: 
							valueCompared = 1
							i = 0
							element1 = self.folders_TypePath[i]
							element2 = other.folders_TypePath[i]
							i = 1
							while ((i < len(self.folders)) & (element1 == element2)):
								element1 = self.folders_TypePath[i]
								element2 = other.folders_TypePath[i] 
								i += 1
							if ((i != len(self.folders)) | (element1 != element2)):
								valueCompared = 0
							else: 
								valueCompared = 1
		else:
			valueCompared = 0;		
		return valueBase == valueCompared
		"""
		return text
		
	def writeFoldersPath(self):
		# Here I need to rewrite the FoldersPath now following the self.new_FoldersPath
		h = ""
		try:
			folderspath=open(self.pathFoldersPath,'w')
			folderspath.write(h.join(self.text))
			folderspath.close()			
		except IOError:
			print("DynamicFunctions/FoldersPath.py does not exist.")
	