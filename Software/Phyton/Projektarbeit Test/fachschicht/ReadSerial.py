from enum import Enum
import serial
import math
import time

D1 = float(0)
D2 = float(0)
H1 = float(0)
T1 = float(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) // SendPin


class ReadSerial:

    def __init__(self):
        pass

    def ReadingSerial(self):
        Serial = serial.Serial('/dev/ttyACM0', 9600) #Port muss davor noch defeniert werden, Alles mit Baudrate von 9600
        Serial.open()
        time.sleep(5)

        finsihedReading = false;
        GPIO.output(16, GPIO.HIGH)


        while finsihedReading == false:

            rawdata = serial.readline()

            if "$" == rawdata:
                GPIO.output(16, GPIO.LOW)
                finsihedReading = true;
                break

            Sensor = [0]*2
            Sensor = rawdata.split('#', 2)
            if "D1" == Sensor[0]:
                D1 = Sensor[1]
            elif "D2" == Sensor[0]:
                D2 = Sensor[1]
            elif "H1" == Sensor[0]:
                H1 = Sensor[1]
            elif "T1" == Sensor[0]:
                T1 = Sensor[1]

