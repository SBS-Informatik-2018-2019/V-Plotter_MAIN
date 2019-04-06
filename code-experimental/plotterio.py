#-*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

#VARIABLES#######################################
READY = 2 #UI pin: (grün)
ACTIVE = 3 #UI pin: (rot/orange)
START = 4 #UI pin: (Knopf rechts)
STOP = 17 #UI pin: (Knopf links)

A=21 #pins: motor A (LINKS)
B=20
C=16
D=12
E=8  #pins: motor B (RECHTS)
F=25
G=24
H=23
#END VARIABLES####################################


# richtet alle GPIO-Pins ein
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


#getters & setters
def getREADY():
    return READY

def getACTIVE():
    return ACTIVE

def getSTART():
    return START

def getSTOP():
    return STOP

def getA():
    return A

def getB():
    return B

def getC():
    return C

def getD():
    return D

def getE():
    return E

def getF():
    return F

def getG():
    return G

def getH():
    return H 
#END getters & setters

# setzt den pin auf den geforderten Wert
def output(pin, value):
    GPIO.output(pin, value)
    return

# gibt True zurück wenn der Pin HIGH ist, sonst False
def input(pin):
    if (GPIO.input(pin) == GPIO.HIGH):
        return True
    else:
        return False

# wartet solange (mind. 1,5sec) bis die Taste -OK- gedückt wurde. Dabei leuchted die grüne READY LED.
def aufOKWarten():
    sleep(1.5)
    print("mit Taste -OK- bestätigen")
    no_input = True
    output(getREADY(), True)
    while(no_input):
        sleep(0.001)
        if (input(getSTART())):
            no_input = False
    output(getREADY(), False)
    print(">>>-OK-")
    return

def cleanup():
    GPIO.cleanup()
    return