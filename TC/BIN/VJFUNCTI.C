#include<stdio.h>

int printline (int n)
 main()
{
 int x;
 printf("enter value of x");
 scanf("%d",&x);
printline(x);
}
int printline(int n)
{
int i;
for(i=1;i<=n;i++)
{
printf("%d",i);
}
}