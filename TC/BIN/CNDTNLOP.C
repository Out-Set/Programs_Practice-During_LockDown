		   /*  conditional operator-?:  */


/*   1:greatest no b/w two   */
#include<stdio.h>
void main()
{
 int a,b;
 clrscr();
 printf("choice 1:enter the two no");
 scanf("%d%d",&a,&b);
 a>b?printf("%d is greatest",a):printf("%d is greatest",b);
 getch();


/*   2:given no is even or odd   */
 printf("\nchoice 2:enter a no");
 scanf("%d",&a);
 a%2==0?printf("%d is even no",a):printf("%d is odd no",a);
 getch();
}