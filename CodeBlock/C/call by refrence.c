#include <stdio.h>
#include <conio.h>
void sum(int *x);
void main()
{
	int n=5;
	clrscr();
	sum(int &n);
	getch();
	return 0;
}
void sum(int *x)
{
	int i,sum=0;
	for(i=0;i<=x;i++);
	sum=sum+i;
	printf("%d",sum);
}
