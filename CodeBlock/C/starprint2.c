main()
{
    int i,j,m,n;
    printf("enter the no of rows: ");
    scanf("%d",&m);
    printf("enter a no just one greater than rows: ");
    scanf("%d",&n);
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=m;j++)
        {
            if(j<=n-i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}
