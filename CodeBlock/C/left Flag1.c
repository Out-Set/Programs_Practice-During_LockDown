void main()
{
    int i,j,k=0,n;
    printf("enter the no of column");
    scanf("%d",&n);
    for(i=1;i<=n*2-1;i++)
    {
        i<=n?k++:k--;
        for(j=1;j<=n;j++)
        {

            if(j<=k)
                printf("%c",k+64);
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}
