#include <stdio.h>
void main()
{
	int i,j,a[5],t;
	printf("enter 5 numbers\n");
	for(i=0;i<5;i++)
	  scanf("%d",&a[i]);
	for(i=0;i<5;i++)
	  printf("%d\t",a[i]);
	  printf("\n");
	for(j=0;j<4;j++)
	  {
	  	for(i=j+1;i<5;i++)
	  	{
	  	 if(a[j]>a[i])
		   {
		   	t=a[i];
		   	a[i]=a[j];
		   	a[j]=t;
		   }	
		}
	  }
	  printf("sorted elements are::");
	  for(i=0;i<5;i++)
	    printf("%d\t",a[i]);
}
