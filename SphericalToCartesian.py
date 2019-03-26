'''
==========================================
 Title:       SphericalToCartesian.py
 Author:      Yannis Ioannidis
 Date:        26 Mar 2019
 Description: Simple spherical to cartesian coordinates conversion and use
=============
'''

import maya.cmds as cmds
import math as math
import time


cmds.file( f=True, new=True )

#shader helper functions
def createMaterial(name,colour,type):
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name + 'SG' )
    cmds.shadingNode( type, asShader=True, name=name )
    cmds.setAttr( name+".color", colour[0], colour[1], colour[2], type='double3')
    cmds.connectAttr(name+".outColor", name+"SG.surfaceShader")

def assignMaterial (name, object):
    cmds.sets(object, edit=True, forceElement=name+'SG')


def assignNewMaterial( name, colour, type, object):
    createMaterial (name, colour, type)
    assignMaterial (name, object)

theta=45 * math.pi/180
phi=10* math.pi/180
#psi=0 * math.pi/180

#..every 5 degrees (incremental phi spherical angle) 
maxJ=90
for j in range(10, maxJ):
    if (j%5==0):
        phi= j * math.pi/180       
        #.. every 45 degrees (incremental thta spherical angle) 
        for i in range(360):#          
            if (i%45==0):
                
                theta=i * math.pi/180
        
                #create a cylinder & and colour it appropriately
                #https://mathinsight.org/spherical_coordinates
                            
                #direction axis
                dirAxis = math.sin(phi)*math.sin(theta), math.cos(phi), math.sin(phi)*math.cos(theta)
                cyl = cmds.polyCylinder(name = 'ball' + str(i)+"_"+str(j),axis=[ dirAxis[0], dirAxis[1], dirAxis[2] ], radius=0.05)
              
                #colour of each theta row
                print j/float(maxJ)
                assignNewMaterial(  'ballShader' + str(i)+"_"+str(j), ( j/float(maxJ), 1-(j/float(maxJ)) ,0), 'blinn', 'ball' + str(i)+"_"+str(j) )
        
                #time.sleep(0.5)
                #move it this much along its direction axis (object space translation)
                cmds.move( dirAxis[0], dirAxis[1], dirAxis[2] )
                cmds.refresh()
                #time.sleep(0.1)
            
            
            
        