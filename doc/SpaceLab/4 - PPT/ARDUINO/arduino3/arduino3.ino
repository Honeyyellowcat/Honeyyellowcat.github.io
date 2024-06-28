#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

// Initialize the stepper motor object
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  // Set maximum speed and acceleration in steps per second per second
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command from Python

    if (command == 'M') {
      int steps = Serial.parseInt(); // Read the number of steps from Python
      // Move the stepper motor
      //stepper.move(steps);
      //stepper.runToPosition();
      // Echo back to Python
      Serial.println("Movement completed");
    } else if (command == 'F') {
      int steps = Serial.parseInt(); // Read the number of steps from Python
      digitalWrite(dirPin, HIGH);
      for (int i = 0; i<=steps; i++){
        digitalWrite(stepPin, HIGH);
        delay(1);
        digitalWrite(stepPin, LOW);
        delay(1);
      }
      
      // Move forward continuously
      //stepper.setSpeed(1000); // Set speed (adjust as needed)
      //stepper.setAcceleration(500); // Set acceleration (adjust as needed)
      //stepper.move(-1); // Move continuously forward
      //stepper.runSpeed();
    } else if (command == 'B') {
      // Move backward continuously
      stepper.setSpeed(-1000); // Set speed (adjust as needed)
      stepper.setAcceleration(500); // Set acceleration (adjust as needed)
      //stepper.move(1); // Move continuously backward
      stepper.runSpeed();
    } else if (command == 'S') {
      // Stop the motor
      stepper.stop();
      Serial.println("Motor stopped");
    }
  }
}
