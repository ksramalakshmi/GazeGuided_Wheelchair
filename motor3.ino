// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;
//char read_value='w';
void setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  //Communication with tracking program
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    //delay(600);
    char read_value=Serial.read();
    Serial.println(read_value);
    if (read_value=='f'){
      
      front();
    }
    else if (read_value=='b'){
      back();
    }
    else if (read_value=='r'){
      right();
    }
    else if(read_value=='s'){
      exit(0);
    }
    else if(read_value=='l'){
      left();
    }
    Serial.println(read_value);
  }
}

/*void loop() {
  if(Serial.available()>0){
    //delay(600);
    String read_value=Serial.readString();
    if (read_value=="f"){
      
      front();
    }
    else if (read_value=="b"){
      back();
    }
    else if (read_value=="r"){
      right();
    }
    else if(read_value=="s"){
      exit(0);
    }
    else if(read_value=="l"){
      left();
    }
    Serial.println(read_value);
  }
}*/


// This function lets you control spinning direction of motors
void front(){
  // Set motors to maximum speed
  // For PWM maximum possible values are 0 to 255
  analogWrite(enA, 105);
  analogWrite(enB, 105);

  // Turn on motor A & B
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(500);
  
  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
void back(){
  analogWrite(enA, 105);
  analogWrite(enB, 105);
  // Now change motor directions
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(200);

  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void left(){
  analogWrite(enA, 105);
  analogWrite(enB, 105);
  // Now change motor directions
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(100);

  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void right(){
  analogWrite(enA, 105);
  analogWrite(enB, 105);
  
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(100);

  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
/*// This function lets you control speed of the motors
void speedControl() {
  // Turn on motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  
  // Accelerate from zero to maximum speed
  for (int i = 0; i < 106; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  
  // Decelerate from maximum speed to zero
  for (int i = 105; i >= 0; --i) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  
  // Now turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
*/
