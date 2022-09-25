#include<stdio.h>
#include<conio.h>
int swap(int x,int y);
main()
{
 int a,b,c;
 clrscr();
 printf("enter the two no");
 scanf("%d%d",&a,&b);
 printf(" before swapping a=%d,b=%d",a,b);
 swap(a,b);
 getch();
}
int swap(int x,int y)
{
 int s,d;
 s=x;
 x=y;
 y=s;
 d=printf("after swapping a=%d,b=%d",x,y);
 return d;
}