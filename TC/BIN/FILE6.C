#include<stdio.h>
int main()
{
 FILE *fp;
 char s[100];
 clrscr();
 fp=fopen("f1.txt","r");
 if(fp==NULL)
 {
  printf("file not found");
  return(1);
 }
 fscanf(fp,""
}