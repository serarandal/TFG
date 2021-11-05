#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>


IPAddress local_IP(192, 168, 1, 110);
IPAddress gateway(192, 168, 1, 2);
IPAddress subnet(255, 255, 0, 0);
const char *ssid = "MOVISTAR_610B";
const char* password = "23F9CACA7C5270A0C677";

ESP8266WebServer server(70);


 
void handleRootPath() 
{            
  server.send(200, "text/plain", "Hello world,send motor data to /data/");
}

void handleSentVar()
{
  if(server.hasArg("plain")==false)
  {
    server.send(200,"text/plain","Data not received");
    return;
  }
  String message = "Body received:\n";
  message += server.arg("plain");
  message += "\n";
 
  server.send(200, "text/plain", message);
  Serial.println(server.arg("plain"));
  controlMotor(server.arg("plain"));
  
}

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void controlMotor(String data)
{
  String data2 = getValue(data, '&',0);
   String angle = getValue(data2, '=',0);
   String strength = getValue(data,'=',1);
   int angleX = angle.toInt();
   int strengthX = strength.toInt();
  int analogStrength = StrengthToAnalog(strengthX);
if(angleX>0 && angleX <90)
{
  //rigth motor
  digitalWrite(2,HIGH);
  digitalWrite(0,LOW);
  analogWrite(4,analogStrength/2);
  //left motor
  digitalWrite(15,HIGH);
  digitalWrite(13,LOW);
  analogWrite(12,analogStrength);
}
if(angleX>90 && angleX <180)
{
  //rigth motor
  digitalWrite(2,HIGH);
  digitalWrite(0,LOW);
  analogWrite(4,analogStrength);
  //left motor
  digitalWrite(15,HIGH);
  digitalWrite(13,LOW);
  analogWrite(12,analogStrength/2);
}
if(angleX>180 && angleX <270)
{
  //rigth motor
  digitalWrite(2,LOW);
  digitalWrite(0,HIGH);
  analogWrite(4,analogStrength);
  //left motor
  digitalWrite(15,LOW);
  digitalWrite(13,HIGH);
  analogWrite(12,analogStrength/2);
}
if(angleX>270 && angleX <360)
{
  //rigth motor
  digitalWrite(2,LOW);
  digitalWrite(0,HIGH);
  analogWrite(4,analogStrength/2);
  //left motor
  digitalWrite(15,LOW);
  digitalWrite(13,HIGH);
  analogWrite(12,analogStrength);
}
   
}

int StrengthToAnalog(float strengthX)
{
  return (strengthX*255)/100;
}

void setup() {
 Serial.begin(115200);
 WiFi.config(local_IP,gateway,subnet);
 WiFi.begin(ssid,password);
 
 while(WiFi.status() != WL_CONNECTED)
 {
  delay(500);
  Serial.println("waiting to connect..."); 
 }

 server.on("/",handleRootPath);
 server.on("/data/",handleSentVar);
 server.begin();
 Serial.println("Server listening");
 Serial.println(WiFi.localIP());

 
 pinMode(2,OUTPUT);
 pinMode(0,OUTPUT);
 pinMode(4,OUTPUT); //analogWriting (PWM)
 
 pinMode(15,OUTPUT);
 pinMode(13,OUTPUT);
 pinMode(12,OUTPUT);//analogWriting (PWM)
}

void loop() {
  
 server.handleClient();
 
 
}
