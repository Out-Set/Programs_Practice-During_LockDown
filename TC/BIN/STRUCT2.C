#include<stdio.h>
long fact(int n);
int main(void)
{
 int num;
 clrscr();
 printf("enter a number\n");
 scanf("%d",&num);
 if(num<0)
  printf("no factorial for -ve");
 else
  printf("factorial of %d is %d\n",num,fact(num));
  getch();
  return 0;
}
long fact(int n)
{
 if(n==0)
 return 1;
 return(n*fact(n-1));
}
