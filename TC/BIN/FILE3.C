#include<stdio.h>
main()
{
 char ch;
 FILE *fp;
 clrscr();
 fp=fopen("f1.txt","rb");
 if(fp==NULL)
 {
  printf("file not found");
  exit(1);
 }
 ch=fgetc(fp);
 while(!feof(fp))
 {
  printf("%ch",ch);
  ch=fgetc(fp);
 }
 fclose(fp);
 getch();
}