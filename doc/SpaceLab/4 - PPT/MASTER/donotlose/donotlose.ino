#include <AccelStepper.h>

const int stepPin = 2; // Step pin connected to Arduino digital pin 2
const int dirPin = 3;  // Direction pin connected to Arduino digital pin 3

AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin); // Stepper motor object

void setup() {
  stepper.setMaxSpeed(3000); // Set maximum speed
  Serial.begin(9600); // Initialize serial communication
  digitalWrite(dirPin, HIGH);
  //digitalWrite(4, HIGH); //LOW is on
}

void loop() {
  if (Serial.available() >= 2) { // Check if there are enough bytes available
    String str = Serial.readString(); // Read the command sent from Python
    String command = str.substring(0,1);
    String stepsstr= str.substring(1,str.length()-1);
    int steps=stepsstr.toInt();
    //Serial.println(command);
    // Check the command received
    //switch (command) {
     // case 'A': // Forward movement
      //case 'B': // Backward movement
       // {
          
         // int steps = Serial.parseInt(); // Read the number of steps
          //Serial.println(steps);
          if (command == "A") // If backward, make steps negative
            digitalWrite(dirPin, HIGH);
          if (command == "B") // If backward, make steps negative
            digitalWrite(dirPin, LOW);
          //stepper.move(steps); // Move the stepper motor
          //stepper.runToPosition(); // Execute the movement
          //break;
          for (int i=0; i<=steps; i++) {
            digitalWrite(stepPin, HIGH);
            delay(1);
            digitalWrite(stepPin, LOW);
            delay(1);
        }
    }
  }
