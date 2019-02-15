#-*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

#VARIABLES#######################################
READY = 2 #UI pin
ACTIVE = 3 #UI pin
START = 4 #UI pin
STOP = 17 #UI pin

A=21 #motor A pins
B=20
C=16
D=12
E=8  #motor B pins
F=25
G=24
H=23
#END VARIABLES####################################

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

# getters & setters
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

def output(pin, value):
    GPIO.output(pin, value)
    return

def input(pin):
    if (GPIO.input(pin) == GPIO.HIGH):
        return 1
    else:
        return 0

def aufOKWarten():
    sleep(2.5)
    print("mit Taste -OK- bestätigen")
    no_input = True
    output(getREADY(), True)
    while(no_input):
        sleep(0.001)
        if (input(getSTART())==1):
            no_input = False
    output(getREADY(), False)
    print(">>>-OK-")
    return

@staticmethod
def cleanup():
    GPIO.cleanup()
    return