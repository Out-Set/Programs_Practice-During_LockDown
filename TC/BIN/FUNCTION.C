#include<stdio.h>
 int add(int x,int y);
 main()
 {
  int a,b,s;
  clrscr();
  printf("enter the values of a & b");
  scanf("%d%d",&a,&b);
  s=add(a,b);
  printf("%d",s);
  getch();
  return(0);
 }
 int add(int x,int y)
 {
 int s;
  s=x+y;
 }
