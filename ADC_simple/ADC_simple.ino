
int signalPin = A0;
int powerPin = A2; 
int counter = 0;
  
void setup() {
  // put your setup code here, to run once:
  pinMode(signalPin, INPUT);
  pinMode(powerPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(signalPin));
  Serial.print(",");
  Serial.println(analogRead(powerPin));
  delay(2);
  
}
