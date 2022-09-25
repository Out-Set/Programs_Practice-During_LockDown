#include<stdio.h>
void main()
{
 int a,b,c;
 float x;
 clrscr();
 printf("enter the values of a,b,c\n");
 scanf("%d%d%d",&a,&b,&c);
 x=a/(b-c);
 printf("x=%f",x);
 getch();
}