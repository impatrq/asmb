class cubo {
  float x;
  float y;
  float l=10;
  float v=1;
  boolean disparar;
  float xp,yp;
  void mover(float xp,float yp)
  {
    x=x+xp*v;
    y=y+yp*v;
  }
  void actualizar()
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
  void dibujar()
  {
    mover(xp,yp);
    rect(x,y,l,l);
  }
  

}
