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
    vi[disparos].x= (mouseX-x)/50;
    vi[disparos].y= (mouseY-y)/50;
  
    pos[disparos].x= x;
    pos[disparos].y= y;    
   
    
    }
    if(disparos>=ball){print("listo");}
    
    //a[disparos].div(dist(mouseX,mouseY,width,height));;
    //b[disparos]=disparos;
  }
  
   void actualizar()
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
  void cambio(int m,boolean p)
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
  void explotar(int m)
  {
    pos[m].x= -10;
    pos[m].y= -10;
    vi[m].x=0;
    vi[m].y=0;
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
