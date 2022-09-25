#include<stdio.h>
void main()
{
int n,rem;
clrscr();
printf("enter the no");
scanf("%d",&n);
while(n>0)
 {
  rem=n%10;
  printf("%d",rem);
  n=n/10;
 }
 getch();
}