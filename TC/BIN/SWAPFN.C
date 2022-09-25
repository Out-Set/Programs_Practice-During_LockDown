#include<stdio.h>
#include<conio.h>
void swapv(int x,int y);
void main()
{
 int a,b;
 clrscr();
 printf("enter the two no\n");
 scanf("%d%d",&a,&b);
 printf("before the swapping a=%d,b=%d\n",a,b);
 swapv(a,b);
 getch();
}
void swapv(int x,int y)
{
 int t;
 t=x;
 x=y;
 y=t;
 printf("after the swapping a=%d,b=%d",x,y);
}