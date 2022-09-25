#include<stdio.h>
#include<conio.h>
void main()
{
 int i,rem,sum=0,c;
 clrscr();
 for(i=101;i<=999;i++)
  {
   while(i!=999)
    {
     rem=i%10;
     sum=sum+rem*rem*rem;
     i=i/10;
    }
   c=sum;
  }
   if(sum==c)
     printf("%d",c);
 getch();
}