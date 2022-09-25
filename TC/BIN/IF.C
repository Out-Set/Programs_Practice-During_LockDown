#include<stdio.h>
void main()
{
 int a,b;
 clrscr();
 printf("HELLO");
  if(1<2) //condition is always true
   printf("\nSAWAN");
    getch();
/* output will be HELLO
		  SAWAN  */
 //press enter key after running it to see result of below code

 if(1>2) //condition is always false
  printf("\nBYE");
   getch();
	/* output is nothing due to false condition*/

		/* greatest no b/w a and b */
printf("\nenter two no");
scanf("%d%d",&a,&b);
 if(a>b)
  printf("%d is the greatest",a);
 if(a<b)
  printf("%d is greatest",b);
 getch();
}