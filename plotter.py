#-*- coding: utf-8 -*-

import xml.etree.ElementTree as ElementTree
import time
import plotterio as IO




#VARIABLES#######################################
FILE="file_scharf.svg" #name der standart datei
#END VARIABLES####################################



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
    main()
    return
        
    
    
    
if __name__ == '__main__':
    try:
        print("Motor an die erste Stelle der Zeichnung bringen")
        time.sleep(2)
        aufEingabeWarten()
        main()
    except KeyboardInterrupt:
        IO.output(IO.getACTIVE(), False)
        IO.output(IO.getREADY(), False)
        IO.cleanup()
        print(" ")
        print("EXIT via KeyboardInterrupt")
    
