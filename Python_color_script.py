import maya.cmds as cmds


def colorControl(self, colorname):
    sels = cmds.ls(sl=True)

    if colorname == 'Grey':
        color = 1
    elif colorname == 'Black':
        color = 2
    elif colorname == 'Dark Grey':
        color = 3
    elif colorname == 'Light Grey':
        color = 4
    elif colorname == 'Dark Red':
        color = 5
    elif colorname == 'Dark Blue':
        color = 6
    elif colorname == 'Blue':
        color = 7
    elif colorname == 'Dark Green':
        color = 8
    elif colorname == 'Dark Purple':
        color = 9
    elif colorname == 'Pink':
        color = 10
    elif colorname == 'Brown':
        color = 11
    elif colorname == 'Dark Brown':
        color = 12
    elif colorname == 'Red':
        color = 13
    elif colorname == 'Green':
        color = 14
    elif colorname == 'Navy':
        color = 15

    else:
        color = 5

    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)

        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, color)


colorControl('blue')