#include<stdio.h>
void sum(int x);
main()
{
 int n;
 print("enter the value of n");
 scanf("%d",&n);
 sum(n);
 getch();
}
int sum(int x)
{
 int i,sum=0;
 for(i=0;i<=x;i++)
  {
   sum=sum+i;
   printf("%d",sum);
  }
}