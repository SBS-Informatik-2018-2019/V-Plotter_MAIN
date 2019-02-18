#-*- coding: utf-8 -*-
import math
import time
import motortreiber as MOTOR
import plotterio as IO

#VARIABLES#######################################
minSchritt = 1 # auflösung der greraden
L = 2030 # abstand der motoren in schritten
actCMD = "l" # do not edit cmd
startPosX = 0 # do not edit startpunkt
startPosY = 0 # do not edit startpunkt
#END VARIABLES####################################

#getters & setters
def getL():
    return L
#END getters & setters

# gib die Seitenlänge der linken Motorschnur bei der Koordinate(x,y) zurück
def getLaengeA(x, y):
    return math.sqrt((x*x)+(y*y))

# gib die Seitenlänge der rechten Motorschnur bei der Koordinate(x,y) zurück
def getLaengeB(x, y):
    return math.sqrt(((L-x)*(L-x))+(y*y))

def beta (a, b):
    return math.acos (-(b * b - a * a - L * L) / (2 * a * L))

# gib die x-Koordinate, wenn die linke Schnur a und die rechte b lang ist, zurück
def getPosX (a, b):
    return math.cos(beta(a, b))*a

# gib die y-Koordinate, wenn die linke Schnur a und die rechte b lang ist, zurück
def getPosY (a, b):
    return math.sin(beta(a, b))*a

# gibt dem Motor seine Anfangsseillängen, zu denen der sich zu Beginn befindet
def initPosition(initX, initY):
    a = getLaengeA(initX, initY)
    b = getLaengeB(initX, initY)
    MOTOR.initLaenge(a, b)
    return

#fährt den Schlitten in einer (fast) graden Liene zu Position (x,y)
def macheGerade(toX, toY):
    fromA = MOTOR.getActMotorLaengeA()
    fromB = MOTOR.getActMotorLaengeB()
    fromX = getPosX(fromA, fromB)
    fromY = getPosY(fromA, fromB)
    toA = getLaengeA(toX, toY)
    toB = getLaengeB(toX, toY)
    wegX = toX - fromX
    wegY = toY - fromY
    schritte = 0
    if abs(wegY) < abs(wegX):
        schritte = int(round(abs(wegX)/minSchritt))
    else:
        schritte = int(round(abs(wegY)/minSchritt))
    for i in range(schritte):
        x = (fromX + i*wegX/schritte)
        y = (fromY + i*wegY/schritte)
        a = getLaengeA(x, y)
        b = getLaengeB(x, y)
        if(MOTOR.setLaenge(a, b)=="stop"):
            return "stop"
        continue
    if(MOTOR.setLaenge(toA, toB)=="stop"):
        return "stop"
    return 0

# cmd = m [MOVETO] oder l [LINETO]
def fahre(toX, toY, cmd):
    if((actCMD == "l") and (cmd == "l")):
        if (macheGerade(toX, toY) == "stop"):
            return "stop"
    if((actCMD == "m") and (cmd == "m")):
        if (macheGerade(toX, toY) == "stop"):
            return "stop"
    if((actCMD == "l") and (cmd == "m")):
        print("STIFT entfernen!")
        IO.aufOKWarten()
        if (macheGerade(toX, toY) == "stop"):
            return "stop"
    if((actCMD == "m") and (cmd == "l")):
        print("STIFT einlegen!")
        IO.aufOKWarten()
        if (macheGerade(toX, toY) == "stop"):
            return "stop"
    return