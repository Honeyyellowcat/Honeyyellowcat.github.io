#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

// Initialize the stepper motor object
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

int stepsTaken = 0; // Variable to track the number of steps taken

void setup() {
  // Set maximum speed and acceleration in steps per second per second
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
}

void loop() {
  // If steps taken is less than 100, continue moving
  if (stepsTaken < 100) {
    // Move the stepper motor 200 steps clockwise
    stepper.move(200);
    stepper.runToPosition();
    stepsTaken += 200; // Increment steps taken

    // Pause for a second
    delay(1000);
    
    // If steps taken exceeds 100, adjust steps to reach exactly 100
    if (stepsTaken > 100) {
      int remainingSteps = 100 - (stepsTaken - 200); // Calculate remaining steps to reach 100
      stepper.move(-remainingSteps);
      stepper.runToPosition();
      stepsTaken = 100; // Update steps taken to exactly 100
    } else {
      // Move the stepper motor 200 steps counterclockwise
      stepper.move(-200);
      stepper.runToPosition();
      stepsTaken += 200; // Increment steps taken

      // Pause for a second
      delay(1000);
    }
  }
}
