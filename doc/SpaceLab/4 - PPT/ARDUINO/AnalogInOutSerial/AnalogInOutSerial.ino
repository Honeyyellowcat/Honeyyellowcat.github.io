#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

// Initialize the stepper motor object
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  // Set maximum speed and acceleration in steps per second per second
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
}

void loop() {
  // Move the stepper motor 200 steps clockwise
  stepper.move(200);
  stepper.runToPosition();

  // Pause for a second
  delay(1000);

  // Move the stepper motor 200 steps counterclockwise
  stepper.move(-200);
  stepper.runToPosition();

  // Pause for a second
  delay(1000);
}
