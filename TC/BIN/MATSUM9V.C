#include<stdio.h>
void main()
{
 int a[9],i,sum=0;
 clrscr();
 for(i=0;i<9;i++)
  {
   printf("enter the value for a[%d]",i);
   scanf("%d",&a[i]);
   sum=sum+a[i];
  }
  printf("sum=%d\n",sum);
 getch();
}