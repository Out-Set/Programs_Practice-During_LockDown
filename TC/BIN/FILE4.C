#include<stdio.h>
int main()
{
 char s[100];
 FILE *fp;
 clrscr();
 fp=fopen("f1.txt","r");
 if(fp==NULL)
 {
  printf("file not found");
  return(1);
 }
 while(fgets(s,99,fp)!=NULL)
 {
  printf("%s",s);
 }
 fclose(fp);
 getch();
}