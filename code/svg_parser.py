#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import scaler as SCALER

#VARIABLES#######################################
FILE="file.svg" #name der standart datei
nameSpace={'svgNs':'http://www.w3.org/2000/svg'}

punkteX = list()
punkteY = list()
punkteCmds = list()

startZx = 0
startZy = 0
#END VARIABLES####################################

# nimmt eine Datei an, um angegebene Datei zu drucken
def parse(file):
    svgLesen(file)
    return

# druckt Standartdatei
def parse_standart():
    global FILE
    svgLesen(FILE)
    return

# Start des Einlesens einer svg-Datei
def svgLesen(file):
    svgRootElement = ET.parse(file).getroot()
    # Einlesen eines Path
    if (svgRootElement.find("svgNs:path", nameSpace) != None):
        pathElement = svgRootElement.find("svgNs:path", nameSpace)
        path = pathElement.get('d')
        print("-> PATH: " + path)
        machePath(path)
    # Anders wird eine Polyline eingelesen
    elif (svgRootElement.find("svgNs:polyline", nameSpace) != None):
        polylineElement = svgRootElement.find("svgNs:polyline", nameSpace)
        points = polylineElement.get('points')
        print("-> Polyline: " + points)
        machePolylineListe(points)
    return

# Fallunterscheidung nach den verschiedenen Befehlen in einem Path
def machePath(path_elements):
    while len(path_elements) != 0:
        path_elements = path_elements.lstrip()

        # ein Moveto bewegt nur den Plotter
        if(path_elements[0] == "M"):
            print("MOVETO - Bitte entfernen sie den Stift!")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            macheMove(path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]
            # der Startpunkt wird für das Z-Element gesetzt
            setzeStart(path_elements)   #!!!!!!!

        # eine einfache Lineto wird gezeichnet
        elif(path_elements[0] == "L"):
            print("LINETO - Zeichnen einer Geraden")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            macheLine(path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]
        
        # H besitzt als Argument die x-Position der Geraden
        elif(path_elements[0] == "H"):
            print("horLINETO - Zeichnen einer horizontalen Geraden")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            laufeCoords(punkteX[len(punkteX)-1], path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]

        # V besitzt als Argument die y-Position der Geraden
        elif(path_elements[0] == "V"):
            print("verLINETO - Zeichnen einer vertikalen Geraden")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            laufeCoords(path_elements[0: index], punkteY[len(punkteY)-1])
            path_elements = path_elements[index: len(path_elements)]

        # EIne Curve soll gezeichnet werden
        elif(path_elements[0] == "C"):
            print("CURVETO - Zeichnen einer Curve")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            macheLine(path_elements[0: index])  #Vereinfachung, Bezier-Bernstein-Approximation
            path_elements = path_elements[index: len(path_elements)]
        
        # eine Zeichnung wird zum Startpunkt zurückgeführt
        elif(path_elements[0] == "Z"):
            print("Zurücklauf - Zeichnen zurück zum Startpunkt")
            laufeZurueck()
            print(startZx + "," + startZy)
            path_elements = path_elements[1: len(path_elements)]
        
        # kein implementiertes Element/ unbekannter Character wird gelesen
        else:
            print("Kein bekanntes Element! - Zeichnen einer Gerade durch alle Argumente")
            path_elements = path_elements[1: len(path_elements)]
            path_elements = path_elements.lstrip()
            index = indexNaechsterBuchstabe(path_elements)
            print(path_elements[0: index])
            macheLine(path_elements[0: index])
            path_elements = path_elements[index: len(path_elements)]
    print("")
    machePathListe()

# speichert die Startposition, um diese für Z-Bewegungen zu nutzen
def setzeStart(string):
    if(string != ""):
        global startZx
        global startZy
        #Startposition
        index = indexNaechsterBuchstabe(string[1: len(string)])
        pos = string[1: index]
        index = string.index(',')
        startZx = pos[0: index-1]
        startZy = pos[index: len(pos)]
    return

