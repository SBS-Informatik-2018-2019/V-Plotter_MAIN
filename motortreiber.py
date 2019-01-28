import threading
from time import sleep
"""motortreiber, noch nicht ganz abgeschlossen, muss aktuell noch von hand ausgeführt werden(siehe sample code unten), ist aber fehlerfrei"""

#import RPi.GPIO as GPIO       #auskommentiert zum testen
#GPIO.setmode(GPIO.BCM)


#############################  # zum testen
class GPIO():
    def output(a,b):
        print(a,b)
        return 0
##############################


Tmin = 0.101 #zum langsamer machen, mindestens 0.001
A=18
B=23
C=24
D=25
E=81 #placeholder numbers, ist noch nicht gebaut
F=82
G=83
H=84
#GPIO.setup(A,GPIO.OUT) #auskommentiert zum testen
#GPIO.setup(B,GPIO.OUT)
#GPIO.setup(C,GPIO.OUT)
#GPIO.setup(D,GPIO.OUT)
#GPIO.setup(E,GPIO.OUT)
#GPIO.setup(F,GPIO.OUT)
#GPIO.setup(G,GPIO.OUT)
#GPIO.setup(H,GPIO.OUT)
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
        print(self.steps)

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
            for i in range (self.steps):
                Step8()
                Step7()
                Step6()
                Step5()
                Step4()
                Step3()
                Step2()
                Step1()

A=motor(4,5,False)
B=motor(10,2,True)
A.start()
B.start()
A.join()
B.join()
