void setup() 
{
   Serial.begin(9600);
   pinMode(13, OUTPUT);
}
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.parseInt();
      if (option >0)
      {     
      for (int i=0;i<option;i++)
        {
          digitalWrite(13,HIGH);
          delay(250);
          digitalWrite(13,LOW);
          delay(250);
         
        } 
      }
     option = 0;        
   }
}

