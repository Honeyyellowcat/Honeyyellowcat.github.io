int pulPin = 2;
int dirPin = 3;
int enPin = 4;

void setup() {
pinMode(pulPin, OUTPUT);
pinMode(dirPin, OUTPUT);
pinMode(enPin, OUTPUT);
digitalWrite(dirPin, LOW);
digitalWrite(enPin, HIGH);
}

void loop() {
    digitalWrite(pulPin, LOW);
    delay(1);
    digitalWrite(pulPin, HIGH);
    delay(1);
}
