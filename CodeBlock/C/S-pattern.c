#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=9;j++)
        {
            if(i==1||i==3||i==5&&(j>=1||j<=9))
                printf("*");
            if(i==2&&j==1)
                printf("*");
            if(i==4&&j==9)
                printf("        *");
            else
                printf(" ");

        }
        printf("\n");
    }
    getch();
}


