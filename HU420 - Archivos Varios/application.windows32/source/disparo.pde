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
  void SetupVectors()
  {
    int i=0;
    while(i<ball)
    {
    vi[i]= new PVector();
    pos[i]= new PVector();
    i++;
    }
  }
  void fuego(float x,float y)
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
  
  void actualizar()
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
  void dibujar(float r)
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
