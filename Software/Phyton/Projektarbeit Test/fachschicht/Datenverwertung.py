#-------------------------------------------------------------------------------
# Name:        Datenverwertung
# Purpose:
#
# Author:      400144
#
# Created:     05.04.2022
# Copyright:   (c) 400144 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Datenverwertung:

    Dirt = 0
    Hum = 0
    Temp = 0

    TemperaturProMin = [None] * 60

    Bodenfeuchtigkeit5Sec = [None] * 12

    Luftfeuchtigkeit15Min = [None] * 4



    def getTemperartur(self):
        TemperaturProMin.append()
        TemperaturProMin.pop(0)



    def getBodenfeuchtigkeit(self):
        Bodenfeuchtigkeit5Sec.append()
        Bodenfeuchtigkeit5Sec.pop(0)


    def getLuftfeuchtigkeit(self):
        Luftfeuchtigkeit15Min.append()
        Luftfeuchtigkeit15Min.pop(0)


    def berechneAvgHum(self):
        i = 0
        AvgHumRaw = 0

        while i != 3:
            AvgHumRaw = AvgHumRaw + Luftfeuchtigkeit15Min[i]

        AvgHum = AvgHumRaw /4


    def berechneAvgDirt(self):
        i = 0
        AvgDirtRaw = 0

        while i != 11:
            AvgDirtRaw = AvgDirtRaw + Bodenfeuchtigkeit5Sec[i]

        AvgDirt = AvgDirtRaw / 12



    def berechneAvgTemp(self):
        i = 0
        AvgTempRaw = 0
        while i != 59:
            AvgTempRaw = AvgTempRaw + TemperaturProMin[i]

        AvgTemp = AvgTempRaw / 60



    def PruefeDirtHumTemp(self):

        berechneAvgHum()
        berechneAVgDirt()
        berechneAvgTemp()
        """



        """
        pass