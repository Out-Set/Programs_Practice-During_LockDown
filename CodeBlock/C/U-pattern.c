
#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=7;j++)
        {
            if(j==1||j==7)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=6;j++)
        {
            if(i==5&&(j==2||j==3||j==4))
                printf(" *");
        }
    }
    getch();
}
