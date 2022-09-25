#include<stdio.h>
void main()
{
 int a,b;
 clrscr();
 printf("enter the value of a & b\n");
 scanf("%d%d",&a,&b);
 a>b?printf("%d is greatest",a):printf("%d is greatest",b);
 getch();
}