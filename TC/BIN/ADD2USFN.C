#include<stdio.h>
#include<conio.h>
int add(int a,int b);
void main()
{
int a,b,c;
clrscr();
printf("enter the two no");
scanf("%d%d",&a,&b);
c=add(a,b);
printf("%d",c);
getch();
}
int add(int a,int b)
{
int s;
   s=a+b;
   return(s);
}