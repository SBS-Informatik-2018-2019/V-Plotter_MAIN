#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import linetracer as LT

#VARIABLES#######################################
FILE="file.svg" #name der standart datei
punkteX = [0,0] # do not edit points
punkteY = [0,0] # do not edit points
#END VARIABLES####################################

# oder mit liste
liste = list(range(3,7)) # [3,4,5,6]
liste.append(8)          # [3,4,5,6,8]
liste.insert(4,7)        # [3,4,5,6,7,8]
liste.extend([2,4,6])    # [3,4,5,6,7,8,2,4,6]
print(liste.count(6))    # 2; 2 mal ist '6' in liste
liste.remove(6)          # [3,4,5,7,8,2,4,6]
print(liste.count(6))    # 1; 1 mal ist '6' in liste
print(liste.index(4))    # 1; erste '4' ist bei Index 1
liste.sort()             # [2,3,4,4,5,6,7,8]
liste.reverse()          # [8,7,6,5,4,4,3,2]
print(liste.pop())       # 2; [8,7,6,5,4,4,3]
#

def svgLesen():
    svgRootElement = ET.parse(FILE).getroot()
    polylineElement = svgRootElement.find("{http://www.w3.org/2000/svg}path")
    string = polylineElement.get('d')
    print("-> PATH: " + string)
    return

def punkteSchreiben():
    global punkteX
    global punkteY
    return

def scalieren():
    return



def machePolyline(file):
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    svgRootElement = ET.parse(file).getroot()
    polylineElement = svgRootElement.find("{http://www.w3.org/2000/svg}polyline")
    points = polylineElement.get('points')
    #print("->Polyline: points=(" + points + ")")
    points = points + " "
    points = points.lstrip()
    index = points.index(',')
    x1 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    points = points[index+1:len(points)]
    points = points.lstrip()
    index = points.index(' ')
    y1 = float(points[0:index])

    points = points[index+1:len(points)]
    points = points.lstrip()
    startPosX = x1
    startPosY = y1
    #print("~~~~~~~~~~~STARTX="+str(startPosX))
    #print("~~~~~~~~~~~STARTY="+str(startPosY))
    actMotorLaengeA = getLaengeA(startPosX, startPosY)
    actMotorLaengeB = getLaengeB(startPosX, startPosY)
    #print("~~~~~~~~~~~STARTMLA="+str(actMotorLaengeA))
    #print("~~~~~~~~~~~STARTMLB="+str(actMotorLaengeB))
    while len(points) != 0:
        points = points.lstrip()
        index = points.index(',')
        x2 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if(x2<=0):
            x2 = 1
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        y2 = float(points[0:index])
        if(y2<=0):
            y2 = 1
        points = points[index+1:len(points)]
        points = points.lstrip()
        if(LT.macheGerade(x1, y1, x2, y2)==1):
            return 1
        x1 = x2
        y1 = y2
        continue
    return