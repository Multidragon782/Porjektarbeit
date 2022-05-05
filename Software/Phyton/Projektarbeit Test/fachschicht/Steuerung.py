import GUI as G
import Datenverwertung as Dv
import Relais as Rl
import ReadSerial as Rd
import multiprocessing
import os

class Steuerung:

    Rd.ReadSerial
    SchalteRelaisHumTemp
    SchalteRelaisLichter
    SchalteRelaisWasseer

    def SchalteRelaisHumTemp():
        if Dv.PruefeHum or Dv.PruefeTemp
                Rl.LuefterAN
    
        else Rl.LuefterAUS  

        pass

    def SchalteRelaisLichter():
        #type boolean
         
        pass

    def SchalteRelaisWasseer():
         if Dv.PruefeDirt
             Rl.WasserschleusseAN

         else Rl.WasserschleusseAUS

        pass

    while True:


