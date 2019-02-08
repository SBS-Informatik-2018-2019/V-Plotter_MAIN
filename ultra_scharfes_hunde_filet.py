#-*- coding: utf-8 -*-
from __future__ import print_function
import math
import xml.etree.ElementTree as ElementTree
import time
import threading
from time import sleep
import RPi.GPIO as GPIO       

#####################################################
minSchritt = 1; # auflösung der greraden
L = 2000 # abstand der motoren in schritten
FILE="file.svg" #name der standart datei
transformator = 1 #


Tmin = 0.005 #zum langsamer machen der motoeren, mindestens 0.001
A=21 #motor A pins
B=20
C=16
D=12
E=8  #motor B pins
F=25
G=24
H=23
READY=2 #UI pins
ACTIVE=3
START=4
STOP=17
startPosX = 0 # do not edit startpunkt
startPosY = 0 # do not edit startpunkt
actMotorLaengeA = 0 # do not edit startpunkt
actMotorLaengeB = 0 # do not edit startpunkt
#######################################################


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.setup(E,GPIO.OUT)
GPIO.setup(F,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(H,GPIO.OUT)
GPIO.setup(ACTIVE,GPIO.OUT)
GPIO.setup(READY,GPIO.OUT)
GPIO.setwarnings(True)

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

class motor (threading.Thread):
    def __init__(self, steps , Tmult , inv):
        threading.Thread.__init__(self)
        self.steps=steps
        self.Tmult=Tmult
        self.time=Tmin*Tmult

        if inv == True:
            self.A=E
            self.B=F
            self.C=G
            self.D=H
        else:
            self.A=A
            self.B=B
            self.C=C
            self.D=D
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
        GPIO.output(self.D, False)

    def run(self):
        #print(self.steps)

        def Step1():
            GPIO.output(self.D, True)
            sleep (self.time)
            GPIO.output(self.D, False)

        def Step2():
            GPIO.output(self.D, True)
            GPIO.output(self.C, True)
            sleep (self.time)
            GPIO.output(self.D, False)
            GPIO.output(self.C, False)

        def Step3():
            GPIO.output(self.C, True)
            sleep (self.time)
            GPIO.output(self.C, False)

        def Step4():
            GPIO.output(self.B, True)
            GPIO.output(self.C, True)
            sleep (self.time)
            GPIO.output(self.B, False)
            GPIO.output(self.C, False)

        def Step5():
            GPIO.output(self.B, True)
            sleep (self.time)
            GPIO.output(self.B, False)

        def Step6():
            GPIO.output(self.A, True)
            GPIO.output(self.B, True)
            sleep (self.time)
            GPIO.output(self.A, False)
            GPIO.output(self.B, False)

        def Step7():
            GPIO.output(self.A, True)
            sleep (self.time)
            GPIO.output(self.A, False)

        def Step8():
            GPIO.output(self.D, True)
            GPIO.output(self.A, True)
            sleep (self.time)
            GPIO.output(self.D, False)
            GPIO.output(self.A, False)


        if self.steps==0:
            return 0
        if self.steps > 0:
            for i in range (self.steps):
                Step1()
                Step2()
                Step3()
                Step4()
                Step5()
                Step6()
                Step7()
                Step8()
        else:
            for i in range (abs(self.steps)):
                Step8()
                Step7()
                Step6()
                Step5()
                Step4()
                Step3()
                Step2()
                Step1()


 
def getLaengeA(x, y):
    return math.sqrt((x*x)+(y*y))
 
def getLaengeB(x, y):
    return math.sqrt(((L-x)*(L-x))+(y*y))
    
def beta (a, b):
    res = math.acos (-(b * b - a * a - L * L) / (2 * a * L))
    return res;
    
def getPosX (a, b):
    res = math.cos(beta(a, b))*a
    return res
    
def getPosY (a, b):
    res = math.sin(beta(a, b))*a
    return res
    
def motorSetLaenge(a, b):
    global actMotorLaengeA
    global actMotorLaengeB
    todoA = int(a - (actMotorLaengeA))
    todoB = - (int(b - (actMotorLaengeB))) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!geändert mal sehen ob dann nicht mehr gespiegelt
    actMotorLaengeA += todoA
    actMotorLaengeB += todoB
    #print("????actML: a/b"+str(actMotorLaengeA)+";"+str(actMotorLaengeB))
    #print("????todotML: a/b"+str(todoA)+";"+str(todoB))
    da=1.0
    db=1.0
    fa=float(abs(todoA))
    fb=float(abs(todoB))
    if (fa==0)| (fb==0):
        pass
    elif fa > fb:
        db=fa/fb
    elif fa < fb:
        da=fb/fa
    A=motor(todoA,da,False)
    B=motor(todoB,db,True)
    A.start()
    B.start()
    A.join()
    B.join()
    if(GPIO.input(STOP)==GPIO.HIGH):
        return 1
    return 0
    

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
    print(" ->neue Gerade: from x,y=(" + str(x1) + "," + str(y1) + ") -> to x,y=(" + str(x2)+ "," + str(y2) + ")                                    ")
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
        print("   ->Pos " +str(i) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + ")")
        if(motorSetLaenge(a, b)==1):
            return 1
        continue
    x = x2
    y = y2
    a = round(getLaengeA(x, y))
    b = round(getLaengeB(x, y))
    rx = getPosX(a, b)
    ry = getPosY(a, b)   
    print("   ->Pos " +str(schritte) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + "): -fertig")
    if(motorSetLaenge(a, b)==1):
        return 1
    return 0

def machePolyline(file):
    global startPosX
    global startPosY
    global actMotorLaengeA
    global actMotorLaengeB
    svgRootElement = ElementTree.parse(file).getroot()
    polylineElement = svgRootElement.find("{http://www.w3.org/2000/svg}polyline")
    points = polylineElement.get('points')
    print("->Polyline: points=(" + points + ")")
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
    print("~~~~~~~~~~~STARTX="+str(startPosX))
    print("~~~~~~~~~~~STARTY="+str(startPosY))
    actMotorLaengeA = getLaengeA(startPosX, startPosY)
    actMotorLaengeB = getLaengeB(startPosX, startPosY)
    print("~~~~~~~~~~~STARTMLA="+str(actMotorLaengeA))
    print("~~~~~~~~~~~STARTMLB="+str(actMotorLaengeB))
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
    time.sleep(1.75)
    no_input = True
    GPIO.output(READY, True)
    while(no_input):
        time.sleep(0.2)
        if (GPIO.input(START)==GPIO.HIGH):
            no_input = False
    GPIO.output(READY, False)
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
    print("#MAIN########################################################################################################################################")
    print("wenn bereit Stift einlegen, Position sollte Startposition der Liene sein und mit Taste -OK- bestätigen")
    aufEingabeWarten()
    print(">>>-OK-")
    GPIO.output(ACTIVE, True)
    if(machePolyline(FILE) == 1):
        print("")
        print(">>>-STOP-")
    else:
        print("")
        print("fertig!")
    print("Stift entfernen mit Taste -OK- bestätigen")
    aufEingabeWarten()
    print(">>>-OK-")
    print("fahre zur Startposition zurück")
    geheStartPos()
    main();
    return
        
    
    
    
if __name__ == '__main__':
    try:
        print("Motor an die erste Stelle der Polyline bringen")
        time.sleep(2)
        print("Bitte mit Taste -OK- bestätigen")
        aufEingabeWarten()
        print(">>>-OK-")
        main()
    except KeyboardInterrupt:
        GPIO.output(ACTIVE, True)
        GPIO.output(READY, False)
        GPIO.cleanup()
        print(" ")
        print("EXIT via KeyboardInterrupt")
    
