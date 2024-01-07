// the setup function runs once when you press reset or power the board
int sensorPin = A0;
word sensorValue2, sensorValue_ppm = 0;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
  
}

// the loop function runs over and over again forever
void loop() {
  int sensorValue = analogRead(A1);
  sensorValue2 = analogRead(sensorPin);
  sensorValue_ppm = map(sensorValue2, 0, 490, 0, 1000);
  // print out the value you read:
  Serial.print(sensorValue);
  Serial.print(",");
  Serial.println(sensorValue_ppm);
  delay(250);                      // wait for a second
}