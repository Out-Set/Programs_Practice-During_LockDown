#include <stdio.h>
void main()
{
	int a1[5]={1,12,23,45,6},a2[5]={3,5,7,9,11},a3[10];
	int i,j,t,k=0;
	for(i=0;i<10;i++)
	{
		for(k=0;k<10;k++)
		{
		
	    	if(i<4)
	    	{
		    	a3[i]=a2[k];
		    	k++;
	    	}
		}
		a3[i]=a1[i];
	}
	printf("elements are::");
	for(i=0;i<10;i++)
	 printf("%d\n",a3[i]);
}
