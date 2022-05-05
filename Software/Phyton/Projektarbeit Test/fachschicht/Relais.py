import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)      #Lüfter
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)      #Lampe
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)      #Pumpe
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)     #Ventil

#Wasserschleuße
def WasserschleusseAN():
    GPIO.output(10, GPIO.LOW)


def WasserschleusseAUS():
    GPIO.output(10, GPIO.HIGH)

#Pumpe
def PumpeAN():
    GPIO.output(8, GPIO.HIGH)

def PumpeAUS():
    GPIO.output(8, GPIO.LOW)

#Licht
def LichtAN():
    GPIO.output(6, GPIO.HIGH)

def LichtAUS():
    GPIO.output(6, GPIO.LOW)

#Lüfter
def LuefterAN():
    GPIO.output(4, GPIO.HIGH)

def LuefterAUS():
    GPIO.output(4, GPIO.LOW)