#-*- coding: utf-8 -*-
import linetracer as LT

#VARIABLES#######################################
STARTX = 800 # Obere linke Ecke des Zeichenbereichs
STARTY = 800 # Obere linke Ecke des Zeichenbereichs
groesseX = 600 # Größe des Zeichenbereichs
groesseY = 600 # Größe des Zeichenbereichs
#END VARIABLES####################################


# gib dem Linetracer (LT) die Startkoordinaten
def initScale():
    LT.initPosition(STARTX, STARTY)
    
# Scaliert auf die maximale Größe und verschiebt in dem Zeichenbereich
def scale(pointsX, pointsY, cmds):
    # die kleinsten Koordinaten werden abgezoden -> das Bild rückt nach oben links
    sortpointsX = pointsX[:]
    sortpointsY = pointsY[:]
    sortpointsX.sort()
    sortpointsY.sort()
    minx = sortpointsX[0]
    miny = sortpointsY[0]
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] - minx
        pointsY[i] = pointsY[i] - miny
    # finde die größten x und y Koordianten und berechne deren Scalierungsfaktor
    sortpointsX = list(pointsX)
    sortpointsY = list(pointsY)
    sortpointsX.sort()
    sortpointsX.reverse()
    sortpointsY.sort()
    sortpointsY.reverse()
    maxx = sortpointsX[0]
    maxy = sortpointsY[0]
    if(maxx == 0):
        scalerX = 9.9e20 
    else:
        scalerX = groesseX / maxx
    if(maxy == 0):
        scalerY = 9.9e20
    else:
        scalerY = groesseY / maxy
    scaler = 0
    # der kleinere Scaler wird genommen damit das Bild nicht über den Rand hinaus geht
    if(scalerX > scalerY):
        scaler = scalerY
    else:
        scaler = scalerX
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] * scaler
        pointsY[i] = pointsY[i] * scaler
    # das Bild wird in den Zeichenbereich geschoben
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] + STARTX
        pointsY[i] = pointsY[i] + STARTY
    # die einzelenen Koordinaten werden mit Lienen abgefahren
    for i in range(len(pointsX)):
        if(LT.fahre(pointsX[i], pointsY[i], cmds[i]) == "stop"):
            return "stop"
    return "fertig"

