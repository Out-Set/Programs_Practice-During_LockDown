#include<stdio.h>
int lwr(char);
int upr(char);
int main()
{
 char ch;
 clrscr();
 printf("enter a character");
 scanf("%ch",&ch);
 lwr(ch);
 puts("char is not alphabetic");
 upr(ch);
 printf("char is non alphabetic");
 getch();
 return(0);
}
int lwr(char ch)
{
 if(ch>=97&&ch<=122)
  puts("char is lwr case");
 else
 return(0);
}
int upr(char ch)
{
 if(ch>=65&&ch<=90)
  puts("char is upr case");
 else
 return(0);
}