/* greatest no b/w three no */

#include<stdio.h>
void main()
{
  int a,b,c;
  clrscr();
  printf("enter three no");
  scanf("%d%d%d",&a,&b,&c);;
  if(a>b)
   {
    if(a>c)
     printf("%d is greatest",a);
    else
     printf("%d is greatest",b);
   }
  if(b>c)
   printf("%d is greatest",b);
  else
   printf("%d is greater",c);
  getch();
}