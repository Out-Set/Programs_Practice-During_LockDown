#include <stdio.h>
main()
{
	int i,a[5],*p;
	p=&a[0];
	for(i=0;i<5;i++)
	  scanf("%d",p+i);
	for(i=0;i<5;i++)
	  printf("%d\t
	  ",*(p+i));
}
