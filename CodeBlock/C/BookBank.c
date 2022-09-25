#include<stdio.h>
#include<conio.h>
int main()
{
    int i;
    FILE *fp;
    char str[100];
    fp=fopen("f1.txt","w");
    if(fp==NULL)
    {
        printf("file not found");
        exit(1);
    }
    printf("Write whatever you want: \n");
    gets(str);
    fputs(str,fp);
    fclose(fp);
    getch();
}
