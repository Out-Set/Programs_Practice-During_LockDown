
#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=7;j++)
        {
            if(j==1||j==5)
                printf(" *");
            else if((i==2)&&(j==2||j==4))
                printf("*");
            else if(i==3&&j==3)
                printf("*");
            else
                printf(" ");

        }
        printf("\n");
    }
    getch();
}



