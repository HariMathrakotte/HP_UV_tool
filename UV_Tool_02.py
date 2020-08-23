import maya.cmds as cmds

# basic PlanarProjection, AutoSeam and Unfold
def basicUnfold(args):
    hpSelection = cmds.ls(sl = True)
    cmds.polyPlanarProjection(hpSelection, ch = 1, md = "x")
    cmds.u3dAutoSeam(hpSelection, s = 0, p = True)
    cmds.u3dUnfold(hpSelection, bi = True, ite = 20, ms = 1024, p = True, tf = True)
    cmds.u3dLayout(hpSelection, res = 256, rot = 2, spc = 0.01, mar = 0.01, box = (0,1,0,1))
    cmds.delete(ch = True)

# u3D Unfold
def cleanUnfold(args):
    hpSelection = cmds.ls(sl = True)
    cmds.u3dUnfold(hpSelection, bi = True, ite = 20, ms = 1024, p = True, tf = True)
    cmds.u3dLayout(hpSelection, res = 256, rot = 2, spc = 0.01, mar = 0.01, box = (0,1,0,1))
    cmds.delete(ch = True)

# clean Layout
def finalLayout(args):
    hpSelection = cmds.ls(sl=True)
    cmds.u3dLayout(hpSelection, res=256, rot=2, scl=1, spc=0.01, mar=0.01, box=(0,1,0,1))
    cmds.delete(ch=True)

def showUI():
    UV_WIN = "UV_Tool"
    if cmds.window(UV_WIN, query=True, exists=True):
        cmds.deleteUI(UV_WIN)

    cmds.window(UV_WIN, title="HP_UV_Tool_v01", resizeToFitChildren = True)

    cmds.columnLayout()
    cmds.separator(style="none", height=20)
    cmds.button(label="Basic_Unfold", width=300, command=basicUnfold)
    cmds.separator(style="none", height=10)
    cmds.button(label="Clean_Unfold", width=300, command=cleanUnfold)
    cmds.separator(style="none", height=10)
    cmds.button(label="Final_Layout", width=300, command=finalLayout)
    cmds.separator(style="none", height=20)
    cmds.showWindow(UV_WIN)
showUI()