PVector c1;
cubo cubo1;
disparo disparador1;
void setup()
{
  size(800,600);
  cubo1 = new cubo();
  disparador1 = new disparo(100);
  disparador1.SetupVectors();
}
void draw()
{
  
background(200);
  cubo1.dibujar();
  disparador1.actualizar();
 disparador1.dibujar(10);
  if(cubo1.disparar){
 disparador1.fuego(cubo1.x,cubo1.y);
  }
 
}

void keyPressed()
{
  cubo1.actualizar();
}
void mousePressed()
{
  cubo1.disparar= true;
 
}
