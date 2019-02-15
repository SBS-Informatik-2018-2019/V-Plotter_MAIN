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


def macheGerade(x1, y1, x2, y2):
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    global actPosX
    global actPosY
    a1 = getLaengeA(x1, y1)
    b1 = getLaengeB(x1, y1)
    a2 = getLaengeA(x2, y2)
    b2 = getLaengeB(x2, y2)
    wegA = a2-a1
    wegB = b2-b1
    wegX = x2-x1
    wegY = y2-y1
   
    if(MOTOR.setLaenge(a1, b1)=="stop"):
        return 1
    schritte = 0
    if abs(wegY) < abs(wegX):
        schritte = int(round(abs(wegX)/minSchritt))
    else:
        schritte = int(round(abs(wegY)/minSchritt))
    for i in range(schritte):
        x = (x1 + i*wegX/schritte)
        y = (y1 + i*wegY/schritte)
        a = round(getLaengeA(x, y))
        b = round(getLaengeB(x, y))
        if(MOTOR.setLaenge(a, b)==1):
            return 1
        continue
    x = x2
    y = y2
    a = round(getLaengeA(x, y))
    b = round(getLaengeB(x, y))
    if(MOTOR.setLaenge(a, b)=="stop"):
        return "stop"
    return 0