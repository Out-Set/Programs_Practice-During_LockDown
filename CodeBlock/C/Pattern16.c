void main()
{
    int i,j,n;
    printf("enter the no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
            if(i==j)
                printf("*");
            else if(i+j==n+1)
                printf("#");
            else
                printf(" ");
        printf("\n");
    }
}
