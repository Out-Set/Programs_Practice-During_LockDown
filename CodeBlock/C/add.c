#include<graphics.h>
int main()
{
	int gd=0;gm;
	initgraph(&gd,&gm,"");
    circle(300,200,100);
    getch();
    closegraph();
}
