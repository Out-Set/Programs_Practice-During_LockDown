#include<stdio.h>
#include<conio.h>
void main()
{
 int c,n,rem,sum=0;
 clrscr();
 printf("enter the no");
 scanf("%d",&n);
 c=n;
 while(c!=0)
  {
   rem=c%10;
   sum=sum+rem*rem*rem;
   c=c/10;
  }
 if(sum==n)
   printf("%d is armstrong no",n);
 else
   printf("%d is not an armstrong no",n);
 getch();
}