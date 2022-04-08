#include <dht.h>

#include "DHT.h" //DHT Bibliothek laden

#define DHTPIN 2 //Der Sensor wird an PIN 2 angeschlossen    

#define DHTTYPE DHT11    // Es handelt sich um den DHT11 Sensor

DHT dht(DHTPIN, DHTTYPE); //Der Sensor wird ab jetzt mit „dth“ angesprochen

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600); //Serialle Schnittstelle starten
 dht.begin(); //DHT11 Sensor starten
}
void loop() 
{
int DirtSen1 = analogRead(A0); //Analog Anschluss (Bodensensor 1) A0 wird auselesen und in "Dirtsen1" gespeichert 
int DirtSen2 = analogRead(A1); //Analog Anschluss (Bodensensor 2) A1 wird auselesen und in "Dirtsen2" gespeichert

HumSen1 = dht.readHumidity(); //Luftfeuchtigkeit auslesen und in „HumSen1“ speichern
TempSen1 = dht.readTemperature(); //Temperatur auslesen und in „TempSen1“ speichern


String strDirtSen1 = "D1#" + DirtSen1;
String strDirtSen2 = "D2#" + DirtSen2;
String strHumSen1 = "H1#" + HumSen1;
String strTemp1 = "T1" + TempSen1;

Serial.println(serDirtSen1);// Bodensensor 1 (DirtSen1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "D1"
Serial.print(strDirtsen2);// Bodensensor 2 (DirtSen2) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "D2"
Serial.println(str HumSen1);// Luftfeuchtigkeitsensor 1 (Hum1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "H1"
Serial.println(strTempSen1);//TemperaturSensor 1 (DirtSen1) wird über Serielle Schnittstelle geschickt,mit dem Vorcode "T1"
delay(1000); //Warte 1000 milisekunden
}
