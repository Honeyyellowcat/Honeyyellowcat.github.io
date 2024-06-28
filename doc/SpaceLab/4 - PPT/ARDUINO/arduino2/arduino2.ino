#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command from serial
    if (command == 'F') { // Forward command
      stepper.move(200);
      stepper.runToPosition();
    } else if (command == 'B') { // Backward command
      stepper.move(-200);
      stepper.runToPosition();
    }
  }
}
