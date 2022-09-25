 /* wap in c to add 5 no */
#include<stdio.h>
void main()
{
 int a[5],i,sum=0;
 clrscr();
 for(i=0;i<5;i++)
  {
   printf("enter the value for a[%d]\n",i);
   scanf("%d",&a[i]);
   sum=sum+a[i];
  }
 printf("sum=%d\n",sum);
 getch();
}
