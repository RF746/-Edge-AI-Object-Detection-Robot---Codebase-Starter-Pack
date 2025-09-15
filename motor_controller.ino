C++ Sketch: `motor_controller.ino`


```cpp
#define IN1 5
#define IN2 6
#define ENA 9


String command = "";


void setup() {
Serial.begin(9600);
pinMode(IN1, OUTPUT);
pinMode(IN2, OUTPUT);
pinMode(ENA, OUTPUT);
}


void loop() {
if (Serial.available()) {
command = Serial.readStringUntil('\n');
command.trim();


if (command == "avoid") {
digitalWrite(IN1, LOW);
digitalWrite(IN2, HIGH);
analogWrite(ENA, 150);
} else if (command == "follow") {
digitalWrite(IN1, HIGH);
digitalWrite(IN2, LOW);
analogWrite(ENA, 200);
} else if (command == "stop") {
digitalWrite(IN1, LOW);
digitalWrite(IN2, LOW);
analogWrite(ENA, 0);
}
}
}
```
