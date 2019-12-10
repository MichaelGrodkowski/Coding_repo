'''
def controlSpawner():
    cmds.listObj = cmds.ls(selection=True)
    bb = [0]
    sels = cmds.listObj

    if len(cmds.listObj) > 1:
        for i in(sels):
            dups = [cmds.duplicate(cmds.listObj)]
            cmds.polyUnite(cmds.listObj)
            cmds.rename('polySurface1', 'dups')
            #cmds.delete('dups')
            bb = cmds.xform('dups',q=True, bb=True,ws=True)
            print bb
        
            xMin = bb[0]
            xMax = bb[3]
            yMin = bb[1]
            yMax = bb[4]
            zMin = bb[2]
            zMax = bb[5]
        
            totalX=0
            totalY=0 
            totalZ=0

            totalX = (xMin + xMax) / 2
            totalY = (yMin + yMax) / 2
            totalZ = (zMin + zMax) / 2
            cmds.circle(nr=(0, 0, 0), c=(totalX, totalY, totalZ))
            cmds.delete('dups', ch=True)
            cmds.delete('dups')
        
    else:
        cmds.listObj = cmds.ls(selection=True)   
        bb = cmds.xform(q=True, bb=True,ws=True)
        print bb
        
        xMin = bb[0]
        xMax = bb[3]
        yMin = bb[1]
        yMax = bb[4]
        zMin = bb[2]
        zMax = bb[5]
        
        totalX=0
        totalY=0 
        totalZ=0

        totalX = (xMin + xMax) / 2
        totalY = (yMin + yMax) / 2
        totalZ = (zMin + zMax) / 2
               
        xRot = cmds.getAttr(listObj, '.tx')
        yRot = 
        zRot = 
               
        
        cmds.circle(nr=(0, 0, 0) ,c=(totalX, totalY, totalZ))
        
controlSpawner()



import maya.cmds as cmds
def renameAndControl(selection_name, amount_of_padding, selection_suffix):
    listObj = cmds.ls(selection=True)
    bb = [0]
    
    for iterator, c in enumerate(listObj):  # enumerate() counts through the list of listObj which is my selection.
        cmds.rename(c, selection_name + "_" + str(iterator + 1).zfill(amount_of_padding) + "_" + selection_suffix)
        cmds.circle(c=(0,0,0))
        
        
'''

import maya.cmds as cmds        
        
def renameAndControl(selection_name, amount_of_padding, selection_suffix):
    sels = cmds.ls(selection=True)
    bb = [0]
    
    #attrValue = cmds.getAttr(sels + "." + attr)

    for iterator, c in enumerate(sels):  # enumerate() counts through the list of listObj which is my selection.
        cmds.rename(c, selection_name + "_" + str(iterator + 1).zfill(amount_of_padding) + "_" + selection_suffix)
        cmds.circle(n=('Left_chain'+ "_" + str(iterator + 1).zfill(amount_of_padding) + "_" + 'CTRL'))
        cmds.listObj = cmds.ls(selection=True)
        bb = [0]
        sels = cmds.listObj

             

renameAndControl("Left_Chain", 3, "GEO")

'''

def ctrl():
    cmds.listobj = cmds.ls(selection=True)
    sels = cmds.listobj

    for sel in sels:
        cmds.circle(,n=('CTRL'))
        cmds.matchTransform(circle, sels)


ctrl()






import maya.cmds as cmds

def contrl():
    mySel = cmds.ls(sl=True)[0]
    for i in mySel:
        dumbCluster = mySel
        clusPos = cmds.xform(dumbCluster, q=True, rp=True)
        cmds.xform(cmds.circle(),q, t=clusPos, ws = True)
        cmds.parent(w=True)
        cmds.delete(dumbCluster)
    
contrl()

'''
