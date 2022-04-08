from enum import Enum
import serial
import math
import time

D1 = float(0)
D2 = float(0)
H1 = float(0)
T1 = float(0)


class ReadSerial:

         ##def __init__(self):

    def ReadingSerial(self):
        Serial = serial.Serial('/dev/ttyACM0', 9600) #Port muss davor noch defeniert werden, Alles mit Baudrate von 9600
        Serial.open()
        time.sleep(5)
        while True:
            rawdata = serial.readline()
            Sensor = [0]*2
            Sensor == rawdata.split('#', 2)
            if Sensor[0] == "D1" :
                D1 == Sensor[1]
            elif Sensor[0] == "D2" :
                D2 == Sensor[1]
            elif Sensor[0] == "H1" :
                H1 == Sensor[1]
            elif Sensor[0] == "T1" :
                T1 == Sensor[1]

