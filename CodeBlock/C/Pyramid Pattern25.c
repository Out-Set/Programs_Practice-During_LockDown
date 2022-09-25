//      E
//     DEF
//    CDEFG
//   BCDEFGH
//  ABCDEFGHI
void main()
{
    int i,j,n;
    printf("enter th no of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n*2;j++)
        {
            if(j>=(n+1)-i&&j<=(n-1)+i )
                printf("%c",j+64);       //printf("*");  anything you want
            else
                printf(" ");
        }
        printf("\n");
    }
    getch();
}
