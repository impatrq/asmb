import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Clases__cubo_dispara_1_0_0 extends PApplet {

PVector c1;
cubo cubo1;
disparo disparador1;
public void setup()
{
  
  cubo1 = new cubo();
  disparador1 = new disparo(100);
  disparador1.SetupVectors();
}
public void draw()
{
  
background(200);
  cubo1.dibujar();
  disparador1.actualizar();
 disparador1.dibujar(10);
  if(cubo1.disparar){
 disparador1.fuego(cubo1.x,cubo1.y);
  }
 
}

public void keyPressed()
{
  cubo1.actualizar();
}
public void mousePressed()
{
  cubo1.disparar= true;
 
}
class cubo {
  float x;
  float y;
  float l=10;
  float v=1;
  boolean disparar;
  float xp,yp;
  public void mover(float xp,float yp)
  {
    x=x+xp*v;
    y=y+yp*v;
  }
  public void actualizar()
  {
    if(keyPressed)
    {
      xp=0;yp=0;
      if (key=='a')
      {xp=-1;}
      if(key=='s')
      {yp=1;}
      if(key=='d')
      {xp=1;}
      if(key=='w')
      {yp=-1;}   
    }
  }
  public void dibujar()
  {
    mover(xp,yp);
    rect(x,y,l,l);
  }
  

}
class disparo
{
  int m=0;
  int ball;
  disparo(int balas)
  {
  ball=balas;
  vi= new PVector[ball];
  pos= new PVector[ball];
  }
  
  PVector[] vi= new PVector[ball];
  PVector[] pos= new PVector[ball];
  int cort;
  
  float v;
  int disparos=-1;
  public void SetupVectors()
  {
    int i=0;
    while(i<ball)
    {
    vi[i]= new PVector();
    pos[i]= new PVector();
    i++;
    }
  }
  public void fuego(float x,float y)
  {
    disparos++;
    if(disparos<ball){
    vi[disparos].x= (mouseX-x)/100;
    vi[disparos].y= (mouseY-y)/100;
  
    pos[disparos].x= x;
    pos[disparos].y= y;    
    ellipse(pos[disparos].x,pos[disparos].y,10,10);
    
    }
    if(disparos>=ball){print("listo");}
    cubo1.disparar=false;
    //a[disparos].div(dist(mouseX,mouseY,width,height));;
    //b[disparos]=disparos;
  }
  
  public void actualizar()
  { 
    while(m<disparos+1)
    {
      if(m<ball){
      pos[m].x=pos[m].x+vi[m].x;
      pos[m].y=pos[m].y+vi[m].y;}
      m++;
    }
    m=0;  
  }
  public void dibujar(float r)
  {
    while(m<disparos+1)
    {
      if(m<ball){
    ellipse(pos[m].x,pos[m].y,r,r); }
    m++;
    }
    m=0;
  }
}
  public void settings() {  size(800,600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "--present", "--window-color=#666666", "--stop-color=#cccccc", "Clases__cubo_dispara_1_0_0" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
