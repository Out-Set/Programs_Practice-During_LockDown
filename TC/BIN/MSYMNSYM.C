#include<stdio.h>
main()
{
int i,j,a[3][3],b[3][3],x=0;
 printf("enter the value for matrix\n");
 for(i=0;i<3;i++)
 {
  for(j=0;j<3;j++)
  {
   scanf("%d",&a[i][j]);
  }
  printf("\n");
 }

 for(i=0;i<3;i++)
 {
  for(j=0;j<3;j++)
  {
   b[j][i]=a[i][j];
  }
 }
 for(i=0;i<3;i++)
 {
  for(j=0;j<3;j++)
  {
   if(a[i][j]!=b[i][j])
   {
   	x++;
   }
  }
 }
 x==0?printf("symmetric"):printf("not symmetric");
 return(0);
}
