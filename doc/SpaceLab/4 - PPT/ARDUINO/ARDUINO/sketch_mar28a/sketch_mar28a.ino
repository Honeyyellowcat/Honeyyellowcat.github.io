// Defining the connecting ports
int portIN1 = 2;  // Connect to the IN1 pin of stepper motor driver
int portIN2 = 3;  // Connect to the IN2 pin of stepper motor driver
int portIN3 = 4;  // Connect to the IN3 pin of stepper motor driver
int portIN4 = 5;  // Connect to the IN4 pin of stepper motor driver

// Converted final variables, used to run the motor
int motRunInt;
String motDirString;
float stepsRev;
float pause;

void setup() {
  Serial.begin(9600);

  pinMode(portIN1, OUTPUT);
  pinMode(portIN2, OUTPUT);
  pinMode(portIN3, OUTPUT);
  pinMode(portIN4, OUTPUT);
}

void loop() {
  // Check to see if anything is available in the serial receive buffer
  while (Serial.available() > 0) {
    // Create a place to hold the incoming message
    static char motData[50]; // Arbitrary length

    // Read the next available byte in the serial receiver buffer
    char charData = Serial.read();

    // Process incoming message
    if (charData != '\n') {
      static unsigned int index_pos = 0;
      motData[index_pos] = charData;
      index_pos++;
    } else {
      motData[index_pos] = '';
      index_pos = 0;

      Parse_the_Data(motData);

      // Operating parameter conversion 
      stepsRev = 360.0 / 0.18 / 4.0; // Set a constant number of steps for 360 degrees
      pause = 60000.0 / (motRunInt * 2049); // Set a constant pause value
      
      if (motDirString == "Clockwise") {
        stepper_Clockwise();
        digitalWrite(portIN1, LOW);
      } else if (motDirString == "Anticlockwise") {
        stepper_Anticlockwise();
        digitalWrite(portIN4, LOW);
      } else {
        Serial.println("Invalid Input. Try Again!");
      }
    }
  }
}

void Parse_the_Data(String dataIn) {
  // Parsing only the direction command
  motDirString = dataIn;
}

void stepper_Anticlockwise() {
  for (int i = 0; i < stepsRev; i++) {
    digitalWrite(portIN1, HIGH);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, LOW);
    delay(pause);
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, HIGH);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, LOW);
    delay(pause);
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, HIGH);
    digitalWrite(portIN4, LOW);
    delay(pause);
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, HIGH);
    delay(pause);
  }
}

void stepper_Clockwise() {
  for (int i = 0; i < stepsRev; i++) {
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, HIGH);
    delay(pause);
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, HIGH);
    digitalWrite(portIN4, LOW);
    delay(pause);
    digitalWrite(portIN1, LOW);
    digitalWrite(portIN2, HIGH);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, LOW);
    delay(pause);
    digitalWrite(portIN1, HIGH);
    digitalWrite(portIN2, LOW);
    digitalWrite(portIN3, LOW);
    digitalWrite(portIN4, LOW);
    delay(pause);
  }
}
