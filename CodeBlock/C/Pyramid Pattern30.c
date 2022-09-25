//      0
//     101
//    21012
//   3210123
//  432101234
void main()
{
    int i,j,n,l=0;
    int k;
    printf("enter the no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        k=l;
        for(j=1;j<=n*2-1;j++)
        {

            if(j>=(n+1)-i&&j<=(n-1)+i)
            {
                printf("%d",k);
                j<n?k--:k++;

            }
            else
                printf(" ");
        }
        l++;
        printf("\n");
    }
    getch();
}
