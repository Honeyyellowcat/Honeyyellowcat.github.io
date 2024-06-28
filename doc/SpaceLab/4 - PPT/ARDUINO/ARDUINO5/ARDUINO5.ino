#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

// Initialize the stepper motor object
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  // Set maximum speed and acceleration in steps per second per second
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read command from serial port
    if (command == 'F') {
      // Move the stepper motor forward
      stepper.move(100); // Adjust the number of steps as needed
      stepper.runToPosition();
      Serial.println("Moving forward");
    } else if (command == 'B') {
      // Move the stepper motor backward
      stepper.move(-100); // Adjust the number of steps as needed
      stepper.runToPosition();
      Serial.println("Moving backward");
    } else if (command == 'S') {
      // Stop the stepper motor
      stepper.stop();
      Serial.println("Motor stopped");
    } else {
      Serial.println("Unknown command");
    }
  }
}
