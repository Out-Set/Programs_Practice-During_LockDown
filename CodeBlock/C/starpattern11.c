//       *
//      ***
//     *****
//    *******
//     *****
//      ***
//       *

void main()
{
    int mid,rows;
    int i,j,k;
    k=0;

    printf("enter the no of rows: ");
    scanf("%d",&rows);

    mid=(rows+1)/2;
    for(i=1;i<=rows;i++)
    {
        i<=(rows+1)/2?k++:k--;
        for(j=1;j<=rows;j++)
        {
            if(j>=(mid+1)-k && j<=(mid-1)+k)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}
