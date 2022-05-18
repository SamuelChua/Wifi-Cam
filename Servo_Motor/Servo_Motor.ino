#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int startpos = 0;    // start angle
int endpos = 180; // end angle
unsigned long duration = 4000; //duration to turn x angle
unsigned long moveStartTime;



void setup() {
  myservo.attach(4);  // attaches the servo on pin 9 to the servo object
  moveStartTime = millis();
  Serial.begin(9600);
}

void loop() { 
 unsigned long progress = millis() - moveStartTime;

 if (progress <= duration){
   long angle = map(progress, 0, duration, startpos, endpos);
   myservo.write(angle);
 }
 else if (progress > duration && progress <= duration*2){ 
   long angle = map(progress, duration, duration*2, endpos, startpos);
   myservo.write(angle); // can look at the speed control moving back to startpos but not most important now
 }
 else
 {
  myservo.detach();
 }



}
