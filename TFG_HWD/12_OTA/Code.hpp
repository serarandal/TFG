void InitCODE()
{
	pinMode(LED_BUILTIN,OUTPUT);
}

void UseCODE()
{
	digitalWrite(LED_BUILTIN,LOW);
	delay(1000);
	digitalWrite(LED_BUILTIN,HIGH);
	delay(1000);
}
