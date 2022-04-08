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
            Sensor = str(0)
            SensorData = float(0)
            Sensor,SensorData == rawdata.split('#', 2)
            if Sensor == "D1" :
                var = D1 == SensorData
            elif Sensor == "D2" :
                var = D2 == SensorData
            elif Sensor == "H1" :
                H1 == SensorData
            elif Sensor == "T1" :
                T1 == SensorData

