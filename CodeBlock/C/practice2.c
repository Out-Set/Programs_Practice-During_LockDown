void main()
{
    int a[]={1,2,1,3,4,5,1,14,3,2,1,3,45,1,13,1};
    int n,index=0;
    printf("enter the no");
    scanf("%d",&n);
    while(index<15)
        if(a[index]==n)
            printf("%d",index);
        index++;
}
