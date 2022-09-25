#include<stdio.h>
#include<conio.h>
void greatestamongthree(int *x,int *y,int *z);
void main()
{
 int x,y,z;
 clrscr();
 printf("entre the three no\n");
 scanf("%d%d%d",&x,&y,&z);
 greatestamongthree(&x,&y,&z);
 getch();
}
void greatestamongthree(int *a,int *b,int *c)
{
 if(*a>*b&&*a>*c)
  printf("%d is greatest",*a);
 if(*b>*a&&*b>*c)
  printf("%d is grestest",*b);
 if(*c>*a&&*c>*b)
  printf("%d is greatest",*c);
}