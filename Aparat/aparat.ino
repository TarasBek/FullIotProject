/* LM35 analog temperature sensor with Arduino example code. More info: https://www.makerguides.com */

// Define to which pin of the Arduino the output of the LM35 is connected:
#define sensorPin A0

int FAN = 7;
void setup() {
  // Begin serial communication at a baud rate of 9600:
  Serial.begin(9600);

  pinMode(FAN, OUTPUT);
  analogReference(INTERNAL);
}

void loop() {
  
      // Get a reading from the temperature sensor:
  int reading = analogRead(sensorPin);

  // Convert the reading into voltage:
  float voltage = reading * (1100 / 1024.0);

  // Convert the voltage into the temperature in degree Celsius:
  int temperature = voltage / 10;

  // Print the temperature in the Serial Monitor:
  Serial.println(temperature);
  if(temperature>=8)
  {
    digitalWrite(FAN,HIGH);
  }
  else
  {
    digitalWrite(FAN,LOW);
  }


  delay(3000); // wait a second between readings
  

}
