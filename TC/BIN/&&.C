#include<stdio.h>
void main()
   /* for logical && both the statement should be true */
{
 int x=9,y;
 clrscr();
 y=x>6&&x>11; //one statement is true another is false
 printf("\%d",y);
 y=x<7&&x>11; //here both are false
 printf("\n%d",y);
 y=x>8&&x<11; //here both are true
 printf("\n%d",y);
 getch();
}
/* out put will be 0
		   0
		   1  */