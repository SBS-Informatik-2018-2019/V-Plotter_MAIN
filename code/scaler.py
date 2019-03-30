#-*- coding: utf-8 -*-
import linetracer as LT

#VARIABLES#######################################
STARTX = 800 # Obere linke Ecke des Zeichenbereichs
STARTY = 800 # Obere linke Ecke des Zeichenbereichs
groesseX = 600 # Größe des Zeichenbereichs
groesseY = 600 # Größe des Zeichenbereichs
#END VARIABLES####################################

#TODO: kommentar
def initScale():
    LT.initPosition(STARTX, STARTY)
    
#TODO: kommentar
def scale(pointsX, pointsY, cmds):
    print(pointsX)
    print(pointsY)
    print(cmds)
    #fix top left
    sortpointsX = pointsX[:]
    sortpointsY = pointsY[:]
    sortpointsX.sort()
    sortpointsY.sort()
    minx = sortpointsX[0]
    miny = sortpointsY[0]
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] - minx
        pointsY[i] = pointsY[i] - miny
    #scale to max
    sortpointsX = list(pointsX)
    sortpointsY = list(pointsY)
    sortpointsX.sort()
    sortpointsX.reverse()
    sortpointsY.sort()
    sortpointsY.reverse()
    maxx = sortpointsX[0]
    if(maxx == 0):
        maxx = 1
    maxy = sortpointsY[0]
    if(maxx == 0):
        scalerX = 99999999999999
    else:
        scalerX = groesseX / maxx
    if(maxy == 0):
        scalerY = 99999999999999
    else:
        scalerY = groesseY / maxy
    scaler = 0
    if(scalerX > scalerY):
        scaler = scalerY
    else:
        scaler = scalerX
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] * scaler
        pointsY[i] = pointsY[i] * scaler
    #pushto drawarea
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] + STARTX
        pointsY[i] = pointsY[i] + STARTY
    print("-->Scaled")
    print(pointsX)
    print(pointsY)
    print(cmds)
    #print
    for i in range(len(pointsX)):
        if(LT.fahre(pointsX[i], pointsY[i], cmds[i]) == "stop"):
            return "stop"
    return

