#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5*2-1;j++)
        {
            if(j==6-i||j==4+i)
                printf("*");
            if(i==3&&(j==4||j==5))
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}

