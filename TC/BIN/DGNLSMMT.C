#define r 3
#define c 3
#include<stdio.h>
void main()
{
 int i,j,a[r][c],sum=0;
 clrscr();
 printf("enter the no for matrix\n");
 for(i=0;i<r;i++)
  for(j=0;j<c;j++)
   scanf("%d",&a[i][j]);


 for(i=0;i<r;i++)
  for(j=0;j<c;j++)
    if(i==j)
     sum=sum+a[i][j];
 printf("\nsum of diagonal are %d",sum);
 getch();
}