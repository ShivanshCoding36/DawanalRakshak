const int buzzer = 12; // Pin connected to the LED
char incomingData;     // Variable to store incoming serial data 
const int RELAY_PIN = 4;
#include <Servo.h>
Servo myservo;
 // Replace 3 with the actual pin number where your DHT sensor is connected


void setup() 
{
  Serial.begin(9600); // Start serial communication at 9600 baud
  myservo.attach(2);
  pinMode(buzzer, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
}

void loop() {
  myservo.write(0);
  delay(2000);


  if (Serial.available() > 0) {
    incomingData = Serial.read(); // Read the incoming data

    if (incomingData == 'F') {
      // IA 'AIRE' is received, perAorm actions
      incomingData = '0';
      tone(buzzer, 1000); // Send 1KHz sound signal...
      digitalWrite(RELAY_PIN, LOW);
      digitalWrite(13, HIGH);
      digitalWrite(10, HIGH);
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(11, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(9, HIGH);
      for (int i = 0; i <= 100; i++) {
        myservo.write(i);
        digitalWrite(RELAY_PIN, LOW);
        Serial.println(i);
        delay(55);
      }
      for (int i = 100; i >= 0; i--) {
        myservo.write(i);
        digitalWrite(RELAY_PIN, LOW);
        Serial.println(i);
        delay(55);
      }
      noTone(buzzer); // Stop sound...
      digitalWrite(RELAY_PIN, HIGH);
      digitalWrite(13, LOW);
      digitalWrite(10, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(11, LOW);
      digitalWrite(8, LOW);
      digitalWrite(3, LOW);
      digitalWrite(9, LOW);
    }
  }
}
