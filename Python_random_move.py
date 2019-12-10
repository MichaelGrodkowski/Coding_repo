import maya.cmds as cmds
import random as rand 

result = cmds.polyCube(w=1, h=1, d=1, name='PCubes#') 
transformName = result[0]
for i in range (0, 20):
    instanceResult = cmds.instance( transformName, name=transformName + '_instance' )

def DoMove(object, attr):
    randValue = rand.uniform(-10, 10)
    attrValue = cmds.getAttr(object + "." + attr)
    cmds.setAttr(object + "." + attr, randValue + attrValue)
    print object
    
def RandomMove():
    c = cmds.ls(selection = True)

    for cur in c:
        DoMove(cur, "tx")
        DoMove(cur, "ty")
        DoMove(cur, "tz")
        
RandomMove()



def RandomMove(maxX, minX, maxY, minY, minZ, maxZ, count):
    cmds.listObj = cmds.ls(selection=True)
    copies = copies[0]

    randx = rand.uniform(maxX, minX)
    randy = rand.uniform(maxY, minY)
    randz = rand.uniform(maxZ, minZ)

    for iterator in range(0, copies):
        copies = cmds.duplicate(cmds.listObj[0])
        randx = rand.uniform(maxX, minX)
        randy = rand.uniform(maxY, minY)
        randz = rand.uniform(maxZ, minZ)

RandomMove(1, 20, 1, 3, 40, 20, 30)



import maya.cmds as cmds
import random as rand
def randoAndDupMove(maxX, minX, maxY, minY, minZ, maxZ, count):
    cmds.listObj = [cmds.ls(selection=True)]

    randx = rand.uniform(maxX, minX)
    randy = rand.uniform(maxY, minY)
    randz = rand.uniform(maxZ, minZ)

    for i in range(0,count):
        copies = [0]
        #cmds.duplicate(cmds.listObj)
        dups = cmds.duplicate(cmds.listObj)

        randx = rand.uniform(maxX, minX)
        randy = rand.uniform(maxY, minY)
        randz = rand.uniform(maxZ, minZ)
        cmds.move(randx, randy, randz, copies[0])


randoAndDupMove(1, 2, 23, 4, 5, 6, 20)







