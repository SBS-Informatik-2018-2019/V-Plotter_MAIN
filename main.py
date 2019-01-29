#-*- coding: utf-8 -*-
import math
import xml.etree.ElementTree as ElementTree
import time

 
minSchritt = 3; """ ???muss 1 sein???"""
L = 500; """ abstand der motoren in schritten"""

actMotorLaengeA = 0; """ wird spaeter als erster Punkt der Polyline gesezt"""
actMotorLaengeB = 0; """ wird spaeter als erster Punkt der Polyline gesezt"""


 
def getLaengeA(x, y):
    return math.sqrt(x*x+y*y)
 
def getLaengeB(x, y):
    return math.sqrt((L-x)*(L-x)+y*y)
    
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
    todoA = a - actMotorLaengeA
    todoB = b - actMotorLaengeA
    time.sleep(0.05)
    return
    

def macheGerade(x1, y1, x2, y2):
    a1 = getLaengeA(x1, y1)
    b1 = getLaengeB(x1, y1)
    a2 = getLaengeA(x2, y2)
    b2 = getLaengeB(x2, y2)
    wegA = a2-a1
    wegB = b2-b1
    wegX = x2-x1
    wegY = y2-y1
    print(" ->neue Gerade: from x,y=(" + str(x1) + "," + str(y1) + ") -> to x,y=(" + str(x2)+ "," + str(y2) + ")									")
    motorSetLaenge(a1, b1)
    schritte = 0
    if abs(wegY) < abs(wegX):
        schritte = round(abs(wegX)/minSchritt)
    else:
        schritte = round(abs(wegY)/minSchritt)
    for i in range(schritte):
        x = (x1 + i*wegX/schritte)
        y = (y1 + i*wegY/schritte)
        a = round(getLaengeA(x, y))
        b = round(getLaengeB(x, y))
        rx = getPosX(a, b)
        ry = getPosY(a, b)
        print("   ->Pos " +str(i) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + ")", end="\r")
        motorSetLaenge(a, b)
        continue
    x = x2
    y = y2
    a = round(getLaengeA(x, y))
    b = round(getLaengeB(x, y))
    rx = getPosX(a, b)
    ry = getPosY(a, b)   
    print("   ->Pos " +str(schritte) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(round(rx)) + "," + str(round(ry)) + ")", end="\r")
    motorSetLaenge(a, b)
    return

def machePolyline(file):
	svgRootElement = ElementTree.parse(file).getroot()
	polylineElement = svgRootElement.find("{http://www.w3.org/2000/svg}polyline")
	points = polylineElement.get('points')
	print("->Polyline: points=(" + points + ")")
	points = points + " "
	points = points.lstrip()
	index = points.index(',')
	x1 = int(points[0:index])
	if(x1<=0):
		x1 = 1
	points = points[index+1:len(points)]
	points = points.lstrip()
	index = points.index(' ')
	y1 = int(points[0:index])
	if(y1<=0):
		y1 = 1
	points = points[index+1:len(points)]
	points = points.lstrip()
	actMotorLaengeA = getLaengeA(x1, y1)
	actMotorLaengeB = getLaengeB(x1, y1)
	
	while len(points) != 0:
		points = points.lstrip()
		index = points.index(',')
		x2 = int(points[0:index])
		if(x2<=0):
			x2 = 1
		points = points[index+1:len(points)]
		points = points.lstrip()
		index = points.index(' ')
		y2 = int(points[0:index])
		if(y2<=0):
			y2 = 1
		points = points[index+1:len(points)]
		points = points.lstrip()
		macheGerade(x1, y1, x2, y2)
		x1 = x2
		y1 = y2
		continue
	
	return
	


def main():
	time.sleep(1)
	print("i: Für eine korrekte Funktion muss die svg-Datei im ersten <svg> Tag mit dem Attribut xmlns='http://www.w3.org/2000/svg' vesehen sein. Im Parsevorgang werden nur die Punkte der ersten Polyline berücksichtigt.")
	time.sleep(1)
	print("i: Die aktuelle Position wird als Startpunkt der Polyline gesetzt. Achten sie darauf, dass die Strecke der einzelnen Linen niemals den Arbeitsbereich des Plotters verlaesst! - viel Spass...
	time.sleep(3)
	file = input(">>> *.svg File ")
	print("")
	machePolyline(file)
	print("")
	weiter = input(">>> weitere Datei (y/n)?:")
	if weiter == "y":
		main();
	return
		
    
    
    
if __name__ == '__main__':
	print("")
	print("--- SBS V Plotter ---")
	time.sleep(1)
	print("Mit dem SBS VPlotter koennen svg-polyline-Elemente von einem V-Plotter gezeichnet werden")
	main()
	print("auf Wiedersehen")
	
	
	
