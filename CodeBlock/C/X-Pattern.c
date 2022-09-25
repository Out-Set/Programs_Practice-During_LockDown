void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5;j++)
        {
            if(j==1||j==2||j==4||j==5){
                if(i==j)
                    printf("*");}
            if(j==6-i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}
