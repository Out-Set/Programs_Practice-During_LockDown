
void main()
{
    int i,j,k,l;
    for(l=1;l<=5;l++)
    {

    for(i=1;i<=10;i++)
    {
        k=6-i;
        for(j=1;j<=10*2;j++)
        {
            if(j==6-i||j==4+i)
                printf("%d",k);
            else
                printf(" ");
        }

    }

    }
}
