#include<stdio.h>
#include<conio.h>
void add(int x,int y);
void main()
{
 int a,b;
 clrscr();
 printf("enter the two no\n");
 scanf("%d%d",&a,&b);
 add(a,b);
 getch();
}
 void add(int x,int y)
{
 int c;
 c=x+y;
 printf("sum of two no is=%d",c);
}