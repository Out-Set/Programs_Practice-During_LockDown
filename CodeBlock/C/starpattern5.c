//   *
//  ***
// *****
// *****
//  ***
//   *
main()
{
    int i,j;
    int x,y;
    int m,n;
    printf("enter the no of rows: ");
    scanf("%d",&x);
    printf("enter the no of columns: ");
    scanf("%d",&y);
    m=x+1;
    n=x-1;

    for(i=1;i<=x;i++)
    {
        for(j=1;j<=y;j++)
        {
            if(j>=m-i && j<=n+i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    n=y+1;

    for(i=1;i<=x;i++)
    {
        for(j=1;j<=y;j++)
        {
            if(j>=i && j<=n-i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}
