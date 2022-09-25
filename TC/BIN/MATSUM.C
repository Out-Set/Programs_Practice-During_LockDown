#define ROW 3
#define COL 4
#include<stdio.h>
void main()
{
 int i,j,mat1[ROW][COL],mat2[ROW][COL],mat3[ROW][COL];
 clrscr();
 printf("enter the value for mat1(%d%d)row wise:\n",ROW,COL);
   for(i=0;i<ROW;i++)
    for(j=0;j<COL;j++)
      scanf("%d",&mat1[i][j]);
 printf("enter the value for mat2(%d%d)row wise:\n",ROW,COL);
   for(i=0;i<ROW;i++)
    for(j=0;j<COL;j++)
      scanf("%d",&mat2[i][j]);

 for(i=0;i<ROW;i++)
  for(j=0;j<COL;j++)
   mat3[i][j]=mat1[i][j]+mat2[i][j];
    printf("the resultant matrix is:\n");
     for(i=0;i<ROW;i++)
     {
       for(j=0;j<COL;j++)
       {
	printf("%d ",mat3[i][j]);
       }
	 printf("\n");
     }
 getch();
}