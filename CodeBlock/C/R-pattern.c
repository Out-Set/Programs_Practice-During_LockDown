#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=3;j++)
        {
            if((i==1||i==3)&&(j>=1||j<=3))
                printf("*");
            if(j==1&&(i==2||i==4||i==5))
                printf("*");
            if((i==2&&j==3)||(i==4&&j==2)||(i==5&&j==3))
                printf(" *");
            else
                printf(" ");

        }
        printf("\n");
    }
    getch();
}



