#-*- coding: utf-8 -*-
import math
import time

#VARIABLES
minSchritt = 1 # auflösung der greraden
L = 2030 # abstand der motoren in schritten
FILE = "file_scharf.svg" #name der datei
READY = 2 #UI pin
ACTIVE = 3 #UI pin
START = 4 #UI pin
STOP = 17 #UI pin

startPosX = 0 # do not edit startpunkt
startPosY = 0 # do not edit startpunkt
actMotorLaengeA = 0 # do not edit actML
actMotorLaengeB = 0 # do not edit actML
actPosX = 0 # do not edit actPos
actPosY = 0 # do not edit actPos
#END VARIABLES


def getLaengeA(x, y):
    return math.sqrt((x*x)+(y*y))
 
def getLaengeB(x, y):
    return math.sqrt(((L-x)*(L-x))+(y*y))
    
def beta (a, b):
    res = math.acos (-(b * b - a * a - L * L) / (2 * a * L))
    return res
    
def getPosX (a, b):
    res = math.cos(beta(a, b))*a
    return res
    
def getPosY (a, b):
    res = math.sin(beta(a, b))*a
    return res
    

    

def macheGerade(x1, y1, x2, y2):
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    a1 = getLaengeA(x1, y1)
    b1 = getLaengeB(x1, y1)
    a2 = getLaengeA(x2, y2)
    b2 = getLaengeB(x2, y2)
    wegA = a2-a1
    wegB = b2-b1
    wegX = x2-x1
    wegY = y2-y1
    #print(" ->neue Gerade: from x,y=(" + str(x1) + "," + str(y1) + ") -> to x,y=(" + str(x2)+ "," + str(y2) + ")                                    ")
    if(motorSetLaenge(a1, b1)==1):
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
        rx = getPosX(a, b)
        ry = getPosY(a, b)
        #print("   ->Pos " +str(i) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + ")")
        if(motorSetLaenge(a, b)==1):
            return 1
        continue
    x = x2
    y = y2
    a = round(getLaengeA(x, y))
    b = round(getLaengeB(x, y))
    rx = getPosX(a, b)
    ry = getPosY(a, b)   
    #print("   ->Pos " +str(schritte) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + "): -fertig")
    if(motorSetLaenge(a, b)==1):
        return 1
    return 0