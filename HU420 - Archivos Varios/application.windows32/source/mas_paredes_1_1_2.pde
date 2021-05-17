pared pared1,pared2,pared3,pared4,pared5;
cubo cubo1;
disparo disparador1;
//cubo cubo2;
//disparo disparador2;
PImage pan= new PImage(); 
int timer=0;

void setup()
{
    
frameRate(30); 
pan = loadImage("pan.png");
  size(1000,700);
  pared1 = new pared(900,600,50,500,1,'r');
  pared2 = new pared(400,300,500,50,2,'p');
  pared3 = new pared(900,600,50,500,3,'p');
  pared4 = new pared(100,600,50,500,4,'r');
  pared5 = new pared(100,600,500,50,4,'e');

  cubo1 = new cubo(10,30,'a','s','d','w');
 // cubo2 = new cubo(100,30,'j','k','l','i');
  disparador1 = new disparo(100,1);
 // disparador2 = new disparo(100,2);
  disparador1.SetupVectors();
 // disparador2.SetupVectors();
}
void draw()
{
  
background(200);
  cubo1.actualizar();
 // cubo2.actualizar();
  cubo1.dibujar(pan);
 // cubo2.dibujar(pan);
  //pared1.display();
  pared3.display();
  pared2.display();
  pared4.display();
  pared5.display();
  disparador1.actualizar();
 // disparador2.actualizar();
 disparador1.dibujar(1);
// disparador2.dibujar(1);
  if(cubo1.disparar){
 disparador1.fuego(cubo1.x+15,cubo1.y+15);
 cubo1.disparar=false;
 timer++;
  }
  //if(cubo2.disparar){
// disparador2.fuego(cubo2.x+15,cubo2.y+15);
// cubo2.disparar=false;
}
 

void mousePressed()
{
  cubo1.disparar= true;
  //cubo2.disparar= true;
}
