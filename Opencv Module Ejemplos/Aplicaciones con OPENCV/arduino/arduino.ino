void setup() 
{
   Serial.begin(9600);
   pinMode(12, OUTPUT);
}
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.read();
      option -= '0';
      if (option == 0)
      {
        digitalWrite(12, LOW);  
      }
      else if (option == 1)
      {
        digitalWrite(12, HIGH);  
      }     
   }
}

