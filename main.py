import math;
import collections;
 
minSchritt = 1; """???muss 1 sein???"""
""" umrechnung schritte - längen"""
L = 100; """ abstand der motoren in schritten"""

actMotorLaengeA = 20;
actMotorLaengeB = 70;


 
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
    print("-->neue Gerade: from x,y=(" + str(x1) + "," + str(y1) + ") -> to x,y=(" + str(x2)+ "," + str(y2) + ")")
    motorSetLaenge(a1, b1)
    schritte = 0
    if abs(wegY) < abs(wegX):
        schritte = round(wegX/minSchritt)
    else:
        schritte = round(wegY/minSchritt)
    for i in range(schritte):
        x = (x1 + i*wegX/schritte)
        y = (y1 + i*wegY/schritte)
        a = round(getLaengeA(x, y))
        b = round(getLaengeB(x, y))
        rx = getPosX(a, b)
        ry = getPosY(a, b)
        print("   ->Pos " +str(i) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(rx) + "," + str(ry) + ")")
        motorSetLaenge(a, b)
        continue
    x = x2
    y = y2
    a = round(getLaengeA(x, y))
    b = round(getLaengeB(x, y))
    rx = getPosX(a, b)
    ry = getPosY(a, b)   
    print("   ->Pos " +str(schritte) + "/" + str(schritte) + ": a,b=[" + str(a) + "," + str(b)+"] x,y~(" + str(round(x)) + "," + str(round(y)) + ") rx,ry=(" + str(rx) + "," + str(ry) + ")")
    motorSetLaenge(a, b)
    return


    
    
if __name__ == '__main__':
    macheGerade(10, 20, 40, 10) 
    
    

