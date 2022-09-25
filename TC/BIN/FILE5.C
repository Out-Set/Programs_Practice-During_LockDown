#include<stdio.h>
int main()
{
 char s[100];
 FILE *fp;
 clrscr();
 fp=fopen("f3.txt","w");
 if(fp==NULL)
 {
  printf("file not found");
  return(1);
 }
 printf("enter the text");
 gets(s);
 fputs(s,fp);
 fclose(fp);
}