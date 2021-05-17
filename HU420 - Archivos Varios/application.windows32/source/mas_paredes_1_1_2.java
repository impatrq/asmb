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

public class mas_paredes_1_1_2 extends PApplet {

pared pared1,pared2,pared3,pared4,pared5;
cubo cubo1;
disparo disparador1;
//cubo cubo2;
//disparo disparador2;
PImage pan= new PImage(); 
int timer=0;

public void setup()
{
    
frameRate(30); 
pan = loadImage("pan.png");
  
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
public void draw()
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
 

public void mousePressed()
{
  cubo1.disparar= true;
  //cubo2.disparar= true;
}
class pared{
  
  
 
  int[] a = new int[0];
  int pared=0;
  int io;
  char[] tipe = new char[0];
  float[] x= new float[0];
  float[] y= new float[0];
  float[] ancho= new float[0];
  float[] alto= new float[0];
  pared(float p1,float p2,float p3,float p4,int pa,char tipo)
  {
    
    if(pa>pared)
    {
    pared= pa;
   
     a = new int[pa];
     tipe = new char[pa];
     x= new float[pa];
     y= new float[pa];
     ancho= new float[pa];
     alto= new float[pa];
     
    }
    
    pa=pa-1;
    a[pa]=color(100,60,50);
    tipe[pa]=tipo;
    x[pa]=p1;
    y[pa]=p2;
    ancho[pa]=p3;
    alto[pa]=p4;
  }
  public void display()
  {
    for(int i=0;i<pared;i++)
    {
      
      fill(a[i]);
      rect(x[i],y[i],ancho[i],-alto[i]);
      fill(255,255,255);
    }
    
    
  }
  public void chocar(float xi,float yi,int m,int N)
  {
    for(int i=0;i<pared;i++)
    {
      io=i;
      
      if(yi<y[i] && yi>y[i]-alto[i] && xi>x[i] && xi<x[i]+ancho[i])
      {
        
          boolean p=true;
          tipo(tipe[i],m,N,i,p);
        
        if(yi<y[i] && yi>y[i]-alto[i])
        
          p=false;
         tipo(tipe[i],m,N,i,p);
                
        
      }
    }
    io=0;
  {
    //romper rebotar o pintar
  }
  }
  public void tipo(char Tipo, int m,int N,int i,boolean p)
  {
    switch(Tipo)
  {
    
    case ('p'):
    if(i==0)pared1.pintar(5,10,10);
    if(i==1)pared2.pintar(1,2,2);
    if(i==2)pared3.pintar(5,10,10);
    break;
    case ('r'):
    if(N==1)disparador1.cambio(m,p);
   // if(N==2)disparador2.cambio(m);                        //aca
    break;
    case ('e'):
    if(N==1) disparador1.explotar(m) ; 
    //if(N==2) disparador2.explotar(m) ;;
    
    
    
    break;
    default:
    print(Tipo);
    break;
  }
  }
  public void pintar(int R,int G,int B)
  {
    a[io]=a[io]+color(R,G,B);   
  }
  public void romper()
  {
    
  }
}
//class ParedDura extends pared  {
  

  
class cubo {
  cubo(float ix,float iy,char ai,char si,char di,char wi)
  {
  x= ix;
  y= iy;
  a=ai;
  s=si;
  d=di;
  w=wi;
  }

  char[] tecla= new char[4];
  char a,s,d,w;
  float x;
  float y;
  float l=30;
  float v=5.6f;
  boolean disparar;
  float xp,yp;
  public void mover(float xp,float yp)
  {
    x=x+xp*v;
    y=y+yp*v;
  }
  public void actualizar()
  {
    xp=0;yp=0;
    if(keyPressed)
    { for(int i=0;i<3;i++)
    {
      tecla[i]=key;
    }
     for(int i=0;i<3;i++)
    {
      if (tecla[i]==a)
      {xp=-1;}
      if(tecla[i]==s)
      {yp=1;}
      if(tecla[i]==d)
      {xp=1;}
      if(tecla[i]==w)
      {yp=-1;}   
    
    }
  }
    
  }
  public void dibujar(PImage pan)
  {
    mover(xp,yp);
    rect(x,y,l,l);
    image(pan,x,y,l,l);
  }
  

}
class disparo
{
  int N;
  int m=0;
  int ball;
  disparo(int balas,int Ntirador)
  {
  ball=balas;
  vi= new PVector[ball];
  pos= new PVector[ball];
  N=Ntirador;
  
  }
  
  PVector[] vi= new PVector[0];
  PVector[] pos= new PVector[0];
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
    vi[disparos].x= (mouseX-x)/50;
    vi[disparos].y= (mouseY-y)/50;
  
    pos[disparos].x= x;
    pos[disparos].y= y;    
   
    
    }
    if(disparos>=ball){print("listo");}
    
    //a[disparos].div(dist(mouseX,mouseY,width,height));;
    //b[disparos]=disparos;
  }
  
   public void actualizar()
  { 
    while(m<disparos+1)
    { 
      if(m<ball)
      {
      pos[m].x=pos[m].x+vi[m].x;
      pos[m].y=pos[m].y+vi[m].y;
      }
      
      pared1.chocar(pos[m].x,pos[m].y,m,N);                    /// cambio
      pared2.chocar(pos[m].x,pos[m].y,m,N);
      pared3.chocar(pos[m].x,pos[m].y,m,N);
      pared4.chocar(pos[m].x,pos[m].y,m,N);
      pared5.chocar(pos[m].x,pos[m].y,m,N);
     // pared6.chocar(pos[m].x,pos[m].y,m,N);
      m++;
      
    }
    m=0;  
  }
  public void cambio(int m,boolean p)
  {
    if(p)
    {
      if(pos[m].x>0)
    vi[m].x=-vi[m].x;
    }
    if(p)
    {
    vi[m].y=-vi[m].y;
    }
  }
  public void explotar(int m)
  {
    pos[m].x= -10;
    pos[m].y= -10;
    vi[m].x=0;
    vi[m].y=0;
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
  public void settings() {  size(1000,700); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "--present", "--window-color=#666666", "--stop-color=#cccccc", "mas_paredes_1_1_2" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
