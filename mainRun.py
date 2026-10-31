from CoreFunctions.CreationFoldersPath import CreationFoldersPath
from CoreFunctions.CreationMainCreation import CreationMainCreation
import json


print("\n")
creationfolderspath=CreationFoldersPath()	
from DynamicFunctions.FoldersPath import FoldersPath

previous_folderspath=FoldersPath()
new_folderspath=FoldersPath()

creationmaincreation=CreationMainCreation(previous_folderspath,new_folderspath)
#creationmaincreation.redoCreationWECClasses()
#print(creationmaincreation)

from DynamicFunctions.MainCreation import MainCreation
mainCreation = MainCreation()

print("\n============================ ELSE ==========================================\n")


#print(mainCreation)
print(json.dumps(mainCreation.getAllOrganisations(),indent=10))

print(json.dumps(mainCreation.getAllWECs(),indent=10))
#print(json.dumps(mainCreation.getAllWECChildren(),indent=10))
#print(json.dumps(mainCreation.getAllWECChildrenObjects(),indent=10))
print("\n============================ ELSE ==========================================\n")

#print(mainCreation.wec11_1_description)


print("\n============================ ELSE Interface ==========================================\n")

#local import
if 0:  # Legacy integration is incomplete; use db_interface/run.py for the working catalogue
    from db_interface.interface.user_interface import MainInterface
	
    mainInterface = MainInterface(mainCreation)
    mainInterface.make_interface()

    mainInterface.run_interface()