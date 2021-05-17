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
  float v=5.6;
  boolean disparar;
  float xp,yp;
  void mover(float xp,float yp)
  {
    x=x+xp*v;
    y=y+yp*v;
  }
  void actualizar()
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
  void dibujar(PImage pan)
  {
    mover(xp,yp);
    rect(x,y,l,l);
    image(pan,x,y,l,l);
  }
  

}
