void main()
{
    int i,j,n;
    printf("enter th no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(j>=i||j<=n)
                printf("%d",j);
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}
