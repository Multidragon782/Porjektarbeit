#include <Adafruit_AHTX0.h>
int SendPin = 13;

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600); //Serialle Schnittstelle starten
 Adafruit_AHTX0 aht;
 pinMode(SendPiin,OUTPUT);
 boolean RepeatSend = false;
}
void loop() 
{
sensors_event_t humidity, temp;
aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
int DirtSen1 = analogRead(A0); //Analog Anschluss (Bodensensor 1) A0 wird auselesen und in "Dirtsen1" gespeichert 
int DirtSen2 = analogRead(A1); //Analog Anschluss (Bodensensor 2) A1 wird auselesen und in "Dirtsen2" gespeichert
HumSen1 = humidity.relative_humidity; //Luftfeuchtigkeit auslesen und in „HumSen1“ speichern
TempSen1 = temp.temperature; //Temperatur auslesen und in „TempSen1“ speichern

String strDirtSen1 = "D1#" + DirtSen1;
String strDirtSen2 = "D2#" + DirtSen2;
String strHumSen1 = "H1#" + HumSen1;
String strTemp1 = "T1" + TempSen1;


if (digitalRead(SendPin) == false)
{
RepeatSend = false;
}

if (digitalRead(Sendpin) == true && RepeatSend = false)
{
Serial.println(serDirtSen1);// Bodensensor 1 (DirtSen1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "D1"
delay(50);
Serial.print(strDirtsen2);// Bodensensor 2 (DirtSen2) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "D2"
delay(50);
Serial.println(str HumSen1);// Luftfeuchtigkeitsensor 1 (Hum1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "H1"
delay(50);
Serial.println(strTempSen1);//TemperaturSensor 1 (DirtSen1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "T1"
delay(50);
RepeatSend = true;
Serial.println("$");
}
delay(100); //Warte 100 milisekunden
}
