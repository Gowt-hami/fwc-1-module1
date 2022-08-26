#include<Arduino.h>
int Z,Y,X,W,F;
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(5, OUTPUT);
    pinMode(6, INPUT);  
    pinMode(7, INPUT);
    pinMode(8, INPUT);
    pinMode(9, INPUT);
    
}

// the loop function runs over and over again forever
void loop() {
  
W = digitalRead(6);//LSB  
X = digitalRead(7);  
Y = digitalRead(8);  
Z = digitalRead(9);//MSB  
F=(X&&!Y&&Z)||(!X&&!Y&&Z)||(!W&&X&&Y)||(W&&!X&&Y)||(W&&X&&Y);
digitalWrite(5,F);
}
