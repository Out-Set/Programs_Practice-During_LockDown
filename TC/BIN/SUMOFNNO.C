#include<stdio.h>
void main()
{
 int n,newn,i,sum=0;
 clrscr();
 printf("enter the no\n");
 scanf("%d",&n);
   for(i=1;i<=n;i++)
    {
     printf("enter the no's\n");
     scanf("%d",&newn);
     sum=sum+newn;
    }
 printf("sum of given n no=%d",sum);
 getch();
}