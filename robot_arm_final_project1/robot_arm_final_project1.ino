#include <Servo.h>

// Define servo objects
Servo servos[5]; // Array for thumb, index, middle, ring, pinky

// Pin definitions
const int servoPins[5] = {3, 5, 6, 9, 10};

void setup() {
  for (int i = 0; i < 5; i++) {
    servos[i].attach(servoPins[i]);
    servos[i].write(0); // Initialize to 0 degrees
  }

  Serial.begin(9600);
  Serial.println("System Ready. Waiting for data...");
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();

    // Decode and move servos
    for (int i = 0; i < 5; i++) {
      servos[i].write((data & (1 << (4 - i))) ? 0 : 180);
    }
  }
}
