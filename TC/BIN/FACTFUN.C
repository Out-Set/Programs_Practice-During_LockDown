#include<stdio.h>
#include<conio.h>
void fact(int x);
int main()
{
 int n;
 clrscr();
 printf("enter the value of n");
 scanf("%d",&n);
 fact(n);
 getch();
 return 0;
}
void fact(int x)
{
 int i,fact=1;
 for(i=1;i<=x;i++)
  {
   fact=fact*i;
   printf("%d\n",fact);
  }
}