#include <AccelStepper.h>

const int stepPin = 2; // Define the step pin of the stepper motor
const int dirPin = 3; // Define the direction pin of the stepper motor
const int enPin = 4;

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin, enPin);

void setup() {
  Serial.begin(9600); // Initialize serial communication
  stepper.setMaxSpeed(1000); // Set maximum speed of the stepper motor
  stepper.setAcceleration(500); // Set acceleration of the stepper motor
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read serial command until newline
    if (command.startsWith("F")) { // Forward command
      int steps = command.substring(1).toInt(); // Extract steps from the command
      stepper.move(steps); // Move the stepper motor forward
      stepper.runToPosition(); // Wait for stepper to complete movement
    } else if (command.startsWith("B")) { // Backward command
      int steps = command.substring(1).toInt(); // Extract steps from the command
      stepper.move(-steps); // Move the stepper motor backward
      stepper.runToPosition(); // Wait for stepper to complete movement
    } else if (command.startsWith("S")) { // Stop command
      stepper.stop(); // Stop the stepper motor
    }
  }
}
