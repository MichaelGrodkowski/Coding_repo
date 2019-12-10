import maya.cmds as cmds

def renameAllObjects(selection_name, amount_of_padding, selection_suffix):
    listObj = cmds.ls(selection=True) 

    
    for iterator,c in enumerate(listObj): #enumerate() counts through the list of listObj which is my selection.
       cmds.rename(c, selection_name + "_" + str(iterator + 1).zfill(amount_of_padding) +"_"+ selection_suffix )
        
renameAllObjects("Left_Chain" , 3 , "GEO" ) #.zfill is a python 3 command that allows for the padding with zeros.

