#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=10;j++)
        {
            if(j==6)
                printf("*");
            if(i==1&&(j>=1||j>=9))
                printf("*");
            else
                printf(" ");

        }
        printf("\n");
    }
    getch();
}

