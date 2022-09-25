#include <stdio.h>
void input(int *p)
{
	int i;
	for(i=0;i<5;i++)
	scanf("%d",(p+i));
}
void sort(int *p)
{
	int i,j,t;
	for(j=o;j<5;j++0)
	{
		for(i=0;i<4-j;i++)
		{
			if(*(p+i)>*(p+i+1))
			{
				t=*(p+i);
				*(p+i)=*(p+i+1);
				*(p+i+i)=t;
			}
		}
	}
}
void disp(int *p)
{
	int i;
	for(i=0;i<5;i++)
	printf("%d",*(p+i));
}
void main()
{
	int a[5];
	input(a);
	sort(a);
	disp(a);
}
