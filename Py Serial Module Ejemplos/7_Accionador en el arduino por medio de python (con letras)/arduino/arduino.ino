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
      if (option == 'e')
        {digitalWrite(13,HIGH);}
      else if (option == 'a')  
          {digitalWrite(13,LOW);} 
   }
}

