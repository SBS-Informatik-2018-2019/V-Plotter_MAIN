#-*- coding: utf-8 -*-
from __future__ import print_function
import math
import xml.etree.ElementTree as ElementTree
import time
import threading
import RPi.GPIO as GPIO

#####################################################
minSchritt = 1 # auflösung der greraden
L = 2030 # abstand der motoren in schritten , auch in svg ändern
FILE="file_scharf.svg" #name der standart datei
transformator = 1 #
READY=2 #UI pins
ACTIVE=3
START=4
STOP=17
startPosX = 0 # do not edit startpunkt
startPosY = 0 # do not edit startpunkt
actMotorLaengeA = 0 # do not edit startpunkt
actMotorLaengeB = 0 # do not edit startpunkt
#######################################################




GPIO.setup(ACTIVE,GPIO.OUT)
GPIO.setup(READY,GPIO.OUT)
GPIO.setup(STOP,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(START,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)
GPIO.output(E, False)
GPIO.output(F, False)
GPIO.output(G, False)
GPIO.output(H, False)

 


def machePolyline(file):
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    svgRootElement = ElementTree.parse(file).getroot()
    polylineElement = svgRootElement.find("{http://www.w3.org/2000/svg}polyline")
    points = polylineElement.get('points')
    #print("->Polyline: points=(" + points + ")")
    points = points + " "
    points = points.lstrip()
    index = points.index(',')
    x1 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if(x1<=0):
        x1 = 1
    if(x1>L):
        x1= L
    points = points[index+1:len(points)]
    points = points.lstrip()
    index = points.index(' ')
    y1 = float(points[0:index])
    if(y1<=0):
        y1 = 1
    points = points[index+1:len(points)]
    points = points.lstrip()
    startPosX = x1
    startPosY = y1
    #print("~~~~~~~~~~~STARTX="+str(startPosX))
    #print("~~~~~~~~~~~STARTY="+str(startPosY))
    actMotorLaengeA = getLaengeA(startPosX, startPosY)
    actMotorLaengeB = getLaengeB(startPosX, startPosY)
    #print("~~~~~~~~~~~STARTMLA="+str(actMotorLaengeA))
    #print("~~~~~~~~~~~STARTMLB="+str(actMotorLaengeB))
    while len(points) != 0:
        points = points.lstrip()
        index = points.index(',')
        x2 = float(points[0:index]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if(x2<=0):
            x2 = 1
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        y2 = float(points[0:index])
        if(y2<=0):
            y2 = 1
        points = points[index+1:len(points)]
        points = points.lstrip()
        if(macheGerade(x1, y1, x2, y2)==1):
            return 1
        x1 = x2
        y1 = y2
        continue
    return
    
def aufEingabeWarten():
    time.sleep(2.5)
    print("mit Taste -OK- bestätigen")
    no_input = True
    GPIO.output(READY, True)
    while(no_input):
        time.sleep(0.001)
        if (GPIO.input(START)==GPIO.HIGH):
            no_input = False
    GPIO.output(READY, False)
    print(">>>-OK-")
    return

def geheStartPos():
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    a = getLaengeA(startPosX, startPosY)
    b = getLaengeB(startPosX, startPosY)
    #print("Startposition"+str(startPosX)+"   "+str(startPosY))
    #print("MLängen"+str(a)+"   "+str(b))
    motorSetLaenge(a, b)
    return

def main():
    print("------------------------------------------------------------")
    print("Bitte Stift einlegen!")
    aufEingabeWarten()
    print("drucken... - mit Taste -STOP- kann der Vorgeng abgebrochen werden")
    if(machePolyline(FILE) == 1):
        print("")
        print(">>>-STOP-")
    else:
        print("")
        print("fertig!")
    print("Stift entfernen!")
    aufEingabeWarten()
    print("")
    geheStartPos()
    main();
    return
        
    
    
    
if __name__ == '__main__':
    try:
        print("Motor an die erste Stelle der Zeichnung bringen")
        time.sleep(2)
        aufEingabeWarten()
        main()
    except KeyboardInterrupt:
        GPIO.output(ACTIVE, False)
        GPIO.output(READY, False)
        GPIO.cleanup()
        print(" ")
        print("EXIT via KeyboardInterrupt")
    
