//111111111111
//222222222222
//333333333333
//444444444444
//555555555555
void main()
{
    int i,j,n,k;
    printf("enter th no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        k=0+i;//k=(n+1)-i;
        for(j=1;j<=n*2;j++)
        {
            if(j>=i||j<=n)
                printf("%d",k);
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}
