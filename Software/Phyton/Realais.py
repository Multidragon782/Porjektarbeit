#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      400136
#
# Created:     05.04.2022
# Copyright:   (c) 400136 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)      #Lüfter
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)      #Lampe
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)      #Pumpe
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)     #Ventil

#Wasserschleuße
class WasserschleußeAN()
    GPIO.output(10, GPIO.HIGH)

class WasserschleußeAUS()
    GPIO.output(10, GPIO.LOW)

#Pumpe
class PumpeAN:
    GPIO.output(8, GPIO.HIGH)

class PumpeAUS:
    GPIO.output(8, GPIO.LOW)

#Licht
class LichtAN:
    GPIO.output(6, GPIO.HIGH)

class LichtAUS:
    GPIO.output(6, GPIO.LOW)

#Lüfter
class LüfterAN:
    GPIO.output(4, GPIO.HIGH)

class LüfterAUS:
    GPIO.output(4, GPIO.LOW)