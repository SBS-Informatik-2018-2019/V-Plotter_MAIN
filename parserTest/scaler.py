

#VARIABLES#######################################

STARTX = 700 # Obere linke Ecke des Zeichenbereichs
STARTY = 700 # Obere linke Ecke des Zeichenbereichs

groesseX = 600 # Größe des Zeichenbereichs
groesseY = 600 # Größe des Zeichenbereichs
#END VARIABLES####################################
if __name__ == "__main__":
    scale()
    pass

def scale(pointsX, pointsY, cmds):
    #fix top left
    sortpointsX = list(pointsX)
    sortpointsY = list(pointsY)
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
    sortpointsX.sort().reverse()
    sortpointsY.sort().reverse()
    maxx = sortpointsX[0]
    maxy = sortpointsY[0]
    scalerX = groesseX / maxx
    scalerY = groesseY / maxy
    scaler = 0
    if(scalerX > scalerY):
        scaler = scalerY
    else:
        scaler = scalerY
    for i in range(len(pointsX)):
        pointsX[i] = pointsX[i] * scaler
        pointsY[i] = pointsY[i] * scaler
