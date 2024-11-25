#include <FastLED.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// LED setup
#define NUM_LEDS 36
#define DATA_PIN 8
CRGB leds[NUM_LEDS];

// Temperature sensor setup
#define ONE_WIRE_BUS 6
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
    // Initialize LED strip
    FastLED.addLeds<WS2811, DATA_PIN, GRB>(leds, NUM_LEDS);
    FastLED.clear();
    FastLED.show();

    // Initialize temperature sensors
    sensors.begin();

    // Initialize serial communication
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil(',');

        if (command == "LightUp") {
            int intensity = Serial.parseInt();
            int ledNumber = Serial.parseInt();
            if (ledNumber >= 0 && ledNumber < NUM_LEDS) {
                leds[ledNumber] = CRGB(intensity, intensity, intensity);
                FastLED.show();
                Serial.println("OK,%d,%d", intensity, ledNumber);
            }
        } else if (command == "Sense") {
            uint64_t address = Serial.parseInt();
            DeviceAddress deviceAddress;
            memcpy(&deviceAddress, &address, sizeof(deviceAddress));
            sensors.requestTemperaturesByAddress(deviceAddress);
            float temperatureC = sensors.getTempC(deviceAddress);
            Serial.print("Temperature: ");
            Serial.println(temperatureC);
        }
    }
}
