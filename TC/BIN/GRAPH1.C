#include<graphics.h>
void main()
{
 int gd=0,gm;
 initgraph(&gd,&gm,"");
 circle(15,10,7);
 getch();
 closegraph();
}