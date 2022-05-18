  /* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>
#define INPUT_SIZE 30

Servo myservo;  // create servo object to control a servo
Servo myservo1;
//SoftwareSerial mySerial(10, 11); // RX, TX
// twelve servo objects can be created on most boards
int hpos = 0, vpos = 0;// variable to store the servo position
int pos1 = 0; 
int pos2 = 0;
//int datafromUser=0;
String inByte;
  

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //mySerial.begin(9600); 
  
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo1.attach(4);  // attaches the servo on pin 4 to the servo object
  myservo.write(0); //Remember to end servo position at 0
  myservo1.write(0);
  myservo.detach();  // attaches the servo on pin 9 to the servo object
  myservo1.detach();
  
  
}


void moveTo1 (int position, int speed){
  unsigned int mapSpeed = map(speed, 0,30,30,0);
  if (position > vpos){
    for (vpos = pos1; vpos <= position; vpos +=1){
      myservo1.write(vpos);
      pos1 = vpos;
      delay(mapSpeed);
    } 
  }
  else{
    for (vpos = pos1; vpos >= position; vpos -=1){
      myservo1.write(vpos);
      pos1 = vpos;
      delay(mapSpeed);
  }
}
  
}

void vert_only(int position){
  myservo1.attach(4);
//  while (Serial.available()){
//    myservo1.attach(4);
//    inByte = Serial.readString();
// 
  Serial.print("Servo in vert position: ");
  Serial.println(String(position));  
//    position = inByte.toInt();
  
  moveTo1(position, 1);
  myservo1.detach();
}


void moveTo (int position, int speed){
  unsigned int mapSpeed = map(speed, 0,30,30,0);
  if (position > hpos){
    for (hpos = pos2; hpos <= position; hpos +=1){
      myservo.write(hpos);
      pos2 = hpos;
      delay(mapSpeed);
    } 
  }
  else{
    for (hpos = pos2; hpos >= position; hpos -=1){
      myservo.write(hpos);
      pos2 = hpos;
      delay(mapSpeed);
  }
}
  
}

void hori(int position){
  
  // put your main code here, to run repeatedly:
  
  myservo.attach(9);
  
  
//  while (Serial.available()){
//    myservo.attach(9);  
//    inByte = Serial.readString();
// 
    Serial.print("Servo in hori position: ");
    Serial.println(String(position));  
//    position = inByte.toInt();
  
  moveTo(position, 1);
  myservo.detach();
}    



//
//void vert(){
//   
//   for (pos2 = 0; pos2 <= 180; pos2 += 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    myservo1.write(pos2);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15 ms for the servo to reach the position
//  }
//  for (pos2 = 180; pos2 >= 0; pos2 -= 1) { // goes from 180 degrees to 0 degrees
//    myservo1.write(pos2);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15 ms for the servo to reach the position
//  }
//  
//}

void loop() { 
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input, INPUT_SIZE);
// Add the final 0 to end the C string
  input[size] = 0;

// Read each command pair 
  char* command = strtok(input, "&");
  while (command != 0)
  {
    // Split the command in two values
    char* separator = strchr(command, ':');
    if (separator != 0)
    {
        // Actually split the string in 2: replace ':' with 0
        *separator = 0;
        int servoId = atoi(command);
        ++separator;
        int position = atoi(separator);
        
        // Do something with servoId and position
        if (servoId == 0){
          hori(position);
        }
        if (servoId == 1){
          vert_only(position);
        }
        // Find the next command in input string
       command = strtok(0, "&");
    }
  
  //vert()
  }
  
}
  


  
//  datafromUser=Serial.read();
//
//  if(datafromUser == '1') 
//  {
//    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//      if (datafromUser == '0'){
//        break;
//      }
//      myservo.write(pos);              // tell servo to go to position in variable 'pos'
//      delay(15);                       // waits 15 ms for the servo to reach the position
//  }
//    for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
//      myservo.write(pos);              // tell servo to go to position in variable 'pos'
//      delay(15);                       // waits 15 ms for the servo to reach the position
//  } 
//  }
//  else if(datafromUser == '0')
//  {
//    myservo.write(pos);
//  }
//  
//  else{
//    myservo.detach();
//  }
//    
//}
