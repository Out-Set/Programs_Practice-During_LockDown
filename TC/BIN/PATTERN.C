#include<stdio.h>
void main()
{
 int i,j,n,choice;
 while(1)
 {
  clrscr();
  printf("enter your choice:\n1:binary pattern\n2:star pattern\n3:exit");
  switch(choice)
  {
   case 1:
    printf("enter the no of rows\n");
    scanf("%d",&n);
    for(i=0;i<=n;i++)
     {
       for(j=0;j<=i;j++)
	{
	  (i+j)%2==0?printf("0"):printf("1");
	}
       printf("\n");
     }
     break;
   case 2:
    printf("enter the no of rows\n");
    scanf("%d",&n);
    for(i=0;i<=n;i++)
     {
       for(j=0;j<=i;j++)
	{
	 printf("*");
	}
       printf("\n");
     }
    break;
   case 3: exit(0);
   default:
     printf("invalid choice");
  }
 getch();
 }
}