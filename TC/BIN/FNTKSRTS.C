#include<stdio.h>
#include<conio.h>
int add(int x,int y);
void main()
{
 int a,b,s;
 clrscr();
 printf("enter the two no");
 scanf("%d%d",&a,&b);
 s=add(a,b);
 printf("sum of two no is=%d",s);
 getch();
}
int add(int x,int y)
{
 int c;
 c=x+y;
 return c;
}