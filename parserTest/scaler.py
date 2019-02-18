

#VARIABLES#######################################

STARTX = 700 # Obere linke Ecke des Zeichenbereichs
STARTY = 700 # Obere linke Ecke des Zeichenbereichs

groesseX = 600 # Größe des Zeichenbereichs
groesseY = 600 # Größe des Zeichenbereichs
#END VARIABLES####################################


def scale(pointsX, pointsY, cmds):
    #fix top left
    sortpointsX = list(pointsX)
    sortpointsY = list(pointsY)
    sortpointsX.sort()
    sortpointsY.sort()
    minx = sortpointsX[0]
    miny = sortpointsX[0]
    for i in range(len(pointsX)):
        pointsX.[i] = pointsX.[i] - minx
        pointsY.[i] = pointsY.[i] - miny
    #scale to max x
    sortpointsX = list(pointsX)
    sortpointsY = list(pointsY)
    sortpointsX.sort().reverse()
    sortpointsY.sort().reverse()
    maxx = sortpointsX[0]
    maxy = sortpointsY[0]
    scalerX = groesseX / maxx
    scalerY = groesseY / maxx
    if(scalerX > scalerY):
        

    for i in range(len(pointsX)):
        pointsX.[i] = pointsX.[i] * scaler
        pointsY.[i] = pointsY.[i] * scaler
    scaler = groesseY / maxx
    for i in range(len(pointsX)):
        pointsX.[i] = pointsX.[i] * scaler
        pointsY.[i] = pointsY.[i] * scaler