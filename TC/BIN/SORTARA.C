#include<stdio.h>
int main()
{
 int i;
 FILE *fp;
 char s[]="hello students";
 fp=fopen("f1.txt","w");
 if(fp==NULL)
 {
  printf("file can't be opened");
  return(1);
 }
 for(i=0;i<strlen(s);i++)
 {
  fputc(s[i],fp);
 }
 fclose(fp);
 getch();
}