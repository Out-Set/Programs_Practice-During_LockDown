#include<stdio.h>
#include<conio.h>
void reverseofano(int x);
void main()
{
 int n;
 clrscr();
 printf("enter the no\n");
 scanf("%d",&n);
 reverseofano(n);
 getch();
}
void reverseofano(int x)
{
 int rem;
 while(x>0)
 {
  rem=x%10;
  printf("%d",rem);
  x=x/10;
 }
}
