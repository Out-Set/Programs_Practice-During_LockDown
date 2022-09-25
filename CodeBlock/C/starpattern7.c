//     *
//    * *
//   * * *
//  * * * *
// * * * * *
main()
{
    int i,j,k;
    int x,y;
    int m,n;
    printf("enter the no of rows: ");
    scanf("%d",&x);
    printf("enter the no of columns: ");
    scanf("%d",&y);
    m=x+1;
    n=x-1;
    k=1;

    for(i=1;i<=x;i++)
    {
        for(j=1;j<=y;j++)
        {
            if(j>=m-i && j<=n+i && k)
                {
                    printf("*");
                    k=0;
                }
            else
                {
                    printf(" ");
                    k=1;
                }
        }
        printf("\n");
    }
}
