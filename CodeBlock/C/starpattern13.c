// *********
//  *******
//   *****
//    ***
//     *

main()
{
    int i,j;
    int rows,column;

    printf("enter the no of rows: ");
    scanf("%d",&rows);

    column=2*rows-1;

    for(i=1;i<=rows;i++)
    {
        for(j=1;j<=column;j++)
        {
            if(j>=i && j<=(column+1)-i)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}
