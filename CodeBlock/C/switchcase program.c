#include<stdlib.h>
#include<conio.h>
#include<stdio.h>
void main()
{
    int a,b,c,choice;

    while(1)
    {
        clrscr();
        printf("1: Enter 1 For addition");
        printf("2: Enter 2 For substraction");
        printf("3: Enter 3 For multiplication");
        printf("4: Enter 4 For Exit");
        switch(choice)
        {
        case 1:
            printf("enter two no: /n");
            scanf("%d%d",&a,&b);
            c=a+b;
            printf("result is: %d",c);
            break;
        case 2:
            printf("enter two no: /n");
            scanf("%d%d",&a,&b);
            c=a-b;
            printf("result is: %d",c);
            break;

        case 3:
            printf("enter two no: /n");
            scanf("%d%d",&a,&b);
            c=a*b;
            printf("result is: %d",c);
            break;

        case 4: exit(0);

        default:
            printf("invalid chioce");
        }
    }
}
