#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      400148
#
# Created:     05.04.2022
# Copyright:   (c) 400148 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import GUI as G
import Datenverwertung as Dv
import Relais as Rl
import ReadSerial as rd
import multiprocessing
import os

class Steuerung:

    Serialloop =  multiprocessing.Process(target=rd.ReadSerial)
    Serialloop.Start


def StartebrechneAvgHum():

    pass

def StartebrechneAvgDirt():

    pass


def StartebrechneAvgTenp():

    pass

def SchalteRelaisHum():
    #type boolean
    pass

def SchalteRelaisTemp():
    #type boolean
	pass

def SchalteRelaisLuft():
    #type boolean
	pass

def SchalteRelaisLichter():
    #type boolean
    pass

while True:
 Dv.PruefeDirtHumTemp

