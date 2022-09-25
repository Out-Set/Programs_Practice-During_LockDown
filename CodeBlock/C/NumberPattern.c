void main()
{
    int i,j,n;
    printf("Enter the no of rows: ");
    scanf("%d",&n);
    int m=(n/2)+1;
    for(i=0;i<n;i++)
    {
        int k=0;
        for(j=0;j<n;j++)
        {
           printf("%d",(m-k));
           if(k<i)
                k++;
           if(j>=n-i+1)
                k--;
        }
        printf("\n");
    }
}
