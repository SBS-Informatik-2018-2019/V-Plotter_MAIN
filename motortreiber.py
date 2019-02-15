#-*- coding: utf-8 -*-
from time import sleep
import threading
import RPi.GPIO as GPIO

Tmin = 0.005 #zum langsamer machen der motoeren, mindestens 0.001
A=21 #motor A pins
B=20
C=16
D=12
E=8  #motor B pins
F=25
G=24
H=23


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
GPIO.setwarnings(True)

def motorSetLaenge(a, b):
    global actMotorLaengeA
    global actMotorLaengeB
    todoA = int(a - (actMotorLaengeA))
    todoB =  int(b - (actMotorLaengeB)) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!geändert mal sehen ob dann nicht mehr gespiegelt
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
    if(GPIO.input(STOP)==GPIO.HIGH):
        return 1
    return 0













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