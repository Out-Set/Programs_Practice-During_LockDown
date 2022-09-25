#include <stdio.h>
#include <stdlib.h>
int swap(int,int);
void main()
{
	int a,b,c;
	printf("entre the no");
	scanf("%d%d",&a,&b);
	c=swap(a,b);
	printf("after swapping a= %d,b= %d",b,a);	
}
int swap(int a,int b)
{
	a=a+b;
	b=a-b;
	a=a-b;
	return(b,a);
}
