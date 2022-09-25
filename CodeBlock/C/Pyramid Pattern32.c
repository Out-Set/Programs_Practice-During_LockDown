//      A
//     ABA
//    ABCBA
//   ABCDCBA
//  ABCDEDCBA
void main()
{
    int i,j,n,l=1;
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
                printf("%c",k+64);
                j<n?k++:k--;

            }
            else
                printf(" ");
        }
        //l++;
        printf("\n");
    }
    getch();
}
