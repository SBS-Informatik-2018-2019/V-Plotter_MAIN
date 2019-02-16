#-*- coding: utf-8 -*-
import math
import time
import motortreiber as MOTOR

#VARIABLES#######################################
minSchritt = 1 # auflösung der greraden
L = 2030 # abstand der motoren in schritten
startPosX = 0 # do not edit startpunkt
startPosY = 0 # do not edit startpunkt
#END VARIABLES####################################

#getters & setters
def getL():
    return L
#END getters & setters

def getLaengeA(x, y):
    return math.sqrt((x*x)+(y*y))

def getLaengeB(x, y):
    return math.sqrt(((L-x)*(L-x))+(y*y))

def beta (a, b):
    return math.acos (-(b * b - a * a - L * L) / (2 * a * L))

def getPosX (a, b):
    return math.cos(beta(a, b))*a

def getPosY (a, b):
    return math.sin(beta(a, b))*a

def initPosition(initX, initY):
    a = getLaengeA(initX, initY)
    b = getLaengeB(initX, initY)
    MOTOR.initLaenge(a, b)
    return

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