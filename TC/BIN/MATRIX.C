#include<stdio.h>
void main()
{
int arr[5],i;
clrscr();
for(i=0;i<5;i++)
  {
   printf("enter the value for arr[%d]",i);
   scanf("%d",&arr[i]);
  }
printf("the array elements are:\n");
for(i=0;i<5;i++)
printf("%d\t",arr[i]);
printf("\n");
getch();
}
