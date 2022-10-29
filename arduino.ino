#include <Stepper.h>

float motorpeed = 60;
const int stepsPerRevolution(){
  int tong = 1000000/(motorSpeed/(60*pulsePerRoundX));
  Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
  } 

int pulsePerRoundX =200;
int stepCount = 0;  
const int out1 = 10;
const int out2 = 9;
const int out3 = 11;
const int out4 = 8;
void setup() {
  
}

void loop() {

  int sensorReading = analogRead(A0);
  int motorSpeed = map(sensorReading, 0, 1023, 0, 100);
    Serial.println(motorSpeed);
    myStepper.setSpeed(motorSpeed);
    myStepper.step(stepsPerRevolution);
    delay(500);
    myStepper.step(-stepsPerRevolution);
    delay(1000);
    }

