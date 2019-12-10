def centerLocator():
    cmds.listObj = cmds.ls(selection=True)
    bb = [0]

    if len(cmds.listObj) > 1:
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
        cmds.spaceLocator(p=(totalX, totalY, totalZ))
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
        cmds.spaceLocator(p=(totalX, totalY, totalZ))

centerLocator()
