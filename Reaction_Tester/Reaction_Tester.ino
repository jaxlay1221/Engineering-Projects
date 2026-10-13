const int Led_Pin = 8;
const int Button = 3;
const int Start_Button = 5;

void setup(){
Serial.begin(9600);
pinMode(Led_Pin, OUTPUT);
pinMode(Button, INPUT_PULLUP);
pinMode(Start_Button, INPUT_PULLUP);
randomSeed(analogRead(A0));
}

unsigned long LedOnTime = 0;
unsigned long wait_start =  0;
int state = 5;
unsigned long random_delay = random(2000,5000);



void loop(){
  if (state == 5){
    if (digitalRead(Start_Button) == LOW){
  wait_start = millis();
  state = 0;}
  }
else if (state == 0){
  if (millis() - wait_start >= random_delay){
  digitalWrite(Led_Pin, HIGH);
  LedOnTime = millis();
  state = 1;
  }
  else if (digitalRead(Button) == LOW and millis() - wait_start < random_delay){
    Serial.print("False Start");
    state = 5;
  }
}

else if (state == 1){
  if (digitalRead(Button) == LOW){
    digitalWrite(Led_Pin, LOW);
    Serial.print("Reaction Time:"); Serial.println(millis() - LedOnTime);
    state = 2;
  }
}
else if (state == 2){
  random_delay = random(2000,5000);
  state = 5;
 }
}


