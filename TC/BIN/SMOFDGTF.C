#include<stdio.h>
#include<conio.h>
int sumofdigit(int x);
void main()
{
 int n,s;
 clrscr();
 printf("enter the no");
 scanf("%d",&n);
 s=sumofdigit(n);
 printf("sum of entered digit is=%d",s);
 getch();
}
int sumofdigit(int x)
{
 int sum=0,rem;
 while(x>0)
 {
  rem=x%10;
  sum=sum+rem;
  x=x/10;
 }
 return sum;
}