#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin); // Stepper motor object
long originalPosition = 0; // Variable to store the original position

void setup() {
  stepper.setMaxSpeed(1000); // Set maximum speed
  Serial.begin(9600); // Initialize serial communication
  originalPosition = 0; // Set the original position to 0
}

void loop() {
  if (Serial.available() >= 2) { // Check if there are enough bytes available
    char command = Serial.read(); // Read the command sent from Python
    
    // Check the command received
    switch (command) {
      case 'A': // Forward movement
      case 'B': // Backward movement
        {
          int steps = Serial.parseInt(); // Read the number of steps
          if (command == 'B') // If backward, make steps negative
            steps = -steps;
          stepper.move(steps); // Move the stepper motor
          stepper.runToPosition(); // Execute the movement
          break;
        }
    }
  }
}
