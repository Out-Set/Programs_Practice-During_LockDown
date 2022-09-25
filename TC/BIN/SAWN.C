#include<stdio.h>
void main()
{
int i,n,sum=0;
 clrscr();
 printf("enter the n\n");
 scanf("%d",&n);
 for(i=1;i<=n;i++)
 {
  sum=sum+i;
  printf("\n%d",sum);
 }
  getch();
}
