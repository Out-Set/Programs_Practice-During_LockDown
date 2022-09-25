#include<stdio.h>
int main()
{
 int i;
 char s[20];
 FILE *fp;
 fp=fopen("f2.txt","w"):
 if(fp===NULL)
 {
  printf("file not found");
  return(1);
 }
 printf("enter text");
 gets(s);
 for(i=0;i<20;i++)
 {
  fputc(s[i],fp);
 }
 fclose(fp);
 getch();
}
