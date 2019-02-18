#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
#import linetracer as LT
#import plotterio as IO

#VARIABLES#######################################
FILE="file.svg" #name der standart datei


nameSpace={'svgNs':'http://www.w3.org/2000/svg'}

punkteX = [0,0] # do not edit points
punkteY = [0,0] # do not edit points
#END VARIABLES####################################

def parse(file):
    svgLesen()
    return

# Start des Einlesens einer svg-Datei
def svgLesen():
    svgRootElement = ET.parse(FILE).getroot()
    if (svgRootElement.find("svgNs:path", nameSpace) != None):
        pathElement = svgRootElement.find("svgNs:path", nameSpace)
        path = pathElement.get('d')
        print("-> PATH: " + path)
        machePath(path)
    elif (svgRootElement.find("svgNs:polyline", nameSpace) != None):
        polylineElement = svgRootElement.find("svgNs:polyline", nameSpace)
        points = polylineElement.get('points')
        print("-> Polyline: " + points)
        machePolyline(machePolylineListe(points))
    return

# Erstellen einer linearen Liste aus den Punkten von Geraden
def punkteSchreiben(points):
    # Schleife über die gesamte Länge des Strings points
    while len(points) != 0:
        # separate x coord from points
        points = points.lstrip()
        index = points.index(',')
        x = float(points[0:index])
        if(x<=0):
            x = 1
        # separate y coord from points
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        y = float(points[0:index])
        if(y<=0):
            y = 1
        
        points = points[index+1:len(points)]
        points = points.lstrip()
#        if(LT.macheGerade(x2, y2)=="stop"):
#            return "stop"
        # Vormerken der Position des Plotters?
        continue
    skalieren()
    return

def convertCurve(curveCoord):
    pass

# Skalieren der Größe auf eine vorbestimmtes Feld des Plotters
def skalieren():
    return

def machePath(path_elements):
    #Startposition
    index = indexNaechsterBuchstabe(path_elements[1: len(path_elements)])
    pos = path_elements[1: index]
    index = path_elements.index(',')
    x1 = pos[0: index-1]
    y1 = pos[index: len(pos)]
    print("StartX: " + x1 + " StartY: " + y1)

    while len(path_elements) != 0:
        if(path_elements[0] == "M"):
            print("MOVETO - Bitte entfernen sie den Stift!")
            path_elements = path_elements[1: len(path_elements)]
#           plotterio.aufOKwarten()
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]

        elif(path_elements[0] == "L"):
            print("LINETO - Zeichnen einer Geraden")
            path_elements = path_elements[1: len(path_elements)]
#           plotterio.aufOKwarten()
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]


def indexNaechsterBuchstabe(string):
    index = len(string)
    if index > string.find('M', 0, index) and string.find('M', 0, index) > 0:
        index = string.find('M', 0, index)
    if index > string.find('L', 0, index) and string.find('L', 0, index) > 0:
        index = string.find('L', 0, index)
    elif index > string.find('C', 0, index) and string.find('C', 0, index) > 0:
        index = string.find('C', 0, index)
    elif index > string.find('Z', 0, index) and string.find('Z', 0, index) > 0:
        index = string.find('Z', 0, index)
    return index


# schrittweise Ansteuern der Koordinaten eine Polylineliste
def machePolylineListe(points):
    points = points + " "
    polylinePointsX = list()
    polylinePointsY = list()
    while len(points) != 0:
        # separate xpolynext and ypolynext coord from points
        points = points.lstrip()
        index = points.index(',')
        polyNextX = float(points[0:index])
        polylinePointsX.append(polyNextX)
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        polyNextY = float(points[0:index])
        polylinePointsY.append(polyNextY)
        points = points[index+1:len(points)]
        points = points.lstrip()
    #goto scaler
    return



# schrittweise Ansteuern der Koordiaten einer PolylineListe
def machePolyline(polylineListe):
    polylineListe.reverse()
    print("MOVETO - Bitte entfernen sie den Stift!")
    # IO.aufOKwarten()
    # if(LT.macheGerade(polylineListe.pop(), polylineListe.pop())=="stop"):
    #       return "stop"
    (str(polylineListe.pop()))
    (str(polylineListe.pop()))
    print("LINE - Bitte legen sie den Stift ein!")
     # IO.aufOKwarten()
                    #LT.initPosition(STARTX,STARTY) Paul Startkoordinaten an Motor übergeben
                    # --> nach main

    # Schleife über die gesamte Liste
    while(len(polylineListe) > 0):
        (str(polylineListe.pop()))
        (str(polylineListe.pop()))
#        if(LT.macheGerade(polylineListe.pop(), polylineListe.pop())=="stop"):
#            return "stop"
        continue
    return