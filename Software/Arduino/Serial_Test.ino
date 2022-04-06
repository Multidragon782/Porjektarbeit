void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int dataOutput = random (0,1000);
  String data = "data=" + String(dataOutput);

  Serial.println(data);

  delay(2500);
}
