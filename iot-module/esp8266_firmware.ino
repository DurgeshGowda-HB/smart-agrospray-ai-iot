// Smart AgroSpray - ESP8266 Firmware
// Controls pesticide spray based on AI signal

#define RELAY_PIN 5   // GPIO5 (D1)
#define BAUD_RATE 9600

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);  // Ensure spray is OFF at start

  Serial.begin(BAUD_RATE);
  Serial.println("Smart AgroSpray System Ready");
}

