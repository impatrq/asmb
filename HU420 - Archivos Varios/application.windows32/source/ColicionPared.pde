class pared{
  
  
 
  color[] a = new color[0];
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
   
     a = new color[pa];
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
  void display()
  {
    for(int i=0;i<pared;i++)
    {
      
      fill(a[i]);
      rect(x[i],y[i],ancho[i],-alto[i]);
      fill(255,255,255);
    }
    
    
  }
  void chocar(float xi,float yi,int m,int N)
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
  void tipo(char Tipo, int m,int N,int i,boolean p)
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
  void pintar(int R,int G,int B)
  {
    a[io]=a[io]+color(R,G,B);   
  }
  void romper()
  {
    
  }
}
//class ParedDura extends pared  {
  

  
