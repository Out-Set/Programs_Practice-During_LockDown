#include<stdio.h>
#include<conio.h>
void add(void);
void main()
{
 clrscr();
 add();
 getch();
}
void add(void)
{
 int s,a,b;
 printf("enter the two no\n");
 scanf("%d%d",&a,&b);
 printf("sum of the two no=%d",a+b);
}