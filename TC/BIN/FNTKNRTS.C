#include<stdio.h>
#include<conio.h>
int add(void);
void main()
{
 int s;
 clrscr();
 s=add();
 printf("sum of two no is=%d",s);
 getch();
}
int add(void)
{
 int a,b,c;
 printf("enter the two no");
 scanf("%d%d",&a,&b);
 c=a+b;
 return c;
}