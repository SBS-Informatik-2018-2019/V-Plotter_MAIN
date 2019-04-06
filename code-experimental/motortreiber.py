#-*- coding: utf-8 -*-
from time import sleep
import threading
import plotterioPRE as IO

#VARIABLES#######################################
Tmin = 0.005 #zum langsamer machen der motoeren, mindestens 0.001
actMotorLaengeA = 0 # do not edit actML
actMotorLaengeB = 0 # do not edit actML
#END VARIABLES####################################

#getters & setters
def getActMotorLaengeA():
    return actMotorLaengeA

def getActMotorLaengeB():
    return actMotorLaengeB
#END getters & setters

# legt die Anfangslängen fest auf die der Motor zu Beginn eingestellt wurde
def initLaenge(a, b):
    global actMotorLaengeA
    global actMotorLaengeB
    actMotorLaengeA = round(a)
    actMotorLaengeB = round(b)

# TODO: KOMMENTAR
def setLaenge(a, b):
    global actMotorLaengeA
    global actMotorLaengeB
    todoA = int(round(a - actMotorLaengeA))
    todoB = int(round(b - actMotorLaengeB))
    actMotorLaengeA += todoA
    actMotorLaengeB += todoB
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
    if(IO.input(IO.getSTOP())):
        return "stop"
    return 0

# TODO: KOMMENTAR
class motor (threading.Thread):
    
    # TODO: KOMMENTAR
    def __init__(self, steps , Tmult , inv):
        threading.Thread.__init__(self)
        self.steps=steps
        self.Tmult=Tmult
        self.time=Tmin*Tmult

        if inv == True:
            self.A=IO.getE()
            self.B=IO.getF()
            self.C=IO.getG()
            self.D=IO.getH()
        else:
            self.A=IO.getA()
            self.B=IO.getB()
            self.C=IO.getC()
            self.D=IO.getD()
        IO.output(self.A, False)
        IO.output(self.B, False)
        IO.output(self.C, False)
        IO.output(self.D, False)

    # TODO: KOMMENTAR
    def run(self):
        def Step1():
            IO.output(self.D, True)
            sleep (self.time)
            IO.output(self.D, False)
        def Step2():
            IO.output(self.D, True)
            IO.output(self.C, True)
            sleep (self.time)
            IO.output(self.D, False)
            IO.output(self.C, False)
        def Step3():
            IO.output(self.C, True)
            sleep (self.time)
            IO.output(self.C, False)
        def Step4():
            IO.output(self.B, True)
            IO.output(self.C, True)
            sleep (self.time)
            IO.output(self.B, False)
            IO.output(self.C, False)
        def Step5():
            IO.output(self.B, True)
            sleep (self.time)
            IO.output(self.B, False)
        def Step6():
            IO.output(self.A, True)
            IO.output(self.B, True)
            sleep (self.time)
            IO.output(self.A, False)
            IO.output(self.B, False)
        def Step7():
            IO.output(self.A, True)
            sleep (self.time)
            IO.output(self.A, False)
        def Step8():
            IO.output(self.D, True)
            IO.output(self.A, True)
            sleep (self.time)
            IO.output(self.D, False)
            IO.output(self.A, False)

        # TODO: KOMMENTAR
        if self.steps==0:
            return 0
        if self.steps > 0:
            i = 0
            while(i < abs(self.steps)):
                Step1()
                Step2()
                Step3()
                Step4()
                Step5()
                Step6()
                Step7()
                Step8()
                i += 1
        else:
            i = 0
            while(i < abs(self.steps)):
                Step8()
                Step7()
                Step6()
                Step5()
                Step4()
                Step3()
                Step2()
                Step1()
                i += 1