
#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=7;j++)
        {
            if(j==1&&(i>=1||i<=5))
                printf("*");
            else if(i==5&&(j>=1||j<=7))
                printf("*");
            else
                printf(" ");

        }
        printf("\n");
    }
    getch();
}



