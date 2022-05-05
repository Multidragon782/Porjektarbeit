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
            i += 1

        AvgHum = AvgHumRaw /4


    def berechneAvgDirt(self):
        i = 0
        AvgDirtRaw = 0

        while i != 11:
            AvgDirtRaw = AvgDirtRaw + Bodenfeuchtigkeit5Sec[i]
            i += 1

        AvgDirt = AvgDirtRaw / 12



    def berechneAvgTemp(self):
        i = 0
        AvgTempRaw = 0
        while i != 59:
            AvgTempRaw = AvgTempRaw + TemperaturProMin[i]
            i += 1

        AvgTemp = AvgTempRaw / 60


    def PruefeHum(HumOp)
        if   berechneAvgHum / HumOp > 1.1:
            True
        
        elif berechneAvgHum / HumOp <= 1.1:
            False


    def PruefeTemp(TempOp)
        if   berechneAvgTemp / TempOp > 1.1: 
            True
        
        elif berechneAvgTemp / TempOp <= 1.1:
            False
    
           
     def PruefeDirt(DirtOp)
         if   berechneAvgDirt / DirtOp >= 0.9: #Wasser aus
            True
        
        elif berechneAvgDirt / DirtOp < 0.9:   #Wasser an
            False 