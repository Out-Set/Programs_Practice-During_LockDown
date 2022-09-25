void main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5*2;j++)
        {
            if(j==6-i||j==4+i)
                printf("%c",64+i);
            else
                printf(" ");
        }
        printf("\n");
    }
}
