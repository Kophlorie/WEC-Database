class FoldersPath:
	fpCount = 0	
	def __init__(self):
		self.folders = ["Database/Company1", "Database/Company1/WEC1", "Database/Company1/WEC1/WEC10", "Database/Company1/WEC1/WEC11", "Database/Company1/WEC1/WEC11/NumericalTest", "Database/Company1/WEC1/WEC11/WaveTank", "Database/Company1/WEC1/WEC11/WaveTank/1_WaveTank", "Database/Company1/WEC1/WEC11/WaveTank/1_WaveTank/Calibration", "Database/Company1/WEC1/WEC11/WaveTank/1_WaveTank/PostProcessing", "Database/Company1/WEC1/WEC11/WaveTank/1_WaveTank/RawData", "Database/Company1/WEC1/WEC11/WaveTank/2_WaveTank", "Database/Company1/WEC1/WEC11/WaveTank/2_WaveTank/Calibration", "Database/Company1/WEC1/WEC11/WaveTank/2_WaveTank/PostProcessing", "Database/Company1/WEC1/WEC11/WaveTank/2_WaveTank/RawData", "Database/Company1/WEC1/WEC12", "Database/Company1/WEC1/WEC12/DryTest", "Database/Company1/WEC1/WEC12/DryTest/1_DryTest", "Database/Company1/WEC1/WEC12/DryTest/1_DryTest/Calibration", "Database/Company1/WEC1/WEC12/DryTest/1_DryTest/PostProcessing", "Database/Company1/WEC1/WEC12/DryTest/1_DryTest/RawData", "Database/Company1/WEC2", "Database/Company1/WEC2/WEC20", "Database/Company1/WEC2/WEC21", "Database/Company1/WEC2/WEC21/DryTest", "Database/Company1/WEC2/WEC21/DryTest/1_DryTest", "Database/Company1/WEC2/WEC21/DryTest/1_DryTest/Calibration", "Database/Company1/WEC2/WEC21/DryTest/1_DryTest/PostProcessing", "Database/Company1/WEC2/WEC21/DryTest/1_DryTest/RawData", "Database/Company1/WEC2/WEC21/WaveTank", "Database/Company1/WEC2/WEC21/WaveTank/1_WaveTank", "Database/Company1/WEC2/WEC21/WaveTank/1_WaveTank/Calibration", "Database/Company1/WEC2/WEC21/WaveTank/1_WaveTank/PostProcessing", "Database/Company1/WEC2/WEC21/WaveTank/1_WaveTank/RawData", "Database/Company1/WEC2/WEC22", "Database/Company1/WEC2/WEC22/WaveTank", "Database/Company1/WEC2/WEC22/WaveTank/1_WaveTank", "Database/Company1/WEC2/WEC22/WaveTank/1_WaveTank/Calibration", "Database/Company1/WEC2/WEC22/WaveTank/1_WaveTank/PostProcessing", "Database/Company1/WEC2/WEC22/WaveTank/1_WaveTank/RawData", "Database/Company2", "Database/Company2/WEC1", "Database/Company2/WEC1/WEC10", "Database/Company2/WEC2", "Database/Company2/WEC2/WEC20", "Database/Company2/WEC2/WEC21", "Database/Company2/WEC3", "Database/Company2/WEC3/WEC30", "Database/Company2/WEC3/WEC31", "Database/Company2/WEC4", "Database/Company2/WEC4/WEC40", "Database/Company2/WEC4/WEC41", "Database/Company2/WEC4/WEC42", "Database/Company2/WEC4/WEC42/DryTest", "Database/Company2/WEC4/WEC42/DryTest/1_DryTest", "Database/Lists", "Database/Lists/Calibrations", "Database/Lists/Organisations", "Database/Lists/People", "Database/Lists/Projects", "Database/Lists/RFID", "Database/Lists/TestingEnvironments", "Database/Lists/TestWECPostProcesses", "Database/Lists/WECs", "Database/NonCompanyRelated", "Database/NonCompanyRelated/Cylinder", "Database/NonCompanyRelated/Cylinder/Cylinder0", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest/Calibration", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest/PostProcessing", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest/RawData", "Database/NonCompanyRelated/Cylinder/Cylinder1", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank/1_WaveTank", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank/1_WaveTank/Calibration", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank/1_WaveTank/PostProcessing", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank/1_WaveTank/RawData", "Database/Weptos", "Database/Weptos/WeptosWEC", "Database/Weptos/WeptosWEC/WeptosWEC0", "Database/Weptos/WeptosWEC/WeptosWEC1", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest/1_DryTest", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest/1_DryTest/Calibration", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest/1_DryTest/PostProcessing", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest/1_DryTest/RawData", "Database/Weptos/WeptosWEC/WeptosWEC2"]
		self.folders_Layer = [0, 1, 2, 2, 3, 3, 4, 5, 5, 5, 4, 5, 5, 5, 2, 3, 4, 5, 5, 5, 1, 2, 2, 3, 4, 5, 5, 5, 3, 4, 5, 5, 5, 2, 3, 4, 5, 5, 5, 0, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 3, 4, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 3, 4, 5, 5, 5, 2, 3, 4, 5, 5, 5, 0, 1, 2, 2, 3, 4, 5, 5, 5, 2]
		self.folders_Position = [2, 3, 0, 2, 0, 2, 3, 0, 0, 0, 3, 0, 0, 0, 1, 1, 3, 0, 0, 0, 3, 0, 2, 1, 3, 0, 0, 0, 1, 3, 0, 0, 0, 1, 1, 3, 0, 0, 0, 4, 1, 0, 2, 0, 0, 2, 0, 0, 3, 0, 0, 1, 1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 3, 0, 0, 0, 1, 1, 3, 0, 0, 0, 1, 3, 0, 1, 1, 3, 0, 0, 0, 0]
		self.folders_Type = ["OrganisationObject", "WECClass", "WECChild", "WECChild", "Absent", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "WECChild", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "WECClass", "WECChild", "WECClassChild", "Absent", "WECChildObject WECChildObject", "Absent", "Absent", "Absent", "Absent", "wecchildObject", "Absent", "Absent", "Absent", "WECChild", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "CompanyObject", "WECClass", "WECChild", "WECClass", "WECChild", "WECChild", "WECClass", "WECChild", "WECChild", "WECClass", "WECChild", "WECChild", "WECChild", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "OrganisationObject", "WECClass", "WEChild", "Absent", "WECChildObject WECChildObject", "Absent", "Absent", "Absent", "WEChild", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "OrganisationObject", "WEC", "WECChild", "WECChild", "Absent", "WECChildObject", "Absent", "Absent", "Absent", "Absent"]
		self.folders_TypePath = ["Database/Company1/Company1_1_description.txt", "Database/Company1/WEC1/WEC1_description.txt", "Database/Company1/WEC1/WEC10/WEC10_description.txt", "Database/Company1/WEC1/WEC11/WEC11_description.txt", "Absent", "Absent", "Database/Company1/WEC1/WEC11/WaveTank/1_WaveTank/WEC11_1_description.txt", "Absent", "Absent", "Absent", "Database/Company1/WEC1/WEC11/WaveTank/2_WaveTank/WEC11_2_description.txt", "Absent", "Absent", "Absent", "Database/Company1/WEC1/WEC12/WEC12_description.txt", "Absent", "Database/Company1/WEC1/WEC12/DryTest/1_DryTest/WEC12_1_description.txt", "Absent", "Absent", "Absent", "Database/Company1/WEC2/WEC2_description.txt", "Database/Company1/WEC2/WEC20/WEC20_description.txt", "Database/Company1/WEC2/WEC21/WEC21_description.txt", "Absent", "Database/Company1/WEC2/WEC21/DryTest/1_DryTest/WEC21_1_description.txt Database/Company1/WEC2/WEC21/DryTest/1_DryTest/WEC21_2_description.txt", "Absent", "Absent", "Absent", "Absent", "Database/Company1/WEC2/WEC21/WaveTank/1_WaveTank/WEC21_1_description.txt", "Absent", "Absent", "Absent", "Database/Company1/WEC2/WEC22/WEC22_description.txt", "Absent", "Database/Company1/WEC2/WEC22/WaveTank/1_WaveTank/WEC22_1_description.txt", "Absent", "Absent", "Absent", "Database/Company2/Company2_1_description.txt", "Database/Company2/WEC1/WEC1_description.txt", "Database/Company2/WEC1/WEC10/WEC10_description.txt", "Database/Company2/WEC2/WEC2_description.txt", "Database/Company2/WEC2/WEC20/WEC20_description.txt", "Database/Company2/WEC2/WEC21/WEC21_description.txt", "Database/Company2/WEC3/WEC3_description.txt", "Database/Company2/WEC3/WEC30/WEC30_description.txt", "Database/Company2/WEC3/WEC31/WEC31_description.txt", "Database/Company2/WEC4/WEC4_description.txt", "Database/Company2/WEC4/WEC40/WEC40_description.txt", "Database/Company2/WEC4/WEC41/WEC41_description.txt", "Database/Company2/WEC4/WEC42/WEC42_description.txt", "Absent", "Database/Company2/WEC4/WEC42/DryTest/1_DryTest/WEC42_1_description.txt", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Absent", "Database/NonCompanyRelated/NonCompanyRelated_1_description.txt", "Database/NonCompanyRelated/Cylinder/Cylinder_description.txt", "Database/NonCompanyRelated/Cylinder/Cylinder0/Cylinder0_description.txt", "Absent", "Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest/Cylinder0_1_description.txt Database/NonCompanyRelated/Cylinder/Cylinder0/DryTest/1_DryTest/Cylinder0_2_description.txt", "Absent", "Absent", "Absent", "Database/NonCompanyRelated/Cylinder/Cylinder1/Cylinder1_description.txt", "Absent", "Database/NonCompanyRelated/Cylinder/Cylinder1/WaveTank/1_WaveTank/Cylinder1_1_description.txt", "Absent", "Absent", "Absent", "Database/Weptos/Weptos_description.txt", "Database/Weptos/WeptosWEC/WeptosWEC_description.txt", "Database/Weptos/WeptosWEC/WeptosWEC0/WeptosWEC0_description.txt", "Database/Weptos/WeptosWEC/WeptosWEC1/WeptosWEC1_description.txt", "Absent", "Database/Weptos/WeptosWEC/WeptosWEC1/DryTest/1_DryTest/WeptosWEC1_1_description.txt", "Absent", "Absent", "Absent", "Absent"]
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
		