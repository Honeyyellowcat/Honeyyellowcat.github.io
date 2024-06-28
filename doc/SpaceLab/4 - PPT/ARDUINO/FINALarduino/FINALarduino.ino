#include <AccelStepper.h> // Including the AccelStepper library

const int stepPin = 2; // Declaring a constant integer variable and assigning the Arduino digital pin 2 to it
const int dirPin = 3;  // Declaring a constant integer variable and assigning the Arduino digital pin 3 to it

// Initializing the stepper motor object with DRIVER mode, step pin, and direction pin
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

int stepsTaken = 0; // Declaring and initializing a variable to track the number of steps taken

void setup() {
  // Setting the maximum speed and acceleration for the stepper motor
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);

  Serial.begin(9600); // Initializing serial communication
}

void loop() {
  // Checking if steps taken is less than 100
  if (stepsTaken < 100) {
    // Moving the stepper motor 200 steps clockwise
    stepper.move(200);
    stepper.runToPosition();
    stepsTaken += 200; // Incrementing steps taken by 200

    // Pausing for a second
    delay(1000);
    
    // Checking if steps taken exceeds 100, and adjusting steps to reach exactly 100
    if (stepsTaken > 100) {
      int remainingSteps = 100 - (stepsTaken - 200); // Calculating remaining steps to reach 100
      stepper.move(-remainingSteps);
      stepper.runToPosition();
      stepsTaken = 100; // Updating steps taken to exactly 100
      
    } else {
      // Moving the stepper motor 200 steps counterclockwise
      stepper.move(-200);
      stepper.runToPosition();
      stepsTaken += 200; // Incrementing steps taken by 200

      // Pausing for a second
      delay(1000);
    }
  }
}
