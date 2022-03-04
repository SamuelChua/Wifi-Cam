#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int startpos = 0;    // start angle
int endpos = 180; // end angle
unsigned long duration = 3000; //duration to turn x angle
unsigned long moveStartTime;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  moveStartTime = millis();
}

void loop() {
 unsigned long progress = millis() - moveStartTime;
 if (progress <= duration){
  long angle = map(progress, 0, duration, startpos, endpos);
  myservo.write(angle);
 }
 else{
  myservo.write(startpos); // can look at the speed control moving back to startpos but not most important now
 }
}