# Bewegung zu zwei Koordinaten wird durchgeführt
def laufeCoords(x, y):
    punkteX.append(float(x))
    punkteY.append(float(y))
    punkteCmds.append('L')
    return

# zurückkehren zur Startposition, nachdem 
def laufeZurueck():
    punkteX.append(float(startZx))
    punkteY.append(float(startZy))
    punkteCmds.append('L')
    return

# der nächste Character wird gefunden
def indexNaechsterBuchstabe(string):
    index = len(string)
    string = string.lstrip()
    if index > string.find('M', 0, index) and string.find('M', 0, index) > 0:
        index = string.find('M', 0, index)
    if index > string.find('L', 0, index) and string.find('L', 0, index) > 0:
        index = string.find('L', 0, index)
    if index > string.find('H', 0, index) and string.find('H', 0, index) > 0:
        index = string.find('H', 0, index)
    if index > string.find('V', 0, index) and string.find('V', 0, index) > 0:
        index = string.find('V', 0, index)
    if index > string.find('C', 0, index) and string.find('C', 0, index) > 0:
        index = string.find('C', 0, index)
    if index > string.find('S', 0, index) and string.find('S', 0, index) > 0:
        index = string.find('S', 0, index)
    if index > string.find('Q', 0, index) and string.find('Q', 0, index) > 0:
        index = string.find('Q', 0, index)
    if index > string.find('T', 0, index) and string.find('T', 0, index) > 0:
        index = string.find('T', 0, index)
    if index > string.find('A', 0, index) and string.find('A', 0, index) > 0:
        index = string.find('A', 0, index)
    if index > string.find('Z', 0, index) and string.find('Z', 0, index) > 0:
        index = string.find('Z', 0, index)
    return index

# Hinzufügen der Punkte eines Moveto-Befehls zu den globalen Listen X,Y & Cmd
def macheMove(moveCoords):
    moveCoords = moveCoords + " "
    while len(moveCoords) != 0:
        moveCoords = moveCoords.lstrip()
        # X- Koordinate auslesen
        index = moveCoords.index(',')
        punkteX.append(float(moveCoords[0: index]))
        moveCoords = moveCoords[index+1: len(moveCoords)].lstrip()
        
        # Y-Koordinate auslesen
        index = moveCoords.index(' ')
        punkteY.append(float(moveCoords[0: index]))
        moveCoords = moveCoords[index+1: len(moveCoords)].lstrip()
        
        punkteCmds.append('M')
    return

# Hinzufügen der Punkte eines Lineto-Befehls zu den globalen Listen X,Y & Cmd
def macheLine(lineCoords):
    lineCoords = lineCoords + " "
    while len(lineCoords) != 0:
        lineCoords = lineCoords.lstrip()
        # X- Koordinate auslesen
        index = lineCoords.index(',')
        punkteX.append(float(lineCoords[0: index]))
        lineCoords = lineCoords[index+1: len(lineCoords)].lstrip()
        
        # Y-Koordinate auslesen
        index = lineCoords.index(' ')
        punkteY.append(float(lineCoords[0: index]))
        lineCoords = lineCoords[index+1: len(lineCoords)].lstrip()
        
        punkteCmds.append('L')
    return

# Hinzufügen der Punkte einer konvertierten Kurve zu den globalen Listen X,Y & Cmd
def macheCurve(curveCoord):
    
    return

# Übergeben der linearen Liste von Punkten an der scaler
def machePathListe():
    print(punkteX)
    print(punkteY)
    print(punkteCmds)
    SCALER.scale(punkteX, punkteY, punkteCmds)
    return


# Erstellen einer linearen Liste aus den Punkten einer Polyline
def machePolylineListe(points):
    points = points + " "
    polylinePointsX = list()
    polylinePointsY = list()
    polylineCMDs = list(("m"))
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
        polylineCMDs.append("l")
        continue
    polylineCMDs.pop()
    SCALER.scale(polylinePointsX, polylinePointsY, polylineCMDs)
    return