#include<stdio.h>
#include<conio.h>
void swapr(int *x,int *y);
int main()
{
int a,b;
clrscr();
printf("enter the values of a and b");
scanf("%d%d",&a,&b);
printf("\n before swaping a=%d,b=%d",a,b);
swapr(&a,&b);
getch();
return 0;
}
void swapr(int *x,int *y)
{
int t;
t=*x;
*x=*y;
*y=t;
printf("\n after swaping a=%d,b=%d",*x,*y);
}