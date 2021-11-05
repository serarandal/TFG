#include <ESP8266WiFi.h>
#include <ArduinoOTA.h>

#include "config.h"  // Sustituir con datos de vuestra red
#include "ESP8266_Utils.hpp"
#include "ESP8266_Utils_OTA.hpp"
#include "Code.hpp"

void setup(){
	Serial.begin(115200);

	ConnectWiFi_STA();

	InitOTA();
  InitCODE();
}

void loop(){
	ArduinoOTA.handle();
  UseCODE();
}
