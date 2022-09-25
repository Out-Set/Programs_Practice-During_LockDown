#include<stdio.h>
void main()
{
 int i,n;
 clrscr();
 printf("enter the no\n");
 scanf("%d",&n);
 for(i=1;i<=10;i++)
   printf("%dx%d=%d\n",n,i,n*i);
 getch();
}