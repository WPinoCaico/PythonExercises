void setup() 
{
   Serial.begin(9600);
   pinMode(13, OUTPUT);
}
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      option -= '0';
      if (option == 0)
      {
        digitalWrite(13, LOW);  
      }
      else if (option == 1)
      {
        digitalWrite(13, HIGH);  
      }     
   }
}

