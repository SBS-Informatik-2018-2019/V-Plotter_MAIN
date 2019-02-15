#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import linetracer as LT
import modulefinder as MOTOR

#VARIABLES#######################################
FILE="file.svg" #name der standart datei
punkteX = [0,0] # do not edit points
punkteY = [0,0] # do not edit points
#END VARIABLES####################################

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