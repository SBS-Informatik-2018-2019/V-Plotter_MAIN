#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

#VARIABLES#######################################
FILE="file.svg" #name der standart datei
STARTX = 800
STARTY = 800
punkteX = [0,0] # do not edit points
punkteY = [0,0] # do not edit points

groesseX = 10000 # Größe des Zeichenbereichs
groesseY = 10000

nameSpace={'svgNs':'http://www.w3.org/2000/svg'}
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

# by Niklas Start des Einlesens einer svg-Datei
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
        machePolyline(points)
    return

# by Paul erstellen einer linearen Liste mit allen Punkten
def punkteSchreiben():
    global punkteX
    global punkteY

    scalieren()
    return

#by Paul Skalieren der Größe auf eine vorbestimmtes Feld des Plotters
def scalieren():
    return



def machePath(path_elements):

    while len(path_elements) != 0:
        if(path_elements[0] == "M"):
            print("MOVETO - Bitte entfernen sie den Stift!")
            path_elements = path_elements[1: len(path_elements)-1]
#           plotterio.aufOKwarten()
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])

        elif(path_elements[0] == "L"):
            print("LINETO - Zeichnen einer Geraden")
            path_elements = path_elements[1: len(path_elements)-1]
#           plotterio.aufOKwarten()
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])

#        path_elements.find(0)
#        path_elements.index("M")

def indexNaechsterBuchstabe(string):
    index = len(string)
    if index > string.find('M', 0, index):
        index = string.find('M', 0, index)
    if index > string.find('L', 0, index):
        index = string.find('L', 0, index)
    elif index > string.find('C', 0, index):
        index = string.find('C', 0, index)
    elif index > string.find('Z', 0, index):
        index = string.find('Z', 0, index)
    return index

# by Paul schrittweise Ansteuern der Koordinaten eine Polyline
def machePolyline(points):

    # separate x1 coord from points
    points = points + " "
    points = points.lstrip()
    index = points.index(',')
    x1 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # separate y1 coord from points
    points = points[index+1:len(points)]
    points = points.lstrip()
    index = points.index(' ')
    y1 = float(points[0:index])

    points = points[index+1:len(points)]
    points = points.lstrip()

    #LT.initPosition(STARTX,STARTY) Paul Startkoordinaten an Motor übergeben

    # Schleife über die gesamte Länge des Strings points (Nutzen einer Liste)
    while len(points) != 0:
        # separate x2 coord from points
        points = points.lstrip()
        index = points.index(',')
        x2 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if(x2<=0):
            x2 = 1
        # separate y2 coord from points
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        y2 = float(points[0:index])
        if(y2<=0):
            y2 = 1
        
        points = points[index+1:len(points)]
        points = points.lstrip()
#        if(LT.macheGerade(x2, y2)=="stop"):
#            return "stop"
        # Vormerken der Position des Plotters? 
        x1 = x2
        y1 = y2
        continue
    return

def parse(file):
    svgLesen()
    return