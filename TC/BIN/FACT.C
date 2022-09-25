#include<stdio.h>
void main()
{
 int i,n,fact=1;
 clrscr();
 printf("enter the n \n");
 scanf("%d",&n);
 for(i=1;i<=n;i++)
 {
 fact=fact*i;
 printf("\n%d",fact);
 }
 getch();
}