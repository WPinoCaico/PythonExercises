long randNumber;

void setup(){
  Serial.begin(9600);

  // Si el pin A0 esta desconectado, entregara datos random
  // noise will cause the call to randomSeed() to generate
  // different seed numbers each time the sketch runs.
  // randomSeed() will then shuffle the random function.
  randomSeed(analogRead(0));
}

void loop() {
  // imprimir un numero random desde 25 a 41
  randNumber = random(25, 41);
  Serial.println(randNumber);

  delay(500);
}
